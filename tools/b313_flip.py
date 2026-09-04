# -*- coding: utf-8 -*-
"""b313_flip.py -- THE COPY-MAKER. ### **THE OWNER INSTRUMENT IS NOT EDITED.**

### ### **WHAT IT DOES.** ### It reads three owner files, applies a DECLARED list of substitutions
### to each, and writes a COPY. ### The originals are opened read-only and are never written.

### ### **THE TWO CLASSES OF SUBSTITUTION, KEPT APART BECAUSE THEY ARE NOT THE SAME KIND OF
### ### CHANGE:**
###   ### **`FLIP`** ### -- the one line per file that carries the exponent. ### **THAT IS THE
###     ### ACT.**
###   ### **`IDENTITY`** ### -- the changes a copy needs in order to BE a copy: it names itself, it
###     imports the flipped layer rather than the owner's, and ### **IT WRITES ITS OUTPUT
###     ### SOMEWHERE ELSE, SO THAT RUNNING IT CANNOT OVERWRITE AN OWNER'S BANKED ARTIFACT.**
###   ### **NEITHER CLASS IS HIDDEN: THE UNIFIED DIFF IS PRINTED IN FULL AND EVERY HUNK IN IT MUST
###   ### CORRESPOND TO A DECLARED SUBSTITUTION.**

### ### **AND THE THREE THINGS THAT MAKE THE COPIES TRUSTWORTHY, EACH MEASURED RATHER THAN
### ### ASSERTED:**
###   ### **(i) EXACTLY-ONCE.** ### Every substitution's `old` must occur EXACTLY ONCE in the
###     source. ### A substitution matching twice would silently change something nobody declared;
###     one matching zero times would leave the copy unflipped while the bank said otherwise.
###   ### **(ii) ROUND TRIP.** ### Applying the inverse substitutions to the copy must reproduce
###     the original ### **BYTE FOR BYTE.** ### That is the cheapest proof that the copy machinery
###     itself introduces nothing -- no re-encoding, no line-ending drift, no stray edit.
###   ### **(iii) NOTHING ELSE CHANGED.** ### The diff's changed-line count must equal the declared
###     substitution count.
"""
import difflib
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FLIP = 'FLIP'
IDENT = 'IDENTITY'

FILES = [
    {
        'name': 'qeps_layer',
        'src': os.path.join(E16, 'qeps_layer.py'),
        'dst': os.path.join(E16, 'b313f_qeps_layer.py'),
        'subs': [
            (FLIP,
             'out[k] = float((lam2 / (1 - lam2) * (r ** -0.5) * I).sum())',
             'out[k] = float((lam2 / (1 - lam2) * (r ** 0.5) * I).sum())',
             "THE FLIP. ### `eps`'s scaling exponent -- the ONE constituent b312 found differing "
             "between the corpus's remainder and the source's. ### **WRITTEN AS A WHOLE LINE, "
             "BECAUSE THE FRAGMENT `(r ** 0.5)` ALREADY OCCURS IN `Qeps` AND THE INVERSE WOULD "
             "NOT BE UNIQUELY LOCATABLE -- WHICH THE ROUND-TRIP CONTROL CAUGHT.**"),
            (IDENT,
             'via (85) with theta(a)f(x) = a^{1/2} f(x/a).',
             'via (85) with theta(a)f(x) = a^{-1/2} f(x/a).',
             "the docstring must not describe a convention the code no longer carries. ### **A "
             "COPY THAT LIES ABOUT ITSELF IS WORSE THAN NO COPY.**"),
            (IDENT,
             '"""Q_eps AND THE OPERATOR LAYER',
             '"""b313 FLIPPED COPY (NOT AN OWNER FILE) -- Q_eps AND THE OPERATOR LAYER',
             "the copy names itself in its first line so it cannot be read as the owner."),
        ],
    },
    {
        'name': 'b38_act10',
        'src': os.path.join(E16, 'b38_act10.py'),
        'dst': os.path.join(E16, 'b313f_b38_act10.py'),
        'subs': [
            (FLIP,
             'out[:, k] = lam2 / (1 - lam2) * (r ** -0.5) * I',
             'out[:, k] = lam2 / (1 - lam2) * (r ** 0.5) * I',
             "THE FLIP. ### `per_mode_eps_grids` -- the remainder AS THE IDENTITY CONSUMES IT. "
             "### Written as a whole line for the same reason."),
            (IDENT,
             'import qeps_layer as Q',
             'import b313f_qeps_layer as Q',
             "the copy must consume the FLIPPED layer, or its `eps_full` and its per-mode grids "
             "would carry two different conventions and the mask-algebra gate would fire."),
            (IDENT,
             r'BANK = r"D:\relay\data\b38_2026-08-18.txt"',
             r'BANK = r"D:\relay\data\b313f_b38_scratch.txt"',
             "### **SO THAT RUNNING THE COPY CANNOT OVERWRITE THE OWNER'S BANKED TABLE.** ### The "
             "copy's `main` is not called by this act, and the redirection is what makes that a "
             "safety property rather than a promise."),
            (IDENT,
             '"""W-CONSTRUCTION-1 act 10',
             '"""b313 FLIPPED COPY (NOT AN OWNER FILE) -- W-CONSTRUCTION-1 act 10',
             "the copy names itself in its first line."),
        ],
    },
    {
        'name': 'b264_eps_decay',
        'src': os.path.join(E16, 'b264_eps_decay.py'),
        'dst': os.path.join(E16, 'b313f_b264_eps_decay.py'),
        'subs': [
            (FLIP,
             'return lam2 / (1 - lam2) * (r ** -0.5) * I',
             'return lam2 / (1 - lam2) * (r ** 0.5) * I',
             "THE FLIP. ### `eps_modes` -- b264's own configurable-node evaluator, which is the "
             "one the ladder runs through. ### Written as a whole line for the same reason."),
            (IDENT,
             '[lam^2/(1-lam^2)] rho^{-1/2} INT',
             '[lam^2/(1-lam^2)] rho^{+1/2} INT',
             "the docstring must not describe a convention the code no longer carries."),
            (IDENT,
             r"BANK = r'D:\relay\data\b264_run.txt'",
             r"BANK = r'D:\relay\data\b313f_b264_scratch.txt'",
             "so that running the copy cannot overwrite b264's banked run."),
            (IDENT,
             r"ROWS = r'D:\relay\data\b264_rows.json'",
             r"ROWS = r'D:\relay\data\b313f_b264_rows.json'",
             "so that running the copy cannot overwrite b264's banked rows -- which this act READS "
             "as the reference column."),
            (IDENT,
             r"CACHE = r'D:\relay\data\b264_cache.npz'",
             r"CACHE = r'D:\relay\data\b313f_b264_cache.npz'",
             "so that running the copy cannot overwrite b264's cache."),
            (IDENT,
             '"""b264_eps_decay.py',
             '"""b313 FLIPPED COPY (NOT AN OWNER FILE) -- b264_eps_decay.py',
             "the copy names itself in its first line."),
        ],
    },
]

