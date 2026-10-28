"""b719 Component 4 -- (R329)(8): THE OFFSET READ, POST HOC, nothing new computed.

  python -X utf8 tools/b719_offset.py dry     # prints the bank
  python -X utf8 tools/b719_offset.py bank    # writes data/b719_offset_read.txt

Reads banked lines and tool source only: b717's seven -39 offsets (data/b717_onsets.txt :22-:28) and the residual (:54); the ferry's
(8)(i) observation (data/b719_ferry.txt :24); the onset's operational definition from the onset tool's source (tools/b709_pairs.py,
onset709 :148-:160 and constants_for709 :163-:189, the route b717 ran); the registered law (data/b716_registrations.txt :61-:66).
Every quoted line is printed with its file and number from the file itself, each needle's yield printed; no arithmetic at any pair.
"""
import io
import os
import sys
import time

D = 'D:/relay'
NL = '\n'
OUT = os.path.join(D, 'data', 'b719_offset_read.txt')


def lines(rel):
    return io.open(os.path.join(D, rel), encoding='utf-8').read().split(NL)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def span(rel, a, b, needles):
    """lines a..b of rel, 1-indexed, each needle's yield inside the span printed; a needle absent stops the tool."""
    L = lines(rel)
    body = L[a - 1:b]
    out = []
    for nd in needles:
        hits = [a + i for i, l in enumerate(body) if nd in l]
        out.append('### needle %r in %s :%d-:%d: yield %d at %s' % (nd, rel, a, b, len(hits), hits))
        if not hits:
            sys.exit('### NEEDLE %r ABSENT FROM %s :%d-:%d -- STOPPED' % (nd, rel, a, b))
    for i, l in enumerate(body):
        out.append('  %s :%d | %s' % (rel, a + i, l))
    return out


