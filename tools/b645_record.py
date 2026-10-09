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


def hold_launch(target):
    """writes the PowerShell launcher for ONE call under tools/build_watch.py (scratchpad) and prints its path: an Interfaces module's build
    (b644's command, its mathlib4 checkout and output directory) or the reader's test (through b645_tests.py); the bank data/b645_build_watch.json."""
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


def rd_sp(name):
    p = os.path.join(SP, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


if __name__ == '__main__':
    args = [x for x in sys.argv[1:] if x != 'dry']
    if not args or args[0] not in globals() or args[0].startswith('_'):
        print('usage: b645_record.py <subcommand> [args] [dry]')
        sys.exit(2)
    globals()[args[0]](*args[1:])
