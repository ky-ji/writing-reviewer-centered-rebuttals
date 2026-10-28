#!/usr/bin/env python3
"""Report cross-review presentation inconsistencies in a rebuttal draft.

Compare reviewer sections for shared terminology, numeric notation, structure,
openings, and closings. Use the observations to guide a side-by-side read.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


DEFAULT_SECTION_PATTERN = (
    r"^(?P<marks>#{1,6})\s+"
    r"(?P<label>(?:R\d+\b.*|Reviewer\b.*|AC\b.*|Area Chair\b.*|"
    r"Meta[- ]Review\b.*|Response to the (?:Area Chair|Meta[- ]Review).*))$"
)

BOUNDARY_RE = re.compile(
    r"^\s*(?:#{1,6}\s+|\*\*(?:W|Q|A)\d+(?:\s+and\s+(?:W|Q)\d+)?[.,:]?)",
    re.IGNORECASE,
)
ANSWER_START_RE = re.compile(r"^\s*\*\*A\d+[.,:]?", re.IGNORECASE)
ITEM_START_RE = re.compile(r"^\s*\*\*(?:W|Q|A)\d+", re.IGNORECASE)
LABEL_ONLY_RE = re.compile(r"^\s*\*\*A\d+[.,:]?\*\*", re.IGNORECASE)
FULL_OPENING_RE = re.compile(r"^\s*\*\*A\d+[.,:]?\s+.+?\*\*", re.IGNORECASE)
GRATITUDE_RE = re.compile(
    r"\b(?:we\s+thank|we\s+appreciate|we\s+are\s+grateful|thank\s+you|"
    r"grateful|sincerely\s+appreciate|invaluable)\b",
    re.IGNORECASE,
)
DECIMAL_RE = re.compile(r"(?<![\w.])(?P<sign>[+-]?)(?P<value>\d+\.\d+)")
UNIT_RE = re.compile(
    r"^\s*(?P<unit>%|percentage\s+points?|points?|pp)(?!\w)",
    re.IGNORECASE,
)

REFERENCE_FAMILIES = {
    "figure reference": {
        "Fig.": re.compile(r"\bFig\.", re.IGNORECASE),
        "Figure": re.compile(r"\bFigure\b", re.IGNORECASE),
    },
    "table reference": {
        "Tab.": re.compile(r"\bTab\.", re.IGNORECASE),
        "Table": re.compile(r"\bTable\b", re.IGNORECASE),
    },
    "section reference": {
        "Sec.": re.compile(r"\bSec\.", re.IGNORECASE),
        "Section": re.compile(r"\bSection\b", re.IGNORECASE),
    },
    "difference unit": {
        "percentage point(s)": re.compile(r"\bpercentage\s+points?\b", re.IGNORECASE),
        "point(s)": re.compile(r"(?<!percentage\s)\bpoints?\b", re.IGNORECASE),
        "pp": re.compile(r"\bpp\b", re.IGNORECASE),
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Compare reviewer sections for terminology, numeric notation, "
            "structure, opening warmth, and closing rhythm."
        )
    )
    parser.add_argument("draft", type=Path, help="Markdown rebuttal draft")
    parser.add_argument(
        "--section-pattern",
        default=DEFAULT_SECTION_PATTERN,
        help="Multiline regex for reviewer headings; named groups label/marks are optional.",
    )
    parser.add_argument(
        "--term-group",
        action="append",
        default=[],
        metavar="LABEL=TERM1|TERM2",
        help=(
            "Optional project-specific aliases to compare. Repeat for multiple concepts, "
            "for example 'baseline=Method A|Baseline A'."
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser.parse_args()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def clean_markdown(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[*_#>]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def reviewer_key(label: str) -> str:
    match = re.match(r"R\d+", label, re.IGNORECASE)
    if match:
        return match.group(0).upper()
    if re.search(r"meta|area chair|\bAC\b", label, re.IGNORECASE):
        return "AC"
    return label.strip()


def split_sections(text: str, pattern: str) -> list[dict[str, Any]]:
    regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
    matches = list(regex.finditer(text))
    sections: list[dict[str, Any]] = []
    for index, match in enumerate(matches):
        label = match.groupdict().get("label") or match.group(0).lstrip("#").strip()
        key = reviewer_key(label)
        if not (re.fullmatch(r"R\d+", key) or key == "AC"):
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        marks = match.groupdict().get("marks") or re.match(r"#+", match.group(0)).group(0)
        sections.append(
            {
                "label": label.strip(),
                "key": key,
                "line": line_number(text, match.start()),
                "heading_depth": len(marks),
                "text": text[match.end() : end].strip(),
            }
        )
    return sections


def reviewer_opening(section_text: str) -> str:
    lines: list[str] = []
    for line in section_text.splitlines():
        if BOUNDARY_RE.match(line):
            break
        if line.strip():
            lines.append(line.strip())
    return clean_markdown(" ".join(lines))


def answer_units(section_text: str, section_line: int) -> list[dict[str, Any]]:
    lines = section_text.splitlines()
    units: list[dict[str, Any]] = []
    starts = [index for index, line in enumerate(lines) if ANSWER_START_RE.match(line)]
    for start in starts:
        end = len(lines)
        for index in range(start + 1, len(lines)):
            if ITEM_START_RE.match(lines[index]) or re.match(r"^#{1,6}\s+", lines[index]):
                end = index
                break
        unit_lines = lines[start:end]
        while unit_lines and (
            not unit_lines[-1].strip()
            or re.fullmatch(r"\s*(?:-{3,}|_{3,}|\*{3,})\s*", unit_lines[-1])
        ):
            unit_lines.pop()
        raw = "\n".join(unit_lines).strip()
        prose = clean_markdown(raw)
        prose = re.sub(r"^A\d+[.,:]?\s*", "", prose, flags=re.IGNORECASE)
        paragraphs = [
            clean_markdown(paragraph)
            for paragraph in re.split(r"\n\s*\n", raw)
            if clean_markdown(paragraph)
        ]
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", prose) if s.strip()]
        style = "other"
        if LABEL_ONLY_RE.match(lines[start]):
            style = "label_only_bold"
        elif FULL_OPENING_RE.match(lines[start]):
            style = "full_opening_bold"
        units.append(
            {
                "line": section_line + start + 1,
                "style": style,
                "opening": sentences[0][:240] if sentences else prose[:240],
                "closing": sentences[-1][:240] if sentences else prose[-240:],
                "we_will_closing": bool(
                    paragraphs and re.search(r"\bwe\s+will\b", paragraphs[-1], re.IGNORECASE)
                ),
            }
        )
    return units


def parse_term_groups(raw_groups: list[str]) -> dict[str, dict[str, re.Pattern[str]]]:
    groups: dict[str, dict[str, re.Pattern[str]]] = {}
    for raw in raw_groups:
        if "=" not in raw:
            raise ValueError(f"invalid --term-group {raw!r}; expected LABEL=TERM1|TERM2")
        label, variants_text = raw.split("=", 1)
        variants = [item.strip() for item in variants_text.split("|") if item.strip()]
        if not label.strip() or len(variants) < 2:
            raise ValueError(f"invalid --term-group {raw!r}; provide a label and at least two terms")
        groups[label.strip()] = {
            variant: re.compile(rf"(?<!\w){re.escape(variant)}(?!\w)", re.IGNORECASE)
            for variant in variants
        }
    return groups


def variant_observations(
    sections: list[dict[str, Any]], families: dict[str, dict[str, re.Pattern[str]]]
) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    for label, variants in families.items():
        used: dict[str, list[dict[str, Any]]] = defaultdict(list)
        reviewers: set[str] = set()
        for section in sections:
            candidates: list[tuple[int, int, str]] = []
            for variant, pattern in variants.items():
                candidates.extend(
                    (match.start(), match.end(), variant)
                    for match in pattern.finditer(section["text"])
                )
            occupied: list[tuple[int, int]] = []
            for start, end, variant in sorted(
                candidates, key=lambda item: (item[0], -(item[1] - item[0]))
            ):
                if any(start < used_end and end > used_start for used_start, used_end in occupied):
                    continue
                occupied.append((start, end))
                used[variant].append(
                    {
                        "reviewer": section["key"],
                        "line": section["line"]
                        + section["text"].count("\n", 0, start)
                        + 1,
                    }
                )
                reviewers.add(section["key"])
        if len(used) >= 2 and len(reviewers) >= 2:
            observations.append(
                {
                    "type": "variant_family",
                    "category": label,
                    "variants": dict(used),
                    "message": f"Multiple {label} forms appear across reviewer sections.",
                }
            )
    return observations


def numeric_observations(sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    values: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for section in sections:
        for match in DECIMAL_RE.finditer(section["text"]):
            value = match.group("value")
            unit_match = UNIT_RE.match(section["text"][match.end() :])
            unit = unit_match.group("unit").lower() if unit_match else "bare"
            unit = re.sub(r"\s+", " ", unit)
            values[value][unit].append(
                {
                    "reviewer": section["key"],
                    "line": section["line"] + section["text"].count("\n", 0, match.start()) + 1,
                    "signed": bool(match.group("sign")),
                }
            )

    mismatches: list[dict[str, Any]] = []
    for value, units in values.items():
        reviewers = {
            location["reviewer"]
            for locations in units.values()
            for location in locations
        }
        if len(units) >= 2 and len(reviewers) >= 2:
            mismatches.append(
                {
                    "value": value,
                    "variants": dict(units),
                }
            )
    if not mismatches:
        return []
    return [
        {
            "type": "numeric_presentation",
            "examples": mismatches[:6],
            "total_values": len(mismatches),
            "message": (
                f"{len(mismatches)} repeated decimal value(s) use different unit forms "
                "across reviewers; examples are grouped below."
            ),
        }
    ]


def structural_observations(profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    if len({profile["heading_depth"] for profile in profiles}) > 1:
        observations.append(
            {
                "type": "heading_depth",
                "variants": {
                    profile["reviewer"]: profile["heading_depth"] for profile in profiles
                },
                "message": "Reviewer-level heading depths differ.",
            }
        )

    internal_headings = {
        profile["reviewer"]: profile["internal_headings"] for profile in profiles
    }
    if any(internal_headings.values()) and len(
        {tuple(headings) for headings in internal_headings.values()}
    ) > 1:
        observations.append(
            {
                "type": "internal_heading_style",
                "variants": internal_headings,
                "message": "Standalone internal heading styles differ across reviewer sections.",
            }
        )

    style_sets = {
        profile["reviewer"]: sorted(
            {answer["style"] for answer in profile["answers"] if answer["style"] != "other"}
        )
        for profile in profiles
    }
    if len({tuple(styles) for styles in style_sets.values()}) > 1 or any(
        len(styles) > 1 for styles in style_sets.values()
    ):
        observations.append(
            {
                "type": "answer_bolding",
                "variants": style_sets,
                "message": "Answer-opening bolding conventions differ across reviewer sections.",
            }
        )

    gratitude = {profile["reviewer"]: profile["opening_gratitude_count"] for profile in profiles}
    opening_words = {profile["reviewer"]: profile["opening_words"] for profile in profiles}
    if gratitude and max(gratitude.values()) - min(gratitude.values()) >= 2:
        observations.append(
            {
                "type": "opening_warmth",
                "variants": gratitude,
                "opening_words": opening_words,
                "message": "Reviewer-level openings have noticeably different gratitude density.",
            }
        )

    revision_rates: dict[str, dict[str, int]] = {}
    for profile in profiles:
        total = len(profile["answers"])
        revision = sum(
            1 for answer in profile["answers"] if answer["we_will_closing"]
        )
        revision_rates[profile["reviewer"]] = {"we_will_closings": revision, "answers": total}
    if len(profiles) >= 2:
        rates = [item["we_will_closings"] / item["answers"] for item in revision_rates.values() if item["answers"]]
        if rates and max(rates) - min(rates) >= 0.6:
            observations.append(
                {
                    "type": "closing_rhythm",
                    "variants": revision_rates,
                    "message": "Use of 'We will...' answer closings is uneven across reviewers.",
                }
            )
    return observations


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    text = args.draft.read_text(encoding="utf-8")
    sections = split_sections(text, args.section_pattern)
    if len(sections) < 2:
        return {
            "draft": str(args.draft),
            "scope": "cross-review consistency only",
            "profiles": [],
            "observations": [],
            "note": "Fewer than two reviewer sections were detected; no cross-review comparison was run.",
        }

    profiles: list[dict[str, Any]] = []
    for section in sections:
        answers = answer_units(section["text"], section["line"])
        opening = reviewer_opening(section["text"])
        profiles.append(
            {
                "reviewer": section["key"],
                "label": section["label"],
                "line": section["line"],
                "characters": len(section["text"]),
                "heading_depth": section["heading_depth"],
                "opening": opening[:300],
                "opening_words": len(opening.split()),
                "opening_gratitude_count": len(GRATITUDE_RE.findall(opening)),
                "w_labels": len(re.findall(r"^\s*\*\*W\d+", section["text"], re.MULTILINE | re.IGNORECASE)),
                "q_labels": len(re.findall(r"^\s*\*\*Q\d+", section["text"], re.MULTILINE | re.IGNORECASE)),
                "internal_headings": [
                    clean_markdown(match.group(0))
                    for match in re.finditer(r"^#{2,6}\s+.+$", section["text"], re.MULTILINE)
                ],
                "answers": answers,
            }
        )

    term_groups = parse_term_groups(args.term_group)
    observations: list[dict[str, Any]] = []
    observations.extend(variant_observations(sections, REFERENCE_FAMILIES))
    observations.extend(variant_observations(sections, term_groups))
    observations.extend(numeric_observations(sections))
    observations.extend(structural_observations(profiles))

    return {
        "draft": str(args.draft),
        "scope": "cross-review consistency only",
        "profiles": profiles,
        "observations": observations,
        "note": "Compare flagged presentation patterns in context before editing.",
    }


def format_location(location: dict[str, Any]) -> str:
    return f"{location['reviewer']} line {location['line']}"


def print_text(report: dict[str, Any]) -> None:
    print("Cross-review consistency scan (advisory)")
    print(f"Draft: {report['draft']}")
    if report["profiles"]:
        labels = ", ".join(profile["reviewer"] for profile in report["profiles"])
        print(f"Compared: {labels}")
    print()

    observations = report["observations"]
    if not observations:
        print("No automated cross-review mismatch was detected in the checked dimensions.")
    else:
        print("Observations:")
        for item in observations:
            print(f"- [{item['type']}] {item['message']}")
            if item["type"] == "numeric_presentation":
                for example in item.get("examples", []):
                    forms: list[str] = []
                    for variant, locations in example["variants"].items():
                        where = ", ".join(
                            format_location(location) for location in locations[:3]
                        )
                        forms.append(f"{variant} ({where})")
                    print(f"  {example['value']}: " + "; ".join(forms))
                remaining = item.get("total_values", 0) - len(item.get("examples", []))
                if remaining > 0:
                    print(f"  ... and {remaining} more repeated value(s)")
                continue
            variants = item.get("variants", {})
            for variant, locations in variants.items():
                if isinstance(locations, list) and locations and isinstance(locations[0], dict):
                    where = ", ".join(format_location(location) for location in locations[:6])
                    print(f"  {variant}: {where}")
                else:
                    print(f"  {variant}: {locations}")
    print()
    print(report["note"])


def main() -> int:
    args = parse_args()
    try:
        report = build_report(args)
    except (OSError, re.error, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print_text(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
