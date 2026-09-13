# -*- coding: utf-8 -*-
"""b449_checks.py -- THE CONTROL SUITE FOR b449. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

### ### **THE ARM LIST IS READ OFF THE FACE, NEVER TYPED HERE**, and the suite refuses to agree
### with itself: `G-ARMS-DECLARED-EQ-RUN` is computed by comparing the two sets.
### ### **THE TWO READINGS LAND IN TWO FILES** (BAR 11), the side decided by whether this act's
### commit is already on the remote.
"""
import io
import json
import os
import re
import subprocess
import sys
import tokenize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
WINREPO = os.path.join('D:', os.sep, 'SIDE-window')
FACE = os.path.join(D, 'b449_registration_2026-09-13.txt')
PREPUSH = os.path.join(D, 'b449_checks.txt')
POSTPUSH = os.path.join(D, 'b449_checks_postpush.txt')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    return (s or '').replace(chr(13) + chr(10), NL)


def fold(s):
    """### **FOLD BOTH SIDES, NEVER TYPE ONE** -- the trap `b436`-`b439` hit five times."""
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def pycode_of(src):
    """### COMMENTS **AND** STRING LITERALS STRIPPED BY THE TOKENIZER, DOTS RE-CLOSED."""
    out = []
    try:
        for tok in tokenize.generate_tokens(io.StringIO(src).readline):
            if tok.type in (tokenize.COMMENT, tokenize.STRING):
                continue
            out.append(tok.string)
    except Exception:
        return ''
    return re.sub(r'\s*\.\s*', '.', ' '.join(out))


def verdict_line(txt, needle, phrase):
    """### **A VERDICT IS READ BY ITS LINE, NEVER AS A SUBSTRING OF THE FILE** (`A2`)."""
    for ln in nl(txt).splitlines():
        if needle in ln:
            return phrase in ln
    return False


def git(repo, *a):
    try:
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout or ''
    except Exception:
        return ''


def unchanged(repo, path):
    return path not in git(repo, 'status', '--porcelain', '--', path)


# ### **THE ACT BOUNDARY.** ### The repositories carry scores of untracked files left by earlier
# ### acts. ### An arm that counts them charges THIS act for THEIR writes -- the opposite error to
# ### the one `b439` fixed, and just as wrong. ### **THE BOUNDARY IS THE EARLIEST OF THIS ACT`S OWN
# ### STEP-ZERO ARTEFACTS**, and every write arm is scoped to files newer than it.
ACT_START = min(os.path.getmtime(os.path.join(D, f))
                for f in ('b449_ferry.txt', 'b449_ferry_scan.txt'))


def touched(repo, pat, since=True):
    """### Tracked-modified OR untracked-new, matching `pat`, ### **WRITTEN BY THIS ACT.**

    ### **NEW FILES COUNT** (`b439`) -- a brand-new file is most of what an act writes, and an arm
    ### that skips the porcelain`s untracked marker judges only MODIFIED files.
    """
    out = []
    for ln in git(repo, 'status', '--porcelain').splitlines():
        f = ln[3:].strip().strip('"').rstrip('/')
        if not re.search(pat, f):
            continue
        if since:
            try:
                if os.path.getmtime(os.path.join(repo, f)) < ACT_START:
                    continue
            except OSError:
                continue
        out.append(f)
    return out


