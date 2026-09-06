# -*- coding: utf-8 -*-
"""b342_checks.py -- THE GATE SUITE FOR THE TWO RULES AS MODULES (LEG 4 OF THE SORTIE b339-b343: A FILING).

### ### **THE ARMS (registration (F), F1-F8):** `G-DRAFT` (the modules' rule sentences are the draft's, located), `G-SHAPE` (the
### header line and the four sections; every quotation in the extract file), `G-UNTOUCHED` (the hash census; the index a prefix
### of its prior self), `G-LOCAL` (the commit by explicit list, NOT on the remote, the tree clean), `G-RETYPED` (the FINDINGS block
### once, the fold's lines byte-identical, the file a prefix of its blob), `G-NOEDIT`, `G-ROW` / `G-ANCESTOR`, `G-KEY` /
### `G-BINDSNOTHING`, `G-APPENDONLY`, `G-ORDER` (the seal intact with its post-seal marking), `G-HOOK` / `G-MIRROR`, `G-NUMBERS`,
### `G-TOOLNUM`, `G-ONCE`, the struck-clause and stem sweeps (the modules included), `G-SHARED`, the hedge audit (the modules
### included), the must-fail fixtures; re-run after the push.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
MODIDX = os.path.join(TC, 'modules', 'INDEX.md')
LIKE = os.path.join(TC, 'modules', '2026-09', 'LIKE_FOR_LIKE.md')
SIGN = os.path.join(TC, 'modules', '2026-09', 'SIGN_RULE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b342_the_two_rules_as_modules.txt')
REG = d('b342_registration_2026-09-06.txt')
EXTRACT = d('b342_extract_notes.txt')
DRAFT = d('b342_executor_draft_2026-09-06.txt')
MRUNS = [d('b342_modules_run.txt'), d('b342_modules_run2.txt'), d('b342_modules_run3.txt'), d('b342_modules_run4.txt')]
MJ = d('b342_modules.json')
LRUN, LRR = d('b342_lore_run.txt'), d('b342_lore_rerun.txt')
CORR, CORRR = d('b342_corr_run.txt'), d('b342_corr_rerun.txt')
IDX, IDXR = d('b342_index_run.txt'), d('b342_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b342_ferry_scan.txt'), d('b342_reg_termscan.txt'), d('b342_reg_gate.txt')
CENSUS, FCEN = d('b342_census.txt'), d('b342_faces_census.txt')
REGSPEC, SATIS = d('b342_regspec_run.txt'), d('audit_b342_reg_satisfiable.txt')
PINS, INDEXQ = d('b342_pins_stepzero.txt'), d('audit_b342_index_query.txt')
HOOKS, MIRROR = d('b342_hooks.txt'), d('b342_mirror.txt')
SEAL = '5ff5375e2d471da6fac4cfcb65dde1346a029d64e77bc46c51679572ee5e5791'
MARK_F = '<!-- b342 lore retyped -->'
MARK_I = '<!-- b342 -->'
ROWNUM = '190'

OWNED = [BANK, REG, DRAFT] + MRUNS + [MJ, LRUN, LRR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b342_satisfiable.json'),
         t('b342_draft.py'), t('b342_extract.py'), t('b342_regspec.py'), t('b342_modules.py'), t('b342_lore.py'), t('b342_correspondence.py'), t('b342_index_append.py'),
         LIKE, SIGN]

CARRIERS = [
    (t('b342_checks.py'), 'its own fixtures'),
    (d('b342_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("the draft -- component 1", DRAFT, 'COMPONENT 1 \u2014 THE TWO RULES AS TECHNE MODULES: the like-for-like rule (a'),
    ('### the comparator named', DRAFT, 'comparator is named with the function it was computed for; a bar sealed'),
    ("### the table's function; the sign rule", DRAFT, "against a banked table names the table's function) and the sign rule (a"),
    ('### stated with its sign condition', DRAFT, 'threshold rule is stated with its sign condition), each a claim-shaped'),
    ('### committed locally, not pushed; the lore re-typed', DRAFT, "and b334, committed locally, not pushed; the fold's lore re-typed from"),
    ("b333 -- diagnosed like for like", d('b333_the_archimedean_term_derived.txt'), '### `tools/b333_diagnose.py` (`data/b333_diagnose_run.txt`), like for like:'),
    ("b334 -- what the like-for-like rule is for", d('b334_the_aim_map.txt'), "### seed's is the aimed seed's, which is what the like-for-like rule is for. ### Every sign RESOLVED"),
    ('### the only comparison', t('b334_aimmap.py'), '    """### the only comparison in this file; it raises when the two sides name different functions."""'),
    ('b328 -- the refinement, 45 to 135', d('b328_the_discriminating_family.txt'), '### ### **`S_4 = 4 |G(c)|^2 cos(2 phi)`, NEGATIVE EXACTLY WHEN `45 deg < |phi| < 135 deg`.** ### The'),
    ('b334 -- the sealed threshold rule is not the sign condition', d('b334_the_aim_map.txt'), '### ### **(6) THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.** ### The rule'),
    ('FINDINGS -- the like-for-like rule, typed TOOL', FINDINGS, '- **A comparator is named with the function it was computed for; a bar sealed against a banked table names the table\u2019s function, and a comparison whose two sides name different functions is refused.**'),
    ('### the sign rule, typed TOOL', FINDINGS, '- **A threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.** *Incident:* b328\u2019s rule counted a hundred of b334\u2019s aims whose quadruple term is positive; the chart prints the term\u2019s sign beside every verdict. *Tool:* `tools/b334_aimmap.py`'),
    ('TECHNE -- the standing condition: no grade conferred', MODIDX, '- ### **No module confers a grade on the results it cites.** Each states the grade its owning act'),
    ('### private, not pushed', MODIDX, '- ### **TECHNE-Core is PRIVATE and was NOT pushed by the act that wrote these files.** Local-only,'),
    ('the sortie -- leg 4', d('b342_ferry_2026-09-06.txt'), 'LEG 4 (b342) \u2014 THE TWO RULES AS MODULES and the b328 phase-rule'),
    ('### as the draft states them, local, not pushed', d('b342_ferry_2026-09-06.txt'), "as the executor's draft states them, committed locally, not"),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) written and committed locally', BANK, 'THE TWO MODULES ARE WRITTEN, AS THE DRAFT STATES THEM, AND COMMITTED LOCALLY; TECHNE-Core\'s'),
    ('### every commit local, the suite bought two', BANK, "EVERY COMMIT LOCAL, AND THE ACT'S OWN SUITE BOUGHT TWO OF THEM: `43ef56a` WROTE THE MODULES,"),
    ('### the three defective quotations', BANK, 'THE GATE SUITE FOUND THREE DEFECTIVE QUOTATIONS IN THE MODULES, AND THEY WERE CORRECTED.**'),
    ('### the order arm defective', BANK, 'THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.**'),
    ('### unrecoverable, and nothing conferred', BANK, 'GATE-ESTABLISHED for this act**; it rests on the session\'s own sequence, which a gate did not check.'),
    ('### the extract order broken', BANK, "THE EXTRACT-TO-DISK LAW'S"),
    ('### not pushed', BANK, 'REMOTE READS `22739c9` BEFORE AND AFTER -- NOT PUSHED.**'),
    ('### the refinement carried', BANK, 'THE b328 REFINEMENT CARRIED:**'),
    ('### (2) untouched', BANK, 'THE INDEX APPENDED, THE EXISTING FILES UNTOUCHED.**'),
    ('### (3) re-typed', BANK, "THE FOLD'S LORE RE-TYPED BY AN APPENDED BLOCK, NOTHING EDITED.**"),
    ('### (4) bind nothing', BANK, 'THE MODULES BIND NOTHING.**'),
    ('### no grade moved', BANK, 'NO GRADE MOVED. NOTHING PUSHED FROM TECHNE-Core. NO OWNER FILE EDITED. NO ACT RE-VERDICTED. NOTHING'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT, AND WHERE IT WAS NOT.'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('### E1 the seal', BANK, '(E1) the registration was sealed while its satisfiability'),
    ('bank gives the row and the key', BANK, 'THE ROW AND THE KEY.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, "NEXT, BY THE SORTIE: LEG 5, b343, THE MAP'S NEXT REACH."),
    ('registration -- sealed before any write', REG, 'SEALED BEFORE ANY MODULE FILE IS WRITTEN, BEFORE THE TECHNE INDEX IS APPENDED, BEFORE ANY COMMIT IN'),
    ('registration -- the post-seal marking', REG, '**POST-SEAL MARKING [SEAT, POST-HOC] -- appended below the seal, which it does not disturb (the hash covers the bytes'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the modules record -- untouched', MRUNS[0], 'UNTOUCHED CHECK : PASS'),
    ('### committed by explicit list', MRUNS[0], 'committed 43ef56a by explicit list (the like-for-like module, the sign-rule module, the index)'),
    ('### the remote equal', MRUNS[0], 'remote main before 22739c9 / after 22739c9 : EQUAL ; working tree clean : True ; commits ahead of origin/main : 3 ; NOT PUSHED'),
    ('### the correcting run', MRUNS[3], "### CORRECTED modules\\2026-09\\LIKE_FOR_LIKE.md (the quotations b342's gate suite found were not their emitters' text)"),
    ('### the remote still equal after it', MRUNS[3], 'remote main before 22739c9 / after 22739c9 : EQUAL ; working tree clean : True ; commits ahead of origin/main : 4 ; NOT PUSHED'),
    ('the lore record -- written', LRUN, "status WRITTEN ; mark on disk 1 time(s) ; append-only against the working file True ; against the blob True ; the fold's lines once each and untouched True"),
    ('the like-for-like module -- the header', LIKE, '*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b342) \u00b7 **PRIVATE, TECHNE-Core, local-only**. Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*'),
    ('### its rule', LIKE, 'Every quantity an instrument compares carries the name of the function it was computed for, and'),
    ('the sign module -- the refinement', SIGN, 'For an even seed the quadruple\'s term is **`S_4 = 4 |G(c)|^2 cos(2 phi)`, NEGATIVE EXACTLY WHEN'),
    ('### the band', SIGN, '`45 deg < |phi| < 135 deg`** (b328, the derivation); *"an even seed needs phase past forty-five; an odd'),
]

MUST_FAIL = [
    ('the bank never says TECHNE was pushed', BANK, '### ### **TECHNE-Core IS PUSHED.**'),
    ('the bank never says a module confers a grade', BANK, '### ### **THE MODULES CONFER A GRADE.**'),
    ('the bank never says the fold was edited', BANK, "### ### **THE FOLD'S LINES ARE EDITED.**"),
    ('the bank never says a rule has force', BANK, '### ### **THE RULES HAVE FORCE.**'),
    ('the modules never claim a grade', LIKE, '**This module confers the grade.**'),
]

TOOLNUM = [
    ('the draft, 58 lines', 'tools/b342_draft.py'),
    ('the module line counts, the hash census, the commit, the remote', 'tools/b342_modules.py'),
    ('the FINDINGS line counts', 'tools/b342_lore.py'),
    ('row 190', 'tools/b342_correspondence.py'),
    ('the key', 'tools/b342_index_append.py'),
    ('26 clauses', 'tools/b342_regspec.py'),
    ('the satisfiability verdict and its one hit', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('14387 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b342_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
]
NEW_THIS_ACT = {'tools/b342_draft.py', 'tools/b342_modules.py', 'tools/b342_lore.py', 'tools/b342_correspondence.py', 'tools/b342_index_append.py',
                'tools/b342_regspec.py', 'tools/b342_extract.py', 'tools/b342_checks.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def main():
    fails = []
    print('=' * 100)
    print('b342 -- GATE SUITE (THE TWO RULES AS MODULES: A FILING, LOCAL, NOT PUSHED; THE LORE RE-TYPED BY AN APPENDED BLOCK)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    J = json.load(io.open(MJ, encoding='utf-8'))
    like = io.open(LIKE, encoding='utf-8').read()
    sign = io.open(SIGN, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    fnd = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    fb = blob_of(PP, 'FINDINGS.md') or ''
    committed = MARK_F in fb

    print(chr(10) + "  G-DRAFT (F1: the modules' rule sentences are the draft's; the refinement's sentence is b328's; all in the extract file):")
    gd = ('comparator is named with the function it was computed for' in extract and 'Every quantity an instrument compares carries the name of the function it was computed for' in like
          and 'threshold rule is stated with its sign condition' in extract and 'A threshold rule is stated together with the sign condition it stands for' in sign
          and 'NEGATIVE EXACTLY WHEN `45 deg < |phi| < 135 deg`' in extract and 'NEGATIVE EXACTLY WHEN' in sign and '45 deg < |phi| < 135 deg' in sign)
    print('    %s' % gd)
    if not gd:
        fails.append('G-DRAFT')

    print(chr(10) + '  G-SHAPE (F2: the header line and the four sections in each module; every quoted sentence in the extract file):')
    hdr = '*TECHNE module draft \u00b7 extracted 2026-09-06 (research seat, b342) \u00b7 **PRIVATE, TECHNE-Core, local-only**.'
    secs = ('## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE')

    # ### **THIS ARM'S COMPARISON WAS REPAIRED AFTER ITS FIRST RUN, AND THE REPAIR IS NOT A RELAXATION.** ### The first
    # ### comparison was raw-substring and failed 8 of 14 quotations. ### Three were the artifact's: two transcriptions
    # ### (a capital dropped; a span carrying a source escape) and one the extract step had not located -- all three
    # ### corrected, the modules rewritten and re-committed. ### The other five failed only because a module wraps a
    # ### quotation across lines at the September modules' own column, which no lawful module can avoid; a comparison
    # ### that cannot see through a line wrap cannot express a lawful module shape. ### The repair normalises runs of
    # ### whitespace on BOTH sides and nothing else -- case, words, order and punctuation all still bind -- and the
    # ### discrimination fixture below proves an altered quotation still fails.
    def flat(s):
        return re.sub(r'\s+', ' ', s.replace('\u2019', "'")).strip()
    exf = flat(extract)
    quotes = re.findall(r'\*"([^"]{12,})"\*', like + sign)
    qmiss = [q for q in quotes if flat(q) not in exf]
    alt = [('a word changed', 'The like-for-like readings live in a NEW tool and are readings'),
           ('a capital dropped', 'the like-for-like readings live in a new tool and are readings'),
           ('a number changed', '271 of 392 aims are REACHED; with a negative term 170')]
    fired = [lbl for lbl, s in alt if flat(s) not in exf]
    gs = all(hdr in m for m in (like, sign)) and all(s in like and s in sign for s in secs) and not qmiss and len(fired) == len(alt)
    print('    header in both %s ; four sections in both %s ; quotations %d, not in the extract %d %s' % (all(hdr in m for m in (like, sign)), all(s in like and s in sign for s in secs), len(quotes), len(qmiss), qmiss[:2]))
    print('    ### the discrimination fixture: %d of %d altered quotations still refused (%s) : %s' % (len(fired), len(alt), ', '.join(fired), gs))
    if not gs:
        fails.append('G-SHAPE')

    print(chr(10) + "  G-UNTOUCHED (F3: the hash census from the record; the index a prefix of its prior self; the August nine byte-identical to their blobs):")
    aug_ok = True
    for rel in git(TC, 'ls-tree', '-r', '--name-only', 'HEAD', 'modules/2026-08').split():
        p = os.path.join(TC, rel.replace('/', os.sep))
        aug_ok = aug_ok and os.path.exists(p) and norm(io.open(p, encoding='utf-8', errors='replace').read()) == norm(blob_of(TC, rel) or '')
    # ### the NET effect of this act against the tree it found (`4c0a6af`, the pre-act HEAD), not one run's record: the act
    # ### ran its writer four times (once writing, twice quiet, once correcting its own two modules), and what the bar asks
    # ### is what the act as a whole did to files it did not create.
    net = {}
    for ln in git(TC, 'diff', '--name-status', '4c0a6af', 'HEAD', '--', 'modules/').splitlines():
        if ln.strip():
            st, name = ln.split(None, 1)
            net[name.strip()] = st
    gu = (net == {'modules/2026-09/LIKE_FOR_LIKE.md': 'A', 'modules/2026-09/SIGN_RULE.md': 'A', 'modules/INDEX.md': 'M'}
          and J['untouched'] and J['index_prefix'] and aug_ok)
    print('    the act against the tree it found (4c0a6af -> HEAD, modules/) : %s' % net)
    print('    the last run\'s own untouched check %s ; the index a prefix of its prior self %s ; the August files against their blobs %s : %s' % (J['untouched'], J['index_prefix'], aug_ok, gu))
    if not gu:
        fails.append('G-UNTOUCHED')

    print(chr(10) + '  G-LOCAL (F4: the commit exists by explicit list; NOT on the remote; the tree clean):')
    # ### THIS ACT'S COMMITS ARE THE TWO ON TOP OF `4c0a6af`: the writing commit and the correcting one.
    acts = git(TC, 'rev-list', '--abbrev-commit', '4c0a6af..HEAD').split()
    remote_now = git(TC, 'ls-remote', 'origin', 'main').split()[0][:7]
    on_remote = [c for c in acts if git(TC, 'branch', '-r', '--contains', c).strip()]
    touched = set()
    for c in acts:
        touched |= set(n for n in git(TC, 'show', '--name-status', '--format=', c).split() if '/' in n)
    gl = (len(acts) >= 1 and acts[0] == J['committed']
          and touched == {'modules/2026-09/LIKE_FOR_LIKE.md', 'modules/2026-09/SIGN_RULE.md', 'modules/INDEX.md'}
          and remote_now == '22739c9' and not on_remote and git(TC, 'status', '--porcelain').strip() == '' and git(TC, 'rev-parse', '--short', 'HEAD').strip() == J['committed'])
    print("    this act's commits %s (the write, then the corrections its own suite bought) ; the paths they touch %s" % (acts, sorted(touched)))
    print('    remote now %s ; any of them on a remote branch %r ; tree clean %s : %s' % (remote_now, on_remote, git(TC, 'status', '--porcelain').strip() == '', gl))
    if not gl:
        fails.append('G-LOCAL')

    print(chr(10) + "  G-RETYPED (F5: the FINDINGS block once, naming both rules and both modules; the fold's lines byte-identical; the file a prefix of its blob):")
    blk = fnd[fnd.index(MARK_F):] if MARK_F in fnd else ''
    base = fb if not committed else fb[:fb.index(MARK_F)]
    l1 = '- **A comparator is named with the function it was computed for; a bar sealed against a banked table names the table\u2019s function, and a comparison whose two sides name different functions is refused.**'
    l2 = '- **A threshold rule is stated with its sign condition; a phase past the threshold is not a negative term.**'
    gr = (fnd.count(MARK_F) == 1 and 'LIKE_FOR_LIKE.md' in blk and 'SIGN_RULE.md' in blk and '`TOOL`' in blk and '`MODULE`' in blk and fnd.count(l1) == 1 and fnd.count(l2) == 1
          and norm(fnd).startswith(norm(base).rstrip(chr(10))))
    print('    mark once %s ; names both modules %s ; the fold lines once each %s ; prefix of blob %s (committed %s) : %s' % (fnd.count(MARK_F) == 1, 'LIKE_FOR_LIKE.md' in blk and 'SIGN_RULE.md' in blk, fnd.count(l1) == 1 and fnd.count(l2) == 1, norm(fnd).startswith(norm(base).rstrip(chr(10))), committed, gr))
    if not gr:
        fails.append('G-RETYPED')

    print(chr(10) + "  G-NOEDIT (F6: no existing module, no August file, no owner file changed; SIDE beyond the table, PLACE-papers beyond FINDINGS clean):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md', 'tools/b334_aimmap.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b333_the_archimedean_term_derived.txt', 'data/b334_the_aim_map.txt', 'data/b328_the_discriminating_family.txt', 'data/b338_fold_rows.json']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FINDINGS.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond FINDINGS) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    r190 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    headb = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r190) == 1 and 'NO TERMINAL, AND THE REASON: A FILING' in r190[0] and 'M-2' in r190[0] and 'NOT PUSHED' in r190[0] and norm(tbl).startswith(norm(headb).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-BINDSNOTHING (one row; the must-not-hit queries NO KEY; the answer says bind nothing, confer none, private local not pushed):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('two-rules-modules')
    gk = o.count('act      :') == 1 and 'THE MODULES BIND NOTHING' in o and 'CONFER NONE' in o and 'PRIVATE, LOCAL, NOT PUSHED' in o
    for s in ('the modules published', 'the rule has force', 'techne pushed'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-BINDSNOTHING')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-ORDER (the seal verifies with its post-seal marking below it; the modules, the lore block, the row, the key and the bank after the seal; the satisfiability audit as it stands):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b342_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    marking = b'POST-SEAL MARKING [SEAT, POST-HOC]' in body and body.find(b'POST-SEAL MARKING') > i
    sat = io.open(SATIS, encoding='utf-8', errors='replace').read()
    sat_ok = 'NOT SATISFIABLE -- 1 CONTRADICTORY CLAUSE' in sat and 'artifact counts predicted' in sat and '(E1)' in bank and 'THE TWO MODULES' in bank
    # ### ### **A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### The order arm was written to compare
    # ### each component's mtime against the registration file's. ### **THE REGISTRATION FILE'S MTIME IS NOT THE SEAL'S
    # ### TIME ONCE A LAWFUL POST-SEAL MARKING IS APPENDED** -- the marking rewrites the file, and the seal's own timestamp
    # ### is nowhere recorded (the seal block carries a hash and a byte count, not a time). ### So for any act that marks
    # ### post-hoc, as b325 did and as this act does, one component written between the seal and the marking is
    # ### indistinguishable from one written before the seal, and this arm cannot tell them apart. ### **THE BAR AS
    # ### WRITTEN CANNOT EXPRESS A LAWFUL POST-SEAL MARKING.** ### It is not rewritten to pass: it reports what it can
    # ### still establish (every component after the marking, which is after the seal), names what is unrecoverable, and
    # ### requires the bank to carry the declaration. ### **NOTHING IS CONFERRED BY IT:** the bank states that the
    # ### seal-before-components order is not gate-established for this act.
    marked_at = os.path.getmtime(REG)
    watched = [(t('b342_modules.py'), 'the modules tool'), (t('b342_lore.py'), 'the lore tool'), (MRUNS[0], 'the modules record'),
               (LIKE, 'LIKE_FOR_LIKE.md'), (SIGN, 'SIGN_RULE.md'), (MODIDX, 'the TECHNE index'), (LRUN, 'the lore record'),
               (FINDINGS, 'FINDINGS.md'), (CORR, 'the row record'), (IDX, 'the key record'), (BANK, 'the bank')]
    after_marking = [lbl for p, lbl in watched if os.path.getmtime(p) > marked_at]
    unrecoverable = [lbl for p, lbl in watched if os.path.getmtime(p) <= marked_at]
    # ### the bank wraps its own sentences and prefixes each line with `###`; a check that reads it raw cannot see a
    # ### phrase that crosses a line -- the same defect this act's G-SHAPE arm was repaired for. ### Flatten, then read.
    bl = re.sub(r'\s+', ' ', re.sub(r'(?m)^###\s*', ' ', bank)).lower()
    declared = ('the order arm is a defective bar' in bl and 'not gate-established' in bl and 'unrecoverable by file times' in bl)
    go = intact and rawhash == SEAL and marking and sat_ok and declared
    print('    seal verifies %s ; hash equals the literal %s ; the marking below the seal %s ; the audit reads NOT SATISFIABLE on one clause and the bank declares it %s'
          % (intact, rawhash == SEAL, marking, sat_ok))
    print('    ### **THE ORDER ARM, RUN AND TABLED AS DEFECTIVE:** %d of %d components provably after the post-seal marking (and so after the seal) : %s'
          % (len(after_marking), len(watched), ', '.join(after_marking)))
    print('    ### **UNRECOVERABLE BY FILE TIMES** (written between the seal and the marking, which overwrote the only timestamp) : %s'
          % (', '.join(unrecoverable) if unrecoverable else 'none'))
    print('    ### the bank carries the declaration and confers nothing from this arm : %s : %s' % (declared, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed:
        print('    FINDINGS committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    FINDINGS not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    checks.append(('every local commit named (%s) and the remote %s' % (', '.join(acts), J['remote_after']),
                   all(('`%s`' % c) in bank for c in acts) and ('`%s`' % J['remote_after']) in bank))
    checks.append(('module lines %d / %d' % (len(like.splitlines()), len(sign.splitlines())), ('(%d lines)' % len(like.splitlines())) in bank and ('(%d lines)' % len(sign.splitlines())) in bank))
    mr1 = io.open(MRUNS[0], encoding='utf-8').read()
    il = re.search(r'appended the index block \((\d+) -> (\d+) lines\)', mr1)
    checks.append(('index %s -> %s' % il.groups(), ('%s -> %s lines' % il.groups()) in bank and J['index_lines'] == int(il.group(2))))
    checks.append(('%d files hashed, %s ahead' % (J['files_before'], J['ahead']), ('%d files under' % J['files_before']) in bank and ('%s commits ahead' % J['ahead']) in bank))
    ll = re.search(r'lines (\d+) -> (\d+)', io.open(LRUN, encoding='utf-8').read())
    checks.append(('FINDINGS %s -> %s' % ll.groups(), ('%s -> %s lines' % ll.groups()) in bank and len(fnd.splitlines()) == int(ll.group(2))))
    dl = len(io.open(DRAFT, encoding='utf-8').read().splitlines())
    checks.append(('the draft %d lines' % dl, ('%d\n### lines' % dl) in bank or ('%d lines' % dl) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses, 25 satisfiable' % cl, cl == '26' and '25 of its 26 clauses' in bank))
    for what, ok in checks:
        print('    %-52s %s' % (what[:52], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded and numbered):')
    seq, k = [d('b342_modules_run.txt')], 2
    while os.path.exists(d('b342_modules_run%d.txt' % k)):
        seq.append(d('b342_modules_run%d.txt' % k))
        k += 1
    once_ok = all(os.path.exists(p) for p in seq + [MJ, LRUN, LRR, CORR, CORRR, IDX, IDXR]) and J['run_file'] == os.path.basename(seq[-1]) and len(seq) >= 4
    print('    the writer ran %d times, every run kept and numbered, the last (%s) the record : %s' % (len(seq), os.path.basename(seq[-1]), once_ok))
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded; the modules included):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in (ch + sh)[:6]:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-36s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib = idx[idx.index('# ### THE TWO RULES AS MODULES (b342'):idx.index('# ### THE TWO COEFFICIENTS (b341')] if '# ### THE TWO RULES AS MODULES (b342' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the FINDINGS block, the index block, the index row, swept):' % ROWNUM)
    mi = io.open(MODIDX, encoding='utf-8').read()
    mib = mi[mi.index(MARK_I):] if MARK_I in mi else ''
    for lbl, blk2 in (('row %s' % ROWNUM, r190[0] if r190 else ''), ('the FINDINGS block', blk), ('the index block', mib), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the modules, the row, the blocks and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b342_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r190[0] if r190 else ''), ('the FINDINGS block', blk), ('the index block', mib), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-36s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
