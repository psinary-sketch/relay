# -*- coding: utf-8 -*-
"""b642_record.py -- THE ACT'S RECORD TOOL, UNDER (R252). ### ONE SUBCOMMAND PER BANK.

### ### b642: LANE THREE, ACT SIXTY-NINE -- SIDE-EXPLICIT-FORMULA v0.26 ON A BRANCH; THE EPSTEIN RUNGS PRICED FROM THE PIN; THE SQUEEZE'S
### COMPILED JAW NAMED. Subcommands write only `data/b642_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad.
### The generic helpers are b633's, b639's and b641's record tools', imported; ledger appends through b566's guarded `append_to`. The
### kernel's modules are written by the seat through the Edit tool on the branch; this tool reads them, builds nothing itself, and banks the
### watchdog logs of the detached builds. No platform is called.
"""
import collections
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b641_record as R41  # noqa: E402
import b642_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'e594f88a-2fab-4757-943d-7ab1bc3de815'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b642_registration_2026-10-08.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of, _nd, predict_cells, _land = R3.lines_of, R3._nd, R3.predict_cells, R3._land
kern_state, sorry_tokens = R3.kern_state, R3.sorry_tokens
KERNS_READ = R41.KERNS_READ
_poss = R41._poss
OAI_NEEDLES = R41.OAI_NEEDLES


def put_txt(name, L):
    _write(os.path.join(SP if DRY else D, name), (NL.join(L) + NL).encode('utf-8'))