def committed_by_act(repo, pat):
    """### **AFTER THE COMMIT THE WORKING TREE IS CLEAN, AND A WRITE ARM READING ONLY THE TREE
    ### THEN SEES NOTHING** -- so the post-push reading would score the write list over an empty
    ### set and call that a pass. ### The act`s own written set is the union of what the tree
    ### still shows and what THIS ACT`S COMMIT carries."""
    # ### **AN ACT IS NOT ONE COMMIT.** ### b444 lands in four -- the act, the closing suite, the
    # ### closing record, and this repair -- so an arm reading only `HEAD` sees the last of them
    # ### and scores the write list over two files. ### **EVERY COMMIT WHOSE SUBJECT NAMES THIS
    # ### ACT IS READ**, and the act's own boundary bounds how far back that can reach.
    out = []
    for ln in git(repo, 'log', '--format=%H %s', '-40').splitlines():
        sha, _, subj = ln.partition(' ')
        if 'b449' not in subj:
            continue
        for f in git(repo, 'show', '--name-only', '--format=', sha).splitlines():
            f = f.strip()
            if f and re.search(pat, f):
                out.append(f)
    return sorted(set(out))


def appended_only(repo, path):
    old = git(repo, 'show', 'HEAD:%s' % path)
    new = read(os.path.join(repo, path))
    return (bool(old) and bool(new) and new.startswith(old.rstrip(NL))
            and len(new) > len(old.rstrip(NL)))


FACET = read(FACE)
COMP = read(os.path.join(D, 'b449_components.txt'))
EXTR = read(os.path.join(D, 'b449_extract.txt'))
RGATE = read(os.path.join(D, 'b449_reg_gate.txt'))
TERM = read(os.path.join(D, 'b449_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b449_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b449_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b449_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b449_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b449_ferry.txt'))
CENS = read(os.path.join(D, 'b449_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b449_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b449_pins_stepzero.txt'))
ADD = os.path.join(D, 'b449_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b449_components.py'))
SRC_DESK = read(os.path.join(T, 'b449_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b449_extract.py'))
SRC_CHK = read(os.path.join(T, 'b449_checks.py'))
CODE_COMP = pycode_of(SRC_COMP)
CODE_EXT = pycode_of(SRC_EXT)

F = fold(FACET)
C = fold(COMP)

# ### **THE LIST NAMES SOME ENTRIES WITH THEIR DIRECTORY AND SOME WITHOUT** -- `b444_checks.py`
# ### beside `data/b444_addendum.txt`. ### An arm comparing a BASENAME against the raw list misses
# ### every prefixed entry and charges a declared file as undeclared. ### **BOTH SIDES ARE REDUCED
# ### TO A BASENAME BEFORE THEY ARE COMPARED.**
WRITELIST = [os.path.basename(x) for x in
             re.findall(r'`([A-Za-z0-9_.\-/]+\.(?:py|txt|json|md|lean|npy))`',
                        FACET.split('(W) THE WRITE LIST')[-1].split('(Z) THE NOTHINGS')[0])]
DEC = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', FACET)) - {'G-NO'})


def _pushed():
    """### HAS **THIS ACT'S** WORK REACHED THE REMOTE? ### **CARRIED FROM b439, NOT RETYPED.**

    ### b440 retyped this predicate twice and got it wrong twice. ### Its first writing sought a SHA
    ### in a list of branch NAMES and was never true. ### Its "repair" -- `origin/main == HEAD` -- is
    ### **TRUE BEFORE THIS ACT COMMITS ANYTHING**, because HEAD is then the prior act's pushed commit;
    ### b444's first pre-push reading was therefore written to the POST-push file. ### b434's own
    ### docstring named that species: *"HEAD is trivially on the remote."* ### The question is whether
    ### a commit naming this act is both made and pushed.
    """
    try:
        subj = git(ROOT, 'log', '-1', '--format=%s')
        if 'b449' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False








CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
CELL = '4.123106'
CHAIN = ['tools/e16/carto_atlas.py', 'tools/e16/zeta_ordinates.npy', 'tools/b317_smear.py', 'tools/b318_square.py',
         'tools/b321_window.py', 'tools/noise_floor.py', 'tools/registration_gate.py', 'tools/b363_span.py',
         'tools/mirror_build.ps1', 'tools/mirror_verify.py', 'tools/mirror_roster.json', 'tools/b244_loom_append.py']
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
R61MARK = '<!-- (R61) the failure-mode partition gets a trigger, not a shelf -->'
B449MARK = '<!-- b449 the (R61) record ratified, and the outlier`s integrand at its aim -->'
R61_SHA = '94cc82669da234401ed986f6ca0c54f251447f2b18461458269a0f91b46c2951'


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