# ### ### **WHAT THE COPY OF THE DECAY TOOL DELIBERATELY DOES *NOT* CHANGE, DECLARED HERE BECAUSE
# ### ### A READER WILL ASK:** ### it still imports the OWNER's `qeps_layer` and the OWNER's
# ### `b38_act10`. ### That is correct and not an oversight: the ladder path uses them only for
# ### `layer()` (the prolate eigensolver, which the exponent does not touch) and for the constants
# ### `EPS_NG` and `EPS_NQ` (node counts). ### **THE EXPONENT DOES NOT REACH EITHER, AND POINTING
# ### THE COPY AT A FLIPPED LAYER WOULD HAVE CHANGED THE NODE COUNTS' PROVENANCE FOR NOTHING.**


def read(path):
    return io.open(path, encoding='utf-8', newline='').read()


def apply_subs(text, subs, inverse=False):
    """### **RETURNS (new_text, [(kind, old, new, count)]).** ### `count` is the number of
    ### occurrences found; the caller refuses anything that is not exactly one."""
    rows = []
    out = text
    for kind, old, new, _why in subs:
        a, b = (new, old) if inverse else (old, new)
        n = out.count(a)
        rows.append((kind, a, b, n))
        if n == 1:
            out = out.replace(a, b)
    return out, rows


def diff(src_text, dst_text, src_name, dst_name):
    return list(difflib.unified_diff(src_text.splitlines(True), dst_text.splitlines(True),
                                     fromfile=src_name, tofile=dst_name, n=1))


def changed_lines(dlines):
    """### Lines the diff actually changes, counting a `-`/`+` pair as one change."""
    minus = [x for x in dlines if x.startswith('-') and not x.startswith('---')]
    plus = [x for x in dlines if x.startswith('+') and not x.startswith('+++')]
    return len(minus), len(plus)


def self_test():
    # ### ### **THE FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT A FAILURE**, or it is a control
    # ### that cannot fire -- b308's finding, applied here.
    ok = []
    subs = [(FLIP, 'AAA', 'BBB', 'why')]
    t, rows = apply_subs('x AAA y', subs)
    ok.append(t == 'x BBB y' and rows[0][3] == 1)
    # ### an `old` occurring twice is REPORTED and NOT applied.
    t2, rows2 = apply_subs('AAA AAA', subs)
    ok.append(rows2[0][3] == 2 and t2 == 'AAA AAA')
    # ### an `old` occurring zero times is REPORTED and NOT applied.
    t3, rows3 = apply_subs('nothing', subs)
    ok.append(rows3[0][3] == 0 and t3 == 'nothing')
    # ### the round trip is exact.
    back, _ = apply_subs(t, subs, inverse=True)
    ok.append(back == 'x AAA y')
    # ### the diff counter sees one change and not two.
    m, p = changed_lines(diff('a\nAAA\nb\n', 'a\nBBB\nb\n', 'x', 'y'))
    ok.append((m, p) == (1, 1))
    # ### and it sees NO change where there is none.
    m0, p0 = changed_lines(diff('a\n', 'a\n', 'x', 'y'))
    ok.append((m0, p0) == (0, 0))
    return all(ok), ok