def build():
    R = []
    R.append('b719 -- (R329)(8): THE OFFSET READ, POST HOC -- b717`s -39 OFFSETS BESIDE THE NAVIGATOR`S 60, THE ONSET`S DEFINITION FROM ITS SOURCE,')
    R.append('THE SUBLEADING TERM FROM THE REGISTERED LAW, ONE HYPOTHESIS (%s)' % utc())
    R.append('')
    R.append('### POST HOC throughout: every figure below was banked before this read, the navigator`s observation was made after the fact on')
    R.append('### banked pairs, and nothing is computed at any pair. The hypothesis of (ii) is registered in data/b719_registrations.txt by a')
    R.append('### commit of its own, for the next tier, and read at no pair this act.')
    R.append('')
    R.append('## (i) THE -39 OFFSETS BESIDE 60, POST HOC')
    R.append('### the navigator`s observation (the ferry, quoted):')
    R += span('data/b719_ferry.txt', 24, 24, ['labelled post hoc', 'from 76 to 802', 'no fixed phase'])
    R.append('### b717`s seven -39 pairs and the residual beside them (quoted):')
    R += span('data/b717_onsets.txt', 22, 28, ['offset +54.8783', 'offset +107.5664'])
    R += span('data/b717_onsets.txt', 54, 55, ['-15 pair 8 +137.3', 'positive at 7 of 7'])
    R.append('### THE READ, POST HOC: at -39 the seven offsets are +54.9, +83.9, +67.2, +155.0, +161.7, +117.4, +107.6 (:22-:28): positive at 7 of')
    R.append('### 7; within 10 of 60 at 2 of 7 (pair 1 +54.9, pair 3 +67.2); above 100 at 4 of 7 (pairs 4-7). The')
    R.append('### ten -15 / Q0 figures the navigator reads near 60 (:54) run +44.9 to +137.3, one of ten above 100 (-15 pair 8). So "near 60"')
    R.append('### does not carry to -39 as it stands: -39`s offsets are of the same order and sign, and spread wider. The turn-period clause is not')
    R.append('### read at -39 here: the seven -39 pairs` periods are not banked, and computing them would be new arithmetic ((R329)(8): nothing new).')
    R.append('')
    R.append('## (ii) THE ONSET`S OPERATIONAL DEFINITION, PRINTED FROM THE ONSET TOOL`S SOURCE (the route b717 ran, data/b717_onsets.txt :5)')
    R += span('tools/b709_pairs.py', 148, 160, ['def onset709(', 'e = Dm - c * (lR * n).exp() + Cc * (n + 1) ** 2 * (ls * n).exp()', 'if e < 0:'])
    R += span('tools/b709_pairs.py', 163, 189, ['z = (1 - 1 / acb(d[2], d[3]))', 'r = (1 + R) / 2', 's = (s1 + R) / 2',
                                                 'Cc = 2 * (2 + 2 * (1 + s) ** 2) * Kk', 'onset709(arb(2), R, arb(1) / 4, Cc, s'])
    R.append('### READ FROM THE SOURCE: n* is the least n >= 1 with')
    R.append('###     2 - (1/4) R^n + C (n + 1)^2 s^n  <  0   (certified, a ball below 0)          [:154-:156, Dm = 2, c = 1/4 from :189]')
    R.append('### where R = |1 - 1/rho_dom| (:167-:168), s = (s1 + R)/2 with s1 = (1 + R)/2 (:170, :179-:180), so s = (1 + 3R)/4, and')
    R.append('### C = 2(2 + 2(1 + s)^2) K (:188). The onset is a CERTIFIED DETECTION INDEX: the first n at which the dominant pair`s modulus term')
    R.append('### (1/4)R^n provably exceeds the on-line background`s bound C(n+1)^2 s^n plus 2. It is not the first sign change of lambda_n. The')
    R.append('### angle theta = arg z is computed (:168) and returned (:190) but enters no line of onset709 (:154 reads R and s alone): the')
    R.append('### definition has no phase in it. The navigator`s "no fixed phase of the turn" is consistent with this definition.')
    R.append('')
    R.append('## (ii) THE REGISTERED LAW AND ITS SUBLEADING TERM')
    R += span('data/b716_registrations.txt', 61, 66, ['r n* = 4 log(4C) + 8 log(n* + 1)', 'r = r(rho) = log |1 - 1/rho', 's = (1 + 3R)/4'])
    R.append('### WRITTEN FROM THE LAW AND THE SOURCE (algebra, no pair): the onset condition is exactly')
    R.append('###     n log(R/s)  >  log(4C) + 2 log(n + 1) + log(1 + 2 / (C (n + 1)^2 s^n)).')
    R.append('### With R = e^r (r = log R, the law`s r(rho), :64) and s = (1 + 3e^r)/4:')
    R.append('###     log s = 3r/4 + 3r^2/32 + O(r^3),   so   4 log(R/s) = r - (3/8) r^2 + O(r^3).')
    R.append('### The law`s first-order form (:63) keeps r and drops the rest: THE SUBLEADING TERM OF THE ON-LINE BACKGROUND is the background`s')
    R.append('### s^n read past first order, -(3/8) r^2 n on the left of the law multiplied by 4, i.e.')
    R.append('###     r n - (3/8) r^2 n + O(r^3 n)  =  4 log(4C) + 8 log(n + 1) + 4 log(1 + 2/(C (n + 1)^2 s^n))   at the onset,')
    R.append('### the last term below 8/(C (n+1)^2 s^n), the constant 2 against a background that is itself ~ R^n/4 there. The onset is the')
    R.append('### least INTEGER past the root, adding a further [0, 1).')
    R.append('')
    R.append('## THE ONE HYPOTHESIS (registered at data/b719_registrations.txt as H-OFFSET, by a commit of its own; computed at no pair this act)')
    R.append('### Let g(n) = r n - 8 log(n + 1) - 4 log(4C), g(n*_pred) = 0 (the law). At the onset g(n*) = (3/8) r^2 n* to this order, and')
    R.append('### g`(n) = r - 8/(n + 1), so')
    R.append('###     n* - n*_pred  =  (3/8) r^2 n* / (r - 8/(n* + 1))  =  (3/8) L / (1 - 8/L`) ,   L = r n*,  L` = r (n* + 1),')
    R.append('### plus the integer step in [0, 1). The offset is the law`s own dropped second-order term: about (3/8) of r(rho) n*, which varies')
    R.append('### with r only through log C and log n*, so it moves little while r(rho) moves 200-fold -- a source for "near 60" that is not a')
    R.append('### wait for a turn; under it -39`s wider spread would sit in L = r n*, through log C and log n*, which this act does not read.')
    R.append('### POST HOC: written after the offsets were seen. Its premise, taken from :64 and not checked here: the law`s r(rho) is log R')
    R.append('### of the tool`s dominant point (:167-:169).')
    R.append('')
    R.append('### ### **(i) READ POST HOC: -39`S SEVEN OFFSETS POSITIVE, +54.9 TO +161.7, FOUR ABOVE 100, NOT "NEAR 60" AS -15 AND Q0`S TEN ;')
    R.append('### (ii) THE ONSET A CERTIFIED DETECTION INDEX WITH NO PHASE IN ITS DEFINITION (tools/b709_pairs.py :154) ; THE SUBLEADING TERM')
    R.append('### -(3/8) r^2 n ; ONE HYPOTHESIS, H-OFFSET, REGISTERED FOR THE NEXT TIER ; NOTHING COMPUTED AT ANY PAIR.**')
    return R


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    R = build()
    if mode == 'bank':
        with open(OUT + '.tmp', 'wb') as fh:
            fh.write((NL.join(R) + NL).encode('utf-8'))
        os.replace(OUT + '.tmp', OUT)
        print('written data/b719_offset_read.txt (%d lines)' % len(R))
    else:
        print(NL.join(R))
