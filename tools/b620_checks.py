# -*- coding: utf-8 -*-
"""b620_checks.py -- THE SUITE OF b620, UNDER (R230): THE SECOND READER -- THE PACKET BUILT WITHOUT REASONS, GRADES OR ACT NUMBERS; THE
READER RUN IN A FRESH SESSION THE AUTHOR OPENS; THE AGREEMENT RATES BANKED AND THE DISAGREEMENTS LISTED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b620_checks.txt before the push and
### data/b620_checks_postpush.txt after it; `--mid <name>` (a re-run at the hold) writes data/<name> and regenerates nothing. `--prerun`
### (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its counts written to
### data/b620_arms_prerun.txt. ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs), each run's ls-remote
### calls banked per repository beside its output (data/b620_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### The harness is b568's to b619's, carried from tools/b619_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b620's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
### once in its source and that its predicate reads. The no-disclosure needles are built at run time from TECHNE-Core's module documents
### and never printed.
"""
import copy
import fnmatch
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import terminal_table as TT   # noqa: E402,F401
import b616_claims as KC0     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b620_registration_2026-10-04.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PACKET = 'b620_reader_packet'
PFILES = ('00_README.txt', '01_ceiling.txt', '02_substitutions.txt', '03_rows.txt', '04_residue.txt')
PRE = dict(relay='958e574c', pp='ee75fcf', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc',
             'SIDE-spinor': '520abe7a'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '3408ac33'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a7f90da7-bccd-48d0-914d-84e76892ff54/scratchpad'
HOLD_TEXT = ('The reader packet is at data/b620_reader_packet/ and the prompt at data/b620_reader_prompt.txt. Open a fresh Claude Code session on D:, '
             'clear it, paste the prompt led with prose, let the reader write data/b620_reader_answers.txt and close; then answer here that the bank is there.')


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    if 'ls-remote' in a:   # ### OPEN_TRAILS :12703: every ls-remote of the run counted per repository
        KC0.LSR[repo] = KC0.LSR.get(repo, 0) + 1
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def gs(repo, *a):
    return git(repo, *a)[1].strip()


def blob(repo, spec):
    r = subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except OSError:
        return ''


def rd(n):
    return read(os.path.join(D, n))


def jl(n):
    try:
        return json.load(io.open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def cr0(b):
    return (b or b'').replace(b'\r\n', b'\n')


def raw(p):
    try:
        return open(p, 'rb').read()
    except OSError:
        return None


def blob_id(b):
    return hashlib.sha1(b'blob %d\0' % len(b) + b).hexdigest()


def files_of(repo, sha):
    return sorted(x for x in gs(repo, 'show', '--name-only', '--pretty=format:', sha).split(NL) if x.strip())


def iso_epoch(s):
    import calendar
    import time
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    return iso_epoch(m.group(1)) if m else None


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b620')
            and 'data/b620_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section)/[^`\s]+)`', w)))


def untracked(repo, *paths):
    return [l[3:].strip() for l in git(repo, 'status', '--porcelain', '--untracked-files=all', '--', *paths)[1].split(NL) if l.startswith('?? ')]


