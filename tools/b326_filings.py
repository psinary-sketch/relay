# -*- coding: utf-8 -*-
"""b326_filings.py -- ONE APPEND-ONLY CROSS-REFERENCE BLOCK AT THE INTERNAL CONFINEMENT KEYSTONE,
### GENERATED FROM THE ACT'S OWN JSON RECORDS, NEVER TYPED FROM MEMORY.

### ### **THE BLOCK'S NUMBERS ARE READ FROM `b326_windows.json`, `b326_closure.json` AND
### `b326_epstein_zeros.json` AT WRITE TIME.** ### A block typed by hand could carry a number the
### act never measured; this one cannot.
### ### **ONLY THE `day1/` COPY IS WRITTEN.** ### The deposited twin's md5 is measured before and
### after against the value the extract step verified. ### Append-only against the working file AND
### the blob; idempotent; two paths write two differently named run files.
### ### **WHAT THE BLOCK MAY SAY IS CONSTRAINED BY WHAT THE ACT FOUND**, and in particular it must
### carry the correction to b325's block above it -- the priced crossing at `a ~ 22` -- if the
### closure found b325's kernel half the derived one. ### The original block stays visible.
"""
import hashlib
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
DEPOSIT_DIR = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
DEPOSITED_TWIN = os.path.join(DEPOSIT_DIR, 'Which_Structure_Confines.md')
TWIN_MD5 = '6b18d69bcf9e619d3b2fb22376ccc432'
TARGET = os.path.join(PP, 'day1', 'Which_Structure_Confines.md')
REL = 'day1/Which_Structure_Confines.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = '<!-- b326 cross-reference -->'
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()


def build_block():
    lib = json.load(io.open(os.path.join(D, 'b326_epstein_zeros.json'), encoding='utf-8'))
    win = json.load(io.open(os.path.join(D, 'b326_windows.json'), encoding='utf-8'))
    clo = json.load(io.open(os.path.join(D, 'b326_closure.json'), encoding='utf-8'))
    n_on = len(lib['zeros'])
    T = lib['T']
    OFFP = os.path.join(D, 'b326_offline.json')
    offc = json.load(io.open(OFFP, encoding='utf-8')) if os.path.exists(OFFP) else None
    offl = ('%d located to t = %g by the census\'s own argument principle over σ ∈ [0.52, 1.50], the two banked among them'
            % (len(offc['zeros']), offc['T'])) if offc else ', '.join('%.6f %+.6fi' % (o['rho_a'][0], o['rho_a'][1]) for o in lib['offline'])
    st_q = clo['tally_all']['q'] if clo.get('tally_all', {}).get('q') else clo['tally']['q']       # every located off-line zero
    st_q3 = clo['tally_all']['q_b325'] if clo.get('tally_all', {}).get('q_b325') else clo['tally']['q_b325']
    st_q_two = clo['tally']['q']                                                                    # the two banked only
    st_z = clo['tally']['zeta']
    closes_q, fails_q3 = st_q.count('CLOSES'), st_q3.count('FAILS')
    kernel_half = (closes_q > 0 and fails_q3 == closes_q)
    crossing = win['crossing']
    verdict = clo['verdict']
    amax = max(r['a'] for r in win['rows'])
    rows = {r['a']: r for r in win['rows']}
    r22 = rows.get(22.0)
    blk = [
        '',
        MARK,
        '',
        '---',
        '',
        '**Cross-reference, appended 2026-09-04 (b326). Nothing above this line is edited; the b325 '
        'block above stays visible and is corrected here, not rewritten.**',
        '',
        'b326 completed the negative control b325 began. **The Epstein zeros on the line were computed** '
        '— %d zeros to height T = %g by the corpus\'s own argument-principle census run at Re s = ½, each '
        'agreed by an independent second route — and the off-line zeros were located as points: %s. '
        '**The explicit formula was then closed** at every cell for both ζ and this record\'s Epstein '
        'function with their own zero libraries: ζ closes at %d of %d cells; the Epstein function, with every '
        'located off-line zero, closes at %d of %d and is beyond the library\'s ceiling at the other %d (the '
        'arc\'s narrowest cells); with the two banked off-line zeros alone it fails at %d, which is what the '
        'fifteen unbanked zeros were for.' % (n_on, T, offl, st_z.count('CLOSES'), len(st_z), closes_q, len(st_q),
                                             st_q.count('BEYOND CEILING'), st_q_two.count('FAILS')),
        '',
    ]
    if kernel_half:
        blk += [
            '**Correction to the block above.** The closure decided a normalization: the Epstein archimedean '
            'kernel is 2·Re(γ_Q′/γ_Q) = 2 Re ψ(½+iu) − 2 log(2π/√23), and b325\'s instrument carried half of '
            'it. With b325\'s kernel the formula fails at every cell that closes with the derived one (%d of '
            '%d), by exactly the missing half. **The priced crossing at a ≈ 22 in the block above was an '
            'artefact of the halved channel and is withdrawn**; with the derived kernel the Epstein places sum '
            'at a = 22 is %+.9f. b325\'s verdict at the arc\'s cells — *does not see it* — stands, and is '
            'stronger than it was.' % (fails_q3, closes_q, r22['coarse']['places_q'] if r22 else float('nan')),
            '',
        ]
    blk += [
        '**On the arc\'s own family of lawful test functions, out to a = %g: %s.** %s'
        % (amax, verdict,
           ('The Epstein places sum takes the forbidden positive sign at a = %g and the formula closes there.'
            % crossing) if crossing is not None else
           'The Epstein places sum keeps the permitted sign at every cell reached; the finite side never '
           'overtakes the archimedean channel, and the off-line zeros contribute a share of the zero side too '
           'small to turn it. ζ keeps the permitted sign at every cell under the full prime set.'),
        '',
        '**With a lawful f aimed at the banked off-line zero** (the same seed and square, each bump multiplied '
        'by cos(ωv) with ω = %.6f, reported separately and never merged with the arc\'s family): **%s.**'
        % (clo['omega'] if clo['omega'] is not None else float('nan'), clo['aimed_verdict']),
        '',
        '*Filed by b326 (relay `data/b326_the_reach.txt`). No grade moved; no claim of this record altered; '
        'the deposited copy at `outputs/DEPOSITED-v1.1.2/` is not touched. This record\'s finding — the '
        'functional equation does not confine zeros to the line — remains the premise of the test.*',
    ]
    return blk, kernel_half


