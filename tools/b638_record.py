# -*- coding: utf-8 -*-
"""b638_record.py -- THE ACT'S RECORD TOOL, UNDER (R248). ### ONE SUBCOMMAND PER BANK.

### ### b638: LANE THREE, ACT SIXTY-FIVE -- THE KEYSTONE CENSUS AT v0.6 UNDER THE READER'S CLAUSE: A PLAIN OPENING, A SHARED GLOSSARY,
### PROVENANCE UNDER THE UPSTREAM EXCLUSION, THE PREMISE TABLE AT 50 HEADS WITH ITS UNNAMED RESIDUE; THE PWSetup MOVES HELD TO A FIELD
### PRINT; THE MIRROR REBUILT ON THE 73-FILE ROSTER.
### Subcommands write only `data/b638_*` unless the docstring names another file; `dry` routes WRITES to the scratchpad. The generic helpers
### are b633's record tool's and b637's, imported; ledger appends through b566's guarded `append_to`. The data is tools/b638_worklist.py;
### the generator tools/chain_page.py takes the glossary block at Component 3 (through the Edit tool, after the seal), and the census at
### v0.6 prints the block through the generator's own renderer. No platform is called; no registry is read; nothing deposits. b628's full
### intake bank is never read here, never staged or committed. A stand-in bank directory named by the environment variable B638_STANDIN is
### read before data/ by the record texts' dry runs alone.
"""
import collections
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b633_record as R3  # noqa: E402
import b637_record as R7  # noqa: E402
import b638_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'b8acf12c-00ee-4167-9344-809d3aa94847'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b638_registration_2026-10-07.txt'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
DRY = R3.DRY
put_txt, put_json, _write, _scan, _clean = R3.put_txt, R3.put_json, R3._write, R3._scan, R3._clean
lines_of, count_cases, COUNT_CASE, _nd, predict_cells, _land = R3.lines_of, R3.count_cases, R3.COUNT_CASE, R3._nd, R3.predict_cells, R3._land
KERNS, KERN_PIN, kern_state, sorry_tokens = R3.KERNS, R3.KERN_PIN, R3.kern_state, R3.sorry_tokens
STANDIN = os.environ.get('B638_STANDIN') if ('dry' in sys.argv[2:]) else None


def _bank_path(name):
    if STANDIN and os.path.exists(os.path.join(STANDIN, name)):
        return os.path.join(STANDIN, name)
    return os.path.join(D, name)


def jl(name):
    try:
        return json.load(io.open(_bank_path(name), encoding='utf-8'))
    except Exception:
        return {}


def rd(name):
    try:
        return io.open(_bank_path(name), encoding='utf-8').read().replace(chr(13), '')
    except OSError:
        return ''


DEFECTS, DEFECT_SHORT, CORRECTION = [], [], ''
_DJ = os.path.join(D, 'b638_defects.json')
if os.path.exists(_DJ):
    _dj = json.load(io.open(_DJ, encoding='utf-8'))
    DEFECTS, DEFECT_SHORT, CORRECTION = list(_dj.get('defects') or []), list(_dj.get('short') or []), _dj.get('correction') or ''


def defects(*a):
    L = ['b638 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b638_defects.txt', L)


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b638_scanfile_%s.md' % name)
    _write(p, text.encode('utf-8'))
    out = _scan(p)
    return out, _clean(out)


def _table(rev=None):
    if rev:
        return json.loads(subprocess.run(['git', '-C', ROOT, 'show', '%s:data/terminal_table.json' % rev], capture_output=True).stdout.decode('utf-8'))['rows']
    return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']


