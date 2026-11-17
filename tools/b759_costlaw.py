# -*- coding: utf-8 -*-
"""tools/b759_costlaw.py -- (R369)(7): F1 AND F2, BANKED AS data/b759_costlaw.txt BY A TOOL COMMITTED BEFORE ITS RUN.

(7)'s words (data/b759_ferry.txt :25): "F1 is the square root of 2 pi times gamma to the power sigma less 1/2, at sigma = 0.95326 and gamma =
16.290216, to three figures, printed beside the quotient of the two banked figures 1.2972e11 and 1.4608e10 (data/b744_zetabox_plan.txt :134;
data/b740_offlinezero_notes.txt :5); where the two agree within one part in a hundred the sentence stands as the block prints it, and where
they do not its words "as Stirling's formula says" are cut and both numbers printed. F2 is e to the power pi (gamma' - gamma)/2 at gamma' =
29.5517610986 and gamma = 16.2902157204 (INSTRUMENTS :556), written a x 10^b to two figures. The navigator's own arithmetic read 8.88 and
1.1 x 10^9; the bank's figures govern."

Every input is read from a bank and none typed here: sigma, gamma, gamma' and the second gamma cut from (7)'s words in the ferry bank; the
figure 1.2972e+11 read at data/b744_zetabox_plan.txt :135, where it stands (the ruling's :134 carries zeta's figure, data/b759_events.txt
(11)), and 1.4608e10 at data/b740_offlinezero_notes.txt :5; INSTRUMENTS :556 read to carry gamma' and gamma, printed by its path, line and
sha256 (16 hex) and not by its words. The navigator's 8.88 and 1.1 x 10^9 are printed beside the computed figures and do not govern.

  control   the tool's planted controls, printed
  bank      the controls, the reads, F1 and F2 and the sentence's form, written to data/b759_costlaw.txt; the fields tool reads its FIELD lines
"""
import hashlib
import io
import math
import os
import re
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b759_worklist as K       # noqa: E402  (PP and INSTRUMENTS, the worklist's)
import figbank as FB            # noqa: E402

NL = '\n'
ACT = 'b759'
BANK = os.path.join(D, 'b759_costlaw.txt')
FERRY = os.path.join(D, 'b759_ferry.txt')
ZB, ZB_LINE = 'data/b744_zetabox_plan.txt', 135
ON, ON_LINE = 'data/b740_offlinezero_notes.txt', 5
INSTR_LINE = 556
NAVIGATOR = ('8.88', '1.1 × 10^9')   # ### the ruling's words, "The navigator's own arithmetic read 8.88 and 1.1 x 10^9", printed beside and not governing


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _lines(rel):
    return io.open(os.path.join(RELAY, rel), encoding='utf-8').read().replace('\r', '').split(NL)


def clause7():
    ls = [l for l in _lines('data/b759_ferry.txt') if l.startswith('(7) ')]
    if len(ls) != 1:
        sys.exit('### (7) NOT READ ONCE IN THE FERRY BANK -- nothing written')
    return ls[0]


def inputs(text):
    """(sigma, gamma) of F1 and (gamma', gamma) of F2, cut from (7)'s words; None where a value is not read once."""
    m1 = re.findall(r'at sigma = ([0-9.]+) and gamma = ([0-9.]+), to three figures', text)
    m2 = re.findall(r"at gamma' = ([0-9.]+) and gamma = ([0-9.]+) \(INSTRUMENTS :556\)", text)
    return (m1[0] if len(m1) == 1 else None), (m2[0] if len(m2) == 1 else None)


def figure_at(rel, line, pat):
    """the one figure matching pat on the bank's line, as a float, with the line's text; (None, text) where not read once."""
    t = _lines(rel)[line - 1]
    m = re.findall(pat, t)
    return (float(m[0]) if len(m) == 1 else None), t


def f1(sigma, gamma):
    return math.sqrt(2 * math.pi) * gamma ** (sigma - 0.5)


def f2(gp, g):
    return math.exp(math.pi * (gp - g) / 2)


def three(x):
    return '%.3g' % x


def sci2(x):
    """a x 10^b to two figures."""
    b = int(math.floor(math.log10(abs(x))))
    a = round(x / 10 ** b, 1)
    if a >= 10:
        a, b = round(a / 10, 1), b + 1
    return '%.1f × 10^%d' % (a, b)


def agree(a, b, part=100):
    return abs(a - b) <= abs(b) / part


def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    c('F1 on planted values: sigma 1/2 gives the square root of 2 pi alone', three(f1(0.5, 7.0)), three(f1(0.5, 7.0)) == '2.51')
    c('F2 on planted heights a difference of 2 ln 10 / pi apart: 10 exactly', round(f2(5 + 2 * math.log(10) / math.pi, 5), 9), abs(f2(5 + 2 * math.log(10) / math.pi, 5) - 10) < 1e-9)
    c('two figures: 1.234e9, 9.96e9 and 1.06e-3 written', (sci2(1.234e9), sci2(9.96e9), sci2(1.06e-3)),
      (sci2(1.234e9), sci2(9.96e9), sci2(1.06e-3)) == ('1.2 × 10^9', '1.0 × 10^10', '1.1 × 10^-3'))
    c('the agreement within one part in a hundred: 8.88 against 8.88 x 1.009 taken, against 8.88 x 1.011 refused',
      (agree(8.88, 8.88 * 1.009), agree(8.88, 8.88 * 1.011)), agree(8.88, 8.88 * 1.009) and not agree(8.88, 8.88 * 1.011))
    pl = 'F1 is x, at sigma = 0.5 and gamma = 2.0, to three figures, ... F2 is y at gamma\' = 3.0 and gamma = 1.0 (INSTRUMENTS :556), written'
    c('the inputs cut from planted words; words missing one value refused', (inputs(pl), inputs(pl.replace('gamma = 2.0, ', ''))[0]),
      inputs(pl) == (('0.5', '2.0'), ('3.0', '1.0')) and inputs(pl.replace('gamma = 2.0, ', ''))[0] is None)
    return L, ok


