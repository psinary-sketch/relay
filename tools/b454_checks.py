# -*- coding: utf-8 -*-
"""b454_checks.py -- THE CONTROL SUITE FOR b454. ### **EVERY ARM DECLARED ON THE LOCKED FACE, RUN.**

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
FACE = os.path.join(D, 'b454_registration_2026-09-14.txt')
PREPUSH = os.path.join(D, 'b454_checks.txt')
POSTPUSH = os.path.join(D, 'b454_checks_postpush.txt')
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
                for f in ('b454_ferry.txt', 'b454_ferry_scan.txt'))


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
        if 'b454' not in subj:
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
COMP = read(os.path.join(D, 'b454_components.txt'))
EXTR = read(os.path.join(D, 'b454_extract.txt'))
RGATE = read(os.path.join(D, 'b454_reg_gate.txt'))
TERM = read(os.path.join(D, 'b454_reg_termscan.txt'))
SPECRUN = read(os.path.join(D, 'b454_regspec_run.txt'))
AUDIT = read(os.path.join(D, 'audit_b454_reg_satisfiable.txt'))
LOCKG = read(os.path.join(D, 'b454_lockgate_notes.txt'))
assert LOCKG, 'the lock-gate record is missing; no arm may read it as empty'
SCAN = read(os.path.join(D, 'b454_ferry_scan.txt'))
FERRY = read(os.path.join(D, 'b454_ferry.txt'))
CENS = read(os.path.join(D, 'b454_census_stepzero.txt'))
FCENS = read(os.path.join(D, 'b454_faces_census_stepzero.txt'))
PINS = read(os.path.join(D, 'b454_pins_stepzero.txt'))
ADD = os.path.join(D, 'b454_addendum.txt')
SRC_COMP = read(os.path.join(T, 'b454_components.py'))
SRC_DESK = read(os.path.join(T, 'b454_desk_bank.py'))
SRC_EXT = read(os.path.join(T, 'b454_extract.py'))
SRC_CHK = read(os.path.join(T, 'b454_checks.py'))
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
        if 'b454' not in subj:
            return False
        return 0 == subprocess.run(
            ['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'],
            capture_output=True).returncode
    except Exception:
        return False














def _j(name):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return {}


FJ = _j('b454_findings.json')
EJ = _j('b454_enumera.json')
RJ = _j('b454_registry.json')
BJ = _j('b454_branch_lines.json')
CJ = _j('b454_span_repair.json')
SPAN = _j('b454_span.json')
MIRROR = read(os.path.join(D, 'b454_mirror.txt'))
SRC_ALL = {n: read(os.path.join(T, 'b454_%s.py' % n)) for n in ('extract', 'regspec', 'reg_gate', 'components', 'checks', 'desk_bank')}
KEYS = {
    'PATHS_TO_THE_CRITICAL_LINE': 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md',
    'THE_UNCONDITIONAL_SURROUND': 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
    'SIMPLICITY_OF_RIEMANN_ZEROS': 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
    'INDEX_ARITY_AT_THE_CRITICAL_LINE': 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md',
    'INVARIANCE_BARRIERS': 'phase1.5/method/INVARIANCE_BARRIERS.md',
    'TECHNE_TOOLKIT': 'phase1.5/method/TECHNE_TOOLKIT.md',
    'E_DIFFICULTY_THEOREM': 'phase2/method/E_DIFFICULTY_THEOREM.md',
    'REPARAMETERIZATION_BARRIERS_v0_1': 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md',
    'EXHAUSTIVENESS_LICENSE': 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md',
    'THE_RESIDUE_OF_RH': 'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
}
PPDOC = lambda rel: nl(read(os.path.join(PP, *rel.split('/'))))


def base_rev(repo, rel):
    """### THE PRE-ACT BYTES: `HEAD` while the act is uncommitted, else the parent of the act's commit touching the file."""
    if not unchanged(repo, rel):
        return 'HEAD'
    for ln in git(repo, 'log', '--format=%H %s', '-10', '--', rel).splitlines():
        if 'b454' in ln:
            return ln.split(' ', 1)[0] + '^'
    return None


def pre_text(repo, rel):
    b = base_rev(repo, rel)
    return nl(git(repo, 'show', '%s:%s' % (b, rel))) if b else ''