def _run_test(rel, bank, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([sys.executable, os.path.join(ROOT, *rel.split('/'))] + list(args), capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=env)
    out = (r.stdout or '') + (r.stderr or '')
    n, p = count_cases(out)
    L = ['b638 -- %s RUN AND COUNTED (%s); exit %d' % (rel, utc(), r.returncode), ''] + out.rstrip(NL).split(NL) + [
        '', '### CASES : %d ; PASSING : %d ; FAILING : %d   ### counted by the numbered case pattern' % (n, p, n - p)]
    put_txt(bank + '.txt', L)
    put_json(bank + '.json', dict(at=utc(), rc=r.returncode, cases=n, passing=p, test=rel,
                                  failing=[re.match(r'^  (\(\d+\))', l).group(1) for l in out.split(NL)
                                           if re.match(COUNT_CASE, l) and not l.rstrip().endswith('PASS')]))
    print(L[-1])


def _diff(path, rev, bank, title):
    old = (_show(RELAY, rev, path) or '').split(NL)
    new = io.open(os.path.join(ROOT, *path.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    dl = list(difflib.unified_diff(old, new, '%s@%s' % (os.path.basename(path), rev), os.path.basename(path), lineterm='', n=0))
    put_txt(bank, ['b638 -- %s, THE DIFF AGAINST relay %s (%s)' % (title, rev, utc()), '',
                   '### lines removed %d ; added %d' % (sum(1 for x in dl if x[:1] == '-' and not x.startswith('---')),
                                                        sum(1 for x in dl if x[:1] == '+' and not x.startswith('+++'))), ''] + dl)


def _cp():
    """### the generator. Its glossary renderer lands at Component 3 (after the seal); before it, a dry run reads the scratchpad prototype,
    ### and a run that writes refuses."""
    import chain_page as CP
    if hasattr(CP, 'glossary_block'):
        return CP
    if not DRY:
        sys.exit('### THE GENERATOR HAS NO GLOSSARY RENDERER YET -- NOTHING WRITTEN')
    import importlib.util
    spec = importlib.util.spec_from_file_location('chain_page_proto', os.path.join(SP, 'proto', 'chain_page.py'))
    P = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(P)
    P.ROOT = RELAY
    P.GLOSSARY_FILE = os.path.join(SP, 'data', 'glossary.txt')
    return P


def _glossary_path():
    p = os.path.join(D, 'glossary.txt')
    return p if (os.path.exists(p) or not DRY) else os.path.join(SP, 'data', 'glossary.txt')


# ================================================================================ READING (1): THE READS
def READS():
    return [
        ('OPEN_TRAILS: the lines the ferry names; the form of an edition and its title clause, the name-and-title exception, the precedence '
         'order, the page clause, the load-bearing clause, the criterion and the lines beneath it, b637`s record and correction, b632`s record',
         PP, PRE_PP, 'OPEN_TRAILS.md', sorted(set(list(K.FERRY_LINES) + [K.FORM, K.NAME_TITLE, K.PRECEDENCE, K.PAGE_CLAUSE, K.LOAD_BEARING,
                                                                         K.CRITERION, K.UNLISTED_LINE, K.UPSTREAM_LINE, K.NAME_LINE,
                                                                         K.SEAL_RULE, K.B637_RECORD, 13195])), 1600),
        ('FINDINGS: b637`s weight line on b636 and b637`s entry', PP, PRE_PP, 'FINDINGS.md', [K.B637_WEIGHT_PRIOR, K.B637_ENTRY], 700),
        ('PLACE-papers the census at v0.5 (read whole; its headings, its §1 table head, its premise table and notes, its last lines printed here, '
         'every cell in relay data/b638_census.txt)', PP, PRE_PP, K.CEN5, ('GREP', r'^#|^\| row \||^\| repository \||^\| face \||^\*The 42|^MET, '), 300),
        ('relay data/b637_census_counts.txt (b637`s counts banked for v0.6), whole', RELAY, PRE_RELAY, 'data/b637_census_counts.txt', ('GREP', r'.'), 260),
        ('relay data/b637_binder_classes.txt: Lean`s kinds and the 26 classes', RELAY, PRE_RELAY, 'data/b637_binder_classes.txt',
         ('GREP', r'Expr\.lean:|^  \| B\d\d \||^### THE GRADE'), 260),
        ('relay tools/e0_rule.py: its docstring and the binder grammar`s lines of RULE_TEXT', RELAY, PRE_RELAY, 'tools/e0_rule.py',
         list(range(1, 25)) + list(range(61, 66)), 200),
        ('relay data/b637_rerun.txt: the moves, the unnamed rows` residue line, the count', RELAY, PRE_RELAY, 'data/b637_rerun.txt',
         ('GREP', r'^### |^  U(05|06|08|09|11|12|16|17) '), 260),
        ('relay data/terminal_table.json at be0dd02d (b637`s act commit): rows by kernel, grade, provenance and kind', RELAY, 'be0dd02d',
         'data/terminal_table.json', ('TABLE', None), 300),
        ('relay tools/chain_page.py: the head line, the column`s head line, the backmatter channel, emit and build', RELAY, PRE_RELAY,
         'tools/chain_page.py', ('GREP', r"^def (emit|emit_dirichlet|build|backmatter_of|node_column)\b|^COLUMN_MARK|L = \['# THE CLAUSE|"
                                         r"L = \[DIR_TITLE|L \+= \[SHAPE_KEY|bm = backmatter_of|page = page \+ NL"), 200),
        ('relay tools/mirror_roster.json as b637 left it: the three appended editions and lastChanged', RELAY, PRE_RELAY, K.ROSTER,
         ('GREP', r'A_Place_to_Stand_v5_18|FINDINGS_AS_THEY_STAND_v0_6|KEYSTONE_CENSUS_v0_5|lastChanged'), 220),
        ('relay tools/mirror_build.ps1 (unedited): its parameter, stage and ROSTER line', RELAY, PRE_RELAY, K.BUILDER,
         ('GREP', r'param\(|mirror-build-|ROSTER|roster-CHANGE'), 200),
        ('relay tools/act_root.py: the census path', RELAY, PRE_RELAY, 'tools/act_root.py', ('GREP', r'^CENSUS = '), 200),
        ('relay data/b637_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b637_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
        ('relay data/b632_reader_answers.txt: the second reader`s G036', RELAY, PRE_RELAY, K.B632_G036[0], [K.B632_G036[1]], 300),
        ('relay data/b632_key.txt: G036`s key line', RELAY, PRE_RELAY, K.B632_KEY_G036[0], [K.B632_KEY_G036[1]], 300),
    ] + [('%s %s @ %s: structure %s and its fields' % (s['kernel'], s['path'], s['pin'], s['name']), s['repo'], s['pin'], s['path'],
          list(range(s['line'], min(s['line'] + 16, len(lines_of(_show(s['repo'], s['pin'], s['path']) or '')) + 1))), 220) for s in K.STRUCTS]


def reads(*a):
    L = ['b638 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        if isinstance(sel, tuple) and sel[0] == 'TABLE':
            rows = json.loads(t).get('rows', [])
            c = collections.Counter((r['repo'], r['grade'], r.get('provenance'), r.get('kind') or '') for r in rows)
            L.append('### %s -- %s @ %s (%d rows; by kernel, grade, provenance and kind:)' % (label, path, at, len(rows)))
            for k_, n_ in sorted(c.items(), key=lambda x: (x[0][0], -x[1])):
                L.append('    %-34s %-26s %-10s %-9s %d' % (k_[0], k_[1], k_[2], k_[3] or '-', n_))
            continue
        if isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b638_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()), len(L)))


# ================================================================================ THE PROMPTS
def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R248) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b638 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b638_author_answers.txt', L)


def answer_of(k):
    R3.rd = lambda name: rd('b638_author_answers.txt') if name == 'b633_author_answers.txt' else rd(name)
    try:
        return R3.answer_of(k)
    finally:
        R3.rd = rd


def kernels(*a):
    put_json('b638_kernels_face.json', dict(at=utc(), kernels=kern_state()))


# ================================================================================ THE SEAL'S HASHES ((R246)(3), OPEN_TRAILS :13307)
def seal_hashes():
    rec_ = jl('b638_seal_hashes.json').get('tools') or {}
    now = {}
    for t in K.SEALED:
        p = os.path.join(ROOT, 'tools', t)
        now[t] = hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None
    out = [(t, 'absent' if (t not in rec_ or now[t] is None) else ('agree' if rec_[t] == now[t] else 'differ')) for t in K.SEALED]
    return rec_, now, out


def seal_check(*a):
    rec_, now, out = seal_hashes()
    L = ['b638 -- THE SEALED TOOLS` HASHES, RECORDED AT THE SEAL AND RECOMPUTED (%s)' % utc(), '']
    L += ['  %-22s recorded %s ; now %s ; %s' % (t, (rec_.get(t) or '-')[:16], (now.get(t) or '-')[:16], v.upper()) for t, v in out]
    L += ['', '### ### **SEALED TOOLS %d ; AGREE %d ; DIFFER %d ; ABSENT %d.**' % (len(out), sum(v == 'agree' for _t, v in out),
                                                                                 sum(v == 'differ' for _t, v in out), sum(v == 'absent' for _t, v in out))]
    tag = a[0] if a and a[0] != 'dry' else 'record'
    put_txt('b638_seal_check_%s.txt' % tag, L)
    print(NL.join(L[2:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES
W_HEAD = ('*Appended 2026-10-07 by b638 to b637’s entry (:%d), under `(R248)`(1) and (3) -- b637 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS, '
          'AND THE SEAT’S FOUR READINGS CONFIRMED:*')
RC_HEAD = ('*Appended 2026-10-07 by b638 beside the title clause of the form of an edition (:%d) and the name-and-title exception (:%d), under '
           '`(R248)`(4) -- THE READER’S CLAUSE, STANDING:*')


def _weight():
    SC, RT, RC, PR, RR = (jl(n_) for n_ in ('b637_scores.json', 'b637_rule_test.json', 'b637_rule_control.json', 'b637_planted_read.json', 'b637_rerun.json'))
    TR, PZ, PX, PM, RO, AR = (jl(n_) for n_ in ('b637_table_regen.json', 'b637_page_zeta.json', 'b637_page_chi.json', 'b637_premises.json',
                                               'b637_roster.json', 'b637_act_root.json'))
    chk = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', rd('b637_checks_postpush.txt'))
    ctl = [r for r in RC.get('runs') or [] if r['test'].endswith('test_e0_rule.py')]
    kk = RR.get('kernels') or {}
    ef, sec = kk.get('SIDE-explicit-formula', {}), kk.get('SIDE-structural-error-correction', {})
    held = lambda ks, w: [k for k in ks if (SC.get(k) or [''])[0].startswith(w)]   # noqa: E731
    same927 = re.search(r'identical block (\d+) of (\d+)', rd('b637_reads.txt'))
    ndef = len([l for l in rd('b637_defects.txt').split(NL) if re.match(r'^    \([a-z]\) ', l)])
    pw = sum(1 for m in RR.get('moves') or [] if m['grade_moved'] and any(' : PWSetup ' in c for c in m['classes']))
    return ('\n%s the classification of %d binder classes from Lean’s four binder kinds and two conclusion positions, one planted declaration per '
            'class with its expected outcome banked before the rule read it (relay data/b637_binder_classes.txt); the E0 rule rewritten as a total '
            'function with names playing no part, a binder fitting no class raised as a bug and never graded; its test %s of %s, the planted '
            'declarations %d as expected, the five-name test one reading where the old rule gave two, the rule as it stood failing %d of the new '
            'cases. The rerun: %d binders, %d unclassed; the textual and elaborated readings agreeing on %s of %s explicit-formula rows (%s '
            'deferring rows uncounted) and %s of %s structural-error-correction rows; %d grades moved, %.2f %% of %d graded rows, every move a '
            'premise the old name test did not read, %d of them on H : PWSetup; all 20 unnamed rows classed, %d resting on a premise with no '
            'nameable head (%s). %d upstream rows a kind; the table moving %d rows; both pages differing in Correspondence rows alone (ζ %d, χ '
            '%d); the named premises %d heads over %d rows against v0.5’s 42 over 63; the mirror roster at %s files, the builder unedited. H71a, '
            'H71b and H71d %s; H71c %s at %.2f %% against the navigator’s 2 %% -- the bound the navigator’s, the %d moves the finding; %s HELD, '
            'N3 with H71c, N5 refuted in letter by the two re-pointed tests as ordered; %s HELD. Relay be0dd02d (closing 2aa41700); PLACE-papers '
            'acad248 (correction 5c4247b); the root %s…; the suite %s of %s; the seven sealed tools matching their hashes. Defects (a)-(%s) the '
            'seat’s, (c) the prompt naming one failing b630 case where three failed, the answer applied to all three, (g) the generator’s '
            'test-bank step skipped before the pre-push suite, corrected at OPEN_TRAILS :%d. The seat’s four readings confirmed by the author: a '
            'binder inside an existential’s body read as part of the conclusion; a binder whose type is an unlisted name applied to arguments read '
            'as a named predicate and marked so, a one-letter type the statement binds nowhere read as a type variable; MET’s names their own '
            'class, graded as premises until a name is ruled a restriction; the rerun’s bank data/elab_types.txt identical in its %s blocks to the '
            'ferry’s data/b634_elab_types.txt. Nothing deposited; no kernel source touched.\n'
            % (W_HEAD % K.B637_ENTRY, len(R7.CLASSES), RT.get('passing'), RT.get('cases'), sum(1 for x in PR.get('rows') or [] if x['test'] == 'class' and x['ok']),
               len(ctl[0]['failing']) if ctl else -1, sum((RR.get('binders') or {}).values()), len(RR.get('bugs') or []), ef.get('agree'), ef.get('both'),
               ef.get('deferred'), sec.get('agree'), sec.get('both'), RR.get('grade_moves', 0), 100.0 * RR.get('grade_moves', 0) / max(1, RR.get('graded', 1)),
               RR.get('graded', 0), pw, len(RR.get('residue') or []), ', '.join(RR.get('residue') or []), TR.get('upstream', 0), len(TR.get('moved') or []),
               (PZ.get('kinds') or {}).get('correspondence row+', 0), (PX.get('kinds') or {}).get('correspondence row+', 0), len(PM.get('rule_heads') or {}),
               sum(len(v) for v in (PM.get('rule_heads') or {}).values()), RO.get('after'),
               'HOLD' if len(held(('H71a', 'H71b', 'H71d'), 'HOLDS')) == 3 else '### NOT ALL HOLD', (SC.get('H71c') or ['?'])[0],
               100.0 * RR.get('grade_moves', 0) / max(1, RR.get('graded', 1)), RR.get('grade_moves', 0), ', '.join(held(('N1', 'N2', 'N4'), 'HELD')),
               '-'.join(held(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD')[::4]) if len(held(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD')) == 5 else held(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'),
               (AR.get('root') or '?')[:8], chk.group(2) if chk else '?', chk.group(1) if chk else '?', 'abcdefghij'[ndef - 1] if ndef else '?',
               K.B637_CORRECTION, same927.group(1) if same927 else '?'))


def _reader_clause():
    return ('\n%s every document opens with a plain statement of its objects for a reader outside the programme -- what the document is '
            'about, in sentences a mathematician who has read none of the corpus can follow; every internal name (h2, the located clause, E0, '
            'DERIVES / INTERFACES / ENCODES, MET, the act numbers, the kernel names) is defined where it enters that document and not by reference '
            'to another; abbreviations are spelled out where they enter; the two generated pages and the keystone census carry a glossary block '
            'printed by the generator from one shared source, relay data/glossary.txt, entered at b638 with the definitions as the programme states '
            'them, the located clause spelled out as the author ruled it: the Riemann Hypothesis holds exactly when the explicit-formula quadratic '
            'form Q(k) = pole term − prime sum + archimedean term is non-negative for every admissible test window k, the theorem h2_sign_iff_rh '
            'deriving the equivalence with no premise, and the open clause being the sign statement h2_sign itself, which the kernel states, '
            'proves equivalent to RH, bounds by its mechanism exclusions, and carries as its one open premise. Existing documents take the clause '
            'at their next editions; the keystone census at v0.6 takes it at b638.\n' % (RC_HEAD % (K.FORM, K.NAME_TITLE)))


def record_lines(*a):
    """### FINDINGS: b637's weight with the four readings confirmed (to :7833). OPEN_TRAILS: the reader's clause beside the title clause."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The binder grammar: ')
    if entry != K.B637_ENTRY:
        sys.exit('### b637`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B637_ENTRY, _weight()), ('OPEN_TRAILS.md', RC_HEAD % (K.FORM, K.NAME_TITLE), _reader_clause())]
    allt = ''.join(t for _f, _h, t in items)
    cells = predict_cells(items[1][2], 'OPEN_TRAILS.md') + predict_cells(items[0][2], 'FINDINGS.md')
    nd, _n = _nd(allt)
    sc, clean = _scan_text(allt, 'lines')
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT') if x in items[0][2].replace('(c) the prompt', '')]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backtick parity odd in: %s ; unread figures: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        return
    if cells or any(nd.values()) or not clean or ticks or unread:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    _land(Q, items, 'b638_record_lines.json', K.B637_ENTRY)


def glossary_read(*a):
    """### Component 1, after the seat's Write and commit: relay data/glossary.txt read by the generator's own parser -- its entries, each a
    ### name, a definition and a source; its commit alone; the block's lines (data/b638_glossary.txt)."""
    CP = _cp()
    p = _glossary_path()
    raw = open(p, 'rb').read()
    ents = CP.glossary_entries(p)
    blk = CP.glossary_block(p)
    com = [h for h in g(RELAY, 'log', '--format=%h', PRE_RELAY + '..HEAD', '--', K.GLOSSARY).split(NL) if h.strip()]
    alone = [h for h in com if sorted(x for x in g(RELAY, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip()) == [K.GLOSSARY]]
    L = ['b638 -- COMPONENT 1, (R248)(4): THE SHARED GLOSSARY, relay %s, READ BY THE GENERATOR`S PARSER (%s)' % (K.GLOSSARY, utc()), '',
         '### bytes %d ; sha256 %s ; entries %d ; comment lines %d ; the commits touching it since %s: %s ; committed alone: %s' % (
             len(raw), sha(raw), len(ents), sum(1 for l in raw.decode('utf-8').split(NL) if l.startswith('#')), PRE_RELAY, com or 'NONE', alone or 'NONE'),
         '### the located clause`s entry as the ruling words it: %s' % any(e[0] == 'the located clause' and e[1].startswith(
             'the Riemann Hypothesis holds exactly when the explicit-formula quadratic form') for e in ents), '',
         '### THE BLOCK, AS EVERY DOCUMENT PRINTS IT (%d lines):' % len(blk)] + ['    ' + l for l in blk]
    L += ['', '### ### **ENTRIES %d ; BLOCK LINES %d ; COMMITTED ALONE %s.**' % (len(ents), len(blk), bool(alone))]
    put_txt('b638_glossary.txt', L)
    put_json('b638_glossary.json', dict(at=utc(), sha256=sha(raw), bytes=len(raw), entries=len(ents), keys=[e[0] for e in ents], block_lines=len(blk),
                                        block_sha256=sha((NL.join(blk) + NL).encode('utf-8')), commits=com, alone=alone))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE FIELD PRINT
def struct_fields(st):
    """### a structure's declaration line and its fields read by git at the pin: [dict(name, line, type)] -- a field a line `  name : type`
    ### (its continuation lines joined), doc comments passed over, the block ending at the first blank or unindented line."""
    t = _show(st['repo'], st['pin'], st['path']) or ''
    ls = t.split(NL)
    head = ls[st['line'] - 1] if 0 < st['line'] <= len(ls) else ''
    out, cur, in_doc = [], None, False
    for i in range(st['line'], len(ls)):
        l = ls[i]
        if in_doc:
            if '-/' in l:
                in_doc = False
            continue
        if re.match(r'^\s*/-', l):
            in_doc = '-/' not in l
            continue
        if not l.strip() or not l.startswith(' '):
            break
        m = re.match(r'^  (\S+) : (.*)$', l)
        if m:
            if cur:
                out.append(cur)
            cur = dict(name=m.group(1), line=i + 1, type=m.group(2).strip())
        elif cur and l.startswith('    '):
            cur['type'] += ' ' + l.strip()
    if cur:
        out.append(cur)
    return head, out


def _head_decl(name, st):
    """### a field type's head named by the rule's typing as unread or unlisted: its declaration in the structure's kernel by git grep at the
    ### pin -- `def NAME ... : Prop :=` or `structure NAME ... : Prop where` -- RETURN (file:line, the line, its kind)."""
    rc = subprocess.run(['git', '-C', st['repo'], 'grep', '-n', '-E', r'^(def|structure|abbrev|class|inductive) %s\b' % re.escape(name), st['pin'], '--', '*.lean'],
                        capture_output=True)
    hits = [x for x in rc.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if x.strip()]
    if not hits:
        return None, None, None
    pth, ln, txt = hits[0].split(':', 3)[1:4] if hits[0].count(':') >= 3 else (hits[0], '', '')
    kind = 'prop' if re.search(r':\s*Prop\s*(:=|where)\s*$', txt.strip()) else ('data' if re.search(r':\s*Type', txt) else None)
    return '%s :%s' % (pth, ln), txt.strip(), kind


def fields(*a):
    """### Component 2, (R248)(2): every structure type among b637's 93 moves, its fields printed from the kernel source at the pin with each
    ### field's kind (Prop or data) -- read by the rule's own typing() in the declaration's context, and where the typing reads a field's head
    ### as a name no lexicon lists, that head's own declaration read by git grep; the ruling applied per type (every field a Prop: the moves on
    ### it stand; a data field: they revert and the grammar takes the data clause), the moves counted per type; the move premises that are no
    ### structure printed beside. Banked as data/b638_structure_fields.txt and its json."""
    import e0_rule as E
    RR = jl('b637_rerun.json')
    moves = [m for m in RR.get('moves') or [] if m['grade_moved']]
    out, L = [], ['b638 -- COMPONENT 2, (R248)(2): THE FIELD PRINT -- EVERY STRUCTURE TYPE AMONG b637`S %d MOVES, EACH FIELD WITH ITS KIND (%s)' % (len(moves), utc()), '',
                  '### each field read by the rule`s own typing() (relay tools/e0_rule.py) in its declaration`s context; a head the typing reads as unlisted or '
                  'unread settled by its own declaration at the pin (git grep). THE RULING`S TEST: every field a Prop -- the moves on the type stand at '
                  'INTERFACES on a premise structure; any field data -- the type is an object of the statement, its moves revert, the grammar gains the '
                  'data-structure clause.', '']
    for st in K.STRUCTS:
        head, fs = struct_fields(st)
        rows = []
        for f in fs:
            ty, how = E.typing(f['type'], st['ctx'])
            decl = None
            if ty is None or how.startswith('UNLEXED'):
                hn = re.match(r'^([A-Za-z_][\w.]*)', f['type'])
                d_where, d_line, d_kind = _head_decl(hn.group(1).split('.')[-1], st) if hn else (None, None, None)
                decl = dict(where=d_where, line=d_line, kind=d_kind)
                kind = d_kind
            else:
                kind = ty
            rows.append(dict(f, typing=ty, how=how, decl=decl, kind=kind))
        pat = re.compile(r' : (?:[\w.]+\.)?%s\b' % re.escape(st['name']))
        on = [m for m in moves if any(pat.search(c) for c in m['classes'])]
        allprop = bool(rows) and all(r['kind'] == 'prop' for r in rows)
        out.append(dict(name=st['name'], kernel=st['kernel'], pin=st['pin'], path=st['path'], line=st['line'], head=head, fields=rows,
                        declared_prop=bool(re.search(r':\s*Prop\s+where\s*$', head)), all_prop=allprop, moves=[m['name'] for m in on],
                        ruling=('the moves stand' if allprop else 'the moves revert')))
        L.append('== structure %s -- %s %s :%d at %s ; declared %s' % (st['name'], st['kernel'], st['path'], st['line'], st['pin'], head.strip()))
        for r in rows:
            L.append('     :%-5d %-18s %-5s %-62s %s' % (r['line'], r['name'], (r['kind'] or 'NONE').upper(), (r['how'] if not r['decl'] else
                     'the typing: %s ; its head`s declaration %s: %s' % (r['how'][:40], r['decl']['where'], r['decl']['line']))[:150], r['type'][:110]))
        L.append('   ### fields %d ; Prop %d ; data %d ; unread %d ; the moves resting on it %d ; THE RULING: %s' % (
            len(rows), sum(r['kind'] == 'prop' for r in rows), sum(r['kind'] == 'data' for r in rows), sum(r['kind'] is None for r in rows), len(on),
            out[-1]['ruling'].upper()))
        L.append('')
    covered = set(n for x in out for n in x['moves'])
    rest = [m for m in moves if m['name'] not in covered]
    L += ['### THE MOVES RESTING ON NO STRUCTURE TYPE (%d), each with the premise binders the rerun printed:' % len(rest)]
    L += ['  %-30s %-62s %s' % (m['repo'], m['name'][:62], '; '.join(m['classes'])[:220]) for m in rest]
    pw = next(x for x in out if x['name'] == 'PWSetup')
    nf = sum(len(x['fields']) for x in out)
    L += ['', '### THE SECOND READER`S G036 AT b632 (relay %s :%d): %s' % (K.B632_G036[0], K.B632_G036[1], (lines_of(_show(RELAY, PRE_RELAY, K.B632_G036[0]) or '') + [''] * 99)[K.B632_G036[1] - 1]),
          '', '### ### **STRUCTURE TYPES %d ; FIELDS %d ; DATA FIELDS %d ; UNREAD %d ; TYPES ALL PROP %d ; MOVES STANDING %d ; MOVES REVERTING %d ; '
          'PWSetup: %d FIELDS, %s, %d MOVES %s.**' % (
              len(out), nf, sum(r['kind'] == 'data' for x in out for r in x['fields']), sum(r['kind'] is None for x in out for r in x['fields']),
              sum(x['all_prop'] for x in out), sum(len(x['moves']) for x in out if x['all_prop']), sum(len(x['moves']) for x in out if not x['all_prop']),
              len(pw['fields']), 'EVERY ONE A PROP' if pw['all_prop'] else 'A DATA FIELD AMONG THEM', len(pw['moves']), 'STANDING' if pw['all_prop'] else 'REVERTING')]
    put_txt('b638_structure_fields.txt', L)
    put_json('b638_structure_fields.json', dict(at=utc(), types=out, rest=[dict(repo=m['repo'], name=m['name'], classes=m['classes']) for m in rest],
                                                fields=nf, all_prop=all(x['all_prop'] for x in out), pwsetup_fields=len(pw['fields']),
                                                pwsetup_moves=len(pw['moves']), pwsetup_all_prop=pw['all_prop'],
                                                standing=sum(len(x['moves']) for x in out if x['all_prop']),
                                                reverting=sum(len(x['moves']) for x in out if not x['all_prop'])))
    print(L[-1])


G_HEAD = '*Appended 2026-10-07 by b638 to b632’s record (:%d), under `(R248)`(2) -- THE SECOND READER’S G036 READING, RESOLVED BY THE FIELD PRINT:*'
B632_RECORD = 13195


def _g036():
    F = jl('b638_structure_fields.json')
    pw = next((x for x in F.get('types') or [] if x['name'] == 'PWSetup'), {})
    return ('\n%s the structure PWSetup Z g0 L M (SIDE-explicit-formula SIDEExplicitFormula/PowerLimit.lean :%s at %s) was printed field by field '
            '(relay data/b638_structure_fields.txt): %d fields, %s, each read by the rule’s own typing. PWSetup is a premise structure about '
            'the fixed objects it names and not an object of the statement, and the %d rows b637’s rewritten rule moved onto it stand. The second '
            'reader’s reading of G036 at b632 (relay data/b632_reader_answers.txt :36: H : PWSetup read as a data binder, “reading uncertain if '
            'PWSetup is a Prop-only structure”) is recorded as the reader’s uncertainty, resolved against it. The other %d structure types among '
            'b637’s moves were printed by the same test, %s.\n' % (
                G_HEAD % B632_RECORD, pw.get('line'), pw.get('pin'), len(pw.get('fields') or []),
                'every one a Prop' if pw.get('all_prop') else '### NOT EVERY ONE A PROP', len(pw.get('moves') or []), len(F.get('types') or []) - 1,
                'every field of each a Prop' if F.get('all_prop') else '### NOT EVERY FIELD A PROP'))


def g036_line(*a):
    """### Component 2 where every field of PWSetup is a Prop: the G036 note appended to OPEN_TRAILS addressed to b632's record (:13195)."""
    F = jl('b638_structure_fields.json')
    if not F:
        sys.exit('### NO FIELD BANK -- NOTHING WRITTEN')
    if not F.get('pwsetup_all_prop'):
        sys.exit('### A DATA FIELD IN PWSetup: THE MOVES REVERT AND NO G036 NOTE IS ENTERED -- NOTHING WRITTEN')
    Q = R2._Q()
    rec_ = lines_of(_show(PP, PRE_PP, 'OPEN_TRAILS.md'))[B632_RECORD - 1]
    if not rec_.startswith('### b632 '):
        sys.exit('### b632`S RECORD IS NOT AT :%d (%s) -- NOTHING WRITTEN' % (B632_RECORD, rec_[:60]))
    t = _g036()
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'g036')
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; backticks %d' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', t.count('`')))
    if DRY:
        print(t)
        return
    if cells or any(nd.values()) or not clean or t.count('`') % 2 or '###' in t:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM OR AN UNREAD FIGURE -- NOTHING WRITTEN')
    _land(Q, [('OPEN_TRAILS.md', G_HEAD % B632_RECORD, t)], 'b638_g036_line.json')


# ================================================================================ COMPONENT 3: THE GLOSSARY BLOCK ON THE PAGES
LIST_HEAD = {k: ['# b638 -- (R248)(4), THE READER`S CLAUSE: b632`s list (relay data/%s), every line unchanged, with the one line' % K.OLD_NODES[k],
                 '# `# glossary` appended, by which the generator prints the glossary block from relay data/glossary.txt beneath the page`s head',
                 '# line (relay tools/chain_page.py, `node_glossary`). A list without that line emits exactly as before.', '#'] for k in ('zeta', 'chi')}


def lists(*a):
    """### Component 3: data/b638_nodes_zeta.txt and data/b638_nodes_chi.txt -- b632's lists, every line unchanged, a head and the mark."""
    for k in ('zeta', 'chi'):
        old = io.open(os.path.join(D, K.OLD_NODES[k]), encoding='utf-8').read().replace(chr(13), '')
        new = NL.join(LIST_HEAD[k]) + NL + old + ('' if old.endswith(NL) else NL) + K.GLOSSARY_MARK + NL
        p = os.path.join(SP if DRY else D, K.NODES[k])
        if not DRY and os.path.exists(p):
            sys.exit('### %s EXISTS -- NOTHING WRITTEN' % K.NODES[k])
        _write(p, new.encode('utf-8'))
        print('  %s : %d lines, b632`s %d carried, sha256 %s' % (K.NODES[k], new.count(NL), old.count(NL), sha(new.encode('utf-8'))[:16]))


def gen_test(*a):
    """### the glossary edit: tools/chain_page.py against relay 2aa41700; tools/test_chain_page_b638.py run and counted."""
    _diff('tools/chain_page.py', PRE_RELAY, 'b638_gen_diff.txt', 'THE GENERATOR`S GLOSSARY BLOCK, (R248)(4)')
    _run_test('tools/test_chain_page_b638.py', 'b638_gen_test')


def glossary_lines(text):
    """### the glossary block's lines as a document prints them: from its heading to its last entry line; [] where there is none."""
    ls = text.replace(chr(13), '').split(NL)
    if '## Glossary' not in ls:
        return []
    i = ls.index('## Glossary')
    j = i + 4
    while j < len(ls) and ls[j].startswith('- **'):
        j += 1
    return ls[i:j]


def page(k, tag='glossary', *a):
    """### ONE page per call in the foreground, re-emitted from the list in force (b638's, from Component 3) and b635's probe (no Lean),
    ### written only where it changed; `tag` names the step: glossary (Component 3) or placement (the page clause after the census)."""
    CP = _cp()
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    nl, pr = K.NODES[k], K.PROBE[k]
    lp = os.path.join(SP if (DRY and not os.path.exists(os.path.join(D, nl))) else D, nl)
    t0 = time.time()
    rc, pg, meta, log = CP.build(lp, os.path.join(SP, '_b638_%s' % k), os.path.join(D, pr))
    secs = int(time.time() - t0)
    bank = 'b638_page_%s_%s.json' % (k, tag)
    if rc:
        put_json(bank, dict(rc=rc, log=log, at=utc(), nodes=nl, probe=pr))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout)
    changed = prev != b
    if changed and not DRY:
        _write(os.path.join(PP, K.PNAME[k]), b)
    if DRY:
        _write(os.path.join(SP, 'b638_page_%s_%s.md' % (k, tag)), b)
    dl = [x for x in difflib.unified_diff(prev.decode('utf-8').split(NL), pg.split(NL), 'HEAD', 'regenerated', lineterm='', n=0)
          if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    ga, gb = R3._grade_cells(prev.decode('utf-8')), R3._grade_cells(pg)
    gmoved = sorted(n for n in set(ga) | set(gb) if ga.get(n) != gb.get(n))

    def kind(x):
        s = x[1:]
        if s.startswith('- **') or s in ('## Glossary',) or s.startswith('*The internal names this document uses'):
            return 'glossary'
        if s.startswith('This page is generated by relay'):
            return 'head line'
        if s.startswith('| keystone naming a node |'):
            return 'placement row'
        if s.startswith('|'):
            return 'correspondence row'
        if s.startswith('#'):
            return 'heading'
        return 'prose' if s.strip() else 'blank'
    kinds = collections.Counter(kind(x) + x[0] for x in dl)
    gl = glossary_lines(pg)
    put_json(bank, dict(page=K.PNAME[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, cells_moved=gmoved, kinds=dict(kinds),
                        glossary_lines=len(gl), glossary_sha256=sha((NL.join(gl) + NL).encode('utf-8')) if gl else None, free_mb_before=fm,
                        seconds=secs, nodes=nl, probe=pr, tag=tag, at=utc(), dry=DRY))
    print('  %s %s : exit %d ; changed against HEAD %s ; %d s ; diff lines %d by kind %s ; cells moved %s ; glossary lines %d' % (
        k, tag, rc, changed, secs, len(dl), dict(kinds), gmoved or 'NONE', len(gl)))


def page_arms(*a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import chain_page as CP
    import b626_record as R26
    L = ['b638 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc())]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b638_gcp'), os.path.join(D, K.PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- %s ; regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', K.NODES[k], r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
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
    put_txt('b638_page_arms.txt', L)
    for l in L:
        print(l[:240])


def tests_after(name=None, *a):
    """### b637's lesson (its defect (b)): after the generator's commit, every test file under tools/ run with the lists in force from this
    ### act (b638's, b635's probes), one per call, appended to data/b638_tests_after.json; `tests_after report` writes the text bank."""
    T_ = os.path.join(ROOT, 'tools')
    bank = os.path.join(D, 'b638_tests_after.json')
    # ### the Lean reader's test reads no generator and runs lean: its step-zero run stands, and no lean call is made after the seal
    names = sorted(f for f in os.listdir(T_) if f.startswith('test_') and (f.endswith('.py') or f.endswith('.sh')) and f != 'test_elab_reader_b634.py')
    if name == 'test_elab_reader_b634.py':
        sys.exit('### THE LEAN READER`S TEST IS NOT RE-RUN AFTER THE SEAL -- NOTHING RUN')
    try:
        j = json.load(io.open(bank, encoding='utf-8'))
    except Exception:
        j = {}
    if name == 'report':
        nf = [n for n in names if n in j and (j[n]['rc'] != 0 or j[n]['failing'])]
        L = ['b638 -- EVERY TEST FILE UNDER tools/ RUN AFTER THE GENERATOR`S COMMIT, THE LISTS IN FORCE b638`S (%s)' % utc(), '']
        L += ['  %-34s exit %s ; cases %s ; passing %s ; failing %s ; %s s' % (n, j[n]['rc'], j[n]['cases'], j[n]['passing'], j[n]['failing'] or 'none',
                                                                         j[n]['seconds']) if n in j else '  %-34s ### NOT RUN' % n for n in names]
        L += ['', '### ### **TEST FILES %d ; RUN %d ; NOT CLEAN %d %s.**' % (len(names), sum(n in j for n in names), len(nf), nf or '')]
        L += ['', '### THE OUTPUTS, WHOLE:'] + [x for n in names if n in j for x in (['', '=== %s' % n] + j[n]['output'].rstrip(NL).split(NL))]
        put_txt('b638_tests_after.txt', L)
        print(NL.join(L[2:2 + len(names) + 3]))
        return
    ZL, ZP_ = os.path.join(D, K.NODES['zeta']), os.path.join(D, K.PROBE['zeta'])
    CL, CPR = os.path.join(D, K.NODES['chi']), os.path.join(D, K.PROBE['chi'])
    ZPAGE = os.path.join(PP, K.PAGE)
    ARGS = {'test_chain_page.py': [ZL, ZP_, ZPAGE, CL, CPR], 'test_g_chain_page.py': [ZL, ZP_, ZPAGE], 'test_e0_rule.py': [K.PLANTED_DIR]}
    cmd = (['bash', os.path.join(T_, name)] if name.endswith('.sh') else [sys.executable, os.path.join(T_, name)]) + ARGS.get(name, [])
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, env=dict(os.environ, PYTHONIOENCODING='utf-8'),
                       timeout=(3000 if name == 'test_elab_reader_b634.py' else 580))
    out = (r.stdout or '') + (r.stderr or '')
    cases = [l for l in out.split(NL) if re.match(COUNT_CASE, l)]
    j = json.load(io.open(bank, encoding='utf-8')) if os.path.exists(bank) else {}
    j[name] = dict(rc=r.returncode, seconds=int(time.time() - t0), cases=len(cases), passing=sum(1 for c in cases if c.rstrip().endswith('PASS')),
                   failing=[re.match(r'^  (\(\d+\))', c).group(1) for c in cases if not c.rstrip().endswith('PASS')],
                   last=([l for l in out.split(NL) if l.strip()][-1:] or [''])[0][:200], args=[os.path.basename(x) for x in ARGS.get(name, [])], output=out)
    put_json('b638_tests_after.json', j)
    x = j[name]
    print('  %-34s exit %d ; cases %d ; passing %d ; failing %s ; %d s ; last: %s' % (name, x['rc'], x['cases'], x['passing'], x['failing'] or 'NONE',
                                                                                  x['seconds'], x['last'][:90]))


# ================================================================================ COMPONENT 4: THE CENSUS READS
PROV = ('cell', 'rule', 'rule-elab', 'none')


def _is_up(r):
    return r.get('kind') == 'upstream'


def _prov_counts(rows):
    c = collections.Counter()
    for r in rows:
        c['upstream' if _is_up(r) else (r.get('provenance') or 'none')] += 1
    return dict((k, c.get(k, 0)) for k in PROV + ('upstream',))


def _prov_cell(p):
    return '%d / %d / %d / %d%s' % (p['cell'], p['rule'], p['rule-elab'], p['none'], (' (+%d upstream)' % p['upstream']) if p['upstream'] else '')


def _cs():
    """### b633's census reads, imported and pointed at this act's pins: PLACE-papers 5c4247b, the mirror roster at relay's step-zero commit,
    ### the census's own previous version at 5c4247b; every repository read by ONE `git ls-remote origin`, cached."""
    import b633_census as CS
    CS.K.PRE_PP = CS.C.PRE_PP = CS.C9.PRE_PP = PRE_PP
    CS.C.STEPZERO = CS.C9.STEPZERO = STEPZERO
    CS.C9.V03_PP = PRE_PP
    return CS


def _v05_rows():
    out = {}
    for i, l in enumerate(lines_of(K.show(K.CEN5)), 1):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if m and m.group(1) not in out and l.count(' | ') >= 8 and i < 80:
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = dict(line=i, text=l, cells=c)
    return out


def _premise_binders(r, E):
    """### a row's premise binders under the live rule: its elaborated head for rule-elab rows (the row's kernel's bank), its textual head else."""
    import terminal_table as TT
    if r.get('provenance') == 'rule-elab':
        bank = {'SIDE-explicit-formula': 'elab_types.txt', 'SIDE-structural-error-correction': 'b636_elab_sec.txt'}.get(r['repo'], 'elab_types.txt')
        e = TT.elab_bank(os.path.join(D, bank)).get(r['name'])
        head = R7._elab_head(e) if e else ''
    else:
        head = R7._textual_head(r.get('statement'))[1] or ''
    return head, [b for b in E.binders_of(head) if b['outcome'] in ('premise', 'seam')] if head else []


def census(*a):
    """### Component 4, (R248)(5): every read of the census at v0.6, banked before any writing (data/b638_census.txt, Parts A-I, and its
    ### json): the root's repository list and one ls-remote each; every cell of §1 old -> new with its source; the kernel column with the
    ### tags re-read; the provenance per row and per repository under the upstream exclusion (cell / rule / rule-elab / none, upstream apart)
    ### from the table at relay HEAD; the faces through v0.25; the Phase 2 rows as b636 re-read them; the ANNEX's intake by digest; the
    ### premise table recomputed (the census's method, b637's) and summed against the table's INTERFACES count; the unnamed residue's binders
    ### printed verbatim; MET."""
    import e0_rule as E
    CS = _cs()
    for name in CS.root_list():
        CS.read_remote(name)
    B = CS.C9.build(read_remotes=True)
    J = B['J']
    for row in J:
        row['editions'] = [e.replace('(v0.4 this edition, beside it)', '(v0.6 this edition, beside it)') for e in row['editions']]
        row['table_line'] = CS.C9.table_line(row)
    rows = _table()
    head = g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()
    by_repo = collections.defaultdict(list)
    for r in rows:
        by_repo[r['repo']].append(r)
    old = _v05_rows()
    prov, changed = {}, []
    intake = CS.intake()
    for row in J:
        rr = [r for k in row['kernel_src'] for r in by_repo.get(k, [])]
        prov[row['n']] = _prov_counts(rr)
        o = old.get(row['n'], {}).get('cells') or []
        nc = [x.strip() for x in row['table_line'].strip().strip('|').split(' | ')]
        if row['n'] == 'R22' and len(o) > 3:
            nc[3] = o[3]   # ### the ANNEX row as at v0.5: its keystones cell carries v0.5's intake figures by digest
        nc.append(_prov_cell(prov[row['n']]))
        row['cells6'] = nc
        cols = ('n', 'label', 'documents', 'keystones', 'editions', 'sieve', 'kernels', 'deposit', 'provenance')
        for i, c in enumerate(cols):
            if i < len(o) and i < len(nc) and o[i] != nc[i]:
                changed.append(dict(row=row['n'], col=c, was=o[i], now=nc[i]))
    column = []
    for name in CS.root_list():
        rt = CS.read_remote(name)
        p = CS.repo_path(name)
        corpus = name in ('relay', 'PLACE-papers')
        cur = CS.C.current_tag(dict(tags=rt['tags'])) if (rt['ok'] and rt['tags'] and not corpus) else None
        column.append(dict(repo=name, corpus=corpus, ok=rt['ok'], local_main=g(p, 'rev-parse', 'main').strip(), remote_main=rt['heads'].get('main'),
                           current=cur, peel=rt['tags'].get(cur) if cur else None, local_peel=(CS.C.local_peel(name, cur) if cur else None),
                           local_only=(CS.C.local_only_tags(name, dict(ok=rt['ok'], tags=rt['tags'])) if not corpus else []),
                           rows=[row['n'] for row in J if name in row['kernel_src']], table=_prov_counts(by_repo.get(name, []))))
    v5col = {}
    for l in lines_of(K.show(K.CEN5)):
        m = re.match(r'^\| (relay|PLACE-papers|SIDE-[\w-]+) \| ', l)
        if m and m.group(1) not in v5col:
            v5col[m.group(1)] = [x.strip() for x in l.strip().strip('|').split(' | ')]
    faces = []
    for fid, label, tag, fsha, prefix, path in CS.K.FACES:
        rs = sorted((r for r in rows if r['repo'] == 'SIDE-explicit-formula' and (r['name'].startswith(prefix) if prefix.endswith('.') else r['name'] == prefix)),
                    key=lambda x: x['name'])
        items = []
        for r in rs:
            _h, pb = _premise_binders(r, E) if r['grade'] == 'INTERFACES' else ('', [])
            items.append(dict(name=r['name'], grade=r['grade'], provenance=r.get('provenance'), premises=['%s : %s' % (b['name'], b['type']) for b in pb]))
        faces.append(dict(id=fid, label=label, tag=tag, commit=g(CS.K.KER, 'rev-parse', '--short=7', tag + '^{commit}').strip(), want=fsha, path=path, items=items))
    P2 = jl('b636_phase2_read.json')
    # ### the premise table: the census's method (b637's premises): rule-graded INTERFACES rows, each premise's named head by
    # ### b632_record.premise_name; rule-elab rows beside; the rows with a premise no head names apart; upstream rows excluded
    heads, eheads, unnamed, byclass = collections.defaultdict(set), collections.defaultdict(set), set(), collections.defaultdict(set)
    for r in rows:
        if _is_up(r) or r['grade'] != 'INTERFACES' or r.get('provenance') not in ('rule', 'rule-elab'):
            continue
        hd, pb = _premise_binders(r, E)
        key = (r['repo'], r['name'])
        for b in pb:
            nm, _w = R7._premise_heads(b, hd)
            byclass[b['cls']].add(key)
            if nm:
                (heads if r.get('provenance') == 'rule' else eheads)[nm].add(key)
            else:
                unnamed.add(key)
    v5p = R7._census_premise_table()
    ledgers = dict((f, lines_of(K.show(f))) for f in ('FINDINGS.md', 'OPEN_TRAILS.md'))
    ptab = []
    for h in sorted(set(heads) | set(eheads)):
        disc = ['%s :%d' % (f.replace('.md', ''), i) for f, ls in ledgers.items() for i, l in enumerate(ls, 1)
                if re.search(r'(?<![\w.])' + re.escape(h) + r'(?![\w])', l) and re.search(r'discharg', l, re.I)]
        ks = sorted(set(k for k, _n in heads.get(h, set()) | eheads.get(h, set())))
        cm = sorted(set((next((r.get('head') or '' for r in rows if (r['repo'], r['name']) == x), '') or '')[:7] for x in heads.get(h, set()) | eheads.get(h, set())))
        ptab.append(dict(head=h, rule=len(heads.get(h, ())), elab=len(eheads.get(h, ())), kernels=ks, commits=[c for c in cm if c],
                         v05=list(v5p[h]) if h in v5p else None, discharge=disc[:4]))
    interfaces = dict(all=sum(1 for r in rows if r['grade'] == 'INTERFACES'), excluded=sum(1 for r in rows if r['grade'] == 'INTERFACES' and not _is_up(r)),
                      rule=sum(1 for r in rows if r['grade'] == 'INTERFACES' and not _is_up(r) and r.get('provenance') == 'rule'),
                      rule_elab=sum(1 for r in rows if r['grade'] == 'INTERFACES' and not _is_up(r) and r.get('provenance') == 'rule-elab'),
                      cell=sum(1 for r in rows if r['grade'] == 'INTERFACES' and not _is_up(r) and r.get('provenance') == 'cell'))
    RR = jl('b637_rerun.json')
    residue = []
    for u in RR.get('unnamed') or []:
        if u['id'] not in (RR.get('residue') or []):
            continue
        r = next((x for x in rows if (x['repo'], x['name']) == (u['repo'], u['name'])), {})
        hd, pb = _premise_binders(r, E) if r else ('', [])
        residue.append(dict(id=u['id'], repo=u['repo'], name=u['name'], grade=r.get('grade'), provenance=r.get('provenance'),
                            binders=[dict(name=b['name'], kind=b['kind'], cls=b['cls'], type=b['type'],
                                          head=(R7._premise_heads(b, hd)[0] or None)) for b in pb]))
    met = sorted(getattr(E, 'MET', []) or [])
    sum_rule = sum(x['rule'] for x in ptab)
    sum_elab = sum(x['elab'] for x in ptab)
    L = ['b638 -- COMPONENT 4, (R248)(5): THE CENSUS READS, BANKED BEFORE ANY WRITING (%s); PLACE-papers %s ; relay %s ; the table at relay %s' % (
        utc(), PRE_PP, head, head), '',
         '### PART A -- THE ROOT`S REPOSITORY LIST (tools/act_root.py repositories() at PLACE-papers %s): %d ; ls-remote reads this run %d, at most %d per '
         'repository' % (PRE_PP, len(CS.root_list()), sum(CS.LSR.values()), max(CS.LSR.values()) if CS.LSR else 0), '    ' + ', '.join(CS.root_list()), '',
         '### PART B -- EVERY CELL OF §1 OLD -> NEW, WITH ITS SOURCE (b619`s resolvers at this act`s pins): %d cells in %d rows' % (
             len(changed), len(set(c['row'] for c in changed)))]
    SRC = dict(documents='REGISTRY @ %s, R-1 and R-2' % PRE_PP, keystones='the class lines; R-10', editions='the editions and the trails; R-9',
               sieve='the sieve v0.6`s headings', kernels='ls-remote, once per repository; R-6', deposit='the mirror roster at relay %s' % STEPZERO,
               provenance='the terminal table at relay %s under the upstream exclusion' % head, label='REGISTRY', n='-')
    for c in changed:
        L += ['  %s %s (%s)' % (c['row'], c['col'], SRC[c['col']]), '      was: %s' % c['was'], '      now: %s' % c['now']]
    L += ['', '### PART C -- THE KERNEL COLUMN AT THE ROOT`S LIST (repository | local main | remote main | current tag = peel at the remote | local peel | '
          'tags the clone carries unpushed | census rows naming it | table rows cell/rule/rule-elab/none, upstream apart | v0.5`s tag cell):']
    for x in column:
        L.append('  %-34s %s | %s | %s | %s | %s | %s | %s | %s' % (
            x['repo'], (x['local_main'] or '')[:7], (x['remote_main'] or '')[:7], ('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else
            ('the corpus`s own' if x['corpus'] else 'no tag'), (x['local_peel'] or '')[:7], x['local_only'] or '-', ', '.join(x['rows']) or '-',
            _prov_cell(x['table']), (v5col.get(x['repo']) or ['', '', '?'])[2]))
    un = [(x['repo'], x['local_only']) for x in column if x['local_only']]
    L += ['  ### kernels carrying tags their remotes do not: %d, tags %d -- %s' % (len(un), sum(len(t) for _r, t in un), un),
          '  ### every current tag reads back at its clone: %s' % all(x['peel'] == x['local_peel'] for x in column if x['current']),
          '  ### tags moved since v0.5: %s' % ([x['repo'] for x in column if v5col.get(x['repo']) and v5col[x['repo']][2] != (
              'the corpus’s own' if x['corpus'] else (('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else 'no tag'))] or 'NONE'), '',
          '### PART D -- THE FACES THROUGH v0.25 (the explicit-formula kernel at v0.22-v0.25, from the table at relay %s):' % head]
    for f in faces:
        L.append('  %s %s at %s = %s (wanted %s) -- %s' % (f['id'], f['label'], f['tag'], f['commit'], f['want'], f['path']))
        L += ['      %-60s %-11s %-9s %s' % (i['name'], i['grade'], i['provenance'], '; '.join(i['premises']) or '-') for i in f['items']]
    L += ['', '### PART E -- PROVENANCE PER ROW UNDER THE EXCLUSION (the table`s rows of the kernels each row names: cell / rule / rule-elab / none, '
          'upstream apart):'] + ['  %s %s   %s' % (n, _prov_cell(v), '') for n, v in sorted(prov.items())]
    L += ['', '### PART F -- THE PHASE 2 ROWS AS b636 RE-READ THEM (relay data/b636_phase2_read.json): SEC`s theorems %s ; rows %d ; triggers %d' % (
        P2.get('theorems'), len(P2.get('rows') or []), len(P2.get('triggers') or []))]
    L += ['  %s' % json.dumps(x, ensure_ascii=False)[:260] for x in P2.get('rows') or []]
    L += ['', '### PART G -- THE ANNEX: the intake pilot`s summary banks (the paper`s text absent): %s ; claims %s ; grades %s ; kernel-verified %s' % (
        ['%s sha256 %s (%d bytes)' % (b['path'], b['sha256'], b['bytes']) for b in intake['banks']], intake['claims'], intake['grades'], intake['kv'])]
    L += ['', '### PART H -- THE PREMISE TABLE (the census`s method, b637`s premises: rule-graded INTERFACES rows, each premise`s named head by '
          'b632_record.premise_name; rule-elab rows beside; upstream rows excluded): heads %d ; rule rows summed %d ; rule-elab rows summed %d ; rows '
          'with a premise no head names %d' % (len([x for x in ptab if x['rule']]), sum_rule, sum_elab, len(unnamed)),
          '  ### THE TABLE`S INTERFACES ROWS: every row %d ; the upstream rows excluded %d ; of them rule %d, rule-elab %d, cell %d' % (
              interfaces['all'], interfaces['excluded'], interfaces['rule'], interfaces['rule_elab'], interfaces['cell']),
          '  ### THE SUM AGAINST THE COUNT ((R248)(5), H72b): the heads` rule rows summed %d against the table`s INTERFACES rows %d (rule-graded %d) ; '
          'with the rule-elab rows %d' % (sum_rule, interfaces['excluded'], interfaces['rule'], sum_rule + sum_elab)]
    L += ['  %-30s rule %3d ; rule-elab %3d ; v0.5 %s ; kernels %s ; discharge %s' % (x['head'], x['rule'], x['elab'], x['v05'] and '%d → %d' % tuple(x['v05'][1:]),
                                                                                    x['kernels'], x['discharge'] or 'none named') for x in ptab]
    L += ['', '### PART I -- THE UNNAMED RESIDUE (relay data/b637_rerun.txt`s %d), EACH ROW`S PREMISE BINDERS PRINTED VERBATIM, NO NAME INVENTED:' % len(residue)]
    for x in residue:
        L.append('  %s %-26s %-62s %s / %s' % (x['id'], x['repo'], x['name'], x['grade'], x['provenance']))
        L += ['      %-5s %-15s %s : %s   (head: %s)' % (b['cls'], b['kind'], b['name'], b['type'], b['head'] or 'none nameable') for b in x['binders']]
    L += ['', '### MET, the rule`s forward guard (relay tools/e0_rule.py MET): %d names -- %s' % (len(met), ', '.join(met)), '',
          '### ### **CELLS CHANGED %d IN %d ROWS ; REPOSITORIES %d ; TAGS MOVED %d ; HEADS %d OVER %d RULE ROWS ; UNNAMED RESIDUE %d ; INTERFACES ROWS %d.**' % (
              len(changed), len(set(c['row'] for c in changed)), len(column),
              len([x for x in column if v5col.get(x['repo']) and v5col[x['repo']][2] != ('the corpus’s own' if x['corpus'] else
                   (('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else 'no tag'))]),
              len([x for x in ptab if x['rule']]), sum_rule, len(residue), interfaces['excluded'])]
    put_txt('b638_census.txt', L)
    put_json('b638_census.json', dict(at=utc(), pre_pp=PRE_PP, relay=head, roots=CS.root_list(), lsr=dict(CS.LSR), changed=changed,
                                      J=[dict(n=row['n'], label=row['label'], heading=row['heading'], cells6=row['cells6'], kernel_src=sorted(row['kernel_src']),
                                              reg_lines=[x['line'] for x in row['rows']], has_keystone=row['has_keystone']) for row in J],
                                      prov=prov, column=column, v5col=v5col, faces=faces, phase2=P2, intake=intake, ptab=ptab, interfaces=interfaces,
                                      unnamed=sorted('%s|%s' % k for k in unnamed), by_class={c: len(v) for c, v in byclass.items()},
                                      residue=residue, met=met, sum_rule=sum_rule, sum_elab=sum_elab))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE EDITION
BM3_TAG = R3.BM3_TAG
BM5_TAG = R3.BM5_TAG
BM6_TAG = '<!-- b638 (R248) THE v0.6 EDITION’S BACK MATTER, 2026-10-07 -->'
OPEN_HEAD = '## What this document is about'
OPENING = [
    OPEN_HEAD, '',
    'This is the census of the papers of A PLACE TO STAND, a research programme whose central result, checked by the Lean 4 system, is a '
    'reduction of the Riemann Hypothesis (RH) to one open statement, the located clause: RH holds exactly when a quadratic form built from the '
    'explicit formula of prime number theory is non-negative on every admissible test window. That statement, h2_sign, is stated in the '
    'programme’s kernel, compiled as equivalent to RH by the theorem h2_sign_iff_rh, and carried as the one open premise; nothing in this '
    'document says that RH or h2_sign holds.', '',
    'The census lists the programme’s papers as its registry, REGISTRY, files them, one row for each phase and cluster of papers. For each row '
    'it names the papers, the ones read as keystones (the papers that carry the programme’s results to a reader outside it, read at Tier K, KC '
    'or C), whether each was written again by the form of an edition, the rows of the sieve the cluster holds, the kernels the papers cite (each '
    'kernel a Lean 4 repository whose name begins SIDE-) with each kernel’s current tag, the deposit state, and how many of those kernels’ '
    'compiled theorems carry a grade and where the grade comes from.', '',
    'A grade reads what a theorem’s statement assumes, not how Lean checks it: DERIVES when the statement establishes the claim from the '
    'objects it names, INTERFACES when it takes the claim as a named hypothesis discharged elsewhere, ENCODES-CONCLUSION when it stipulates what '
    'is claimed. The shared rule E0 reads the grades by classing every binder of a statement by its kind, its typing and its form; the back '
    'matter names the classes and the named premises the INTERFACES rows rest on. The glossary below defines every internal name this '
    'document uses; the sections after it keep the wording of the census’s earlier editions, each change recorded in the back matter.']
H39 = ('*(read 2026-10-06, b633; relay `data/b633_census.txt`)*', '*(read 2026-10-07, b638; relay `data/b638_census.txt`)*')
INTRO41 = ('Each cell is read at PLACE-papers e67c43b or at the remote', 'Each cell is read at PLACE-papers 5c4247b or at the remote')
HEAD45 = ('kernels’ table rows: cell / rule / none |', 'kernels’ table rows: cell / rule / rule-elab / none (upstream apart) |')
S1A_H = ('*(read 2026-10-06, b633, under `(R243)`(6)(i); relay `data/b633_census.txt`, Part C)*',
         '*(read 2026-10-07, b638, the tags re-read under `(R248)`(5); relay `data/b638_census.txt`, Part C)*')
S1A_I = (('its repository list at PLACE-papers e67c43b, the list b632’s root was taken over', 'its repository list at PLACE-papers 5c4247b, the list b637’s root was taken over'),
         ('and its rows in the terminal table by provenance.', 'and its rows in the terminal table by provenance, the upstream rows apart.'))
S1A_HEAD = ('| table rows: cell / rule / none |', '| table rows: cell / rule / rule-elab / none (upstream apart) |')
S1B_H = ('*(under `(R243)`(6)(ii); relay `data/b633_census.txt`, Part D)*', '*(under `(R243)`(6)(ii), read again at v0.6 under `(R248)`(5); relay `data/b638_census.txt`, Part D)*')
S1C_H = ('*(under `(R243)`(6)(iv); relay `data/b633_census.txt`, Part F)*',
         '*(under `(R243)`(6)(iv); read again by b636 under `(R246)`(4), its four rows unchanged and no trigger; relay `data/b636_phase2_read.txt`)*')
TAGS_OLD = ('2 kernels carry 3 tags their remotes do not (relay `data/b633_census.txt`, Part C) -- of W-ORD-TAG-REMOTES’ nine (OPEN_TRAILS :12597), '
            'the tags b623 pushed now read at their remotes, and each tag still local is named unpushed in its kernel’s cell in §1;')


def _version6(CJ):
    return ('*v0.6, 2026-10-07 -- the census under the reader’s clause: a plain opening for a reader outside the programme and the shared glossary '
            'block at its head; the kernel column with the tags re-read; the provenance column under the upstream exclusion, cell / rule / rule-elab / '
            'none with the upstream rows counted apart; the faces through v0.25 and the Phase 2 rows as b636 read them again; in back matter the '
            'premise table at %d heads over %d rows with its unnamed residue, MET beside it, and the binder grammar the grades rest on; v0.5 stands '
            'beside it, unedited.*' % (len([x for x in CJ['ptab'] if x['rule']]), CJ['sum_rule']))


def _prov43(CJ):
    return ('The last column, ruled at v0.5 (`(R243)`(6)(iii)) and read at v0.6 under the upstream exclusion (`(R247)`(2), `(R248)`(5)), counts the '
            'terminal table’s rows of the kernels the row names by provenance -- cell (a ledger cell grades it), rule (the shared E0 rule reads its '
            'statement), rule-elab (the rule reads the declaration’s elaborated type where the textual reading differs or defers) and none '
            '(ungraded) -- in the table at relay %s, the upstream rows (a declaration outside every kernel, its grade cell —) counted apart in '
            'parentheses; a kernel named in several rows is counted in each, so the column reads how much of each cluster’s compiled surface is '
            'ledger-graded, rule-graded or ungraded.' % CJ['relay'])


def _tags_new(CJ):
    un = [(x['repo'], x['local_only']) for x in CJ['column'] if x['local_only']]
    return ('%d kernels carry %d tags their remotes do not (relay `data/b638_census.txt`, Part C) -- of W-ORD-TAG-REMOTES’ nine (OPEN_TRAILS :12597), '
            'the tags b623 pushed now read at their remotes, and each tag still local is named unpushed in its kernel’s cell in §1;' % (
                len(un), sum(len(t) for _r, t in un)))


def _cellx(s):
    return s.replace('|', '¦')


def _col_line(x):
    cur = 'the corpus’s own' if x['corpus'] else (('%s = %s' % (x['current'], (x['peel'] or '')[:7])) if x['current'] else 'no tag')
    un = ', '.join('%s = %s' % tuple(t) for t in x['local_only']) or '—'
    return '| %s | %s / %s | %s | %s | %s | %s |' % (x['repo'], (x['local_main'] or '')[:7], (x['remote_main'] or '')[:7], cur, un,
                                                   ', '.join(x['rows']) or '—', _prov_cell(x['table']))


def _face_line(f):
    decl = '; '.join('`%s` %s (%s)' % (i['name'].split('SIDEExplicitFormula.', 1)[-1], i['grade'], i['provenance']) for i in f['items'])
    prem = '; '.join('`%s` on %s' % (i['name'].split('.')[-1], ', '.join(i['premises'])) for i in f['items'] if i['premises']) or '—'
    if f['id'] == 'F2':
        decl += ('; its field `two_thirds` cites `Zeta23.thmB₀_mult` at anthropics/formal-math 3635e748, its axioms read from that '
                 'repository’s AUDIT.md :80, discharged at its source kernel and not in this one')
        em = next((r for r in _table() if r['name'] == 'SIDEExplicitFormula.Simplicity.exceptional_mass_le_third'), {})
        prem = '`exceptional_mass_le_third` on hP : SimpleProportion (%s, %s)' % (em.get('grade'), em.get('provenance'))
    return '| %s %s | %s = %s | `%s` | %s | %s |' % (f['id'], f['label'], f['tag'], f['commit'], f['path'], _cellx(decl), _cellx(prem))


def _edition(CJ, cur, gl):
    """### v0.6 from v0.5's lines by transforms; RETURN (lines, where, kinds, ins, pos)."""
    def at(prefix, start=1):
        return next(i for i, l in enumerate(cur, 1) if i >= start and l.startswith(prefix))
    i10 = at('*v0.5, 2026-10-06')
    i39 = at('## §1 — THE PHASES AND CLUSTERS')
    i41 = at('One row per phase and cluster as REGISTRY lists them')
    i43 = at('The last column, ruled at v0.5')
    i45 = at('| row | phase and cluster |')
    rows_at = [i for i, l in enumerate(cur, 1) if re.match(r'^\| R\d\d \| ', l) and i45 < i < i45 + 30]
    i71 = at('## §1A — THE KERNEL COLUMN AT THE ROOT’S LIST')
    i73 = at('Every repository the act root names', i71)
    i75 = at('| repository | main, clone / remote |', i71)
    i116 = at('## §1B — THE EXPLICIT-FORMULA KERNEL’S FACES')
    col_at = [i for i, l in enumerate(cur, 1) if i75 + 1 < i < i116 and re.match(r'^\| (relay|PLACE-papers|SIDE-[\w-]+) \| ', l)]
    i118 = at('Each face at its tag', i116)
    i127 = at('## §1C — THE PHASE 2 ROWS')
    face_at = [i for i, l in enumerate(cur, 1) if i118 < i < i127 and re.match(r'^\| F\d ', l)]
    i152 = at('- **Local tags the remotes do not carry.**')
    J = dict((r['n'], r) for r in CJ['J'])
    col = dict((x['repo'], x) for x in CJ['column'])
    faces = dict((f['id'], f) for f in CJ['faces'])
    out, where, kinds, ins, pos = [], {}, {}, {}, {}

    def add(l, key=None):
        out.append(l)
        if key:
            pos[key] = len(out)
        return len(out)

    def rw(i, l, new, key, kind):
        where[i], kinds[i] = add(new, key), kind
        if new == l:
            kinds[i] = 'carried'

    for i, l in enumerate(cur, 1):
        if i == 1:
            where[i], kinds[i] = add(l), 'carried'
            add('')
            a = add(OPENING[0], 'opening')
            for x in OPENING[1:]:
                add(x)
            ins['the plain opening'] = (a, len(out))
            add('')
            a = add(gl[0], 'glossary')
            for x in gl[1:]:
                add(x)
            ins['the glossary block'] = (a, len(out))
            continue
        if i == i10:
            a = add(_version6(CJ), 'ver')
            add('')
            ins['the version line'] = (a, a)
        if i == i39:
            rw(i, l, l.replace(H39[0], H39[1]), 'h39', 'rewritten (fact)')
        elif i == i41:
            rw(i, l, l.replace(INTRO41[0], INTRO41[1]), 'intro', 'rewritten (fact)')
        elif i == i43:
            rw(i, l, _prov43(CJ), 'prov43', 'rewritten (ruled)')
        elif i == i45:
            rw(i, l, l.replace(HEAD45[0], HEAD45[1]), 'h45', 'rewritten (ruled)')
        elif i in rows_at:
            n = re.match(r'^\| (R\d\d) \| ', l).group(1)
            rw(i, l, '| ' + ' | '.join(J[n]['cells6']) + ' |', n, 'row rewritten')
        elif i == i71:
            rw(i, l, l.replace(S1A_H[0], S1A_H[1]), 's1a', 'rewritten (fact)')
        elif i == i73:
            nl = l
            for o, n in S1A_I:
                nl = nl.replace(o, n)
            rw(i, l, nl, 's1a_intro', 'rewritten (fact; ruled)')
        elif i == i75:
            rw(i, l, l.replace(S1A_HEAD[0], S1A_HEAD[1]), 's1a_head', 'rewritten (ruled)')
        elif i in col_at:
            n = re.match(r'^\| (\S+) \| ', l).group(1)
            rw(i, l, _col_line(col[n]), 'col_' + n, 'row rewritten')
        elif i == i116:
            rw(i, l, l.replace(S1B_H[0], S1B_H[1]), 's1b', 'rewritten (fact)')
        elif i == i118:
            rw(i, l, re.sub(r'the table read at relay \w+\.', 'the table read at relay %s.' % CJ['relay'], l), 's1b_intro', 'rewritten (fact)')
        elif i in face_at:
            n = re.match(r'^\| (F\d) ', l).group(1)
            rw(i, l, _face_line(faces[n]), n, 'row rewritten')
        elif i == i127:
            rw(i, l, l.replace(S1C_H[0], S1C_H[1]), 's1c', 'rewritten (ruled)')
        elif i == i152:
            rw(i, l, l.replace(TAGS_OLD, _tags_new(CJ)), 'tags', 'rewritten (fact)')
        else:
            where[i], kinds[i] = add(l), 'carried'
    return out, where, kinds, ins, pos


def _bm6(CJ, cur, where, kinds, ins, pos):
    J = dict((r['n'], r) for r in CJ['J'])
    ch = collections.defaultdict(list)
    for c in CJ['changed']:
        ch[c['row']].append(c['col'])
    SRC = dict(documents='REGISTRY (PLACE-papers 5c4247b), R-1 and R-2', keystones='the class lines; R-10', editions='the editions and the trails; R-9',
               sieve='the sieve v0.6’s headings', kernels='ls-remote, once per repository; R-6', deposit='the mirror roster at relay %s' % STEPZERO,
               provenance='the terminal table at relay %s, R-19' % CJ['relay'], label='REGISTRY', n='—')
    inv = dict((w, i) for i, w in where.items())
    nheads = len([x for x in CJ['ptab'] if x['rule']])
    I_ = CJ['interfaces']
    L = ['', BM6_TAG, '',
         '## Back matter of the v0.6 edition — written 2026-10-07 by b638 under the author’s ruling `(R248)`(4)-(5), by the form of `(R187)`(5), its '
         'clauses and the precedence order, under the reader’s clause', '',
         '### The readings v0.6 adds, each the seat’s and strikeable', '',
         '- **R-19, the provenance column.** The terminal table at relay %s is read by provenance -- cell, rule, rule-elab, none -- and a row of the '
         'kind upstream (its declaration outside every kernel; `(R247)`(2), OPEN_TRAILS :13335) is counted apart, in parentheses, in §1 and §1A '
         'alike.' % CJ['relay'],
         '- **R-20, the reader’s clause.** The opening and the glossary block stand at the head, beneath the title; the class lines, the version '
         'lines and the sections after them keep the earlier editions’ wording, their internal names defined by the glossary block where it '
         'names them, and the back matter of v0.3-v0.5 carried under the history clause, unedited.',
         '- **R-21, the tags.** Every repository of the act root’s list at PLACE-papers 5c4247b is read by one `git ls-remote`, its current '
         'tag the remote’s highest by the peel, as R-13 reads it.',
         '- **R-22, the premise table.** The census’s method at b637 (relay `data/b637_premises.txt`): the rule-graded INTERFACES rows, each '
         'premise binder’s named head by the census’s reader, the rule-elab rows printed beside, the upstream rows excluded; a premise binder '
         'whose head the reader cannot name is printed in the residue in its own words.',
         '- **R-23, the faces and the Phase 2 rows.** The faces at v0.22-v0.25 are read from the table at relay %s with each premise binder the '
         'live rule reads; the Phase 2 rows stand as b636 read them again (relay `data/b636_phase2_read.txt`).' % CJ['relay'], '',
         '### The cells changed, by row and column (both wordings in relay `data/b638_census.txt`, Part B)', '',
         '| row | this edition’s line | v0.5 line | columns changed | source |', '|:--|:--|:--|:--|:--|']
    v5row = dict((re.match(r'^\| (R\d\d) \| ', cur[i - 1]).group(1), i) for i, k in kinds.items() if re.match(r'^\| R\d\d \| ', cur[i - 1])
                 and i in where and k == 'row rewritten')
    for n in sorted(J):
        cols = ch.get(n, [])
        L.append('| %s | {E:%s} | :%s | %s | %s |' % (n, n, v5row.get(n, '?'), ', '.join(cols) or '—', '; '.join(SRC[c] for c in cols) or '—'))
    L += ['', '*%d cells changed in %d rows.*' % (len(CJ['changed']), len(ch)), '',
          '### Rewrites under the clauses', '', '| line | v0.5 line | was | now | clause | the object named |', '|:--|:--|:--|:--|:--|:--|']
    rws = [('h39', H39[0], H39[1], 'fact', 'the read and its bank'), ('intro', INTRO41[0], INTRO41[1], 'fact', 'the pin read'),
           ('prov43', 'The last column, ruled at v0.5 … cell / rule / none …', 'The last column … cell / rule / rule-elab / none … the upstream rows … counted apart',
            'ruled', 'the provenance column under the exclusion, `(R248)`(5)'),
           ('h45', HEAD45[0], HEAD45[1], 'ruled', 'the provenance column'), ('s1a', S1A_H[0], S1A_H[1], 'fact', 'the tags re-read'),
           ('s1a_intro', S1A_I[0][0], S1A_I[0][1], 'fact', 'the root list read'), ('s1a_intro', S1A_I[1][0], S1A_I[1][1], 'ruled', 'the exclusion'),
           ('s1a_head', S1A_HEAD[0], S1A_HEAD[1], 'ruled', 'the provenance column'), ('s1b', S1B_H[0], S1B_H[1], 'fact', 'the faces read again'),
           ('s1c', S1C_H[0], S1C_H[1], 'ruled', 'the Phase 2 rows as b636 read them again, `(R248)`(5)'),
           ('tags', TAGS_OLD, _tags_new(CJ), 'fact', 'the tags read by ls-remote')]
    for key, was, now, clause, obj in rws:
        if was == now or key not in pos:
            continue
        L.append('| {E:%s} | :%s | “%s” | “%s” | %s | %s |' % (key, inv.get(pos[key], '?'), _cellx(was), _cellx(now), clause, obj))
    L += ['', '*The §1A rows, the §1B rows and the §1 rows are read again as rows; each is listed in the Correspondence below.*', '',
          '### Insertions ordered by the ruling', '', '| lines | what | Status |', '|:--|:--|:--|',
          '| {E:opening} | the plain opening, `(R248)`(4) | inserted |', '| {E:glossary} | the glossary block, `(R248)`(4), from relay `data/glossary.txt` | inserted |',
          '| {E:ver} | the version line, above v0.5’s | inserted |', '',
          '### The named premises the INTERFACES rows rest on, at v0.6 (`(R248)`(5)), and MET', '',
          'The census’s method, read again at the table at relay %s with the upstream rows excluded (relay `data/b638_census.txt`, Part H): each '
          'head printed with the kernels its rows sit in, the commits the table read them at, the rule-graded rows resting on it, the rule-elab '
          'rows beside, its count at v0.5 and whether a ledger names its discharge.' % CJ['relay'], '',
          '| named premise | kernels | commits read at | rule rows | rule-elab rows | v0.5 (b632 → v0.5) | a ledger naming its discharge |',
          '|:--|:--|:--|:--|:--|:--|:--|']
    for x in CJ['ptab']:
        L.append('| %s | %s | %s | %d | %d | %s | %s |' % (x['head'], ', '.join(x['kernels']) or '—', ', '.join(x['commits']) or '—', x['rule'], x['elab'],
                                                          ('%d → %d' % tuple(x['v05'][1:])) if x['v05'] else '—', ', '.join(x['discharge']) or 'none named'))
    L += ['', '*%d heads carry rule-graded rows, their rows summing to %d, a row counted once for each named premise it rests on; the rule-elab '
          'rows beside sum to %d; %d rows rest on a premise no head names. The table’s INTERFACES rows, the upstream rows excluded, number %d: '
          'rule %d, rule-elab %d, cell %d.*' % (nheads, CJ['sum_rule'], CJ['sum_elab'], len(CJ['unnamed']), I_['excluded'], I_['rule'], I_['rule_elab'],
                                               I_['cell']), '',
          '#### The residue: the premises with no nameable head', '',
          'b637 read the twenty unnamed rows by class (relay `data/b637_rerun.txt`); %d rest INTERFACES on a premise whose head the census’s reader '
          'cannot name. Each is printed with its premise binder as the rule reads it, and no name is given to it.' % len(CJ['residue']), '',
          '| id | kernel | declaration | grade (provenance) | the premise binder, as read | its class |', '|:--|:--|:--|:--|:--|:--|']
    for x in CJ['residue']:
        bs = [b for b in x['binders'] if not b['head']] or x['binders']
        L.append('| %s | %s | `%s` | %s (%s) | %s | %s |' % (x['id'], x['repo'], x['name'], x['grade'], x['provenance'],
                                                           _cellx('; '.join('`%s : %s`' % (b['name'], ' '.join(b['type'].split())) for b in bs)),
                                                           ', '.join(sorted(set(b['cls'] for b in bs)))))
    stem = [m for m in CJ['met'] if re.search(r'gap|blind', m, re.I)]   # ### a name carrying a stem the scanner bans: pointed to the bank, as v0.5 did
    L += ['', 'MET, the rule’s forward guard (OPEN_TRAILS :13221; relay `tools/e0_rule.py`), holds %d names, each read as a premise until the author '
          'rules it a restriction: %s%s.' % (len(CJ['met']), ', '.join(m for m in CJ['met'] if m not in stem),
                                            ('; and %d name whose own spelling carries a stem the scanner bans, printed in relay `data/b638_census.txt`, '
                                             'Part I' % len(stem)) if stem else ''), '',
          '### The binder grammar the grades rest on', '',
          'Every grade in this census’s provenance column that reads rule or rule-elab rests on the binder grammar of b637 (`(R247)`(4); relay '
          '`data/b637_binder_classes.txt` and the docstring of relay `tools/e0_rule.py`): every binder of a statement -- the header’s groups, the '
          'conclusion’s leading telescope, the antecedents of its implication and the binders of an existential in it -- is classed by its kind, '
          'its typing (a Prop or data) and its form, the grade following the classes’ outcomes, a binder’s name no part of its reading and a binder '
          'reaching no class raised as a bug. The classes number %d:' % len(R7.CLASSES), '',
          '| class | kind | typing | form | outcome |', '|:--|:--|:--|:--|:--|']
    L += ['| %s | %s | %s | %s | %s |' % (c[0], c[1], c[2], _cellx(c[3].replace('`', '’')), c[4]) for c in R7.CLASSES]
    L += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.6 | `%s` | written at b638 |' % K.CEN6, '| v0.5 | `%s` | unedited |' % K.CEN5, '| v0.4 | `%s` | unedited |' % K.CEN4,
          '| v0.3 | `phase2/method/THE_KEYSTONE_CENSUS_v0_3.md` | unedited |',
          '| the current version (v0.1 with its v0.2 section) | `phase2/method/THE_KEYSTONE_CENSUS.md` | unedited |',
          '| the census bank | relay `data/b638_census.txt` | banked before this edition |',
          '| the glossary | relay `data/glossary.txt` | read, printed by relay `tools/chain_page.py` |',
          '| the registry read | `REGISTRY.md` (read at PLACE-papers 5c4247b) | read, unedited |',
          '| the sieve read | `%s` | read, unedited |' % K.SIEVE6,
          '| the terminal table | relay `data/terminal_table.json` @ %s | read |' % CJ['relay'],
          '| the binder classes | relay `data/b637_binder_classes.txt` | read |',
          '| the structure fields | relay `data/b638_structure_fields.txt` | read |',
          '| the Phase 2 rows read again | relay `data/b636_phase2_read.txt` | read |',
          '| the intake summary | relay `data/b628_intake_summary.txt`, `data/b628_intake_summary.json` | read by digest |',
          '', '### Correspondence', '', '| row | this edition’s line | phase and cluster | REGISTRY rows (lines) | keystone | Status |', '|:--|:--|:--|:--|:--|:--|']
    for n in sorted(J):
        r = J[n]
        L.append('| %s | {E:%s} | %s | %s | %s | read again |' % (n, n, _cellx(r['label']), ', '.join(':%d' % x for x in r['reg_lines']),
                                                                 'yes' if r['has_keystone'] else 'none'))
    for f in CJ['faces']:
        L.append('| %s | {E:%s} | %s, SIDE-explicit-formula %s = %s | — | — | read again |' % (f['id'], f['id'], f['label'], f['tag'], f['commit']))
    L += ['', '### Version history', '',
          '- **v0.6, 2026-10-07 (b638, `(R248)`(4)-(5))**: the census under the reader’s clause -- the plain opening and the glossary block; %d cells '
          'changed in %d rows; the kernel column with the tags re-read at the root’s %d repositories; the provenance column under the upstream '
          'exclusion; the faces through v0.25; the Phase 2 rows as b636 read them again; the premise table at %d heads over %d rows with its '
          'residue of %d, MET beside it; the binder grammar’s %d classes. v0.5 stands beside it, unedited.' % (
              len(CJ['changed']), len(ch), len(CJ['roots']), nheads, CJ['sum_rule'], len(CJ['residue']), len(R7.CLASSES)),
          '- **v0.5, 2026-10-06 (b633)**, **v0.4, 2026-10-04 (b619)**, **v0.3, 2026-10-03 (b610)**, **v0.2, 2026-09-28 (b553)** and **v0.1, 2026-08-12**: '
          'carried above.']
    return L


def _edpath():
    return os.path.join(SP, 'b638_census_dry.md') if DRY else os.path.join(PP, *K.CEN6.split('/'))


def _ed():
    return lines_of(open(_edpath(), encoding='utf-8').read().replace(chr(13), ''))


def _count(ls):
    return sum(len(R3.R4._segs(l)) for l in ls)


def edition(*a):
    """### PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_6.md beside v0.5 (unedited), and data/b638_edition.json. `dry`: the scratchpad.
    ### The re-pin step is last: the {E:n} tokens resolved against the final file."""
    CJ = jl('b638_census.json')
    if not CJ:
        sys.exit('### NO CENSUS BANK -- NOTHING WRITTEN')
    CP = _cp()
    gl = CP.glossary_block(_glossary_path())
    cur = lines_of(K.show(K.CEN5))
    out, where, kinds, ins, pos = _edition(CJ, cur, gl)
    bm = _bm6(CJ, cur, where, kinds, ins, pos)
    lines = out + bm
    for k2, (a_, b_) in ins.items():
        pos.setdefault(k2, a_)
    unres = [m.group(1) for l in lines for m in re.finditer(r'\{E:(\w+)\}', l) if m.group(1) not in pos]
    if unres:
        sys.exit('### UNRESOLVED TOKENS %s -- NOTHING WRITTEN' % sorted(set(unres)))
    lines = [re.sub(r'\{E:(\w+)\}', lambda m: ':%d' % pos[m.group(1)], l) for l in lines]
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = _edpath()
    if not DRY and os.path.exists(dest):
        sys.exit('### v0.6 EXISTS -- NOTHING WRITTEN')
    _write(dest, b)
    v3bm = lines.index(BM3_TAG) + 1
    bm6 = lines.index(BM6_TAG) + 1
    seg_d = [dict(line=i, at=where[i], d=len(R3.R4._segs(lines[where[i] - 1])) - len(R3.R4._segs(cur[i - 1])), kind=k)
             for i, k in kinds.items() if k != 'carried']
    ins_lines = [l for k2, (a_, b_) in ins.items() if k2 != 'the version line' for l in lines[a_ - 1:b_]]
    J2 = dict(at=utc(), path=K.CEN6, sha256=sha(b), bytes=len(b), lines=len(lines), body_end=v3bm - 1, v3bm=v3bm, bm=bm6, pos=pos,
              where={str(k2): v for k2, v in where.items()}, kinds={str(k2): v for k2, v in kinds.items()}, ins=ins,
              version=_count([_version6(CJ)]), ruled=_count(ins_lines), removals=0, seg_d=seg_d,
              n_body=_count(lines[:v3bm - 1]), n_cur_body=_count(cur[:cur.index(BM3_TAG)]), n_bm6=_count(lines[bm6 - 1:]), dry=DRY,
              glossary_sha256=sha((NL.join(gl) + NL).encode('utf-8')), glossary_lines=len(gl))
    print('  %s : %d lines, %d bytes, sha256 %s ; body %d sentences (v0.5 %d) ; ruled %d ; version %d ; rewrites` segment change %s' % (
        ('DRY ' + dest) if DRY else K.CEN6, len(lines), len(b), J2['sha256'][:16], J2['n_body'], J2['n_cur_body'], J2['ruled'], J2['version'],
        [x['d'] for x in seg_d if x['d']]))
    put_json('b638_edition.json', J2)


def termscan(*a):
    t = _scan(_edpath())
    put_txt('b638_census_termscan.txt', t.rstrip(NL).split(NL))
    print('  ' + ' ; '.join(l.strip() for l in t.split(NL) if re.search(r'live uses|VERDICT', l)))


LOCATED = 'the Riemann Hypothesis holds exactly when the explicit-formula quadratic form'


def _ceiling_hits(lines):
    """### the ceiling pattern's hits, each (line, match, excepted?): a hit in the glossary's located-clause entry is the author's ruled
    ### wording ((R248)(4)) and is printed excepted, by the name-and-title exception's reading of a ruled sentence carried verbatim."""
    out = []
    for i, l in enumerate(lines, 1):
        for m in R3.R4.CEILING.finditer(l):
            out.append((i, m.group(0), l.startswith('- **the located clause** — ' + LOCATED)))
    return out


def bank(*a):
    """### data/b638_edition_CENSUS.txt (the diff bank) and data/b638_h28.json: H28a-H28c scored."""
    E = jl('b638_edition.json')
    ed = _ed()
    cur = lines_of(K.show(K.CEN5))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### v0.6 ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b638_census_termscan.txt')
    clean = _clean(scan)
    live = re.search(r'live uses\s*: (\d+)', scan)
    body = ed[:E['body_end']]
    hits = _ceiling_hits(body)
    beyond = [x for x in hits if not x[2]]
    beyond0 = _ceiling_hits(cur[:cur.index(BM3_TAG)])
    ok, bad = 0, []
    for i, l in enumerate(cur, 1):
        if not l.strip():
            continue
        k = E['kinds'].get(str(i))
        w = E['where'].get(str(i))
        good = bool(w) and (ed[w - 1] == l if k == 'carried' else (ed[w - 1].split(' | ')[0] == l.split(' | ')[0] if k == 'row rewritten' else ed[w - 1] != l))
        ok += good
        if not good:
            bad.append(i)
    segc = sum(abs(x['d']) for x in E['seg_d'])
    allowed = E['removals'] + E['ruled'] + E['version'] + segc
    dn = E['n_body'] - E['n_cur_body']
    h28a = 'HOLDS, VACUOUSLY'
    h28b = 'HOLDS' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and len(beyond) <= len(beyond0) else 'REFUTED'
    kh = R3.keystone_hits(NL.join(ed))
    L = ['b638 -- COMPONENT 5: THE DIFF BANK OF THE_KEYSTONE_CENSUS v0.6 against v0.5 at %s; the final file sha256 %s (%d lines, %d bytes)' % (
        PRE_PP, E['sha256'], E['lines'], E['bytes']), '',
         '### THE COUNTS, SEPARATELY: the body v0.5 %d sentences, v0.6 %d (%+d); removals 0; the ruled insertions %d (the opening and the glossary '
         'block); the version line %d; the rewrites` segment change %d; v0.6`s own back matter %d' % (E['n_cur_body'], E['n_body'], dn, E['ruled'],
                                                                                                   E['version'], segc, E['n_bm6']), '',
         '### EVERY v0.5 LINE THAT MOVED IN MEANING, BOTH WORDINGS (every other line carried verbatim at its mapped line):']
    for i, l in enumerate(cur, 1):
        k = E['kinds'].get(str(i), 'carried')
        if k == 'carried':
            continue
        w = E['where'].get(str(i))
        L += ['  v0.5 :%d -> :%s %s' % (i, w, k), '      was: %s' % l[:2400], '      now: %s' % ed[w - 1][:2600]]
    L += ['### THE INSERTIONS: %s' % E['ins'],
          '### CARRIED: %d of %d non-blank v0.5 lines found at their mapped line, verbatim or as their recorded rewrite (failing %s)' % (
              ok, sum(1 for l in cur if l.strip()), bad or 'none'),
          '### THE SCANNER: %s, live %s ; the ceiling pattern in the body: %d hits, %d excepted as the author`s ruled wording (%s), %d beyond (v0.5`s body %d)' % (
              'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(hits), len(hits) - len(beyond),
              ['%d %s' % (x[0], x[1]) for x in hits if x[2]], len(beyond), len(beyond0)),
          '### THE PAGE NODES THE EDITION NAMES (the generator`s keystone pattern): %s' % kh, '',
          '### ### **H28a %s** -- the census has no work-list, so no MOVED-IN-MEANING sentence; beside it, every changed cell names its source (the '
          'census bank`s Part B) and every rewrite its clause (the back matter)' % h28a,
          '### ### **H28b %s** -- the body %+d against at most %d (removals 0 + ruled %d + version %d + the rewrites` segment change %d)' % (
              h28b, dn, allowed, E['ruled'], E['version'], segc),
          '### ### **H28c %s** -- the scanner %s, %s live stems by its count; the ceiling pattern in the body %d beyond the excepted against v0.5`s %d' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(beyond), len(beyond0)),
          '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' if not bad else '### ### **HELD AT %s.**' % bad]
    put_txt('b638_edition_CENSUS.txt', L)
    put_json('b638_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, body_dn=dn, allowed=allowed, clean=clean, live=int(live.group(1)) if live else None,
                                   beyond=len(beyond), beyond0=len(beyond0), excepted=[list(x) for x in hits if x[2]], carried_ok=ok, carried_bad=bad,
                                   vacuous_a=True, keystone_hits=kh))
    for l in L[-5:]:
        print(l[:260])


def repin(*a):
    E = jl('b638_edition.json')
    ed = _ed()
    L = ['b638 -- THE RE-PIN STEP (R190)(3), THE FORM`S LAST: THE_KEYSTONE_CENSUS v0.6`s own cited lines read against its final file (sha256 %s)' % E['sha256'][:16]]
    ok = n = 0
    for k2, v in sorted(E['pos'].items(), key=lambda kv: kv[1]):
        n += 1
        l = ed[v - 1] if 0 < v <= len(ed) else ''
        if re.fullmatch(r'R\d\d', k2):
            good = l.startswith('| %s | ' % k2) and v < E['body_end']
        elif re.fullmatch(r'F\d', k2):
            good = l.startswith('| %s ' % k2) and v < E['body_end']
        elif k2.startswith('col_'):
            good = l.startswith('| %s | ' % k2[4:]) and v < E['body_end']
        elif k2 == 'ver':
            good = l.startswith('*v0.6, 2026-10-07 -- the census under the reader’s clause')
        elif k2 in ('opening', 'the plain opening'):
            good = l == OPEN_HEAD
        elif k2 in ('glossary', 'the glossary block'):
            good = l == '## Glossary'
        elif k2 == 'the version line':
            good = l.startswith('*v0.6, ')
        elif k2 == 'prov43':
            good = l.startswith('The last column, ruled at v0.5') and 'rule-elab' in l
        elif k2 in ('s1a', 's1b', 's1c'):
            good = l.startswith('## §1%s — ' % k2[-1].upper())
        elif k2 == 'h39':
            good = H39[1] in l
        elif k2 == 'intro':
            good = INTRO41[1] in l
        elif k2 in ('h45', 's1a_head'):
            good = 'rule-elab / none (upstream apart) |' in l
        elif k2 == 's1a_intro':
            good = S1A_I[0][1] in l
        elif k2 == 's1b_intro':
            good = l.startswith('Each face at its tag')
        elif k2 == 'tags':
            good = l.startswith('- **Local tags the remotes do not carry.**') and 'b638_census' in l
        else:
            good = bool(l.strip())
        ok += good
        L.append('  {E:%s} -> :%d %s %s' % (k2, v, 'HOLDS' if good else '### FAILS', l[:120]))
    unres = re.findall(r'\{E:\w+\}', NL.join(ed))
    L += ['### unresolved tokens: %s' % (unres or 'none'), '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (ok, n)]
    put_txt('b638_repin.txt', L)
    put_json('b638_repin.json', dict(at=utc(), held=ok, of=n, unresolved=unres))
    print(L[-1])


NAME_PATS = (r'`[^`]+`', r'\b[A-Z][A-Z0-9]*(?:[-_][A-Z0-9]+)+\b|\b[A-Z][A-Z0-9]+\b', r'\b[a-z][a-z0-9]*_[a-z0-9_]+\b', r'\bSIDE-[\w-]*',
             r'\bb\d{3}\b', r'\(R\d+\)', r'\bTier [A-Z]+\b')


def opening_scan(text=None, keys=None):
    """### H72d: the opening's internal names -- backticked spans, upper-case tokens, snake_case identifiers, SIDE- names, act numbers,
    ### rulings, tiers -- each found inside a glossary key; and every key the opening carries defined by its line in the same document's
    ### glossary block. RETURN (names, undefined, keys used, keys without their line)."""
    ls = (text if text is not None else NL.join(_ed())).split(NL)
    if OPEN_HEAD not in ls or '## Glossary' not in ls:
        return [], ['### NO OPENING OR NO GLOSSARY'], [], []
    op = NL.join(ls[ls.index(OPEN_HEAD) + 1:ls.index('## Glossary')])
    gl = glossary_lines(NL.join(ls))
    keys = keys if keys is not None else [k for k, _d, _s in _cp().glossary_entries(_glossary_path())]
    names = sorted(set(m.group(0).strip('`') for p in NAME_PATS for m in re.finditer(p, op)))
    undefined = [n for n in names if not any(n in k or k in n and len(k) > 1 for k in keys)]
    used = [k for k in keys if re.search(r'(?<![\w-])' + re.escape(k) + r'(?![\w-])', op)]
    noline = [k for k in used if not any(l.startswith('- **%s** — ' % k) for l in gl)]
    return names, undefined, used, noline


def opening(*a):
    """### H72d's scan of the census's opening against the glossary's keys, banked as data/b638_opening.txt and its json."""
    names, undefined, used, noline = opening_scan()
    L = ['b638 -- COMPONENT 5, H72d: THE CENSUS`S OPENING SCANNED AGAINST THE GLOSSARY`S KEYS (%s)' % utc(), '',
         '### the internal names the opening carries (%d): %s' % (len(names), names),
         '### each found inside a glossary key: undefined %s' % (undefined or 'NONE'),
         '### the glossary keys the opening carries (%d): %s' % (len(used), used),
         '### each defined by its line in the same document`s glossary block: without its line %s' % (noline or 'NONE'), '',
         '### ### **NAMES %d ; UNDEFINED %d ; KEYS USED %d ; KEYS WITHOUT THEIR LINE %d.**' % (len(names), len(undefined), len(used), len(noline))]
    put_txt('b638_opening.txt', L)
    put_json('b638_opening.json', dict(at=utc(), names=names, undefined=undefined, used=used, noline=noline))
    print(L[-1])


def actroot_test(*a):
    """### Component 5's last step: tools/act_root.py's census path at v0.6 through the Edit tool, its test re-pointed; the diffs against
    ### relay 2aa41700 and the test run and counted (data/b638_actroot_diff.txt, data/b638_actroot_test.txt)."""
    _diff('tools/act_root.py', PRE_RELAY, 'b638_actroot_diff.txt', 'THE ACT ROOT`S CENSUS PATH AT v0.6, (R248)(5)')
    _diff('tools/test_act_root.py', PRE_RELAY, 'b638_actroot_test_diff.txt', 'ITS TEST, CASE (9) AT v0.6')
    _run_test('tools/test_act_root.py', 'b638_actroot_test')


# ================================================================================ THE TABLE AT THE END
def table(*a):
    """### the terminal table regenerated; every row whose grade, provenance, mark or kind moved printed (data/b638_table_<tag>.txt, json)."""
    rows0 = _table()
    before = R7._table_state(rows0)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    rows1 = _table()
    after = R7._table_state(rows1)
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    tag = a[0] if a and a[0] != 'dry' else 'final'
    files = [f for f in K.TABLE_FILES if g(RELAY, 'diff', '--name-only', '--', 'data/' + f).strip()]
    L = ['b638 -- THE TERMINAL TABLE REGENERATED, %s (%s); exit %d' % (tag, utc(), r.returncode), '',
         '### rows %d ; added %d ; gone %d ; grade, provenance, mark or kind moved %d ; the table files that moved against relay HEAD: %s' % (
             len(rows1), len(added), len(gone), len(moved), files or 'NONE'),
         '### provenance under the exclusion: %s' % _prov_counts(rows1), '### EVERY MOVE:']
    L += ['  MOVED %s / %-62s %s -> %s' % (k[0], k[1], before[k], after[k]) for k in moved]
    L += ['  ADDED %s / %s %s' % (k[0], k[1], after[k]) for k in added] + ['  GONE  %s / %s %s' % (k[0], k[1], before[k]) for k in gone]
    L += ['', '### ### **ROWS MOVED %d ; ADDED %d ; GONE %d ; GRADE MOVED %d.**' % (len(moved), len(added), len(gone),
                                                                               sum(1 for k in moved if before[k][0] != after[k][0]))]
    if r.returncode:
        L += ['### THE GENERATOR EXITED %d:' % r.returncode] + (r.stdout + r.stderr).rstrip(NL).split(NL)[-15:]
    put_txt('b638_table_%s.txt' % tag, L)
    put_json('b638_table_%s.json' % tag, dict(at=utc(), rc=r.returncode, moved=[[k[0], k[1], list(before[k]), list(after[k])] for k in moved],
                                              added=[list(k) for k in added], gone=[list(k) for k in gone], files_moved=files,
                                              grade_moved=[list(k) for k in moved if before[k][0] != after[k][0]], prov=_prov_counts(rows1)))
    print(L[2])
    print(L[-1])


# ================================================================================ COMPONENT 6: THE ROOT
ROOT_EXCLUDE = re.compile(r'^b638_(defects|scores|desk_notes|components|checks.*|lsr.*|exercise|findings|trail|correction|closing.*|'
                          r'act_root.*|root_arm.*|.*push_out.*|census_closing|faces_census_closing|pins_closing|scanfile_.*|seal_check_.*|mirror.*)\.(txt|json|md)$')


def root_banks():
    return sorted('data/' + f for f in os.listdir(D) if f.startswith('b638_') and os.path.isfile(os.path.join(D, f)) and not ROOT_EXCLUDE.match(f))


def root(*a):
    banks = root_banks() + [K.GLOSSARY]
    print('  banks named: %d' % len(banks))
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'act_root.py'), 'compute', 'b638'] + banks + ([] if DRY else ['--write']),
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout or '') + (r.stderr or '')
    print(NL.join(out.rstrip(NL).split(NL)[-4:]))
    if r.returncode:
        sys.exit('### act_root.py exit %d' % r.returncode)


def root_arm(*a):
    """### the one-byte control, offline; the chain's verify is read inside the suite alone."""
    import shutil
    import act_root as AR
    J = jl('b638_act_root.json')
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
    L = ['b638 -- THE ACT-ROOT ARM`S OFFLINE CONTROL (%s); the chain`s verify is read inside the suite alone' % utc(), '',
         '### the one-byte control: a copy of %s with its first byte changed; the root over the copy %s ; over the bank %s (banked %s)' % (
             bank_, r2, same, J['root']), '',
         '### ### **THE RECOMPUTED ROOT EQUALS THE TOOL`S %s ; THE ONE-BYTE CONTROL CHANGES IT %s.**' % (same == J['root'], r2 != J['root'])]
    put_txt('b638_root_arm.txt', L)
    put_json('b638_root_arm.json', dict(at=utc(), bank=bank_, root_copy=r2, root_recomputed=same, root=J['root']))
    print(L[-1])


# ================================================================================ THE SCORES
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'README.md', K.CEN4, K.CEN5, K.MONO, K.SIEVE6)
HKEYS = ('H72a', 'H72b', 'H72c', 'H72d', 'H28a', 'H28b', 'H28c')
NK = ('N1', 'N2', 'N3', 'N4', 'N5')
SK = ('S1', 'S2', 'S3', 'S4', 'S5')
SCORE_KEYS = HKEYS + NK + SK
N5_ALLOWED = {'data/b637_closing_push_out.txt', 'data/act_roots.txt', K.GLOSSARY, 'tools/chain_page.py', 'tools/test_chain_page_b638.py',
              'tools/act_root.py', 'tools/test_act_root.py', 'tools/mirror_prevbuild.json'}
N5_PP = ('FINDINGS.md', 'OPEN_TRAILS.md', K.PAGE, K.DIR_PAGE, K.CEN6)


def n5(trail_line=None, ot=None, *a):
    """### (R248)'s N5, the file-set by PATH; no sealed tool's hash differs; the kernels untouched; nothing deposits."""
    if isinstance(trail_line, str):
        trail_line = int(trail_line.split('=')[-1])
    ot_text = ot if ot is not None else io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ot_lines = lines_of(ot_text)
    if trail_line is None:
        rec_ok, rec_state = False, 'no expected line given'
    elif len(ot_lines) >= trail_line and ot_lines[trail_line - 1] == TRAIL_HEAD:
        rec_ok, rec_state = True, 'the trail record written at :%d' % trail_line
    elif TRAIL_HEAD not in ot_text and len(ot_lines) < trail_line:
        rec_ok, rec_state = True, 'the trail record pending at :%d (the trails end at :%d)' % (trail_line, len(ot_lines))
    else:
        rec_ok, rec_state = False, 'the trail record neither at :%s nor pending' % trail_line
    face = jl('b638_kernels_face.json').get('kernels') or {}
    now = kern_state(list(face))
    kern_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in N5_PP]
    relay_ch = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL) if x.strip()))
    beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b638_|audit_b638_)', x) or re.match(r'^data/terminal_table', x) or x in N5_ALLOWED)]
    tracked_local = bool(g(RELAY, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK).strip())
    untracked_local = g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip().startswith('??')
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    rule_touched = [x for x in relay_ch if x in ('tools/e0_rule.py', 'tools/test_e0_rule.py')]
    ok = kern_ok and not pp_beyond and not beyond and rec_ok and not tracked_local and untracked_local and not differ and not rule_touched
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; every kernel`s tracked tree unmoved against the face %s; PLACE-papers %s (beyond the ledgers, the pages and the census '
            'at v0.6: %s); %s; relay beyond the list, matched by path: %s; the rule untouched (its edit not needed by (2)) %s; the sealed tools` '
            'hashes not agreeing %s; b628`s local intake bank in any relay commit %s, untracked now %s; no identifier of the author in any outbound '
            'request' % (kern_ok, pp_ch, pp_beyond or 'NONE', rec_state, beyond or 'NONE', not rule_touched, differ or 'NONE', tracked_local, untracked_local))


def _vac(ok, n, word):
    return ('%s, VACUOUSLY' % word) if (ok and n == 0) else word


def _page_text(k):
    return R2.cr0(subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + K.PNAME[k]], capture_output=True).stdout).decode('utf-8', 'replace')


def h72():
    """### H72a-H72d recomputed from the documents and the banks: RETURN {key: (verdict, why)}."""
    CJ, F = jl('b638_census.json'), jl('b638_structure_fields.json')
    ed = _ed() if os.path.exists(_edpath()) else []
    ged = glossary_lines(NL.join(ed))
    gz, gx = glossary_lines(_page_text('zeta')), glossary_lines(_page_text('chi'))
    a_ok = bool(ged) and ged == gz == gx
    I_ = CJ.get('interfaces') or {}
    total = CJ.get('sum_rule', 0) + CJ.get('sum_elab', 0)
    b_ok = bool(CJ) and total == I_.get('excluded')
    cur = lines_of(K.show(K.CEN5))
    cls5 = [l for l in cur if l.startswith('**DOCUMENT CLASS')]
    cls6 = [l for l in ed if l.startswith('**DOCUMENT CLASS')]
    tier_sentence = 'the census’s tier stands at C' in NL.join(ed)
    c_ok = bool(ed) and cls5 == cls6 and all('TIER C' in l for l in cls6) and tier_sentence
    names, undefined, used, noline = opening_scan(NL.join(ed)) if ed else ([], ['### NO EDITION'], [], [])
    d_ok = bool(names) and not undefined and not noline
    return {
        'H72a': (('HOLDS' if a_ok else 'REFUTED'), 'the glossary block: the census at v0.6 %d lines, the ζ page at PLACE-papers HEAD %d, the χ page %d; byte for '
                 'byte alike %s' % (len(ged), len(gz), len(gx), a_ok)),
        'H72b': (('HOLDS' if b_ok else 'REFUTED'), 'the premise table`s row counts summed %d (rule %d + rule-elab %d) against the table`s INTERFACES rows %s, the '
                 'upstream rows excluded (rule-graded %s, rule-elab %s, cell %s); the rule rows alone %d against the rule-graded %s; %d rows on a premise no '
                 'head names; after (2)`s ruling, no row reverting (data/b638_census.txt, Part H)' % (
                     total, CJ.get('sum_rule', 0), CJ.get('sum_elab', 0), I_.get('excluded'), I_.get('rule'), I_.get('rule_elab'), I_.get('cell'),
                     CJ.get('sum_rule', 0), I_.get('rule'), len(CJ.get('unnamed') or []))),
        'H72c': (('HOLDS' if c_ok else 'REFUTED'), 'the class lines at v0.6 equal v0.5`s %s and read TIER C %s; §1C`s sentence, the tier standing at C, carried %s; '
                 'the tier unchanged from v0.5' % (cls5 == cls6, all('TIER C' in l for l in cls6) and bool(cls6), tier_sentence)),
        'H72d': (('HOLDS' if d_ok else 'REFUTED'), 'the opening`s internal names %d, each inside a glossary key (undefined %s); the keys it carries %d, each '
                 'defined by its line in the same document (without %s)' % (len(names), undefined or 'none', len(used), noline or 'none')),
    }


def scores(*a):
    H28, GT, TF, RA, GJ, F = (jl(n_) for n_ in ('b638_h28.json', 'b638_gen_test.json', 'b638_table_final.json', 'b638_root_arm.json',
                                               'b638_glossary.json', 'b638_structure_fields.json'))
    tl = [x for x in a if x.startswith('trail_line=')]
    n5v = n5(int(tl[0].split('=')[1]) if tl else None)
    S = h72()
    g036 = jl('b638_g036_line.json')
    n3_ok = bool(F) and ((F.get('pwsetup_all_prop') and F.get('pwsetup_moves') == 51 and bool(g036.get('lines'))) or
                         (not F.get('pwsetup_all_prop') and F.get('reverting', 0) >= 51))
    _r, _n, sh = seal_hashes()
    bld = g(RELAY, 'diff', '--name-only', PRE_RELAY, '--', K.BUILDER).strip() + g(RELAY, 'diff', '--name-only', '--', K.BUILDER).strip()
    S.update({
        'H28a': (H28.get('H28a', 'PENDING'), 'the census has no work-list (data/b638_edition_CENSUS.txt)'),
        'H28b': (H28.get('H28b', 'PENDING'), 'the body %s against at most %s' % (H28.get('body_dn'), H28.get('allowed'))),
        'H28c': (H28.get('H28c', 'PENDING'), 'the scanner clean %s, live %s; the ceiling pattern beyond the excepted %s against v0.5`s %s, excepted %s' % (
            H28.get('clean'), H28.get('live'), H28.get('beyond'), H28.get('beyond0'), H28.get('excepted'))),
        'N1': (('HELD' if S['H72a'][0] == 'HOLDS' else 'REFUTED'), 'as H72a'),
        'N2': (('HELD' if S['H72b'][0] == 'HOLDS' else 'REFUTED'), 'as H72b'),
        'N3': (('HELD' if n3_ok else 'REFUTED'), 'PWSetup`s %s fields %s; %s moves %s; the G036 note entered %s (data/b638_structure_fields.txt)' % (
            F.get('pwsetup_fields'), 'every one a Prop' if F.get('pwsetup_all_prop') else 'a data field among them', F.get('pwsetup_moves'),
            'standing' if F.get('pwsetup_all_prop') else 'reverting', bool(g036.get('lines')))),
        'N4': (('HELD' if S['H72d'][0] == 'HOLDS' else 'REFUTED'), 'as H72d'),
        'N5': n5v,
        'S1': (('HELD' if GJ and GJ.get('entries') and GJ.get('alone') and GJ.get('block_lines') == GJ.get('entries') + 4 else 'REFUTED'),
               'the glossary: %s entries, each a name, a definition and a source, its block %s lines; committed alone %s' % (
                   GJ.get('entries'), GJ.get('block_lines'), bool(GJ.get('alone')))),
        'S2': (('HELD' if GT and GT.get('rc') == 0 and GT.get('passing') == GT.get('cases') and GT.get('cases', 0) >= 6 else 'REFUTED'),
               'the generator`s test %s of %s, a list without the mark emitting as before among its cases' % (GT.get('passing'), GT.get('cases'))),
        'S3': (('HELD' if TF and not TF.get('moved') and not TF.get('gone') and not TF.get('added') else 'REFUTED'),
               'the table regenerated at the end moves %s rows' % len(TF.get('moved') or [])),
        'S4': (('HELD' if RA and RA.get('root_recomputed') == RA.get('root') and RA.get('root_copy') != RA.get('root') else 'REFUTED'),
               'the root recomputed equal %s; the control changes it %s' % (RA.get('root_recomputed') == RA.get('root') if RA else None,
                                                                            RA.get('root_copy') != RA.get('root') if RA else None)),
        'S5': (('HELD' if sh and all(v == 'agree' for _t, v in sh) and not bld else 'REFUTED'),
               'the sealed tools` hashes at the record: %s; the builder unedited %s' % (dict(collections.Counter(v for _t, v in sh)), not bld)),
    })
    put_json('b638_scores.json', S)
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:300]))


