# -*- coding: utf-8 -*-
"""tools/b757_outcomes.py -- (R367)(4)-(7): EACH RESULT'S SENTENCE, THE RULING'S TEXT WITH ITS FIELDS FILLED FROM THE ACT'S BANKS AND NOTHING ELSE.

Each sentence is cut at run time from the ferry bank (data/b757_ferry.txt, the clause's quoted text after its outcome's words), and its
angle-bracket fields are filled from the dispatch rows (data/b757_dispatch_rows.json) and the kernel's tree at the built commit, each field
printed with the bank or blob it came from. No sentence is typed here. The outcome of each item is read from its rows by the clause's own
test, printed beside the sentence.

  join     (4): the join's one dispatch, read: the exit file, the axioms print, the lines against the joined print_targets.txt; the outcome and
           its sentence, the reading behind it (the declaration the environment held, in each module declaring it, with the commits that added
           them and the branches holding those commits; the names the workflow's grammar refused, with the bank that first entered them)
  bank     every item composed so far, written to data/b757_outcomes.txt and data/b757_outcomes.json (written whole at each run, by this tool)
"""
import io
import json
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b757_worklist as K        # noqa: E402

NL = '\n'
ACT = 'b757'
EF = K.EF_DIR
FERRY = os.path.join(D, 'b757_ferry.txt')
ROWS = os.path.join(D, 'b757_dispatch_rows.json')
BANK = os.path.join(D, 'b757_outcomes.txt')
BANKJ = os.path.join(D, 'b757_outcomes.json')
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
MAIN_AT_STEPZERO = '8fbab45d'


