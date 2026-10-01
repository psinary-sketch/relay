#!/usr/bin/env bash
# push_gated.sh -- THE PUSH DISCIPLINE, (R171)(2), written at b561.
#
# usage: push_gated.sh <repo> <push-branch> [tag[::message] ...]
#
# b560's defect (e): a chained command piped `git push origin main` through `tail`; the pre-push hook refused the push,
# the pipe returned tail's status, and the chain went on to push the tag, so the remote carried a tag peeled to a commit
# its main did not hold. The standing rule from (R171)(2):
#   (1) this script runs with pipefail (and -e, -u); no push's status passes through a pipe;
#   (2) main is pushed from <push-branch> (the hook, Rule 4.10, reads the CHECKED-OUT branch, so the branch is checked
#       out for the push and the checkout restored after) and READ BACK by ls-remote, equal to <push-branch>'s tip;
#   (3) only then is each tag pushed, and each tag's peeled SHA read back at the remote equal to its local peel.
# A refused push, an unequal read-back, or a failed tag push exits non-zero at once, and no later push runs.
# Exit codes: 0 all pushed and read back; 2 usage; 3 main push refused; 4 main read-back unequal; 5 a tag push refused;
# 6 a tag read-back unequal; 7 a tag argument refused before any push (the tag already exists, locally or at the
# remote); 8 the tag could not be made; 9 (R179)(5) the table check refused a PLACE-papers push. The script prints one
# line per step; it deletes nothing.
#
# ### THE TAG IS MADE HERE, (R178)(3), b567's defect (g): the seat made the annotated tag v0.10 by hand before main was
# ### read back. From b568 the script MAKES every tag it is given -- annotated, at the SHA it has just read back at the
# ### remote, after that SHA has been compared equal to the local tip IN THIS RUN -- and refuses a tag argument whose
# ### name already exists locally or at the remote, before anything is pushed. A tag argument is NAME or NAME::MESSAGE;
# ### without a message the tag's message is "NAME -- made by push_gated.sh after main read back at <sha>". The seat
# ### no longer runs `git tag` by hand for a kernel tag. The test is relay tools/test_push_gated.sh.
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "push_gated: usage: push_gated.sh <repo> <push-branch> [tag[::message] ...]" >&2
  exit 2
fi
repo="$1"; branch="$2"; shift 2

# ### THE CAPTURE, (R175)(5), b564's defect (i): a push piped through `tail` lost the pre-push hook's lines. When the
# ### environment carries PUSH_GATED_LOG=<path>, every line this script and the git commands it runs write -- the hook's
# ### own output included -- is appended to that file as well as printed. The exit codes are this script's, unchanged.
if [ -n "${PUSH_GATED_LOG:-}" ]; then
  exec > >(tee -a "$PUSH_GATED_LOG") 2>&1
  echo "push_gated: capture on -> $PUSH_GATED_LOG ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
fi
case "$branch" in
  push-*|repair-*) ;;
  *) echo "push_gated: REFUSED -- <push-branch> must be push-* or repair-* (Rule 4.10): $branch" >&2; exit 2;;
esac

prev=$(git -C "$repo" symbolic-ref --short HEAD)
tip=$(git -C "$repo" rev-parse "refs/heads/$branch")
echo "push_gated: repo $repo ; branch $branch ; tip $tip ; checkout before $prev"

# ### (R178)(3): every tag argument is checked BEFORE anything is pushed. A name that exists already was made outside
# ### this script (by hand, or by an earlier run) and is refused; nothing is pushed.
for arg in "$@"; do
  tname="${arg%%::*}"
  if [ -z "$tname" ]; then
    echo "push_gated: REFUSED -- an empty tag name in argument '$arg'" >&2
    exit 7
  fi
  if git -C "$repo" rev-parse -q --verify "refs/tags/$tname" >/dev/null; then
    echo "push_gated: REFUSED -- tag $tname already exists locally; this script makes the tag after main's read-back (R178)(3). NOTHING IS PUSHED" >&2
    exit 7
  fi
  if [ -n "$(git -C "$repo" ls-remote origin "refs/tags/$tname")" ]; then
    echo "push_gated: REFUSED -- tag $tname already exists at the remote. NOTHING IS PUSHED" >&2
    exit 7
  fi