def written_files(lock_epoch):
    out = set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay']).split(NL) if x.strip())
    out |= set(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], 'HEAD').split(NL) if x.strip())
    for p in untracked(ROOT, 'data', 'tools'):
        try:
            if os.path.getmtime(os.path.join(ROOT, p)) > lock_epoch - 3 * 3600:
                out.add(p)
        except OSError:
            pass
    res = ['relay/' + x for x in out]
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        if repo == PP:
            ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    l = cr0(b).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def sources():
    import b620_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b620_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b620_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b620_ferry.txt'), scan=rd('b620_ferry_scan.txt'), cens=rd('b620_census_stepzero.txt'),
        fcens=rd('b620_faces_census_stepzero.txt'), pins0=rd('b620_pins_stepzero.txt'), procs=rd('b620_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b619_closing.txt'), reads=rd('b620_reads.txt'), branches=rd('b620_branches.txt'), answers=rd('b620_author_answers.txt'),
        prerun=rd('b620_arms_prerun.txt'), defects=rd('b620_defects.txt'),
        pj=jl('b620_packet.json'), key=jl('b620_key.json'), keytxt=rd('b620_key.txt'), prompt=rd('b620_reader_prompt.txt'),
        pfiles={f: read(os.path.join(D, PACKET, f)) for f in PFILES}, ag=jl('b620_agreement.json'), agtxt=rd('b620_agreement.txt'),
        reader=rd('b620_reader_answers.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b619_checks.py', 'b619_record.py', 'b619_census.py', 'b611_claims.py', 'b612_claims.py', 'b613_claims.py', 'b614_claims.py',
                        'b615_claims.py', 'b616_claims.py', 'b616_record.py', 'b604_record.py', 'b602_record.py', 'b560_record.py', 'b566_record.py',
                        'test_chain_page_b596.py', 'chain_page.py', 'g_chain_page.py', 'push_gated.sh', 'banned_terms.py', 'terminal_table.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in REC.CURRENTS},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b620_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b619*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b620_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b620_mustnotexist.txt')), table_changed=None,
        fj=jl('b620_findings.json'), tj=jl('b620_trail.json'), sc=jl('b620_scores.json'), desk=rd('b620_desk_notes.txt'),
        rl=jl('b620_record_lines.json'), PZ=jl('b620_page_zeta.json'), PX=jl('b620_page_chi.json'), arms_c2=rd('b620_page_arms_c2.txt'),
        lsr=None,
        rlog=[l.split(' ', 1) for l in gs(ROOT, 'log', '--format=%h %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = {k: list(v) for k, v in REC.kern_state(list(S['kern_face'])).items()} if S['kern_face'] else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    ptext = NL.join(S['pfiles'].values()) + NL + S['prompt']
    S['ptext'] = ptext
    S['nd_packet'] = R6.nd_hits(ptext, S['nd_sets'])[0]
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b620_', 'audit_b620_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += list(S['pfiles'].values())
    pub += [read(f) for f in tools]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES:
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['keystone_changes'] = sorted(x for x in ch if x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/') or x.startswith('heritage/'))
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S['pp_head'], S['pp_remote'] = gs(PP, 'rev-parse', 'HEAD'), KC0.remote_refs(PP).get('refs/heads/main', '')   # ### read once (OPEN_TRAILS :12703)
    # ### the packet's items recomputed now from the banks and the blobs
    S['subs_now'] = REC.subs_mono() + REC.subs_sieve()
    S['res_now'] = REC.residue()
    S['ceil_now'] = REC.ceiling()
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b620_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b620_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    return X


# ### the act's own predicates
def put(S, k, v):
    S[k] = v
    return S


def oline(S, n):
    ls = S['ot'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def fline(S, n):
    ls = S['find'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def trail(S):
    t = S['ot']
    i = t.find(S['REC'].TRAIL_HEAD)
    return t[i:] if i >= 0 else ''


def procs_ok(S):
    p = S['procs']
    rows = [l for l in p.split(NL) if re.match(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python|tail)\.exe', l)]
    return 'powershell.exe' in p and '### ORPHANS:' in p and '\\v1.0\\' in p and all('### STOPPED BY PID' in l for l in rows) \
        and 'tail' in p.split('### names matched:')[1].split(NL)[0]


def weight_ok(S):
    x = (S['rl'].get('lines') or [{}])[0]
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7404)' in a and 'b619 AT ITS WEIGHT' in a \
        and 'the suite 76 of 76 before the push and 76 of 76 after it' in a and 'the mid-act run 55 of 76 by design' in a \
        and 'Confirmed by the author:' in a and 'not re-pinned' in a and x['line'] > 7404


def packet_banked(S):
    pj = S['pj']
    fl = pj.get('files') or {}
    return bool(fl) and all(hashlib.sha256((S['pfiles'][f].rstrip(NL) + NL).encode('utf-8')).hexdigest() == fl.get(f) for f in PFILES) \
        and hashlib.sha256((S['prompt'].rstrip(NL) + NL).encode('utf-8')).hexdigest() == pj.get('prompt_sha') and pj.get('dry') is False


def packet_alone(S):
    pk = [h for h, s in S['rlog'] if s.startswith("b620 (R230)(2): the reader's packet")]
    return len(pk) == 1 and sorted(files_of(ROOT, pk[0])) == sorted(['data/%s/%s' % (PACKET, f) for f in PFILES] + ['data/b620_reader_prompt.txt'])


def packet_clean(S):
    REC = S['REC']
    rows = S['pfiles']['03_rows.txt']
    seat = [l for f in PFILES for l in S['pfiles'][f].split(NL) if not re.match(r'^  (FIRST WORDING|SECOND WORDING)|^  \S|^    :\d+ ', l)]
    return bool(rows) and not REC.ACT_RE.search(S['ptext']) and not REC.GRADE_RE.search(rows + NL + NL.join(seat)) \
        and not REC.MARK_RE.search(NL.join(S['pfiles'].values()))


def key_covers(S):
    K = S['key']
    ids = set(re.findall(r'^([SRX]\d{3}) -- ', NL.join(S['pfiles'].values()), re.M))
    kid = set(x['id'] for x in (K.get('subs') or []) + (K.get('rows') or []) + (K.get('residue') or []))
    return bool(ids) and ids == kid and len(K.get('subs') or []) == len(S['subs_now']) and len(K.get('residue') or []) == len(S['res_now']) \
        and len(K.get('rows') or []) == 120 and K.get('seed') == S['REC'].SEED


def subs_now_ok(S):
    K = S['key']
    ks = sorted((x['bank'], x['bank_line'], x['was'], x['now']) for x in K.get('subs') or [])
    ns = sorted((x['bank'], x['bank_line'], x['was'], x['now']) for x in S['subs_now'])
    return bool(ns) and ks == ns


def ceiling_ok(S):
    c = S['pfiles']['01_ceiling.txt'].split(NL)
    return bool(S['ceil_now']) and S['ceil_now'][0].startswith('Supportable: *RH reduced to a single located clause') and \
        all(l in c for l in S['ceil_now']) and S['pfiles']['01_ceiling.txt'].count('Supportable: *RH reduced') == 1


def hold_ok(S):
    a = S['answers']
    return HOLD_TEXT in a and 'RESULT (transcript line' in a and re.search(r'### b620 -- THE AUTHOR`S ANSWERS, 1 prompt\(s\)', a) is not None


def reader_ok(S):
    REC = S['REC']
    A = {}
    for l in S['reader'].split(NL):
        m = re.match(r'^\s*([SRX]\d{3})\s*\|\s*([^|]+?)\s*\|', l)
        if m:
            A[m.group(1)] = m.group(2).strip()
    K = S['key']
    ids = [x['id'] for x in (K.get('subs') or []) + (K.get('rows') or []) + (K.get('residue') or [])]
    ok_v = all((i[0] == 'S' and A.get(i) in ('SAME-OBJECT', 'DIFFERENT-OBJECT', 'BEYOND-CEILING')) or (i[0] == 'R' and A.get(i) in REC.GRADES)
               or (i[0] == 'X' and A.get(i) in ('AT', 'BEYOND')) for i in ids)
    return bool(ids) and ok_v


def agreement_now(S):
    """### the rates recomputed now from the reader's bank and the key, against the agreement bank"""
    A = {}
    for l in S['reader'].split(NL):
        m = re.match(r'^\s*([SRX]\d{3})\s*\|\s*([^|]+?)\s*\|', l)
        if m:
            A[m.group(1)] = m.group(2).strip()
    K, AG = S['key'], S['ag']
    def rate(xs):
        return sum(1 for x in xs if A.get(x['id']) == x['seat']) / max(1, len(xs))
    sm = [x for x in K.get('subs') or [] if x['doc'] == 'the monograph']
    ss = [x for x in K.get('subs') or [] if x['doc'] == 'the sieve']
    nd = sum(1 for x in (K.get('subs') or []) + (K.get('rows') or []) + (K.get('residue') or []) if A.get(x['id']) != x['seat'])
    return bool(AG) and abs(rate(sm) - AG.get('r_m', -1)) < 1e-9 and abs(rate(ss) - AG.get('r_s', -1)) < 1e-9 \
        and abs(rate(K.get('rows') or []) - AG.get('r_y', -1)) < 1e-9 and nd == AG.get('n_dis') and '### ### **H54a ' in S['agtxt']


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h54_ok(S, k):
    AG = S['ag']
    want = {'H54a': 'HOLDS' if AG.get('r_m', 0) >= 0.85 and AG.get('r_s', 0) >= 0.80 else 'REFUTED',
            'H54b': 'HOLDS' if any(d['reader'] == 'BEYOND-CEILING' and d['seat'] == 'SAME-OBJECT' for d in AG.get('dis_s') or []) else 'REFUTED',
            'H54c': 'HOLDS' if AG.get('r_y', 0) >= 0.75 else 'REFUTED',
            'H54d': 'HOLDS' if S['nd_packet'] and not any(S['nd_packet'].values()) else 'REFUTED'}[k]
    return bool(AG) and _h(S, k, want)


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def pages_banked(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        if z.get('changed') is True:
            out.append(z.get('rc') == 0 and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256'))
        else:
            out.append(z.get('rc') == 0 and z.get('changed') is False and bool(a) and a == b == c and hashlib.sha256(c).hexdigest() == z.get('sha256'))
    return all(out)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        if z.get('changed') is True:
            c = [h for h, f in S['pp_files'].items() if p in f]
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b620 (R230): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    return all(out) and bool(S['PZ']) and bool(S['PX'])


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The second reader over the monograph’s three editions') \
        and all(x in tail for x in ('**The packet**', '**The keying.**', '**The record line.**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                                    '**Next.**', 'b621'))


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def kernels_untouched(S):
    return all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == '' \
        and 'v0.21' in S['ktags'] and 'v0.22' not in S['ktags'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') \
        and S['lv_dirty'] == '' and len(S['kern_face']) == 5 and S['kern_face'] == S['kern_now']


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


def _mut_pf(S, f, old, new):
    return put(S, 'pfiles', dict(S['pfiles'], **{f: S['pfiles'][f].replace(old, new, 1)}))


READ_NEEDLES = ('OPEN_TRAILS.md @ ee75fcf2', 'README.md @ ee75fcf2', 'data/b606_edition_PLACE.txt @ 958e574c', 'data/b607_edition_PLACE.txt @ 958e574c',
                'data/b608_edition_PLACE.txt @ 958e574c', 'data/b604_edition_FINDINGS_STAND.txt @ 958e574c', 'data/b605_edition_FINDINGS_STAND.txt @ 958e574c',
                'data/b609_edition_FINDINGS_STAND.txt @ 958e574c', 'data/b617_edition_FINDINGS_STAND.txt @ 958e574c', 'data/b609_residue_seed.txt @ 958e574c',
                'data/b610_residue_addendum.txt @ 958e574c', 'data/b614_second_reader_addendum.txt @ 958e574c', 'tools/b616_record.py @ 958e574c',
                'data/b619_closing_push_out.txt @ 3408ac33', 'FINDINGS.md @ ee75fcf2', ':12212 ', ':12542 ', ':12673 ', ':12799 ', ':12801 ', ':11864 ', ':12228 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R230) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 lean.exe  lean x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b619`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b619' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b620 -- x'])),
    ('G-R230-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R230) END' in S['ferry'] and S['ot'].count('**(R230) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R230) ratified', '(R230) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the hold`s one prompt, verbatim, its options and its answer', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('1 prompt(s)', '2 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 3408ac33`s files', lambda S: S['pushout'][0] == ['data/b619_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b619_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b619') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b619'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b619`s suite, record tool and census module, the six synthesis acts` claims modules, b616`s record tool, the shared record tools, the control`s test file, the generator, its arm, the push gate, the scanner and the table generator against 958e574c',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 20,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b613_claims.py': (S['inst']['b613_claims.py'][0], (S['inst']['b613_claims.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b619`s weight and the five confirmations', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('the mid-act run 55 of 76 by design', 'x'))),
    ('G-PACKET-BANKED', 'the packet`s five files and the prompt on disk against the packet bank`s sha256 of each', lambda S: packet_banked(S),
     lambda S: _mut_pf(S, '01_ceiling.txt', 'Supportable:', 'Supportable :')),
    ('G-PACKET-ALONE', 'relay`s log since 958e574c: the packet and the prompt in one commit of their own', lambda S: packet_alone(S),
     lambda S: put(S, 'rlog', [[h, s.replace("the reader's packet", 'x')] for h, s in S['rlog']])),
    ('G-PACKET-CLEAN', 'the packet and the prompt read now: no act number; no grade word in the rows or in any line the seat wrote; no mark', lambda S: packet_clean(S),
     lambda S: _mut_pf(S, '03_rows.txt', 'R001 -- ', 'R001 -- (statement-grade) ')),
    ('G-PACKET-NODISCLOSURE', 'the no-disclosure arm run afresh over the packet and the prompt', lambda S: bool(S['nd_packet']) and not any(S['nd_packet'].values()),
     lambda S: put(S, 'nd_packet', dict(S['nd_packet'], method=1))),
    ('G-KEY-COVERS', 'the key against the packet`s item ids and the items recomputed now: every id keyed once, the seed, the counts', lambda S: key_covers(S),
     lambda S: put(S, 'key', dict(S['key'], seed=1))),
    ('G-SUBS-NOW', 'the substitutions extracted afresh from the seven diff banks and the sieve`s blobs against the key`s, pair by pair', lambda S: subs_now_ok(S),
     lambda S: put(S, 'subs_now', S['subs_now'][1:])),
    ('G-CEILING-ONCE', 'the packet`s ceiling file against README :106-:111 at ee75fcf, the sentence once', lambda S: ceiling_ok(S),
     lambda S: _mut_pf(S, '01_ceiling.txt', 'Not supportable: *RH proved.*', 'Not supportable: *RH.*')),
    ('G-READER-BANK', 'the reader`s bank: every keyed item answered once in its vocabulary', lambda S: reader_ok(S),
     lambda S: put(S, 'reader', re.sub(r'^S001 \|[^\n]*', 'S001 | MAYBE | x', S['reader'], count=1, flags=re.M))),
    ('G-AGREEMENT-NOW', 'the rates and the disagreement count recomputed now from the reader`s bank and the key, against the agreement bank', lambda S: agreement_now(S),
     lambda S: put(S, 'ag', dict(S['ag'], r_m=-1))),
    ('G-H54A-SCORED', 'H54a recomputed from the agreement bank, against the scores and the desk', lambda S: h54_ok(S, 'H54a'), lambda S: _sc(S, 'H54a')),
    ('G-H54B-SCORED', 'H54b recomputed from the agreement bank, against the scores and the desk', lambda S: h54_ok(S, 'H54b'), lambda S: _sc(S, 'H54b')),
    ('G-H54C-SCORED', 'H54c recomputed from the agreement bank, against the scores and the desk', lambda S: h54_ok(S, 'H54c'), lambda S: _sc(S, 'H54c')),
    ('G-H54D-SCORED', 'H54d recomputed from the no-disclosure arm over the packet, against the scores and the desk', lambda S: h54_ok(S, 'H54d'), lambda S: _sc(S, 'H54d')),
    ('G-EDITIONS-UNEDITED', 'the batch`s editions, the census v0.4, the six syntheses, README, ERRATA, REGISTRY and SPIRAL_MAP on disk and at HEAD against ee75fcf',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'day1/A_Place_to_Stand_v5_16.md': (
         S['currents']['day1/A_Place_to_Stand_v5_16.md'][0] + b'x', S['currents']['day1/A_Place_to_Stand_v5_16.md'][1], S['currents']['day1/A_Place_to_Stand_v5_16.md'][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, its relay banks, the packet and its tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted and committed, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since ee75fcf: a changed page in one commit of its own, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the disagreements by edition and line', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The disagreements, for the author’s ruling, by edition and line**' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('**The disagreements, for the author’s ruling', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b621, the author’s rulings on the disagreements applied as editions where ruled' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b621, the author’s rulings on the disagreements applied as editions where ruled', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-spinor': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b620_record.py'): S['tooltext'].get(os.path.join(T, 'b620_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1, outputs and heritage paths, tracked and untracked: none changed',
     lambda S: S['keystone_changes'] == [], lambda S: put(S, 'keystone_changes', ['phase1.5/method/ENUMERA_v1_6.md'])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 958e574c, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b619_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md'] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-UNMOVED', 'the regenerated table`s diff: no row added or gone and no grade cell moved, as the face declares', lambda S: S['table_changed'] is not None
     and S['table_changed'] == [], lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b620')" in S['suite'] and "data/b620_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b620')", ''))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)', lambda S: lsr_ok(S),
     lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def main():
    import time
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b620 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT, AT THE HOLD' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a re-run at the hold; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN or MID) else regenerate()
    if RERUN:
        d = jl('terminal_table_diff.json')
        S['table_changed'] = [list(x) for x in (d.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in (d.get('added') or []) + (d.get('gone') or [])]
    elif not (PRERUN or MID):
        S['table_changed'] = ([list(x) for x in (gen_diff.get('changed') or [])] + [list(x) if isinstance(x, list) else [x] for x in
                                                                                    (gen_diff.get('added') or []) + (gen_diff.get('gone') or [])]) \
            if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-46s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
    fail, defective, negfail, EX = [], [], 0, {}
    for name, reads, pred, pos in ARMS:
        if name == 'G-ARMS-NO-LIVE-LIMB':
            S['no_live_limb'] = not defective
        try:
            live = bool(pred(S))
        except Exception as e:
            live = False
            rec('  ### %s raised %s: %s' % (name, type(e).__name__, str(e)[:160]))
        try:
            neg = bool(pred(copy.copy(S)))
        except Exception:
            neg = False
        try:
            m = pos(copy.copy(S))
            posv = bool(pred(m)) if isinstance(m, dict) else False
        except Exception:
            posv = False
        if not live:
            fail.append(name)
        if neg != live:
            negfail += 1
        if posv:
            defective.append(name)
        EX[name] = dict(live=live, neg=neg, pos=posv, reads=reads)
        rec('  %-46s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL',
                                           'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    rec('')
    rec('  ### files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                  if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN or MID):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b620_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b620_checks_postpush.txt' if pushed else 'b620_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b620_arms_prerun.txt', 'b620_lsr_prerun.json').replace('b620_checks', 'b620_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b620_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
