# -*- coding: utf-8 -*-
"""b342_draft.py -- THE EXECUTOR'S DRAFT, BANKED VERBATIM FROM THE SESSION TRANSCRIPT. ### A READ, TO DISK.

### ### **WHY.** ### The sortie's leg 4 orders the two rules *as the executor's draft states them*. ### That draft is the
### `DRAFT -- NAVIGATOR EDITS` block of the b338 STOP, which lives only in the session transcript (the Claude Code
### JSONL), not in any repo. ### This tool locates that assistant message by its uuid, pulls the fenced block verbatim,
### and banks it so the extract step can quote it at a line. ### Nothing else is read from the transcript.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
TRANSCRIPT = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--', '41ec74a6-756c-4480-bbf3-5e7c45e947a9.jsonl')
UUID = '81fff50b-2b56-43ec-b9f0-27a2166c0123'
OUT = os.path.join(D, 'b342_executor_draft_2026-09-06.txt')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    with io.open(TRANSCRIPT, encoding='utf-8', errors='replace') as f:
        for ln in f:
            if UUID not in ln:
                continue
            j = json.loads(ln)
            if j.get('uuid') != UUID:
                continue
            c = j['message']['content']
            txt = ''.join(p.get('text', '') for p in c if isinstance(p, dict) and p.get('type') == 'text')
            i = txt.index('```' + chr(10) + 'DRAFT')
            k = txt.index('```', i + 3)
            block = txt[i + 4:k].rstrip() + chr(10)
            head = ('### THE EXECUTOR\'S DRAFT -- the `DRAFT -- NAVIGATOR EDITS` block of the b338 STOP, banked verbatim from the session\n'
                    '### transcript (assistant message uuid %s, timestamp %s) by tools/b342_draft.py.\n'
                    '### It bound nothing when written; the sortie ferry of 2026-09-06 cites it for legs 4 and 5.\n\n' % (UUID, j.get('timestamp')))
            io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(head + block)
            print('banked %s : %d lines' % (os.path.basename(OUT), len((head + block).splitlines())))
            return 0
    print('### the draft message was not found in the transcript')
    return 1


if __name__ == '__main__':
    sys.exit(main())