# ================================================================================ COMPONENT 6: THE RECORD
TRAIL_HEAD = ('### b638 — lane three, act sixty-five under (R248): the keystone census at v0.6 under the reader’s clause, a plain opening and a '
              'shared glossary, provenance under the upstream exclusion, the premise table with its unnamed residue; the PWSetup moves held to a '
              'field print; the mirror rebuilt on the 73-file roster')


def _figures():
    CJ, F, TB = jl('b638_census.json'), jl('b638_structure_fields.json'), jl('b638_table_final.json')
    p = TB.get('prov') or _prov_counts(_table())
    return dict(CJ=CJ, F=F, c=p['cell'], r=p['rule'], e=p['rule-elab'], n=p['none'], u=p['upstream'], h=len([x for x in CJ.get('ptab') or [] if x['rule']]),
                k=CJ.get('sum_rule', 0), q=len(CJ.get('residue') or []), f=F.get('pwsetup_fields'), m=F.get('pwsetup_moves'),
                kind='all Props' if F.get('pwsetup_all_prop') else 'a data field among them', stand='standing' if F.get('pwsetup_all_prop') else 'reverting')


def _title_entry():
    f = _figures()
    return ('## The keystone census at v0.6 under the reader’s clause: a plain opening and a shared glossary, provenance %d/%d/%d/%d with %d upstream '
            'rows apart, the premise table at %d heads over %d rows with %d unnamed; PWSetup’s %s fields %s, %s moves %s' % (
                f['c'], f['r'], f['e'], f['n'], f['u'], f['h'], f['k'], f['q'], f['f'], f['kind'], f['m'], f['stand']))


