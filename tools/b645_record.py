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
    return ('`%s` (%s, read at the pin: %s)' % (name, decl.split(':')[0], needle), [decl])


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
    52: ('OVERREACHES', 'Route 1`s structural_exhaustiveness_proved takes ConservationHypothesis (h_cons) at v1.5 -- not unconditional; Route 2`s '
         'spectral_cannon is no sub-RH statement; Route 3`s premise is RH restated', ['route1', 'cannon', 'route3', 'chrh'],
         'RE-CUT: | MONO | DOWNSTREAM — no route independent of RH | R1 `structural_exhaustiveness_proved` takes ConservationHypothesis, RH restated (`ch_iff_rh`); R2 `spectral_cannon` is a fact on the line, no route to σ = 1/2; R3 `riemann_hypothesis(h_cons)` encodes its conclusion |'),
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
    75: ('OVERREACHES', 'Route 1`s terminal takes ConservationHypothesis at v1.5 (INTERFACES, not DERIVES); Route 3 encodes its conclusion',
         ['route1', 'route3', 'chrh'],
         'RE-CUT: | MONO §25.8 | axiom profiles only, grades in prose | Route 1 INTERFACES on ConservationHypothesis · Route 2 DERIVES (a fact on the line, no route to σ = 1/2) · Route 3 ENCODES-CONCLUSION (ConservationHypothesis is RH restated, `ch_iff_rh`) |'),
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
                112: ['cannon'], 113: ['c7'], 114: ['route3', 'chrh'], 122: ['h2rh'], 123: ['goal', 'mellin'], 124: ['route1'],
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
