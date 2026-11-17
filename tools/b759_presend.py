# -*- coding: utf-8 -*-
"""tools/b759_presend.py -- (R369)(5): "THE PRE-SEND READS of (R368)(4), carried and banked as data/b759_presend.txt: duplicates 0; the
filter's refusals the two known." The two reads and their controls are tools/b758_presend.py's, imported and not changed (its reader of the
targets, the libraries and the namespaces tools/b757_join.py's, through it): (i) each fully qualified declaration name in one module over the
targets' modules and their import closure in the kernel's tree, the duplicates printed, 0 wanted; (ii) each line of print_targets.txt against
the workflow's filter (build-module.yml :91), the lines it refuses printed, the two known (:358 and :359, each carrying the Greek capital
lambda). This file's own: the bank's name, its head, and the two revisions read -- main 630cba16, where push-b759-weil is made, and the
branch's tip the dispatch is sent at. Reads only; the one write is data/b759_presend.txt (through standing.figbank).

THE SALT CHECK, (R369)(5): "printed before the send: the statement beside h2_sign's, the same expression with primeTermQ cQ and archTermQ
where primeSum and archTerm stand, under a negation, binding no hypothesis." Read from the blobs at the tip: h2_sign's body
(SIDEExplicitFormula/H2Sign.lean, after `def h2_sign : Prop :=`) and zq_weil_positivity_fails's statement (Schema/Wide/HalfScaleControl.lean,
between its name and `:= by`); the body taken into the control's names (classK and poleTerm qualified by B321, primeSum to
`primeTermQ (fun n => cQ n)`, archTerm to archTermQ), a negation put before it, and the two read equal with the whitespace collapsed; no
binder between the theorem's name and its colon; `open scoped ComplexOrder in` the line before its docstring and no other line of the file
opening ComplexOrder. Its planted controls: a binder, primeSum left, the negation dropped, each refused.

  control               b758's controls and the salt check's, printed
  read <rev>            both reads at a revision, printed
  salt <rev>            the salt check at a revision, printed
  bank <before> <tip>   the controls, both reads at each revision and the salt check at the tip, written to data/b759_presend.txt with the
                        foot read at the tip
"""
import os
import re
import sys

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b758_presend as P         # noqa: E402  ### b758's two reads and controls, imported and not changed
import figbank as FB             # noqa: E402

NL = '\n'
ACT = 'b759'
BANK = os.path.join(D, 'b759_presend.txt')
KNOWN = [358, 359]   # ### the filter's two known refusals at 630cba16 (data/b758_presend.txt; b759 step zero, data/b759_events.txt (14))
H2_PATH = 'SIDEExplicitFormula/H2Sign.lean'
WEIL_PATH = 'SIDEExplicitFormula/Schema/Wide/HalfScaleControl.lean'
WEIL = 'zq_weil_positivity_fails'
SUBS = ((r'\bclassK\b', 'B321.classK'), (r'\bpoleTerm\b', 'B321.poleTerm'), (r'\bprimeSum\b', 'primeTermQ (fun n => cQ n)'),
        (r'\barchTerm\b', 'archTermQ'))


def _ws(s):
    return ' '.join(s.split())


def h2_body(text):
    """h2_sign's body as H2Sign.lean writes it: after `def h2_sign : Prop :=`, to the first empty line; '' where unread."""
    m = re.search(r'^def h2_sign : Prop :=\n(.*?)\n\s*\n', text.replace('\r', ''), re.S | re.M)
    return _ws(m.group(1)) if m else ''


def weil_parts(text, name=WEIL):
    """(the binders between the theorem's name and its colon, the statement between the colon and `:= by`, the line before its docstring,
    the lines of the file opening ComplexOrder); (None, '', '', []) where the theorem is unread."""
    t = text.replace('\r', '')
    m = re.search(r'^theorem %s\b(.*?):\s(.*?):= by' % re.escape(name), t, re.S | re.M)
    if not m:
        return None, '', '', []
    ls = t.split(NL)
    k = t[:m.start()].count(NL)               # ### the theorem's line, 0-based
    j = k - 1
    while j >= 0 and not ls[j].startswith('/--'):
        j -= 1
    before = ls[j - 1] if j >= 1 else ''
    opens = [n + 1 for n, l in enumerate(ls) if re.match(r'^\s*open\b.*\bComplexOrder\b', l)]
    return _ws(m.group(1)), _ws(m.group(2)), before, opens


def salt_of(h2_text, weil_text, name=WEIL):
    """the salt check, pure: (lines, passed)."""
    body = h2_body(h2_text)
    want = body
    for a, b in SUBS:
        want = re.sub(a, b, want)
    want = '¬ ' + want
    binders, stmt, before, opens = weil_parts(weil_text, name)
    eq = bool(body) and stmt == want
    nob = binders == ''
    co = before.strip() == 'open scoped ComplexOrder in' and len(opens) == 1
    L = ['  h2_sign (%s, its body)        : %s' % (H2_PATH, body or 'UNREAD'),
         '  the body in the control`s names : %s' % want,
         '  %s (%s)  : %s' % (name, WEIL_PATH, stmt or 'UNREAD'),
         '  THE SAME EXPRESSION UNDER A NEGATION: %s ; BINDERS BEFORE ITS COLON: %s ; ComplexOrder OPENED FOR IT ALONE: %s (the line before its '
         'docstring %r ; the file`s lines opening ComplexOrder %s)' % ('EQUAL' if eq else 'UNEQUAL', binders if binders else 'none (binding no hypothesis)',
                                                                     'YES' if co else 'NO', before.strip(), opens)]
    return L, eq and nob and co