def _finding_text():
    S, rl, J, GJ = jl('b638_scores.json'), jl('b638_record_lines.json'), jl('b638_act_root.json'), jl('b638_glossary.json')
    f = _figures()
    CJ, F = f['CJ'], f['F']
    E_ = jl('b638_edition.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b638_author_answers.txt'), re.M))
    t = _title_entry()
    pz, px = jl('b638_page_zeta_glossary.json'), jl('b638_page_chi_glossary.json')
    I_ = CJ.get('interfaces') or {}
    e = ['', t, '',
         '*Filed at b638 on the author’s ruling `(R248)`%s. Banks: relay `data/glossary.txt`, `data/b638_structure_fields.txt`, `data/b638_census.txt`, '
         '`data/b638_edition_CENSUS.txt`, `data/b638_opening.txt`, `data/b638_page_arms.txt`, `data/b638_act_root.txt`; the mirror’s, '
         '`data/b638_mirror.txt`, written after the act’s last push. Nothing deposits.*' % ((' and the author’s answers (%d)' % n_ans) if n_ans else ''), '',
         '**The glossary** (Components 1 and 3): relay data/glossary.txt, %s entries, each internal name the two generated pages and the census use '
         'defined in the programme’s own words with where the programme states it, the located clause spelled out as the author ruled it; the '
         'generator prints it beneath a page’s head line where the page’s list carries the mark, a list without the mark emitting as before; both '
         'pages re-emitted from b632’s lists with the mark and b635’s probes, their diffs by kind ζ %s and χ %s, the block %s lines on each. H72a %s.' % (
             GJ.get('entries'), ', '.join('%s %d' % kv for kv in sorted((pz.get('kinds') or {}).items())) or '—',
             ', '.join('%s %d' % kv for kv in sorted((px.get('kinds') or {}).items())) or '—', pz.get('glossary_lines'), (S.get('H72a') or ['?'])[0]), '',
         '**The field print** (Component 2): the %d structure types among b637’s moves printed field by field from the kernel source at the pin, '
         'each field’s kind read by the rule’s own typing; %d fields, %s. PWSetup’s %s fields are %s, so the %s rows resting on it stand at '
         'INTERFACES on a premise structure, and the second reader’s G036 reading at b632 is recorded as an uncertainty resolved against it.' % (
             len(F.get('types') or []), F.get('fields') or 0, 'every one a Prop' if F.get('all_prop') else 'a data field among them', f['f'], f['kind'],
             f['m']), '',
         '**The census at v0.6** (Components 4 and 5): phase2/method/THE_KEYSTONE_CENSUS_v0_6.md beside v0.5, unedited; a plain opening for a reader '
         'outside the programme and the glossary block at its head; %d cells changed in %d rows; the kernel column at %d repositories with the tags '
         're-read; the provenance column cell / rule / rule-elab / none with the upstream rows apart; the faces through v0.25; the Phase 2 rows as '
         'b636 read them again; in back matter the premise table at %d heads over %d rule rows (%d rule-elab beside), its residue of %d printed in '
         'their own words, MET beside, and the binder grammar’s 26 classes. The table’s INTERFACES rows number %s with the upstream rows excluded. '
         'H72b %s, H72c %s, H72d %s; H28a %s, H28b %s, H28c %s.' % (
             len(CJ.get('changed') or []), len(set(c['row'] for c in CJ.get('changed') or [])), len(CJ.get('column') or []), f['h'], f['k'],
             CJ.get('sum_elab', 0), f['q'], I_.get('excluded'), (S.get('H72b') or ['?'])[0], (S.get('H72c') or ['?'])[0], (S.get('H72d') or ['?'])[0],
             (S.get('H28a') or ['?'])[0], (S.get('H28b') or ['?'])[0], (S.get('H28c') or ['?'])[0]), '',
         '**The record lines** (`(R248)`(1), (2), (4)): b637 at its weight with the four readings confirmed (FINDINGS :%s); the reader’s clause beside '
         'the title clause (OPEN_TRAILS :%s); the G036 note (:%s).' % (
             (rl.get('lines') or [{}])[0].get('line'), (rl.get('lines') or [{}, {}])[1].get('line') if len(rl.get('lines') or []) > 1 else None,
             ((jl('b638_g036_line.json').get('lines') or [{}])[0]).get('line')), '',
         '**The root.** b638 over %d repositories, %d tags and %d banks; its chain verified inside the suite.' % (
             len((J.get('reads') or {}).get('heads') or []), len((J.get('reads') or {}).get('tags') or []), len((J.get('reads') or {}).get('banks') or [])), '',
         '**The scores.** ' + ', '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): it carries b633’s census (FINDINGS :7725) to a reader outside the programme and reads '
         'b637’s binder grammar (FINDINGS :7833) as the ground the census’s grades rest on; the glossary binds the census to the two generated pages '
         'by one source. It strengthens the programme’s offering of a census a mathematician who has read none of the corpus can follow, every '
         'internal name defined where it enters.', '',
         '**Next.** Per `(R248)`(6): b639, the deposit -- the author’s own act on the (R110) route, with the mirror rebuilt at this act’s close and '
         'the deposit bank refreshed to the census at v0.6, the seat preparing and depositing nothing; or, the deposit held, the per-cluster '
         'fact-item editions of Phase 1.2 under the reader’s clause; the author rules on the closing.', '',
         '*Nothing deposits; nothing here is a statement that RH or GRH holds or locates any zero; a rule grade reads a statement’s binders.*', '']
    return t, NL.join(e)


