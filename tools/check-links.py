#!/usr/bin/env python3
"""Validate internal links across the Fish Disease Library vault.

Checks every .md file under "Fish Disease Library/" for:
  - unresolved [[wikilinks]] and ![[embeds]] (with optional |alias or #heading)
  - wikilinks that only resolve by case (case-mismatch warning)
  - obsidian://open ... URIs (break on the published site)
  - hardcoded https://fishdiseases.manolinaqua.com links (should be wikilinks)

Exit code is non-zero if any hard error (unresolved link, obsidian:// URI,
hardcoded site link) is found. Case-mismatch warnings do not fail the build.
"""
import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent / "Fish Disease Library"

WIKILINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
OBSIDIAN_URI_RE = re.compile(r"obsidian://open\?[^\s)]+")
SITE_URL_RE = re.compile(r"https://fishdiseases\.manolinaqua\.com/\S*")


def build_file_index(vault: Path) -> dict[str, Path]:
    """Map every name a wikilink could use to the file it resolves to.

    Obsidian resolves [[Name]] by bare filename (no extension) for notes,
    and by full filename (with extension) for other files like images. It
    also accepts a partial vault-relative path ending in either form.
    """
    index: dict[str, Path] = {}
    for path in vault.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(vault)
        for name in {path.name, path.stem, str(rel), str(rel.with_suffix(""))}:
            index[name] = path
    return index


def main() -> int:
    if not VAULT.is_dir():
        print(f"Vault not found: {VAULT}", file=sys.stderr)
        return 2

    index = build_file_index(VAULT)
    lower_index = {name.lower(): name for name in index}

    errors: list[str] = []
    warnings: list[str] = []

    for md_file in sorted(VAULT.rglob("*.md")):
        rel = md_file.relative_to(VAULT.parent)
        text = md_file.read_text(encoding="utf-8")

        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if target in index:
                continue
            if target.lower() in lower_index:
                warnings.append(
                    f"{rel}: case-mismatch wikilink [[{target}]] "
                    f"(actual: {lower_index[target.lower()]})"
                )
                continue
            errors.append(f"{rel}: unresolved wikilink [[{target}]]")

        for m in OBSIDIAN_URI_RE.finditer(text):
            errors.append(f"{rel}: obsidian:// URI breaks on published site: {m.group(0)}")

        for m in SITE_URL_RE.finditer(text):
            errors.append(f"{rel}: hardcoded site URL (use a wikilink instead): {m.group(0)}")

    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")

    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