def put_json(name, j):
    _write(os.path.join(SP if DRY else D, name), (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def jl(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    try:
        return io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b642_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b642 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b642_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b642_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('relay data/b641_keiper_status.txt: every candidate statement', RELAY, PRE_RELAY, 'data/b641_keiper_status.txt', ('GREP', r'CANDIDATE|^### \(\w\d\)'), 300),
        ('relay data/b641_window_epstein_status.txt: every candidate statement', RELAY, PRE_RELAY, 'data/b641_window_epstein_status.txt',
         ('GREP', r'CANDIDATE|^### \(\w\d\)'), 300),
        ('relay data/b641_premise_status.txt: the Dedekind candidates and statuses', RELAY, PRE_RELAY, 'data/b641_premise_status.txt',
         ('GREP', r'CANDIDATE|^### \(D\d\)|STATUS :|WITNESS CLASS|VALUE :|COUNTEREXAMPLE|SUFFICIENT|row resting'), 300),
        ('SIDE-explicit-formula: the Keiper definitions the statements name', K.EF, K.EF_PIN, 'SIDEExplicitFormula/Keiper.lean',
         [47, 73, 76, 79, 82, 86, 89, 92, 95, 101, 107, 117, 122, 126], 220),
        ('SIDE-explicit-formula: the window definitions', K.EF, K.EF_PIN, 'SIDEExplicitFormula/Schema/PlateauRamp.lean', [19, 20, 21, 45, 48, 51, 55, 173, 178, 181], 220),
        ('SIDE-explicit-formula: Family.lean`s two premises', K.EF, K.EF_PIN, 'SIDEExplicitFormula/Schema/Family.lean', [255, 256, 257, 261, 264, 265, 269, 270], 220),
        ('SIDE-explicit-formula: dedekind_rhs and dedekind_three', K.EF, K.EF_PIN, 'SIDEExplicitFormula/Schema/Dedekind.lean', [55, 56, 57, 58, 59, 60, 61, 62, 70, 71, 72], 220),
        ('SIDE-explicit-formula: EpsteinPremises at v0.16', K.EF, K.EPSTEIN_PIN, 'SIDEExplicitFormula/Schema/Epstein.lean', [38, 39, 40, 41, 42, 43, 44], 220),
        ('Mathlib at the pin: the convolution theorem', K.EF + '/.lake/packages/mathlib', K.MATHLIB_PIN, 'Mathlib/Analysis/Fourier/Convolution.lean',
         [116, 117, 118, 119, 120, 121], 200),
        ('the census at v0.6: the premise table (:958-:1019), 60 rows -- the 50 heads of b640`s status bank and the rows read by the '
         'elaborated reader alone', PP, PRE_PP, K.CEN6, list(range(958, 1020)), 200),
        ('Zeta23 at 3635e748: ZetaZeroFree', K.Z23, K.Z23_PIN, K.ZZF_FILE, list(range(K.ZZF_LINE_SOURCE, K.ZZF_LINE_SOURCE + 6)), 220),
        ('SIDE-explicit-formula`s vendored copy at 8c51431: ZetaZeroFree', K.EF, K.EF_PIN, K.ZZF_FILE, list(range(K.ZZF_LINE_VENDORED, K.ZZF_LINE_VENDORED + 6)), 220),
        ('THE_UNCONDITIONAL_SURROUND v0.5: section 6a', PP, PRE_PP, K.SURROUND, ('GREP', r'^## 6a|One jaw is the Euler|no zero-free region'), 400),
        ('OPEN_TRAILS: the form clause, the build lines, the test-pin line, the patch work-order, b641`s block, its correction', PP, PRE_PP,
         'OPEN_TRAILS.md', sorted(set(K.FERRY_LINES + (K.STMT_PIN_BLOCK,))), 900),
        ('FINDINGS: b641`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B641_ENTRY], 400),
        ('relay data/b641_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b641_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    L = ['b642 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)] if isinstance(sel, tuple) else \
            [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    zl = io.open(os.path.join(SP, 'zzf_1.log'), encoding='utf-8', errors='replace').read() if os.path.exists(os.path.join(SP, 'zzf_1.log')) else ''
    L += ['### ZetaZeroFree`s #check and #print axioms, read at SIDE-explicit-formula 8c51431`s built vendored module (lake env lean, detached; '
          'the scratchpad`s zzf_1.log):'] + ['    ' + l for l in zl.split(NL) if l.strip() and not l.startswith('### SAMPLE')]
    L += ['', '### the ruling`s ":2485 at 3635e748" read beside both: :2485 is the vendored copy`s line at 8c51431; at 3635e748 the lemma is at '
          ':%d and :2485 falls inside LogDerivZetaBnd; the statement at the two lines byte-identical.' % K.ZZF_LINE_SOURCE,
          '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### the branch: SIDE-explicit-formula %s at %s ; main %s' % (K.EF_BRANCH, g(K.EF, 'rev-parse', K.EF_BRANCH).strip()[:12],
                                                                        g(K.EF, 'rev-parse', 'main').strip()[:12]),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b642_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()) + 1, len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R252) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b642 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in since:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not since:
        L.append('### NONE: no prompt has been put to the author in this act.')
    put_txt('b642_author_answers.txt', L)
    print('  prompts banked: %d' % n)


def answer_of(k):
    R3.rd = lambda name: rd('b642_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b642_kernels_face.json', dict(at=utc(), kernels=kern_state(list(KERNS_READ))))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R252)(1), (2) AND (5)
W_HEAD = '*Appended 2026-10-08 by b642 to b641’s entry (:%d), under `(R252)`(1) -- b641 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
OR_HEAD = ('*Appended 2026-10-08 by b642 to b641’s record (:%d), under `(R252)`(2) -- THE ORDER OF `(R251)`(8) REVERSED: b642 THE PROVING ACT, '
           'b643 THE CENSUS:*')
SQ_HEAD = ('*Appended 2026-10-08 by b642 beneath `(R251)`(7)’s block (:%d), under `(R252)`(5) -- A CORRECTION IN THE NAVIGATOR’S NAME: '
           'W-ORD-H2-STRIP-AXIS WITHDRAWN; THE SQUEEZE’S COMPILED JAW NAMED:*')
LA_HEAD = '*Appended 2026-10-08 by b642, under `(R252)`(5) -- W-ORD-H2-LATTICE, ENTERED, NOT ACTED, TRIGGER THE AUTHOR’S WORD AFTER b643’S CENSUS:*'
PI_HEAD = ('*Appended 2026-10-08 by b642, under `(R252)`(5) -- W-ORD-H2-PI1, ENTERED, NOT ACTED, TRIGGER THE AUTHOR’S WORD BEFORE THE OPENING OF '
           'THE CENSUS AT v0.7 IS WRITTEN:*')


def _zzf():
    t = io.open(os.path.join(SP, 'zzf_1.log'), encoding='utf-8', errors='replace').read() if os.path.exists(os.path.join(SP, 'zzf_1.log')) else ''
    ax = re.search(r"'ZetaZeroFree' depends on axioms: \[([^\]]*)\]", t)
    src = lines_of(_show(K.Z23, K.Z23_PIN, K.ZZF_FILE) or '')
    stmt = ' '.join(x.strip() for x in src[K.ZZF_LINE_SOURCE - 1:K.ZZF_LINE_SOURCE + 5])
    return stmt, (ax.group(1) if ax else None)


def _weight():
    S, J, PS = jl('b641_scores.json'), jl('b641_act_root.json'), jl('b641_premise_status.json')
    pre = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b641_checks.txt'))
    post = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b641_checks_postpush.txt'))
    nd = len(jl('b641_defects.json').get('defects') or [])
    na = len(re.findall(r'^### PROMPT ', rd('b641_author_answers.txt'), re.M))
    sh = jl('b641_seal_hashes.json')
    ded = dict((x['key'], x['status']) for x in PS.get('dedekind') or [])
    return ('\n%s the needle (relay c607f25c): an assertion matches, a denial does not, the three hand-read answers 3 of 3, N1 %s. The root '
            'order (relay a2b0c105): a root leaving out the act`s seal bank refused, the root`s time recorded, a named bank written after it '
            'read DISAGREE, its test 5 of 5. Step zero 32 of 32. Keiper`s seven OPEN, the window`s two OPEN, the Epstein count field OPEN; '
            'TrivialSummandPremise %s, the seat`s computation, not compiled, dedekind_rhs at v0.25 a theorem on a premise with no witness, its '
            'grade unchanged and its row annotated; EulerFactorPremise %s; the seven patch versions resolved, none written. The phrase entered '
            'PLACE-papers at b39217fe naming no ruling and relay at bf2405b9 under (R63) and (R64), reusable with that provenance. The '
            'outside read banked, the ledgers carrying the neutral clause. %d edits after the seal, each declared, the sealed tools agreeing '
            '7 of 7. The suite %s of %s pre-push and %s of %s post-push, the root arm failing on b640`s chain line, which disagrees on two '
            'banks after b640`s closing commit re-wrote its answers bank past its root; b641`s own root agrees; b640`s line annotated, not '
            'recomputed. Defects (a)-(h), %d, as the seat listed them; the entry`s count corrected at OPEN_TRAILS :%d. %d prompts. Relay '
            '78488b56 and 10fdca58; PLACE-papers 93db626; the root %s… (previous b640`s). Nothing deposited; no kernel source touched.\n' % (
                W_HEAD % K.B641_ENTRY, (S.get('N1') or ['?'])[0], ded.get('D1', '?'), ded.get('D2', '?'), len(sh.get('amendments') or []),
                pre.group(2) if pre else '?', pre.group(1) if pre else '?', post.group(2) if post else '?', post.group(1) if post else '?',
                nd, K.B641_CORRECTION, na, (J.get('root') or '?')[:16]))


def _order_text():
    return ('\n%s `(R251)`(8) named b642 the census; the research changed what the census would count -- five declarations ripe and a '
            'premise refuted -- so b642 is the proving act (SIDE-explicit-formula v0.26 on a branch from v0.25 = 8c51431) and b643 the census '
            'at v0.7 with six statuses, which reads the repaired kernel once. The navigator’s sentence at b641, "constructs one", reads '
            '"constructs the function"; the instance exists at v0.16 (SIDEExplicitFormula/Schema/Epstein.lean at c404e72).\n' % (OR_HEAD % K.B641_RECORD))


def _squeeze_text():
    stmt, ax = _zzf()
    return ('\n%s W-ORD-H2-STRIP-AXIS, as the navigator proposed it at b641, is WITHDRAWN: the θ-jaw is THE_UNCONDITIONAL_SURROUND §6a’s '
            'Euler jaw (phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md, section 6a: "One jaw is the Euler zero-free region ... pressing in '
            'from σ = 1"), not a new axis. The compiled Euler jaw is ZetaZeroFree, read by the seat at Zeta23/FromPNTPlus/ZetaBounds.lean :%d '
            'at 3635e748 and in SIDE-explicit-formula’s vendored copy at :%d at 8c51431, the statement at the two lines identical: "%s" -- its '
            'axiom print, read at the built vendored module: [%s], the standard three. The ruling’s ":2485 at 3635e748" names the vendored '
            'copy’s line; at 3635e748 :2485 falls inside LogDerivZetaBnd. The transversality jaw stands at question grade, its width the '
            'derivative’s modulus at a zero, its target close-pair control at height.\n' % (
                SQ_HEAD % K.STMT_PIN_BLOCK, K.ZZF_LINE_SOURCE, K.ZZF_LINE_VENDORED, stmt.replace(':= by', '').strip(), ax or '### NOT READ'))


def _lattice_text():
    return ('\n%s the closure table regenerated from grades by the terminal-table tool, on the axes height, test class, instance, register '
            'and family, so that every cell of the squeeze reads a compiled grade or its absence. Not acted at b642.\n' % LA_HEAD)


def _pi1_text():
    return ('\n%s the Π⁰₁ form of RH read at its source (Kreisel; Davis, Matijasevič and Robinson 1976) and, if it stands, the three terminal '
            'states stated in one paragraph at the census’s opening. Not acted at b642.\n' % PI_HEAD)


def record_lines(*a):
    """### Component 1, (R252)(1), (2) and (5): FINDINGS, b641 at its weight (to :7939); OPEN_TRAILS, the order clause (to b641's record),
    ### the squeeze correction beneath (R251)(7)'s block, W-ORD-H2-LATTICE and W-ORD-H2-PI1."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The needle and the root order; ')
    if entry != K.B641_ENTRY:
        sys.exit('### b641`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    if _zzf()[1] is None:
        sys.exit('### ZetaZeroFree`S AXIOM PRINT NOT READ -- NOTHING WRITTEN')
    items = [('FINDINGS.md', W_HEAD % K.B641_ENTRY, _poss(_weight())), ('OPEN_TRAILS.md', OR_HEAD % K.B641_RECORD, _poss(_order_text())),
             ('OPEN_TRAILS.md', SQ_HEAD % K.STMT_PIN_BLOCK, _poss(_squeeze_text())), ('OPEN_TRAILS.md', LA_HEAD, _poss(_lattice_text())),
             ('OPEN_TRAILS.md', PI_HEAD, _poss(_pi1_text()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None') if x in allt]
    oai_ = [n for n in OAI_NEEDLES if n in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks: %s ; unread figures: %s ; the collection named: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', oai_ or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread or oai_:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    _land(Q, items, 'b642_record_lines.json', K.B641_ENTRY)


# ================================================================================ COMPONENT 2: THE DECLARATIONS, (R252)(3)(a)-(d)
STD3 = '[propext, Classical.choice, Quot.sound]'
DECL_MODS = [('KeiperIdentities', 'SIDEExplicitFormula/KeiperIdentities.lean', '(3)(a)'),
             ('WindowProofs', 'SIDEExplicitFormula/Schema/WindowProofs.lean', '(3)(b)'),
             ('FamilyPremises', 'SIDEExplicitFormula/Schema/FamilyPremises.lean', '(3)(c)'),
             ('DedekindRestated', 'SIDEExplicitFormula/Schema/DedekindRestated.lean', '(3)(d)')]
DOC_MODS = [('Family', 'SIDEExplicitFormula/Schema/Family.lean', '(3)(d) docstring'),
            ('Dedekind', 'SIDEExplicitFormula/Schema/Dedekind.lean', '(3)(d) docstring')]


def _ef(*a):
    return subprocess.run(['git', '-C', K.EF] + list(a), capture_output=True, text=True, encoding='utf-8').stdout.strip()


def _axlog(tag):
    """the watchdog log of one AxiomCheck run: (text, [(name, set)], [names with no axiom]); wrapped prints joined."""
    p = os.path.join(SP, 'ax_%s.log' % tag)
    t = io.open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    j = re.sub(r',\s*\n\s*', ', ', t)
    return (t, re.findall(r"'([^\n]*?)' depends on axioms: (\[[^\]]*\])", j),
            re.findall(r"'([^\n]*?)' does not depend on any axioms", j))


def _buildlogs():
    L = []
    for f in sorted(x for x in os.listdir(SP) if (x.startswith('build_') or x.startswith('ax_')) and x.endswith('.log')):
        t = io.open(os.path.join(SP, f), encoding='utf-8').read().splitlines()
        st = [x for x in t if x.startswith('### START')]
        ex = [x for x in t if x.startswith('### EXIT')]
        fr = [int(v) for x in t if x.startswith('### ') for v in re.findall(r'free (\d+) MB', x)]
        lo = min(fr) if fr else None
        s0 = re.search(r'free (\d+)', st[0]).group(1) if st else '?'
        L.append('%s: start free %s MB; lowest sampled free %s MB%s; %s' % (
            f, s0, lo, '  CROSSING below the hold' if lo is not None and lo < 2560 else '', ex[-1][4:] if ex else 'NO EXIT LINE'))
        L += ['    ' + x.strip() for x in t if re.search(r'\] Built SIDEExplicitFormula', x)]
    return L


def declarations(*a):
    """data/b642_declarations.txt: the branch's commits each with its stat, the modules' blobs and sha256, every #print axioms of the
    four AxiomCheck runs with the #check statements verbatim, and every watchdog log's start, lowest sampled and exit free memory."""
    L = ['b642 -- DECLARATIONS OF THE PROVING ACT (ruling (R252)(2)-(3)), SIDE-explicit-formula branch %s' % K.EF_BRANCH,
         'base %s (v0.25); HEAD %s; Lean v4.34.0-rc1, Mathlib de5ce8a9.' % (K.EF_PIN, _ef('rev-parse', K.EF_BRANCH)),
         'Every #print axioms below is the compiler`s output, read from the run log named; wrapped prints joined. Nothing here deposits.',
         '', '== COMMITS ON %s (oldest first), each alone, its stat printed' % K.EF_BRANCH, '']
    for line in _ef('log', '--reverse', '--format=%H %s', '%s..%s' % (K.EF_PIN, K.EF_BRANCH)).splitlines():
        L.append(line)
        L.append('    ' + _ef('show', '--stat', '--format=', line.split()[0]).replace(NL, NL + '    '))
    L += ['', '== MODULES: blob sha at the branch, sha256 of the working file, lines', '']
    for _m, p, cl in DECL_MODS + DOC_MODS:
        b = open(os.path.join(K.EF, p), 'rb').read()
        L.append('%s  %s  blob %s  sha256 %s  lines %d' % (p, cl, _ef('rev-parse', '%s:%s' % (K.EF_BRANCH, p)),
                                                           hashlib.sha256(b).hexdigest(), b.count(b'\n')))
    tot = bad = 0
    for m, _p, cl in DECL_MODS:
        t, prints, nodep = _axlog(m)
        std = sum(1 for _n, s in prints if s == STD3)
        tot += len(prints) + len(nodep)
        bad += len(prints) - std + ('sorryAx' in t)
        L += ['', '== %s -- ruling %s; AxiomCheck%s.lean, run log ax_%s.log' % (m, cl, m, m), '']
        L += [x for x in t.splitlines() if x.startswith('### ') and not x.startswith('### SAMPLE')][-2:]
        L.append('prints %d; at exactly %s: %d; with no axiom: %d; other: %d; sorryAx in the log: %s' % (
            len(prints) + len(nodep), STD3, std, len(nodep), len(prints) - std, 'sorryAx' in t))
        L += ['  %s: %s' % (n, s) for n, s in prints] + ['  %s: NO AXIOM' % n for n in nodep]
        L.append('-- #check (the statements, verbatim from the compiler):')
        body = [x for x in t.splitlines() if not x.startswith('### ')]
        k = max([i for i, x in enumerate(body) if 'depends on axioms' in x or 'does not depend' in x] or [-1])
        rest = body[k + 1:]
        while rest and not re.match(r'^[A-Za-z@]', rest[0]):
            rest = rest[1:]
        L += ['  ' + x for x in rest]
    L += ['', '== TOTAL: %d prints over the four modules; beyond the standard three or sorryAx: %d' % (tot, bad), '',
          '== WATCHDOG LOGS (build1.py, detached); the hold is 2,560 MB of free memory, read at the start', ''] + _buildlogs()
    print('  prints %d ; beyond the standard three or sorryAx %d ; lines %d' % (tot, bad, len(L)))
    put_txt('b642_declarations.txt', L)


# ================================================================================ COMPONENT 3: NON-VACUITY, (R252)(3)(e)
NV_FILE = 'SIDEExplicitFormula/SaltCheckNonvacuity.lean'
# ### head -> ('W', [(repo, rev, file, theorem)], degenerate note or '') | ('U', class, reason). New witnesses are this act's Salt module
# at the branch; existing ones the census's salt cells at their pins, each re-read below by its theorem line.
_N = ('SIDE-explicit-formula', K.EF_BRANCH, NV_FILE)
_LIB = 'a library predicate the table carries as DOMAIN, witnessed at the type its consumers use'
NV = {
    'AnalyticOnNhd': ('W', [_N + ('analyticOnNhd_witness',)], ''),
    'Continuous': ('W', [_N + ('continuous_witness',)], ''),
    'EqOn': ('W', [_N + ('eqOn_witness',)], ''),
    'HasCompactSupport': ('W', [_N + ('hasCompactSupport_witness',),
                                ('SIDE-explicit-formula', K.EF_PIN, 'SIDEExplicitFormula/Schema/SaltCheckPlateauRamp.lean',
                                 'window_even_compact_at_seven')], ''),
    'HasDerivAt': ('W', [_N + ('hasDerivAt_witness',)], ''),
    'Integrable': ('W', [_N + ('integrable_witness',)], ''),
    'IsOpen': ('W', [_N + ('isOpen_witness',)], ''),
    'IsRoot': ('W', [_N + ('isRoot_witness',)], ''),
    'Monotone': ('W', [_N + ('monotone_witness',)], ''),
    'Prime': ('W', [_N + ('nat_prime_witness',), _N + ('prime_witness',)], ''),
    'StrictMono': ('W', [_N + ('strictMono_witness',)], ''),
    'Tendsto': ('W', [_N + ('tendsto_witness',)], ''),
    'PWSetup': ('W', [_N + ('pwSetup_zero',)], 'DEGENERATE: the zero base at L = 0, M = 1, every score 0; the structure is not empty, its '
                'consumers` bases are not witnessed'),
    'farSmall': ('W', [_N + ('farSmall_zero',)], 'DEGENERATE: the zero base, both sides 0; Component 3`s hypothesis at a non-zero base is '
                 'not witnessed'),
    'PlattTrudgianHeight': ('W', [_N + ('plattTrudgianHeight_neg_one',)], 'DEGENERATE: the height -1, an empty range; at plattTrudgianT '
                            '(3 * 10^12) the premise stays CITED, not witnessed'),
    'zeroSideNeg': ('W', [_N + ('zeroSideNeg_witness',)], ''),
    'SymPairBound': ('W', [_N + ('symPairBound_witness',)], ''),
    'ZetaSeam': ('W', [_N + ('zetaSeam_witness',)], ''),
    'IsTrivialPoint': ('W', [_N + ('isTrivialPoint_parity',)], ''),
    'EulerFactorPremise': ('W', [_N + ('eulerFactorPremise_witness',)], ''),
    'WindowObligations': ('W', [_N + ('windowObligations_witness',)], ''),
    'EpsteinPremises': ('W', [('SIDE-explicit-formula', K.EF_PIN, 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'toy_premises'),
                              ('SIDE-explicit-formula', K.EF_PIN, 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'empty_premises')], ''),
    'HCount': ('W', [('SIDE-explicit-formula', K.EF_PIN, 'SIDEExplicitFormula/SaltCheckSimplicity.lean', 'toy_count'),
                     ('SIDE-explicit-formula', K.EF_PIN, 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'toy_count')], ''),
    'IsExpansion': ('W', [('SIDE-lv-conservation', '2f71068', 'SIDELvConservation/SaltCheck_LeadLaw.lean', 'expansion_exists_of_palindromic'),
                          ('SIDE-lv-conservation', '2f71068', 'SIDELvConservation/SaltCheck_LeadLaw.lean', 'expansion_at_zero')], ''),
    'TrivialSummandPremise': ('U', 'REFUTED', 'refuted in the kernel at b642: Schema/FamilyPremises.lean not_trivialSummandPremise proves '
                              '¬ TrivialSummandPremise, so no witness exists; the restated TrivialSummandPremise` is witnessed (the added row)'),
    'BoundPremises': ('U', 'CONTENT', 'its fields are certified digit claims (Euler`s gamma to the table`s width, the Stieltjes constants 1 to 11, '
                      'zeta at 2 to 12); a witness is their proof, and no compiled proof exists at v0.26 (B1-B3 named WITNESSED candidates by '
                      'interval arithmetic at b641, not compiled)'),
    'KeiperObligations': ('U', 'CONTENT', 'three of its four fields are proved at b642 (binomialTransform_holds, logDerivSplit_holds, '
                          'stieltjesLog_holds); the fourth, gammaZeta (GammaRZetaValues, obligation (O4)), has no compiled proof at v0.26'),
    'NymanBeurlingPremise': ('U', 'CONTENT', 'its one field is NB <-> RiemannHypothesis, the classical equivalence, CITED; no proof of it is '
                             'in the kernel or in Mathlib at de5ce8a9'),
}
NV_OTHER = ('declared in %s (%s:%d at %s); that kernel has no Salt module naming it at its pin (git grep over its files named *salt*: %d '
            'files, 0 hits) and is not importable from SIDE-explicit-formula; no kernel but SIDE-explicit-formula is written this act '
            '((R252) N5)')
NV_ADDED = ('TrivialSummandPremise`', [_N + ("trivialSummandPremise'_witness'",)], 'the head this act adds ((R252)(3)(d)); outside the 50')


def _theorem_line(repo, rev, path, name):
    src = lines_of(_show('D:/' + repo, rev, path) or '')
    pat = re.compile(r'^theorem %s(?=[\s:({\[]|$)' % re.escape(name))
    return [i + 1 for i, x in enumerate(src) if pat.match(x)]


def nonvacuity(*a):
    """data/b642_nonvacuity.txt: the census's 50 heads (b641's premise table, census v0.6), each WITNESSED by a theorem in a
    Salt module (its line re-read at its revision; the new ones` #print axioms from ax_Nonvacuity.log) or UNWITNESSED with the reason;
    counts by outcome, then each outcome's rows. Refuses to write if a head has no outcome, two, or a cited theorem is not found."""
    P = jl('b641_premise_status.json')
    heads = P.get('heads') or []
    _t, prints, nodep = _axlog('Nonvacuity')
    ax = dict((n.split('.')[-1], s) for n, s in prints)
    ax.update((n.split('.')[-1], 'NO AXIOM') for n in nodep)
    salt_files = {}
    rows, errs = [], []
    for v in heads:
        h = v['head']
        o = NV.get(h)
        if o is None:
            dcl = v.get('decl') or {}
            repo = dcl.get('repo')
            if not repo or repo == 'SIDE-explicit-formula':
                errs.append('%s: no outcome' % h)
                continue
            if repo not in salt_files:
                fl = subprocess.run(['git', '-C', 'D:/' + repo, 'ls-tree', '-r', '--name-only', dcl['pin']], capture_output=True,
                                             text=True, encoding='utf-8').stdout.split()
                salt_files[repo] = [f for f in fl if 'salt' in f.lower() and f.endswith('.lean')]
            sf = salt_files[repo]
            hits = subprocess.run(['git', '-C', 'D:/' + repo, 'grep', '-n', '-w', h, dcl['pin'], '--'] + sf, capture_output=True, text=True,
                                  encoding='utf-8').stdout.strip() if sf else ''
            if hits:
                errs.append('%s: salt hits in %s -- read them before UNWITNESSED' % (h, repo))
                continue
            why = NV_OTHER % (repo, dcl['file'], dcl['line'], dcl['pin'], len(sf))
            st = ['%s:%s %s' % (x['file'], x['line'], x['name']) for x in v.get('standalone') or []]
            if st:
                why += '; an in-kernel instance outside a Salt module, from b641`s bank: ' + ', '.join(st)
            rows.append(dict(head=h, outcome='UNWITNESSED', cls='OTHER-KERNEL', reason=why, was=v['status']))
            continue
        if o[0] == 'W':
            ws = []
            for repo, rev, path, name in o[1]:
                ln = _theorem_line(repo, rev, path, name)
                if len(ln) != 1:
                    errs.append('%s: %s not found once in %s at %s (%s)' % (h, name, path, rev, ln))
                new = path == NV_FILE
                ws.append(dict(repo=repo, rev=rev, file=path, line=ln[0] if ln else None, theorem=name,
                               new=new, axioms=ax.get(name) if new else 'at the pin`s own AxiomCheck'))
                if new and ax.get(name) not in (STD3, 'NO AXIOM'):
                    errs.append('%s: %s axioms %s' % (h, name, ax.get(name)))
            rows.append(dict(head=h, outcome='WITNESSED', cls='DEGENERATE' if o[2] else ('NEW' if any(w['new'] for w in ws) else 'EXISTING'),
                             witnesses=ws, note=o[2], was=v['status']))
        else:
            rows.append(dict(head=h, outcome='UNWITNESSED', cls=o[1], reason=o[2], was=v['status']))
    extra = [k for k in NV if k not in [v['head'] for v in heads]]
    if extra:
        errs.append('outcomes for heads not in the table: %s' % extra)
    nm, ws, note = NV_ADDED
    ln = _theorem_line(*ws[0])
    if len(ln) != 1 or ax.get(ws[0][3]) not in (STD3, 'NO AXIOM'):
        errs.append('%s: %s found at %s, axioms %s' % (nm, ws[0][3], ln, ax.get(ws[0][3])))
    added = dict(head=nm, outcome='WITNESSED', cls='ADDED', witnesses=[dict(file=NV_FILE, line=ln[0] if ln else None, theorem=ws[0][3],
                                                                            axioms=ax.get(ws[0][3]))], note=note)
    cnt = collections.Counter(r['outcome'] for r in rows)
    cls = collections.Counter((r['outcome'], r['cls']) for r in rows)
    L = ['b642 -- NON-VACUITY OVER THE PREMISE TABLE (ruling (R252)(3)(e), W-ORD-PREMISE-NONVACUITY acted)',
         'heads: %d, from data/b641_premise_status.json (the census v0.6 premise table`s 50 heads); Salt module %s at %s %s' % (
             len(heads), NV_FILE, K.EF_BRANCH, _ef('rev-parse', '--short', K.EF_BRANCH)),
         'rule (quoted): "a witness theorem or example in a Salt module, or the structure printed as UNWITNESSED in the bank with the reason".',
         'A DEGENERATE witness satisfies the structure where it says nothing; it is counted WITNESSED and named DEGENERATE beside the count.',
         '', '== COUNTS', '',
         'WITNESSED %d ; UNWITNESSED %d ; total %d ; both 0 ; neither %d' % (cnt['WITNESSED'], cnt['UNWITNESSED'], len(rows),
                                                                              len(heads) - len(rows))]
    L += ['  %s / %s: %d' % (k[0], k[1], n) for k, n in sorted(cls.items())]
    L.append('  WITNESSED and not DEGENERATE: %d' % sum(1 for r in rows if r['outcome'] == 'WITNESSED' and r['cls'] != 'DEGENERATE'))
    for oc in ('WITNESSED', 'UNWITNESSED'):
        L += ['', '== %s (%d)' % (oc, cnt[oc]), '']
        for r in rows:
            if r['outcome'] != oc:
                continue
            L.append('%s  [%s; b641 status %s]' % (r['head'], r['cls'], r['was']))
            for w in r.get('witnesses') or []:
                L.append('    %s %s:%s %s  axioms %s' % (w['repo'], w['file'], w['line'], w['theorem'], w['axioms']))
            if r.get('note'):
                L.append('    ' + r['note'])
            if r.get('reason'):
                L.append('    reason: ' + r['reason'])
    L += ['', '== THE ADDED ROW (outside the 50)', '', '%s  [ADDED] %s:%s %s  axioms %s' % (
        nm, NV_FILE, added['witnesses'][0]['line'], ws[0][3], added['witnesses'][0]['axioms']), '    ' + note]
    print('  ' + L[7])
    for x in L[8:8 + len(cls) + 1]:
        print(x)
    if errs:
        print(NL.join('  ### ' + e for e in errs))
        sys.exit('### NON-VACUITY: %d ERRORS -- NOTHING WRITTEN' % len(errs))
    put_txt('b642_nonvacuity.txt', L)


# ================================================================================ COMPONENT 5: THE GRADES AT THE ELABORATED READER
# ### Every new declaration is a name an AxiomCheck file at the branch prints; each module read by b634's reader (its generator and parser,
# ### imported) in ONE call that imports that module alone, run detached by the seat (lean_run.sh, the watchdog) and never by this tool. The
# ### changed declarations (docstrings only at b642) are read beside the new, in the module that imports them.
ELAB_DIR = os.path.join(SP, 'b642_elab')
ELAB_MODS = [('KeiperIdentities', 'SIDEExplicitFormula.KeiperIdentities', 'AxiomCheckKeiperIdentities.lean', []),
             ('WindowProofs', 'SIDEExplicitFormula.Schema.WindowProofs', 'AxiomCheckWindowProofs.lean', []),
             ('FamilyPremises', 'SIDEExplicitFormula.Schema.FamilyPremises', 'AxiomCheckFamilyPremises.lean',
              ['SIDEExplicitFormula.Schema.Family.TrivialSummandPremise']),
             ('DedekindRestated', 'SIDEExplicitFormula.Schema.DedekindRestated', 'AxiomCheckDedekindRestated.lean', []),
             ('Nonvacuity', 'SIDEExplicitFormula.SaltCheckNonvacuity', 'AxiomCheckNonvacuity.lean', [])]
CHANGED = ('SIDEExplicitFormula.Schema.Family.TrivialSummandPremise', 'SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs')
# ### the gate's grade is banked as printed; a row the seat reads otherwise carries its note beside it and is not regraded here.
GRADE_NOTES = {
    'SIDEExplicitFormula.Keiper.contDiff_riemannZeta₀': (
        'INSTRUMENT MISREADING, NOT REGRADED: the binder n : WithTop ℕ∞ is data (the smoothness order); e0_rule.typing has no lexicon entry '
        'for WithTop and reads it as an unlexed named predicate (typing prop, class B17, outcome premise). The shared rule is not edited at b642.'),
    'SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs\'': (
        '(R243)(2): TrivialSummandPremise` is a predicate the rule meets for the first time; it is printed, not graded INTERFACES. Both '
        'premises it takes are witnessed (trivialSummandPremise`_witness at the constant 1; eulerFactorPremise_three at q = 3).'),
    'SIDEExplicitFormula.Keiper.analyticAt_logDeriv': (
        '(R180)(2)(f) as written: IsOpen U and DifferentiableOn ℂ f U restrict U, which the conclusion does not mention, so they read as '
        'premises; a general lemma whose hypotheses its caller discharges (logDerivSplit_holds is DERIVES).'),
}


def _elab_names(ax):
    return re.findall(r'^#print axioms (\S+)', _show(K.EF, K.EF_BRANCH, ax) or '', re.M)


def elab_gen(*a):
    """the reader's files in the scratchpad, one per module (b634_elab.gen); prints each file's path and name count. Writes no bank."""
    import b634_elab as EL
    for tag, mod, ax, extra in ELAB_MODS:
        names = _elab_names(ax) + extra
        p = EL.gen(mod, names, os.path.join(ELAB_DIR, 'b642_elab_%s.lean' % tag))
        print('  %-18s %-48s names %3d  %s' % (tag, mod, len(names), p.replace('\\', '/')))


def grades(*a):
    """data/b642_grades.txt: each new and changed declaration's elaborated statement (b634's reader) and its E0 grade (tools/e0_rule.py,
    through b634_record's header), with its axioms from the module's AxiomCheck run; counts by grade and by module. Refuses if a name is
    MISSING, unread, or a reader run has no EXIT 0."""
    import b634_elab as EL
    import b634_record as R34
    import e0_rule as E
    L = ['b642 -- THE GRADES AT THE ELABORATED READER (ruling (R252)(3), Component 5), SIDE-explicit-formula %s %s' % (
        K.EF_BRANCH, _ef('rev-parse', '--short', K.EF_BRANCH)), ''] + E.RULE_TEXT + ['']
    errs, rows = [], []
    for tag, mod, ax, extra in ELAB_MODS:
        names = _elab_names(ax) + extra
        lg = os.path.join(SP, 'elab_%s.log' % tag)
        t = io.open(lg, encoding='utf-8').read() if os.path.exists(lg) else ''
        ex = [x for x in t.splitlines() if x.startswith('### EXIT')]
        if not ex or not ex[-1].startswith('### EXIT 0'):
            errs.append('%s: run log %s %s' % (tag, lg, ex[-1] if ex else 'has no EXIT line'))
        got = EL.parse(t)
        _t, prints, nodep = _axlog('Nonvacuity' if tag == 'Nonvacuity' else tag)
        axd = dict(prints)
        axd.update((n, 'NO AXIOM') for n in nodep)
        st = [x for x in t.splitlines() if x.startswith('### START')]
        L += ['== %s (%s), %d names; %s' % (tag, mod, len(names), ex[-1][4:] if ex else 'NO EXIT'),
              '   ' + (st[0][4:120] if st else 'NO START'), '']
        for n in names:
            e = got.get(n)
            if e is None or e.get('missing'):
                errs.append('%s: %s %s' % (tag, n, 'MISSING' if e else 'unread'))
                continue
            try:
                gr, why, _b = E.grade(R34._elab_header(e), 'theorem' if e['kind'] == 'theorem' else 'def')
            except Exception as x:   # ### an unclassed binder is printed, not graded
                gr, why = 'UNCLASSED', str(x)
            rows.append(dict(module=tag, name=n, kind=e['kind'], grade=gr, why=why, axioms=axd.get(n, 'not printed'),
                             changed=n in CHANGED))
            L.append('%s  %s  %s%s' % (gr, e['kind'], n, '  [CHANGED: docstring only]' if n in CHANGED else ''))
            L.append('    statement: %s' % R34._elab_header(e)[:900])
            L.append('    why: %s' % (why or '-'))
            L.append('    axioms: %s' % axd.get(n, 'not printed'))
            if n in GRADE_NOTES:
                L.append('    note: ' + GRADE_NOTES[n])
        L.append('')
    cnt = collections.Counter(r['grade'] for r in rows)
    L += ['== COUNTS: %d declarations read; %s' % (len(rows), ' ; '.join('%s %d' % kv for kv in sorted(cnt.items())))]
    for tag, *_r in ELAB_MODS:
        c = collections.Counter(r['grade'] for r in rows if r['module'] == tag)
        L.append('   %-18s %s' % (tag, ' ; '.join('%s %d' % kv for kv in sorted(c.items()))))
    thm = [r for r in rows if r['kind'] == 'theorem']
    L.append('   theorems %d ; at the standard three or no axiom %d' % (len(thm), sum(1 for r in thm if r['axioms'] in (STD3, 'NO AXIOM'))))
    for r in rows:
        if r['kind'] == 'theorem' and r['axioms'] not in (STD3, 'NO AXIOM'):
            errs.append('%s: axioms %s' % (r['name'], r['axioms']))
    print(NL.join(L[-(len(ELAB_MODS) + 2):]))
    if errs:
        print(NL.join('  ### ' + e for e in errs))
        sys.exit('### GRADES: %d ERRORS -- NOTHING WRITTEN' % len(errs))
    put_txt('b642_grades.txt', L)


def _rows_state(rows):
    out = {}
    for r in rows:
        out.setdefault((r['repo'], r['name']), (r['grade'], r.get('provenance'), r.get('mark') or '', r.get('kind') or ''))
    return out


def table(*a):
    """data/b642_table.txt: tools/terminal_table.py run (it writes the TABLE_FILES the closing regenerates); the rows read before from the
    table committed at b641's close (relay PRE_RELAY) and after from the regenerated data/terminal_table.json, diffed by row (repo, name):
    added, gone, moved, grade moved, each printed. The table confers no grade: a row moves only when a ledger cell does."""
    before = _rows_state(json.loads(_show(RELAY, PRE_RELAY, 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    after = _rows_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    gm = [k for k in moved if before[k][0] != after[k][0]]
    L = ['b642 -- THE TERMINAL TABLE REGENERATED AT v0.26`s BRANCH STATE (%s); tools/terminal_table.py exit %d' % (utc(), r.returncode),
         'before: data/terminal_table.json at relay %s (b641`s close, v0.25); after: the regenerated data/terminal_table.json' % PRE_RELAY, '',
         '### rows before %d ; after %d ; added %d ; gone %d ; moved %d ; grade moved %d' % (len(before), len(rows1), len(added), len(gone),
                                                                                           len(moved), len(gm))]
    L += ['  + %s %s %s' % (k[0], k[1], after[k]) for k in added] + ['  - %s %s %s' % (k[0], k[1], before[k]) for k in gone]
    L += ['  ~ %s %s %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved]
    gate = dict((m.group(3), m.group(1)) for m in re.finditer(r'^(\S+)  (theorem|def)  (\S+)', rd('b642_grades.txt'), re.M))
    t1 = dict((rw['name'], rw) for rw in rows1 if rw['repo'] == 'SIDE-explicit-formula')
    dis = [(n, gate[n], t1[n]['grade'] if n in t1 else 'NO ROW', (t1.get(n) or {}).get('provenance')) for n in sorted(gate)
           if (t1.get(n) or {}).get('grade') != gate[n]]
    heads = sorted(set(rw.get('head') for rw in rows1 if rw['repo'] == 'SIDE-explicit-formula'))
    L += ['', '### the kernel commit the table read SIDE-explicit-formula at (its rows` head): %s ; the branch %s' % (
        heads, _ef('rev-parse', K.EF_BRANCH)[:12])]
    L += ['### THE TABLE BESIDE THE GATE (data/b642_grades.txt): %d names graded by the gate ; in the table %d ; grades differing %d' % (
        len(gate), sum(1 for n in gate if n in t1), len(dis))]
    L += ['    %s : gate %s ; table %s (provenance %s)' % x for x in dis]
    if dis:
        L.append('    ### each differing row is a primed name the table`s textual reader does not resolve; the table grades such names from '
                 'b634`s elaborated bank (provenance rule-elab), which predates them; the gate`s grade stands in data/b642_grades.txt')
    L += ['', '### the tool`s last lines:'] + ['    ' + x for x in (r.stdout or '').strip().split(NL)[-6:]]
    if r.returncode:
        L += ['    ' + x for x in (r.stderr or '').strip().split(NL)[-10:]]
    put_txt('b642_table.txt', L)
    print(L[3])


def page(k, *a):
    """b640's re-emit, carried: the page `k` (zeta | chi) generated from its node list and banked probe output (no lean call) against the
    table as regenerated; written to PLACE-papers only when its bytes differ from HEAD's (and never under `dry`); data/b642_page_<k>.json
    carries the diff by line and the grade cells moved."""
    import difflib
    import time
    import b638_record as R8
    CP = R8._cp()
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, _meta, log = CP.build(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b642_%s' % k), os.path.join(D, K.PROBE[k]))
    if rc:
        put_json('b642_page_%s.json' % k, dict(rc=rc, log=log, at=utc()))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))
    put_json('b642_page_%s.json' % k, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved,
                                           free_mb_before=fm, seconds=int(time.time() - t0), at=utc(), written=bool(changed and not DRY)))
    print('  %s : exit %d ; changed against PLACE-papers HEAD %s ; diff lines %d ; cells moved %s' % (k, rc, changed, len(dl), gmoved or 'NONE'))


def page_arms(*a):
    """b640's page arms and frozen control, carried: G-CHAIN-PAGE and G-CHAIN-PAGE-CHI regenerate each page from its banked probe output
    and compare it with PLACE-papers HEAD's; the frozen control (test_chain_page_b596) at its relay pin. data/b642_page_arms.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b642 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b642_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; first differing line %s' % (arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'],
                                                                                         r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    save = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        c = TC.control()
    finally:
        CP.E0 = save
    for x in c:
        L.append('    %s (E0 at %s) %s : %s -- exit %d' % (TC.ARM, TC.RELAY_PIN, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b642_page_arms.txt', L)
    print(NL.join(l[:200] for l in L))


def pstatus(*a):
    """the premise table recomputed by b640's status reader (as b641 ran it) over the table as regenerated, its banks named b642's:
    data/b642_premise_status.txt and .json; beside it b641's, diffed by row (title, stamp and b641's (R251)(5) lines aside), the heads
    added, gone and moved printed."""
    import difflib
    import b640_record as R40
    saved = (R40.put_txt, R40.put_json)
    got = {}
    R40.put_txt = lambda name, L: got.__setitem__(name.replace('b640_', 'b642_'), L)
    R40.put_json = lambda name, j: got.__setitem__(name.replace('b640_', 'b642_'), j)
    try:
        R40.status()
    finally:
        R40.put_txt, R40.put_json = saved
    L, J = got['b642_premise_status.txt'], got['b642_premise_status.json']
    L = [('b642 -- THE PREMISE TABLE RECOMPUTED BY b640`S READER AT v0.26`S BRANCH STATE' + l[l.index(' ('):]) if l.startswith('b640 -- COMPONENT 2')
         else l for l in L]
    strip_ = lambda ls: [l for l in ls if not l.startswith(('b640 -- COMPONENT 2', 'b641 -- COMPONENT 5', 'b642 -- THE PREMISE TABLE',   # noqa: E731
                                                           '### the kernels read at the commits')) and not l.startswith('      (R251)(5)')]
    old = lines_of(rd('b641_premise_status.txt'))
    i = next((j for j, l in enumerate(old) if l.startswith('### THE DEDEKIND PREMISES, (R251)(5)')), len(old))
    dif = [x for x in difflib.unified_diff(strip_(old[:i]), strip_(L), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    h0 = dict((x['head'], x['status']) for x in jl('b641_premise_status.json').get('heads') or [])
    h1 = dict((x['head'], x['status']) for x in J.get('heads') or [])
    moved = sorted(h for h in set(h0) & set(h1) if h0[h] != h1[h])
    added, gone = sorted(set(h1) - set(h0)), sorted(set(h0) - set(h1))
    L += ['', '### BESIDE b641`S data/b641_premise_status.txt, BY ROW (titles, stamps and b641`s (R251)(5) lines aside): %d line(s)' % len(dif)]
    L += ['    ' + x[:300] for x in dif[:300]]
    L += ['### heads b641 %d ; b642 %d ; added %s ; gone %s ; status moved %s' % (len(h0), len(h1), added or 'NONE', gone or 'NONE',
                                                                                  ['%s %s -> %s' % (h, h0[h], h1[h]) for h in moved] or 'NONE'),
          '', '### ### **HEADS %d ; ADDED %d ; GONE %d ; STATUS MOVED %d ; ROWS DIFFERING %d.**' % (len(h1), len(added), len(gone), len(moved), len(dif))]
    put_txt('b642_premise_status.txt', L)
    put_json('b642_premise_status.json', dict(J, at=utc(), diff=dif, added=added, gone=gone, moved=moved))
    print(L[-1])


# ================================================================================ COMPONENT 6: THE EPSTEIN RUNGS, (R252)(4) -- A PROBE AND A BANK, NO BUILD
MATHLIB = K.EF + '/.lake/packages/mathlib'
# ### rung -> greps (label, pattern, pathspec, print every hit?) and the price read from the hits. A wide grep prints its count and the
# ### hits the price cites; a grep whose hits were hand-read prints them all with the reading.
EP_RUNGS = [
    ('R1 THE LATTICE SUM AND ITS CONVERGENCE', [
        ('ZLattice summability', r'^lemma (summable_norm_rpow|summable_norm_sub_rpow|tsum_norm_rpow_le)\b', 'Mathlib/Algebra/Module/ZLattice/Summable.lean', True),
        ('Eisenstein summability over Z^2 (integer weight, holomorphic)', r'^(lemma|theorem) (summable_norm_eisSummand|summable_eisSummand)\b',
         'Mathlib/NumberTheory/ModularForms/EisensteinSeries/*', True),
        ('a non-holomorphic (real-analytic) Eisenstein series', r'[Nn]onholomorphic|realAnalyticEisenstein', 'Mathlib/*', True),
        ('Epstein, anywhere', r'[Ee]pstein', 'Mathlib/*', True)],
     'ONE ACT: Z_Q(s) = sum over Z^2 minus 0 of Q(m, n)^(-s) for Q = x^2 + xy + 6y^2 = |m + n tau|^2, tau = (1 + sqrt(-23))/2; Q is comparable '
     'to the squared norm of a rank-2 lattice, so summable_norm_rpow (exponent -2 Re s < -2) gives absolute convergence on Re s > 1 and '
     'holomorphy by locally uniform convergence. The Eisenstein lemmas are for integer weight k >= 3 and holomorphic summands only; no '
     'real-analytic Eisenstein series and no Epstein zeta is at the pin.'),
    ('R2 THE THETA AND ITS INVERSION', [
        ('Poisson summation', r'^theorem (Real\.tsum_eq_tsum_fourier\S*|SchwartzMap\.tsum_eq_tsum_fourier)\b', 'Mathlib/Analysis/Fourier/PoissonSummation.lean', True),
        ('Gaussian sums over Z (a linear term allowed)', r'^theorem (Complex\.tsum_exp_neg_quadratic|Complex\.tsum_exp_neg_mul_int_sq|Real\.tsum_exp_neg_mul_int_sq)\b',
         'Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean', True),
        ('the Jacobi theta transformation', r'^theorem (jacobiTheta₂_functional_equation|jacobiTheta_S_smul)\b', 'Mathlib/NumberTheory/ModularForms/JacobiTheta/*', True),
        ('Poisson summation over a lattice or in more than one real dimension', r'[Pp]oisson.*(ZLattice|EuclideanSpace|Fin 2|ι →)|(ZLattice|EuclideanSpace).*[Pp]oisson',
         'Mathlib/*', True),
        ('a theta of a quadratic or binary form', r'BinaryQuadraticForm|QuadraticForm.*[Tt]heta|[Tt]heta.*QuadraticForm', 'Mathlib/*', True)],
     'TWO ACTS: Poisson summation at the pin is one-dimensional (Real and Schwartz on R) and no lattice or binary-form theta is there; '
     'Theta_Q(t) = sum exp(-pi t Q(m, n)) is reached by completing the square, Q = (m + n/2)^2 + (23/4) n^2, an iterated sum whose inner '
     'sum is a shifted Gaussian (Complex.tsum_exp_neg_quadratic, the linear term b) -- one act for the inversion Theta_Q(1/t) = '
     '(2/sqrt 23) t Theta_Q*(t) with Q* the dual form (equivalent to Q), one for the interchange of the iterated sums and the bounds.'),
    ('R3 THE FUNCTIONAL EQUATION AND THE CONTINUATION', [
        ('the abstract Mellin functional equation', r'^(structure WeakFEPair|structure IsStrongFEPair|theorem (functional_equation|differentiable_Λ₀|hasMellin|Λ_residue_k))\b',
         'Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', True),
        ('the Dedekind zeta (defined; residue only)', r'^(def|theorem) dedekindZeta\S*', 'Mathlib/NumberTheory/NumberField/DedekindZeta.lean', True),
        ('Hecke (class-group character) L-functions', r'HeckeCharacter|heckeLFunction|HeckeL', 'Mathlib/*', True)],
     'ONE ACT, AFTER R2: Theta_Q - 1 and its dual as a WeakFEPair (weight k = 1) give Lambda_Q = (2 pi / sqrt 23)^(-s) Gamma(s) Z_Q(s), its '
     'functional equation (functional_equation), continuation (differentiable_Λ₀) and the pole at s = 1 (Λ_residue_k). The Dedekind zeta '
     'of Q(sqrt -23) is defined at the pin with its residue only (no functional equation), and no Hecke L-function is there, so the '
     'decomposition Z_Q = (1/3)(zeta_K + 2 L(chi)) is not a route at the pin.'),
    ('R4 THE EXPLICIT FORMULA', [
        ('"explicit formula", every hit hand-read', r'[Ee]xplicit formula|ExplicitFormula', 'Mathlib/*', True),
        ('a Hadamard factorization (every hit hand-read: the matrix Hadamard product, none a factorization)', r'^(theorem|lemma) [^ ]*[Hh]adamard',
         'Mathlib/*', True)],
     'THREE ACTS AT THE LEAST, re-priced at its ruling: no hit concerns a sum over zeros (all 33 hand-read: derivative, trace, Catalan, '
     'special-value and coordinate formulas), and the pin holds no Hadamard factorization; the explicit formula for Z_Q needs its order-1 '
     'product or a contour argument, a zero count (the field E1 asks for), and the schema`s test-function side -- the kernel`s route for zeta '
     '(Zeta23/WeilEF, vendored) is the model, Z_Q has no Euler product (class number 3).'),
    ('R5 THE OFF-LINE ZERO AS A CERTIFIED WITNESS', [
        ('Davenport and Heilbronn', r'Davenport|Heilbronn', 'Mathlib/*', True),
        ('interval arithmetic', r'[Ii]nterval arithmetic', 'Mathlib/*', True)],
     'ONE ACT FOR A WITNESSED CERTIFICATE, A COMPILED ONE UNPRICED: the hits are the Cauchy-Davenport theorem and order-theoretic intervals; '
     'the pin holds no certified evaluation of an analytic function. A certificate by ball arithmetic outside Lean (python-flint Arb, the '
     'b627 instrument) is WITNESSED, not compiled.'),
]
EP_ESTIMATE = 'b641`s estimate (relay data/b641_closing.txt :127-:131): four acts at the least, each re-priced at the ruling that starts it'


def epstein(*a):
    """data/b642_epstein_rungs.txt: each rung`s greps at Mathlib de5ce8a9 (the kernel`s package checkout, read at the pin by git grep, never
    the working tree), every hit by file and line, and the rung priced in acts from the hits; the total beside b641`s four-act estimate."""
    pin = g(MATHLIB, 'rev-parse', 'HEAD').strip()
    L = ['b642 -- THE EPSTEIN RUNGS PRICED FROM THE PIN (ruling (R252)(4)); a probe and a bank, no build',
         'Mathlib %s (the pin %s: %s); W-ORD-EPSTEIN-ZQ`s five rungs; every grep `git grep -n -E` at the pin' % (
             pin[:12], K.MATHLIB_PIN[:8], 'AGREE' if pin == K.MATHLIB_PIN else '### DISAGREE'), '']
    errs = [] if pin == K.MATHLIB_PIN else ['the package checkout is not at the pin']
    for title, greps, price in EP_RUNGS:
        L += ['== ' + title, '']
        for label, pat, spec, _all in greps:
            r = subprocess.run(['git', '-C', MATHLIB, 'grep', '-n', '-E', pat, K.MATHLIB_PIN, '--', spec], capture_output=True)
            hits = [x.split(':', 1)[1] for x in r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if x]
            L.append('-- %s : %d hit(s)  [pattern %s ; path %s]' % (label, len(hits), pat, spec))
            L += ['     %s' % h[:200] for h in hits]
        L += ['', '   PRICE: ' + price, '']
    L += ['== THE READ PRICE: R1 one act, R2 two, R3 one, R4 three at the least, R5 one (witnessed) -- EIGHT ACTS AT THE LEAST, the compiled '
          'certificate unpriced; beside it ' + EP_ESTIMATE + '. The two count differently: the estimate ends at the local count (R4`s field), '
          'the rungs run to the off-line zero.']
    if errs:
        sys.exit('### ' + '; '.join(errs))
    put_txt('b642_epstein_rungs.txt', L)
    print(L[-1][:200])