def run():
    L, ok = controls()
    text = clause7()
    i1, i2 = inputs(text)
    if not i1 or not i2:
        sys.exit('### THE INPUTS NOT CUT ONCE FROM (7) -- nothing written')
    sigma, gamma = float(i1[0]), float(i1[1])
    gp, g = float(i2[0]), float(i2[1])
    zb, zbt = figure_at(ZB, ZB_LINE, r'e\^\(πγ/2\) = ([0-9.]+e\+[0-9]+)')
    on, ont = figure_at(ON, ON_LINE, r'\(([0-9.]+e[0-9]+)\)')
    inl = io.open(os.path.join(K.PP, K.INSTRUMENTS), encoding='utf-8').read().replace('\r', '').split(NL)[INSTR_LINE - 1]
    in_ok = i2[0] in inl and i2[1] in inl
    if zb is None or on is None:
        sys.exit('### A BANKED FIGURE NOT READ ONCE AT ITS LINE -- nothing written')
    F1 = f1(sigma, gamma)
    Q = zb / on
    ag = agree(F1, Q)
    F2 = f2(gp, g)
    form = 'STANDS AS THE BLOCK PRINTS IT' if ag else 'CUT: its words "as Stirling`s formula says" cut and both numbers printed'
    out = ['%s -- (R369)(7): F1 AND F2, THE COST LAW`S TWO FIGURES, FROM THE BANKS (%s, tools/b759_costlaw.py)' % (ACT, _now()), '',
           '## THE CONTROLS'] + L + ['  controls %d of %d as wanted' % (sum(ok), len(ok)), '',
           '## THE INPUTS, EACH READ FROM A BANK',
           '  from (7)`s words (data/b759_ferry.txt :25): F1 at sigma = %s and gamma = %s ; F2 at gamma` = %s and gamma = %s' % (i1[0], i1[1], i2[0], i2[1]),
           '  %s :%d (the ruling cites :134, which carries zeta`s figure; events (11)): e^(pi gamma/2) = %s' % (ZB, ZB_LINE, '%.4e' % zb),
           '  %s :%d: 1/|Gamma(cA)| = %s' % (ON, ON_LINE, '%.4e' % on),
           '  phase1.5/method/INSTRUMENTS.md :%d (sha256 %s, cited by digest, not quoted): carries gamma` %s and gamma %s: %s' % (
               INSTR_LINE, hashlib.sha256(inl.encode('utf-8')).hexdigest()[:16], i2[0], i2[1], 'YES' if in_ok else 'NO'), '',
           '## F1: sqrt(2 pi) gamma^(sigma - 1/2)',
           '  F1 = %.6f, to three figures %s ; the quotient of the two banked figures %.4e / %.4e = %.6f ; their difference %.4f%% of the quotient' % (
               F1, three(F1), zb, on, Q, 100 * abs(F1 - Q) / Q),
           '  within one part in a hundred: %s -> the sentence %s' % ('YES' if ag else 'NO', form),
           '  the navigator`s own arithmetic: %s (does not govern)' % NAVIGATOR[0], '',
           '## F2: e^(pi (gamma` - gamma)/2)',
           '  F2 = %.6e, written to two figures %s ; the navigator`s own arithmetic: %s (does not govern)' % (F2, sci2(F2), NAVIGATOR[1]), '',
           'FIELD F1 = %s' % three(F1),
           'FIELD F1_QUOTIENT = %.3g' % Q,
           'FIELD F1_SENTENCE = %s' % ('STANDS' if ag else 'CUT'),
           'FIELD F2 = %s' % sci2(F2), '',
           '### ### **F1 %s (THE QUOTIENT %.3g, %s) ; F2 %s ; INSTRUMENTS :556 %s ; CONTROLS %d OF %d.**' % (
               three(F1), Q, 'AGREEING WITHIN ONE PART IN A HUNDRED, THE SENTENCE STANDS' if ag else 'NOT AGREEING, THE WORDS CUT', sci2(F2),
               'CARRYING BOTH HEIGHTS' if in_ok else 'NOT CARRYING BOTH HEIGHTS', sum(ok), len(ok))]
    return out, all(ok) and in_ok


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['control']:
        L_, ok_ = controls()
        print(NL.join(L_))
        print('### CONTROLS %d OF %d AS WANTED' % (sum(ok_), len(ok_)))
    elif a[:1] == ['bank']:
        out_, good_ = run()
        if not good_:
            print(NL.join(out_))
            sys.exit('### A CONTROL OR THE INSTRUMENTS READ NOT AS WANTED -- nothing written')
        r_ = FB.write(BANK, NL.join(out_))
        print(NL.join(out_))
        print('written data/b759_costlaw.txt ; figbank: %s' % r_['why'])
    else:
        sys.exit(__doc__)
