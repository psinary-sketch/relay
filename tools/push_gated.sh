#!/usr/bin/env bash
# push_gated.sh -- THE PUSH DISCIPLINE, (R171)(2), written at b561.
#
# usage: push_gated.sh <repo> <push-branch> [tag ...]
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
# 6 a tag read-back unequal. The script prints one line per step; it deletes nothing.
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "push_gated: usage: push_gated.sh <repo> <push-branch> [tag ...]" >&2
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

git -C "$repo" checkout -q "$branch"
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
  echo "push_gated: MAIN READ-BACK UNEQUAL ($remote_main != $tip) -- NO TAG IS PUSHED" >&2
  exit 4
fi

for tag in "$@"; do
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