EP_HEAD = ('*Appended 2026-10-08 by b642 to b641’s W-ORD-EPSTEIN-ZQ block (:%d), under `(R252)`(4) -- THE PRICE READ FROM THE PIN, THE '
           'ESTIMATE KEPT BESIDE IT:*')


def _epstein_ot_text():
    return (NL + EP_HEAD % K.EPSTEIN_ZQ + ' The five rungs priced from Mathlib at de5ce8a9 by git grep, each hit by file and line in relay '
            'data/b642_epstein_rungs.txt: (R1) the lattice sum and its convergence, one act, through `ZLattice.summable_norm_rpow` '
            '(Mathlib/Algebra/Module/ZLattice/Summable.lean :226); (R2) the theta and its inversion, two acts, Poisson summation at the pin '
            'being one-dimensional (Mathlib/Analysis/Fourier/PoissonSummation.lean :103, :195, :206, :220) with the shifted Gaussian sum '
            '`Complex.tsum_exp_neg_quadratic` (Mathlib/Analysis/SpecialFunctions/Gaussian/PoissonSummation.lean :87) and no lattice or '
            'binary-form theta; (R3) the functional equation and the continuation, one act after (R2), through `WeakFEPair` '
            '(Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean :80, its functional equation :425); (R4) the explicit formula, three acts at '
            'the least, no hit at the pin concerning a sum over zeros and no Hadamard factorization; (R5) the off-line zero, one act for a '
            'certificate by ball arithmetic outside Lean (WITNESSED, not compiled), a compiled certificate unpriced. THE READ PRICE, '
            'replacing the price b641 printed in relay data/b641_closing.txt: eight acts at the least. THE ESTIMATE, kept beside it: '
            'four acts at the least, ending at the local count; each act re-priced at the ruling that starts it.' + NL)