done
readback_equal=0

git -C "$repo" checkout -q "$branch"

# ### (R179)(5), b569: DEFECT (k) MADE A CHECK. Before a push of a repository whose directory is named PLACE-papers, the
# ### terminal table is regenerated in memory (relay tools/table_gate.py; HEAD is now the push branch's tip) and its grade
# ### cells diffed against relay HEAD's committed table; a moved cell the act's face does not name (`TABLE CELL: <repo> /
# ### <name>`) refuses the push: exit 9, the checkout restored, NOTHING IS PUSHED. TABLE_GATE_ARGS only ADDS arguments to the
# ### call (the test's fixture files); nothing skips it.
if [ "$(basename "$(cd "$repo" && pwd)")" = "PLACE-papers" ]; then
  tools_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  set +e
  # shellcheck disable=SC2086
  PYTHONIOENCODING=utf-8 python "$tools_dir/table_gate.py" --repo "$repo" ${TABLE_GATE_ARGS:-}
  rc=$?
  set -e
  if [ "$rc" -ne 0 ]; then
    git -C "$repo" checkout -q "$prev"
    echo "push_gated: TABLE CHECK REFUSED THE PUSH (table_gate exit $rc) -- NOTHING IS PUSHED" >&2
    exit 9
  fi
fi

set +e
git -C "$repo" push origin "$branch:main"
rc=$?
set -e
git -C "$repo" checkout -q "$prev"
if [ "$rc" -ne 0 ]; then
  echo "push_gated: MAIN PUSH REFUSED (exit $rc) -- NO TAG IS PUSHED" >&2
  exit 3
fi

remote_main=$(git -C "$repo" ls-remote origin refs/heads/main | cut -f1)
echo "push_gated: main read back at the remote: $remote_main"
if [ "$remote_main" != "$tip" ]; then
  echo "push_gated: MAIN READ-BACK UNEQUAL ($remote_main != $tip) -- NO TAG IS MADE OR PUSHED" >&2
  exit 4
fi
readback_equal=1

for arg in "$@"; do
  tag="${arg%%::*}"
  if [ "$arg" != "$tag" ]; then msg="${arg#*::}"; else msg="$tag -- made by push_gated.sh after main read back at $remote_main"; fi
  # ### the guard the ruling names: no tag is made unless the read-back happened, and was equal, in this run.
  if [ "$readback_equal" -ne 1 ]; then
    echo "push_gated: REFUSED -- tag $tag requested without an equal read-back in this run" >&2
    exit 8
  fi
  set +e
  git -C "$repo" tag -a "$tag" -m "$msg" "$remote_main"
  rc=$?
  set -e
  if [ "$rc" -ne 0 ]; then
    echo "push_gated: TAG NOT MADE ($tag, exit $rc)" >&2
    exit 8
  fi
  echo "push_gated: tag $tag made at the read-back $remote_main ($(git -C "$repo" rev-parse "refs/tags/$tag"))"
  set +e
  git -C "$repo" push origin "refs/tags/$tag"
  rc=$?
  set -e
  if [ "$rc" -ne 0 ]; then
    echo "push_gated: TAG PUSH REFUSED ($tag, exit $rc)" >&2
    exit 5
  fi
  local_peel=$(git -C "$repo" rev-parse "$tag^{}")
  remote_peel=$(git -C "$repo" ls-remote origin "refs/tags/$tag^{}" | cut -f1)
  echo "push_gated: tag $tag peeled local $local_peel remote $remote_peel"
  if [ "$remote_peel" != "$local_peel" ]; then
    echo "push_gated: TAG READ-BACK UNEQUAL ($tag)" >&2
    exit 6
  fi
done
echo "push_gated: DONE -- main and $# tag(s) pushed and read back"
