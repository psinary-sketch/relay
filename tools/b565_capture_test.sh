#!/usr/bin/env bash
# b565_capture_test.sh -- THE TEST OF push_gated.sh's CAPTURE, (R175)(5). Writes the scratchpad only: a bare repository, a
# working clone whose pre-push hook prints a marker line, and two log paths. Both polarities: with PUSH_GATED_LOG set the
# marker and the read-back land in the log and the exit is 0; with it unset no log file is written. Deletes nothing.
# usage: b565_capture_test.sh <scratch dir>
set -uo pipefail
S="$1"
PG="$(cd "$(dirname "$0")" && pwd)/push_gated.sh"
W="$S/capture_test_$(date +%s)"
mkdir -p "$W"
git init -q --bare "$W/origin.git"
git init -q "$W/work"
git -C "$W/work" config user.email test@example.invalid
git -C "$W/work" config user.name capture-test
mkdir -p "$W/work/.hooks"
printf '#!/bin/sh\necho "B565-HOOK-MARKER: pre-push ran"\nexit 0\n' > "$W/work/.hooks/pre-push"
chmod +x "$W/work/.hooks/pre-push"
git -C "$W/work" config core.hooksPath .hooks
git -C "$W/work" remote add origin "$W/origin.git"
echo x > "$W/work/f.txt"
git -C "$W/work" add f.txt
git -C "$W/work" commit -q -m first
git -C "$W/work" branch -M main
git -C "$W/work" push -q origin main 2>/dev/null
echo y >> "$W/work/f.txt"
git -C "$W/work" commit -q -am second
git -C "$W/work" branch push-test main
PUSH_GATED_LOG="$W/on.log" bash "$PG" "$W/work" push-test
rc_on=$?
sleep 1
git -C "$W/work" commit -q --allow-empty -m third
git -C "$W/work" branch -f push-test main
bash "$PG" "$W/work" push-test > "$W/off_console.txt" 2>&1
rc_off=$?
m_on=$(grep -c "B565-HOOK-MARKER" "$W/on.log" 2>/dev/null || echo 0)
rb_on=$(grep -c "push_gated: main read back at the remote" "$W/on.log" 2>/dev/null || echo 0)
m_off_console=$(grep -c "B565-HOOK-MARKER" "$W/off_console.txt" 2>/dev/null || echo 0)
off_log=$(ls "$W"/off.log 2>/dev/null | wc -l)
echo "### b565 -- THE CAPTURE TEST (scratch: $W)"
echo "    (i)  PUSH_GATED_LOG set : exit $rc_on ; the hook's marker lines in the log $m_on ; the read-back line in the log $rb_on"
echo "    (ii) PUSH_GATED_LOG unset: exit $rc_off ; the hook's marker on the console $m_off_console ; a log file written $off_log"
if [ "$rc_on" -eq 0 ] && [ "$m_on" -ge 1 ] && [ "$rb_on" -ge 1 ] && [ "$rc_off" -eq 0 ] && [ "$m_off_console" -ge 1 ] && [ "$off_log" -eq 0 ]; then
  echo "### ### **CAPTURE TEST : PASS** -- the hook's own line reaches the log when asked, and nothing is logged when not."
  exit 0
fi
echo "### ### **CAPTURE TEST : FAIL**"
exit 1