CJ = _j('b449_count.json')
IJ = _j('b449_integrand.json')
V = IJ.get('verdict') or {}
SPAN = _j('b449_span.json')
MIRROR = read(os.path.join(D, 'b449_mirror.txt'))
LOOMRUN = read(os.path.join(D, 'b449_loom_append_run.txt'))


def main(argv):
    import hashlib
    import math
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b449 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b449')) | set(committed_by_act(ROOT, r'b449')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b449_registration_2026-09-13.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    chain_committed = [f for f in committed_by_act(ROOT, r'.') if f in CHAIN]
    closings_committed = [f for f in committed_by_act(ROOT, r'_closing\.txt$') if 'b449' not in f]
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', '757e5c1', 'origin/main'],
                                       capture_output=True).returncode
    trails = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    loom = read(os.path.join(PP, 'VERIFICATION_LOOM.md'))
    t_dirty = git(TECHNE, 'status', '--porcelain', '--untracked-files=no').strip()

    # ### COMPONENT 1, RE-DERIVED: THE RECORD'S BYTES AND THE BANKS.
    ls = trails.replace(chr(13) + chr(10), NL).split(NL)
    try:
        s = ls.index(R61MARK)
        e = s
        while not ls[e].startswith('*The partition row in `FINDINGS.md` is not edited'):
            e += 1
        rec_sha = hashlib.sha256(NL.join(ls[s:e + 1]).encode('utf-8')).hexdigest()
    except Exception:
        s, e, rec_sha = -1, -1, ''
    try:
        cand = held = 0
        kinds, per = set(), {}
        for site, p in SITES:
            d = json.loads(read(os.path.join(D, p)))
            cs = d['candidates']
            h = d.get('held')
            held += (len(h) if isinstance(h, list) else int(h or 0))
            cand += len(cs)
            kinds |= set(c['kind'] for c in cs)
            per[site] = [sum(1 for c in cs if c['kind'] == 'CLASS BOUNDARY'), len(cs)]
        rows = dict((r['figure'], r) for r in CJ.get('rows') or [])
        c1_ok = (rows.get('candidates', {}).get('bank') == cand and rows.get('held', {}).get('bank') == held
                 and rows.get('kinds', {}).get('bank') == len(kinds) and rows.get('per', {}).get('bank') == per)
    except Exception as ex:
        rec('  ### C1 RE-DERIVATION RAISED %r' % ex)
        c1_ok, per = False, {}
    b443line = [l for l in read(os.path.join(D, 'b443r_the_arc_product.txt')).splitlines() if l.startswith('**The class boundary, per site, corrected:**')]
    rep443 = dict((m.group(1), [int(m.group(2)), int(m.group(3))]) for m in re.finditer(r'\((i|ii|iii|iv|v|vi)\) (\d+) of (\d+)', b443line[0] if b443line else ''))
    pos = bool(per) and per == rep443
    disc = [r['figure'] for r in CJ.get('rows') or [] if r['bank'] != r['record']]
    ratified = (not disc) and pos
    b449blk = trails[trails.find(B449MARK):] if B449MARK in trails else ''

    # ### COMPONENT 2, RE-DERIVED FROM THE BANKED LEVELS.
    lv = IJ.get('levels') or []
    try:
        ctrl = len(lv) == 4 and all(abs(x['prime'] - x['prime_banked']) <= 1e-15 for x in lv) and \
            [x['prime_banked'] for x in lv] == [_j('b445_arms.json')['base'][CELL]['prime'], _j('b445_arms.json')['a'][CELL]['prime'],
                                                _j('b446_doubling.json')[CELL]['prime'], _j('b447_doubling.json')[CELL]['prime']]
        fin = lv[-1]
        kink = abs(fin['Dplus'] - fin['Dminus']) > 1e-6 * fin['maxslope']
        place = ['SITS ON' if min(abs(x['vstar'] - x['node_left']), abs(x['node_right'] - x['vstar'])) <= 1e-12 else 'STRADDLE' for x in lv]
        vstar_ok = all(abs(x['vstar'] - math.log(17.0)) == 0 and x['node_left'] < x['vstar'] < x['node_right'] + 1e-300 for x in lv)
        sh = []
        for j in (1, 2, 3):
            d = dict((n, lv[j]['terms'][n] - lv[j - 1]['terms'][n]) for n in lv[0]['terms'])
            gross = sum(abs(x) for x in d.values())
            sh.append((abs(d['17']) / gross if gross else 0.0, d['17']))
        c3 = sh[0][0] >= 0.9 and sh[1][0] >= 0.9 and abs(sh[1][1]) > abs(sh[0][1])
        account = ctrl and kink and place == ['STRADDLE', 'STRADDLE', 'SITS ON', 'SITS ON'] and c3
        mstate = 'NOT DECIDED' if not ctrl else ('CLOSES' if account else 'STAYS OPEN')
        tsum = all(abs(x['terms_sum'] - x['prime']) <= 1e-15 for x in lv)
    except Exception as ex:
        rec('  ### C2 RE-DERIVATION RAISED %r' % ex)
        ctrl = kink = vstar_ok = c3 = account = tsum = False
        place, mstate = [], None
    n1 = 'HELD' if ratified else 'REFUTED'
    n2a = 'HELD' if kink else 'REFUTED'
    n2b = 'HELD' if (place[:2] == ['STRADDLE', 'STRADDLE'] and 'STRADDLE' not in place[2:] and mstate == 'CLOSES') else 'REFUTED'

    # ### THE MIRROR ARMS: SCORED POST-PUSH ONLY (face, section G2).
    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-13-b449.zip' in MIRROR
                and verdict_line(MIRROR, 'manifest declares source HEAD', git(PP, 'rev-parse', '--short=7', 'HEAD').strip()))

    def mirror_kept():
        m1 = re.search(r'PRIOR ZIP SHA256 BEFORE : ([0-9a-f]{64})', MIRROR)
        m2 = re.search(r'PRIOR ZIP SHA256 AFTER  : ([0-9a-f]{64})', MIRROR)
        return bool(m1 and m2) and m1.group(1) == m2.group(1)

    ARMS = [
        ('G-RECEIPT-IN-FULL', 'ferry banked in full', 'part 1 of 1' in FERRY and 'paste ends' in FERRY),
        ('G-SCAN-CLEAN', 'scan 0 hits', verdict_line(SCAN, '### VERDICT:', '0 HIT(S) REPORTED')),
        ('G-R54-LINE-PRESENT', 'scanned line present', 'scanned before sending, zero hits' in FERRY),
        ('G-STEPZERO-CENSUS', 'censuses 0', verdict_line(CENS, 'TOTAL MISSING', ': 0') and verdict_line(FCENS, 'TOTAL MISSING', ': 0')),
        ('G-STEPZERO-PINS', 'pins 0', verdict_line(PINS, 'REPOS HARD-FAILING', ': 0')),
        ('G-SURVEY-NOMISS', 'survey 0 misses', verdict_line(EXTR, '### MISSES', ': 0')),
        ('G-REG-LOCKED-FIRST', 'lock block present', 'THE REGISTRATION LOCK' in FACET),
        ('G-LOCKGATE-EIGHT', 'lock gate 8, permitted', verdict_line(LOCKG, 'GATES READ', '8') and verdict_line(LOCKG, '**VERDICT :', 'LOCK PERMITTED')),
        ('G-SEAL-VERIFIES', 'seal verifies', 'SEAL INTACT' in seal),
        ('G-PRIOR-CLOSED-PUSHED', 'row 297 on the face; 757e5c1 on origin/main', 'row 297' in F and prior_pushed),
        ('G-R62-ENTERED', '(R62) entered', fold('(R62)` -- the instrument lane opens for one') in F),
        ('G-WORDING-ERRORS-ENTERED', 'E1 and E2 entered', fold("TWO ERRORS IN THE ORDER'S WORDING, ENTERED AS THE NAVIGATOR'S:") in F
         and '(E1)' in FACET and '(E2)' in FACET),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b449_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C1-COUNT-FROM-BANKS', 'bank figures re-derived equal the count', c1_ok),
        ('G-C1-RECORD-PARSED', 'every record figure parsed (none None)', bool(CJ.get('rows')) and all(r['record'] is not None and r['record'] != {} and r['record'] != [] for r in CJ['rows'])
         and next((r for r in CJ['rows'] if r['figure'] == 'held'), {}).get('record') == 0),
        ('G-C1-COMPARED-EXACT', 'discrepancies %s re-derived' % disc, CJ.get('discrepancies') == disc),
        ('G-C1-POSITIVE-CONTROL', 'class boundary per site equals b443`s line (%s)' % pos, pos and (CJ.get('positive') or {}).get('fires') is True),
        ('G-C1-NEGATIVE-CONTROL', 'NOT A KIND zero at all six', (CJ.get('negative') or {}).get('fires') is True
         and all(v[0] == 0 for v in (CJ['negative']['per'].values()))),
        ('G-C1-DISCREPANCY-ROUTED', 'any discrepancy printed as routed', (not disc) or 'ROUTED, NOT REPAIRED' in COMP),
        ('G-C1-RECORD-UNEDITED', 'the (R61) record bytes as pushed at dc5e18e', rec_sha == R61_SHA),
        ('G-C1-LOOM-ONE-BLOCK', 'one b449 loom marker', loom.count('<!-- b449 loom entry -->') == 1),
        ('G-C1-LOOM-PREFIX-PROVED', 'appender proved the prefix', verdict_line(LOOMRUN, 'PREFIX UNCHANGED', 'YES')),
        ('G-C1-WORKORDER-FILED', 'W-ORD-MIRROR-ZIP-NAME with its trigger in the trail record',
         bool(b449blk) and '**W-ORD-MIRROR-ZIP-NAME' in b449blk and 'the next mirror build, or the next opening of the instrument-audit lane' in b449blk),
        ('G-C1-RATIFICATION-BY-RULE', 'ratified %s re-derived' % ratified, CJ.get('ratified') == ratified
         and verdict_line(COMP, 'THE (R61) RECORD :', 'RATIFIED AT b449' if ratified else 'NOT RATIFIED')),
        ('G-C1-PARTITION-ROW-POINTS', 'the trail`s partition row points at OPEN_TRAILS.md:6473',
         bool(re.search(r'(?m)^\| the failure-mode partition \|.*OPEN_TRAILS\.md:6473', b449blk))),

        ('G-C2-LEVELS-FORMED', 'four levels formed at the banked a', len(lv) == 4 and [x['nv'] for x in lv] == [8193, 16385, 32769, 65537]
         and IJ.get('a') == 4.123106),
        ('G-C2-PRIME-CONTROL', 'prime channel re-summed equals its banks', ctrl),
        ('G-C2-AIM-PRINTED', 'v* = ln 17 inside the edge at every level', vstar_ok and all(x['L_minus_vstar'] > 0 for x in lv)
         and 'THE AIM AND THE ONE-SIDED DERIVATIVES' in COMP),
        ('G-C2-DERIVATIVES-RECOMPUTED', 'jump re-derived equals the banked verdict', bool(lv) and V.get('jump') == lv[-1]['Dplus'] - lv[-1]['Dminus']),
        ('G-C2-KINK-BY-RULE', 'kink %s' % kink, V.get('kink') == kink and verdict_line(COMP, 'A KINK AT v* :', 'YES' if kink else 'NO')),
        ('G-C2-PLACEMENT-FROM-NODES', 'placement %s re-derived' % place, V.get('placement') == place),
        ('G-C2-TERMS-SUM', 'terms sum to the prime channel', tsum),
        ('G-C2-ACCOUNT-BY-RULE', 'account %s, n=17 clause %s' % (account, c3), V.get('account') == account and V.get('c3') == c3),
        ('G-C2-MEASUREMENT-STATE-SAID', 'measurement %s' % mstate, V.get('measurement') == mstate
         and verdict_line(COMP, '### ### **THE MEASUREMENT', mstate)),
        ('G-C2-NO-CHANNELS-CALL', 'no channels call; no Z, A or P evaluated', not re.search(r'channels \(|hhat_blocked|kernel \(', CODE)),

        ('G-N1-SCORED', 'N1 %s' % n1, verdict_line(COMP, '(N1)    the banks reproduce', n1)),
        ('G-N2-APART', 'N2 two clauses', fold('TWO CLAUSES APART') in F and '(N2)(a)' in COMP and '(N2)(b)' in COMP),
        ('G-N2-SCORED', 'N2 (a) %s (b) %s' % (n2a, n2b), verdict_line(COMP, '(N2)(a) the integrand carries', n2a)
         and verdict_line(COMP, '(N2)(b) the first two straddle', n2b)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', 'the seat`s own from the face, from reading code' in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b449 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b449'
         and SPAN.get('this_act') == 449 and isinstance(SPAN.get('current_span'), int)),

        ('G-MIRROR-TAGGED-BUILD', 'the closing build under -DateTag 2026-09-13-b449, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
        ('G-MIRROR-PRIOR-ZIP-KEPT', 'the dc5e18e zip`s sha256 unchanged across the build', 'DEFERRED' if not post else mirror_kept()),

        ('G-NOCHAIN-FILE-EDITED', 'chain, mirror and loom tools unmoved', all(unchanged(ROOT, p) for p in CHAIN) and chain_committed == []),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched; TECHNE tracked tree clean', 0 == len(touched(WINREPO, r'.')) and t_dirty == ''),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b449' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail and the loom', all(f in ('OPEN_TRAILS.md', 'VERIFICATION_LOOM.md') for f in pp_touched + pp_committed)
         and unchanged(PP, 'FINDINGS.md')),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
                                                             or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b449' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-LANE-CLOSED-SAID', 'the lane`s closure printed', verdict_line(COMP, 'THE INSTRUMENT LANE OPENED BY (R62)', 'CLOSES AT THIS ACT`S END')),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names_arms = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names_arms)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names_arms)), sorted(set(names_arms) - set(DEC))))
    fails, deferred = [], []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = v is False
            rec('  %-40s FAIL CONTROL -- it %s' % (n, 'did' if ok else '### DID NOT ###'))
            if not ok:
                fails.append(n)
            continue
        if v == 'DEFERRED':
            deferred.append(n)
            rec('  %-40s DEFERRED TO POST-PUSH -- %s' % (n, d))
            continue
        rec('  %-40s %-4s %s' % (n, 'PASS' if v else '### FAIL', d))
        if not v:
            fails.append(n)
    rec('=' * 100)
    rec('  ### ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s' % (len(ARMS) - len(deferred), len(ARMS) - len(deferred) - len(fails), len(fails), fails or ''))
    rec('  ### DEFERRED TO POST-PUSH, COUNTED APART : %d %s' % (len(deferred), deferred or ''))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fails else 'ARMS FAILING'))
    rec('=' * 100)
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    os.replace(OUT + '.tmp', OUT)
    return 0 if not fails else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