def epstein_ot(*a):
    """### Component 6`s ledger line, (R252)(4): the read price appended to OPEN_TRAILS beneath b641`s W-ORD-EPSTEIN-ZQ block, the estimate
    ### kept beside it; landed by b633`s _land (b566's guarded append_to), its line banked in data/b642_record_lines_epstein.json."""
    Q = R2._Q()
    at = Q.line_of(Q.OT, '*Appended 2026-10-08 by b641, under the author’s answer at b641’s Component 4 -- W-ORD-EPSTEIN-ZQ')
    if at != K.EPSTEIN_ZQ:
        sys.exit('### b641`S EPSTEIN BLOCK MOVED (%s) -- NOTHING WRITTEN' % at)
    t = _poss(_epstein_ot_text())
    items = [('OPEN_TRAILS.md', EP_HEAD % K.EPSTEIN_ZQ, t)]
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'epstein')
    unread = [x for x in ('?', '### NOT', 'None') if x in t]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks: %s ; unread figures: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', t.count('`') % 2, unread or 'NONE'))
    if DRY:
        print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or t.count('`') % 2 or unread:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    _land(Q, items, 'b642_record_lines_epstein.json', K.EPSTEIN_ZQ)


# ================================================================================ COMPONENT 7: THE SEAL'S HASHES, THE MERGE READ BACK
def seal_hashes():
    rec_ = jl('b642_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b642 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b642_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


def _kernel_push():
    """the merge`s read-backs from the kernel push capture: main at the remote, the tag made and its peel at the remote."""
    t = rd('b642_kernel_push_out.txt')
    m = re.search(r'push_gated: main read back at the remote: (\w+)', t)
    tg = re.search(r'push_gated: tag (\S+) made at the read-back (\w+)', t)
    pe = re.search(r'push_gated: tag %s peeled local (\w+) remote (\w+)' % re.escape(K.EF_TAG), t)
    return dict(main=m.group(1) if m else None, tag=tg.group(1) if tg else None, tag_at=tg.group(2) if tg else None,
                peel=pe.group(2) if pe and pe.group(1) == pe.group(2) else None)


def merge_read(*a):
    """data/b642_merge.txt: SIDE-explicit-formula after the merge -- main, the branch, the tag`s peel, locally and in the push capture; main`s
    reflog since the step-zero face (one fast-forward expected); the branch`s commits each with its files; the closure build`s status."""
    kp = _kernel_push()
    main_, br, peel = _ef('rev-parse', 'main'), _ef('rev-parse', K.EF_BRANCH), _ef('rev-parse', '%s^{commit}' % K.EF_TAG)
    face = (jl('b642_kernels_face.json').get('kernels') or {}).get('SIDE-explicit-formula') or []
    refl = _ef('reflog', 'show', '--format=%H %gs', 'refs/heads/main').split(NL)[:4]
    L = ['b642 -- THE MERGE OF %s INTO SIDE-explicit-formula main AND THE TAG %s, READ BACK (%s)' % (K.EF_BRANCH, K.EF_TAG, utc()), '',
         '### step-zero face: main %s' % (face[0] if face else '### NOT READ'),
         '### main %s ; %s %s ; %s peeled %s' % (main_[:12], K.EF_BRANCH, br[:12], K.EF_TAG, peel[:12]),
         '### the push capture (data/b642_kernel_push_out.txt): main read back %s ; tag %s made at %s ; peel at the remote %s' % (
             (kp['main'] or '### NOT READ')[:12], kp['tag'], (kp['tag_at'] or '-')[:12], (kp['peel'] or '### NOT READ')[:12]),
         '### main`s reflog, newest first: %s' % ' | '.join(x[:90] for x in refl),
         '### the merge is a fast-forward: %s' % (subprocess.run(['git', '-C', K.EF, 'merge-base', '--is-ancestor', K.EF_PIN, main_]).returncode == 0
                                                and main_ == br),
         '### the closure build: NOT RUN -- the merge is a fast-forward to the branch tip, each of whose modules was built at its commit, one '
         'module per call (data/b642_declarations.txt`s watchdog logs); a closure build is a serial module list or not run (:13067)', '',
         '### THE BRANCH`S COMMITS, EACH ALONE:']
    for line in _ef('log', '--reverse', '--format=%h %s', '%s..%s' % (K.EF_PIN, main_)).splitlines():
        h = line.split()[0]
        L.append('    %s  %s  [%s]' % (h, line[len(h) + 1:][:110], ', '.join(_ef('show', '--name-only', '--format=', h).split())))
    ok = main_ == br == peel == (kp['main'] or '') == (kp['peel'] or '') and kp['tag'] == K.EF_TAG
    L += ['', '### ### **MAIN = %s = %s = THE REMOTE`S MAIN = THE REMOTE`S PEEL : %s.**' % (K.EF_BRANCH, K.EF_TAG, ok)]
    put_txt('b642_merge.txt', L)
    print(L[-1])


# ================================================================================ THE ROOT
ROOT_EXCLUDE = re.compile(r'^b642_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b642_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    """### (R251)(3): the act root, the last step of the act -- after the last declared seal re-run; no bank it names is written after it."""
    banks = root_banks()
    print('  banks named: %d ; the seal bank among them %s' % (len(banks), 'data/b642_seal_hashes.json' in banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b642'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    print(NL.join(((r.stdout or '') + (r.stderr or '')).rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the root recomputed from its banked items offline and a one-byte change on a copy of one bank moving it; the local part of verify
    ### -- every bank the root names unchanged and none written after the root. Writes data/b642_root_arm.*, which the root does not name."""
    import shutil
    import tempfile
    import act_root as AR
    J = jl('b642_act_root.json')
    bank_ = [it.split()[0] for it in J['items'] if it.startswith('data/')][0]
    tmp = tempfile.mkdtemp()
    cp = os.path.join(tmp, os.path.basename(bank_))
    shutil.copy(os.path.join(ROOT, *bank_.split('/')), cp)
    b = bytearray(open(cp, 'rb').read())
    b[0] ^= 0x01
    open(cp, 'wb').write(bytes(b))
    items2 = [('%s %s' % (bank_, AR.sha256_file(cp)) if it.split()[0] == bank_ else it) for it in J['items']]
    r2 = AR.root_of(items2, J['previous'])
    same = AR.root_of(J['items'], J['previous'])
    late = []
    for it in J['items']:
        p = it.split()
        if p[0].startswith('data/'):
            fp = os.path.join(ROOT, *p[0].split('/'))
            if not os.path.exists(fp) or AR.sha256_file(fp) != p[1]:
                late.append('%s changed' % p[0])
            elif os.path.getmtime(fp) > J.get('at_epoch', 0) + AR.ORDER_SLACK:
                late.append('%s written after the root' % p[0])
    L = ['b642 -- THE ACT-ROOT ARM`S OFFLINE CONTROL AND THE ROOT ORDER READ LOCALLY (%s)' % utc(), '',
         '### the root`s time %s ; banks named %d ; changed or written after the root: %s' % (J.get('at'), len([i for i in J['items'] if i.startswith('data/')]), late or 'NONE'),
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s ; THE ROOT ORDER HOLDS LOCALLY %s.**' % (
             same == J['root'], r2 != J['root'], not late)]
    put_txt('b642_root_arm.txt', L)
    put_json('b642_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root'], late=late))
    print(L[-1])


# ================================================================================ THE SCORES AND THE RECORD
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = NK + SK
SIX_BANKS = ('b642_declarations', 'b642_nonvacuity', 'b642_grades', 'b642_table', 'b642_premise_status', 'b642_epstein_rungs')
N5_ALLOWED = {'data/b641_closing_push_out.txt', 'data/act_roots.txt'}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md')
N5_EF = ('SIDEExplicitFormula/KeiperIdentities.lean', 'SIDEExplicitFormula/Schema/WindowProofs.lean', 'SIDEExplicitFormula/Schema/FamilyPremises.lean',
         'SIDEExplicitFormula/Schema/DedekindRestated.lean', 'SIDEExplicitFormula/SaltCheckNonvacuity.lean', 'SIDEExplicitFormula/Schema/Family.lean',
         'SIDEExplicitFormula/Schema/Dedekind.lean', 'SIDEExplicitFormula/Schema/PlateauRamp.lean', 'AxiomCheckKeiperIdentities.lean',
         'AxiomCheckWindowProofs.lean', 'AxiomCheckFamilyPremises.lean', 'AxiomCheckDedekindRestated.lean', 'AxiomCheckNonvacuity.lean')
N1_NAMES = ('SIDEExplicitFormula.Keiper.binomialTransform_holds', 'SIDEExplicitFormula.Keiper.logDerivSplit_holds',
            'SIDEExplicitFormula.Keiper.stieltjesLog_holds', 'SIDEExplicitFormula.Schema.PlateauRamp.convStep_holds',
            'SIDEExplicitFormula.Schema.PlateauRamp.smooth4_holds')
N2_NAMES = ('SIDEExplicitFormula.Schema.Family.not_trivialSummandPremise', "SIDEExplicitFormula.Schema.Dedekind.trivialSummandPremise'_witness",
            "SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'")


def _grade_rows():
    """the grades bank read back: {name: (grade, kind, axioms)}."""
    out, cur = {}, None
    for l in lines_of(rd('b642_grades.txt')):
        m = re.match(r'^(\S+)  (theorem|def)  (\S+)', l)
        if m:
            cur = m.group(3)
            out[cur] = [m.group(1), m.group(2), None]
        elif cur and l.startswith('    axioms: '):
            out[cur][2] = l[len('    axioms: '):]
    return out


def _nv_counts():
    t = rd('b642_nonvacuity.txt')
    m = re.search(r'^WITNESSED (\d+) ; UNWITNESSED (\d+) ; total (\d+) ; both (\d+) ; neither (\d+)', t, re.M)
    return tuple(int(x) for x in m.groups()) if m else None


def _u():
    c = _nv_counts()
    return c[1] if c else None


def _nv_classes():
    """the non-vacuity bank`s class lines read back: {(outcome, class): n}."""
    return dict(((m.group(1), m.group(2)), int(m.group(3))) for m in
                re.finditer(r'^  (WITNESSED|UNWITNESSED) / (\S+): (\d+)$', rd('b642_nonvacuity.txt'), re.M))


def TRAIL_HEAD():
    return ('### b642 — lane three, act sixty-nine under (R252): SIDE-explicit-formula v0.26 — Keiper’s three identities at every index, the '
            'window’s two, TrivialSummandPremise refuted in the kernel and restated with a witness, dedekind_rhs re-proved, non-vacuity '
            'witnesses over the premise table; the PlateauRamp docstring at its pin; the Epstein rungs priced from the pin; the squeeze’s '
            'compiled jaw named')


def _n5_kernels():
    """every kernel the face read unmoved but SIDE-explicit-formula; SIDE-explicit-formula`s main moved once, by the merge, to the branch tip
    and the tag; its branches the face`s plus the act`s branch."""
    face = jl('b642_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    bad = [k for k, v in face.items() if k != 'SIDE-explicit-formula' and now.get(k) != list(v)]
    ef0, ef1 = face.get('SIDE-explicit-formula') or [], now.get('SIDE-explicit-formula') or []
    main_ = _ef('rev-parse', 'main')
    refl = [x.split()[0] for x in _ef('reflog', 'show', '--format=%H', 'refs/heads/main').split(NL) if x.strip()]
    ef_ok = bool(ef0) and main_ == _ef('rev-parse', K.EF_BRANCH) == _ef('rev-parse', '%s^{commit}' % K.EF_TAG) \
        and len(refl) >= 2 and refl[0] == main_ and refl[1].startswith(K.EF_PIN)
    files = sorted(x for x in _ef('diff', '--name-only', K.EF_PIN, main_).split(NL) if x.strip())
    beyond = [f for f in files if f not in N5_EF]
    return bool(face) and not bad and ef_ok and not beyond, bad, ef_ok, beyond, ef0[:1], ef1[:1]


def n5(trail_line=None):
    ot_text = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD():
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD() not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d' % trail_line
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    k_ok, k_bad, ef_ok, ef_beyond, ef0, ef1 = _n5_kernels()
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b642_|audit_b642_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    six = [b for b in SIX_BANKS if not os.path.exists(os.path.join(D, b + '.txt'))]
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    ok = k_ok and not pp_beyond and not beyond and rec_ok and not differ and not six and untracked_local
    return ('HELD' if ok else 'REFUTED',
            'nothing deposited (no platform called); every kernel but SIDE-explicit-formula unmoved %s (moved: %s); SIDE-explicit-formula`s main '
            'moved once, by the merge, from %s to the branch tip and %s %s, its files beyond the branch`s modules and the docstrings: %s; '
            'PLACE-papers %s (beyond: %s); %s; relay beyond the act`s own banks and tools, the table and the roots file: %s; the six banks '
            'absent: %s; sealed tools not agreeing %s; b628`s bank untracked %s; no identifier of the author in any outbound request' % (
                not k_bad, k_bad or 'NONE', ef0, K.EF_TAG, ef_ok, ef_beyond or 'NONE', pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE',
                six or 'NONE', differ or 'NONE', untracked_local))


def scores(*a):
    TB, RA, ST = jl('b642_table_final.json'), jl('b642_root_arm.json'), jl('b642_tests_stepzero.json')
    tl = [x for x in a if x.startswith('trail_line=')]
    _r, _n, sh = seal_hashes()
    G = _grade_rows()
    n1 = [(n.split('.')[-1], (G.get(n) or ['?', '', '?'])[0], (G.get(n) or ['?', '', '?'])[2]) for n in N1_NAMES]
    n1_ok = all(gr == 'DERIVES' and ax == STD3 for _n_, gr, ax in n1)
    n2 = [(n.split('.')[-1], (G.get(n) or ['?', '', '?'])[0], (G.get(n) or ['?', '', '?'])[2]) for n in N2_NAMES]
    n2_ax = all(ax == STD3 for _n_, _gr, ax in n2)
    rhs_grade = n2[2][1]
    nv = _nv_counts()
    nv_ok = bool(nv) and nv[2] == 50 and nv[3] == 0 and nv[4] == 0 and nv[0] + nv[1] == 50 and rd('b642_nonvacuity.txt').count('    reason: ') == nv[1]
    tb = rd('b642_table.txt')
    tm = re.search(r'added (\d+) ; gone (\d+) ; moved (\d+) ; grade moved (\d+)', tb)
    added_names = [l.split()[2] for l in lines_of(tb) if l.startswith('  + SIDE-explicit-formula ')]
    added_ok = bool(added_names) and all(n in G for n in added_names)
    n4_ok = bool(tm) and tm.group(2) == '0' and tm.group(3) == '0' and tm.group(4) == '0' and added_ok and int(tm.group(1)) == len(added_names)
    clean_tests = [n for n, x in ST.items() if x.get('rc') == 0 and not x.get('failing')]
    dm = re.search(r'TOTAL: (\d+) prints over the four modules; beyond the standard three or sorryAx: (\d+)', rd('b642_declarations.txt'))
    _t, nvp, nvn = _axlog('Nonvacuity')
    s1_ok = bool(dm) and dm.group(2) == '0' and len(nvp) + len(nvn) == 23 and all(s == STD3 for _n_, s in nvp)
    S = {
        'N1': (('HELD' if n1_ok else 'REFUTED'),
               'K1-K3 and W1-W2 at the elaborated reader and their axiom prints: %s; no premise binder in any of the five' % '; '.join(
                   '%s %s %s' % x for x in n1)),
        'N2': (('HELD' if n2_ax and rhs_grade == 'INTERFACES' else 'REFUTED IN ONE CLAUSE' if n2_ax else 'REFUTED'),
               'not_trivialSummandPremise, the restated premise`s witness and dedekind_rhs` each at the standard three (%s); dedekind_rhs` read %s '
               'by the gate, not INTERFACES -- (R243)(2): TrivialSummandPremise` is a predicate the rule meets for the first time, printed and not '
               'graded; both premises it takes carry a witness (trivialSummandPremise`_witness at the constant 1, eulerFactorPremise_three)' % (
                   '; '.join('%s %s' % (x[0], x[2]) for x in n2), rhs_grade)),
        'N3': (('HELD' if nv_ok else 'REFUTED'),
               'heads %s: WITNESSED %s, UNWITNESSED %s each with its reason, both %s, neither %s (data/b642_nonvacuity.txt)' % (
                   nv[2] if nv else '?', nv[0] if nv else '?', nv[1] if nv else '?', nv[3] if nv else '?', nv[4] if nv else '?')),
        'N4': (('HELD' if n4_ok else 'REFUTED'),
               'the table against b641`s: %s; every added row a declaration the act adds %s; dedekind_rhs`s row unmoved, its annotation the '
               'record`s' % (tm.group(0) if tm else '### NOT READ', added_ok)),
        'N5': n5(int(tl[0].split('=')[1]) if tl else None),
        'S1': (('HELD' if s1_ok else 'REFUTED'),
               'the declarations` prints %s, beyond the standard three or sorryAx %s; the salt module`s %d, at the standard three or none' % (
                   dm.group(1) if dm else '?', dm.group(2) if dm else '?', len(nvp) + len(nvn))),
        'S2': (('HELD' if ST and len(clean_tests) == len(ST) else 'REFUTED'), 'every test file clean at step zero: %d of %d' % (len(clean_tests), len(ST))),
        'S3': (('HELD' if TB and not TB.get('moved') and not TB.get('gone') else 'REFUTED') if TB else 'PENDING',
               'the table regenerated at the end: moved %s, gone %s, added %s' % (len(TB.get('moved') or []), len(TB.get('gone') or []),
                                                                                 len(TB.get('added') or []))),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED') if RA else 'PENDING',
               'the root recomputed equal and the one-byte control moving it'),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) else 'REFUTED'), 'the sealed tools` hashes %s' % dict(collections.Counter(v for _t, v in sh))),
    }
    put_json('b642_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:260]))


def table_final(*a):
    """the table at the end (b641`s form, b642`s banks): the regenerated table against b641`s committed one, by row, and the rows added named."""
    before = _rows_state(json.loads(_show(RELAY, PRE_RELAY, 'data/terminal_table.json'))['rows'])
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    after = _rows_state(json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    L = ['b642 -- THE TERMINAL TABLE REGENERATED, final (%s); exit %d' % (utc(), r.returncode), '',
         '### rows %d ; added %d ; gone %d ; moved %d' % (len(after), len(added), len(gone), len(moved)),
         '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone), sum(1 for k in moved if before[k][0] != after[k][0]))]
    put_txt('b642_table_final.txt', L)
    put_json('b642_table_final.json', dict(at=utc(), rc=r.returncode, moved=[list(k) for k in moved], added=[list(k) for k in added],
                                           gone=[list(k) for k in gone], grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]]))
    print(L[-1])


def _title():
    return ('## SIDE-explicit-formula v0.26: Keiper’s three identities at every index, the window’s two, TrivialSummandPremise refuted in the '
            'kernel and restated with a witness, dedekind_rhs re-proved, non-vacuity witnesses over the premise table with %s unwitnessed; the '
            'PlateauRamp docstring at its pin; the Epstein rungs priced from the pin; the squeeze’s compiled jaw named' % _u())


TITLE = _title()


def _finding_text():
    S, rl, J, re_ = (jl(n_) for n_ in ('b642_scores.json', 'b642_record_lines.json', 'b642_act_root.json', 'b642_record_lines_epstein.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b642_author_answers.txt'), re.M))
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}, {}]
    ep = (re_.get('lines') or [{}])[0]
    nv = _nv_counts() or (0, 0, 0, 0, 0)
    ncl = _nv_classes()
    G = _grade_rows()
    gc = collections.Counter(v[0] for v in G.values())
    kp = _kernel_push()
    dm = re.search(r'TOTAL: (\d+) prints', rd('b642_declarations.txt'))
    sc = lambda k: (S.get(k) or ['?'])[0]   # noqa: E731
    e = ['', TITLE, '',
         '*Filed at b642 on the author’s ruling `(R252)`%s. Banks: relay `data/b642_declarations.txt`, `data/b642_nonvacuity.txt`, '
         '`data/b642_grades.txt`, `data/b642_table.txt`, `data/b642_premise_status.txt`, `data/b642_epstein_rungs.txt`, `data/b642_merge.txt`, '
         '`data/b642_act_root.txt`.*' % ((' and the author’s answers (%d)' % n_ans) if n_ans else ''), '',
         '**The declarations** (Component 2, `(R252)`(3)(a)-(d)): SIDE-explicit-formula v0.26 on the branch %s from v0.25 = %s, every commit '
         'alone. Keiper’s three identities at every index -- `binomialTransform_holds`, `logDerivSplit_holds`, `stieltjesLog_holds` '
         '(SIDEExplicitFormula/KeiperIdentities.lean), the fourth obligation not here; the window’s two -- `convStep_holds`, through Mathlib’s '
         '`Real.fourier_mul_convolution_eq` with the weight `e^(-(Im z) u)`, and `smooth4_holds` (Schema/WindowProofs.lean); '
         '`not_trivialSummandPremise` (the pole term `8 sinh(1/4)` at the box of half-width 1/2), `eulerFactorPremise_of_primitive` and '
         '`not_eulerFactorPremise_six` (the point mass at `log 2`) (Schema/FamilyPremises.lean); `TrivialSummandPremise` kept with its '
         'docstring naming its refutation, `TrivialSummandPremise’` beside it carrying the pole term as a term, its witness at the constant 1 '
         'built before `dedekind_rhs’` is proved on it and `EulerFactorPremise q`, the v0.25 `dedekind_rhs` kept under a docstring naming the '
         'refuted premise, `dedekind_three` re-checked by `rfl` (Schema/DedekindRestated.lean). %s prints over the four modules, each '
         '`[propext, Classical.choice, Quot.sound]`, no `sorryAx`. N1 %s; N2 %s.' % (K.EF_BRANCH, K.EF_PIN, dm.group(1) if dm else '?',
                                                                                   sc('N1'), sc('N2')), '',
         '**The non-vacuity** (Component 3, `(R252)`(3)(e), W-ORD-PREMISE-NONVACUITY acted): the census’s %d heads, %d WITNESSED -- by a theorem '
         'in a Salt module, %d of them in SIDEExplicitFormula/SaltCheckNonvacuity.lean, %d of those DEGENERATE (`PWSetup`, `farSmall`, '
         '`PlattTrudgianHeight`, each at a parameter where it says nothing, and marked so), %d by Salt modules already at the pin -- and %d '
         'UNWITNESSED, each with its reason: %d declared in kernels this act does not write, %d refuted (`TrivialSummandPremise`), %d whose '
         'witness is a proof the kernel does not have (`BoundPremises`, `KeiperObligations`, `NymanBeurlingPremise`); none both, none '
         'neither. N3 %s.' % (
             nv[2], nv[0], ncl.get(('WITNESSED', 'NEW'), 0) + ncl.get(('WITNESSED', 'DEGENERATE'), 0), ncl.get(('WITNESSED', 'DEGENERATE'), 0),
             ncl.get(('WITNESSED', 'EXISTING'), 0), nv[1], ncl.get(('UNWITNESSED', 'OTHER-KERNEL'), 0), ncl.get(('UNWITNESSED', 'REFUTED'), 0),
             ncl.get(('UNWITNESSED', 'CONTENT'), 0), sc('N3')), '',
         '**The docstring** (Component 4, `(R252)`(3)(f), W-ORD-PLATEAURAMP-DOCSTRING acted): Schema/PlateauRamp.lean :19-:20 names the pin’s '
         'theorem, `Real.fourier_mul_convolution_eq` (Mathlib/Analysis/Fourier/Convolution.lean :119), integrable functions at real '
         'frequency, where it read Schwartz functions only; committed alone, the module rebuilt, its importers current.', '',
         '**The grades, the table, the pages** (Component 5): every new and changed declaration read at the elaborated reader and graded by '
         'the E0 gate -- %s; the gate reads a data binder of the Keiper module’s smoothness lemma, its order in WithTop ℕ∞, as a named '
         'predicate, an instrument misreading banked as printed with its note (relay data/b642_grades.txt). The terminal table regenerated: '
         'no row moved or gone, the rows added the act’s declarations, three primed '
         'names left ungraded by the table’s textual reader and graded by the gate. Both pages unchanged, the page arms 2 of 2 and the frozen '
         'control 2 of 2. The premise table recomputed beside b641’s: `EulerFactorPremise` OPEN to WITNESSED, `WindowObligations` OPEN to '
         'DISCHARGED, no other status moved. N4 %s.' % (', '.join('%s %d' % kv for kv in sorted(gc.items())), sc('N4')), '',
         '**The Epstein rungs** (Component 6, `(R252)`(4)): each rung of W-ORD-EPSTEIN-ZQ priced from Mathlib at de5ce8a9 by git grep, every '
         'hit by file and line: eight acts at the least, the four-act estimate kept beside it (OPEN_TRAILS :%s).' % ep.get('line'), '',
         '**The merge** (Component 7): %s merged into SIDE-explicit-formula main by a fast-forward and tagged %s at %s, main and the tag’s peel '
         'read back at the remote; the closure build not run, each module having been built at its commit.' % (
             K.EF_BRANCH, K.EF_TAG, (kp.get('peel') or '?')[:7]), '',
         '**The record lines** (`(R252)`(1), (2), (5)): b641 at its weight (FINDINGS :%s); the order of `(R251)`(8) reversed (OPEN_TRAILS :%s); '
         'the squeeze’s correction in the navigator’s name, its compiled jaw `ZetaZeroFree` named (:%s); W-ORD-H2-LATTICE (:%s) and '
         'W-ORD-H2-PI1 (:%s) entered with triggers.' % (ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line'),
                                                        ls[4].get('line')), '',
         '**The root.** b642 over %d repositories, %d tags and %d banks, the last step of the act’s banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, sc(k2)) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it re-reads b641’s research discharge (FINDINGS :%d) as compiled statements -- '
         'the five declarations b641 found ripe now theorems, the premise b641 found false by computation now refuted in the kernel -- and '
         'b631’s Dedekind instance by a premise that holds. It strengthens the programme’s offering of an assumption list a reader can check: '
         'every premise structure the census counts now carries a witness or a printed reason why it does not.' % K.B641_ENTRY, '',
         '**Next.** Per `(R252)`(7): b643, the author’s word pending, the census at v0.7 with the status column over six statuses and the '
         'non-vacuity bank, read by the second reader.', '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero; a theorem here is a statement about the kernel’s definitions, '
         'and a witness shows a premise structure is not empty.*', '']
    return TITLE, NL.join(e)


