# -*- coding: utf-8 -*-
"""test_edit_route_b646.py -- THE EDIT-ROUTE ARM'S PLANTED TEST, (R256)(2): one command of each kind fails the arm; the house forms pass.

### Numbered cases `  (n) ... PASS|FAIL` ((R233)(3)). Each planted command must carry its kind; each house-form command must carry none.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edit_route as ER  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PLANTED = [
    ('S', "sed -i 's/a/b/' tools/b999_record.py"),
    ('S', "cd /d/relay && sed -Ei 's/x/y/' data/b999.txt"),
    ('H', "cat > tools/b999_record.py <<'EOF'\nprint(1)\nEOF"),
    ('H', "python - <<'PY'\nopen('/d/relay/tools/b999.py','w').write('x')\nPY"),
    ('H', "echo x >> /d/relay/tools/b999.py"),
    ('H', "Get-Content a.py | Out-File -Encoding utf8 D:\\relay\\tools\\b999.py"),
    ('H', "cp /d/relay/tools/b645_tests.py tools/b999_tests.py"),
    ('R', "rm data/b999_scratch.txt"),
    ('R', "rm -rf build/*"),
    ('R', "Remove-Item .\\data\\b999.txt -Force"),
    ('R', "git -C /d/relay rm data/b999.txt"),
    ('R', "git branch -d push-b64*"),
    ('R', "git branch --merged | grep push | xargs git branch -d"),
    ('R', "rm -f \"$SPD/x.txt\""),
]
HOUSE = [
    "sed -n '1,20p' tools/b645_record.py",
    "cat /d/relay/tools/b645_tests.py 2>/dev/null > /d/relay/data/b999_copy.txt",
    "python -c \"print(1 if 2>1 else 0); open('tools/x')\"",
    "git -C /d/relay commit -q -m \"b999: rm data/x; sed -i in a message > tools/y\"",
    "rm -f /d/relay/data/b999_scratch.txt && ls /d/relay/data",
    "Remove-Item -LiteralPath 'D:\\relay\\data\\b999.txt' -Force -Confirm:$false",
    "git -C /d/relay branch -d push-b645 push-b645-closing push-b645-root",
    "git push origin --delete push-b645-root",
    "grep -n 'x' tools/e0_rule.py | head > /d/relay/data/b999.txt",
    "python tools/b646_record.py commands",
]


def main():
    n, bad = 0, 0
    for kind, cmd in PLANTED:
        n += 1
        o = ER.offences(cmd)
        ok = any(k.startswith(kind) for k, _ in o)
        bad += not ok
        print('  (%d) planted %s %-60r -> %s  %s' % (n, kind, cmd[:60], [k for k, _ in o] or 'NONE', 'PASS' if ok else 'FAIL'))
    for cmd in HOUSE:
        n += 1
        o = ER.offences(cmd)
        ok = not o
        bad += not ok
        print('  (%d) house form %-62r -> %s  %s' % (n, cmd[:62], o or 'NONE', 'PASS' if ok else 'FAIL'))
    rows = [{'n': i, 'tool': 'Bash', 'cmd': c} for i, (_, c) in enumerate(PLANTED)] + [{'n': 100 + i, 'tool': 'Bash', 'cmd': c} for i, c in enumerate(HOUSE)]
    n += 1
    hit = ER.scan(rows)
    ok = len(hit) == len(PLANTED) and all(r['n'] < 100 for r, _ in hit)
    bad += not ok
    print('  (%d) scan over the mixed bank flags the %d planted rows and no house-form row -> %d flagged  %s' % (n, len(PLANTED), len(hit), 'PASS' if ok else 'FAIL'))
    print('### %d cases, %d failing' % (n, bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
