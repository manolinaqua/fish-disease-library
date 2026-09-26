#!/usr/bin/env bash
# Apply the chapter renames listed in tools/rename-map.tsv.
#
# For every row with a real target path (not "(unchanged...)", "(delete...)",
# "(split...)" or "(merge...)"), this does `git mv` and then rewrites every
# `[[Old Name]]` / `[[Old Name|alias]]` wikilink across the vault to the new
# name, preserving any `|alias` suffix.
#
# Rows marked (delete ...), (split ...) or "MERGE" are content decisions that
# need a human editorial pass first — this script skips them and prints a
# reminder instead of guessing.
#
# Usage: tools/apply-renames.sh [--dry-run]

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAP_FILE="$REPO_ROOT/tools/rename-map.tsv"
DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

cd "$REPO_ROOT"

tail -n +2 "$MAP_FILE" | while IFS=$'\t' read -r current proposed notes; do
    [[ -z "$current" ]] && continue

    if [[ "$proposed" == "(unchanged"* || "$proposed" == "(delete"* || "$proposed" == "(split"* || "$proposed" == "MERGE"* ]]; then
        echo "SKIP (needs editorial decision): $current -> $proposed"
        continue
    fi

    if [[ ! -f "$current" ]]; then
        echo "WARN: source not found, skipping: $current" >&2
        continue
    fi

    old_stem="$(basename "$current" .md)"
    new_stem="$(basename "$proposed" .md)"

    echo "RENAME: $current -> $proposed"
    if ! $DRY_RUN; then
        mkdir -p "$(dirname "$proposed")"
        git mv "$current" "$proposed"
    fi

    # Rewrite [[Old Stem]] and [[Old Stem|alias]] everywhere, preserving alias.
    if ! $DRY_RUN; then
        find "$REPO_ROOT/Fish Disease Library" -name '*.md' -print0 |
            xargs -0 sed -i '' \
                -e "s/\[\[${old_stem//\//\\/}\]\]/[[${new_stem//\//\\/}]]/g" \
                -e "s/\[\[${old_stem//\//\\/}|/[[${new_stem//\//\\/}|/g"
    fi
done

echo
echo "Done. Rows marked SKIP need a manual merge/split/delete pass — see the notes column in tools/rename-map.tsv."
echo "Run 'python3 tools/check-links.py' afterwards to confirm no links broke."