FOR_AUTHOR = ('(1) the census’s 50 heads read from b641’s premise status bank, the heads of the census v0.6 premise table; (2) a head declared in '
              'a kernel this act does not write read UNWITNESSED with its reason, an in-kernel instance outside a Salt module named beside it '
              'and not counted; (3) a witness at a parameter where the structure says nothing counted WITNESSED and marked DEGENERATE; (4) a '
              'witness that restates a kernel theorem in the Salt module counted as the Salt module’s; (5) the gate’s grade banked as printed '
              'where the seat reads it otherwise, with a note; (6) the closure build not run, the merge being a fast-forward to modules each '
              'built at its commit')


def _trail_text():
    S, fj, rl, J, re_ = (jl(n_) for n_ in ('b642_scores.json', 'b642_findings.json', 'b642_record_lines.json', 'b642_act_root.json',
                                           'b642_record_lines_epstein.json'))
    n_ans = len(re.findall(r'^### PROMPT ', rd('b642_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}, {}]
    ep = (re_.get('lines') or [{}])[0]
    kp = _kernel_push()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R252) ratified.** (1) b641 at its weight. (2) The order of (R251)(8) reversed. (3) The proving act: K1-K3, W1-W2, the '
             'Dedekind premises in the kernel, the restated premise and dedekind_rhs re-proved, non-vacuity, the PlateauRamp docstring. (4) '
             'The Epstein rungs priced. (5) The squeeze’s correction. (6) The face sealed after the components. (7) The act after: b643.', '',
             '**Entered:** FINDINGS.md:%s (b641’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the order), :%s (the squeeze’s correction), :%s '
             '(W-ORD-H2-LATTICE), :%s (W-ORD-H2-PI1), :%s (the Epstein price); this record.' % (
                 ls[0].get('line'), fj.get('entry_line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line'), ls[4].get('line'), ep.get('line')), '',
             '**The kernel:** SIDE-explicit-formula %s = `%s`, %s merged into main by a fast-forward, main and the tag read back at the remote.' % (
                 K.EF_TAG, (kp.get('peel') or '?')[:12], K.EF_BRANCH), '',
             '**Act root:** b642 `%s` (previous `%s`, b641’s; relay data/act_roots.txt), computed after the last bank it names.' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b642_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): b643 names no kernel terminal; the census’s status column reads the non-vacuity bank '
             'and the six statuses.', '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b642_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R252)`(7), b643, the author’s word pending; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b642_scores.json')
    L = ['=' * 104, 'b642 -- THE DESK.', '=' * 104, ''] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SCORE_KEYS]
    L += [''] + rd('b642_defects.txt').rstrip(NL).split(NL)
    put_txt('b642_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J, re_ = (jl(n_) for n_ in ('b642_scores.json', 'b642_findings.json', 'b642_trail.json', 'b642_record_lines.json',
                                               'b642_act_root.json', 'b642_record_lines_epstein.json'))
    ls = (rl.get('lines') or []) + [{}, {}, {}, {}, {}]
    nv = _nv_counts() or (0, 0, 0, 0, 0)
    kp = _kernel_push()
    L = ['b642 -- THE COMPONENTS, BANKED UNDER (R252).', '',
         '### COMPONENT 0 : step zero (data/b642_tests_stepzero.txt, data/b642_procs_stepzero.txt, data/b642_branches.txt)',
         '### COMPONENT 1 : b641`s weight FINDINGS :%s ; the order OPEN_TRAILS :%s ; the squeeze :%s ; W-ORD-H2-LATTICE :%s ; W-ORD-H2-PI1 :%s' % (
             ls[0].get('line'), ls[1].get('line'), ls[2].get('line'), ls[3].get('line'), ls[4].get('line')),
         '### COMPONENT 2 : the declarations (data/b642_declarations.txt) ; N1 %s ; N2 %s' % (S['N1'][0], S['N2'][0]),
         '### COMPONENT 3 : non-vacuity (data/b642_nonvacuity.txt) : WITNESSED %d ; UNWITNESSED %d ; N3 %s' % (nv[0], nv[1], S['N3'][0]),
         '### COMPONENT 4 : the PlateauRamp docstring (data/b642_declarations.txt, its commit)',
         '### COMPONENT 5 : the grades, the table, the pages, the premise table (data/b642_grades.txt, data/b642_table.txt, data/b642_page_*.json, '
         'data/b642_page_arms.txt, data/b642_premise_status.txt) ; N4 %s' % S['N4'][0],
         '### COMPONENT 6 : the Epstein rungs (data/b642_epstein_rungs.txt) ; OPEN_TRAILS :%s' % ((re_.get('lines') or [{}])[0].get('line')),
         '### COMPONENT 7 : the seal (data/b642_seal_hashes.json) ; the merge (data/b642_merge.txt) ; %s = %s' % (K.EF_TAG, (kp.get('peel') or '?')[:12]),
         '### COMPONENT 8 : the root %s ; FINDINGS :%s ; OPEN_TRAILS :%s' % ((J.get('root') or '')[:16], fj.get('entry_line'), tj.get('line'))]
    put_txt('b642_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    e = _poss(e)
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE ENTRY -- NOTHING WRITTEN')
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    unread = [x for x in ('### NOT', 'None', '?;', ' ? ', '`?`') if x in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', unread or 'NONE'))
    if 'dry' in a:
        print(e)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b642_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _poss(_trail_text())
    if e.count('`') % 2:
        sys.exit('### ODD BACKTICKS IN THE RECORD -- NOTHING WRITTEN')
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    unread = [x for x in ('### NOT', 'None', '`?`') if x in e]
    print('  table cells: %s ; nd %s ; scanner %s ; unread figures %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', unread or 'NONE'))
    if 'dry' in a:
        print(e[:7000])
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or unread:
        sys.exit('### NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD())
    r = Q.append_to(Q.OT, e)
    put_json('b642_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD()), head=TRAIL_HEAD(), append=r))
    print('  OPEN_TRAILS record :%s' % jl('b642_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-08 by b642 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD())
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    if 'dry' in a:
        print(t)
        return
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b642_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


# ================================================================================ THE DISPATCHER
if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'answer_of', 'put_txt', 'put_json', 'act_from', 'READS', 'seal_hashes', 'n5',
                                                          'TRAIL_HEAD', 'root_banks'):
        print('usage: b642_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
