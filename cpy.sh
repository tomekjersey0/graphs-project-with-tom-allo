#!/usr/bin/env bash
# dump_dir.sh — recursively copy directory contents with filename tags
#
# Usage: ./dump_dir.sh [options] <source_dir> [output_file]
#
# Options:
#   -i <pattern>   Ignore files/dirs matching this name or glob (repeatable)
#   -h             Show this help
#
# Examples:
#   ./dump_dir.sh ./my-project
#   ./dump_dir.sh ./my-project output.txt
#   ./dump_dir.sh -i node_modules -i .git ./my-project
#   ./dump_dir.sh -i "*.log" -i "__pycache__" -i ".env" ./my-project out.txt

set -euo pipefail

usage() {
  sed -n '/^# Usage:/,/^[^#]/{ /^#/{ s/^# \?//; p } }' "$0"
  exit 0
}

IGNORE_PATTERNS=()

while getopts ":i:h" opt; do
  case $opt in
    i) IGNORE_PATTERNS+=("$OPTARG") ;;
    h) usage ;;
    :) echo "Error: -$OPTARG requires an argument." >&2; exit 1 ;;
    \?) echo "Error: Unknown option -$OPTARG" >&2; exit 1 ;;
  esac
done
shift $((OPTIND - 1))

SOURCE_DIR="${1:?Usage: $0 [-i pattern] ... <source_dir> [output_file]}"
OUTPUT_FILE="${2:-}"

SOURCE_DIR="$(realpath "$SOURCE_DIR")"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Error: '$SOURCE_DIR' is not a directory." >&2
  exit 1
fi

# Build find arguments for ignore patterns.
# Each pattern prunes matching dirs and skips matching files.
build_find_args() {
  local args=()
  for pattern in "${IGNORE_PATTERNS[@]}"; do
    args+=( \( -name "$pattern" -prune \) -o )
  done
  # After all prunes, match only regular files and print0
  args+=( -type f -print0 )
  printf '%s\0' "${args[@]}"
}

dump() {
  local find_args=()
  while IFS= read -r -d '' arg; do
    find_args+=("$arg")
  done < <(build_find_args)

  while IFS= read -r -d '' filepath; do
    relative="${filepath#"$SOURCE_DIR"/}"
    echo "<file name=\"$relative\">"
    cat "$filepath"
    echo
    echo "</file>"
  done < <(find "$SOURCE_DIR" "${find_args[@]}" | sort -z)
}

if [[ -n "$OUTPUT_FILE" ]]; then
  dump > "$OUTPUT_FILE"
  echo "Written to: $OUTPUT_FILE" >&2
else
  dump
fi