def g(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def ferry():
    return io.open(FERRY, encoding='utf-8').read().replace('\r', '').split(NL)


def clause(n):
    """(line number, text) of the ferry line opening '(n) '."""
    L = ferry()
    hit = [(i + 1, l) for i, l in enumerate(L) if l.startswith('(%d) ' % n)]
    if len(hit) != 1:
        sys.exit('### CLAUSE (%d) NOT READ ONCE IN THE FERRY BANK (%d lines) -- nothing written' % (n, len(hit)))
    return hit[0]


def quoted_after(text, words):
    """the quoted sentence after `words` in the clause's text."""
    i = text.find(words)
    if i < 0:
        return None
    m = re.match(r'\s*"(.*?)"', text[i + len(words):])
    return m.group(1) if m else None


def rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def fill(sentence, fields):
    out = sentence
    for k, v in fields.items():
        out = out.replace('<%s>' % k, str(v))
    left = re.findall(r'<[^<>]+>', out)
    return out, left


def join():
    ln, text = clause(4)
    yes = quoted_after(text, 'THE SENTENCE IF IT COMPILES:')
    no = quoted_after(text, 'THE SENTENCE IF IT DOES NOT:')
    R = rows()
    disp = [r for r in R if r.get('kind') == 'dispatch' and r.get('item') in ('join', 'join-repair')]
    reads = dict((int(r['run']), r) for r in R if r.get('kind') == 'read')
    out = ['## (4) THE JOIN (the ferry bank :%d; the sentences cut from it: compiled %d characters, not %d characters)' % (ln, len(yes or ''), len(no or ''))]
    if not disp or not yes or not no:
        out.append('  ### NO JOIN DISPATCH ROWED OR A SENTENCE NOT CUT -- nothing composed')
        return out, None
    d = disp[-1]
    rd = reads.get(int(d['run']))
    if not rd:
        out.append('  ### THE JOIN`S RUN %s NOT READ -- nothing composed' % d['run'])
        return out, None
    targets = rd.get('targets')
    ok = rd.get('build_exit') == '0' and rd.get('built_equal') and not rd.get('stop') and rd.get('axiom_lines') == targets \
        and rd.get('axiom_within') == targets and not rd.get('axiom_missing_n') and not rd.get('sorryAx') and not (rd.get('axioms_refused') or '').strip()
    out.append('  the dispatches: %s' % ', '.join('%d %s run %s at %s' % (x['n'], x['item'], x['run'], x['sha'][:8]) for x in disp))
    out.append('  THE RUN %s READ (data/b757_dispatch_rows.json): exit file %s ; built %s, equal to the dispatched commit %s ; stopped under the hold %s ; '
               'errors %d ; sorry warnings %s ; runner low %s MB' % (d['run'], rd.get('build_exit'), (rd.get('built_ref') or '')[:8], rd.get('built_equal'),
                                                                   bool(rd.get('stop')), len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('runner_low_mb')))
    out.append('  THE AXIOMS PRINT: %s' % rd.get('axioms_print'))
    out.append('  AGAINST THE JOINED print_targets.txt (%s lines): axioms lines %s ; within the standard three %s ; outside %d ; without a line %s ; sorryAx %s' % (
        targets, rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}), rd.get('axiom_missing_n'), rd.get('sorryAx')))
    for l in (rd.get('axioms_refused') or '').split(NL):
        if l.strip():
            out.append('  REFUSED BY THE WORKFLOW`S GRAMMAR (ASCII names alone): %s' % l.strip())
    out.append('  WHAT THE RUN MUST SHOW ((R367)(4)): the exit file 0 ; an axioms line within the standard three for each line ; no line naming sorryAx -> %s' % (
        'SHOWN' if ok else 'NOT SHOWN'))
    rec = dict(item='join', clause_line=ln, run=int(d['run']), sha=d['sha'], shown=ok)
    if ok:
        peel = (rd.get('built_ref') or '')[:8]
        s, left = fill(yes, {'peel': peel, 'run id': d['run'], 'n': rd.get('axiom_lines')})
        rec.update(outcome='COMPILED', sentence=s, unfilled=left)
        out.append('  THE OUTCOME: COMPILED -- main moves to %s by the gated push`s default mode and v0.39 is cut at its read-back' % peel)
    else:
        # ### the break: where the print's import failed, the module named and the line of the declaration the environment already held
        m = re.search(r"import (\S+) failed, environment already contains '([^']+)' from (\S+)", rd.get('axioms_print') or '')
        mod, line, reading = None, None, []
        if m:
            mod, held, other = m.group(1), m.group(2), m.group(3)
            base = held.split('.')
            name = [x for x in base if not re.match(r'^(match_\d+|proof_\d+|eq_\d+)$', x)][-1]
            for mm in (mod, other):
                path = mm.replace('.', '/') + '.lean'
                src = g('show', '%s:%s' % (d['sha'], path)).split(NL)
                decl = [i + 1 for i, l in enumerate(src) if re.match(r'^\s*(noncomputable\s+)?(def|theorem|abbrev|instance|structure)\s+%s\b' % re.escape(name), l)]
                imps = [l.split()[1] for l in src if l.startswith('import ')]
                added = g('log', '--format=%h', '--diff-filter=A', d['sha'], '--', path).split()
                held_by = [b.strip(' *') for b in g('branch', '--contains', added[-1]).split(NL) if b.strip()] if added else []
                reading.append('  %s (%s): `%s` declared at :%s ; imports %s ; added by %s ; that commit held by %s' % (
                    mm, path, name, ', :'.join(str(x) for x in decl) or 'NONE', ', '.join(imps), ', '.join(added) or 'NONE', ', '.join(held_by) or 'NONE'))
                if mm == mod and decl:
                    line = decl[0]
            out.append('  THE BREAK: the print`s import of the %d target modules together failed at %s, whose `%s` the environment already held from %s:' % (
                len((d.get('target') or '').split()), mod, name, other))
            out.extend(reading)
        if mod and line:
            s, left = fill(no, {'module': mod, 'line': line, 'run id': d['run']})
            rec.update(outcome='BROKE', sentence=s, unfilled=left, module=mod, line=line)
            out.append('  THE OUTCOME: THE FAILING OUTCOME ((R367)(4): "any other break is the failing outcome"; the break is not at (ii)`s file, so no second '
                       'dispatch): main stands at %s, no tag cut, the four branches as they stood; (5) built past zq-b730`s tip' % MAIN_AT_STEPZERO)
        else:
            rec.update(outcome='NOT READ', sentence=None, unfilled=None)
            out.append('  ### THE BREAK NOT READ FROM THE PRINT -- no sentence composed')
    out.append('  THE SENTENCE: %s' % (rec.get('sentence') or 'NONE'))
    out.append('  fields left unfilled: %s' % (rec.get('unfilled') if rec.get('unfilled') is not None else '-'))
    return out, rec


def bank():
    lines, recs = [], []
    for fn in (join,):
        o, r = fn()
        lines += o + ['']
        if r:
            recs.append(r)
    head = ['%s -- (R367)(4)-(7): EACH RESULT`S SENTENCE, THE RULING`S TEXT WITH ITS FIELDS FILLED FROM THE ACT`S BANKS (tools/b757_outcomes.py)' % ACT, '']
    tail = ['### ### **THE OUTCOMES: %s.**' % ' ; '.join('%s %s' % (r['item'].upper(), r['outcome']) for r in recs)]
    txt = NL.join(head + lines + tail) + NL
    with open(BANK, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt)
    tmp = BANKJ + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(recs, f, ensure_ascii=False, indent=1)
        f.write(NL)
    os.replace(tmp, BANKJ)
    print(txt)
    print('written data/b757_outcomes.txt and data/b757_outcomes.json (%d items)' % len(recs))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] not in ('join', 'bank'):
        sys.exit(__doc__)
    if a[0] == 'join':
        o, _r = join()
        print(NL.join(o))
    else:
        bank()