def _next_lines():
    return ['b639 names no kernel terminal; the deposit is the author’s own act, and the fact-item editions read the clusters they are given']


FOR_AUTHOR = ('(1) the writing law read as the form of an edition (:%d) with its title clause and the name-and-title exception (:%d), the reader’s '
              'clause appended beside them; (2) the glossary’s keys as the internal names the two pages and the census use, the act numbers and the '
              'kernel names each under one entry (bNNN; SIDE-); (3) the glossary printed beneath a page’s head line where its list carries the mark, '
              'b638’s lists b632’s with the mark; (4) a field whose head the rule’s typing reads as unlisted or unread settled by that head’s own '
              'declaration at the pin; (5) the census’s every cell re-read, the ANNEX row’s intake cell carried as v0.5 inserted it; (6) both pages '
              're-emitted again after the census by the page clause (:%d), the census at v0.6 a keystone naming their nodes; (7) the ceiling hit in '
              'the glossary’s located clause the author’s ruled wording, excepted; (8) the carried body and the earlier back matter under the history '
              'clause, their names defined by the glossary where it names them' % (K.FORM, K.NAME_TITLE, K.PAGE_CLAUSE))


def _trail_text():
    S, fj, rl, J = (jl(n_) for n_ in ('b638_scores.json', 'b638_findings.json', 'b638_record_lines.json', 'b638_act_root.json'))
    gj = jl('b638_g036_line.json')
    n_ans = len(re.findall(r'^### PROMPT ', rd('b638_author_answers.txt'), re.M))
    _r, _n, sh = seal_hashes()
    ls = (rl.get('lines') or [{}, {}])
    rows_ = ['', TRAIL_HEAD, '',
             '**(R248) ratified.** (1) b637 at its weight. (2) The PWSetup moves held to a field print. (3) The seat’s four readings confirmed. (4) '
             'The reader’s clause. (5) The keystone census at v0.6. (6) The act after: b639.', '',
             '**Entered:** FINDINGS.md:%s (b637’s weight), :%s (the entry); OPEN_TRAILS.md:%s (the reader’s clause, standing), :%s (the G036 note); '
             'this record.' % (ls[0].get('line'), fj.get('entry_line'), ls[1].get('line') if len(ls) > 1 else None, ((gj.get('lines') or [{}])[0]).get('line')), '',
             '**Act root:** b638 `%s` (previous `%s`, b637’s; relay data/act_roots.txt).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d (relay data/b638_author_answers.txt).' % n_ans, '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**The next act’s terminals** (`(R237)`(4)): %s.' % ' / '.join(_next_lines()), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**Defects** (relay data/b638_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k2, (S.get(k2) or ['?'])[0]) for k2 in SCORE_KEYS) + '.**', '',
             '**The mirror:** built after the act’s last push by the unedited builder on the %d-file roster; its digests in relay data/b638_mirror.txt, '
             'banked at the closing.' % K.ROSTER_FILES, '',
             '**Next:** per `(R248)`(6), b639 on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def desk(*a):
    S = jl('b638_scores.json')
    L = ['=' * 104, 'b638 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H72a-H72d, (R248)(5); H28a-H28c, the form.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2.upper(), S[k2][0], S[k2][1]) for k2 in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k2, S[k2][0], S[k2][1]) for k2 in SK]
    L += ['', '### ### **H : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k2][0].startswith('HOLDS') for k2 in HKEYS), sum(S[k2][0] == 'REFUTED' for k2 in HKEYS), sum(S[k2][0].startswith('HELD') for k2 in NK),
                             sum(S[k2][0] == 'REFUTED' for k2 in NK), sum(S[k2][0].startswith('HELD') for k2 in SK), sum(S[k2][0] == 'REFUTED' for k2 in SK)), '']
    L += rd('b638_defects.txt').rstrip(NL).split(NL)
    put_txt('b638_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, J = (jl(n_) for n_ in ('b638_scores.json', 'b638_findings.json', 'b638_trail.json', 'b638_record_lines.json', 'b638_act_root.json'))
    ls = rl.get('lines') or [{}, {}]
    L = ['b638 -- THE COMPONENTS, BANKED UNDER (R248).', '',
         '### COMPONENT 0 : the process listing ; b637`s closing push-out relay %s ; push-b637* deleted by name (data/b638_branches.txt) ; every test '
         'file run (data/b638_tests_stepzero.txt) ; the suite at HEAD before the face (data/b638_arms_prerun.txt) ; the sealed tools` hashes at the '
         'seal (data/b638_seal_hashes.json) ; b628`s local intake bank untracked' % STEPZERO,
         '### COMPONENT 1 : b637`s weight FINDINGS :%s ; the reader`s clause OPEN_TRAILS :%s ; the glossary relay data/glossary.txt (data/b638_glossary.txt)' % (
             ls[0].get('line'), ls[1].get('line') if len(ls) > 1 else None),
         '### COMPONENT 2 : the field print (data/b638_structure_fields.txt) ; the G036 note (data/b638_g036_line.json) ; N3 %s' % S['N3'][0],
         '### COMPONENT 3 : the generator (data/b638_gen_diff.txt, data/b638_gen_test.txt) ; the lists data/b638_nodes_zeta.txt, data/b638_nodes_chi.txt ; '
         'the pages (data/b638_page_*_glossary.json) ; every test after the commit (data/b638_tests_after.txt) ; H72a %s' % S['H72a'][0],
         '### COMPONENT 4 : the census reads (data/b638_census.txt)',
         '### COMPONENT 5 : the edition (data/b638_edition_CENSUS.txt, data/b638_repin.txt, data/b638_census_termscan.txt, data/b638_opening.txt) ; the '
         'pages again by the page clause (data/b638_page_*_placement.json) ; page arms data/b638_page_arms.txt ; the act root`s census path '
         '(data/b638_actroot_test.txt) ; H72b %s ; H72c %s ; H72d %s ; H28a %s ; H28b %s ; H28c %s' % (
             S['H72b'][0], S['H72c'][0], S['H72d'][0], S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 6 : FINDINGS :%s (the entry) ; OPEN_TRAILS :%s (the record) ; the root %s ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s ; the mirror after '
         'the last push (data/b638_mirror.txt)' % (fj.get('entry_line'), tj.get('line'), (J.get('root') or '')[:16], S['N1'][0], S['N2'][0], S['N3'][0],
                                                 S['N4'][0], S['N5'][0])]
    put_txt('b638_components.txt', L)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    cells = predict_cells(e, 'FINDINGS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  table cells the entry would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b638_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    cells = predict_cells(e, 'OPEN_TRAILS.md')
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  table cells the record would make: %s ; no-disclosure hits: %s ; scanner %s' % (cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e[:9000])
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b638_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b638_trail.json')['line'])


CORR_HEAD = '*Appended 2026-10-07 by b638 to its record (:%d) -- A CORRECTION, THE SEAT’S:*'


def correction(*a):
    Q = R2._Q()
    if not CORRECTION:
        sys.exit('### NO CORRECTION IN data/b638_defects.json -- NOTHING WRITTEN')
    rec_ = Q.line_of(Q.OT, TRAIL_HEAD)
    t = '\n%s %s\n' % (CORR_HEAD % rec_, CORRECTION)
    cells = predict_cells(t, 'OPEN_TRAILS.md')
    nd, _n = _nd(t)
    sc, clean = _scan_text(t, 'correction')
    if 'dry' in a:
        print(t)
        return
    if cells or any(nd.values()) or not clean:
        sys.exit('### THE LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, CORR_HEAD % rec_)
    r = Q.append_to(Q.OT, t)
    put_json('b638_correction.json', dict(line=Q.line_of(Q.OT, CORR_HEAD % rec_), head=CORR_HEAD % rec_, append=r))
    print('  OPEN_TRAILS correction :%s' % Q.line_of(Q.OT, CORR_HEAD % rec_))


# ================================================================================ THE MIRROR, AFTER THE LAST PUSH
ZIP = K.MIRROR_ZIP
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % K.MIRROR_TAG)


def mbuild(*a):
    """### the builder, unedited, with -DateTag, after the act's last push (PLACE-papers HEAD at its remote); it writes the zip in
    ### D:/MY-DOwnloads, its stage in %TEMP% and relay tools/mirror_prevbuild.json (its state). Refuses if the zip or stage exists."""
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED (the builder deletes a same-named one)')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag', K.MIRROR_TAG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b638_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-1500:], r.stderr[-800:], 'exit', r.returncode)


def mroot(*a):
    """### OPEN_TRAILS :12929, standing: the line "Act root: <act> <root>" from relay data/act_roots.txt's last line added to MANIFEST in its
    ### stage, in MANIFEST's own form -- the staged MANIFEST written and the zip's one entry updated in place."""
    last = [l for l in io.open(os.path.join(D, 'act_roots.txt'), encoding='utf-8').read().split(NL) if l.strip()][-1].split()
    if last[0] != 'b638':
        sys.exit('### THE ROOTS FILE`S LAST LINE IS %s, NOT b638`s -- NOTHING WRITTEN' % last[0])
    line = 'Act root: %s %s' % (last[0], last[1])
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'Act root: ' in raw:
        sys.exit('### THE ROOT LINE IS IN THE STAGED MANIFEST ALREADY -- REFUSING TO WRITE IT TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    sep = '\r\n' if '\r\n' in text else '\n'
    out = text.rstrip('\r\n') + sep + sep + line + sep
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b638_mirror_root.json', dict(at=utc(), line=line, bom=bom, zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode,
                                           update_err=ps.stderr.strip()))
    print('  %s ; update rc %d ; zip sha256 %s -> %s' % (line, ps.returncode, before[:16], after[:16]))


