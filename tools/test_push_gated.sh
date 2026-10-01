#!/usr/bin/env bash
# test_push_gated.sh -- THE TEST OF push_gated.sh's TAG INSTRUMENT, (R178)(3), written at b568.
#
# usage: bash tools/test_push_gated.sh
#
# Every case runs the script against THROWAWAY repositories made under a fresh `mktemp -d` (left for the OS; this test
# deletes nothing): a bare "origin" and a clone of it. No network remote is touched and no hook or switch is added to
# the script for the test -- a mismatch is made the way a real one would arise, by the remote's own post-receive hook
# moving its main after the push, so the script's ls-remote read-back differs from the tip it pushed.
#   A  equal read-back           -> exit 0; the tag made locally at the read-back SHA, pushed, peeled equal at the remote
#   B  read-back made to MISMATCH -> exit 4; NO tag made locally, NONE at the remote          ((R178)(3)'s named case)
#   C  main push refused          -> exit 3; NO tag made locally, NONE at the remote
#   D  tag made by hand first     -> exit 7; nothing pushed (the remote main unmoved)
#   E  a branch not push-*        -> exit 2
#   F  NAME::MESSAGE              -> exit 0; the tag's message is MESSAGE
#   G-I (R179)(5) the table check over a clone named PLACE-papers (see the cases below)
set -uo pipefail

SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/push_gated.sh"
W=$(mktemp -d) || exit 9
echo "test_push_gated: script $SCRIPT ; sha256 $(sha256sum "$SCRIPT" | cut -c1-16) ; scratch $W"
G() { git -c user.name=t -c user.email=t@invalid -c init.defaultBranch=main "$@"; }

mk() {   # mk <case> -> makes $W/<case>/origin.git (bare, main at base) and $W/<case>/work (main at base, push-t at a child)
  local c="$W/$1"
  mkdir -p "$c" && G init -q --bare "$c/origin.git" && G clone -q "$c/origin.git" "$c/work" 2>/dev/null &&
  G -C "$c/work" commit -q --allow-empty -m base && G -C "$c/work" push -q origin main 2>/dev/null &&
  G -C "$c/work" checkout -q -b push-t && G -C "$c/work" commit -q --allow-empty -m child && G -C "$c/work" checkout -q main
}

pass=0; total=0
check() {   # check <label> <wanted> <got>
  total=$((total + 1))
  if [ "$2" = "$3" ]; then pass=$((pass + 1)); echo "  $1 : wanted $2 ; got $3 ; PASS"; else echo "  $1 : wanted $2 ; got $3 ; ### FAIL"; fi
}
has_local_tag() { git -C "$1/work" rev-parse -q --verify "refs/tags/$2" >/dev/null && echo yes || echo no; }
has_remote_tag() { [ -n "$(git -C "$1/work" ls-remote origin "refs/tags/$2")" ] && echo yes || echo no; }

echo "### CASE A -- equal read-back"
mk A; c="$W/A"
bash "$SCRIPT" "$c/work" push-t vT >"$c/out.txt" 2>&1; rc=$?
check "A exit" 0 "$rc"
check "A tag made locally" yes "$(has_local_tag "$c" vT)"
check "A tag peeled = pushed tip" "$(git -C "$c/work" rev-parse push-t)" "$(git -C "$c/work" ls-remote origin 'refs/tags/vT^{}' | cut -f1)"
check "A tag made after the read-back line" yes "$(awk '/main read back at the remote/{r=NR} /tag vT made at the read-back/{t=NR} END{print (r && t && r < t) ? "yes" : "no"}' "$c/out.txt")"

echo "### CASE B -- the read-back made to MISMATCH (the remote's post-receive hook moves main back to base)"
mk B; c="$W/B"
base=$(git -C "$c/work" rev-parse main)
printf '#!/bin/sh\ngit update-ref refs/heads/main %s\n' "$base" >"$c/origin.git/hooks/post-receive"; chmod +x "$c/origin.git/hooks/post-receive"
bash "$SCRIPT" "$c/work" push-t vT >"$c/out.txt" 2>&1; rc=$?
check "B exit" 4 "$rc"
check "B the script printed the unequal read-back" yes "$(grep -q 'MAIN READ-BACK UNEQUAL' "$c/out.txt" && echo yes || echo no)"
check "B NO tag made locally" no "$(has_local_tag "$c" vT)"
check "B NO tag at the remote" no "$(has_remote_tag "$c" vT)"

echo "### CASE C -- the main push refused (the remote's pre-receive hook exits 1)"
mk C; c="$W/C"
printf '#!/bin/sh\nexit 1\n' >"$c/origin.git/hooks/pre-receive"; chmod +x "$c/origin.git/hooks/pre-receive"
bash "$SCRIPT" "$c/work" push-t vT >"$c/out.txt" 2>&1; rc=$?
check "C exit" 3 "$rc"
check "C NO tag made locally" no "$(has_local_tag "$c" vT)"
check "C NO tag at the remote" no "$(has_remote_tag "$c" vT)"

