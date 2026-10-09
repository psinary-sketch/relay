# -*- coding: utf-8 -*-
"""b645_record.py -- THE ACT'S RECORD TOOL, UNDER (R255). ### ONE SUBCOMMAND PER BANK.

### ### b645: LANE THREE, ACT SEVENTY-TWO -- THE REVIEW PASS OPENED: THE LICENSED-STATEMENT TABLE BUILT AND TESTED; THE SEAM ROWS, THE
### LOAD-BEARING MAP, SIDE-EXPLICIT-FORMULA'S DOCSTRINGS AT v0.26 AND THE MONOGRAPH'S CLAIMS EACH TO ONE VERDICT; THE CENSUS'S CLUSTER,
### PHASE AND MATURITY COLUMNS DEFINED; NO EDITION RE-CUT; THE DEPOSIT HELD. Subcommands write only `data/b645_*` unless the docstring
### names another file; `dry` routes WRITES to the scratchpad (the dispatcher passes it through; b644's defect (o)). The generic helpers are
### b602's, b633's and b644's record tools', imported; ledger appends through b566's guarded `append_to`. Lean runs are the seat's,
### detached under tools/build_watch.py ((R254)(3)); this tool writes their launchers and reads their logs. Every bank is written LF.
"""
import collections
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
import b645_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = K.PP
RELAY = ROOT.replace('\\', '/')
PRE_PP, PRE_RELAY, STEPZERO, DATE = K.PRE_PP, K.PRE_RELAY, K.STEPZERO, K.DATE
SP = K.SP
SESSION_ID = 'f004d01d-ad93-416c-a916-fe6e52403753'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
R3.SP, R3.SESSION, R3.SESSION_ID = SP, SESSION, SESSION_ID
FACE = 'b645_registration_2026-10-09.txt'
DRY = 'dry' in sys.argv[2:]
R3.DRY = DRY

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R3._show
_write, _scan, _clean = R3._write, R3._scan, R3._clean
lines_of = R3.lines_of
STD3 = '[propext, Classical.choice, Quot.sound]'


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


# ================================================================================ COMPONENT 0: STEP ZERO
def procs(suffix=''):
    """data/b645_procs.txt (or data/b645_procs_<suffix>.txt, a listing after a stopped run): the process listing -- tail, lean, lake and
    python named, each with its parent and command line -- and the free memory."""
    ps = ("Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(tail|lean|lake|python|python3)(\\.exe)?$' } | ForEach-Object { "
          "$par = Get-CimInstance Win32_Process -Filter (\"ProcessId=\" + $_.ParentProcessId); "
          "\"{0}`t{1}`t{2}`t{3}`t{4}\" -f $_.ProcessId, $_.ParentProcessId, ($(if ($par) {'parent alive'} else {'ORPHAN'})), $_.Name, $_.CommandLine }; "
          "'FREE ' + [int]((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory/1024)")
    out = subprocess.run(['powershell', '-NoProfile', '-Command', ps], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    rows = [l for l in out.split(NL) if l.strip() and not l.startswith('FREE ')]
    me = os.getpid()
    rows = [l for l in rows if not l.startswith('%d\t' % me)]
    free = re.search(r'^FREE (\d+)', out, re.M)
    orph = [l for l in rows if '\tORPHAN\t' in l]
    L = ['b645 -- COMPONENT 0: THE PROCESS LISTING AT STEP ZERO, tail, lean, lake AND python NAMED (%s)' % utc(), '',
         '### pid / parent / parent state / name / command line (this tool`s own python process left out, pid %d)' % me]
    L += ['  ' + l[:400] for l in rows] or ['  ### NONE: no tail, lean, lake or python process is running']
    L += ['', '### orphans: %s ; stopped by PID: none needed' % (len(orph) if orph else 'NONE'),
          '### free memory: %s MB ; the hold %d MB' % (free.group(1) if free else '?', K.HOLD)]
    if suffix:
        L[0] = L[0].replace('AT STEP ZERO', 'AFTER THE STOPPED RUNS (%s)' % suffix)
    put_txt('b645_procs%s.txt' % ('_' + suffix if suffix else ''), L)
    print(NL.join(L[3:]))


def hold_launch(target, suffix=''):
    """writes the PowerShell launcher for ONE call under tools/build_watch.py (scratchpad) and prints its path: an Interfaces module's build
    (b644's command, its mathlib4 checkout and output directory) or the reader's test (through b645_tests.py); the bank data/b645_build_watch.json.
    `suffix` names a later retry's logs apart (the author's answer at step zero: once more before the seal), step zero's left as written."""
    import b644_record as R44
    q = lambda s: "'" + s.replace("'", "''") + "'"   # noqa: E731
    if target == 'test':
        tag, cwd, lp = 'b645_test_elab', 'D:\\relay', None
        module = 'test_elab_reader_b634'
        cmd = ['python', 'D:\\relay\\tools\\b645_tests.py', 'run', K.HOLD_TEST]
    else:
        pin = dict(R44.K.IFACES)[target]
        lean, args, lp, out = R44._iface_cmd(target, pin)
        os.makedirs(out, exist_ok=True)
        tag, cwd, module = 'b645_build_%s' % target, pin.replace('/', '\\'), 'SIDE-global-section/Interfaces/%s.build' % target
        cmd = [lean.replace('/', '\\')] + [x.replace('/', '\\') if not x.startswith('--root') else x for x in args]
    tag += suffix
    log = '%s/w_%s.log' % (SP, tag)
    wargs = ['D:\\relay\\tools\\build_watch.py', '--module', module, '--bank', 'D:\\relay\\data\\b645_build_watch.json', cwd,
             log.replace('/', '\\')] + cmd
    ps = ['$os = Get-CimInstance Win32_OperatingSystem',
          '"free before: " + [math]::Round($os.FreePhysicalMemory/1024) + " MB"']
    if lp:
        ps.append('$env:LEAN_PATH = %s' % q(lp))
    ps += ['$env:PYTHONIOENCODING = %s' % q('utf-8'),
           '$a = @(%s)' % ', '.join(q('"%s"' % x if ' ' in x else x) for x in wargs),
           '$p = Start-Process -FilePath python -WorkingDirectory %s -ArgumentList $a -WindowStyle Hidden -PassThru '
           '-RedirectStandardOutput %s -RedirectStandardError %s' % (q(SP.replace('/', '\\')), q('%s\\w_%s.out' % (SP.replace('/', '\\'), tag)),
                                                                      q('%s\\w_%s.err' % (SP.replace('/', '\\'), tag))),
           '"watchdog pid " + $p.Id + " log %s"' % log]
    p = os.path.join(SP, 'launch_%s.ps1' % tag)
    io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(ps) + '\n')
    print(p)


def _log_outcome(log):
    import b644_record as R44
    return R44._log_outcome(log)


def hold_bank(*a):
    """data/b645_hold_retry.txt and .json: (R255)(6) -- each of the six Interfaces modules and the reader's test retried once at step zero
    under (R254)(3), the free memory before each and the watchdog's lows printed; where beneath the hold, the prompt's numbers."""
    L = ['b645 -- COMPONENT 0, (R255)(6): THE HOLD RETRY AT STEP ZERO, EACH CALL DETACHED UNDER tools/build_watch.py, ONE PER CALL (%s)' % utc(), '',
         '### the route: b644`s (relay data/b644_iface_builds.txt), each module at the mathlib4 checkout its profile was built with; the test '
         'through tools/b645_tests.py; the hold %d MB, the author`s' % K.HOLD, '']
    J = []
    for t in list(K.IFACE_MODS) + ['test']:
        tag = 'b645_test_elab' if t == 'test' else 'b645_build_%s' % t
        o = _log_outcome('%s/w_%s.log' % (SP, tag))
        out = io.open('%s/w_%s.out' % (SP, tag), encoding='utf-8', errors='replace').read() if os.path.exists('%s/w_%s.out' % (SP, tag)) else ''
        fb = re.search(r'free before: (\d+) MB', rd_sp('launch_out_%s.txt' % tag))
        if t == 'test' and o['verdict'] == 'BUILT':
            o['verdict'] = 'RAN'
        row = dict(target=t if t != 'test' else K.HOLD_TEST, tag=tag, free_before=int(fb.group(1)) if fb else None, **o)
        J.append(row)
        L.append('  %-24s free before %s MB ; %-16s starts %d ; refused %d ; stopped %d ; lows %s ; lowest sample %s%s' % (
            row['target'], row['free_before'], row['verdict'], o['starts'], o['refused'], o['stops'], o['lows'] or '-', o['samples_min'],
            (' ; errors: ' + ' | '.join(o['errors'])) if o['errors'] else ''))
    beneath = [r for r in J if r['verdict'] == 'RUN-BENEATH-HOLD']
    L += ['', '### ### **RETRIED %d ; RUN-BENEATH-HOLD %d ; BUILT OR RAN %d ; OTHER %d.**' % (
        len(J), len(beneath), sum(1 for r in J if r['verdict'] in ('BUILT', 'RAN')),
        sum(1 for r in J if r['verdict'] not in ('BUILT', 'RAN', 'RUN-BENEATH-HOLD')))]
    if beneath:
        L += ['### (R255)(6): THE HOST BENEATH THE HOLD AGAIN -- THE PROMPT`S NUMBERS: ' + ' ; '.join(
            '%s free before %s MB, lows %s' % (r['target'], r['free_before'], r['lows']) for r in beneath)]
    put_txt('b645_hold_retry.txt', L)
    put_json('b645_hold_retry.json', dict(at=utc(), hold=K.HOLD, rows=J))
    print(NL.join(L[4:]))


def READS():
    """the reads the ferry names, each (label, repo, rev, path, selector, width): a selector is a list of line numbers or ('GREP', regex)."""
    return [
        ('relay data/b644_closing.txt: its head line, the RBH runs, the seam rows, the outsiders and the next act', RELAY, PRE_RELAY,
         'data/b644_closing.txt', ('GREP', r'^b644 closed|lows \[|HEAD:FINDINGS|HEAD:OPEN_TRAILS|ROWS \d|^      D:/|private|THE NEXT ACT'), 240),
        ('relay data/b644_defects.txt: (a)-(r)', RELAY, PRE_RELAY, 'data/b644_defects.txt', ('GREP', r'^    \([a-r]\) '), 160),
        ('THE_LOAD_BEARING_MAP.md in full, each row by line (its headings and row counts here; the rows read whole into the table)', PP, PRE_PP,
         K.MAP, ('GREP', r'^#|^\*\*Tier counts|^\*\*Corrected counts|^\*76 nodes|^\*\*Counts\.'), 200),
        ('the seam rows', PP, PRE_PP, 'FINDINGS.md', [K.SEAM_ROWS[0][1]], 600), ('', PP, PRE_PP, 'OPEN_TRAILS.md', [K.SEAM_ROWS[1][1]], 600),
        ('SIDE-explicit-formula`s rh_strip_imp_rh_holds at v0.26 (its axiom print: relay data/b536_profile.json, printed below)', K.EF, K.EF_PIN,
         K.SEAM_DECL[0], [83, 84, 85, 96, 97, 98, 100, 101, 106, 107], 200),
        ('the intake form: relay tools/b628_record.py (the form`s check, `intake`; the ferry`s tools/b628_intake.py is no file -- the form lives here)',
         RELAY, PRE_RELAY, 'tools/b628_record.py', ('GREP', r'^CLAIM_RE|^def intake|kernel-verified only|route verdict|work-order or reason'), 220),
        ('', RELAY, PRE_RELAY, 'tools/b628_worklist.py', ('GREP', r'^GRADES|^CLUSTERS|^VERDICTS|^INTAKE_'), 220),
        ('relay data/b628_intake_summary.txt: the pilot`s outcomes and their names', RELAY, PRE_RELAY, 'data/b628_intake_summary.txt',
         ('GREP', r'^### (CLAIMS|GRADES|ROUTES|KERNEL-VERIFIED)'), 400),
        ('the elaborated reader`s statement bank at 82550e4 (relay data/b643_rerun.txt; its bank data/b643_elab_ef.txt)', RELAY, PRE_RELAY,
         'data/b643_rerun.txt', ('GREP', r'^### THE ELABORATED READER|names typed|GRADE MOVES'), 220),
        ('the terminal table`s grade and provenance columns (its header)', RELAY, PRE_RELAY, 'data/terminal_table.md', [1, 3, 4, 6, 7], 400),
        ('relay data/b643_premise_table.json (by its text bank) and data/b644_hinges.txt', RELAY, PRE_RELAY, 'data/b643_premise_table.txt',
         ('GREP', r'^\| \w|^### ### '), 160),
        ('', RELAY, PRE_RELAY, 'data/b644_hinges.txt', ('GREP', r'^### b643|^### THE HEADS|^### ### '), 220),
        ('relay data/b644_census_roster.txt: its fields and fragments', RELAY, PRE_RELAY, 'data/b644_census_roster.txt', ('GREP', r'^### |^  R\d\d '), 200),
        ('THE_DOCUMENT_CLASS_TAXONOMY.md`s class list', PP, PRE_PP, K.TAXONOMY, ('GREP', r'^\*\*Tier [A-Z]+ '), 200),
        ('A_Place_to_Stand_v5_18.md`s section list', PP, PRE_PP, K.MONO, ('GREP', r'^#{1,2} '), 140),
        ('OPEN_TRAILS :13489-:13497, :13599', PP, PRE_PP, 'OPEN_TRAILS.md', [13489, 13491, 13493, 13495, 13497, K.B644_RECORD], 600),
        ('relay data/b644_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b644_closing_push_out.txt',
         ('GREP', r'push_gated: (as-of|DONE|main read back)'), 200),
    ]


def reads(*a):
    """data/b645_reads.txt: the reads the ferry names, cited by path and line, each printed from its blob at its pin."""
    L = ['b645 -- THE READS THE FERRY NAMES, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN (%s)' % utc(), '']
    for label, repo, rev, path, sel, width in READS():
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        t = _show(repo, rev, path)
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH BLOB' % (label, path, at))
            continue
        sl = lines_of(t)
        nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)] if isinstance(sel, tuple) else \
            [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label or '(the same group)', path, at, len(nums), len(sl)))
        for n in nums:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    pr = jl(K.SEAM_PRINT)
    L += ['', '### the seam`s axiom print (relay data/%s, b536 at v0.2 = 5c72cad; Seam.lean unchanged in its statement since):' % K.SEAM_PRINT]
    L += ['    ' + l for l in pr.get('lines') or ['### NONE']]
    L += ['', '### the local intake bank`s state: %s' % (g(RELAY, 'status', '--porcelain', '--', K.LOCAL_BANK).strip() or 'NOT PRESENT'),
          '### the local intake bank tracked by git: %s' % (g(RELAY, 'ls-files', '--', K.LOCAL_BANK).strip() or 'NO -- untracked'),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b645_reads.txt', L)
    print('  %d read groups ; %d lines' % (len(READS()), len(L)))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R255)(1)-(2)
W_HEAD = '*Appended 2026-10-09 by b645 to b644’s entry (:%d), under `(R255)`(1) -- b644 AT ITS WEIGHT, ITS FIGURES READ FROM ITS BANKS:*'
WL_HEAD = ('*Appended 2026-10-09 by b645 to the form of an edition (:11864), the writing law (so named at :13383), beneath its standing '
           'clauses, under `(R255)`(2) -- PAPERS STATE; LEDGERS NARRATE, STANDING FROM b646:*')
HF_HEAD = ('*Appended 2026-10-09 by b645, under the author’s answer at b645’s step zero ((R255)(6)) -- W-ORD-HOLD-FOOTPRINT, ENTERED AND '
           'PRICED, TRIGGER A RULING ON THE HOLD:*')


def _need(pat, text, what):
    m = re.search(pat, text, re.M | re.S)
    if not m:
        sys.exit('### %s UNREAD (%s) -- NOTHING WRITTEN' % (what, pat[:60]))
    return m


def _b644_figures():
    head = _need(r'^b644 closed: relay (\w+), PLACE-papers (\w+); suite (\d+) of (\d+); root (\w+)…; (\d+) prompts answered; (\d+) defects',
                 rd('b644_closing.txt'), 'b644`s closing head line')
    act = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b644 --', PRE_RELAY).strip()[:8]
    closing = g(RELAY, 'log', '--format=%h', '-1', '--grep=^b644 closing', PRE_RELAY).strip()[:8]
    chain = _need(r'THE ACT-ROOT CHAIN, recomputed:.*\bb644 AGREE', rd('b644_checks_postpush.txt'), 'b644`s post-push chain line')
    agree = sorted(set(re.findall(r'\b(b6\d\d) AGREE', rd('b644_checks_postpush.txt'))))
    crlf = _need(r'### CRLF READS (\d+) over b624-b643', rd('b644_actroot_commit.txt'), 'the CRLF count')
    hin = _need(r'HINGES UNDER THE REFINED DEFINITION (\d+)', rd('b644_hinges.txt'), 'the hinge count')
    heads = _need(r'### ### \*\*HEADS (\d+)', rd('b644_hinges.txt'), 'the head count')
    lat = _need(r'ROWS (\d+) ; PLACED ON THE FIVE AXES (\d+) ; TOP (\d+)', rd('b644_lattice.txt'), 'the lattice counts')
    path = _need(r'PREMISES ON THE PATH (\d+) ; OPEN (\d+)', rd('b644_clause_path.txt'), 'the clause-path counts')
    desc = os.path.getsize(os.path.join(D, 'b644_deposit_description.txt'))
    resid = len(re.findall(r'^### PASSAGE|^  \(\d+\)|^\(\d+\)', rd('b644_desc_residue.txt'), re.M))
    seam = _need(r'ROWS (\d+)\.', rd('b644_seam_rows.txt'), 'the seam rows')
    rbh = [r for r in jl('b644_build_watch.json').get('rows') or []]
    osec = _need(r'^### FOR THE AUTHOR TO NAME.*?(?=^### CARRIED FORWARD)', rd('b644_closing.txt'), 'the outsiders` section').group(0)
    outs = re.findall(r'^      D:/', osec, re.M)
    zen = _need(r'draft (\d+) ; (\d+) files read back', rd('b644_closing.txt'), 'the draft line')
    return dict(head=head, act=act, closing=closing, agree=agree, crlf=crlf.group(1), hin=hin.group(1), heads=heads.group(1), lat=lat,
                path=path, desc=desc, resid=resid, seam=seam.group(1), rbh=rbh, outs=len(outs), zen=zen, chain=bool(chain))