def mverify(*a):
    """### relay tools/mirror_verify.py on the zip, all three clauses, run from PLACE-papers (clause 2's ls-remote is cwd-dependent)"""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b638_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-1200:])


def mbank(*a):
    """### data/b638_mirror.txt and its json: the zip's md5, sha256 and size, its file count, the MANIFEST's md5, its ROSTER line and its root
    ### line, the previous build's MANIFEST md5, the verification's verdict; the no-disclosure arm over the zip's file list."""
    import b616_record as R6
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    text = man.decode('utf-8-sig').replace(chr(13), '')
    ls = text.split(NL)
    rows = [l for l in ls if re.match(r'^\| [^|:]', l) and not l.startswith('| flat file')]
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    zb = open(ZIP, 'rb').read()
    ver = rd('b638_mirror_verify.txt')
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in ver
    prev_md5 = hashlib.md5(zipfile.ZipFile(K.MIRROR_PREV).read('MANIFEST.md')).hexdigest() if os.path.exists(K.MIRROR_PREV) else None
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    head = next((l for l in ls if l.startswith('Source: PLACE-papers @')), '')
    files = [n for n in names if n != 'MANIFEST.md']
    L = ['b638 -- THE MIRROR, BUILT AFTER THE ACT`S LAST PUSH BY THE UNEDITED BUILDER ON THE %d-FILE ROSTER, banked %s' % (K.ROSTER_FILES, utc()),
         '### THE ZIP (for the author`s upload) : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), hashlib.md5(zb).hexdigest(), hashlib.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; %d bytes ; %d rows ; entries in the zip %d (files %d + MANIFEST)' % (
             hashlib.md5(man).hexdigest(), len(man), len(rows), len(names), len(files)),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'),
         '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         '### THE SOURCE LINE : %s' % head,
         '### THE PREVIOUS BUILD : %s, MANIFEST md5 %s' % (K.MIRROR_PREV, prev_md5),
         '### THE VERIFICATION (relay data/b638_mirror_verify.txt): %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd),
         '### THE FILE LIST:'] + ['    %s' % n for n in names] + ['### THE MANIFEST, WHOLE:'] + ['    ' + l for l in ls]
    put_txt('b638_mirror.txt', L)
    put_json('b638_mirror.json', dict(at=utc(), zip=ZIP, zip_md5=hashlib.md5(zb).hexdigest(), zip_sha256=hashlib.sha256(zb).hexdigest(), bytes=len(zb),
                                      manifest_md5=hashlib.md5(man).hexdigest(), rows=len(rows), entries=len(names), files=len(files),
                                      roster_line=rosterl, root_line=rootl[0] if rootl else '', prev_manifest_md5=prev_md5, clean=clean, nd=dict(nd), source=head))
    for l in L[:9]:
        print(l[:300])


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_') or cmd in ('jl', 'rd', 'seal_hashes', 'root_banks', 'answer_of', 'n5', 'struct_fields', 'glossary_lines',
                                                          'opening_scan', 'h72'):
        print('usage: b638_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
