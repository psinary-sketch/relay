# -*- coding: utf-8 -*-
"""b711_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b711's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (ec2d71b5, a NEW session after the author's /clear; the anchor (R321)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b711, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b711_citation_check.txt
### (.json) ; `ferry` -> data/b711_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Written by the Write tool at b711 from b710_citation.py's form (its engine :1-:101 and :344-:484, read at step zero), its cite rows this
### ruling's; this tool writes only the banks named above. A kernel's file at a tag is read here by `git cat-file` and `git grep` inside this
### tool (a named tool's read, its rows banked), never printed whole.
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b677_citation as C   # noqa: E402  ### the helpers, imported unchanged
import b711_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R321)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b711_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
    return REC.R.ROOT_EXCLUDE


C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd = C.g, C.rd
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def _ws(s):
    return ''.join((s or '').split())


def _jl(name):
    try:
        return json.loads(rd(os.path.join(D, name)) or '{}')
    except Exception:
        return {}


def _blob(repo, rev, path):
    """a file's text at a revision, read inside the tool (`git cat-file -p`), '' when absent."""
    r = subprocess.run(['git', '-C', repo, 'cat-file', '-p', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''


def _decl_files(repo, rev, name):
    """the .lean files at `rev` that DECLARE `name` (its last dotted component after theorem/lemma/def/structure), by git grep -l inside the tool."""
    short = name.split('.')[-1]
    r = subprocess.run(['git', '-C', repo, 'grep', '-l', '-E', r'^\s*(private\s+)?(theorem|lemma|def|structure|abbrev|instance)\s+' + re.escape(short) + r'(\s|$|:)',
                        rev, '--', '*.lean'], capture_output=True)
    return [l.split(':', 1)[1] for l in r.stdout.decode('utf-8', 'replace').split(NL) if ':' in l]


def _decl_line(text, short):
    rx = re.compile(r'^\s*(private\s+)?(theorem|lemma|def|structure|abbrev|instance)\s+' + re.escape(short) + r'(\s|$|:)')
    return next((i + 1 for i, l in enumerate(text.split(NL)) if rx.match(l)), 0)


def _remote_heads(repo):
    out = g(repo, 'ls-remote', '--heads', 'origin')[1] or ''
    return dict((l.split('\t', 1)[1].strip(), l.split('\t', 1)[0]) for l in out.split(NL) if '\t' in l)


def _quote(text, start, stop):
    """the ruling's quotation that opens with `start`, cut at `stop` (the quotation's own closing mark and the clause after it)."""
    i = text.find(start)
    if i < 0:
        return ''
    j = text.find(stop, i)
    return text[i:j] if j > 0 else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    text = C.ferry_text()
    # ### the ferry's read-first list and the banks (R321) names, by existence
    for f in ('data/b710_closing.txt', 'data/b710_defects.txt', 'data/standing_clauses_v1.txt', 'data/b710_reading5.txt', 'data/b710_registrations.txt',
              'data/b709_registrations.txt', 'data/b709_port.txt', 'data/b709_pairs.txt', 'data/b710_tool_repairs.txt', 'data/b710_closing_push_out.txt',
              'data/b710_ferry.txt', 'data/b710_rules.txt', 'data/b710_fit.txt', 'data/b710_r5_search.txt', 'data/b710_standing_control.json',
              'data/b710_scores.json', 'data/b710_scores_close.json', 'data/b710_mirror.txt', 'data/b710_root_banks.txt', 'data/b710_act_root.json',
              'data/b710_checks.txt', 'data/b710_checks_postpush.txt', 'data/b710_seal_hashes.json', 'data/b710_citation_check.txt', 'data/b710_report.txt',
              'data/b709_report.txt', 'data/b707_onset.txt', 'data/b705_i6_ranking.txt', 'data/b675_corrigenda.txt', 'data/act_roots.txt', 'data/b675_rules.txt',
              'data/b680_rules.txt', 'data/b684_rules.txt', 'data/b686_rules.txt', 'data/b692_rules.txt', 'data/b706_rules.txt', 'data/b708_rules.txt',
              'data/b709_rules.txt', K.B710_FACE, 'tools/b710_worklist.py', 'tools/b710_tests.py', 'tools/b710_citation.py', 'tools/b710_record.py',
              'tools/b710_checks.py', 'tools/b710_closing.py', 'tools/b710_reg_gate.py', 'tools/b710_regspec.py', 'tools/b710_corrigendum.py',
              'tools/b710_carry.py', 'tools/b710_standing.py', 'tools/b710_locate.py', 'tools/b710_report.py', 'tools/b709_pairs.py', 'tools/b707_onset.py',
              'tools/b675_li_bench.py', 'tools/b696_witness_balls.py', 'tools/b706_standing_figures.py', 'tools/circuit_read.py', 'tools/mirror_verify.py',
              'tools/mirror_build.ps1', 'tools/mirror_prevbuild.json', 'tools/push_gated.sh', 'tools/act_root.py', 'tools/ferry_scan.py', 'tools/b682_citation.py',
              'tools/b678_corrigendum.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R321)(1): the head line, by the ruling's own reading (the line as delimited by the outer quotes and the line's end)
    cl = lines_of(p('data', 'b710_closing.txt'))
    q = _quote(text, 'b710 closed: relay', '”; the head line carries')
    exact = q == cl[0]
    norm = lambda s: _ws(s).replace('`', '').replace('“', '"').replace('”', '"')   # noqa: E731
    diffs = [(i, a, b) for i, (a, b) in enumerate(zip(q, cl[0])) if a != b][:4]
    add('ruling (1)', 'data/b710_closing.txt :1, the head line, against (R321)(1)`s quote as delimited by the outer quotes and the line`s end',
        exact, 'quote %d characters, the line %d ; equal byte for byte %s ; equal after the backticks are dropped and the curly inner quotes read straight %s ; '
        'the first differences (offset, ruling, line): %s -- the line carries RECORD`S (a backtick) twice where the quotation reads RECORDS, and the PLACE-papers '
        'subject in straight quotes where the quotation curls them' % (len(q), len(cl[0]), exact, norm(q) == norm(cl[0]), diffs), '0-1')
    add('ruling (1)', 'the head line carries the closing tool`s capture-name failure text where the record`s commits belong, defect (k)',
        cl[0].count('IS NOT THE RECORD`S CAPTURE') == 2 and 'IS NOT THE RECORD`S CAPTURE' in ' '.join(lines_of(p('data', 'b710_defects.txt'))),
        'data/b710_closing.txt :1 (twice) ; data/b710_defects.txt (k) :89-:96', '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b710_closing.txt, the carried-forward rows (a)-(h) and the branch row (f) by line', cf > 0 and first(cl, '    (a) ', cf) and first(cl, '    (f) Branches left', cf),
        'data/b710_closing.txt :%d (the head), (a) :%d, (f) :%d, (h) :%d' % (cf, first(cl, '    (a) ', cf), first(cl, '    (f) Branches left', cf), first(cl, '    (h) ', cf)), '0-1')
    add('ruling (1)', 'reading 5 in data/b710_reading5.txt', 'READING 5: THE PRINCIPLES 4' in ' '.join(lines_of(p('data', 'b710_reading5.txt'))), 'data/b710_reading5.txt :191', '1')
    add('ruling (1)', 'the entry at FINDINGS :10246', at(fi, 10246).startswith('## '), 'FINDINGS :10246 %r' % at(fi, 10246)[:90], '1')
    add('ruling (1)', 'the moves-by-locus table entered in OPEN_TRAILS (W-ORD-MOVES-BY-LOCUS)', 'W-ORD-MOVES-BY-LOCUS' in at(ot, 15804), 'OPEN_TRAILS :15804', '1')
    add('ruling (1); ruling (3)', 'W-ORD-READING5-INDEPENDENCE at :15806', 'W-ORD-READING5-INDEPENDENCE' in at(ot, 15806), 'OPEN_TRAILS :15806', '0-1')
    add('ruling (1)', 'the trail at :15808', at(ot, 15808).startswith('### b710'), 'OPEN_TRAILS :15808 %r' % at(ot, 15808)[:60], '1')
    ctl = _jl('b710_standing_control.json')
    add('ruling (1)', 'the standing clauses banked at data/standing_clauses_v1.txt, the re-assembly control equal', 'VERSION: 1' in (rd(p('data', 'standing_clauses_v1.txt')) or '') and ctl.get('ok') is True,
        'data/standing_clauses_v1.txt :3 ; data/b710_standing_control.json ok %s' % ctl.get('ok'), '1')
    reg = g(ROOT, 'log', '--format=%h %s', '--', 'data/b710_registrations.txt')[1] or ''
    add('ruling (1)', 'data/b710_registrations.txt committed at step zero (the refined law, the surgery, the coefficient observation)',
        reg.strip().split(NL)[-1].startswith('41ff1193') and len(reg.strip().split(NL)) == 1, 'git log of the bank: %r' % reg.strip()[:90], '1')
    row = act_root_line('b710')
    ar = _jl('b710_act_root.json')
    rb = ' '.join(lines_of(p('data', 'b710_root_banks.txt')))
    add('ruling (1)', 'the root 11fe3e21 over 105 banks chained from b3213c0b', bool(row) and row[0][1].startswith('11fe3e21') and 'BANKS 105' in rb and 'b3213c0b' in json.dumps(ar),
        'data/act_roots.txt row b710 %s ; data/b710_root_banks.txt BANKS 105 %s ; prev b3213c0b in data/b710_act_root.json %s' % (
            row[0][1][:16] if row else 'NONE', 'BANKS 105' in rb, 'b3213c0b' in json.dumps(ar)), '1')
    cpp = rd(p('data', 'b710_checks_postpush.txt')) or ''
    cpr = rd(p('data', 'b710_checks.txt')) or ''
    fl = re.search(r'LIVE FAILING : \d+ (\[.*?\])', cpp)
    add('ruling (1)', 'the chain b624-b710 AGREE (G-ACTROOT-VERIFY not failing post-push); suite 138 of 143 pre-push and 137 post-push',
        bool(fl) and 'G-ACTROOT-VERIFY' not in fl.group(1) and 'LIVE PASSING : 137' in cpp and 'LIVE PASSING : 138' in cpr and 'ARMS RUN : 143' in cpp,
        'data/b710_checks.txt, data/b710_checks_postpush.txt: failing post-push %s' % (fl.group(1) if fl else 'NONE'), '1')
    mr = rd(p('data', 'b710_mirror.txt')) or ''
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-24-b710.zip CLEAN on all three clauses over 70 files', 'CLEAN ON ALL THREE CLAUSES' in mr and re.search(r'\b70 files\b', mr) is not None
        and os.path.exists(K.MIRROR_ZIP), 'data/b710_mirror.txt: "70 files" %s ; the zip exists %s ; the closing :68 reads "entries 71" (the MANIFEST beside the 70)' % (
            re.search(r'\b70 files\b', mr) is not None, os.path.exists(K.MIRROR_ZIP)), '1')
    sc, scc = _jl('b710_scores.json'), _jl('b710_scores_close.json')
    flat = json.dumps(sc) + json.dumps(scc)
    add('ruling (1)', 'N1-N5 and S1-S3 HELD', 'REFUTED' not in flat and flat.count('HELD') >= 8, 'data/b710_scores.json, _close.json: REFUTED %d ; HELD %d' % (flat.count('REFUTED'), flat.count('HELD')), '1')
    add('ruling (1)', 'the fourteen sealed tools` hashes equal at the close', 'AGREE 14 of 14' in at(cl, 20), 'data/b710_closing.txt :20 %r' % at(cl, 20).strip(), '1')
    n1 = at(cl, 85)
    add('ruling (1)', 'no dispatch, no lean on the host', 'runner dispatches banked 0' in n1 and "lean or lake (relay data/b710_commands.json): []" in n1, 'data/b710_closing.txt :85', '1')
    dl = lines_of(p('data', 'b710_defects.txt'))
    lets = ''.join(m.group(1) for l in dl for m in [re.match(r'^    \(([a-z])\) ', l)] if m)
    owners = set(re.match(r'^    \([a-z]\) (THE [A-Z]+)', l).group(1) for l in dl if re.match(r'^    \([a-z]\) THE ', l))
    add('ruling (1)', 'eleven defects (a)-(k), all the seat`s', lets == 'abcdefghijk' and owners == {'THE SEAT'}, 'data/b710_defects.txt letters %s ; owners %s' % (lets, sorted(owners)), '1')
    add('ruling (1); ruling (10)', '"Nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b711_worklist.py DRAFT', '6')
    # ### (R321)(2): the four structural repairs and the three item repairs, their objects located
    ck = rd(p('tools', 'b710_checks.py')) or ''
    for arm in ('G-CLOSING-DRY-STEP', 'G-REPORT-UNSEALED', 'G-AXIS-REGISTERED', 'G-ANSWERS-BEFORE-WRITES', 'G-SEALED-AFTER-COMPONENTS', 'G-TRAIL-LINES-EQUAL-DEFECTS',
                'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-ACTROOT-LAST'):
        add('ruling (2)', 'the arm %s in the carried suite (tools/b710_checks.py)' % arm, ("'%s'" % arm) in ck, 'named in the suite %s' % (("'%s'" % arm) in ck), '1, 5')
    add('ruling (2)(i)', 'the trail-equality arms are three (the ruling`s "the three trail-equality arms")',
        sum(("'%s'" % a) in ck for a in ('G-TRAIL-LINES-EQUAL-DEFECTS', 'G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL')) == 3, 'tools/b710_checks.py', '1')
    add('ruling (2)(iii)', 'the three needles of b708-b710 named by the ruling, each in its act`s suite',
        "'G-CLOSING-DRY-STEP'" in (rd(p('tools', 'b708_checks.py')) or '') and "'G-REPORT-UNSEALED'" in (rd(p('tools', 'b709_checks.py')) or '') and "'G-AXIS-REGISTERED'" in (rd(p('tools', 'b709_checks.py')) or ''),
        'tools/b708_checks.py G-CLOSING-DRY-STEP ; tools/b709_checks.py G-REPORT-UNSEALED, G-AXIS-REGISTERED (b710 carried and repaired the two, data/b710_tool_repairs.txt (1)-(2))', '1')
    add('ruling (2)(ii)', 'data/act_roots.txt, the root list every bank writer is to read', len(lines_of(p('data', 'act_roots.txt'))) > 80 and bool(row), 'data/act_roots.txt, its b710 row', '1')
    add('ruling (2)(ii)', 'the b670 form of the mirror (the builder excepted from the membrane)', os.path.exists(p('data', 'b670_mirror.txt')) or os.path.exists(p('tools', 'mirror_build.ps1')),
        'tools/mirror_build.ps1 ; data/b670_mirror.txt %s' % os.path.exists(p('data', 'b670_mirror.txt')), '1')
    clo = rd(p('tools', 'b710_closing.py')) or ''
    add('ruling (2) (k)', 'the closing`s head-line builder and its capture-name failure text', 'IS NOT THE RECORD' in clo and 'def head_line' in (rd(p('tools', 'b634_closing.py')) or clo),
        'tools/b710_closing.py carries the failure text %s ; the head-line builder tools/b634_closing.py head_line %s' % ('IS NOT THE RECORD' in clo, 'def head_line' in (rd(p('tools', 'b634_closing.py')) or '')), '1')
    l682 = lines_of(p('tools', 'b682_citation.py'))
    b710c = rd(p('data', 'b710_citation_check.txt')) or ''
    n468 = re.findall(r"the answer carrying '[^']*', 468 characters", b710c)
    add('ruling (2)', 'the citation tool`s answer check reading 468 characters -- the cut at tools/b682_citation.py :221 (from the last BEGIN before the needle to the '
        'first "END" after it, a substring any capitalised word carrying END matches) and b710`s answer check of 468 characters',
        "best.find('END', k)" in at(l682, 221) and bool(n468), 'tools/b682_citation.py :221 %r ; data/b710_citation_check.txt: answers of 468 characters %d' % (at(l682, 221).strip(), len(n468)), '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (30), b710`s)', bool(last) and re.match(r'^\s*\(30\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    for f in ('data/standing_clauses_v2.txt', 'data/b711_tool_repairs.txt', 'data/b711_independence.txt', 'data/b711_port.txt', 'data/b711_join_grade.txt',
              'tools/b711_surgery.py', 'tools/b711_coeffs.py', 'tools/b711_axis.py', 'data/b711_rules.txt', 'data/b712_rules.txt'):
        add('ruling (2)-(9)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-6')
    # ### (R321)(3): the named terminals, each at its kernel and tag, its declaration located inside this tool (no line printed to the seat)
    for kern, tag, f, name in K.INDEPENDENCE_TERMINALS:
        repo = 'D:/' + kern
        tg = (g(repo, 'rev-parse', '--verify', '-q', tag + '^{commit}')[1] or '').strip()
        if name == 'Independence lemma':
            files = (g(repo, 'grep', '-l', '-i', '-e', 'independ', tag, '--', '*.lean')[1] or '').strip()
            decls = [l for l in _blob(repo, tag, f).split(NL) if re.match(r'^\s*(theorem|lemma|def|structure)\s', l)]
            add('ruling (3)', '%s: "its Independence lemma" at %s %s' % (kern, kern, tag), bool(files),
                'the .lean files at %s naming "independ" in any case: %s ; the declarations of %s at %s: %s -- NO DECLARATION NAMED FOR INDEPENDENCE; the per-statement '
                'lemmas are statement_a..statement_d (Lemmas 2.1, 3.1, 4.1 of the source paper and (d)) and the instance sideIDS' % (
                    tag, files or 'NONE', f, tag, [re.match(r'^\s*\w+\s+(\S+)', l).group(1) for l in decls]), '0 (3)')
            continue
        if name == 'the codimension terminals':
            t = _blob(repo, tag, f)
            ths = [re.match(r'^\s*(theorem|lemma)\s+(\S+)', l).group(2) for l in t.split(NL) if re.match(r'^\s*(theorem|lemma)\s', l)]
            add('ruling (3)', '%s: the codimension terminals at %s (%s)' % (kern, tag, f), bool(tg) and len(ths) > 0, 'the tag %s ; theorems in the file at the tag %d: %s' % (tg[:8], len(ths), ths[:12]), '0 (3)')
            continue
        short = name.split('.')[-1]
        df = _decl_files(repo, tag, short)
        t = _blob(repo, tag, df[0]) if df else ''
        ns = '.'.join(name.split('.')[:-1])
        ns_ok = not ns or ns.split('.')[-1] in ' '.join(l for l in t.split(NL) if l.startswith('namespace ')) or ns == kern.replace('SIDE-', 'SIDE').title().replace('-', '')
        add('ruling (3)', '%s %s at %s' % (kern, name, tag), bool(tg) and bool(df) and ns_ok,
            'the tag %s ; declared in %s at :%d ; the namespace %r %s' % (tg[:8], df or 'NONE', _decl_line(t, short) if t else 0, ns or '-', 'read' if ns_ok else 'NOT IN THE FILE`S namespace LINES'), '0 (3)')
    sl = _blob('D:/SIDE-kernel', 'v1.8', 'Kernel/SilenceTheorem.lean').split(NL)
    add('ruling (3)', 'silence_universal at SIDE-kernel Kernel/SilenceTheorem.lean :74', at(sl, 74).startswith('theorem silence_universal'), ':74 %r' % at(sl, 74)[:40], '0 (3)')
    ee = lines_of(os.path.join(PP, K.EXCLUSION_ENGINE))
    graded = [(n, i) for i in range(K.EE_TABLE[0], K.EE_TABLE[1] + 1) for n in ('silence_universal', 'kappa_zero_of_no_mechanism', 'parametric_mechanism_theorem', 'interface_split',
                                                                                  'offLine_of_codim_two', 'identity_formation_bijection', 'T3prime_shared_witness', 'lam_add',
                                                                                  'productLemma_holds', 'family_theorem', 'h2_sign_cfg_iff_target', 'h2_sign_sum_iff_rh') if '`%s`' % n in at(ee, i)]
    add('ruling (3)', 'EXCLUSION_ENGINE`s terminal table (phase1.5/method/EXCLUSION_ENGINE.md :185-:206), the named terminals it grades',
        at(ee, 185).startswith('| Terminal | Location | Grade') and len(graded) == 5,
        'the header :185 ; graded rows: %s ; the other named terminals no row of the table names' % ', '.join('%s :%d' % x for x in graded), '0 (3)')
    add('ruling (3)', 'T3″ (T3doubleprime_general_commutation_fails) to be read as Independence`s control object "where its statement bears that reading"', True,
        'read at the supplement from its statement; the reading not taken here', '0 (3)')
    srch = lines_of(p('data', 'b710_r5_search.txt'))
    add('ruling (3)', 'the search query that missed them at b710 (data/b710_r5_search.txt :70-:131 and :586-:598, OPEN_TRAILS :15806)', len(srch) >= 598 and 'Independence' in ' '.join(srch[69:131]),
        'data/b710_r5_search.txt %d lines ; :70 %r' % (len(srch), at(srch, 70)[:60]), '0 (3)')
    # ### (R321)(4): the port and the join
    pl = lines_of(p('data', 'b709_port.txt'))
    loc = (g(K.LV_DIR, 'rev-parse', 'port-b707')[1] or '').strip()
    add('ruling (4)', 'port-b707 at b709`s one commit 92af8a34 (the edit`s base)', loc == K.PORT_TIP, 'local port-b707 %s' % loc[:8], '2')
    add('ruling (4)', 'DirichletC7Order.lean :212:55 and the signature data/b709_port.txt reads',
        'DirichletC7Order.lean:212:55' in at(pl, 21) and 'WeakFEPair.hasMellin (hurwitzEvenFEPair a).toStrongFEPair w' in at(pl, 47) and '.k < re ?m' in at(pl, 45),
        'data/b709_port.txt :21 ; :40-:47 (the argument w of type ℂ where hasMellin`s first explicit argument is (hurwitzEvenFEPair a).toStrongFEPair.k < re ?m)', '2')
    blob = _blob(K.LV_DIR, K.PORT_TIP, K.PORT_MODULE).split(NL)
    add('ruling (4)', 'the module at the port`s tip, its line 212 holding the hasMellin call', 'hasMellin' in at(blob, 212), '%s at 92af8a34: %d lines ; :212 carries hasMellin %s' % (K.PORT_MODULE, len(blob), 'hasMellin' in at(blob, 212)), '2')
    add('ruling (4)', 'the other failing lines after :212 (data/b709_port.txt :12-:17: :212:6, :193:0 timeouts; :333:8 cascade; :501:31 StrongFEPair.Λ_eq; :500:82; :574:39)',
        all(x in ' '.join(pl[10:18]) for x in ('212:6', '193:0', '333:8', '501:31', '500:82', '574:39')), 'data/b709_port.txt :11-:17 -- "nothing else edited" ((R321)(4)) leaves them as they stand', '2')
    rp = _blob(K.LV_DIR, K.LV_V0100, 'SIDELvConservation/RegisterPentagon.lean')
    add('ruling (4)', 'Register4_positivity at 93c27ec', 'Register4_positivity' in rp, 'SIDELvConservation/RegisterPentagon.lean at 93c27ec :%d' % first(rp.split(NL), 'Register4_positivity'), '2')
    lv_tags = (g(K.LV_DIR, 'tag', '--points-at', K.LV_V0100)[1] or '').split()
    add('ruling (4)', '93c27ec the deposit v0.10.0', 'v0.10.0' in lv_tags, 'tags at 93c27ec: %s' % lv_tags, '2')
    jl = rd(os.path.join(K.JOIN_DIR, 'lakefile.lean')) or rd(os.path.join(K.JOIN_DIR, 'lakefile.toml')) or ''
    add('ruling (4)', 'SIDE-faces-join`s lakefile requiring SIDE-lv-conservation by revision', 'sideLvConservation' in jl or 'SIDE-lv-conservation' in jl,
        'the lakefile names lv %s ; its rev %s' % ('sideLvConservation' in jl, (re.search(r'SIDE-lv-conservation[^\n]*\n?[^\n]*@\s*"([0-9a-f]+)"', jl) or re.search('', '')).group(0)[:120]), '2')
    fj = (g(K.JOIN_DIR, 'grep', '-l', '-w', 'faces_join', 'HEAD', '--', '*.lean')[1] or '').strip()
    add('ruling (4)', 'faces_join at SIDE-faces-join', bool(fj), 'files %s' % fj, '2')
    wf = os.path.exists(os.path.join(K.LV_DIR, '.github', 'workflows', 'build-module.yml')) and os.path.exists(os.path.join(K.JOIN_DIR, '.github', 'workflows', 'build-module.yml'))
    add('ruling (4)', 'the two workflows the two dispatches run (lv`s and the join`s build-module.yml)', wf, 'both present at the working trees %s' % wf, '2')
    jt = (g(K.JOIN_DIR, 'tag', '-l')[1] or '').split()
    add('ruling (4)', 'SIDE-faces-join untagged (v0.1.0 only on DERIVES)', not jt, 'tags %s' % jt, '2')
    add('ruling (4)', 'W-ORD-LV-FORWARD-PORT at OPEN_TRAILS :15686 and W-ORD-LV-CLOSURE-JOIN at :15452', 'W-ORD-LV-FORWARD-PORT' in at(ot, 15686) and 'W-ORD-LV-CLOSURE-JOIN' in at(ot, 15452),
        'OPEN_TRAILS :15686, :15452', '2')
    add('ruling (4)', 'W-ORD-LV-PORT-TAG -- TO BE ENTERED', not any('W-ORD-LV-PORT-TAG' in l for l in ot), 'absent from OPEN_TRAILS, as ordered', '6')
    # ### (R321)(5)-(7): the registrations and the list
    rg = rd(p('data', 'b710_registrations.txt')) or ''
    add('ruling (5)', 'data/b710_registrations.txt (ii) the surgery and (iii) the coefficient observation', '(ii) THE SURGERY AT Q0' in rg and '(iii) THE COEFFICIENT OBSERVATION' in rg,
        'data/b710_registrations.txt :51, :71', '3')
    rpt = rd(p('data', 'b709_report.txt')) or ''
    add('ruling (5)', 'each family`s onset radius (data/b709_report.txt :16: the band at rung log 32381, rho_0 at the midpoint of log 929 and log 937)',
        'rung log 32381' in rpt and 'midpoint between log 929 and log 937' in rpt, 'data/b709_report.txt :16', '3')
    add('ruling (5)', 'n = e^{10.39} past the band`s onset rung 32381', 2.718281828459045 ** 10.39 > 32381, 'e^10.39 = %.1f' % (2.718281828459045 ** 10.39), '3')
    add('ruling (5)', '"the least height of a certified zero with Re rho > 1 in the extended list" -- the list`s off-line search region (data/b709_pairs.txt :7-:8)',
        'sigma >= 1/2 + 0.02' in ' '.join(lines_of(p('data', 'b709_pairs.txt'))[6:8]), 'data/b709_pairs.txt :7 the right half-strip sigma >= 1/2 + 0.02, its upper sigma read from the tool', '3')
    r9 = rd(p('data', 'b709_registrations.txt')) or ''
    add('ruling (6)', 'data/b709_registrations.txt`s representation-coordinates row', '(e) REPRESENTATION COORDINATES' in r9 and 'HYPOTHESIS' in r9 and 'FALSIFIER' in r9,
        'data/b709_registrations.txt :10-:58', '3')
    add('ruling (6)', 'the ranking`s row data/b705_i6_ranking.txt :58', '(e) representation coordinates' in at(lines_of(p('data', 'b705_i6_ranking.txt')), 58), 'data/b705_i6_ranking.txt :58', '3')
    add('ruling (7)', 'W-ORD-Q0-ZEROS-443 at OPEN_TRAILS :15764', 'W-ORD-Q0-ZEROS-443' in at(ot, 15764), 'OPEN_TRAILS :15764', '4')
    pr = lines_of(p('data', 'b709_pairs.txt'))
    add('ruling (7)', 'the list complete to 325; pair 11 needing 405.4 and pair 15 442.3', 'THE LIST COMPLETE TO T0` = 325' in at(pr, 36) and 'T0` needed > 405.4' in at(pr, 52) and 'T0` needed > 442.3' in at(pr, 56),
        'data/b709_pairs.txt :36, :52, :56', '4')
    bands = [round(K.LIST_FROM + K.LIST_STEP * i, 1) for i in range(9) if K.LIST_FROM + K.LIST_STEP * i <= K.LIST_TO + K.LIST_STEP]
    add('ruling (7)', 'the bands from 325 in fifteens to past 443', bands[-1] >= 443, 'the band edges %s -- %d bands' % (bands, len(bands) - 1), '4')
    add('ruling (7)', 'pair 11 and 15`s refined predictions in data/b710_registrations.txt (i)', '12294837' in rg and '14776940' in rg and '[0.9, 1.1]' in rg, 'data/b710_registrations.txt :34-:37', '4')
    add('ruling (7)', 'b709`s foreground form (tools/b709_pairs.py, its bands)', os.path.exists(p('tools', 'b709_pairs.py')), 'tools/b709_pairs.py', '4')
    # ### (R321)(8): the branches
    merged = g(ROOT, 'branch', '--merged', 'main')[1] or ''
    mpp = g(PP, 'branch', '--merged', 'main')[1] or ''
    for repo, names in K.DELETE:
        lst = merged if repo == 'D:/relay' else mpp
        for b in names:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    push710 = sorted(x.strip(' *') for x in merged.split(NL) if x.strip(' *').startswith('push-b710')) + sorted(x.strip(' *') for x in mpp.split(NL) if x.strip(' *').startswith('push-b710'))
    add('ruling (8)', 'the push-b710 branches of the relay and of PLACE-papers are the eight the worklist names', len(push710) == 8 == sum(len(n) for _r, n in K.DELETE), 'listed %s' % push710, '0')
    lh = _remote_heads(K.LV_DIR)
    add('ruling (8)', 'port-b707 at 92af8a34 locally and at the remote, NOT deleted (one ls-remote of SIDE-lv-conservation)', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    st = g(ROOT, 'status', '--porcelain', '--', 'data/b710_closing_push_out.txt')[1] or ''
    add('ruling (8)', 'data/b710_closing_push_out.txt uncommitted at the act`s start (the closing b0d874f7 pushed and read back at :5)', st.startswith('??') and 'b0d874f7' in at(lines_of(p('data', 'b710_closing_push_out.txt')), 5),
        'git status %r ; :5' % st.strip(), '0')
    add('ruling (8)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b711_worklist.py HOLD', '0')
    # ### (R321)(9)-(11)
    add('ruling (9)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ruling (9)', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'tools/mirror_prevbuild.json', '5')
    add('ruling (11)', 'the faces row (the faces page)', os.path.exists(os.path.join(PP, K.FACES_PAGE)), 'PLACE-papers %s' % K.FACES_PAGE, '6')
    # ### the ferry's standing references
    add('ferry C5', 'data/b675_rules.txt row 1', '(1)' in (rd(p('data', 'b675_rules.txt')) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry C5', 'the four standing arms` figures tool and b710`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b710_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b710_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', os.path.exists(p('data', 'b684_rules.txt')), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'the chain halves as b693 drew them, b711 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b711'), 'tools/b711_worklist.py CHAIN_HALVES', '5')
    add('ferry C0', 'this act`s session transcript (a new session) and b710`s', os.path.exists(C.SESSION) and os.path.exists('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.PREV_SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b710_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R321)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b710_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b710_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R321)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b711_citation_check.txt', 'b711_citation_check.json'):
        MEM.guard('b711', n_, _root_exclude())
    for name, data in (('b711_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b711_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b711 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR OR ENTERED BY THE FACT CLAUSE BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b711_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b711_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b711_ferry_scan.txt')
    MEM.guard('b711', 'b711_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b711_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### b706's repair of the answer checker (b705 defect (n)), carried: a token that a bank's row names as a sha256 -- the root list, a hashes
# ### bank's row, a bank line carrying "sha256" -- or that a kernel's lakefile or manifest pins as a rev, is not a commit.
_HEX8 = re.compile(r'(?<![0-9a-f])([0-9a-f]{8})(?![0-9a-f])')


def _sha_rows():
    out = {}
    for q in [os.path.join(D, 'act_roots.txt')] + sorted(glob.glob(os.path.join(D, '*.txt')), reverse=True):   # ### the later act's row named first
        t = rd(q) or ''
        if 'sha256' not in t and not q.endswith('act_roots.txt') and not q.endswith('_hashes.txt'):
            continue
        for i, l in enumerate(t.split(NL), 1):
            if 'sha256' in l or q.endswith('act_roots.txt') or q.endswith('_hashes.txt'):
                for m in re.finditer(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])', l):
                    out.setdefault(m.group(1)[:8], ('data/' + os.path.basename(q), i))
    for kd in sorted(d_ for d_ in os.listdir('D:/') if d_.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d_, '.git'))):
        for f in ('lakefile.toml', 'lakefile.lean', 'lake-manifest.json'):
            t = rd(os.path.join('D:/', kd, f)) or ''
            for i, l in enumerate(t.split(NL), 1):
                for m in re.finditer(r'(?:rev\s*=\s*"|"rev"\s*:\s*"|@\s*"|rev\s+")([0-9a-f]{40})"', l):
                    out.setdefault(m.group(1)[:8], ('%s/%s' % (kd, f), i))
    return out


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b711, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b711'))
    shas = _sha_rows()
    base = P.C._user_texts

    def masked(*k, **kw):
        out = []
        for t in base(*k, **kw):
            if t and needle in t:
                for m in _HEX8.finditer(t):
                    h8 = m.group(1)
                    if h8 in shas:
                        print('  ### SHA256 PREFIX %s... NAMED BY %s :%d -- a root or file hash by its bank`s row, not a commit; OK, masked from the commit reading' % (h8, shas[h8][0], shas[h8][1]))
                        t = t.replace(h8, 'SHA-' + h8[:4] + '-' + h8[4:])
            out.append(t)
        return out

    P.C._user_texts = masked
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b711')
    # ### (R321)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b710's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b711', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b711)', 'exec'), ns)
    ns['answer'](needle)


def replay(needle, session_id, anchor, *a):
    """`replay <needle> <session id> <anchor>`: the repair's control, print only -- b682's selection (:210-:219, the latest user text after the
    anchor carrying the needle and an answer's mark) over the named session, then its cut two ways: b682's (`best.find('END', k)`) and the
    repaired (`best.rfind('END')`); each cut's length and its last 60 characters printed; nothing written."""
    import b682_citation as P
    P.C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % session_id
    P.C.SESSIONS_AFTER = ()
    best, seen = None, False
    for t in P.C._user_texts():
        if anchor in t:
            seen = True
        u = t.replace('\u2019', "'")
        if seen and needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u
                                     or 'user has answered' in u):
            best = t
    if best is None:
        print('  ### NO ANSWER CARRYING %r AFTER %r IN SESSION %s' % (needle, anchor, session_id))
        return
    k = best.find(needle)
    out = {}
    for label, e0 in (('b682', best.find('END', k)), ('repaired', best.rfind('END'))):
        b0 = best.rfind('BEGIN', 0, k)
        cut = best[b0:e0 + 3] if b0 >= 0 and e0 > k else best
        out[label] = cut
        print('  %-8s cut: %d characters ; ends %r' % (label, len(cut), cut[-60:]))
    print('  the whole answer %d characters ; the repaired cut equal to the text from its BEGIN to its last END: %s' % (
        len(best), out['repaired'] == best[best.rfind('BEGIN', 0, k):best.rfind('END') + 3]))
    return dict((k_, len(v)) for k_, v in out.items())


def word(needle, *a):
    """(R278)(4) on an author's word delivered as a bare BEGIN ... END paste: b694's route."""
    import b682_citation as P
    base = C._user_texts

    def marked(*k, **kw):
        return [("THE AUTHOR'S WORD " + t) if (t or '').lstrip().startswith(('BEGIN', '<pasted_content')) and 'END' in (t or '') else t
                for t in base(*k, **kw)]

    C._user_texts = marked
    P.C._user_texts = marked
    answer(needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer, 'word': word, 'replay': replay}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
