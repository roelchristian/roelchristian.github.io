#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from datetime import date, datetime

try:
    import yaml  # pip install pyyaml
except ImportError:
    print("Missing dependency: PyYAML. Install with: pip install pyyaml", file=sys.stderr)
    raise


# Script location: ROOT/util/script/sort_links.py
# So project root is two levels up from this file (script -> util -> root).
ROOT_DIR: Path = Path(__file__).resolve().parents[2]

# Save as VARIABLE the link dir (the directory containing links.yml)
LINKS_DIR: Path = ROOT_DIR / "_data"
LINKS_FILE: Path = LINKS_DIR / "links.yml"


def _normalize_date(d) -> date | None:
    """Accept YAML-parsed dates (date/datetime) or ISO strings YYYY-MM-DD."""
    if d is None:
        return None
    if isinstance(d, datetime):
        return d.date()
    if isinstance(d, date):
        return d
    if isinstance(d, str):
        return date.fromisoformat(d.strip())
    raise TypeError(f"Unsupported date type: {type(d)}")


def _iso_date_or_none(d) -> str | None:
    nd = _normalize_date(d)
    return nd.isoformat() if nd else None


def main() -> int:
    if not LINKS_FILE.exists() or not LINKS_FILE.is_file():
        print(f"ERROR: Expected file does not exist: {LINKS_FILE}", file=sys.stderr)
        return 2

    with LINKS_FILE.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict):
        print("ERROR: links.yml root must be a mapping (dict).", file=sys.stderr)
        return 3

    links = data.get("links", [])
    if links is None:
        links = []
    if not isinstance(links, list):
        print("ERROR: 'links' must be a list.", file=sys.stderr)
        return 4

    def sort_key(item: dict):
        # Missing/invalid dates go last; ties broken by URL.
        d = None
        try:
            d = _normalize_date(item.get("date"))
        except Exception:
            d = None
        return (d is None, d or date.max, str(item.get("url", "")))

    # Sort in place (ascending date)
    links_sorted = sorted(
        (x for x in links if isinstance(x, dict)),
        key=sort_key
    )

    # Normalize date values back to ISO strings for stable YAML output
    for item in links_sorted:
        if "date" in item:
            item["date"] = _iso_date_or_none(item.get("date"))

    data["links"] = links_sorted

    yaml_text = yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=120
    )

    # Overwrite existing file only
    with LINKS_FILE.open("w", encoding="utf-8") as f:
        f.write(yaml_text)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