def build(write=True, verbose=True):
    """### **BUILDS EVERY COPY AND RETURNS (ok, report_lines).**"""
    out, allok = [], True

    def rec(s):
        out.append(s)
        if verbose:
            print(s)

    good, arms = self_test()
    rec('  ### THE COPY-MAKER\'S OWN FIXTURES, RUN BEFORE IT TOUCHES A FILE : %s  %s'
        % (arms, 'PASS' if good else '### FAIL ###'))
    rec('  ### **ARMS 2 AND 3 ARE THE ONES THAT MATTER: A SUBSTITUTION MATCHING TWICE, OR NOT AT')
    rec('  ### ALL, IS REPORTED AND REFUSED RATHER THAN APPLIED.**')
    if not good:
        return False, out

    for spec in FILES:
        src = read(spec['src'])
        dst, rows = apply_subs(src, spec['subs'])
        rec('')
        rec('  ' + '-' * 96)
        rec('  ### %s  ->  %s' % (os.path.basename(spec['src']), os.path.basename(spec['dst'])))
        rec('  ' + '-' * 96)
        bad = [r for r in rows if r[3] != 1]
        for (kind, a, b, n), (_k, _o, _nn, why) in zip(rows, spec['subs']):
            rec('    [%-8s] occurrences=%d  %s' % (kind, n, 'OK' if n == 1 else '### REFUSED ###'))
            rec('       - %s' % a.strip()[:92])
            rec('       + %s' % b.strip()[:92])
            rec('       ### %s' % why)
        if bad:
            allok = False
            rec('    ### ### **REFUSING TO WRITE THIS COPY: %d SUBSTITUTION(S) DID NOT MATCH'
                ' EXACTLY ONCE.**' % len(bad))
            continue

        # ### (ii) THE ROUND TRIP, BEFORE THE COPY IS TRUSTED FOR ANYTHING.
        back, _ = apply_subs(dst, spec['subs'], inverse=True)
        rt = (back == src)
        rec('    ### ROUND TRIP -- the inverse substitutions reproduce the original BYTE FOR')
        rec('    ### BYTE : %s  %s' % (rt, 'PASS' if rt else '### FAIL ###'))
        if not rt:
            allok = False

        # ### (iii) NOTHING ELSE CHANGED.
        dl = diff(src, dst, 'a/' + os.path.basename(spec['src']),
                  'b/' + os.path.basename(spec['dst']))
        m, p = changed_lines(dl)
        want = len(spec['subs'])
        rec('    ### THE DIFF: %d line(s) removed, %d added; declared substitutions %d ; '
            'MATCH : %s  %s' % (m, p, want, m == p == want,
                                'PASS' if m == p == want else '### FAIL ###'))
        if not (m == p == want):
            allok = False
        rec('    ### THE UNIFIED DIFF, PRINTED IN FULL:')
        for ln in dl:
            rec('      | %s' % ln.rstrip('\n'))

        if not (rt and m == p == want):
            rec('    ### ### **REFUSING TO WRITE THIS COPY: A CONTROL FAILED.** ### A copy that')
            rec('    ### cannot be inverted back to its original, or that changes a line nobody')
            rec('    ### declared, is not a copy of anything.')
            continue
        if write:
            open(spec['dst'] + '.tmp', 'wb').write(dst.encode('utf-8'))
            os.replace(spec['dst'] + '.tmp', spec['dst'])
            back2 = read(spec['dst'])
            same = (back2 == dst)
            rec('    ### WRITTEN AND READ BACK : %s  %s'
                % (same, 'PASS' if same else '### FAIL ###'))
            if not same:
                allok = False
    return allok, out


def main(argv):
    print('=' * 100)
    print('b313_flip.py -- THE COPY-MAKER. ### THE OWNER INSTRUMENT IS NOT EDITED.')
    print('=' * 100)
    ok, _ = build(write=True, verbose=True)
    print()
    print('  ### ### **ALL COPIES BUILT AND VERIFIED : %s**' % ok)
    print('  ### **AND WHAT THIS TOOL DOES NOT CLAIM: ### IT DOES NOT CLAIM THE FLIP IS RIGHT.**')
    print('  ### The flip is licensed by the source\'s own definition, quoted in the bank; this')
    print('  ### tool only guarantees that the copy differs from the owner in exactly the declared')
    print('  ### places and in no others.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