def salt_controls():
    L, ok = [], []
    h2 = NL.join(['def h2_sign : Prop :=', '  ∀ k : ℝ → ℂ, classK k → 0 ≤ poleTerm k - primeSum k + archTerm k', '', 'x'])
    good = ['open scoped ComplexOrder in', '/-- d -/', 'theorem t :', '    ¬ ∀ k : ℝ → ℂ, B321.classK k →',
            '      0 ≤ B321.poleTerm k - primeTermQ (fun n => cQ n) k + archTermQ k := by', '  intro h']
    cases = [('the planted theorem as ordered', good, True),
             ('a hypothesis bound before its colon', [good[0], good[1], 'theorem t (hk : True) :'] + good[3:], False),
             ('primeSum left in place of primeTermQ', good[:4] + ['      0 ≤ B321.poleTerm k - primeSum k + archTermQ k := by'] + good[5:], False),
             ('the negation dropped', good[:3] + ['    ∀ k : ℝ → ℂ, B321.classK k →'] + good[4:], False),
             ('ComplexOrder opened for the whole file', ['open scoped ComplexOrder'] + good[1:], False)]
    for what, lines, want in cases:
        _L, got = salt_of(h2, NL.join(lines), 't')
        ok.append(got == want)
        L.append('  (s%d) %s: %s -> %s' % (len(ok), what, 'PASSED' if got else 'REFUSED', 'AS WANTED' if got == want else 'NOT AS WANTED'))
    return L, ok


def salt_at(rev):
    sha = P.J.g('rev-parse', rev).strip()
    L, passed = salt_of(P.J.g('show', '%s:%s' % (rev, H2_PATH)), P.J.g('show', '%s:%s' % (rev, WEIL_PATH)))
    return ['## THE SALT CHECK AT %s (%s)' % (rev, sha[:8])] + L, passed


def cmd_bank(before, tip):
    L, ok = P.controls()
    sL, sok = salt_controls()
    L, ok = L + ['  THE SALT CHECK`S PLANTED CONTROLS:'] + sL, ok + sok
    lb, fb = P.read_at(before)
    lt, ft = P.read_at(tip)
    st, spass = salt_at(tip)
    known = ft['filtered'] == KNOWN
    out = ['%s -- (R369)(5): THE PRE-SEND READS OF (R368)(4), CARRIED, IN SIDE-explicit-formula, BEFORE THE DISPATCH (%s)' % (ACT, P._now()), '',
           '### (i) each fully qualified declaration name in one module, over the targets` modules and their import closure in the tree, the',
           '### duplicates printed, 0 wanted at the tip; (ii) each line of print_targets.txt against build-module.yml :91`s filter, the lines it',
           '### refuses printed, the two known wanted (:358 and :359, each carrying the Greek capital lambda); the file not edited for them, the',
           '### workflow not widened. The reads and controls are tools/b758_presend.py`s, imported and not changed.',
           '', '## THE CONTROLS'] + L + ['', '### main as b758 left it (v0.40), where push-b759-weil is made'] + lb + [
           '', '### the tip the dispatch is sent at'] + lt + ['', '### (R369)(5): the salt check, printed before the send'] + st + ['',
           '### ### **THE PRE-SEND READS AT %s: DUPLICATES %d (OVER THE TARGETS %d) ; ANONYMOUS PAIRS %d (OF %d, %d UNREAD) ; REFUSED BY THE FILTER %d (%s), '
           'THE TWO KNOWN %s ; TARGETS %d MODULES FOR %d NAMES, %d REFUSED, MODULES REFUSED %d ; THE SALT CHECK %s ; CONTROLS %d OF %d.**' % (
               ft['sha'][:8], ft['dup_c'], ft['dup_t'], ft['anon_pairs'], ft['anon'], ft['anon_unread'], len(ft['filtered']),
               ', '.join(':%d' % n for n in ft['filtered']) or 'none', 'YES' if known else 'NO', ft['modules'], ft['names'], ft['refused_targets'],
               ft['target_refused'], 'PASSED' if spass else 'REFUSED', sum(ok), len(ok))]
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b759_presend.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = P.controls()
        sL_, sok_ = salt_controls()
        print(NL.join(L_ + ['  THE SALT CHECK`S PLANTED CONTROLS:'] + sL_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_ + sok_), len(ok_ + sok_)))
    elif a[:1] == ['read'] and len(a) == 2:
        P.cmd_read(a[1])
    elif a[:1] == ['salt'] and len(a) == 2:
        sL_, sp_ = salt_at(a[1])
        print(NL.join(sL_))
        print('### THE SALT CHECK %s' % ('PASSED' if sp_ else 'REFUSED'))
    elif a[:1] == ['bank'] and len(a) == 3:
        cmd_bank(a[1], a[2])
    else:
        sys.exit(__doc__)