echo "### CASE D -- a tag made by hand before the run"
mk D; c="$W/D"
G -C "$c/work" tag -a vT -m hand push-t
before=$(git -C "$c/work" ls-remote origin refs/heads/main | cut -f1)
bash "$SCRIPT" "$c/work" push-t vT >"$c/out.txt" 2>&1; rc=$?
check "D exit" 7 "$rc"
check "D remote main unmoved" "$before" "$(git -C "$c/work" ls-remote origin refs/heads/main | cut -f1)"
check "D NO tag at the remote" no "$(has_remote_tag "$c" vT)"

echo "### CASE E -- a branch not push-* or repair-*"
mk E; c="$W/E"
G -C "$c/work" branch other push-t
bash "$SCRIPT" "$c/work" other vT >"$c/out.txt" 2>&1; rc=$?
check "E exit" 2 "$rc"
check "E NO tag made locally" no "$(has_local_tag "$c" vT)"

echo "### CASE F -- NAME::MESSAGE"
mk F; c="$W/F"
bash "$SCRIPT" "$c/work" push-t "vT::v0 -- the test's message" >"$c/out.txt" 2>&1; rc=$?
check "F exit" 0 "$rc"
check "F the tag's message" "v0 -- the test's message" "$(git -C "$c/work" tag -l --format='%(contents:subject)' vT)"

# ### (R179)(5), b569: THE TABLE CHECK. The work clone is named PLACE-papers, so push_gated.sh calls relay tools/table_gate.py
# ### before the main push; TABLE_GATE_ARGS gives it fixture tables and a fixture face (the seam only adds arguments).
#   G  the grade cells unchanged              -> exit 0; main pushed
#   H  a grade cell MUTATED (R / b moved)     -> exit 9; the remote main unmoved, the checkout restored
#   I  the same mutation NAMED on the face    -> exit 0; main pushed
mkpp() {   # mkpp <case> -> like mk, the work clone named PLACE-papers
  local c="$W/$1"
  mkdir -p "$c" && G init -q --bare "$c/origin.git" && G clone -q "$c/origin.git" "$c/PLACE-papers" 2>/dev/null &&
  G -C "$c/PLACE-papers" commit -q --allow-empty -m base && G -C "$c/PLACE-papers" push -q origin main 2>/dev/null &&
  G -C "$c/PLACE-papers" checkout -q -b push-t && G -C "$c/PLACE-papers" commit -q --allow-empty -m child &&
  G -C "$c/PLACE-papers" checkout -q main
  printf '{"rows": [{"repo": "R", "name": "a", "grade": "DERIVES"}, {"repo": "R", "name": "b", "grade": "ENCODES-CONCLUSION"}]}\n' >"$c/prior.json"
  printf '{"rows": [{"repo": "R", "name": "a", "grade": "DERIVES"}, {"repo": "R", "name": "b", "grade": "ENCODES-CONCLUSION"}]}\n' >"$c/same.json"
  printf '{"rows": [{"repo": "R", "name": "a", "grade": "DERIVES"}, {"repo": "R", "name": "b", "grade": "CONFLICT"}]}\n' >"$c/mut.json"
  printf '### a face naming no cell\n' >"$c/face_none.txt"
  printf '### a face naming the cell\n### TABLE CELL: R / b\n' >"$c/face_named.txt"
}
for cs in G H I; do
  mkpp "$cs"; c="$W/$cs"
  case "$cs" in
    G) args="--prior $c/prior.json --now $c/same.json --face $c/face_none.txt"; want=0;;
    H) args="--prior $c/prior.json --now $c/mut.json --face $c/face_none.txt"; want=9;;
    I) args="--prior $c/prior.json --now $c/mut.json --face $c/face_named.txt"; want=0;;
  esac
  echo "### CASE $cs -- the table check ($args)"
  before=$(git -C "$c/PLACE-papers" ls-remote origin refs/heads/main | cut -f1)
  TABLE_GATE_ARGS="$args" bash "$SCRIPT" "$c/PLACE-papers" push-t >"$c/out.txt" 2>&1; rc=$?
  check "$cs exit" "$want" "$rc"
  check "$cs the table check ran before the push" yes "$(grep -q '^table_gate: face ' "$c/out.txt" && echo yes || echo no)"
  if [ "$want" -eq 9 ]; then
    check "$cs remote main unmoved" "$before" "$(git -C "$c/PLACE-papers" ls-remote origin refs/heads/main | cut -f1)"
    check "$cs the moved cell printed" yes "$(grep -q 'R / b : ENCODES-CONCLUSION -> CONFLICT' "$c/out.txt" && echo yes || echo no)"
    check "$cs checkout restored" main "$(git -C "$c/PLACE-papers" symbolic-ref --short HEAD)"
  else
    check "$cs remote main = pushed tip" "$(git -C "$c/PLACE-papers" rev-parse push-t)" "$(git -C "$c/PLACE-papers" ls-remote origin refs/heads/main | cut -f1)"
  fi
done

echo "### ### **$pass of $total checks as wanted -- $([ "$pass" -eq "$total" ] && echo PASS || echo FAIL)**"
[ "$pass" -eq "$total" ]