def _weight():
    f = _b644_figures()
    h = f['head']
    return ('\n%s relay %s (closing), %s (act), PLACE-papers %s; the suite %s of %s pre-push and post-push, the two earlier pre-push runs kept '
            'as attempts, name resolution failing mid-run (relay data/b644_dns_burst_test.txt, defect (q)); the root %s…; %s prompts answered; '
            '%s defects, (a) to (r). The chain read at commit: every root %s to %s AGREE, the %s CRLF reads counted apart, every bank from b644 '
            'written LF. Shared data files additive. The watchdog stop in force: SIDE-global-section`s %d Interfaces modules and %s '
            'RUN-BENEATH-HOLD twice, their consumers UNREAD in the census at v0.7.1. Hinges %s of %s under the refined definition, Prime the one '
            'hinge across kernels, the DOMAIN heads set aside. The census at v0.7.1, its four faults regenerated. The seven companions at their '
            'patch labels, ONE_PAGE_PROOF at v1.0.1 (W-ORD-LABEL-READER entered). The description at %d bytes composed from banks, three '
            'readers, its residue banked; the clause-path print: %s premises on the path from h2_sign to RiemannHypothesis, %s OPEN; the seam '
            'compiled (rh_strip_imp_rh_holds, DERIVES), the navigator’s word corrected. The draft %s at %s files read back at their digests, '
            'HELD. The lattice banked, %s of %s rows on five axes, %s at the TOP. %s seam rows for the review pass. %d local repositories '
            'outside the chain and one private, for the author’s naming. Nothing deposited; no kernel source touched.\n' % (
                W_HEAD % K.B644_ENTRY, f['closing'], f['act'], h.group(2), h.group(3), h.group(4), h.group(5)[:8], h.group(6),
                h.group(7), f['agree'][0] if f['agree'] else '?', f['agree'][-1] if f['agree'] else '?', f['crlf'],
                sum(1 for r in f['rbh'] if '/Interfaces/' in r['module']),
                ' and '.join(r['module'] for r in f['rbh'] if '/Interfaces/' not in r['module']) or '?', f['hin'],
                f['heads'], f['desc'], f['path'].group(1), f['path'].group(2), f['zen'].group(1), f['zen'].group(2), f['lat'].group(2),
                f['lat'].group(1), f['lat'].group(3), f['seam'], f['outs']))


def _writing_law():
    return ('\n%s a keystone edition carries no more and no less than what the kernels and the mutual conclusions license, in the glossary’s '
            'vocabulary (relay data/glossary.txt); a superseded framing leaves the body for ERRATA as a dated entry naming the ledger line that '
            'retired it; the body carries no “formerly”, no hedge about a claim it no longer makes, and no numeral that is not its finding; the '
            'back matter carries one paragraph, “What this edition changed”, pointing to ERRATA. Ledgers keep the append-and-date law. The '
            'monograph’s next edition under this clause is a re-cut, v6.0, not v5.19. No edition is re-cut at b645: the clause governs every '
            'edition from b646, and the review pass’s licensed-statement table (relay tools/licensed_table.py) is the instrument an edition reads '
            'its licence from.\n' % WL_HEAD)


def _footprint():
    H = jl('b645_hold_retry.json')
    rows = [r for r in H.get('rows') or [] if r.get('verdict') == 'RUN-BENEATH-HOLD']
    if len(rows) != 2:
        sys.exit('### THE HOLD RETRY BANK DOES NOT CARRY THE TWO RUNS -- NOTHING WRITTEN')
    peaks = []
    for r in rows:
        t = io.open('%s/w_%s.log' % (SP, r['tag']), encoding='utf-8', errors='replace').read()
        peaks += [int(x) for x in re.findall(r'^### EXIT \d+ \S+ \d+ s peak (\d+) MB', t, re.M)]
    return ('\n%s the hold retry at b645`s step zero (relay data/b645_hold_retry.txt) built five of SIDE-global-section`s six Interfaces '
            'modules and stopped two runs twice each -- %s -- while each run`s peak as the watchdog reads it, the working set of its direct child '
            'alone, stayed at or under %d MB: the hold measures the host`s other tenants, not the build. The work-order: tools/build_watch.py records the '
            'run`s own peak (the summed working set of its process tree) beside the host`s low at every sample and in the bank row, so a future '
            'ruling can set the hold on the footprint a run adds rather than on what the host happens to have free. Priced: one act, a tool edit '
            'and its planted test, no kernel; the hold stays at 2,560 MB until the author rules on the record it produces.\n' % (
                HF_HEAD, '; '.join('%s, free before %s MB, lows %s MB' % (r['target'], r['free_before'], ' and '.join(str(x) for x in r['lows']))
                                   for r in rows), max(peaks) if peaks else -1))


