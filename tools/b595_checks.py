# -*- coding: utf-8 -*-
"""b595_checks.py -- THE SUITE OF b595, UNDER (R205): THE DELIBERATION TREE MODULE WRITTEN FROM THE PROMPTS AS A NEW DOCUMENT IN
TECHNE-Core, PRIVATE AND NOT PUSHED; THE b547 CITATION SETTLED BY HISTORY LINES.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b595_checks.txt before the push and
### data/b595_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b595_arms_prerun.txt and nothing else.
### ### **THIS SUITE CARRIES NO SENTENCE OF THE DOCUMENT'S BODY**: G-NO-BODY-PUBLIC builds its needles at run time from the
### TECHNE-Core file. ### The harness is b568's to b594's, carried; the arms are b595's.
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

NL = chr(10)
PP, GS, KER, TE = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula', 'D:/MY-DOwnloads/TECHNE-Core'
TX = 'C:/Users/echo chamber/.claude/projects/D--'
FACE = os.path.join(D, 'b595_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
FACES = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md'
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'
DOC_REL = 'modules/2026-10/DELIBERATION_TREE.md'
EXT_REL = 'modules/2026-10/DELIBERATION_TREE_nodes.json'
SIB_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
PRE = dict(relay='4924e098', pp='b229ff9', gs='3528bcf', te='12e4176', te_origin='29208f6')
PRE_HEADS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72'}
STEPZERO = '6a123282'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/cbf1b30e-1310-463d-994c-65478058bd99/scratchpad'


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
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


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def files_of(repo, sha_):
    return sorted(x for x in gs(repo, 'show', '--name-only', '--pretty=format:', sha_).split(NL) if x.strip())


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b595')
            and 'data/b595_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
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
            ch |= set(untracked(PP, 'phase1.5', 'phase2'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    return cr0(b).decode('utf-8', 'replace').split(NL)


def sources():
    import b595_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b595_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b595_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b595_ferry.txt'), scan=rd('b595_ferry_scan.txt'), cens=rd('b595_census_stepzero.txt'),
        fcens=rd('b595_faces_census_stepzero.txt'), pins0=rd('b595_pins_stepzero.txt'), procs=rd('b595_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b594_closing.txt'), reads=rd('b595_reads.txt'), branches=rd('b595_branches.txt'), answers=rd('b595_author_answers.txt'),
        prerun=rd('b595_arms_prerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain'),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b594*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b595_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b595_mustnotexist.txt')), table_changed=None,
        fj=jl('b595_findings.json'), tj=jl('b595_trail.json'), sc=jl('b595_scores.json'), desk=rd('b595_desk_notes.txt'),
        wl1=jl('b595_weight_line.json'), rl=jl('b595_rule_lines.json'),
    )
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
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
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs'))
    S['pp_changed'] = sorted(ch)
    S['keystone_changes'] = sorted(x for x in ch if x.startswith('phase') or x.startswith('day1/') or x.startswith('outputs/'))
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    REC = S['REC']
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b592_nodes.txt'), os.path.join(SP, '_b595_gcp'), os.path.join(D, 'b592_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b592_nodes_chi.txt'), os.path.join(SP, '_b595_gcp'), os.path.join(D, 'b592_chi_probe_out.txt'))
    X['nb'], X['h33'], X['scan_placed'] = jl('b595_nodes.json'), jl('b595_h33.json'), jl('b595_doc_scan_placed.json')
    X['cs'], X['cite_bank'], X['repin'] = jl('b595_citation_search.json'), rd('b595_citation_4787.txt'), jl('b595_balpos_repin.json')
    X['nbp'], X['page_arms'] = rd('b595_no_body_public.txt'), rd('b595_page_arms.txt')
    X['faces_pre'], X['faces_head'] = cr0(blob(PP, PRE['pp'] + ':' + FACES)), cr0(blob(PP, 'HEAD:' + FACES))
    X['balpos_pre'], X['balpos_head'] = cr0(blob(PP, PRE['pp'] + ':' + BALPOS)), cr0(blob(PP, 'HEAD:' + BALPOS))
    X['grep_pre'] = sorted((l.split(':')[1], int(l.split(':')[2])) for l in gs(PP, 'grep', '-n', '-I', '-E', r'FINDINGS\.md`?:4787\b', PRE['pp'], '--').split(NL) if l.strip())
    X['doc_raw'] = raw(TE + '/' + DOC_REL)
    X['doc'] = cr0(X['doc_raw']).decode('utf-8', 'replace') if X['doc_raw'] else ''
    X['doc_head'] = cr0(blob(TE, 'HEAD:' + DOC_REL))
    X['ext_raw'] = raw(TE + '/' + EXT_REL)
    X['ext_head'] = blob(TE, 'HEAD:' + EXT_REL)
    try:
        X['ext'] = json.loads(cr0(X['ext_raw']).decode('utf-8')) if X['ext_raw'] else {}
    except Exception:
        X['ext'] = {}
    X['te_dir'] = sorted(x.split('/')[-1] for x in gs(TE, 'ls-tree', '--name-only', 'HEAD', 'modules/2026-10/').split(NL) if x.strip())
    X['te_log'] = [(l.split(' ', 1)[0], files_of(TE, l.split(' ', 1)[0])) for l in gs(TE, 'log', '--reverse', '--pretty=%H %s', PRE['te'] + '..HEAD').split(NL) if l.strip()]
    X['te_origin'], X['te_head'] = gs(TE, 'rev-parse', 'origin/main'), gs(TE, 'rev-parse', 'HEAD')
    X['te_origin_tree'] = gs(TE, 'ls-tree', '--name-only', 'origin/main', '--', 'modules/2026-10/')
    X['sib'] = (cr0(raw(TE + '/' + SIB_REL)), cr0(blob(TE, PRE['te'] + ':' + SIB_REL)), cr0(blob(TE, 'HEAD:' + SIB_REL)))
    # ### the transcript lines each node points at: the tool-use id must sit on the cited line of the cited session file
    want = {}
    for x in X['nb'].get('nodes', []):
        want.setdefault(x['session'], {})[x['call_line']] = x['tool_use_id']
    found = {}
    for f, lines in want.items():
        hit = set()
        try:
            with io.open(os.path.join(TX, f), encoding='utf-8') as fh:
                for i, ln in enumerate(fh, 1):
                    if i in lines and lines[i] in ln and '"AskUserQuestion"' in ln:
                        hit.add(i)
        except OSError:
            pass
        found[f] = hit
    X['tx_found'] = found
    pub = {}
    for p in sorted(glob.glob(os.path.join(D, 'b595_*'))) + S['tools']:
        pub[os.path.relpath(p, ROOT).replace(os.sep, '/')] = read(p)
    pub['PLACE-papers appended'] = (S['fi_now'] or b'')[len(S['fi_pre'] or b''):].decode('utf-8', 'replace') + \
        (S['ot_now'] or b'')[len(S['ot_pre'] or b''):].decode('utf-8', 'replace')
    pub['PLACE-papers history lines'] = NL.join(set(lines_of(X['faces_head'])) - set(lines_of(X['faces_pre']))) + NL + \
        NL.join(set(lines_of(X['balpos_head'])) - set(lines_of(X['balpos_pre'])))
    pub['SIDE-global-section appended'] = (S['corr_now'] or b'')[len(S['corr_pre'] or b''):].decode('utf-8', 'replace')
    X['public'] = pub
    return X


# ### the act's own predicates
def flat(s):
    return ' '.join(s.split())


def needles(S):
    return S['REC']._prose_sentences(S['doc']) if S['doc'] else []


def no_body_public(S):
    nd = [flat(x) for x in needles(S)]
    if len(nd) < 30:
        return False
    for name, txt in S['public'].items():
        f = flat(txt)
        if any(n in f for n in nd):
            return False
    return 'NO BODY SENTENCE REACHES' in S['nbp']


def answers_banked(S):
    a = S['answers']
    return a.count('### PROMPT ') == 3 and a.count('\n  OPTION ') == 11 and a.count('[RECOMMENDED]') == 3 and a.count('\nRESULT: ') == 2 \
        and a.count('### CALL tool-use id ') == 2 \
        and 'Answer to the node-source prompt: option 1' in a and 'Answer to the relayed-mark prompt: option 1' in a \
        and 'Answer to the line-place prompt: option 1' in a


def rule_line_ok(S):
    rl = S['rl'].get('lines', [])
    return len(rl) == 1 and oline(S, rl[0]['line']).startswith(rl[0]['head']) and '(:12228)' in rl[0]['head'] \
        and 'EVERY PROMPT BANKED VERBATIM' in rl[0]['head'] and 'its question, its options and the recommended mark verbatim' in oline(S, rl[0]['line'])


def cite_search_ok(S):
    rows = sorted((p, n) for p, n in S['cs'].get('rows', []))
    return len(rows) >= 20 and rows == S['grep_pre'] and all(('### %s --' % p) in S['cite_bank'] for p in set(p for p, _ in rows)) \
        and 'FINDINGS :4787 is "" (blank)' in S['cite_bank']


def faces_line_ok(S):
    REC = S['REC']
    pre, head = lines_of(S['faces_pre']), lines_of(S['faces_head'])
    want = pre[:REC.FACES_AFTER] + ['', REC.FACES_LINE] + pre[REC.FACES_AFTER:]
    return bool(S['faces_pre']) and head == want and 'FINDINGS :4788' in REC.FACES_LINE


def balpos_line_ok(S):
    REC = S['REC']
    pre, head = lines_of(S['balpos_pre']), lines_of(S['balpos_head'])
    if not pre or not head:
        return False
    tag = [i for i, l in enumerate(pre) if l.startswith('<!-- b593 (R203) THE v0.9.5 EDITION')]
    if len(tag) != 1:
        return False
    rp = list(pre)
    n = 0
    for i in range(tag[0], len(rp)):
        t = REC._repin_balpos_line(rp[i])
        n += sum(1 for _ in re.finditer(r'(?<!v0\.9\.4 ):(?:783|791)\b', rp[i])) if t != rp[i] else 0
        rp[i] = t
    want = rp[:REC.BALPOS_AFTER] + ['', REC.BALPOS_LINE] + rp[REC.BALPOS_AFTER:]
    return head == want and n == 7 and S['repin'].get('cells') == 7 and 'v0.9.4 :776' in NL.join(head) and 'beneath v0.9.4 :782' in NL.join(head)


def cites_alone(S):
    log = S['pp_log']
    f = [h for h, s_ in log if S['pp_files'][h] == [FACES] and s_.startswith('b595 housekeeping -- FACES')]
    b = [h for h, s_ in log if S['pp_files'][h] == [BALPOS] and s_.startswith('b595 housekeeping -- BALANCE')]
    return len(f) == 1 and len(b) == 1 and all(set(S['pp_files'][h]) <= {FACES, BALPOS, 'FINDINGS.md', 'OPEN_TRAILS.md'} for h, _s in log) \
        and all(len(S['pp_files'][h]) == 1 for h, _s in log if (FACES in S['pp_files'][h] or BALPOS in S['pp_files'][h]))


def nodes_bank_ok(S):
    nb, ext = S['nb'], S['ext']
    ns, xs = nb.get('nodes', []), ext.get('nodes', [])
    if len(ns) != 44 or len(xs) != 44:
        return False
    for a, x in zip(ns, xs):
        if a['n'] != x['n'] or a['tool_use_id'] != x['tool_use_id'] or a['sha256_question'] != sha(x['question']) \
                or a['sha256_options'] != sha(json.dumps(x['options'], ensure_ascii=False, sort_keys=True)) \
                or a['sha256_answer'] != (sha(x['answer']) if x['answer'] else None) or a['call_line'] not in S['tx_found'].get(a['session'], set()):
            return False
    return nb.get('counts') == S['REC'].counts(xs) and not any('question' in a or 'options' in a or 'answer' in a for a in ns)


def ext_placed(S):
    r = S['ext_raw']
    return r is not None and S['ext_head'] is not None and cr0(r) == cr0(S['ext_head']) and sha(cr0(S['ext_head'])) == S['nb'].get('extraction', {}).get('sha256')


def doc_placed(S):
    return bool(S['doc_raw']) and cr0(S['doc_raw']) == S['doc_head'] and sha(S['doc_head']) == S['h33'].get('sha256') \
        and S['te_dir'] == ['DELIBERATION_TREE.md', 'DELIBERATION_TREE_nodes.json']


def doc_form(S):
    d = S['doc']
    ls = d.split(NL)
    heads = ['## (i) ', '## (ii) ', '## (iii) ', '## (iv) ', '## (v) ', '## (vi) ', '## (vii) ', '## (viii) ']
    pos = [d.find(NL + h) for h in heads]
    viii = d[d.find(NL + '## (viii) '):] if pos[-1] >= 0 else ''
    return bool(ls) and ls[0].startswith('# THE DELIBERATION TREE') and ls[2] == '*v0.1 — 2026-10-02*' and all(p >= 0 for p in pos) \
        and pos == sorted(pos) and viii.find('### Placement') >= 0 and viii.find('### Correspondence') > viii.find('### Placement')


def doc_table(S):
    REC = S['REC']
    rows = [l for l in S['doc'].split(NL) if re.match(r'^\| \d+ \| b\d{3} \| ', l)]
    xs = S['ext'].get('nodes', [])
    return len(rows) == 44 and rows == REC._table(xs)[2:] and (REC.TABLE_HEAD in S['doc'])


def doc_counts(S):
    REC = S['REC']
    xs = S['ext'].get('nodes', [])
    ct = REC._counts_table(REC.counts(xs))
    d = S['doc']
    return bool(xs) and all(r in d.split(NL) for r in ct) and REC.counts(xs) == S['nb'].get('counts')


def doc_words(S):
    REC = S['REC']
    w = sum(REC._words_outside_tables(S['doc'], [k]) for k in ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'))
    return bool(S['doc']) and 300 <= w <= 2500 and w == S['h33'].get('body_words')


def h33a_ok(S):
    H = S['h33']
    want = 'HOLDS' if len(H.get('both', [1] * 99)) >= 25 else 'REFUTED'
    return H.get('H33a') == want and S['sc'].get('H33a', [''])[0] == want and H.get('nodes') == len(S['ext'].get('nodes', []))


def h33b_ok(S):
    xs = S['ext'].get('nodes', [])
    wr = [x for x in xs if x['answered'] and x['recommended']]
    m = [x for x in wr if x['answered'] == x['recommended']]
    want = 'HOLDS' if wr and len(m) / float(len(wr)) <= 0.8 else 'REFUTED'
    return bool(wr) and S['h33'].get('H33b') == want and S['sc'].get('H33b', [''])[0] == want


def h33c_ok(S):
    C = S['REC'].counts(S['ext'].get('nodes', []))
    want = 'HOLDS' if not C['answers producing a clause and later reversed'] else 'REFUTED'
    return bool(S['ext'].get('nodes')) and S['h33'].get('H33c') == want and S['sc'].get('H33c', [''])[0] == want


def h33d_ok(S):
    import banned_terms as BT
    REC = S['REC']
    d = S['doc']
    if not d:
        return False
    st = sum(1 for l in d.split(NL) for _m in BT.PAT.finditer(l) if not any(rx.search(l) for rx, _ in BT.EXCEPT))
    ce = sum(1 for l in d.split(NL) for _m in REC.CEILING.finditer(l))
    want = 'HOLDS' if st == 0 and ce == 0 else 'REFUTED'
    H = S['h33']
    return H.get('H33d') == want and S['sc'].get('H33d', [''])[0] == want and H.get('stems_whole') == st and H.get('ceiling_whole') == ce


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 18]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The document**' in tail and ('sha256 `%s`' % S['h33'].get('sha256', '#')) in tail \
        and 'TECHNE-Core' in tail and 'not pushed' in tail and '44 nodes' in tail and '**Read in mutual light**' in tail \
        and '**The b547 citation**' in tail and 'FINDINGS :4788' in tail


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


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R205) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and '### ORPHANS:' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 grep.exe  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b594`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b594' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b595 -- x'])),
    ('G-R205-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R205) END' in S['ferry'] and S['ot'].count('**(R205) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R205) ratified', '(R205) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b592_author_answers.txt @', 'data/b593_author_answers.txt @', 'OPEN_TRAILS.md @ b229ff9', 'FINDINGS.md @ b229ff9',
        FACES + ' @ b229ff9', BALPOS + ' @ b229ff9', 'tools/banned_terms.py @', 'data/b594_closing_push_out.txt @', 'tools/b591_checks.py @',
        'THE_LOCATED_CLAUSE_METHOD.md (the sibling, private) @')) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: three prompts, question, options and recommended mark verbatim, each result', lambda S: answers_banked(S),
     lambda S: put(S, 'answers', S['answers'].replace('[RECOMMENDED]', '', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 6a123282`s files', lambda S: S['pushout'][0] == ['data/b594_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b594') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b594'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'epstein-b590': '0000000'}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked weight line', lambda S: fline(S, S['wl1'].get('line')).startswith(S['wl1'].get('head', '#'))
     and '(:6818)' in fline(S, S['wl1']['line']) and 'b594 AT ITS WEIGHT' in fline(S, S['wl1']['line']) and 'The suite read 66 of 66.' in fline(S, S['wl1']['line']),
     lambda S: put(S, 'wl1', dict(S['wl1'], line=1))),
    ('G-RULE-LINE', 'OPEN_TRAILS at the standing line on prompts banked verbatim', lambda S: rule_line_ok(S), lambda S: put(S, 'rl', dict(S['rl'], lines=[]))),
    ('G-CITATION-SEARCH', 'PLACE-papers at b229ff9 grepped afresh for the :4787 citation, against the bank', lambda S: cite_search_ok(S),
     lambda S: put(S, 'grep_pre', S['grep_pre'][1:])),
    ('G-FACES-HISTORY-LINE', 'FACES v0.2 at HEAD against b229ff9: the one history line beneath b547`s block, nothing else', lambda S: faces_line_ok(S),
     lambda S: put(S, 'faces_head', S['faces_head'].replace(b'FINDINGS :4788', b'FINDINGS :4787', 1))),
    ('G-BALPOS-HISTORY-LINE', 'BALPOS v0.9.5 at HEAD against b229ff9: the history line beneath b545`s block and seven cells re-pinned, nothing else',
     lambda S: balpos_line_ok(S), lambda S: put(S, 'balpos_head', S['balpos_head'].replace(b'v0.9.4 :776', b'v0.9.4 :778', 1))),
    ('G-CITATIONS-COMMITTED-ALONE', 'PLACE-papers` log since b229ff9: each history line committed alone', lambda S: cites_alone(S),
     lambda S: put(S, 'pp_files', {h: ([FACES, BALPOS] if f in ([FACES], [BALPOS]) else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b592`s v0.16 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the history-line commits', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['page_arms']
     and 'G-CHAIN-PAGE : PASS' in S['page_arms'] and 'G-CHAIN-PAGE-CHI : PASS' in S['page_arms'],
     lambda S: put(S, 'page_arms', S['page_arms'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-NODES-BANK', 'the relay node bank against the TECHNE-Core extraction and each session file at its cited line', lambda S: nodes_bank_ok(S),
     lambda S: put(S, 'tx_found', {k: set() for k in S['tx_found']})),
    ('G-EXTRACTION-PLACED', 'the TECHNE-Core extraction`s bytes, its HEAD blob and the relay bank`s digest', lambda S: ext_placed(S),
     lambda S: put(S, 'ext_raw', (S['ext_raw'] or b'') + b' ')),
    ('G-DOC-PLACED', 'the TECHNE-Core file`s bytes, its HEAD blob, its directory and the banked digest', lambda S: doc_placed(S),
     lambda S: put(S, 'doc_raw', (S['doc_raw'] or b'') + b'x')),
    ('G-DOC-COMMITS-ALONE', 'TECHNE-Core`s log since 12e4176: the extraction alone, then the document alone', lambda S: [f for _h, f in S['te_log']] == [[EXT_REL], [DOC_REL]],
     lambda S: put(S, 'te_log', S['te_log'] + [('x', ['y'])])),
    ('G-DOC-NOT-PUSHED', 'TECHNE-Core`s remote-tracking main against its HEAD and its tree', lambda S: S['te_origin'].startswith(PRE['te_origin'])
     and S['te_head'] != S['te_origin'] and S['te_origin_tree'] == '', lambda S: put(S, 'te_origin', S['te_head'])),
    ('G-SIBLING-UNEDITED', 'the method document on disk and at HEAD against 12e4176', lambda S: bool(S['sib'][1]) and S['sib'][0] == S['sib'][1] == S['sib'][2],
     lambda S: put(S, 'sib', (S['sib'][0] + b'x', S['sib'][1], S['sib'][2]))),
    ('G-DOC-FORM', 'the file`s title, version line, section heads in order, Placement and Correspondence', lambda S: doc_form(S),
     lambda S: put(S, 'doc', S['doc'].replace('*v0.1 — 2026-10-02*', '*v0.1*'))),
    ('G-DOC-TABLE', 'the file`s 44 rows against the extraction rendered afresh', lambda S: doc_table(S),
     lambda S: put(S, 'doc', S['doc'].replace('| 44 | b593 |', '| 44 | b592 |'))),
    ('G-DOC-COUNTS', 'the file`s counts table and the relay bank`s counts against the extraction counted afresh', lambda S: doc_counts(S),
     lambda S: put(S, 'nb', dict(S['nb'], counts=dict(S['nb'].get('counts', {}), **{'prompts (nodes)': 45})))),
    ('G-DOC-WORDS', 'the body outside the tables, counted afresh against the cap and the bank', lambda S: doc_words(S),
     lambda S: put(S, 'h33', dict(S['h33'], body_words=1))),
    ('G-H33A-SCORED', 'the relay banks read for question and option set, the scores', lambda S: h33a_ok(S), lambda S: put(S, 'h33', dict(S['h33'], H33a='HOLDS'))),
    ('G-H33B-SCORED', 'the extraction`s answered nodes counted afresh against the cap', lambda S: h33b_ok(S), lambda S: put(S, 'h33', dict(S['h33'], H33b='HOLDS'))),
    ('G-H33C-SCORED', 'the extraction`s clauses and reversals counted afresh', lambda S: h33c_ok(S), lambda S: put(S, 'h33', dict(S['h33'], H33c='REFUTED'))),
    ('G-H33D-SCORED', 'the file scanned afresh for stems and the ceiling, whole', lambda S: h33d_ok(S), lambda S: put(S, 'h33', dict(S['h33'], stems_whole=-1))),
    ('G-NO-BODY-PUBLIC', 'every relay file this act writes, every appended PLACE-papers byte, both history lines and SIDE-global-section, against '
                         'needles built at run time from the TECHNE-Core file', lambda S: no_body_public(S),
     lambda S: put(S, 'public', dict(S['public'], **{'data/b595_x.txt': (needles(S) or ['x'])[0]}))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-ANSWERS-RECORDED', 'this act`s trail record', lambda S: '**Answered before the seal, by the author** (relay data/b595_author_answers.txt)' in trail(S)
     and 'the standing line that every prompt is banked verbatim' in trail(S) and '**Recorded as the navigator’s:**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Recorded as the navigator’s:**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY’s edition' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY’s edition', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-explicit-formula': '0'}))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b595_record.py'): S['tooltext'].get(os.path.join(T, 'b595_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == sorted([BALPOS, FACES]),
     lambda S: put(S, 'keystone_changes', sorted([BALPOS, FACES, 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md']))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 4924e098, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b594_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', BALPOS, FACES]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b595')" in S['suite'] and "data/b595_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b595')", ''))),
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
    pushed = RERUN or (not PRERUN and is_pushed())
    rec('=' * 104)
    rec('b595 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN:
        rec('### run at (UTC) : %s   ### the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
            % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    rec('=' * 104)
    S = sources()
    rc_gen, gen_diff = (0, dict(rerun=True)) if (RERUN or PRERUN) else regenerate()
    if RERUN:
        S['table_changed'] = []
    elif not PRERUN:
        S['table_changed'] = [list(x) for x in (gen_diff.get('changed') or [])] if rc_gen == 0 and 'changed' in gen_diff else None
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    rec('  arms in the (G2) block : %d ; run here : %d' % (len(declared), len(names)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-40s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
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
        rec('  %-40s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL',
                                           'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    rec('')
    rec('  ### files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                  if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    if not (RERUN or PRERUN):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), gen_diff.get('changed') or ''))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b595_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b595_checks_postpush.txt' if pushed else 'b595_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b595_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