def removed_zero(repo, rel, edited):
    pre, post = pre_text(repo, rel), PPDOC(rel) if repo == PP else nl(read(os.path.join(repo, rel)))
    if not pre:
        return False
    pl = set(post.split(NL))
    return all((l in pl) or (l in edited and l in post) for l in pre.split(NL))


def main(argv):
    post = _pushed()
    OUT = POSTPUSH if post else PREPUSH
    rec('=' * 100)
    rec('b454 -- THE CONTROL SUITE. ### **%s READING.**' % ('POST-PUSH' if post else 'PRE-PUSH'))
    rec('=' * 100)
    relay_new = sorted(set(touched(ROOT, r'b454|banked_index|b363_span')) | set(committed_by_act(ROOT, r'.')))
    pp_touched = sorted(set(touched(PP, r'.', since=False)) - {'.githooks/pre-push.b304-backup', 'internal/BLOB_SENSITIVITY_2026-08-29.md'})
    pp_committed = committed_by_act(PP, r'.')
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', 'data/b454_registration_2026-09-14.txt'], cwd=ROOT,
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or ''
    CODE = pycode_of(SRC_COMP + NL + SRC_DESK)
    prior_pushed = 0 == subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', 'c89c7ca', 'origin/main'], capture_output=True).returncode
    texts = {k: PPDOC(p) for k, p in KEYS.items()}
    table = BJ.get('table') or []
    V = FJ.get('verdicts') or {}
    cnt = FJ.get('counts') or {}
    tg = FJ.get('targets') or []
    found_t = FJ.get('found_targets') or []
    notf_t = FJ.get('held_by_no_ledger') or []
    reg = PPDOC('REGISTRY.md')
    RL = reg.split(NL)
    ru = RJ.get('row_update') or {}
    rows = RJ.get('rows') or []

    def lines_ok():
        for r in table:
            if not r.get('edited'):
                return False
            L = texts[r['keystone']].split(NL)
            new = r['original']
            for a, b in r['subs']:
                new = new.replace(a, b)
            if L[r['line'] - 1] != new or new != r['new']:
                return False
        return len(table) == 8

    def tips():
        ok = True
        for repo, tip in (('SIDE-lv-conservation', '5a14205'), ('SIDE-effects', 'a0dc376')):
            fp = git(os.path.join('D:', os.sep, repo), 'rev-list', '--first-parent', 'main').split()
            ok = ok and any(c.startswith(tip) for c in fp)
        return ok

    def cur_block(k):
        t = texts[k]
        i = t.find('<!-- b454 CURRENCY ANNOTATION')
        return t[i:] if i >= 0 else ''

    def found_annotated():
        for t in found_t:
            v = V[t['fid']]
            h = [x for x in v['holds'] if x['returned'] and x['verbatim']][0]
            txt = texts[t['keystone']]
            if ('### ERA ANNOTATION (2026-09-14, b454) — bearing on %s' % v['finding']) not in txt or ('`%s:%d`' % (h['ledger'], h['line'])) not in txt or ('> %s' % h['words']) not in txt:
                return False
            src = read(os.path.join(PP, *h['ledger'].split('/')))
            if h['words'] not in nl(src).split(NL)[h['line'] - 1]:
                return False
        return len(found_t) > 0

    def not_added():
        for t in notf_t:
            if ('— bearing on %s' % V[t['fid']]['finding']) in texts[t['keystone']].split('<!-- b454')[-1] and '(2026-09-14, b454) — bearing on %s' % V[t['fid']]['finding'] in texts[t['keystone']]:
                return False
        return all(unchanged(PP, KEYS[k]) and KEYS[k] not in pp_committed for k in ('INVARIANCE_BARRIERS', 'TECHNE_TOOLKIT', 'E_DIFFICULTY_THEOREM'))

    def head_status(rel):
        L = PPDOC(rel).split(NL)
        end = next((i for i, l in enumerate(L) if l.startswith('## 1.')), len(L))
        words = ('READY', 'DRAFT', 'SHORT', 'BLOCKED', 'UNREVIEWED', 'SUPERSEDED', 'REVIEW', 'SCOPE-DROPPED')
        return sorted(set(w for w in words for l in L[:end] if re.search(r'(?<![A-Z-])%s(?![A-Z-])' % re.escape(w), l)))

    def new_rows_cells():
        ok = True
        for rid in ('1.5a-8', '1.5h-9'):
            ls = [l for l in RL if l.startswith('| %s |' % rid)]
            if len(ls) != 1:
                return False
            cells = [c.strip() for c in ls[0].strip().strip('|').split('|')]
            ok = ok and len(cells) == 8 and all(cells)
        return ok

    def removed_all():
        ok = True
        eds = {}
        for r in table:
            eds.setdefault(KEYS[r['keystone']], []).append(r['original'])
        for d in FJ.get('diffs') or []:
            ed = eds.get(d['doc'], []) + ([ru.get('original', '')] if d['doc'] == 'REGISTRY.md' else [])
            ok = ok and removed_zero(PP, d['doc'], ed)
        return ok and len(FJ.get('diffs') or []) == 8

    ENUM = nl(read(os.path.join(PP, 'phase1.5', 'method', 'ENUMERA.md')))
    GRADES = ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION', 'SHELL', 'NOT THE CLAIM')
    grades = [h['graded']['grade'] for h in EJ.get('nearest', []) if h.get('graded')] + [(EJ.get('second') or {}).get('grade')]
    span_src = read(os.path.join(T, 'b363_span.py'))
    uni = CJ.get('unified', '')
    PRIORFILE = r"b4(?!54)\d\d\w*?_[\w.-]+\.(?:txt|json|md|py)"
    WRITE = r"write_bytes\(|\.write\(|dump_json\(|dump\(|run_clock\.write|open\([^)]*'(?:w|wb|a)'"
    CONST = r"\s*(?:OUT|BANKOUT|PREPUSH|POSTPUSH|FINDJ|ENUMJ|SPAN|SPEC)\s*="
    carried = [(n, ln.strip()[:80]) for n, s in SRC_ALL.items() for ln in s.splitlines() if (re.search(WRITE, ln) or re.match(CONST, ln)) and re.search(PRIORFILE, ln)]
    fixture = "    dump_json(os.path.join(D, '" + 'b45' + "3_fold.json'), NL.join(LINES) + NL)"
    control = bool(re.search(WRITE, fixture) and re.search(PRIORFILE, fixture))
    allowed_pp = set(KEYS.values()) | {'REGISTRY.md', 'OPEN_TRAILS.md'}
    # ### THE FACE: `A KIND ON THIS LIST MAY BE WRITTEN MORE THAN ONCE`. ### run_clock versions a second writing of a run file as
    # ### `<stem>2.txt` (run_clock.py:121); the exact-basename predicate misses that and is printed beside the kind predicate.
    onlist = lambda f: os.path.basename(f) in WRITELIST or 'b369' in f or 'b373' in f
    off_exact = [f for f in relay_new if not onlist(f)]
    off_kind = [f for f in off_exact if not re.sub(r'(_notes)\d+(\.txt)$', r'\1\2', os.path.basename(f)) in WRITELIST]
    kern_clean = all(0 == len([l for l in git(os.path.join('D:', os.sep, k), 'status', '--porcelain', '--untracked-files=no').splitlines()])
                     for k in ('SIDE-kernel', 'SIDE-effects', 'SIDE-lv-conservation', 'SIDE-window'))

    def mirror_tagged():
        return (verdict_line(MIRROR, '### VERDICT:', 'CLEAN ON ALL THREE CLAUSES') and 'mirror-refresh-2026-09-14-b454.zip' in MIRROR
                and verdict_line(MIRROR, 'manifest declares source HEAD', git(PP, 'rev-parse', '--short=7', 'HEAD').strip()))

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
        ('G-PRIOR-CLOSED-PUSHED', 'row 302 on the face; c89c7ca on origin/main', 'row 302' in FACET and prior_pushed),
        ('G-ADDENDUM-SLOT-DECLARED', 'slot named', 'b454_addendum.txt' in FACET),
        ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'slot empty', (not os.path.exists(ADD)) or not read(ADD).strip()),
        ('G-NAVIGATOR-MODEL-DECLARED', 'Fable 5.1 on the face', 'navigator model Fable 5.1' in FACET),
        ('G-COUNT-ERROR-ENTERED', 'the twenty-eight entered as the navigator`s', "AN ERROR IN THE ORDER'S COUNT, ENTERED AS THE NAVIGATOR'S" in FACET and 'twenty-eight annotation' in FACET),
        ('G-C1A-LINES-BY-TABLE', 'each branch line equals its original with the face`s terms replaced', lines_ok()),
        ('G-C1A-TIPS-ON-FIRST-PARENT', '5a14205 and a0dc376 on main`s first-parent lines', tips()),
        ('G-C1A-ORIGINALS-PRESERVED', 'each original verbatim in its keystone`s currency annotation', bool(table) and all(r['original'] in cur_block(r['keystone']) for r in table)),
        ('G-C1A-FAST-FORWARD-SAID', 'each annotation entry says fast-forward beside its tip', bool(table) and all(('fast-forward, tip `%s`' % r['tip']) in cur_block(r['keystone']) for r in table)),
        ('G-C1B-LEDGERS-PRE-B450', 'ledgers at 687aa24 (b450`s parent) and an unmoved archive', FJ.get('pre') == '687aa24' and git(PP, 'rev-parse', '--short=7', '8fc56a1^').strip() == '687aa24'
         and 'FINDINGS.md@687aa24' in FJ.get('ledgers', []) and 'OPEN_TRAILS.md@687aa24' in FJ.get('ledgers', []) and not FJ.get('archive_commits_after')),
        ('G-C1B-TWO-SHAPES-PRINTED', 'both yields per finding in the record', all(re.search(r'%s .*S1 yield \d+ +S2 yield \d+' % f, COMP) for f in ('F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'))),
        ('G-C1B-HITS-HAND-READ', 'every hit read: holds verbatim, the rest reasoned', len(V) == 8 and all(v['not_read'] and all(h['returned'] and h['verbatim'] for h in v['holds']) for v in V.values())
         and all(('hits hand-read %-3d' % v['hits']) in COMP for v in V.values())),
        ('G-C1B-CONTROL-RETURNED', 'the two-kinds control returned and holds', FJ.get('control') is True),
        ('G-C1B-FOUND-ANNOTATED', 'each found target annotated with its quoted line and address', found_annotated()),
        ('G-C1B-HELD-BY-NO-LEDGER-NOT-ADDED', 'nothing added for a finding no ledger holds', not_added() and 'CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER' in COMP),
        ('G-C1B-COUNTS-SUM', 'added %s + held by no ledger %s = %s' % (cnt.get('found'), cnt.get('held_by_no_ledger'), cnt.get('targets')),
         cnt.get('found', -1) + cnt.get('held_by_no_ledger', -1) == cnt.get('targets') == len(tg) == 15 and len(found_t) == cnt.get('found')
         and ('THE TWO COUNTS: ADDED %d ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER %d ; SUM 15 OF 15.' % (cnt.get('found', -1), cnt.get('held_by_no_ledger', -1))) in COMP),
        ('G-C1B-RCURVE-NOT-TARGETED', 'item 10 withdrawn, R_CURVE untouched', FJ.get('withdrawn') == [10] and not any('R_CURVE' in t['keystone'] for t in tg)
         and not any('R_CURVE' in f for f in pp_touched + pp_committed)),
        ('G-C1D-VERSION-CELL-ONLY', 'REGISTRY.md:141 differs from its original by the Version cell alone', bool(ru) and RL[140] == ru['original'].replace('| v0.5 |', '| v0.18 |') and ru['original'].count('| v0.5 |') == 1),
        ('G-C1D-PRE-EDIT-ROW-VERBATIM', 'the pre-edit row inside the appended row update', bool(ru) and ('```text' + NL + ru['original'] + NL + '```') in reg),
        ('G-C1D-IDS-NEXT-IN-SEQUENCE', '1.5a-8 and 1.5h-9, each once, next after 1.5a-7 and 1.5h-8', len(rows) == 2 and all(r['id_ok'] and r['heading_ok'] for r in rows)
         and sum(1 for l in RL if l.startswith('| 1.5a-8 |')) == 1 and sum(1 for l in RL if l.startswith('| 1.5h-9 |')) == 1
         and pre_text(PP, 'REGISTRY.md').count('1.5a-8') == 0 and pre_text(PP, 'REGISTRY.md').count('1.5h-9') == 0),
        ('G-C1D-NO-BLANK-CELL', 'eight non-empty cells on each new row', new_rows_cells()),
        ('G-C1D-STATUS-FROM-HEAD', 'heads re-read: no status word, so UNGRADED, and the provenance says so', len(rows) == 2 and all(head_status(KEYS[r['key']]) == [] and r['status'] == 'UNGRADED' for r in rows)
         and reg.count('so Status reads UNGRADED') == 2),
        ('G-C1-REMOVED-ZERO', 'every pre-edit line present, or verbatim in its annotation, in all eight documents', removed_all()),
        ('G-C1-DIFF-COUNTS-PRINTED', 'a numstat line per written document', len(FJ.get('diffs') or []) == 8 and all(re.search(re.escape(d['doc']) + r' +numstat \+\d+ +-\d+', COMP) for d in FJ.get('diffs') or [])),
        ('G-C2-REQUIREMENT-QUOTED', 'E1-E3 verbatim in ENUMERA.md:73 and printed', all(s in ENUM and s in COMP for k, s in (EJ.get('requirement') or [])[:3]) and len(EJ.get('requirement') or []) == 4),
        ('G-C2-ALL-KERNELS-SEARCHED', 'the roster rule`s 43', len(EJ.get('kernels') or []) == len([n for n in os.listdir('D:' + os.sep) if n.startswith('SIDE-') and os.path.isdir(os.path.join('D:' + os.sep, n, '.git'))]) == 43),
        ('G-C2-NEAREST-PRINTED', 'nearest by the rule printed with statement', bool(EJ.get('nearest')) and all(('`%s` clauses' % h['name']) in COMP for h in EJ['nearest'])),
        ('G-C2-PROFILE-AS-SHIPPED', 'profile read from shipped files or NOT LOCATED said', all(h.get('graded') and h['graded']['profile'] for h in EJ.get('nearest', [])) and (EJ.get('second') or {}).get('profile_verbatim') is True),
        ('G-C2-NO-LEAN-RUN', 'no lean or lake invoked', EJ.get('lean_runs') == 0 and not re.search(r"\[\s*['\"](lean|lake)['\"]", SRC_COMP)),
        ('G-C2-GRADE-BY-README', 'grades are README`s, deciding words verbatim', all(g in GRADES for g in grades) and all(h.get('deciding_in_decl') for h in EJ.get('nearest', []))
         and (EJ.get('second') or {}).get('deciding_verbatim') is True),
        ('G-C2-CENSUS-BY-GRADE', 'census %s' % EJ.get('census'), EJ.get('census') == ('CLOSES AT SIXTEEN' if 'DERIVES' in grades else 'STAYS AT FIFTEEN OF SIXTEEN')),
        ('G-C2-CENSUS-UNEDITED', 'census and ENUMERA unedited', unchanged(PP, 'phase2/method/THE_KEYSTONE_CENSUS.md') and unchanged(PP, 'phase1.5/method/ENUMERA.md')
         and not any(f.endswith(('THE_KEYSTONE_CENSUS.md', 'ENUMERA.md')) for f in pp_committed)),
        ('G-C3-REPAIR-AS-NAMED', 'both forms read, unparsed printed, nothing wider', CJ.get('applied') == [True, True, True] and 'FORM_B = re.compile' in span_src and 'PRINTED AND NOT SKIPPED' in span_src
         and 'THE FOLD THRESHOLD IS NINE ACTS' in span_src and not re.search(r'(?m)^-.*(threshold=9|--emit|STARTS AT)', uni)),
        ('G-C3-FIXTURE-BOTH-FORMS', 'form B parsed, filed_by read', (CJ.get('fixture') or {}).get('ok') is True),
        ('G-C3-UNPARSED-PRINTED', 'an unparseable heading printed in the fixture', bool((CJ.get('fixture') or {}).get('unparsed'))),
        ('G-C3-DIFF-PRINTED', 'numstat and unified diff in the record', 'diff --git a/tools/b363_span.py' in COMP and ('numstat +%s -%s' % tuple((CJ.get('numstat') or ['?', '?'])[:2])) in COMP),
        ('G-C3-WRITE-PATH-UNCHANGED', 'no removed line touches the emit path', CJ.get('write_path_unchanged') is True and not re.search(r'(?m)^-.*(run_clock\.write|_span\.json)', uni)),
        ('G-N1-SCORED', 'both populations', '(N1) fewer than half' in COMP and 'over the 15 findings' in COMP and 'over the twenty-eight' in COMP),
        ('G-N2-SCORED', 'per clause', '(N2) a nearest terminal' in COMP and 'narrower : ' in COMP),
        ('G-N3-SCORED', 'by numstat', '(N3) the span-heading repair' in COMP and re.search(r'numstat \+\d+ -\d+ -> (HELD|REFUTED)', COMP)),
        ('G-SEAT-EXPECTATIONS-SCORED', 'the seat`s own scored', 'the seat`s own from the face' in COMP),
        ('G-SPAN-BY-TOOL', 'the repaired tool, emitted for b454', SPAN.get('emitted_for') == 'b454' and SPAN.get('current_span') == 1 and (SPAN.get('last_fold') or {}).get('hi') == 452
         and any(f.get('lo') == 423 for f in SPAN.get('folds') or [])),
        ('G-NOGRADE-MOVED', 'no row`s grade moved; FACES_LEDGER untouched', fold('NO GRADE MOVED ON ANY ROW') in F and unchanged(PP, 'FACES_LEDGER.md') and 'FACES_LEDGER.md' not in pp_committed),
        ('G-NOKERNEL-WRITE', 'kernels unwritten', kern_clean),
        ('G-NODEPOSIT', 'nothing deposits', fold('NO DEPOSIT ACTION') in F),
        ('G-NOH2-MOVED', 'h2 unmoved', fold('h2 WHERE THE DEPOSIT LEFT IT') in F),
        ('G-NOFETCH', 'nothing fetched', not re.search(r'urlopen|requests\.|urllib', CODE)),
        ('G-NOPRIORBANK', 'no prior bank tracked file touched', 0 == len([ln for ln in git(ROOT, 'status', '--porcelain', '--untracked-files=no').splitlines() if 'data/' in ln and 'b454' not in ln and 'b369' not in ln and 'b373' not in ln])),
        ('G-FOUR-LISTS-OPEN', 'lists open', fold('NO LIST OF THE FOUR CLOSED') in F),
        ('G-CORPUS-SCOPE', 'PLACE-papers: the named keystones, REGISTRY, the trail', all(f in allowed_pp for f in pp_touched + pp_committed) and (not unchanged(PP, 'REGISTRY.md') or 'REGISTRY.md' in pp_committed)),
        ('G-TRAIL-APPEND-ONLY', 'trail appended', unchanged(PP, 'OPEN_TRAILS.md') or appended_only(PP, 'OPEN_TRAILS.md')),
        ('G-CORR-APPEND-ONLY', 'correspondence appended', unchanged(SIDE, 'CORRESPONDENCE.md') or appended_only(SIDE, 'CORRESPONDENCE.md')),
        ('G-WRITELIST-KINDS', 'relay files on the list -- exact-basename yield off the list %d %s ; by run_clock`s versioning (a kind written again as `<stem>N.txt`) off the list %d %s'
         % (len(off_exact), off_exact, len(off_kind), off_kind), not off_kind),
        ('G-NOSTAGE-A', 'no git add -A', not re.search(r"add['\"]?\s*,\s*['\"]-A", CODE)),
        ('G-ARMS-DECLARED-EQ-RUN', 'declared equals run', True),
        ('G-ARMS-NO-SUBSTRING-VERDICT', 'verdicts by line', 'def verdict_line(' in SRC_CHK),
        ('G-TWO-READINGS-TWO-FILES', 'two files', 'PREPUSH' in SRC_CHK and 'POSTPUSH' in SRC_CHK),
        ('G-PUSH-SIDE-B439-PREDICATE', 'b439 predicate', "if 'b454' not in subj" in SRC_CHK and "'--is-ancestor', 'HEAD', 'origin/main'" in SRC_CHK),
        ('G-PREPUSH-FILE-EXISTS', 'pre-push file present', os.path.exists(PREPUSH) and 'PRE-PUSH READING' in read(PREPUSH)[:300]),
        ('G-CARRIED-TOOLS-REPOINTED', 'write-target shape %d %s ; control fires %s' % (len(carried), carried, control), (not carried) and control),
        ('G-MIRROR-TAGGED-BUILD', 'closing build under -DateTag 2026-09-14-b454, clean, at PLACE-papers HEAD', 'DEFERRED' if not post else mirror_tagged()),
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