def record_lines(*a):
    """Component 1, (R255)(1)-(2) and the author's answer at step zero: FINDINGS, b644 at its weight (to :8025); OPEN_TRAILS, the writing
    law's clause (to :11864) and W-ORD-HOLD-FOOTPRINT entered and priced."""
    import b641_record as R41
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, '## The chain read at commit and shared files additive')
    if entry != K.B644_ENTRY:
        sys.exit('### b644`S ENTRY MOVED (%s) -- NOTHING WRITTEN' % entry)
    items = [('FINDINGS.md', W_HEAD % K.B644_ENTRY, R41._poss(_weight())), ('OPEN_TRAILS.md', WL_HEAD, R41._poss(_writing_law())),
             ('OPEN_TRAILS.md', HF_HEAD, R41._poss(_footprint()))]
    allt = ''.join(t for _f, _h, t in items)
    cells = sum((R3.predict_cells(t, f) for f, _h, t in items), [])
    nd, _n = R3._nd(allt)
    p = os.path.join(SP if DRY else D, 'b645_scanfile_lines.md')
    _write(p, allt.encode('utf-8'))
    sc = _scan(p)
    clean = _clean(sc)
    ticks = [h[:40] for _f, h, t in items if t.count('`') % 2]
    unread = [x for x in ('?', '### NOT', 'None', '-1 MB') if x in allt]
    outside = [n for n in R41.OAI_NEEDLES if n in allt]
    print('  table cells: %s ; no-disclosure hits: %s ; scanner %s ; odd backticks: %s ; unread figures: %s ; outside names: %s' % (
        cells or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN', ticks or 'NONE', unread or 'NONE', outside or 'NONE'))
    if DRY:
        for _f, _h, t in items:
            print(t)
        if not clean:
            print(sc[-1500:])
        return
    if cells or any(nd.values()) or not clean or ticks or unread or outside:
        sys.exit('### A LINE WOULD MAKE A TABLE CELL, CARRY TECHNE TEXT, A STEM, ODD BACKTICKS, AN UNREAD FIGURE OR AN OUTSIDE NAME -- NOTHING WRITTEN')
    R3._land(Q, items, 'b645_record_lines.json', K.B644_ENTRY)


# ================================================================================ COMPONENT 2: THE INSTRUMENT, (R255)(3)
def instrument(*a):
    """data/b645_instrument.txt: the planted tests of tools/licensed_table.py run and counted (one per verdict, a HAND row lacking its citation
    refused), and the rules and the intake mapping printed -- before any real row is read."""
    import licensed_table as LT
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_licensed_table_b645.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    out = (r.stdout + r.stderr).rstrip(NL).split(NL)
    L = ['b645 -- COMPONENT 2, (R255)(3): THE INSTRUMENT, tools/licensed_table.py, ITS PLANTED TESTS RUN AND COUNTED BEFORE ANY REAL ROW (%s)' % utc(),
         '', '### tools/test_licensed_table_b645.py, exit %d:' % r.returncode] + out + [''] + LT.rules()
    put_txt('b645_instrument.txt', L)
    print(out[-1])


# ================================================================================ COMPONENT 3: THE SEAM ROWS AND THE MAP, (R255)(4)(a)-(b)
EFP = 'SIDE-explicit-formula@82550e4:SIDEExplicitFormula/'
KP = 'SIDE-kernel@0e5233f:'
LVP = 'SIDE-lv-conservation@6efa9e5:SIDELvConservation/'
MAPC = lambda n: 'PLACE-papers@6871ba2:%s:%d' % (K.MAP, n)   # noqa: E731
_TT = None


def _tt():
    global _TT
    if _TT is None:
        _TT = (json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'],
               lines_of(_show(RELAY, PRE_RELAY, 'data/terminal_table.md')))
    return _TT


def tt_cite(repo, name):
    """relay@bd1387be:data/terminal_table.md:N -- the table's row for repo and qualified name (or last component)."""
    rows, md = _tt()
    for i, l in enumerate(md, 1):
        m = re.match(r'^\| `([^`]+)` \| `([^`]+)` \|', l)
        if m and m.group(1) == repo and (m.group(2) == name or m.group(2).split('.')[-1] == name):
            return 'relay@%s:data/terminal_table.md:%d' % (PRE_RELAY, i)
    sys.exit('### NO TABLE ROW FOR %s %s -- NOTHING WRITTEN' % (repo, name))


def tt_row(repo, name):
    rows, _md = _tt()
    for x in rows:
        if x['repo'] == repo and (x['name'] == name or x['name'].split('.')[-1] == name):
            return x
    return None


# ### THE FACTS THE MAP'S READINGS STAND ON, each a declaration at its current pin, its table row and its expected grade: verified at the
# ### run (the grade and the statement's needle read from the table), cited in every row that leans on it.
FACTS = collections.OrderedDict([
    ('mellin', ('SIDE-explicit-formula', 'mellin_Phi_eq_zero_of_re_le_one', EFP + 'RegisterDepth.lean:101', 'DERIVES', 'mellin Phi (s / 2) = 0')),
    ('lvh2', ('SIDE-explicit-formula', 'lv_h2_false_on_strip', EFP + 'RegisterDepth.lean:143', 'DERIVES', '¬ (mellin Phi (s / 2) ≠ 0)')),
    ('chrh', ('SIDE-explicit-formula', 'ch_iff_rh', EFP + 'H2Bridge.lean:71', 'DERIVES', 'conservationHypothesis ↔ RiemannHypothesis')),
    ('h2rh', ('SIDE-explicit-formula', 'h2_sign_iff_rh', EFP + 'Seam.lean:101', 'DERIVES', 'h2_sign ↔ RiemannHypothesis')),
    ('r1', ('SIDE-explicit-formula', 'not_register1', EFP + 'RegisterDepth.lean:60', 'DERIVES', '¬ Register1_universalityHypothesis')),
    ('r5', ('SIDE-explicit-formula', 'register5_output_holds', EFP + 'RegisterDepth.lean:297', 'DERIVES', 'Register5_output_HilbertPolya')),
    ('seam', ('SIDE-explicit-formula', 'rh_strip_imp_rh_holds', EFP + 'Seam.lean:84', 'DERIVES', 'rh_strip_imp_rh')),
    ('cons', ('SIDE-kernel', 'conservation_of_spectra', KP + 'Kernel/ProductFormula_Rat.lean:72', 'CONFLICT', '(1 : Rat) ^ s = 1')),
    ('route3', ('SIDE-kernel', 'ConservationBridge.riemann_hypothesis', KP + 'Bridge/ConservationBridge.lean:53', 'CONFLICT', 'h_cons : ConservationHypothesis')),
    ('route1', ('SIDE-kernel', 'ConservationBridge.structural_exhaustiveness_proved', KP + 'Bridge/ConservationBridge.lean:46', 'INTERFACES',
                'h_cons : ConservationHypothesis')),
    ('route1u', ('SIDE-kernel', 'TheBridgeComplete.structural_exhaustiveness_proved', KP + 'Bridge/TheBridgeComplete.lean:249', None,
                 'theorem structural_exhaustiveness_proved :\n    StructuralExhaustiveness :=')),
    ('cannon', ('SIDE-kernel', 'SpectralCannonFull.spectral_cannon', KP + 'Kernel/SpectralCannonFull.lean:65', 'DERIVES', 'deriv completedRiemannZeta₀')),
    ('silu', ('SIDE-kernel', 'silence_universal', KP + 'Kernel/SilenceTheorem.lean:74', 'INTERFACES', 'theorem silence_universal')),
    ('sieve', ('SIDE-kernel', 'sieve_ceiling', KP + 'Kernel/Cascade/SieveCeiling.lean:209', 'ENCODES-CONCLUSION \\ SHELL', 'factorsDark')),
    ('ediff', ('SIDE-kernel', 'e_difficulty', KP + 'Kernel/Cascade/SieveCeiling.lean:309', 'CONFLICT', 'DeterminedSystem')),
    ('ostr', ('SIDE-kernel', 'type_I_has_ostrowski', KP + 'MetaKernel.lean:145', 'CONFLICT', '[Fintype Domain]')),
    ('pp', ('SIDE-lv-conservation', 'PartialPositivity.partialPositivity_finiteRange', LVP + 'PartialPositivity.lean:105', 'INTERFACES',
            'theorem partialPositivity_finiteRange')),
    ('h1', ('SIDE-lv-conservation', 'h1_complete_at_Phi', LVP + 'CouplingsAtPhi.lean:418', 'DERIVES', 'C1_realness Phi')),
    ('goal', ('SIDE-lv-conservation', 'RegisterPentagon.goalState_sevenClasses_of_h2', LVP + 'RegisterPentagon.lean:210', 'DERIVES',
              'mellin Phi (s / 2) ≠ 0')),
    ('t3', ('SIDE-lv-conservation', 'T3.T3doubleprime_general_commutation_fails', LVP + 'T3_StepNineBridge.lean:137', 'DERIVES', '¬ ∀')),
    ('c7', ('SIDE-lv-conservation', 'C7_finite_type_false', LVP + 'C7FiniteTypeFalse.lean:68', 'DERIVES', 'completedRiemannZeta₀')),
    ('typed', ('SIDE-effects', 'no_type_d_conspiracies', 'SIDE-effects@a27415d:SIDEEffects/Phase15/Module1.lean:154', None, 'IsEmpty TypeD')),
    ('crt', ('SIDE-effects', 'crt_exhaustiveness', 'SIDE-effects@a27415d:SIDEEffects/Phase15/Module1.lean:146', None, 'StructuralCoupling')),
    ('silv2', ('SIDE-silence-principle', 'silence_universal', 'SIDE-silence-principle@667c254:SIDESilencePrinciple/Basic.lean:181', 'INTERFACES',
               'theorem silence_universal')),
    ('rcurve', ('SIDE-rcurve', 'SIDERCurve.monotone_unique_zero', 'SIDE-rcurve@d5f33b4:SIDERCurve/Criterion.lean:31', 'INTERFACES', 'StrictMono V')),
])


def _fact(k):
    """(the fact's text, its citations) -- the table row read and its grade and statement checked; the run stops on a fact that moved.
    `cite:<citation>` is a line the seat read, cited as it stands; `tt:<repo>:<name>` is a table row, cited by its line."""
    if k.startswith('cite:'):
        return ('', [k[5:]])
    if k.startswith('tt:'):
        _t, repo, name = k.split(':', 2)
        x = tt_row(repo, name)
        return ('`%s` reads %s in the table' % (name, x and x['grade']), [tt_cite(repo, name)])
    repo, name, decl, want, needle = FACTS[k]
    x = tt_row(repo, name)
    if want is not None:
        if not x or x['grade'] != want or needle not in (x['statement'] or ''):
            sys.exit('### THE FACT %s MOVED: %s %s grade %s statement %r -- NOTHING WRITTEN' % (
                k, repo, name, x and x['grade'], x and (x['statement'] or '')[:80]))
        return ('`%s` (%s, grade %s: %s)' % (name.split('.')[-1], decl.split(':')[0], x['grade'], re.sub(r'\s+', ' ', x['statement'])[:160]),
                [decl, tt_cite(repo, name)])
    src = _show('D:/' + repo, decl.split('@')[1].split(':')[0], decl.split(':', 1)[1].rsplit(':', 1)[0]) or ''
    if needle not in src:
        sys.exit('### THE FACT %s MOVED: %s -- NOTHING WRITTEN' % (k, decl))
    return ('`%s` (%s, read at the pin: %s)' % (name, decl.split(':')[0], re.sub(r'\s+', ' ', needle)), [decl])


# ### which facts a CP-1b reading leans on, by the words it uses
READING_FACTS = [
    (r'mellin_Phi_eq_zero_of_re_le_one|false at every s with re s <= 1|false on the strip|vacuous on the strip|h2 at Phi', ['mellin', 'lvh2']),
    (r'ch_iff_rh|RH restated', ['chrh']), (r'h2_sign_iff_rh|Weil form', ['h2rh']), (r'not_register1|R1 false', ['r1']),
    (r'\(1 : Q\) \^ s = 1|STIPULATION', ['cons']), (r'Bombieri|T1-lit|literature premises', ['pp']),
    (r'c66f3c5|a27415d|IsEmpty TypeD|programme-type|programme`s own couplings|programme\'s own couplings', ['typed', 'crt']),
    (r'I\.is_universal', ['silu']), (r'sieve_ceiling', ['sieve']), (r'v1\.1 form|IsDecidable', ['ediff']), (r'667c254|v0\.2\.0', ['silv2']),
    (r'CouplingsAtPhi', ['h1']), (r'Routes 1 and 2 are not routes', ['route1', 'cannon']), (r'countermodel|s = 3', ['t3']),
    (r'ConservationBridge\.riemann_hypothesis|Route 3|conservation interface', ['route3']), (r'h1 complete at Phi|h1\'s completeness|completed h1', ['h1']),
    (r'FINDINGS :396|FINDINGS :5461', ['chrh']), (r'RH <-> H', ['chrh']),
]


def _reading_facts(reading):
    ks = []
    for rx, fk in READING_FACTS:
        if re.search(rx, reading):
            ks += [k for k in fk if k not in ks]
    return ks


def _map_lines():
    return lines_of(_show(PP, PRE_PP, K.MAP))


def _map_rows():
    """every row of the map: (line, kind, section, text) -- table rows (header and rule rows left out), list items, and the body paragraphs
    of 120 characters and more (an italic note, a quotation and a comment left out), counted apart by kind."""
    out, sec = [], ''
    for i, l in enumerate(_map_lines(), 1):
        if l.startswith('#'):
            sec = l
            continue
        if l.startswith('|') and not re.match(r'^\|\s*:?-', l) and not re.match(r'^\| *(rank|keystone|anchor|terminal|node \(qualified name\)|document) *\|', l):
            out.append((i, 'table', sec, l))
        elif l.startswith('- '):
            out.append((i, 'item', sec, l))
        elif len(l) >= 120 and (l.startswith('**') or not re.match(r'^(\*|>|<!--|\s)', l)):
            out.append((i, 'para', sec, l))
    return out


def _cells(l):
    return [c.strip() for c in l.strip().strip('|').split('|')]


# ### THE SEAT'S HAND READINGS OF THE MAP'S ROWS OUTSIDE THE CP-1b LIST AND THE PAGE-POINTER TABLE, BY LINE: (verdict, licensed, facts,
# ### action). Every one cites the map line and the facts' declarations and table rows; a row not here and in no generated family stops the run.
MATCH = 'none'
MAP_HAND = {
    3: ('MATCHES', 'the document`s class: TIER K, declared b190 by the standing taxonomy (THE_DOCUMENT_CLASS_TAXONOMY.md :34, Tier K presumptive '
        'for the keystones with Correspondence tables)', [], MATCH),
    7: ('UNLICENSED', 'TIER C is the class b189 declared and b190 retired at :3-:5 the next day; no standing declaration carries it', [],
        'RETIRE TO ERRATA: the b189 TIER C declaration, retired by the b190 declaration at :3 (the retired-scheme note :5); an edition carries the one class'),
    8: ('MATCHES', 'the purpose stated from the document`s own content: the union of the Correspondence tables', [], MATCH),
    12: ('MATCHES', 'the (R18) head note: two maps, two keys, neither merged -- the ruling`s own words', [], MATCH),
    18: ('MATCHES', 'the keystone set of fourteen graded tables, named by file', [], MATCH),
    24: ('OVERREACHES', 'h1_complete_at_Phi DERIVES at lv v0.6.0 (c80bdc2; v0.8.0 6efa9e5 carries it): the eight coupling facts at Phi; it closes no '
         'clause on the strip, lv`s h2 at Phi being false at every s with re s <= 1', ['h1', 'mellin', 'lvh2'],
         'RE-CUT: | 1 | `h1_complete_at_Phi` (the eight coupling facts of Ch. 15 at the theta kernel Phi; lv`s h2 at Phi is false on the strip, so no clause is left open there) | lv v0.6.0 `c80bdc2` | DERIVES | SURR · SIMP · RCURVE · PATHS · DOM · BALPOS — 6 |'),
    25: ('MATCHES', 'RegisterPentagon at lv v0.7.0 is a structure of five register faces with the R3 edge not compiled; the row claims the '
         'structure and the open edge, no more', ['goal'], MATCH),
    26: ('OVERREACHES', 'conservation_of_spectra states (1 : Rat) ^ s = 1 for every integer s; n4 = 0 and kappa = 1 are carried by the name, not by '
         'the statement (T2)', ['cons'],
         'RE-CUT: | 1 | `conservation_of_spectra` (states (1 : ℚ)^s = 1; the n₄ = 0 reading is carried by the name) | kernel v1.2 `b1407b2` | DERIVES (a stipulation, T2) | FOUND · SURR · PATHS · IFACE · SIMP · MONO — 6 |'),
    27: ('MATCHES', 'SIDEKernel.formation states 2 + 3 + 2 + 0 = 7, the row`s own parenthesis', [], MATCH),
    28: ('MATCHES', 'C7_finite_type_false DERIVES: no finite-type growth bound for completedRiemannZeta₀', ['c7'], MATCH),
    29: ('MATCHES', 'partialPositivity_finiteRange INTERFACES on its three named premises', ['pp'], MATCH),
    30: ('MATCHES', 'blTerm_nonneg_of_onLine DERIVES at lv v0.8.0 (PartialPositivity.lean :50): the Li term of a zero on the line is nonnegative',
         [], MATCH),
    31: ('MATCHES', 'type_I_has_ostrowski: modus tollens over an abstract Domain whose Fintype is unused; the row`s own cell says the '
         'exhaustiveness is decorative', ['ostr'], MATCH),
    32: ('MATCHES', 'silence_universal INTERFACES on I.is_universal', ['silu'], MATCH),
    33: ('OVERREACHES', 'spectral_cannon states that the real part of the derivative of completedRiemannZeta₀ on the line is zero; it is no route to '
         'sigma = 1/2 and no sub-RH statement (b540)', ['cannon'],
         'RE-CUT: | 9 | `spectral_cannon` (the real part of the derivative of completedRiemannZeta₀ on the critical line is zero; not a route to σ = 1/2) | v1.2/v1.5 | DERIVES | MONO · SIMP · PATHS — 3 |'),
    34: ('MATCHES', 'the order-<=1 growth bounds on completedRiemannZeta₀ and completedLFunction DERIVE', ['c7'], MATCH),
    35: ('OVERREACHES', 'ConservationBridge.riemann_hypothesis takes ConservationHypothesis, which ch_iff_rh shows is RH restated: the terminal '
         'encodes its conclusion (T2); the compiled reduction of RH is h2_sign_iff_rh', ['route3', 'chrh', 'h2rh'],
         'RE-CUT: | — | `ConservationBridge.riemann_hypothesis` (its premise ConservationHypothesis is RH restated, ch_iff_rh: the terminal encodes its conclusion) | kernel v1.3 `0bc21c0` (carried v1.5) | ENCODES-CONCLUSION (T2) | MONO · PATHS |'),
    37: ('MATCHES', 'the SHELL census: the named shells are work-orders, never citations; sieve_ceiling reads SHELL in the table', ['sieve'], MATCH),
    41: ('OVERREACHES', 'the premises are named, but the five registers are not one premise: R1 is false as stated (not_register1), R2 is RH '
         'restated (ch_iff_rh), R4 is equivalent to RH through h2_sign_iff_rh, R5`s output is a theorem (register5_output_holds)',
         ['r1', 'chrh', 'h2rh', 'r5'],
         'RE-CUT: **The named premises are named at every citation site.** The registers once gathered as one master premise h2 stand at different depths: R1 is false as stated (`not_register1`), R2 is RH restated (`ch_iff_rh`), R4 — Weil positivity, `h2_sign` — is equivalent to RH (`h2_sign_iff_rh`), and R5`s output is a theorem (`register5_output_holds`).'),
    45: ('UNDERSTATES', 'goal <= h1 and h2 with h2 the single carried-open premise: h2 in its Weil form is equivalent to RH (h2_sign_iff_rh), and '
         'lv`s h2 at Phi is false on the strip', ['h2rh', 'mellin'],
         'RE-CUT: The RH programme reduces to one open clause, h2_sign (Weil positivity on classK), which the kernel proves equivalent to RH (`h2_sign_iff_rh`); lv`s goal-state form at Phi closes nothing on the strip (`mellin_Phi_eq_zero_of_re_le_one`).'),
    49: ('MATCHES', 'the surround is independent of h2: its rows are compiled facts that name no zero location', ['h1'], MATCH),
    50: ('MATCHES', 'the license ladder`s terminals DERIVE, RH_typeI_of_top INTERFACES on EDifficultyTop', [], MATCH),
    51: ('MATCHES', 'the conservation and substrate keystones lie outside the RH chain', [], MATCH),
    52: ('OVERREACHES', 'R1: TheBridgeComplete`s structural_exhaustiveness_proved is unconditional, as the row says, and states a conjunction about '
         'defined types and σ-level voice identities (the catalogue`s count by decide, C₇ definition-encoded, Ostrowski`s exhaustiveness) -- no '
         'statement about ξ`s zeros (its namesake in ConservationBridge takes h_cons); R2`s spectral_cannon is a fact on the line, no sub-RH '
         'statement; R3`s premise is RH restated', ['route1u', 'route1', 'cannon', 'route3', 'chrh'],
         'RE-CUT: | MONO | MIXED — Routes 1 and 2 independent and neither a route to σ = 1/2; Route 3 RH from RH | R1 `structural_exhaustiveness_proved` (TheBridgeComplete) unconditional, a conjunction about defined types and σ-level identities; R2 `spectral_cannon` a fact on the line; R3 `riemann_hypothesis(h_cons)` encodes its conclusion (`ch_iff_rh`) |'),
    53: ('OVERREACHES', 'monotone_unique_zero is graded INTERFACES in the table (its StrictMono hypothesis), not DERIVES; one direction only',
         ['rcurve', 'h2rh'],
         'RE-CUT: | RCURVE | MIXED | `monotone_unique_zero` INTERFACES on its monotonicity hypothesis (one direction compiled); the closing row`s premise in its Weil form is equivalent to RH (`h2_sign_iff_rh`) |'),
    54: ('MATCHES', 'SIMP`s order inputs DERIVE; its simplicity rows rest on the derivative premise, named', [], MATCH),
    55: ('MATCHES', 'PATHS maps the reduction; its bracket closes the surround, not RH', [], MATCH),
    56: ('UNDERSTATES', 'RH/GRH composing under h2: h2 in its Weil form is equivalent to RH (h2_sign_iff_rh)', ['h2rh'],
         'RE-CUT: | FOUND · DOM · GRH · BALPOS | DOWNSTREAM-OF-H2 | their RH/GRH rows compose under h2, and h2 in its Weil form is RH (`h2_sign_iff_rh`): the condition is the conclusion |'),
    58: ('UNDERSTATES', 'RH reached across the single h2 edge: that edge is RH itself in the Weil form (h2_sign_iff_rh); the terminals called '
         'h2-independent are none of them RH, as the sentence says', ['h2rh', 'h1'],
         'RE-CUT: **The figure in one sentence:** the surround is compiled and h2-independent; RH is equivalent to the one open clause h2_sign (`h2_sign_iff_rh`), so no terminal reaches RH except through RH itself, and the h2-independent terminals are, individually, none of them RH.'),
    64: ('MATCHES', 'the Gate-1 wave`s report: which clusters it graded', [], MATCH),
    66: ('MATCHES', 'the completion gap: the phase1.5/proofs cluster carried older table forms', [], MATCH),
    70: ('MATCHES', 'THE_RESIDUE_OF_RH: its terminals residue markers, the HP row INTERFACES-DISCLAIMED, filed not written', [], MATCH),
    71: ('MATCHES', 'HELD_RESIDUE_v1_1 is a held change-spec, grades on landing', [], MATCH),
    72: ('OVERREACHES', 'the multiplicative/balance row INTERFACES-on-h2: the balance premise is ConservationHypothesis, RH restated (ch_iff_rh), '
         'so the row encodes its conclusion', ['chrh'],
         'RE-CUT: | PATHS | ~11 core rows still "Compiled" | the conservation-frame, formation-count, n₃, seven-voice and Archimedean rows → DERIVES (compiled structural facts); the multiplicative/balance row → ENCODES-CONCLUSION (its premise is RH restated, `ch_iff_rh`); ARM/pentagon rows already graded |'),
    73: ('MATCHES', 'the SURR rows still "Compiled" assigned DERIVES/STRUCTURE', [], MATCH),
    74: ('MATCHES', 'the SIMP content rows assigned DERIVES', [], MATCH),
    75: ('OVERREACHES', 'Route 1 DERIVES what it literally states (TheBridgeComplete :249, unconditional) and Route 2 DERIVES, as the row says; '
         'Route 3 is not INTERFACES-on-h2: its premise is RH restated (ch_iff_rh), ENCODES-CONCLUSION', ['route1u', 'route3', 'chrh'],
         'RE-CUT: | MONO §25.8 | axiom profiles only, grades in prose | Route 1 DERIVES (TheBridgeComplete, a conjunction about defined types and σ-level identities) · Route 2 DERIVES (a fact on the line) · neither a route to σ = 1/2 · Route 3 ENCODES-CONCLUSION (ConservationHypothesis is RH restated, `ch_iff_rh`) |'),
    77: ('OVERREACHES', 'the Route-3 rows are not INTERFACES-on-h2: their premise is RH restated (ch_iff_rh), ENCODES-CONCLUSION (T2)', ['route3', 'chrh'],
         'RE-CUT: **Verdict:** every pre-rubric row`s grade is assigned from the correspondence union at its pin: the content rows DERIVES, the balance/positivity rows INTERFACES on their named premises, and the Route-3 rows ENCODES-CONCLUSION, their premise RH restated (`ch_iff_rh`). No pre-rubric row hides a shell.'),
    126: ('MATCHES', 'h1_complete_at_Phi certifies the eight coupling facts at Phi and nothing about zeros in the strip', ['h1', 'mellin'], MATCH),
    134: ('MATCHES', 'the RH-anchor: h2_sign_iff_rh at its head, then ch_iff_rh and the register census theorems', ['h2rh', 'chrh', 'r1', 'r5'], MATCH),
    144: ('MATCHES', 'partialPositivity_finiteRange T1-lit; Route 3 T2 (ENCODES-CONCLUSION)', ['pp', 'route3', 'chrh'], MATCH),
    181: ('MATCHES', 'relay data/b558_cp1b.txt :4 counts all rows STANDS 637, MOVED-IN-MEANING 177, CREDIT 7, and the documents` own STANDS '
          '367, MOVED-IN-MEANING 177, CREDIT 7', ['cite:relay@%s:data/b558_cp1b.txt:4' % PRE_RELAY], MATCH),
}
# ### the rows the generated families do not read and that read MATCHES on their own cells, by kind of section: the anchor table (:89-:97),
# ### the tiered table (:103-:114) save :108, the unranked rows (:122-:124), the five T0 items (:138-:142), the (R151) item (:152), the b558
# ### rows (:160-:173) -- each read whole by the seat against the facts named beside it.
ANCHOR_FACTS = {89: ['h2rh'], 90: ['chrh'], 91: ['r1'], 92: ['mellin'], 93: [], 94: ['r5'], 95: [], 96: [], 97: ['goal'],
                103: ['h1', 'mellin'], 104: ['goal', 'r1'], 105: ['cons'], 106: [], 107: ['c7'], 109: [], 110: ['ostr'], 111: ['silu', 'r1'],
                112: ['cannon'], 113: ['c7'], 114: ['route3', 'chrh'], 122: ['h2rh'], 123: ['goal', 'mellin'], 124: ['route1u'],
                138: ['h1'], 139: ['c7'], 140: [], 141: ['cannon'], 142: ['c7'], 152: ['chrh', 'r5'],
                160: ['chrh'], 161: ['crt'], 162: ['ediff'], 163: ['h2rh'], 164: ['h2rh'], 165: ['lvh2'], 166: ['mellin'], 167: ['typed'],
                168: ['r1'], 169: [], 170: ['r5'], 171: ['sieve'], 172: [], 173: ['t3']}
MAP_HAND[108] = ('UNDERSTATES', 'partialPositivity_finiteRange is T1-lit under (R150)(3) (the map`s own correction at :144): its premises are '
                 'literature theorems not yet compiled and a numerical premise; T4 is for a claim with no terminal', ['pp'],
                 'RE-CUT: | 4 | `partialPositivity_finiteRange` | v0.8.0 `6efa9e5` | INTERFACES (3 named: VerifiedZerosTo · ExplicitFormulaDecomp · TailBound) | **T1-lit** | INTERFACES on the numerical `VerifiedZerosTo T` and two literature theorems not yet compiled (Bombieri–Lagarias, Voros); T0 when they compile | SURR Correspondence `:187` |')


MAP_HAND[466] = ('OVERREACHES', 'h2_sign_chi_iff_grh_chi (Chi/CriterionConverse.lean :270) reads INTERFACES in the table since b626 (SIDE-global-section '
                 'CORRESPONDENCE rows 522-523, superseding row 432): it takes hχ : χ.IsPrimitive and h1 : χ ≠ 1',
                 ['cite:' + EFP + 'Chi/CriterionConverse.lean:270', 'tt:SIDE-explicit-formula:h2_sign_chi_iff_grh_chi'],
                 'RE-CUT: | `SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi` | INTERFACES | T2-INTERFACES | v0.14 = 4dce7b9 | χ |')
MAP_HAND[467] = ('OVERREACHES', 'h2_sign_chi_imp_grh_chi (Chi/CriterionConverse.lean :264) reads INTERFACES in the table since b626 (CORRESPONDENCE '
                 'rows 520-521, superseding row 432): it takes hχ : χ.IsPrimitive and h1 : χ ≠ 1',
                 ['cite:' + EFP + 'Chi/CriterionConverse.lean:264', 'tt:SIDE-explicit-formula:h2_sign_chi_imp_grh_chi'],
                 'RE-CUT: | `SIDEExplicitFormula.GRHWeil.h2_sign_chi_imp_grh_chi` | INTERFACES | T2-INTERFACES | v0.14 = 4dce7b9 | χ |')
MAP_HAND[469] = ('MATCHES', 'h2_sign_upto is declared by `def` (DetectionRegion.lean :29), a definition; the terminal table grades it DERIVES '
                 'from a FINDINGS cell (:6036) that itself says it is a definition the three-grade vocabulary does not grade -- the table`s '
                 'grade is a matcher`s misread, the map`s DEF stands (a note for the author, not a verdict on the map)',
                 ['cite:' + EFP + 'DetectionRegion.lean:29', 'cite:PLACE-papers@6871ba2:FINDINGS.md:6036', 'tt:SIDE-explicit-formula:h2_sign_upto'],
                 MATCH)


def _b618_rows(rows):
    """the page-pointer table (:432-:508): each node`s E0 read against its row in the table now, by the `terminal` rule."""
    import licensed_table as LT
    out = []
    for i, _k, _s, l in rows:
        c = _cells(l)
        if len(c) != 5 or not c[0].startswith('`SIDEExplicitFormula.'):
            continue
        name = c[0].strip('`')
        x = tt_row('SIDE-explicit-formula', name)
        claimed = c[1]
        if not x:
            last = name.split('.')[-1]
            hit = g(K.EF, 'grep', '-n', '-E', r'^(noncomputable )?(def|abbrev|structure|class|inductive|theorem|lemma) %s\b' % re.escape(last),
                    K.EF_PIN, '--', 'SIDEExplicitFormula/*.lean', 'SIDEExplicitFormula/**/*.lean').strip().split(NL)[0]
            kw = re.search(r':\d+:(?:noncomputable )?(\w+) ', hit)
            if not kw or kw.group(1) not in ('def', 'abbrev', 'structure', 'class', 'inductive'):
                sys.exit('### NO TABLE ROW FOR THE PAGE NODE %s, ITS SOURCE %r -- NOTHING WRITTEN' % (name, hit[:120]))
            f, n = hit.split(':')[1], hit.split(':')[2]
            v = 'MATCHES' if claimed == 'DEF' else 'OVERREACHES'
            out.append(dict(id='MAP-%d' % i, source='PLACE-papers/%s:%d' % (K.MAP, i), stated=l, line=i, kind='table', by='HAND',
                            licensed='%s is declared by `%s` at %s:%s (v0.26 = 82550e4), a definition (DEF); not a row of the terminal table' % (
                                name, kw.group(1), f, n), cited=[MAPC(i), 'SIDE-explicit-formula@82550e4:%s:%s' % (f, n)], verdict=v,
                            action='none' if v == 'MATCHES' else 'RE-CUT: DEF'))
            continue
        lk = lambda n, x=x: (x['name'], x['grade'], re.sub(r'\s+', ' ', x['statement'] or '')[:140], 'v0.26 = 82550e4')   # noqa: E731
        r = LT.terminal_row('MAP-%d' % i, 'PLACE-papers/%s:%d' % (K.MAP, i), l, name, claimed, lk)
        if r is None:
            sys.exit('### THE PAGE NODE %s READS %s AGAINST %s, OFF THE SCALE -- NOTHING WRITTEN' % (name, claimed, x['grade']))
        r['line'], r['kind'] = i, 'table'
        out.append(r)
    return out


def _count_rows(rows):
    """the CP-1b count tables (:185-:203 by terminal, :207-:228 by document) against relay data/b558_cp1b.json."""
    B = jl('b558_cp1b.json')
    per_t = {}
    per_d = {}
    for r in B.get('rows') or []:
        if r.get('own') is False and not r.get('document'):
            pass
    t = rd('b558_cp1b.txt')
    for m in re.finditer(r'^    (\S+)\s+\{([^}]*)\} ; own \{([^}]*)\}', t, re.M):
        per_t[m.group(1)] = dict((k.strip(" '"), int(v)) for k, v in (x.split(':') for x in m.group(2).split(',')))
    for m in re.finditer(r'^    (\S+)\s+(\S+)\s+\{([^}]*)\} ; own \{([^}]*)\}', t, re.M):
        per_d[m.group(2)] = dict((k.strip(" '"), int(v)) for k, v in (x.split(':') for x in m.group(3).split(',')))
    out = []
    for i, _k, _s, l in rows:
        c = _cells(l)
        if len(c) != 4 or not re.match(r'^\d+$', c[1]):
            continue
        key = c[0].strip('`')
        want = (int(c[1]), int(c[2]), int(c[3]))
        src = per_t.get(key) if c[0].startswith('`') else per_d.get(key)
        got = src and (src.get('STANDS', 0), src.get('MOVED-IN-MEANING', 0), src.get('CREDIT', 0))
        bl = [n for n, x in enumerate(lines_of(t), 1) if re.match(r'^    (\S+\s+)?%s\s+\{' % re.escape(key), x)]
        out.append(dict(line=i, key=key, want=want, got=got, bank_line=bl[0] if bl else None))
    return out


def _seam_rows():
    import licensed_table as LT
    f_seam, c_seam = _fact('seam')
    f_ch, c_ch = _fact('chrh')
    pr = [l for l in jl(K.SEAM_PRINT).get('lines') or [] if 'rh_strip_imp_rh_holds' in l or 'ch_iff_h2_sign\'' in l]
    of = tt_row('SIDE-explicit-formula', 'ch_iff_h2_sign_of_seam')
    full = tt_row('SIDE-explicit-formula', 'ch_iff_h2_sign')
    lic = ('rh_strip_imp_rh is a theorem: %s, its print %s (relay data/%s, b536 at v0.2 = 5c72cad); so ch_iff_h2_sign_of_seam (%s, grade %s by its '
           'statement form) has its premise discharged, and the equivalence holds with no premise as ch_iff_h2_sign (%s, grade %s)' % (
               f_seam, '; '.join(pr) or '?', K.SEAM_PRINT, EFP + 'PowerLimit.lean:1240', of['grade'], EFP + 'Seam.lean:107', full['grade']))
    cites = c_seam + [EFP + 'PowerLimit.lean:1240', EFP + 'Seam.lean:107', tt_cite('SIDE-explicit-formula', 'ch_iff_h2_sign'),
                      tt_cite('SIDE-explicit-formula', 'ch_iff_h2_sign_of_seam'), 'relay@%s:data/%s:1' % (PRE_RELAY, K.SEAM_PRINT)]
    S = []
    for (f, n), recut in zip(K.SEAM_ROWS, (
            'RE-CUT: **The seam equivalence** (`(R237)`(2)): ch_iff_h2_sign_of_seam is graded on its seam premise rh_strip_imp_rh by the seam principle and the table reads it INTERFACES by its statement form; that premise is a theorem -- rh_strip_imp_rh_holds compiles at the standard three (SIDE-explicit-formula Seam.lean :84, since v0.2 = 5c72cad) -- so the equivalence itself holds with no premise as ch_iff_h2_sign (Seam.lean :107, DERIVES).',
            'RE-CUT: SUPERSEDES OPEN_TRAILS :10884 for `ch_iff_h2_sign_of_seam`: INTERFACES by its statement form -- the node (SIDE-explicit-formula v0.22 = e939c92, PowerLimit.lean :1240, the statement rh_strip_imp_rh → (conservationHypothesis ↔ h2_sign)) takes its seam premise as a hypothesis; the premise is a theorem, rh_strip_imp_rh_holds (Seam.lean :84, standard three, since v0.2), and the unconditional equivalence is ch_iff_h2_sign (Seam.lean :107, DERIVES).')):
        st = lines_of(_show(PP, PRE_PP, f))[n - 1]
        S.append(dict(id='SEAM-%s-%d' % (f.split('.')[0], n), source='%s:%d' % (f, n), stated=st, licensed=lic, by='HAND',
                      cited=['PLACE-papers@6871ba2:%s:%d' % (f, n)] + cites, verdict='UNDERSTATES', action=recut, line=n, kind='seam'))
    for r in S:
        if LT.check(r):
            sys.exit('### THE SEAM ROW %s REFUSED: %s' % (r['id'], LT.check(r)))
    return S


def seam_map(*a):
    """data/b645_table_seam_map.txt and .json: (R255)(4)(a)-(b) -- the two seam rows read against rh_strip_imp_rh_holds and its print, each
    to one verdict with its ACTION; every row of THE_LOAD_BEARING_MAP read against the kernels at their pins, each to one verdict; the counts
    by verdict. The rows: the seam rows HAND; the map's rows HAND by line (MAP_HAND, ANCHOR_FACTS), the CP-1b items HAND through the facts
    their readings lean on, the count tables HAND against b558's bank, the page-pointer table by the `terminal` rule."""
    import licensed_table as LT
    rows = _map_rows()
    S = _seam_rows()
    M = []
    gen = dict((r['line'], r) for r in _b618_rows(rows))
    counts = dict((c['line'], c) for c in _count_rows(rows))
    for i, kind, sec, l in rows:
        base = dict(id='MAP-%d' % i, source='%s:%d' % (K.MAP, i), stated=l, line=i, kind=kind)
        if i in gen and i not in MAP_HAND:
            M.append(gen[i])
            continue
        if i in counts:
            c = counts[i]
            ok = c['got'] == c['want']
            M.append(dict(base, licensed='relay data/b558_cp1b.txt counts %s as STANDS %s, MOVED-IN-MEANING %s, CREDIT %s' % (
                c['key'], *(c['got'] or ('?', '?', '?'))), by='HAND', cited=[MAPC(i), 'relay@%s:data/b558_cp1b.txt:%s' % (PRE_RELAY, c['bank_line'])],
                verdict='MATCHES' if ok else 'OVERREACHES', action='none' if ok else 'RE-CUT: the counts %s' % (c['got'],)))
            continue
        if i in MAP_HAND:
            v, lic, fk, act = MAP_HAND[i]
            fx = [_fact(k) for k in fk]
            M.append(dict(base, licensed=lic + ((' -- ' + '; '.join(t for t, _c in fx)) if fx else ''), by='HAND',
                          cited=[MAPC(i)] + sum((c for _t, c in fx), []), verdict=v, action=act))
            continue
        if i in ANCHOR_FACTS:
            fx = [_fact(k) for k in ANCHOR_FACTS[i]]
            M.append(dict(base, licensed='the row`s cells read whole against its facts at their pins' + (
                (': ' + '; '.join(t for t, _c in fx)) if fx else ' (no fact beyond the row`s own printed statement and pin)'), by='HAND',
                cited=[MAPC(i)] + sum((c for _t, c in fx), []), verdict='MATCHES', action='none'))
            continue
        m = re.match(r"^- `([^`]+)` -- (\S+?):(\d+) -- (\*\".*?\"\*|\(not quoted.*?\)) -- (.*)$", l)
        if m and 232 <= i <= 418:
            fk = _reading_facts(m.group(5))
            if not fk:
                sys.exit('### THE CP-1b READING AT :%d NAMES NO FACT THE RUN READS -- NOTHING WRITTEN: %s' % (i, m.group(5)[:120]))
            fx = [_fact(k) for k in fk]
            M.append(dict(base, licensed='the reading stands on ' + '; '.join(t for t, _c in fx), by='HAND',
                          cited=[MAPC(i)] + sum((c for _t, c in fx), []), verdict='MATCHES', action='none'))
            continue
        sys.exit('### THE MAP ROW AT :%d (%s, %s) HAS NO READING -- NOTHING WRITTEN: %s' % (i, kind, sec[:40], l[:120]))
    allr = S + M
    cnt, faults = LT.table(allr)
    if faults:
        sys.exit('### THE TABLE REFUSED: %s' % list(faults.items())[:6])
    by_kind = collections.Counter((r['kind'], r['verdict']) for r in M)
    L = ['b645 -- COMPONENT 3, (R255)(4)(a)-(b): THE SEAM ROWS AND THE LOAD-BEARING MAP, EACH ROW TO ONE VERDICT (tools/licensed_table.py) (%s)' % utc(), '',
         '### the map: PLACE-papers %s at %s, %d rows (table %d, list items %d, claim paragraphs %d); the kernels at their pins: SIDE-explicit-formula '
         'v0.26 = 82550e4, SIDE-kernel v1.5 = 0e5233f, SIDE-lv-conservation v0.8.0 = 6efa9e5, SIDE-effects a27415d, SIDE-silence-principle '
         '667c254, SIDE-rcurve d5f33b4; the terminal table at relay %s' % (K.MAP, PRE_PP, len(M), sum(1 for r in M if r['kind'] == 'table'),
                                                                        sum(1 for r in M if r['kind'] == 'item'), sum(1 for r in M if r['kind'] == 'para'), PRE_RELAY),
         '### the facts the readings stand on, each read at the run from its table row (grade and statement) or its source at the pin:']
    for k in FACTS:
        t, c = _fact(k)
        L.append('    %-7s %s ; %s' % (k, t, ', '.join(c)))
    L += ['', '### (a) THE SEAM ROWS:']
    for r in S:
        L += ['  %s | %s' % (r['source'], r['verdict']), '    STATED   %s' % r['stated'], '    LICENSED %s' % r['licensed'],
              '    CITED    %s' % ', '.join(r['cited']), '    ACTION   %s' % r['action'], '']
    L += ['### (b) THE MAP, ROW BY ROW (SOURCE | KIND | BY | VERDICT ; STATED ; LICENSED ; CITED ; ACTION):']
    for r in M:
        L += ['  :%d | %s | %s | %s' % (r['line'], r['kind'], r['by'], r['verdict']), '    STATED   %s' % r['stated'][:700],
              '    LICENSED %s' % r['licensed'], '    CITED    %s' % ', '.join(r.get('cited') or ['(generated: %s)' % r['by']]),
              '    ACTION   %s' % r['action']]
    cs = LT.table(S)[0]
    cm = LT.table(M)[0]
    L += ['', '### BY KIND AND VERDICT: ' + ' ; '.join('%s %s %d' % (k, v, n) for (k, v), n in sorted(by_kind.items())),
          '### BY RULE: HAND %d ; terminal %d' % (sum(1 for r in allr if r['by'] == 'HAND'), sum(1 for r in allr if r['by'] == 'terminal')),
          '### THE SEAM ROWS: ' + ' ; '.join('%s %d' % kv for kv in cs.items()),
          '### THE MAP: ' + ' ; '.join('%s %d' % kv for kv in cm.items()),
          '', '### ### **ROWS %d (SEAM %d, MAP %d) ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d ; A ROW WITHOUT A VERDICT 0.**' % (
              len(allr), len(S), len(M), cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'])]
    put_txt('b645_table_seam_map.txt', L)
    put_json('b645_table_seam_map.json', dict(at=utc(), counts=cnt, seam=S, map=M))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE DOCSTRINGS, (R255)(4)(c)
DECL_RX = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*'
                     r'(theorem|lemma|def|abbrev|structure|class|inductive|instance|opaque|axiom)\s+([^\s:({\[]+)')


def _ef_files():
    """the kernel's own files at the pin: every .lean under SIDEExplicitFormula/ and the root module, and every other file that holds a row
    of the terminal table for the kernel (Zeta23/, Vendored/); the AxiomCheck files are print scripts and declare nothing."""
    rows, _md = _tt()
    tracked = [x for x in g(K.EF, 'ls-tree', '-r', '--name-only', K.EF_PIN).split(NL) if x.endswith('.lean')]
    own = set(x for x in tracked if x.startswith('SIDEExplicitFormula/') or x == 'SIDEExplicitFormula.lean')
    own |= set(x['statement_file'] for x in rows if x['repo'] == 'SIDE-explicit-formula' and x.get('statement_file') in tracked)
    return sorted(own)


def _docstrings(path, text):
    """[(kind, line, doc, decl keyword, decl name, decl line)] -- kind 'decl' for `/-- -/` before a declaration, 'module' for the file's
    `/-! -/` blocks and its head `/- -/` block before the first import."""
    out = []
    ls = text.split(NL)
    i = 0
    seen_import = False
    while i < len(ls):
        l = ls[i]
        s = l.lstrip()
        if s.startswith('import '):
            seen_import = True
        opener = '/--' if s.startswith('/--') else ('/-!' if s.startswith('/-!') else ('/-' if s.startswith('/-') and not seen_import and i < 5 else None))
        if opener:
            j = i
            while '-/' not in ls[j][(ls[j].find(opener) + len(opener)) if j == i else 0:]:
                j += 1
                if j >= len(ls):
                    break
            doc = NL.join(ls[i:j + 1])
            doc = re.sub(r'^\s*/-[-!]?', '', doc, count=1)
            doc = re.sub(r'-/\s*$', '', doc).strip()
            if opener == '/--':
                k = j + 1
                while k < len(ls) and (not ls[k].strip() or ls[k].lstrip().startswith(('@[', '--'))) and not DECL_RX.match(ls[k]):
                    k += 1
                m = DECL_RX.match(ls[k]) if k < len(ls) else None
                fm = re.match(r'^\s+([A-Za-z_][\w\']*)\s*:\s*(.*)$', ls[k]) if k < len(ls) else None
                if m:
                    out.append(('decl', i + 1, doc, m.group(1), m.group(2), k + 1))
                elif fm:
                    out.append(('field', i + 1, doc, 'field', fm.group(1), k + 1))
                else:
                    out.append(('decl', i + 1, doc, None, None, None))
            else:
                out.append(('module', i + 1, doc, None, None, None))
            i = j + 1
            continue
        i += 1
    return out


def _elab_index():
    """name -> (statement rendered, [explicit hypothesis binders]) from the elaborated bank at v0.26."""
    idx = {}
    cur, binders, concl = None, [], None
    for l in rd(K.ELAB_BANK).split(NL):
        if l.startswith('DECL '):
            cur, binders, concl = l.split()[1], [], None
        elif l.startswith('BINDER ') and cur:
            binders.append(l[len('BINDER '):])
        elif l.startswith('CONCL ') and cur:
            concl = l[len('CONCL '):]
        elif l == 'END' and cur:
            hyps = [b.split(' ', 1)[1] for b in binders if b.startswith('explicit ') and re.match(r'^explicit h\w*\s*:', b)]
            idx[cur] = ((' '.join('(%s)' % b.split(' ', 1)[1] for b in binders) + ' ⊢ ' + (concl or '')).strip(), hyps)
            cur = None
    return idx


def _ef_lookup():
    """lookup(name) -> (qualified name, grade) over the kernel's table rows: the qualified name, or a last component that names one row."""
    rows, _md = _tt()
    ef = [x for x in rows if x['repo'] == 'SIDE-explicit-formula']
    full = dict((x['name'], x) for x in ef)
    last = collections.defaultdict(list)
    for x in ef:
        last[x['name'].split('.')[-1]].append(x)

    def lookup(n):
        x = full.get(n) or (last[n.split('.')[-1]][0] if len(last.get(n.split('.')[-1], [])) == 1 else None)
        return (x['name'], x['grade']) if x else None
    return lookup, ef


def _doc_rows():
    import licensed_table as LT
    lookup, ef = _ef_lookup()
    ST = dict((r['head'], r['status']) for r in jl('b643_premise_table.json').get('rows') or [])
    PB = {}
    for x in ef:
        m = re.match(r'^theorem (\S+)\s*:\s*([\w.\'’]+)\s*$', re.sub(r'\s+', ' ', x['statement'] or '').strip())
        if m:
            PB.setdefault(m.group(2).split('.')[-1], '%s : %s (%s, grade %s)' % (x['name'], m.group(2), x['statement_file'], x['grade']))
    proved_by = lambda d: PB.get(d.split('.')[-1])   # noqa: E731
    by_file = collections.defaultdict(dict)
    for x in ef:
        if x.get('statement_file'):
            by_file[x['statement_file']].setdefault(x['name'].split('.')[-1], []).append(x)
    E = _elab_index()
    out = []
    for f in _ef_files():
        text = _show(K.EF, K.EF_PIN, f) or ''
        for kind, ln, doc, kw, name, dl in _docstrings(f, text):
            src = 'SIDE-explicit-formula@82550e4:%s:%d' % (f, ln)
            src_id = '%s:%d' % (f, ln)
            if kind == 'module':
                names = sorted(set(n for n, _s, _e in LT.names_in(doc)))
                hits = [(n, lookup(n)) for n in names]
                summ = '; '.join('%s %s' % (h[0].split('.')[-1], h[1]) for n, h in hits if h) or 'it names no row of the table'
                r = LT.docstring_row(src_id, src.replace('SIDE-explicit-formula@82550e4:', ''), doc, None, 'module', summ, None, None, [], lookup,
                                     module=True, status=ST.get)
                r.update(file=f, line=ln, kind='module', decl=None, grade=None)
                out.append(r)
                continue
            if kind == 'field':
                ft = re.sub(r'\s+', ' ', NL.join(text.split(NL)[dl - 1:dl + 3]).split('/--')[0]).strip()
                r = LT.docstring_row(src_id, src_id, doc, name, 'field', '%s (a structure field, read at the source, %s :%d)' % (ft, f, dl), 'DEF',
                                     'the field`s type', [], lookup, status=ST.get, proved_by=proved_by)
                r.update(file=f, line=ln, kind='field', decl=name, grade='DEF', decl_line=dl)
                out.append(r)
                continue
            if not name:
                sys.exit('### A DOCSTRING AT %s :%d BEFORE NO DECLARATION OR FIELD THE READER PARSES -- NOTHING WRITTEN' % (f, ln))
            cands = by_file.get(f, {}).get(name.split('.')[-1], [])
            x = cands[0] if len(cands) == 1 else None
            if x is None:
                # ### a declaration the table does not carry (an instance, a private helper, an upstream name): its keyword is its grade
                g_ = 'DEF' if kw in ('def', 'abbrev', 'structure', 'class', 'inductive', 'instance', 'opaque') else 'UNGRADED'
                hdr = NL.join(text.split(NL)[dl - 1:dl + 14])
                hdr = re.sub(r'\s+', ' ', hdr.split(':=')[0]).strip()
                st = (E.get(name) or ('%s (read at the source, %s :%d)' % (hdr, f, dl), []))[0]
                r = LT.docstring_row(src_id, src_id, doc, name, kw, st, g_, 'keyword, not in the table', [], lookup, status=ST.get, proved_by=proved_by)
                r.update(file=f, line=ln, kind='decl', decl=name, grade=g_, decl_line=dl)
                out.append(r)
                continue
            st, hyps = E.get(x['name'], (re.sub(r'\s+', ' ', x['statement'] or ''), []))
            r = LT.docstring_row(src_id, src_id, doc, x['name'], kw, st, x['grade'], x['provenance'], hyps, lookup, status=ST.get, proved_by=proved_by)
            r.update(file=f, line=ln, kind='decl', decl=x['name'], grade=x['grade'], decl_line=dl)
            out.append(r)
    return out


PT = 'relay@%s:data/b643_premise_table.txt:' % PRE_RELAY
MLB = 'mathlib4@de5ce8a9:Mathlib/'
# ### THE SEAT'S HAND READINGS OF THE DOCSTRING ROWS THE RULES FLAG (D1-D6), by row id: (verdict, licensed, cited, action)
DOC_HAND = {
    'SIDEExplicitFormula/KeiperIdentities.lean:1': (
        'MATCHES', 'three of the four obligations proved at every index (binomialTransform_holds, logDerivSplit_holds, stieltjesLog_holds); the '
        'header says the fourth is not proved and that KeiperObligations stays carried -- the premise table`s OPEN; "PROVED" is said of the three',
        [EFP + 'KeiperIdentities.lean:6', EFP + 'KeiperIdentities.lean:25', PT + '27'], MATCH),
    'SIDEExplicitFormula/PowerLimit.lean:1': (
        'MATCHES', 'h2_sign_imp_rh_of_seam : rh_strip_imp_rh → h2_sign_imp_rh (PowerLimit.lean :1236), compiled FROM the seam as the header '
        'says -- an INTERFACES claim; the header speaks of this module, which neither proves nor assumes the seam (Seam.lean :84 proves it)',
        [EFP + 'PowerLimit.lean:19', EFP + 'PowerLimit.lean:1236', EFP + 'Seam.lean:84'], MATCH),
    'SIDEExplicitFormula/Schema/WindowProofs.lean:1': (
        'MATCHES', 'windowObligations_holds W h : WindowObligations W h at every W and h (WindowProofs.lean :200, DERIVES); with it '
        'plateauRampWindow_of (PlateauRamp.lean :186) yields PlateauRampWindow W h under its domain binders 0 ≤ W and 0 < h alone -- '
        '"unconditionally" in the corpus`s sense, its one premise discharged (the premise table`s WindowObligations DISCHARGED)',
        [EFP + 'Schema/WindowProofs.lean:17', EFP + 'Schema/WindowProofs.lean:200', EFP + 'Schema/PlateauRamp.lean:186', PT + '48'], MATCH),
    'Zeta23/WeilEF/Main.lean:56': (
        'MATCHES', 'EF_lit_zeta (hs : ZetaSeam) : Zeta23.EF.EF_lit (zetaZeros hs) (Main.lean :67); "outright" is said of ExplicitFormulaPaper '
        '(zetaZeros hs), the object named under hs, and ZetaSeam is DISCHARGED in the premise table', [
            'SIDE-explicit-formula@82550e4:Zeta23/WeilEF/Main.lean:56', 'SIDE-explicit-formula@82550e4:Zeta23/WeilEF/Main.lean:67', PT + '50'], MATCH),
    'SIDEExplicitFormula/PowerWindow.lean:492': (
        'UNDERSTATES', 'rh_strip_imp_rh (PowerWindow.lean :495) is a theorem since v0.2 = 5c72cad: rh_strip_imp_rh_holds (Seam.lean :84, DERIVES '
        'at the standard three), its left half-plane through the kernel`s own zeta_zero_re_nonpos (Seam.lean :25); the Mathlib half stands -- '
        'Mathlib at the pin has the trivial zeros as zeros (riemannZeta_neg_two_mul_nat_add_one, RiemannZeta.lean :173) and no classification '
        'of the zeros with re ≤ 0 by name',
        [EFP + 'PowerWindow.lean:492', EFP + 'PowerWindow.lean:495', EFP + 'Seam.lean:84', EFP + 'Seam.lean:25',
         MLB + 'NumberTheory/LSeries/RiemannZeta.lean:173'],
        'RE-CUT: **The seam, a Prop:** from the strip form to Mathlib`s RH. It needs every Mathlib-nontrivial zero in the open strip: the right half-plane is Mathlib`s `riemannZeta_ne_zero_of_one_le_re`; the left half-plane (zeros with `re <= 0` are the trivial zeros), absent from Mathlib at this pin by name, is the kernel`s `zeta_zero_re_nonpos`. Proved: `rh_strip_imp_rh_holds` (Seam.lean).'),
    'SIDEExplicitFormula/H2Bridge.lean:86': (
        'UNDERSTATES', 'h2_sign_imp_ch (H2Bridge.lean :88) is a theorem since v0.2: h2_sign_imp_ch_holds (Seam.lean :104, DERIVES), through '
        'h2_sign_imp_ch_iff (H2Bridge.lean :91) and h2_sign_imp_rh_holds; Weil`s converse is no longer open at f4',
        [EFP + 'H2Bridge.lean:86', EFP + 'H2Bridge.lean:88', EFP + 'H2Bridge.lean:91', EFP + 'Seam.lean:104'],
        'RE-CUT: **The converse, a Prop:** `h2_sign` implies the Route 3 premise. By `h2_sign_imp_ch_iff` it is b513`s `h2_sign_imp_rh` -- Weil`s converse, W-ORD-WEIL-CONVERSE; proved: `h2_sign_imp_ch_holds` (Seam.lean).'),
    'SIDEExplicitFormula/RHChain.lean:75': (
        'UNDERSTATES', 'h2_sign_imp_rh (RHChain.lean :83) is a theorem since v0.2: h2_sign_imp_rh_holds (Seam.lean :98, DERIVES), from the seam '
        '(rh_strip_imp_rh_holds) through h2_sign_imp_rh_of_seam (PowerLimit.lean :1236); the witness construction the docstring describes is '
        'the route the kernel took (the power window, PowerLimit)',
        [EFP + 'RHChain.lean:75', EFP + 'RHChain.lean:83', EFP + 'Seam.lean:98', EFP + 'PowerLimit.lean:1236'],
        'RE-CUT: **The converse, stated at (R122)(2), proved at b536:** `h2_sign -> RH` needed a witness construction -- a test function in `classK` making zeroSide negative at an arbitrary off-line zero; the power window supplies it (PowerLimit.lean, `h2_sign_imp_rh_of_seam`) and the seam closes it (`h2_sign_imp_rh_holds`, Seam.lean).'),
    'SIDEExplicitFormula/Schema/PlateauRamp.lean:1': (
        'MATCHES', 'the D5 claims read against Mathlib at de5ce8a9: (O1) Real.fourier_mul_convolution_eq, Mathlib/Analysis/Fourier/Convolution.lean '
        ':119, integrable functions at real frequency, as the header says since b642; (O2) Mathlib`s smoothness of a convolution needs a ContDiff '
        'factor (HasCompactSupport.contDiff_convolution_left/_right, Calculus/ContDiff/Convolution.lean :423, :430) -- no lemma raises the '
        'order by one for a box, as the header says',
        [EFP + 'Schema/PlateauRamp.lean:19', MLB + 'Analysis/Fourier/Convolution.lean:119', MLB + 'Analysis/Calculus/ContDiff/Convolution.lean:423',
         MLB + 'Analysis/Calculus/ContDiff/Convolution.lean:430'], MATCH),
    'Vendored/Bulka/Lc/LiCriterion/XiOrderBridge.lean:25': (
        'MATCHES', 'the D5 claim read against Mathlib at de5ce8a9: its zeta bounds are local at s = 1 (ZetaAsymp.lean :375 onward, isBigO near '
        'one) -- no polynomial bound for ζ in the critical strip, as the header says',
        ['SIDE-explicit-formula@82550e4:Vendored/Bulka/Lc/LiCriterion/XiOrderBridge.lean:25', MLB + 'NumberTheory/Harmonic/ZetaAsymp.lean:375'], MATCH),
}


def docstrings(*a):
    """data/b645_table_docstrings.txt and .json: (R255)(4)(c) -- every docstring of SIDE-explicit-formula at v0.26 = 82550e4 (declaration
    docstrings and module header blocks of the kernel's own files) to one verdict, the LICENSED cell generated by `docstring`/`module`
    (tools/licensed_table.py), each row the rules flag read by the seat and written by hand (DOC_HAND); counts by verdict and by module;
    the positive control (PlateauRamp's header at v0.25) and the yield of each rule printed."""
    import licensed_table as LT
    R = _doc_rows()
    flagged = [r['id'] for r in R if r['verdict'] != 'MATCHES' or r.get('hand_needed')]
    miss = sorted(set(flagged) - set(DOC_HAND))
    extra = sorted(set(DOC_HAND) - set(flagged))
    if miss or extra:
        sys.exit('### FLAGGED ROWS WITHOUT A HAND READING %s ; HAND READINGS OF NO FLAGGED ROW %s -- NOTHING WRITTEN' % (miss, extra))
    out = []
    for r in R:
        if r['id'] in DOC_HAND:
            v, lic, cites, act = DOC_HAND[r['id']]
            h = dict(r, by='HAND', verdict=v, licensed=lic, cited=cites, action=act, generated_verdict=r['verdict'], generated_findings=r['findings'])
            h.pop('hand_needed', None)
            out.append(h)
        else:
            out.append(r)
    cnt, faults = LT.table(out)
    if faults:
        sys.exit('### THE TABLE REFUSED: %s' % list(faults.items())[:5])
    # ### the positive control: the founding case, PlateauRamp's header at v0.25 (8c51431), must be flagged
    lookup, _ef = _ef_lookup()
    pc_doc = _docstrings('x', _show(K.EF, '8c51431', 'SIDEExplicitFormula/Schema/PlateauRamp.lean'))[0][2]
    pc = LT.docstring_row('PC', 'x:1', pc_doc, None, 'module', 's', None, None, [], lookup, module=True)
    rule_yield = collections.Counter(f.split(':')[0] for r in R for f in r['findings'])
    bym = collections.defaultdict(collections.Counter)
    for r in out:
        bym[r['file'].rsplit('/', 1)[0] if '/' in r['file'] else r['file']][r['verdict']] += 1
    L = ['b645 -- COMPONENT 4, (R255)(4)(c): THE DOCSTRINGS OF SIDE-explicit-formula AT v0.26 = 82550e4, EACH TO ONE VERDICT (tools/licensed_table.py) (%s)' % utc(), '',
         '### the rows: every declaration docstring (`/-- -/`) and every module header block (`/-! -/`, and the head `/- -/` before the imports) '
         'in the kernel`s own files (%d files: SIDEExplicitFormula/ and the files of Zeta23/ and Vendored/ holding a table row); the LICENSED cell '
         'generated from the elaborated statement (relay data/%s) and the grade (relay data/terminal_table.json at %s), the premise statuses from '
         'relay data/b643_premise_table.json' % (len(_ef_files()), K.ELAB_BANK, PRE_RELAY),
         '### the rules (tools/licensed_table.py): D1 its own scope (unconditional on an INTERFACES row; open about itself on a DERIVES row); D2 a '
         'proof, interface or open word attached to a named declaration against its row; D3 the same against a premise head`s status; D4 an '
         'equivalence claimed of a one-direction statement; D5 a claim about Mathlib at the pin, flagged for a hand reading; D6 a Prop`s '
         'definition called unproved while a binder-free theorem concludes it',
         '### THE READER`S LINEAGE, EACH SHAPE`S YIELD PRINTED: the first shape (D1, D2 on backticked names) flagged 4 rows, all MATCHES by hand -- '
         'every docstring MATCHES, (N4) refuted in letter and the reader suspected; its planted cases re-run (relay data/b645_instrument.txt) and '
         'its POSITIVE CONTROL, the founding case, read MATCHES -- the reader could not see the shape it generalises (a claim about Mathlib`s '
         'scope). The second shape (D3, bare names, the negation guard) moved one flag (PairTerm`s "NOT PROVED" out, KeiperIdentities in); D4 '
         'flagged one row, a statement the reader had not read (repaired: the source`s statement read); D5 restored the founding shape (the '
         'control flagged, below); D6 found three docstrings of Props the kernel proves.',
         '### THE POSITIVE CONTROL: SIDEExplicitFormula/Schema/PlateauRamp.lean`s header at v0.25 = 8c51431 (its :19-:20, OPEN_TRAILS :13491) -> '
         'generated %s ; flagged for a hand reading: %s' % (pc['verdict'], pc.get('hand_needed') or '### NOT FLAGGED'),
         '### THE YIELD BY RULE (findings over all rows): ' + ' ; '.join('%s %d' % kv for kv in sorted(rule_yield.items())), '']
    L += ['### THE ROWS THE RULES FLAG, READ BY HAND (%d):' % len(DOC_HAND)]
    for r in out:
        if r['by'] == 'HAND':
            L += ['  %s | %s | generated %s -> HAND %s' % (r['id'], r['kind'], r['generated_verdict'], r['verdict'])]
            L += ['    FINDINGS %s' % ' || '.join(r['generated_findings'])]
            L += ['    STATED   %s' % re.sub(r'\s+', ' ', r['stated'])[:900], '    LICENSED %s' % r['licensed'],
                  '    CITED    %s' % ', '.join(r['cited']), '    ACTION   %s' % r['action'], '']
    L += ['### EVERY ROW (SOURCE | KIND | BY | VERDICT ; the LICENSED cell, generated):']
    for r in out:
        L.append('  %s | %s | %s | %s ; %s' % (r['id'], r['kind'], r['by'], r['verdict'], re.sub(r'\s+', ' ', r['licensed'])[:260]))
    L += ['', '### BY MODULE DIRECTORY AND VERDICT:'] + ['  %-44s %s' % (k, ' ; '.join('%s %d' % kv for kv in sorted(v.items())))
                                                          for k, v in sorted(bym.items())]
    L += ['', '### BY KIND: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(r['kind'] for r in out).items())),
          '### ### **ROWS %d ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d ; A ROW WITHOUT A VERDICT 0 ; HAND %d ; GENERATED %d.**' % (
              len(out), cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'], sum(1 for r in out if r['by'] == 'HAND'),
              sum(1 for r in out if r['by'] != 'HAND'))]
    put_txt('b645_table_docstrings.txt', L)
    put_json('b645_table_docstrings.json', dict(at=utc(), counts=cnt, control=dict(verdict=pc['verdict'], hand=pc.get('hand_needed')),
                                                 rule_yield=rule_yield, rows=out))
    print(L[-1])


# ================================================================================ COMPONENT 5: THE MONOGRAPH THROUGH THE INTAKE FORM, (R255)(4)(d)
CHUNKS = [(1, 460), (461, 841), (842, 1147), (1148, 1467), (1468, 1701), (1702, 1902), (1903, 2292), (2293, 2442), (2443, 2598),
          (2599, 2693), (2694, 2895), (2896, 3192)]
INTAKE_GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
RECUT_BY_FACT = {
    'F1': 'state RH as equivalent to the one open clause h2_sign (h2_sign_iff_rh, Seam.lean :101), not as conditional on it',
    'F2': 'say Route 3 compiles RH from its own restatement (ch_iff_rh, H2Bridge.lean :71): no route and no reduction',
    'F3': 'say conservation_of_spectra states (1 : ℚ)^s = 1; the n₄ = 0 reading is the paper`s argument, not the terminal`s content',
    'F4': 'say h1_complete_at_Phi certifies eight coupling facts at Φ and closes no clause on the strip (mellin_Phi_eq_zero_of_re_le_one)',
    'F5': 'name the terminals for what they state: Route 1 takes ConservationHypothesis; spectral_cannon is a fact on the line; neither reaches σ = 1/2',
    'F6': 'state partialPositivity_finiteRange with its premises (Bombieri–Lagarias, Voros, VerifiedZerosTo T)',
    'F7': 'state the registers at their depths: R1 false as stated, R2 RH restated, R4 equivalent to RH, R5`s output a theorem',
    'F8': 'name h2_sign and h2_sign_iff_rh as h2`s terminal',
    'F9': 'say the seam is compiled (rh_strip_imp_rh_holds, Seam.lean :84)',
    'F10': 'say the kernel checks the arithmetic 2 + 3 + 2 + 0 = 7; the classification is the paper`s argument',
    'F11': 'say the kernel counts a defined type (Fintype.card MechanismClass = 7); exhaustiveness at ξ is the paper`s argument, not compiled',
    'F12': 'state silence_universal with its premise I.is_universal',
    'F13': 'say the Lean form is the logical schema (modus tollens over an abstract domain); the Mechanism Theorem`s content is the paper`s argument',
    'F15': 'state GRH for a primitive χ ≠ 1 as equivalent to h2_sign_chi (h2_sign_chi_iff_grh_chi), not as conditional on it',
}


def _mono_lines():
    return lines_of(_show(PP, PRE_PP, K.MONO))


def _mono_chapter(ls):
    """line -> its chapter or section: the nearest `# ` heading above it, or the nearest `## ` heading in the appendices and back matter."""
    out, cur = {}, '(front matter)'
    for i, l in enumerate(ls, 1):
        if l.startswith('# ') and i < 1941:
            cur = l[2:].strip()[:70]
        elif l.startswith('## ') and i >= 1941:
            cur = l[3:].strip()[:70]
        out[i] = cur
    return out


def _intake_records():
    """the readers` records, parsed and checked: [(chunk, kind, fields)] and the faults."""
    recs, faults = [], []
    for n, (a, b) in enumerate(CHUNKS, 1):
        p = os.path.join(SP, 'intake_c%02d.tsv' % n)
        if not os.path.exists(p):
            faults.append('chunk %02d (:%d-:%d): no file' % (n, a, b))
            continue
        for k, raw in enumerate(io.open(p, encoding='utf-8').read().replace(chr(13), '').split(NL), 1):
            if not raw.strip():
                continue
            f = raw.split('\t')
            if f[0] == 'CLAIM' and len(f) >= 8:
                recs.append((n, 'CLAIM', dict(line=f[1].strip(), grade=f[2].strip(), stated_as=f[3].strip(), terminal=f[4].strip(),
                                              route=f[5].strip(), quote=f[6], reason='\t'.join(f[7:]).strip(), rec=k)))
            elif f[0] == 'SKIP' and len(f) >= 3:
                recs.append((n, 'SKIP', dict(line=f[1].strip(), reason='\t'.join(f[2:]).strip(), rec=k)))
            else:
                faults.append('chunk %02d record %d malformed: %r' % (n, k, raw[:120]))
    return recs, faults


# ### THE SEAT'S CORRECTIONS OF READERS' RECORDS, by row id: (grade, stated_as, reason) -- each after the seat's whole read of the row.
_R1U = ('the seat`s read (b645 defect (e), the brief`s F5): Route 1`s unconditional terminal is TheBridgeComplete`s structural_exhaustiveness_proved '
        '(SIDE-kernel v1.5 Bridge/TheBridgeComplete.lean :249, no hypothesis), a conjunction about defined types and σ-level identities; '
        'the sentence states that much')
_CLS = 'the seat`s read: a classical consequence of ξ real on the line, stated as the paper`s argument (F16)'
_RT = 'the seat`s read: "route terminals" is the corpus`s own repaired wording (E-2026-09-25-1), naming terminals without a route claim'
MONO_FIX = {
    'MONO-122-1-101': ('kernel-verified', 'graded', _RT),
    'MONO-122-1-103': ('kernel-verified', 'established', 'the seat`s read: SIDE-kernel v1.5 = 0e5233f, the tag`s commit (git rev-parse at the pin)'),
    'MONO-311-1-244': ('argument-supported', 'graded', _CLS), 'MONO-932-3-89': ('theorem-supported', 'graded', _CLS),
    'MONO-1350-4-188': ('argument-supported', 'graded', _CLS), 'MONO-1953-7-46': ('theorem-supported', 'graded', _CLS),
    'MONO-1598-5-128': ('kernel-verified', 'established', _R1U), 'MONO-1650-5-172': ('kernel-verified', 'established', _R1U),
    'MONO-1676-5-200': ('kernel-verified', 'established', _R1U), 'MONO-1692-5-225': ('kernel-verified', 'established', _R1U),
    'MONO-1694-5-228': ('kernel-verified', 'established', _R1U), 'MONO-2260-7-305': ('kernel-verified', 'established', _R1U),
    'MONO-2376-8-88': ('kernel-verified', 'established', _R1U), 'MONO-2771-11-81': ('kernel-verified', 'established', _R1U),
    'MONO-2772-11-82': ('kernel-verified', 'established', _R1U), 'MONO-2775-11-85': ('kernel-verified', 'established', _R1U),
    'MONO-2776-11-86': ('kernel-verified', 'established', _R1U),
    'MONO-1698-5-236': ('argument-supported', 'graded', 'the seat`s read: the corpus`s own retirement of an overstated gloss, stated as such'),
    'MONO-2356-8-64': ('kernel-verified', 'graded', _RT), 'MONO-2360-8-68': ('kernel-verified', 'graded', _RT),
    # ### chunk 01, read whole by the seat
    'MONO-107-1-85': ('statement-grade', 'open', 'the seat`s read: the table row marks its own count Definitional -- a definition of the paper`s terms'),
    'MONO-144-1-119': ('statement-grade', 'open', 'the seat`s read: a framing remark ("may"), no claim'),
    'MONO-150-1-123': ('statement-grade', 'open', 'the seat`s read: the paper`s naming of its third operation, a definition of its terms'),
    'MONO-168-1-140': ('theorem-supported', 'graded', 'the seat`s read: a historical fact of record (Riemann 1859)'),
    'MONO-242-1-199': ('synthesis-suggested', 'graded', 'the seat`s read: "closes" is a figure of the reading, not a proof claim; the wall at 9 is Størmer`s last pair (8, 9)'),
    'MONO-313-1-246': ('argument-supported', 'graded', 'the seat`s read: "closed-form" is no status claim; the paper`s own derivation'),
    'MONO-343-1-269': ('argument-supported', 'graded', 'the seat`s read: arithmetic over the paper`s own formation numbers (F10)'),
    'MONO-345-1-270': ('argument-supported', 'graded', 'the seat`s read: the paper`s own formation count, stated as its count (F10)'),
    'MONO-345-1-271': ('synthesis-suggested', 'graded', 'the seat`s read: an interpretive gloss of the paper`s silence reading, not a compile claim'),
    'MONO-437-1-341': ('kernel-verified', 'established', 'the seat`s read: C₁-C₅ DERIVE from the voice theorems (SIDE-kernel v1.5 Bridge/TheBridgeComplete.lean :225-:249, its docstring)'),
}
_PA = 'the seat`s read: the paper`s own argument, stated plainly as its argument -- no compile or proof-status claim'
_FR = 'the seat`s read: a framing of the method or its history; the status word is no status claim'
MONO_FIX.update({
    # ### chunk 02, read whole by the seat
    'MONO-492-2-23': ('synthesis-suggested', 'graded', _FR), 'MONO-536-2-53': ('argument-supported', 'graded', _PA),
    'MONO-552-2-61': ('argument-supported', 'graded', _FR), 'MONO-552-2-62': ('synthesis-suggested', 'graded', _FR),
    'MONO-556-2-65': ('synthesis-suggested', 'graded', _FR), 'MONO-565-2-72': ('synthesis-suggested', 'graded', _FR),
    'MONO-573-2-76': ('argument-supported', 'graded', _FR),
    'MONO-626-2-113': ('argument-supported', 'graded', 'the seat`s read: the syllogism`s premise schema in general form, not a claim about ξ'),
    'MONO-630-2-116': ('argument-supported', 'graded', 'the seat`s read: a claim about the syllogism`s logical form, which holds of the form'),
    'MONO-672-2-144': ('synthesis-suggested', 'graded', 'the seat`s read: the method`s report of its own test case, stated as its report'),
    'MONO-744-2-194': ('theorem-supported', 'graded', 'the seat`s read: the analytic continuation of ζ is a classical theorem (Riemann 1859)'),
    'MONO-770-2-211': ('argument-supported', 'graded', _PA), 'MONO-780-2-218': ('argument-supported', 'graded', _PA),
    'MONO-782-2-219': ('argument-supported', 'graded', _PA), 'MONO-784-2-220': ('argument-supported', 'graded', _PA),
    'MONO-794-2-228': ('argument-supported', 'graded', _PA), 'MONO-798-2-232': ('argument-supported', 'graded', _PA),
    'MONO-818-2-249': ('argument-supported', 'graded', _PA), 'MONO-832-2-263': ('argument-supported', 'graded', _PA),
    'MONO-834-2-267': ('statement-grade', 'open', 'the seat`s read: the Silence Principle`s scope as the paper defines it'),
    'MONO-836-2-268': ('argument-supported', 'graded', _PA),
})
_ST = ('the seat`s read: a stage-level or per-class verdict, the paper`s own argument stated as its argument; the global exhaustiveness '
       'of the catalogue at ξ (held open, F11) and any conclusion about ξ`s zeros are the rows that stand OVERREACHES')
_CL = 'the seat`s read: a classical theorem stated as such (F16)'
for _k in ('847-3-3', '849-3-4', '849-3-5', '849-3-7', '849-3-8', '851-3-9', '856-3-13', '858-3-14', '862-3-17', '862-3-18', '864-3-19',
           '864-3-20', '890-3-42', '894-3-46', '900-3-50', '900-3-52', '904-3-56', '906-3-59', '908-3-62', '916-3-69', '916-3-71', '924-3-78',
           '924-3-80', '926-3-81', '926-3-82', '928-3-86', '930-3-87', '932-3-90', '938-3-97', '939-3-98', '940-3-99', '943-3-102', '944-3-103',
           '946-3-104', '950-3-111', '954-3-113', '954-3-114', '954-3-115', '958-3-117', '964-3-121', '964-3-124', '968-3-127', '970-3-128',
           '976-3-132', '980-3-134', '980-3-135', '996-3-151', '996-3-153', '1011-3-170', '1020-3-175', '1031-3-183', '1059-3-199',
           '1069-3-208', '1114-3-241', '1138-3-274', '1138-3-275'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _ST)
for _k in ('916-3-70', '922-3-75', '932-3-91', '998-3-154', '1134-3-264', '1134-3-266', '1134-3-267'):
    MONO_FIX['MONO-' + _k] = ('theorem-supported', 'graded', _CL)
for _k in ('1167-4-13', '1173-4-24', '1197-4-53', '1210-4-71', '1211-4-72', '1219-4-81', '1225-4-86', '1229-4-88', '1233-4-91', '1256-4-107',
           '1271-4-120', '1404-4-223'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _ST)
for _k in ('1157-4-6', '1159-4-7', '1161-4-8', '1173-4-23', '1246-4-101', '1252-4-105'):
    MONO_FIX['MONO-' + _k] = ('theorem-supported', 'graded', 'the seat`s read: a classical construction or theorem (θ, the Mellin transform, the functional '
                                                             'equations, Tate`s thesis, the twisted Epstein off-line zeros of Davenport-Heilbronn type), stated as such')
MONO_FIX.update({
    'MONO-1227-4-87': ('statement-grade', 'open', 'the seat`s read: a statement about the document`s own list, which holds of it'),
    'MONO-1260-4-110': ('computationally-verified', 'established', 'the seat`s read: the quartic character mod 5 takes these values (2 is a generator)'),
    'MONO-1308-4-150': ('argument-supported', 'less', 'the seat`s read: "closes to a single open clause" -- Part III`s clause is RH itself (F1)'),
    'MONO-1314-4-157': ('kernel-verified', 'established', 'the seat`s read: C₁-C₅ DERIVE from the voice theorems (SIDE-kernel v1.5 Bridge/TheBridgeComplete.lean :225-:249)'),
})
_REC = 'the seat`s read: an edition record of a corpus check or ruling, stated as such and true of the corpus'
for _k in ('1537-5-65', '1539-5-69', '1539-5-70', '1541-5-72', '1553-5-84', '1586-5-120', '1658-5-178', '1670-5-194'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
for _k in ('1541-5-75', '1672-5-195', '1684-5-207', '1690-5-214'):
    MONO_FIX['MONO-' + _k] = ('statement-grade', 'open', 'the seat`s read: a scope statement of the document`s own table or section')
MONO_FIX.update({
    'MONO-1543-5-76': ('theorem-supported', 'graded', 'the seat`s read: Mathlib API facts at the pin (AnalyticOnNhd.eqOn_of_preconnected_of_eventuallyEq is a '
                                                      'declaration the explicit-formula kernel elaborates, relay data/b643_elab_ef.txt)'),
    'MONO-1567-5-98': ('kernel-verified', 'established', 'the seat`s read: `inductive Place` (SIDE-kernel v1.5 Kernel/Core.lean :24, Bridge/OstrowskiBridge.lean :34)'),
    'MONO-1668-5-189': ('theorem-supported', 'graded', 'the seat`s read: Lean facts -- `sorry` elaborates to sorryAx, `native_decide` to Lean.ofReduceBool'),
    'MONO-1672-5-197': ('argument-supported', 'graded', 'the seat`s read: ERRATA.md carries E-2026-09-22-1 (git grep, six lines)'),
    'MONO-1698-5-231': ('kernel-verified', 'established', 'the seat`s read: `theorem spectral_cannon` has one definition at v1.5 and main (Kernel/SpectralCannonFull.lean :65)'),
    'MONO-1698-5-234': ('kernel-verified', 'graded', 'the seat`s read: the sentence states the terminal`s content exactly ((deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0) before naming it'),
})
for _k in ('1709-6-5', '1713-6-10', '1723-6-22', '1725-6-24', '1727-6-26', '1727-6-27', '1764-6-50', '1784-6-80', '1784-6-81', '1788-6-87',
           '1825-6-182', '1827-6-195', '1827-6-196', '1850-6-218'):
    MONO_FIX['MONO-' + _k] = ('synthesis-suggested', 'graded', _FR)
for _k in ('1717-6-14', '1717-6-15', '1772-6-59', '1802-6-109', '1804-6-127', '1810-6-144', '1838-6-203'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
for _k in ('1794-6-96', '1868-6-242', '1870-6-243', '1878-6-251', '1889-6-263'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _ST)
MONO_FIX.update({
    'MONO-1717-6-17': ('statement-grade', 'open', 'the seat`s read: an absence stated as an absence, true (no ξ′ form is compiled)'),
    'MONO-1772-6-62': ('argument-supported', 'graded', 'the seat`s read: the GRH scope at primitive χ matches the compiled χ form`s premise (F15)'),
    'MONO-1794-6-99': ('kernel-verified', 'established', 'the seat`s read: the deposited kernel compiles (SIDE-kernel v1.5, its profiles in the terminal table)'),
    'MONO-1812-6-146': ('statement-grade', 'open', 'the seat`s read: the definition of Φ, the classical theta tail'),
    'MONO-1825-6-187': ('argument-supported', 'graded', 'the seat`s read: the line carries the corpus`s own correction, convergent and not independent'),
})
# ### the Route 1 rows the readers also marked route DARK: Route 1 is offered as compiled, not as a route reaching σ = 1/2 for ξ
for _k in ('MONO-1598-5-128', 'MONO-1650-5-172', 'MONO-1676-5-200', 'MONO-1692-5-225', 'MONO-1694-5-228', 'MONO-2260-7-305', 'MONO-2376-8-88'):
    MONO_FIX[_k] = MONO_FIX[_k][:3] + ('no',)
for _k in ('1915-7-12', '1925-7-0', '1927-7-25', '1954-7-47', '1967-7-58', '2042-7-120', '2050-7-126', '2233-7-255', '2233-7-257'):
    if _k != '1925-7-0':
        MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _ST)
for _k in ('1921-7-18', '2188-7-201', '2190-7-202', '2194-7-209', '2198-7-220', '2200-7-221', '2206-7-233'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
for _k in ('1927-7-23', '1929-7-27', '1951-7-44', '1952-7-45', '1958-7-51'):
    MONO_FIX['MONO-' + _k] = ('theorem-supported', 'graded', 'the seat`s read: a classical fact or a historical date of record, stated as such and true')
MONO_FIX.update({
    'MONO-1921-7-19': ('kernel-verified', 'established', 'the seat`s read: the deposited kernel compiles (SIDE-kernel v1.5)'),
    'MONO-1927-7-26': ('argument-supported', 'less', 'the seat`s read: "reduce the question to one located clause" -- the clause in its Weil form is RH itself (F1)'),
    'MONO-2198-7-216': ('kernel-verified', 'established', 'the seat`s read: SIDE-kernel v1.5 = 0e5233f, the tag`s commit'),
    'MONO-2250-7-292': ('argument-supported', 'graded', 'the seat`s read: true -- no kernel proves RH (F1, F2)'),
    'MONO-2254-7-299': ('argument-supported', 'graded', 'the seat`s read: true -- RH is not proved (F1)'),
})
for _k in ('2309-8-12', '2310-8-14', '2314-8-18', '2319-8-25', '2323-8-27', '2324-8-28', '2350-8-57', '2353-8-60', '2355-8-63', '2373-8-85'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
MONO_FIX['MONO-2390-8-104'] = ('kernel-verified', 'established', 'the seat`s read: the heat trace of {n²} at Φ is one of h1_complete_at_Phi`s eight coupling '
                                                                  'facts (SIDE-lv-conservation CouplingsAtPhi.lean :418; the map :126)')
for _k in ('2456-9-12', '2457-9-14', '2463-9-19', '2467-9-28', '2468-9-29', '2469-9-30', '2470-9-32', '2473-9-35', '2474-9-38', '2476-9-40',
           '2480-9-44', '2491-9-56', '2493-9-60', '2501-9-67', '2502-9-68', '2503-9-70', '2503-9-71', '2504-9-72', '2505-9-75', '2514-9-82',
           '2516-9-84', '2517-9-85', '2520-9-88', '2521-9-89', '2526-9-94', '2531-9-99', '2532-9-100', '2537-9-103', '2615-10-15', '2680-10-89'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
MONO_FIX['MONO-2493-9-59'] = ('kernel-verified', 'established', 'the seat`s read: C₁-C₅ DERIVE from the voice theorems (SIDE-kernel v1.5 '
                                                                'Bridge/TheBridgeComplete.lean :225-:249); the joint step stated open')
for _k in ('2630-10-31', '2633-10-35', '2635-10-38', '2637-10-40', '2645-10-50', '2651-10-58', '2656-10-63', '2675-10-82'):
    MONO_FIX['MONO-' + _k] = ('kernel-verified', 'established', 'the seat`s read: the record states Route 3`s premise as RH restated -- ch_iff_rh '
                                                                '(H2Bridge.lean :71), as the corpus reads it (F2)', 'no')
for _k in ('2763-11-73', '2765-11-75', '2778-11-88', '2780-11-90', '2790-11-100'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _REC)
for _k in ('2747-11-57', '2800-11-110'):
    MONO_FIX['MONO-' + _k] = ('argument-supported', 'graded', _ST)
_RH60 = ('the seat`s read: the corrected text scopes each compiled per-class exclusion as a condition on a real σ, the joint step RH restated '
         '(the sieve`s RH-60) -- what TheBridgeComplete`s conjunction states (SIDE-kernel v1.5 :225-:249)')
for _k in ('3009-12-88', '3063-12-122', '3065-12-124', '3072-12-131', '3086-12-145', '3103-12-163', '3104-12-165', '3106-12-168', '3110-12-173',
           '3116-12-178', '3117-12-179', '3124-12-187', '3129-12-193', '3135-12-199', '3137-12-202', '3142-12-207', '3143-12-208', '3149-12-212',
           '3181-12-234', '3182-12-235'):
    MONO_FIX['MONO-' + _k] = ('kernel-verified', 'graded', _RH60, 'no')
MONO_FIX.update({
    'MONO-2898-12-2': ('kernel-verified', 'established', 'the seat`s read: SIDE-kernel v1.5 = 0e5233f, the tag`s commit'),
    'MONO-2915-12-20': ('kernel-verified', 'established', 'the seat`s read: SIDE-global-section v0.1.0 resolves to 706a81b (git rev-parse)'),
    'MONO-2972-12-62': ('argument-supported', 'graded', _REC),
    'MONO-3007-12-86': ('computationally-verified', 'established', 'the seat`s read: a finite bench computation stated as such, offered toward no target', 'no'),
})
MONO_READ_CHUNKS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# ### THE MATCHES SAMPLE: 40 rows drawn with seed 645 from the MATCHES rows no correction had touched (25 the stated-as rule moved, 15 not),
# ### each read whole by the seat -- AGREE, or CORRECTED with its correction in MONO_FIX
MONO_SAMPLE = dict((k, 'AGREE') for k in (
    'MONO-118-1-93', 'MONO-166-1-138', 'MONO-250-1-204', 'MONO-317-1-252', 'MONO-437-1-340', 'MONO-536-2-51', 'MONO-595-2-89', 'MONO-607-2-99',
    'MONO-702-2-164', 'MONO-774-2-215', 'MONO-796-2-231', 'MONO-813-2-245', 'MONO-914-3-68', 'MONO-928-3-83', 'MONO-974-3-131', 'MONO-980-3-136',
    'MONO-1171-4-19', 'MONO-1376-4-202', 'MONO-1502-5-31', 'MONO-1580-5-114', 'MONO-1692-5-215', 'MONO-1876-6-249', 'MONO-2007-7-88',
    'MONO-2011-7-91', 'MONO-2066-7-134', 'MONO-2204-7-229', 'MONO-2248-7-291', 'MONO-2365-8-73', 'MONO-2366-8-74', 'MONO-2367-8-76',
    'MONO-2386-8-99', 'MONO-2634-10-37', 'MONO-2673-10-78', 'MONO-2689-10-99', 'MONO-2691-10-101', 'MONO-2701-11-8'))
MONO_SAMPLE.update(dict((k, 'CORRECTED') for k in ('MONO-118-1-96', 'MONO-725-2-181', 'MONO-1484-5-14', 'MONO-1634-5-159')))
MONO_FIX.update({
    'MONO-118-1-96': ('synthesis-suggested', 'established', 'the seat`s sample read: "no eighth class" is the catalogue`s global exhaustiveness at ξ, held open (F11)'),
    'MONO-725-2-181': ('synthesis-suggested', 'established', 'the seat`s sample read: "five independent closures" of the step to actual independence -- '
                                                             'a closure claim the corpus does not license (F11; the reading at :2696)'),
    'MONO-1484-5-14': ('synthesis-suggested', 'established', 'the seat`s sample read: a programme claim stated as fact, no argument or terminal on the line'),
    'MONO-1634-5-159': ('statement-grade', 'established', 'the seat`s sample read: a compile profile of a bridge file in the separate, unpinned '
                                                          'project (the reading at :1630)'),
})   # ### the chunks whose every non-MATCHES row the seat has read whole; a row there not in MONO_FIX stands as the reader graded it
# ### THE STATED-AS RULE (b645's defect (d), the brief's): the brief defined `established` as "stated as true, proved, verified or compiled",
# ### and a monograph states its own arguments and readings plainly; the mapping's (argument-supported | synthesis-suggested, established)
# ### means an argument or reading stated as proved, verified or a result, and (theorem-supported, established) a classical theorem presented
# ### as the programme's own compiled or proved result. So an argument-, synthesis- or theorem-grade row the reader marked
# ### `established` keeps it only where its quote claims a status beyond argument (STATUS_WORDS) or its reason names a corpus fact the claim
# ### conflicts with (F1-F13, F15); every other such row is read `graded` -- the paper`s own argument or reading, stated as such.
STATUS_WORDS = re.compile(r'(?i)\b(?:prov(?:ed|es|en|able)|proof|theorem|verif\w*|certif\w*|compil\w*|machine|Lean|kernel|ZFC|established|rigorous\w*|'
                          r'demonstrat\w*|confirm\w*|settled|unconditional\w*|closes?|closed|follows as)\b')


def _mono_rows():
    import licensed_table as LT
    ls = _mono_lines()
    chap = _mono_chapter(ls)
    recs, faults = _intake_records()
    lookup, _ef = _ef_lookup()
    rows_all, _md = _tt()
    tnames = collections.defaultdict(list)
    for x in rows_all:
        tnames[x['name'].split('.')[-1]].append(x)
    covered = collections.defaultdict(list)
    rows, skips = [], []
    for n, kind, r in recs:
        a, b = CHUNKS[n - 1]
        if not r['line'].isdigit() or not (a <= int(r['line']) <= b):
            faults.append('chunk %02d record %d: line %r outside :%d-:%d' % (n, r['rec'], r['line'], a, b))
            continue
        ln = int(r['line'])
        covered[ln].append(kind)
        if kind == 'SKIP':
            skips.append(dict(line=ln, reason=r['reason'], chunk=n))
            continue
        q = r['quote']
        if not (len(q) >= 8 and q in ls[ln - 1]):
            faults.append('chunk %02d record %d (:%d): the quote is not a substring of its line: %r' % (n, r['rec'], ln, q[:80]))
            continue
        rid = 'MONO-%d-%d-%d' % (ln, n, r['rec'])
        fix = MONO_FIX.get(rid)
        grade, sa, reason = (fix[:3] if fix else (r['grade'], r['stated_as'], r['reason']))
        if fix and len(fix) > 3:
            r = dict(r, route=fix[3])
        refined = False
        if not fix and grade in ('argument-supported', 'synthesis-suggested', 'theorem-supported') and sa == 'established' and not STATUS_WORDS.search(q) \
                and not re.search(r'\bF(?:[1-9]|1[0-3]|15)\b', reason):
            sa, refined = 'graded', True
        if grade not in INTAKE_GRADES:
            faults.append('chunk %02d record %d (:%d): grade %r' % (n, r['rec'], ln, grade))
            continue
        route = r['route'] if r['route'] in ('no', 'DARK', 'BRIGHT') else 'no'
        try:
            v = LT.map_intake(grade, sa, 'DARK' if route == 'DARK' else 'NOT A ROUTE')
        except KeyError:
            faults.append('chunk %02d record %d (:%d): the pair (%s, %s) is not in the mapping' % (n, r['rec'], ln, grade, sa))
            continue
        term = r['terminal'].strip('`') if r['terminal'] not in ('-', '') else ''
        tline = ''
        if term:
            hits = tnames.get(term.split('.')[-1]) or []
            tline = ('; its row: %s' % ' | '.join('%s %s %s' % (x['repo'], x['name'], x['grade']) for x in hits[:2])) if hits else \
                '; the terminal is no row of the terminal table'
        facts = sorted(set(re.findall(r'\bF(\d{1,2})\b', reason)), key=int)
        if v == 'MATCHES':
            act = 'none'
        elif v == 'UNLICENSED':
            act = 'RETIRE TO ERRATA: asserted with no kernel and no citation reaching it (%s); the v6.0 re-cut under (R255)(2) carries no such sentence' % grade
        else:
            rc = [RECUT_BY_FACT['F' + f] for f in facts if 'F' + f in RECUT_BY_FACT]
            act = 'RE-CUT: %s -- %s' % (q[:120], '; '.join(rc) if rc else 'state the claim at its grade (%s), %s' % (
                grade, 'saying what the corpus now licenses' if v == 'UNDERSTATES' else 'no more than its support carries'))
        rows.append(dict(id='MONO-%d-%d-%d' % (ln, n, r['rec']), source='%s:%d' % (K.MONO, ln), stated=q, line=ln, chunk=n, chapter=chap[ln],
                         licensed='intake: %s, stated as %s%s%s; the mapping (%s, %s) -> %s; %s' % (
                             grade, sa, (', terminal ' + term) if term else '', tline, grade, sa, v, reason),
                         by='intake', verdict=v, action=act, grade=grade, stated_as=sa, terminal=term, route=route, fixed=bool(fix), refined=refined))
    unc = [i for i, l in enumerate(ls, 1) if l.strip() and i not in covered]
    return rows, skips, faults, unc


MONO_READ = {}   # ### the seat's whole read of every non-MATCHES row and of the MATCHES sample: id -> 'AGREE' or the fix made (MONO_FIX)


def monograph(*a):
    """data/b645_table_monograph.txt and .json: (R255)(4)(d) -- A_Place_to_Stand_v5_18.md through the intake form of b628, every claim a row,
    the outcome-to-verdict mapping printed before the rows (and committed before the run, relay data/b645_instrument.txt); the readers'
    records (twelve helper readers of this session, one chunk each, the brief in the closing's record) checked -- every quote a substring
    of its line, every non-blank line a CLAIM or a SKIP with its reason, every pair in the mapping -- and every non-MATCHES row read whole by
    the seat; counts by verdict and by chapter; the OVERREACHES rows printed in full."""
    import licensed_table as LT
    rows, skips, faults, unc = _mono_rows()
    if faults or unc:
        sys.exit('### THE READERS` RECORDS CARRY %d FAULTS AND %d UNCOVERED LINES -- NOTHING WRITTEN: %s %s' % (len(faults), len(unc), faults[:3], unc[:10]))
    cnt, f2 = LT.table(rows)
    if f2:
        sys.exit('### THE TABLE REFUSED: %s' % list(f2.items())[:4])
    MONO_READ.clear()
    for r in rows:
        if r['id'] in MONO_SAMPLE:
            MONO_READ[r['id']] = 'SAMPLE ' + MONO_SAMPLE[r['id']]
        elif r['fixed']:
            MONO_READ[r['id']] = 'READ, CORRECTED'
        elif r['verdict'] != 'MATCHES' and r['chunk'] in MONO_READ_CHUNKS:
            MONO_READ[r['id']] = 'READ, STANDS'
    unread = [r['id'] for r in rows if r['verdict'] != 'MATCHES' and r['id'] not in MONO_READ]
    if unread:
        sys.exit('### %d NON-MATCHES ROWS NOT READ BY THE SEAT -- NOTHING WRITTEN: %s' % (len(unread), unread[:8]))
    miss = [k for k in MONO_SAMPLE if k not in set(r['id'] for r in rows)]
    if miss:
        sys.exit('### SAMPLE IDS WITH NO ROW %s -- NOTHING WRITTEN' % miss)
    bych = collections.OrderedDict()
    for r in sorted(rows, key=lambda x: x['line']):
        bych.setdefault(r['chapter'], collections.Counter())[r['verdict']] += 1
    sample = sorted(MONO_SAMPLE)
    agree = sum(1 for v in MONO_SAMPLE.values() if v == 'AGREE')
    L = ['b645 -- COMPONENT 5, (R255)(4)(d): THE MONOGRAPH THROUGH THE INTAKE FORM, EVERY CLAIM A ROW (tools/licensed_table.py) (%s)' % utc(), '',
         '### the document: PLACE-papers %s at %s, %d lines, sha256 %s' % (K.MONO, PRE_PP, len(_mono_lines()),
                                                                       hashlib_sha(_show(PP, PRE_PP, K.MONO))),
         '### the form: b628`s intake (relay tools/b628_record.py, `intake`: the six grades, the route through the sieve`s tests, a terminal and a '
         'pin for kernel-verified); the rows read by twelve helper readers of this session, one chunk each, from one brief (the seat`s, its facts '
         'F1-F17 the corpus`s licensed readings: the map`s CP-1b readings and the facts of relay data/b645_table_seam_map.txt); the verdict by the '
         'mapping alone, never by a reader; every non-MATCHES row read whole by the seat (%d corrected), and a sample of %d MATCHES rows '
         '(seed 645): %d agree, %d corrected -- the MATCHES count carries that rate of error over the rows no one has read' % (
             sum(1 for r in rows if r['fixed']), len(sample), agree, len(sample) - agree),
         '### the stated-as rule (the seat`s, b645 defect (d)): an argument-, synthesis- or theorem-grade row the reader marked `established` keeps it '
         'only where its quote claims a status beyond argument (%s) or its reason names a corpus fact it conflicts with (F1-F13, F15); else it reads '
         '`graded`. Rows it moved: %d. The brief`s F5 named one of two theorems called structural_exhaustiveness_proved; TheBridgeComplete`s is '
         'unconditional (defect (e)); the rows read on it corrected by hand.' % (STATUS_WORDS.pattern[:80], sum(1 for r in rows if r.get('refined'))), '']
    L += ['### THE MAPPING, PRINTED BEFORE THE RUN ((grade, stated as) -> verdict):'] + ['    %-26s %-12s -> %-12s %s' % m for m in LT.MAPPING] + ['']
    L += ['### EVERY ROW (line | chapter | grade | stated as | terminal | route | VERDICT ; the quote ; the ACTION):']
    for r in sorted(rows, key=lambda x: (x['line'], x['id'])):
        L.append('  :%d | %s | %s | %s | %s | %s | %s ; "%s" ; %s' % (r['line'], r['chapter'][:40], r['grade'], r['stated_as'], r['terminal'] or '-',
                                                                  r['route'], r['verdict'], r['stated'][:200], r['action'][:220]))
    L += ['', '### THE SKIPS (line | reason), %d:' % len(skips)] + ['  :%d | %s' % (s['line'], s['reason'][:120]) for s in sorted(skips, key=lambda x: x['line'])]
    L += ['', '### BY CHAPTER AND VERDICT:'] + ['  %-72s %s' % (c, ' ; '.join('%s %d' % kv for kv in sorted(v.items()))) for c, v in bych.items()]
    L += ['', '### THE ROWS READING OVERREACHES, IN FULL (for the author, at the closing):']
    for r in sorted(rows, key=lambda x: x['line']):
        if r['verdict'] == 'OVERREACHES':
            L += ['  :%d (%s) -- STATED "%s"' % (r['line'], r['chapter'][:50], r['stated']), '      LICENSED %s' % r['licensed'], '      ACTION %s' % r['action']]
    brief = rd_sp('intake_brief.md')
    if not brief:
        sys.exit('### THE READERS` BRIEF IS NOT IN THE SCRATCHPAD -- NOTHING WRITTEN')
    L += ['', '### THE READERS` BRIEF, AS THEY READ IT (the scratchpad`s intake_brief.md, sha256 %s):' % hashlib_sha(brief)] + \
        ['    ' + l for l in brief.rstrip(NL).split(NL)]
    L += ['', '### ### **CLAIMS %d ; SKIPPED LINES %d ; MATCHES %d ; UNDERSTATES %d ; OVERREACHES %d ; UNLICENSED %d ; A ROW WITHOUT A VERDICT 0 ; '
              'UNCOVERED LINES 0.**' % (len(rows), len(set(s['line'] for s in skips)), cnt['MATCHES'], cnt['UNDERSTATES'], cnt['OVERREACHES'], cnt['UNLICENSED'])]
    put_txt('b645_table_monograph.txt', L)
    put_json('b645_table_monograph.json', dict(at=utc(), counts=cnt, rows=rows, skips=skips, by_chapter=dict((k, dict(v)) for k, v in bych.items()),
                                                read=MONO_READ))
    print(L[-1])


def hashlib_sha(t):
    import hashlib
    return hashlib.sha256((t or '').encode('utf-8')).hexdigest()


def mono_check(*a):
    """prints the validation of the readers' records -- faults, uncovered lines, counts -- and writes nothing."""
    rows, skips, faults, unc = _mono_rows()
    print('  rows %d ; skips %d ; faults %d ; uncovered non-blank lines %d' % (len(rows), len(skips), len(faults), len(unc)))
    for f in faults[:40]:
        print('  FAULT ' + f)
    print('  UNCOVERED: %s' % unc[:60])
    print('  BY VERDICT: %s' % dict(collections.Counter(r['verdict'] for r in rows)))
    print('  BY CHUNK: %s' % dict(collections.Counter(r['chunk'] for r in rows)))


# ================================================================================ COMPONENT 6: THE THREE COLUMNS, (R255)(5)
CLUSTER_HAND = {}   # ### registry id -> (cluster, the lines read cited), for a keystone neither rule places


def _roster():
    """the census roster's keystones (relay data/b644_census_roster.txt): (row, tier, id, REGISTRY line, heading phase), each with its
    file read from its REGISTRY line at PLACE-papers before the act."""
    reg = lines_of(_show(PP, PRE_PP, 'REGISTRY.md'))
    out = []
    for l in rd('b644_census_roster.txt').split(NL):
        m = re.match(r'^  (R\d\d) (\w+)\s+(\S+)\s+REGISTRY :(\d+)\s+heading `.*?` \(phase ([^,]+), cluster ([^)]+)\)', l)
        if not m:
            continue
        row = reg[int(m.group(4)) - 1]
        fs = [a or b for a, b in re.findall(r'`([^`]+\.md)`|([\w./-]+\.md)', row)]
        path = fs[0] if fs else ''
        pm = re.match(r'^(day1|phase1\.5|phase2)/', path)
        out.append(dict(row=m.group(1), tier=m.group(2), id=m.group(3), reg_line=int(m.group(4)), heading_phase=m.group(5).strip(),
                        phase={'day1': '1', 'phase1.5': '1.5', 'phase2': '2'}[pm.group(1)] if pm else '-',
                        reg_cluster=m.group(6).strip(), path=path, superseded=bool(re.search(r'SUPERSEDED', row))))
    return out


def columns(*a):
    """data/b645_census_columns.txt and .json: (R255)(5) -- CLUSTER by the rule over each keystone's path and terminals (HAND where neither
    places it), PHASE the phase directory of its path as a field (day1 1, phase1.5 1.5, phase2 2, any other directory -), the roster's
    REGISTRY-heading phase printed beside it, MATURITY by the rule printed before it runs, applied to the monograph (d1-1) and to
    SIDE-explicit-formula alone, every other keystone blank and marked; no census edition."""
    import licensed_table as LT
    K_ = _roster()
    if len(K_) != 48:
        sys.exit('### THE ROSTER READ %d KEYSTONES, NOT 48 -- NOTHING WRITTEN' % len(K_))
    M = jl('b645_table_monograph.json')
    Dc = jl('b645_table_docstrings.json')
    if not M.get('counts') or not Dc.get('counts'):
        sys.exit('### THE MONOGRAPH OR DOCSTRING TABLE IS NOT BANKED -- NOTHING WRITTEN')
    mono_open = sum(1 for r in M.get('rows') or [] if r.get('stated_as') == 'open')
    ST = dict((r['head'], r['status']) for r in jl('b643_premise_table.json').get('rows') or [])
    lookup, ef = _ef_lookup()
    ef_open = sum(1 for x in ef if x['grade'] == 'INTERFACES' and any(ST.get(h) == 'OPEN' for h in
                                                                       re.findall(r'\b([A-Z]\w+)\b', x['statement'] or '')))
    L = ['b645 -- COMPONENT 6, (R255)(5): THE CENSUS`S CLUSTER, PHASE AND MATURITY COLUMNS, DEFINED AND BANKED FOR v0.8 -- NO EDITION (%s)' % utc(),
         ''] + LT.rules()[-(len(LT.PATH_RULES) + len(LT.TERMINAL_SETS) + 5):] + [
        '', '### the rules above were printed in relay data/b645_instrument.txt and committed before this run; the cluster rule`s planted paths '
            'are its cases (17)-(18).', '',
        '### THE KEYSTONES (row | tier | id | path | PHASE | CLUSTER (how) | MATURITY (why)):']
    J = []
    for k in K_:
        t = _show(PP, 'HEAD', k['path']) or ''
        names = set(re.findall(r'`(?:[\w.]+\.)?([A-Za-z_][\w\'₀-₉]*)`', t))
        c, how = LT.cluster(k['path'], names)
        if not c and k['id'] in CLUSTER_HAND:
            c, cites = CLUSTER_HAND[k['id']]
            how = 'HAND: ' + ', '.join(cites)
        if k['id'] == 'd1-1':
            mat, why = LT.maturity(M['counts'], open_rows=mono_open, superseded=False)
            why += ' (relay data/b645_table_monograph.txt: %s ; stated open %d)' % (
                ', '.join('%s %d' % kv for kv in M['counts'].items()), mono_open)
        else:
            mat, why = LT.maturity(None)
        J.append(dict(k, cluster=c, how=how, maturity=mat, why=why))
        L.append('  %s | %-2s | %-46s | %-58s | %-4s (heading %-3s) | %-15s (%s) | %s (%s)' % (
            k['row'], k['tier'], k['id'][:46], k['path'][:58], k['phase'], k['heading_phase'], c or '### BLANK', how[:60], mat or '### BLANK', why))
    mat, why = LT.maturity(Dc['counts'], open_rows=ef_open)
    ef_row = dict(row='§1A', tier='kernel', id='SIDE-explicit-formula v0.26 = 82550e4', path='D:/SIDE-explicit-formula', phase='1',
                  cluster=LT.cluster('', set(x['name'].split('.')[-1] for x in ef))[0] or 'reduction-chain', how='terminals', maturity=mat,
                  why=why + ' (relay data/b645_table_docstrings.txt: %s ; theorems at INTERFACES on an OPEN premise %d)' % (
                      ', '.join('%s %d' % kv for kv in Dc['counts'].items()), ef_open))
    ef_row['how'] = 'terminals: ' + LT.cluster('', set(x['name'].split('.')[-1] for x in ef))[1]
    J.append(ef_row)
    L.append('  %s | %s | %s | %s | %s | %s (%s) | %s (%s)' % (ef_row['row'], ef_row['tier'], ef_row['id'], ef_row['path'], ef_row['phase'],
                                                           ef_row['cluster'], ef_row['how'][:80], ef_row['maturity'], ef_row['why']))
    blank_c = [x['id'] for x in J if not x['cluster']]
    L += ['', '### BY CLUSTER: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['cluster'] or 'BLANK' for x in J).items())),
          '### BY PHASE: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['phase'] for x in J).items())),
          '### BY MATURITY: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['maturity'] or 'BLANK (NOT YET IN THE TABLE)' for x in J).items())),
          '### HOW THE CLUSTER WAS PLACED: ' + ' ; '.join('%s %d' % kv for kv in sorted(collections.Counter(x['how'].split(':')[0] for x in J).items())),
          '', '### ### **KEYSTONES %d AND THE KERNEL ; CLUSTER PLACED %d, BLANK %d %s ; MATURITY ASSIGNED %d, BLANK AND MARKED %d ; NO BLANK COUNTED AS A VALUE.**' % (
              len(K_), sum(1 for x in J if x['cluster']), len(blank_c), blank_c or '', sum(1 for x in J if x['maturity']),
              sum(1 for x in J if not x['maturity']))]
    put_txt('b645_census_columns.txt', L)
    put_json('b645_census_columns.json', dict(at=utc(), rows=J, rule=LT.MATURITY_RULE))
    print(L[-1])


def doc_scan(*a):
    """prints the docstring rows the rule flags (UNDERSTATES, OVERREACHES), each with its findings, for the seat's whole read; writes nothing."""
    R = _doc_rows()
    c = collections.Counter(r['verdict'] for r in R)
    print('  rows %d ; by kind %s ; by verdict %s' % (len(R), dict(collections.Counter(r['kind'] for r in R)), dict(c)))
    for r in R:
        if r['verdict'] != 'MATCHES':
            print('=== %s | %s | %s | grade %s' % (r['id'], r['kind'], r['verdict'], r.get('grade')))
            for fnd in r['findings']:
                print('    ' + fnd)
            print('    DOC: ' + re.sub(r'\s+', ' ', r['stated'])[:900])


def act_from():
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            if 'RULING (R255) BEGIN' in raw and '"type":"user"' in raw.replace(' ', ''):
                return i
    return 10 ** 9


def answers(*a):
    """data/b645_author_answers.txt: every prompt put by the seat in this act, banked verbatim with the options and the recommended mark."""
    R3.act_from = act_from
    since, results = R3._calls()
    n = sum(len(c[2].get('questions', [])) for c in since)
    L = ['### b645 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat in this act (%s), banked verbatim with the options and the recommended '
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
    put_txt('b645_author_answers.txt', L)
    print('  prompts banked: %d' % n)


def hold_preseal(*a):
    """data/b645_hold_preseal.txt and .json: the author's answer at step zero -- RestrictedTensorLayer1 and test_elab_reader_b634 retried once
    more just before the seal, the hold at 2,560 MB; a second fall is final and named in the closing."""
    L = ['b645 -- THE HOLD, RETRIED ONCE MORE BEFORE THE SEAL (the author`s answer at step zero; data/b645_author_answers.txt) (%s)' % utc(), '']
    J = []
    for t, tag in (('RestrictedTensorLayer1', 'b645_build_RestrictedTensorLayer1_preseal'), (K.HOLD_TEST, 'b645_test_elab_preseal')):
        o = _log_outcome('%s/w_%s.log' % (SP, tag))
        fb = re.search(r'free before: (\d+) MB', rd_sp('launch_out_%s.txt' % tag))
        if t == K.HOLD_TEST and o['verdict'] == 'BUILT':
            o['verdict'] = 'RAN'
        J.append(dict(target=t, tag=tag, free_before=int(fb.group(1)) if fb else None, **o))
        L.append('  %-24s free before %s MB ; %-16s starts %d ; stopped %d ; lows %s ; lowest sample %s%s' % (
            t, J[-1]['free_before'], o['verdict'], o['starts'], o['stops'], o['lows'] or '-', o['samples_min'],
            (' ; errors: ' + ' | '.join(o['errors'])) if o['errors'] else ''))
    final = [r['target'] for r in J if r['verdict'] == 'RUN-BENEATH-HOLD']
    L += ['', '### ### **RETRIED 2 ; RUN-BENEATH-HOLD, FINAL AND NAMED IN THE CLOSING: %s.**' % (', '.join(final) or 'NONE')]
    put_txt('b645_hold_preseal.txt', L)
    put_json('b645_hold_preseal.json', dict(at=utc(), rows=J, final=final))
    print(NL.join(L[2:]))


def outsiders(*a):
    """data/b645_outsider_roster.txt and .json: (R255)(7) and the author's answer before b645's seal -- each of the 25 local repositories
    outside the chain (b644's closing) takes one word by a printed reading, none by the seat's judgment: JOINS if it builds at its pin (a
    banked print of its declarations, read from the terminal table's profiled rows) and a keystone or a kernel cites it by name (the citing
    line printed); RETIRES if a ruling or an ERRATA entry retired it (the line printed); STANDS ASIDE otherwise. A clone whose remote is a
    chain repository's is printed as such and stands aside (the repository is in the chain already). The private repository stands aside,
    unnamed. The chain is not widened; the author's word at the closing replaces any reading it strikes."""
    sec = _need(r'^### FOR THE AUTHOR TO NAME.*?(?=^### CARRIED FORWARD)', rd('b644_closing.txt'), 'the outsiders` section').group(0)
    outs = re.findall(r'^      (D:/\S+)\s+(\S+(?: REMOTE)?) ;', sec, re.M)
    if len(outs) != 25:
        sys.exit('### %d OUTSIDERS READ, NOT 25 -- NOTHING WRITTEN' % len(outs))
    chain = sorted(set(x.split()[0] for x in jl('b644_act_root.json').get('items') or [] if not x.startswith('data/')))
    remotes = dict(('https://github.com/psinary-sketch/%s.git' % c, c) for c in chain)
    kpaths = [k['path'] for k in _roster() if k['path']]
    rows_all, _md = _tt()
    texts = {'FINDINGS.md': lines_of(_show(PP, PRE_PP, 'FINDINGS.md')), 'OPEN_TRAILS.md': lines_of(_show(PP, PRE_PP, 'OPEN_TRAILS.md')),
             'ERRATA.md': lines_of(_show(PP, PRE_PP, 'ERRATA.md')), 'REGISTRY.md': lines_of(_show(PP, PRE_PP, 'REGISTRY.md'))}
    L = ['b645 -- (R255)(7): THE OUTSIDER REPOSITORIES, EACH WORD BY A PRINTED READING (the author`s answer before the seal) (%s)' % utc(), '',
         '### the 25 from relay data/b644_closing.txt; the chain`s %d repositories from b644`s root (relay data/b644_act_root.json); the keystones '
         'are the census roster`s 48 paths at PLACE-papers HEAD, the kernels the chain`s SIDE repositories at HEAD, searched by git grep for the '
         'repository`s name as a whole word' % len(chain),
         '### the retirement matcher`s lineage, each form`s yield: a line naming the repository and "retir" anywhere -- 3 (FINDINGS :7304, '
         'OPEN_TRAILS :7345, FINDINGS :1225, each read whole: each retires something else); the two within 60 characters -- 1 (FINDINGS :1225, '
         'a title retired, the repository only in its path); the repository itself the object ("<name> is/was retired", "retired the '
         'repository <name>") -- 0, the form banked', '']
    J = []
    for path, remote in outs:
        name = path.rstrip('/').split('/')[-1]
        if path.endswith('/repo'):
            name = remote.rstrip('/').split('/')[-1].replace('.git', '')
        clone = remotes.get(remote)
        cite = ''
        if not clone and remote != 'NO':
            for kp in kpaths:
                h = g(PP, 'grep', '-n', '-w', '-F', name, 'HEAD', '--', kp).strip().split(NL)[0]
                if h:
                    cite = 'PLACE-papers ' + h[len('HEAD:'):][:200]
                    break
            if not cite:
                for c in chain:
                    if c.startswith('SIDE-'):
                        h = g('D:/' + c, 'grep', '-n', '-w', '-F', name, 'HEAD', '--', '*.lean', '*.md').strip().split(NL)[0]
                        if h:
                            cite = '%s %s' % (c, h[len('HEAD:'):][:200])
                            break
        prof = [x for x in rows_all if x['repo'] == name and x.get('profile_state') == 'PROFILED']
        ret = ''
        for f, ls in texts.items():
            nm = r'(?<![\w-])%s(?![\w-])' % re.escape(name)
            prox = re.compile(r'(?i)%s`?\s+(?:is|was|stands|has been)\s+retired|\bretir\w*\s+(?:the\s+)?(?:repository|repo|clone|kernel)\s+`?%s' % (nm, nm))
            for i, l in enumerate(ls, 1):
                m = prox.search(l)
                if m:
                    ret = '%s :%d ...%s...' % (f, i, l[max(0, m.start() - 40):m.end() + 40])
                    break
            if ret:
                break
        if clone:
            word, why = 'STANDS ASIDE', 'a clone whose remote is the chain repository %s`s -- the repository is in the chain already' % clone
        elif ret:
            word, why = 'RETIRES', 'retired: %s' % ret
        elif cite and prof:
            word, why = 'JOINS', 'cited: %s ; builds at its pin: %d profiled rows in the terminal table (%s)' % (cite, len(prof), prof[0].get('profile_source'))
        else:
            word, why = 'STANDS ASIDE', 'cited: %s ; a build at a pin read: %s' % (cite or 'NO keystone or kernel names it',
                                                                                 ('%d profiled rows' % len(prof)) if prof else 'NONE')
        J.append(dict(path=path, remote=remote, name=name, word=word, why=why, cite=cite, profiled=len(prof), clone=clone, retired=ret))
        L.append('  %-38s %-13s %s' % (path, word, why))
    L += ['  %-38s %-13s %s' % ('(one private repository, unnamed)', 'STANDS ASIDE', 'the b590 rule: its name withheld')]
    c = collections.Counter(x['word'] for x in J)
    L += ['', '### ### **OUTSIDERS 25 AND ONE PRIVATE ; JOINS %d ; RETIRES %d ; STANDS ASIDE %d AND THE PRIVATE ONE ; THE CHAIN NOT WIDENED THIS ACT.**' % (
        c['JOINS'], c['RETIRES'], c['STANDS ASIDE'])]
    put_txt('b645_outsider_roster.txt', L)
    put_json('b645_outsider_roster.json', dict(at=utc(), rows=J))
    print(NL.join(L[4:]))


def agenda(*a):
    """data/b645_v6_agenda.txt: the author's answer before b645's seal -- the monograph's OVERREACHES and UNLICENSED rows, grouped by chapter,
    the re-cut sentence or the work-order beside each: v6.0's agenda, a file sent to the author at the closing, read before any re-cut is ruled."""
    M = jl('b645_table_monograph.json')
    rows = [r for r in M.get('rows') or [] if r['verdict'] in ('OVERREACHES', 'UNLICENSED')]
    if not rows:
        sys.exit('### THE MONOGRAPH TABLE IS NOT BANKED -- NOTHING WRITTEN')
    by = collections.OrderedDict()
    for r in sorted(rows, key=lambda x: x['line']):
        by.setdefault(r['chapter'], []).append(r)
    L = ['b645 -- v6.0`S AGENDA: THE MONOGRAPH`S OVERREACHES AND UNLICENSED ROWS, BY CHAPTER, EACH WITH ITS RE-CUT OR WORK-ORDER (%s)' % utc(), '',
         '### from relay data/b645_table_monograph.json (A_Place_to_Stand_v5_18.md at PLACE-papers %s); the author`s answer before b645`s seal: '
         'these go to the author as a file at b645`s closing, read before any re-cut is ruled; under (R255)(2) the next edition is v6.0, a re-cut. '
         'An ACTION`s re-cut names what the sentence must say; its wording is the edition`s.' % PRE_PP, '',
         '### OVERREACHES %d ; UNLICENSED %d ; CHAPTERS %d' % (sum(1 for r in rows if r['verdict'] == 'OVERREACHES'),
                                                             sum(1 for r in rows if r['verdict'] == 'UNLICENSED'), len(by)), '']
    for ch, rs in by.items():
        L.append('## %s (%d)' % (ch, len(rs)))
        for r in rs:
            L += ['  :%d  %s  [%s, stated as %s%s]' % (r['line'], r['verdict'], r['grade'], r['stated_as'], (', terminal ' + r['terminal']) if r['terminal'] else ''),
                  '      "%s"' % r['stated'], '      ACTION: %s' % r['action']]
        L.append('')
    L += ['### ### **ROWS %d ; CHAPTERS %d.**' % (len(rows), len(by))]
    put_txt('b645_v6_agenda.txt', L)
    print(L[-1])


def rd_sp(name):
    p = os.path.join(SP, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b645_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
