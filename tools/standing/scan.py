# -*- coding: utf-8 -*-
"""standing/scan.py -- THE LITERAL SCAN OVER tools/standing/ ((R325)(3)(ii) and the author's word (1)(a) of the toolset act) and the
delete-free reading (the class repair (4)(v)).

Each standing file is split by Python's tokenizer into code (every token but comments and statement-level strings) and prose (comments
and docstrings). Counted in the code: act literals (a `b` and three digits as a word), ruling literals (an `R` and three digits as a
word), hexadecimal runs of seven to forty characters (an object's name), and imports of a module whose name carries an act number.
Counted apart in the prose: the act literals that cite a provenance. The delete-free reading: the words of tools/b703_checks.py
no_delete (:1334-:1339, provenance, copied) over the code. VERSION is read whole as code.

  python -X utf8 tools/standing/scan.py          prints the scan; writes nothing
  python -X utf8 tools/standing/scan.py bank     the same, banked as data/<act>_standing_scan.txt
"""
import io
import os
import re
import sys
import time
import tokenize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

S = os.path.dirname(os.path.abspath(__file__))
NL = '\n'
# an act literal is `b` and three digits not inside a longer word or number; `_` may follow it (a bank's or a module's name: the word
# boundary of the closure measurement's pattern reads no boundary before `_`, and so misses every act-named file -- the control below)
PATTERNS = (('act literals', re.compile(r'(?<![A-Za-z0-9])b\d{3}(?!\d)')), ('ruling literals', re.compile(r'(?<![A-Za-z0-9])R\d{3}(?!\d)')),
            ('hex runs', re.compile(r'(?<![A-Za-z0-9_])[0-9a-f]{7,40}(?![A-Za-z0-9_])')))
# the scan's positive control: a planted source, each kind once in the code and an act literal once in the prose
PLANT = ('# a provenance comment citing b' + '714\n'
         'import b' + '714_checks\n'
         "x = 'data/b" + "714_steps.json'\n"
         "r = '(R" + "324)'\n"
         "c = '1992" + "a71c'\n"
         'os' + '.remove(x)\n')
PLANT_WANT = dict(act=2, ruling=1, hex=1, imports=1, deletes=1, prose=1)   # the import's module name is an act literal in the code too
ACT_IMPORT = re.compile(r'^\s*(?:import|from)\s+(b\d{3}\w*)', re.M)
DELETE_WORDS = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
                'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D',
                'worktree' + ' remove' + r'\b', 'tag' + ' -' + 'd' + r'\b']
DELETE = re.compile(r'(' + '|'.join(DELETE_WORDS) + r')')


def split(text):
    """(code, prose) of a Python source by its tokens: comments and statement-level strings are prose, blanked in place in the code (the
    code keeps its own text, so `os.remove` stays one word)."""
    lines_ = text.split(NL)
    starts = [0]
    for l in lines_:
        starts.append(starts[-1] + len(l) + 1)
    spans, prose = [], []
    prev = tokenize.NEWLINE
    for tok in tokenize.generate_tokens(io.StringIO(text).readline):
        if tok.type == tokenize.COMMENT or (
                tok.type == tokenize.STRING and prev in (tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT, tokenize.ENCODING)):
            prose.append(tok.string)
            spans.append((starts[tok.start[0] - 1] + tok.start[1], starts[tok.end[0] - 1] + tok.end[1]))
        if tok.type not in (tokenize.COMMENT, tokenize.NL):
            prev = tok.type
    code = list(text)
    for a, b in spans:
        for i in range(a, b):
            if code[i] != NL:
                code[i] = ' '
    return ''.join(code), NL.join(prose)


def count(text):
    code, prose = split(text)
    h = dict((k, p.findall(code)) for k, p in PATTERNS)
    return dict(act=len(h['act literals']), ruling=len(h['ruling literals']), hex=len(h['hex runs']), imports=len(ACT_IMPORT.findall(text)),
                deletes=len(DELETE.findall(code)), prose=len(PATTERNS[0][1].findall(prose)))


def files(root=S):
    return sorted(f for f in os.listdir(root) if f.endswith('.py') or f == 'VERSION')


def scan(root=S):
    rows = []
    for f in files(root):
        t = A.rd_path(os.path.join(root, f))
        code, prose = (t, '') if f == 'VERSION' else split(t)
        hits = dict((k, p.findall(code)) for k, p in PATTERNS)
        rows.append(dict(file=f, lines=t.count(NL), hits=hits, imports=ACT_IMPORT.findall(t),
                         prose=len(PATTERNS[0][1].findall(prose)), deletes=DELETE.findall(code)))
    return rows


def lines(root=S):
    rows = scan(root)
    cur = A.current()
    ver = A.rd_path(os.path.join(root, 'VERSION')).strip()
    L = ['%s -- THE LITERAL SCAN OVER tools/standing/ AT %s (%s)' % (cur['act'], ver, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### rows are the toolset`s files: lines ; in the code -- act literals, ruling literals, hex runs, act-named imports, delete words ;',
         '### in the prose, counted apart -- act literals citing a provenance. Written by tools/standing/scan.py.', '']
    for r in rows:
        L.append('  %-16s lines %4d | code: act %d ruling %d hex %d imports %d deletes %d | prose act %d%s' % (
            r['file'], r['lines'], len(r['hits']['act literals']), len(r['hits']['ruling literals']), len(r['hits']['hex runs']),
            len(r['imports']), len(r['deletes']), r['prose'],
            ''.join(' ; %s %s' % (k, v) for k, v in r['hits'].items() if v) + (' ; imports %s' % r['imports'] if r['imports'] else '')
            + (' ; deletes %s' % r['deletes'] if r['deletes'] else '')))
    code = sum(len(v) for r in rows for v in r['hits'].values()) + sum(len(r['imports']) for r in rows)
    dele = sum(len(r['deletes']) for r in rows)
    pc = count(PLANT)
    L += ['', '### THE SCAN`S POSITIVE CONTROL, a planted source of six lines: found %s ; wanted %s ; AS WANTED %s ; the closure measurement`s '
          'pattern \\bb\\d{3}\\b over the same code finds %d act literal(s)' % (
              pc, PLANT_WANT, pc == PLANT_WANT, len(re.findall(r'\bb\d{3}\b', split(PLANT)[0])))]
    if pc != PLANT_WANT:
        code += 1   # a scan that cannot find its needles reads no zero
    L += ['', '### ### **FILES %d ; LITERALS IN THE CODE %d (ACT %d, RULING %d, HEX %d, ACT-NAMED IMPORTS %d) ; PROVENANCE IN THE PROSE %d ; '
          'DELETE WORDS IN THE CODE %d.**' % (len(rows), code, sum(len(r['hits']['act literals']) for r in rows),
                                              sum(len(r['hits']['ruling literals']) for r in rows), sum(len(r['hits']['hex runs']) for r in rows),
                                              sum(len(r['imports']) for r in rows), sum(r['prose'] for r in rows), dele)]
    return L, code, dele


def main(route):
    L, code, dele = lines()
    if route == 'bank':
        p = os.path.join(A.D, '%s_standing_scan.txt' % A.current()['act'])
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    print(NL.join(L))
    return 0 if (code == 0 and dele == 0) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
