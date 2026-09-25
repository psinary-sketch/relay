# -*- coding: utf-8 -*-
"""b539_anchor.py -- COMPONENT 1: THE ANCHOR TIER, PRINTED FROM A FRESH RUN. ### `python tools/b539_anchor.py run`

### READING (5): one `lake env lean` run, from a scratchpad check file, in SIDE-explicit-formula's tree at 81ae175; each
### anchor's `#print axioms` line (wrapped lines joined) is compared with its bank, and on any difference the tool prints the
### diff and exits 3 -- the act stops. `lake env lean` without `-o` writes no build product. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B539_SCRATCH', '')
NL = chr(10)
B = 'SIDEExplicitFormula.B321.'
R = 'SIDEExplicitFormula.RegisterDepth.'
ANCHORS = [  # name, module, pin, the bank its axiom line is compared with
    (B + 'h2_sign_iff_rh', 'SIDEExplicitFormula/Seam.lean', 'v0.2 = 5c72cad (identical at 81ae175)', 'b536_profile_log.txt'),
    (B + 'ch_iff_rh', 'SIDEExplicitFormula/H2Bridge.lean', '81ae175 (identical at v0.2)', 'b532_profile_log.txt'),
    (R + 'not_register1', 'SIDEExplicitFormula/RegisterDepth.lean', '81ae175', 'b538_profile_log2.txt'),
    (R + 'mellin_Phi_eq_zero_of_re_le_one', 'SIDEExplicitFormula/RegisterDepth.lean', '81ae175', 'b538_profile_log2.txt'),
    (R + 'lvh2_corrected_iff', 'SIDEExplicitFormula/RegisterDepth.lean', '81ae175', 'b538_profile_log2.txt'),
    (R + 'register5_output_holds', 'SIDEExplicitFormula/RegisterDepth.lean', '81ae175', 'b538_profile_log2.txt'),
    (B + 'b321_identity', 'SIDEExplicitFormula/B321Identity.lean', '81ae175 (identical at v0.2)', 'b510_profile_log.txt'),
    (B + 'not_f4_needs', 'SIDEExplicitFormula/RestBound.lean', '81ae175 (identical at v0.2)', 'b530_profile_log.txt')]
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def joined(out):
    raw, res, i = out.replace(chr(13), '').split(NL), [], 0
    while i < len(raw):
        l = raw[i]
        if 'depends on axioms: [' in l:
            while ']' not in l and i + 1 < len(raw):
                i += 1
                l = l.rstrip() + ' ' + raw[i].strip()
        res.append(l.strip())
        i += 1
    return res


def axline(lines, full):
    return next((l for l in lines if l.startswith("'%s' " % full) and ('depends on axioms' in l or 'does not depend' in l)), None)


def checks(out, names):
    """### each `#check @name` output, from its first line to the next `@`-headed or quoted line."""
    lines = out.replace(chr(13), '').split(NL)
    res = {}
    for n in names:
        i = next((k for k, l in enumerate(lines) if l.startswith('@%s :' % n) or l.startswith('%s :' % n)), None)
        if i is None:
            res[n] = None
            continue
        blk = [lines[i]]
        for l in lines[i + 1:]:
            if l.startswith('@') or l.startswith("'") or re.match(r'^[A-Za-z]', l):
                break
            blk.append(l)
        res[n] = ' '.join(' '.join(blk).split())
    return res


def run():
    names = [a[0] for a in ANCHORS]
    src = ['import SIDEExplicitFormula.RegisterDepth', ''] + ['#print axioms ' + n for n in names] + [''] + ['#check @' + n for n in names]
    p = os.path.join(SCR, 'b539_anchor_check.lean')
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    head = subprocess.run(['git', '-C', KER, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    secs = time.time() - t0
    io.open(os.path.join(D, 'b539_anchor_log.txt'), 'w', encoding='utf-8', newline=NL).write(
        '$ lake env lean %s  (cwd SIDE-explicit-formula at %s)%sexit %d ; %.1f s%s--- source ---%s%s%s--- stdout ---%s%s%s--- stderr ---%s%s%s'
        % (p, head, NL, r.returncode, secs, NL, NL, NL.join(src), NL, NL, r.stdout, NL, NL, r.stderr, NL))
    fresh = joined(r.stdout)
    chk = checks(r.stdout, names)
    rows, diffs = [], []
    for n, mod, pin, bank in ANCHORS:
        f = axline(fresh, n)
        b = axline(joined(io.open(os.path.join(D, bank), encoding='utf-8', errors='replace').read()), n)
        rows.append(dict(name=n, module=mod, pin=pin, fresh=f, bank=bank, banked=b, equal=(f is not None and f == b), check=chk.get(n)))
        if not (f is not None and f == b):
            diffs.append(dict(name=n, fresh=f, banked=b))
    res = dict(head=head, exit=r.returncode, seconds=round(secs, 1), rows=rows, diffs=diffs, sorry=('sorryAx' in r.stdout),
               r3='R3 UNDECIDED -- the census row (FINDINGS.md:4787), no theorem decides it')
    io.open(os.path.join(D, 'b539_anchor.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print('  fresh run at SIDE-explicit-formula %s : exit %d ; %.1f s' % (head[:12], r.returncode, secs))
    for x in rows:
        print('  %-60s %s' % (x['name'], 'EQUAL TO ITS BANK' if x['equal'] else '### DIFFERS'))
        print('      fresh : %s' % x['fresh'])
        print('      #check : %s' % (x['check'] or 'NONE')[:300])
    print('  %s' % res['r3'])
    if diffs:
        print('### ### **A FRESH LINE DIFFERS FROM ITS BANK -- THE ACT STOPS HERE.**')
        for d0 in diffs:
            print('    %s%s      fresh : %s%s      bank  : %s' % (d0['name'], NL, d0['fresh'], NL, d0['banked']))
        return 3
    print('  ### ### **EVERY ANCHOR LINE EQUALS ITS BANK : %d of %d.**' % (len(rows), len(rows)))
    return 0


if __name__ == '__main__':
    sys.exit({'run': run}[sys.argv[1]]())
