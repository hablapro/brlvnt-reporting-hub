#!/usr/bin/env bash
# Scaffold a reporting month. Run from the repo root.
#
#   ./scripts/new_month.sh ggmi 2026-08
#   ./scripts/new_month.sh gcg  2026-08
#
# Creates reports/forex/<entity>/<YYYY-MM>/{data/sources,qa,model,output} and
# drops in the figures.json, qa-and-model.md and BUILD-STATUS.md stubs. Safe
# to re-run: it never overwrites a file that already exists.
set -euo pipefail

entity="${1:-}"
month="${2:-}"
if [[ ! "$entity" =~ ^(ggmi|gcg)$ ]] || [[ ! "$month" =~ ^[0-9]{4}-[0-9]{2}$ ]]; then
  echo "usage: $0 <ggmi|gcg> <YYYY-MM>" >&2
  exit 2
fi

root="reports/forex/$entity/$month"
tpl="templates/month"
[[ -d "$tpl" ]] || { echo "run this from the repo root ($tpl not found)" >&2; exit 2; }

case "$entity" in
  ggmi) label="GGMI (LATAM)" ;;
  gcg)  label="GCG (US Hispanic)" ;;
esac
pretty="$(python3 -c "import datetime,sys;print(datetime.date(*map(int,sys.argv[1].split('-')),1).strftime('%B %Y'))" "$month")"

mkdir -p "$root"/{data/sources,qa,model,output}
for d in data/sources qa model output; do
  [[ -e "$root/$d/.gitkeep" ]] || touch "$root/$d/.gitkeep"
done

for f in figures.json qa-and-model.md BUILD-STATUS.md; do
  src="$tpl/$f"
  case "$f" in
    figures.json)     dst="$root/figures.json" ;;
    qa-and-model.md)  dst="$root/qa/qa-and-model.md" ;;
    BUILD-STATUS.md)  dst="$root/BUILD-STATUS.md" ;;
  esac
  if [[ -e "$dst" ]]; then
    echo "  skip (exists)  $dst"
    continue
  fi
  sed -e "s/{{ENTITY_LABEL}}/$label/g" \
      -e "s/{{ENTITY}}/$entity/g" \
      -e "s/{{MONTH}}/$month/g" \
      -e "s/{{MONTH_PRETTY}}/$pretty/g" "$src" > "$dst"
  echo "  created        $dst"
done

echo
echo "Scaffolded $label $pretty at $root"
echo "Next: docs/RUNBOOK.md phase 0 (kickoff inputs). Do not pull data before"
echo "the two standing questions are answered: what does the client already"
echo "hold, and how is the agency scored."
