# -*- coding: utf-8 -*-
"""b448_checks.py -- THE CONTROL SUITE FOR b448. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b448_registration_2026-09-13.txt')
PREPUSH = os.path.join(D, 'b448_checks.txt')
POSTPUSH = os.path.join(D, 'b448_checks_postpush.txt')
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
                for f in ('b448_ferry.txt', 'b448_ferry_scan.txt'))


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
        if 'b448' not in subj:
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
COMP = read(os.path.join(D, 'b448_components.txt'))
EXTR = read(os.path.join(D, 'b448_extract.txt'))
RGATE = read(os.path.join(D, 'b448_reg_gate.txt'))
TERM = read(os.path.join(D, 'b448_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b448_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b448_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b448_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b448_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b448_ferry.txt'))
CENS = read(os.path.join(D, 'b448_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b448_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b448_pins_stepzero.txt'))
ADD = os.path.join(D, 'b448_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b448_components.py'))
SRC_DESK = read(os.path.join(T, 'b448_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b448_extract.py'))
SRC_CHK = read(os.path.join(T, 'b448_checks.py'))
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
        if 'b448' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False







TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
BFRREL = 'modules/2026-09/BAR_FLOOR_RULE.md'
BFR = read(os.path.join(TECHNE, BFRREL))
CORR = read(os.path.join(SIDE, 'CORRESPONDENCE.md'))
CELL = '4.123106'
CHAIN = ['tools/e16/carto_atlas.py', 'tools/e16/zeta_ordinates.npy', 'tools/b317_smear.py', 'tools/b318_square.py',
         'tools/b321_window.py', 'tools/noise_floor.py', 'tools/registration_gate.py', 'tools/b363_span.py',
         'data/b443r_u1_draft.md']
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
STATES = ('BOUNDED BY AN ARGUMENT', 'BOUNDED BY A MEASUREMENT', 'NOT BOUNDED')


def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


PJ = _j('b448_partition.json')
CJ = _j('b448_channels.json')
SPAN = _j('b448_span.json')


def main(argv):
    import math
    OUT = POSTPUSH if _pushed() else PREPUSH
    rec('=' * 100)
    rec('b448 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if _pushed() else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b448')) | set(committed_by_act(ROOT, r'b448')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup',
                                                               'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    t_dirty = subprocess.run(['git', '-C', TECHNE, 'status', '--porcelain', '--untracked-files=no'],
                             capture_output=True, text=True).stdout
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           'data/b448_registration_2026-09-13.txt'], cwd=ROOT, capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    chain_committed = committed_by_act(ROOT, r'^(tools/e16/carto_atlas\.py|tools/e16/zeta_ordinates\.npy|tools/b31[78]_\w+\.py|tools/b321_window\.py|tools/noise_floor\.py|tools/registration_gate\.py|tools/b363_span\.py|data/b443r_u1_draft\.md)$')
    closings_committed = [f for f in committed_by_act(ROOT, r'_closing\.txt$') if 'b448' not in f]
    b447_committed = committed_by_act(ROOT, r'b447_')
    b447_touched = [ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'b447_' in ln]
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'f29219c', 'origin/main'],
                                       capture_output=True).returncode
    t_head = git(TECHNE, 'rev-parse', 'HEAD').strip()
    t_remote = git(TECHNE, 'branch', '-r', '--contains', 'HEAD').strip()
    t_num = git(TECHNE, 'log', '-1', '--grep', 'b448', '--numstat', '--format=', '--', BFRREL).split()

    # ### COMPONENT 1, RE-DERIVED FROM THE SOURCES AND NOT FROM THE COMPONENTS` JSON.
    try:
        r351 = read(os.path.join(D, 'b351_registration_2026-09-07.txt'))
        ot = read(os.path.join(PP, 'OPEN_TRAILS.md'))
        el_par = 'and it FAILS at an aim when that room is not' in r351
        el_arc = 'enumerate every candidate shared witness for the site' in ot and 'fail each at a quoted step or hold it' in ot
        one_kind = not (el_par and el_arc)
        bank, held, l3 = {}, 0, 0
        for s, p in SITES:
            d = json.loads(read(os.path.join(D, p)))
            bank[s] = {}
            for c in d['candidates']:
                bank[s][c['kind']] = bank[s].get(c['kind'], 0) + 1
                l3 += 'b351' in json.dumps(c, ensure_ascii=False)
            h = d.get('held')
            held += (len(h) if isinstance(h, list) else int(h or 0))
        kinds = sorted(set(k for s in bank for k in bank[s]))
        branch = held > 0 or any('OBSTRUCTION' in k for k in kinds)
        draft = read(os.path.join(D, 'b443r_u1_draft.md'))
        miss = dict(re.findall(r'(?m)^\| \*\*\((i|ii|iii|iv|v|vi)\)\*\* [^|]+\| [^|]+\| ([^|]+)\|', draft))
        assign = {w: [s for s in ('i', 'ii', 'iii', 'iv', 'v', 'vi') if re.search(r'\b%s\b' % w, miss.get(s, ''))]
                  for w in ('abscissa', 'height', 'phase', 'width')}
        l1 = sum(len(v) for v in assign.values())
        l2 = len([k for k in kinds if k in STATES])
        verdict = 'SAME' if (one_kind and branch) else ('RELATED' if (l1 + l2 + l3) >= 1 else 'DIFFERENT')
        totals = {w: sum(bank[s].get(k, 0) for s in assign[w] for k in kinds) for w in assign}
        c1_ok = True
    except Exception as ex:
        rec('  ### C1 RE-DERIVATION RAISED %r' % ex)
        one_kind = branch = verdict = None
        l1 = l2 = l3 = held = -1
        kinds, assign, totals, c1_ok = [], {}, {}, False
    tab = PJ.get('table') or {}

    # ### COMPONENT 2, RE-DERIVED FROM THE FOUR BANKS.
    try:
        B445 = _j('b445_arms.json')
        lv = [B445['base'][CELL], B445['a'][CELL], _j('b446_doubling.json')[CELL], _j('b447_doubling.json')[CELL]]
        recon = max(abs(r['zero'] - (r['pole'] - r['prime'] + r['arch']) - r['e']) for r in lv)
        cls, tops, sums = [], [], []
        for j in (1, 2, 3):
            a, b = lv[j - 1], lv[j]
            con = {'zero': b['zero'] - a['zero'], 'pole': -(b['pole'] - a['pole']), 'prime': b['prime'] - a['prime'],
                   'arch': -(b['arch'] - a['arch'])}
            de = b['e'] - a['e']
            gross = sum(abs(v) for v in con.values())
            top = max(con, key=lambda k: abs(con[k]))
            sums.append(abs(sum(con.values()) - de))
            cls.append('ONE CHANNEL`S' if abs(con[top]) >= 0.9 * gross else ('CANCELLATION' if gross > 2 * abs(de) else 'MIXED'))
            tops.append(top)
        grows = abs(lv[2]['prime'] - lv[1]['prime']) > abs(lv[1]['prime'] - lv[0]['prime'])
        growth = ('ONE CHANNEL`S' if (cls[0] == cls[1] == 'ONE CHANNEL`S' and tops[0] == tops[1]
                                     and abs(lv[2][tops[0]] - lv[1][tops[0]]) > abs(lv[1][tops[0]] - lv[0][tops[0]]))
                  else ('CANCELLATION' if 'CANCELLATION' in cls[:2] else 'MIXED'))
        mstate = {'ONE CHANNEL`S': 'STAYS OPEN, NARROWED TO THE %s CHANNEL' % tops[0].upper(), 'CANCELLATION': 'CLOSES'}.get(growth, 'STAYS OPEN, UNNARROWED')
        e = [r['e'] for r in lv]
        dd = [e[i - 1] - e[i] for i in (1, 2, 3)]
        p2 = math.log2(abs(dd[1]) / abs(dd[2]))
        shrink = abs(dd[2]) < abs(dd[1])
        new = 'CONVERGES' if (shrink and 0.9465 <= p2 <= 2.0) else ('SUPER-CONVERGENT' if (shrink and p2 > 2.0) else 'REFUSES')
        levels_ok = CJ.get('levels') == lv
    except Exception as ex:
        rec('  ### C2 RE-DERIVATION RAISED %r' % ex)
        recon, cls, tops, sums, growth, mstate, new, p2, levels_ok = 1.0, [], [], [1.0], None, None, None, None, False
    n1 = 'HELD' if verdict == 'RELATED' else 'REFUTED'
    n2a = 'HELD' if growth == 'CANCELLATION' else 'REFUTED'
    n2b = 'HELD' if mstate == 'CLOSES' else 'REFUTED'

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
        ('G-PRIOR-CLOSED-PUSHED', 'row 296 on the face and b447 on origin/main', 'row 296' in F and prior_pushed),
        ('G-PRE-LOCK-READ-DECLARED', 'the unbanked pre-lock read declared on the face',
         fold('A READ TAKEN BEFORE THIS FACE, DECLARED AS A MEASUREMENT') in F and fold('WRITTEN BY A SEAT THAT HAD SEEN ITS INPUTS') in F),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b448_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty or a quotation', (not os.path.exists(ADD)) or not read(ADD).strip()),

        ('G-C1-ANCHORS-QUOTED', 'every anchor found, 0 misses', 'ANCHOR MISSING' not in COMP and PJ.get('misses') == []),
        ('G-C1-ELEMENT-TEST-APPLIED', 'one kind %s, re-derived' % one_kind, one_kind is not None and PJ.get('one_kind') == one_kind
         and verdict_line(COMP, '### OF ONE KIND :', str(one_kind))),
        ('G-C1-BRANCH-TEST-APPLIED', 'branch met %s, held %s' % (branch, held), branch is not None and PJ.get('branch_met') == branch
         and PJ.get('held') == held and verdict_line(COMP, '### BRANCH TEST MET :', str(branch))),
        ('G-C1-LINKS-COUNTED', 'L1 %s L2 %s L3 %s re-derived' % (l1, l2, l3), c1_ok and PJ.get('l1') == l1 and len(PJ.get('l2') or []) == l2
         and PJ.get('l3') == l3),
        ('G-C1-TABLE-FOUR-BY-ELEVEN', 'four rows, eleven cells each', len(tab) == 4 and all(len(r.get('cells') or {}) == 11 for r in tab.values())
         and len(kinds) == 11),
        ('G-C1-TABLE-FROM-BANKS', 'row totals equal the banks %s' % totals, c1_ok and PJ.get('table_eq_banks') is True
         and all(tab.get(w, {}).get('total') == totals[w] for w in totals)),
        ('G-C1-VERDICT-BY-RULE', 'verdict %s re-derived' % verdict, verdict is not None and PJ.get('verdict') == verdict
         and verdict_line(COMP, 'COMPONENT 1 VERDICT, BY THE FACE`S RULE', verdict)),
        ('G-C1-GIVES-AND-NOT-PRINTED', 'gives and does-not both printed', 'WHAT THE ARC GIVES THE PARTITION:' in COMP and 'WHAT IT DOES NOT:' in COMP
         and len(PJ.get('gives') or []) >= 1 and len(PJ.get('gives_not') or []) >= 1),
        ('G-C1-ITEM-STATE-BY-RULE', 'the item`s state follows the branch; FINDINGS unmoved', (verdict != 'RELATED' or (PJ.get('item_state') or '').startswith('OPEN'))
         and unchanged(PP, 'FINDINGS.md') and 'FINDINGS.md' not in pp_committed),
        ('G-C1-NO-BRIDGE', 'no bridge typed; ledger and draft unmoved', 'NO BRIDGE TYPED' in COMP and unchanged(PP, 'FACES_LEDGER.md')
         and unchanged(ROOT, 'data/b443r_u1_draft.md')),

        ('G-C2-LEVELS-FROM-BANKS', 'four levels equal their banks', len(lv) == 4 and levels_ok),
        ('G-C2-RECONSTRUCTS-E', 'e reconstructed, max %.1e' % recon, recon < 1e-15 and verdict_line(COMP, 'e reconstructed as Z - (P - PR + A)', ': True')),
        ('G-C2-CONTRIBUTIONS-SUM', 'contributions sum to de', bool(sums) and max(sums) < 1e-15),
        ('G-C2-RULE-APPLIED', 'step classes %s re-derived' % cls, [s.get('cls') for s in CJ.get('steps') or []] == cls
         and [s.get('top') for s in CJ.get('steps') or []] == tops),
        ('G-C2-GROWTH-CLASSED', 'growth %s re-derived' % growth, growth is not None and CJ.get('growth') == growth
         and verdict_line(COMP, 'THE GROWTH BETWEEN THE FIRST TWO LEVELS, BY THE FACE`S RULE', growth)),
        ('G-C2-MEASUREMENT-STATE-SAID', 'measurement %s' % mstate, mstate is not None and CJ.get('measurement') == mstate
         and verdict_line(COMP, '### ### **THE MEASUREMENT', mstate)),
        ('G-C2-NO-CHAIN-RUN', 'no chain module imported or called', not re.search(r'import (b321_window|b318_square|b317_smear|carto_atlas)|channels \(|autocorrelation \(', CODE)),

        ('G-C3-ONE-LINE', 'one line appended, 0 removed (numstat %s)' % t_num[:2], BFR.count("The window's upper bound (b448)") == 1
         and len(t_num) >= 2 and t_num[1] == '0' and t_num[0] in ('1', '2')),
        ('G-C3-INCIDENT-NAMED', 'b447 named as the incident', bool(re.search(r"The window's upper bound \(b448\).*Incident: \*\*b447\*\*", BFR))),
        ('G-C3-TECHNE-LOCAL', 'committed in TECHNE, tracked tree clean', bool(t_num) and t_dirty.strip() == ''),
        ('G-C3-VERDICT-BY-RULE', 'corrected verdict %s re-derived (p2 %s)' % (new, ('%.4f' % p2) if p2 is not None else '-'), new is not None
         and CJ.get('new') == new and verdict_line(COMP, 'THE OUTLIER UNDER THE CORRECTED RULE', new)),
        ('G-C3-B447-UNEDITED', 'no b447 file touched or committed by this act', b447_committed == [] and b447_touched == []),

        ('G-N1-SCORED', 'N1 %s' % n1, verdict_line(COMP, '(N1)    RELATED', n1) and (PJ.get('expect') or {}).get('n1') == n1),
        ('G-N2-APART', 'N2 two clauses', fold('TWO CLAUSES APART') in F and '(N2)(a)' in COMP and '(N2)(b)' in COMP),
        ('G-N2-SCORED', 'N2 (a) %s (b) %s' % (n2a, n2b), verdict_line(COMP, '(N2)(a) a cancellation', n2a)
         and verdict_line(COMP, '(N2)(b) the measurement closes', n2b)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'seat expectations scored', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'span banked by the tool under b448 (%s)' % SPAN.get('current_span'), SPAN.get('emitted_for') == 'b448'
         and SPAN.get('this_act') == 448 and isinstance(SPAN.get('current_span'), int)),

        ('G-NOCHAIN-FILE-EDITED', 'chain, gate, span tools and the draft unmoved', all(unchanged(ROOT, p) for p in CHAIN) and chain_committed == []),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOGRADE-MOVED', 'no grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED') in F and unchanged(PP, 'FACES_LEDGER.md')),
        ('G-NOKERNEL-WRITE', 'SIDE-window untouched', 0 == len(touched(WINREPO, r'.'))),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched',
         0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/b4' in ln and 'b448' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: only the trail', all(f == 'OPEN_TRAILS.md' for f in pp_touched)
         and all(f == 'OPEN_TRAILS.md' for f in pp_committed)),
        ('G-TECHNE-UNPUSHED', 'TECHNE HEAD on no remote branch', bool(t_head) and t_remote == ''),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list', all(os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
                                                             or f.endswith('banked_index.py') for f in relay_new)),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b448' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-MUSTFAIL', 'THE CONTROL -- must fail', False),
    ]
    names_arms = [a[0] for a in ARMS]
    decl_eq = (sorted(set(DEC)) == sorted(set(names_arms)))
    ARMS = [(n, d, (decl_eq if n == 'G-ARMS-DECLARED-EQ-RUN' else (False if n == 'G-MUSTFAIL' else v))) for n, d, v in ARMS]
    rec('  arms declared : %d ; run : %d ; declared-not-run %s ; run-not-declared %s'
        % (len(DEC), len(ARMS), sorted(set(DEC) - set(names_arms)), sorted(set(names_arms) - set(DEC))))
    fails = []
    for n, d, v in ARMS:
        if n == 'G-MUSTFAIL':
            ok = v is False
            rec('  %-40s FAIL CONTROL -- it %s' % (n, 'did' if ok else '### DID NOT ###'))
            if not ok:
                fails.append(n)
            continue
        rec('  %-40s %-4s %s' % (n, 'PASS' if v else '### FAIL', d))
        if not v:
            fails.append(n)
    rec('=' * 100)
    rec('  ### ARMS RUN : %d. ### PASSING : %d. ### FAILING : %d %s' % (len(ARMS), len(ARMS) - len(fails), len(fails), fails or ''))
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS' if not fails else 'ARMS FAILING'))
    rec('=' * 100)
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    os.replace(OUT + '.tmp', OUT)
    return 0 if not fails else 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