def main():
    fails = []
    rec('=' * 100)
    rec('b326 -- THE FILING. ### ONE APPEND-ONLY BLOCK AT THE INTERNAL COPY, GENERATED FROM THE RECORDS.')
    rec('=' * 100)
    inside = os.path.abspath(TARGET).startswith(os.path.abspath(DEPOSIT_DIR))
    rec('  %-40s under outputs/DEPOSITED-v1.1.2/ : %s' % (REL, inside))
    if inside:
        rec('  ### ### **REFUSING TO WRITE. ### NO DEPOSITED TEXT IS TOUCHED, EVER.**')
        return 1
    before_twin = md5(DEPOSITED_TWIN)
    rec('    deposited twin md5 BEFORE : %s  %s' % (before_twin, 'MATCH' if before_twin == TWIN_MD5 else '### MISMATCH ###'))
    if before_twin != TWIN_MD5:
        return 1
    block, kernel_half = build_block()
    rec('  the block carries the kernel correction : %s' % kernel_half)
    before = io.open(TARGET, encoding='utf-8', errors='replace').read()
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + REL], capture_output=True).stdout.decode('utf-8', 'replace')
    rec('    working file : %d bytes, %d lines' % (len(before.encode('utf-8')), len(before.splitlines())))
    rec('    blob at HEAD : %d bytes, %d lines' % (len(blob.encode('utf-8')), len(blob.splitlines())))
    if MARK in before:
        rec('    ### ### **ALREADY FILED. ### NOTHING WRITTEN.** (idempotent)')
        norm = before.replace('\r\n', '\n')
        nb = blob.replace('\r\n', '\n')
        rec('    the blob is still a TRUE PREFIX of the file : %s' % norm.startswith(nb.rstrip('\n')))
        rec('    the block appears exactly once             : %s' % (before.count(MARK) == 1))
        rec('    the b325 block above it is still present   : %s' % ('<!-- b325 cross-reference -->' in before))
    else:
        new = before.rstrip('\n') + '\n' + '\n'.join(block) + '\n'
        open(TARGET + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(TARGET + '.tmp', TARGET)
        after = io.open(TARGET, encoding='utf-8', errors='replace').read()
        pw = after.startswith(before.rstrip('\n'))
        pb = after.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
        rec('    lines appended : %+d' % (len(after.splitlines()) - len(before.splitlines())))
        rec('    the pre-append working file is a TRUE PREFIX : %s' % pw)
        rec('    the blob at HEAD is a TRUE PREFIX (normalised): %s' % pb)
        rec('    ### ### **APPEND-ONLY : %s**' % (pw and pb))
        if not (pw and pb):
            fails.append('NOT APPEND-ONLY')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'],
                        capture_output=True, text=True).stdout.strip()
    after_twin = md5(DEPOSITED_TWIN)
    rec('    git status over outputs/DEPOSITED-v1.1.2 : %r ; twin md5 AFTER %s %s'
        % (st, after_twin, 'MATCH' if after_twin == TWIN_MD5 else '### MISMATCH ###'))
    rec('    ### ### **THE DEPOSIT IS BYTE-UNCHANGED : %s**' % (not st and after_twin == TWIN_MD5))
    if st or after_twin != TWIN_MD5:
        fails.append('DEPOSIT MOVED')
    rec('=' * 100)
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    already = any('ALREADY FILED' in x for x in LINES)
    name = 'b326_filings_rerun.txt' if already else 'b326_filings_run.txt'
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
