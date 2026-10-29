# -*- coding: utf-8 -*-
"""standing/repeat.py -- v1.4.0 ((R334)(2), standing clauses v9 row (83)): THE REPEAT CLASSES' REPAIRS, ONE FUNCTION OR GUARD PER CLASS,
called from the fold's templates by one line each (the templates' line numbers kept, so no act's OVERRIDE moves) and from the act's tools.
Written at b724 by the Write tool; each repair's control is tools/standing/v140.py's, on the class's last banked instance.

  (iii) carried_failing(face_text)       the face's declared carried failures, read from its line, not a hand tuple
        prepush_after_record(act, root)  a pre-push reading refused once the act's components bank is committed (b723 event (16))
        seal_against_worklist(seal, sealed)  the seal's tools against the worklist's SEALED, both ways (b722 event (12))
  (iv)  phases(root)                     the step recorder's phases from data/act_current.json's components (`lock` among them)
        bookkeeping_only(files, act)     a commit carrying only the act's step, hashes and hook banks: no step of its own
        sealed_after(rows, rlog, plog, pre, files_of, act)   G-SEALED-AFTER-COMPONENTS by the lock's phase, bookkeeping commits exempt
  (v)   retired_reads(text, act, tools_dir)   a route reading a retired bank or a tool file the fold does not write
  (vi)  quarters(reads, first, last)     the chain's first half cut where the banked walks halve
  (vii) others_running(table, self_pid)  another suite part in the process table; refuse_concurrent_part(part) the guard
  (ix)  shifted_missing(src, dst, tools_dir)  a module or tool path the carry's substitution named that does not exist
  (x)   grade(ok, yes, no)               the grade sentence composed from the check's result
"""
import json
import os
import re
import subprocess
import sys

NL = '\n'
TOOLS = ('checks', 'citation', 'closing', 'record', 'reg_gate', 'regspec', 'report')   # ### the fold's seven: no tools/<act>_<tool>.py since v1.3.0
RETIRED_KINDS = ('readfirst_diff', 'readfirst_closure')   # ### (R332)(2)(iii): the closure reader and its diff retired from b722


# ================================================================================ (iii) HAND-KEPT NAME LISTS
DECLARED = re.compile(r'DECLARED BEFORE THE LOCK, BY NAME:\*\*\s*(.*)$', re.M)


def carried_failing(face_text):
    """the arms the face declares failing on real state before the lock (its line "... DECLARED BEFORE THE LOCK, BY NAME:** `G-...`"), in
    the order written; () where the face declares none or carries no such line."""
    m = DECLARED.search(face_text or '')
    return tuple(re.findall(r'`(G-[A-Z0-9-]+)`', m.group(1))) if m else ()


def _git(root, *a):
    return subprocess.run(['git', '-C', root] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def record_committed(act, root):
    """True once data/<act>_components.txt is carried by HEAD's tree: the record is committed, the pre-push reading is over."""
    return bool(_git(root, 'ls-tree', '--name-only', 'HEAD', '--', 'data/%s_components.txt' % act))


def prepush_after_record(act, root, pushed, other_mode):
    """b723 event (16): a part run with no mode after the record read PRE-PUSH (is_pushed False at a step-row tip) and wrote over the committed
    pre-push bank. Refused here: a pre-push reading (not pushed, no pre-run, mid, --prev or --rerun-postpush) once the record is committed;
    the post-push reading is the re-run's, to a file of its own ((R334)(1))."""
    if pushed or other_mode or not record_committed(act, root):
        return None
    sys.exit('### THE RECORD IS COMMITTED (data/%s_components.txt AT HEAD) AND THIS PART WOULD READ PRE-PUSH, OVER THE COMMITTED PRE-PUSH BANK -- '
             'NOTHING RUN: the post-push reading is `--rerun-postpush %s_checks_postpush.txt` ((R334)(1))' % (act, act))


def prev_carries(prev, own, n):
    """`--prev`'s worklist: the previous act's value is read for name n only where it carries one in this act's shape -- not missing, not
    None, and (where this act's is a string, a tuple or a list) of the same kind, a string against a string. Otherwise this act's value: the
    hand list _PrevWorklist.OWN missed names the previous worklist set to None (b722 events (8)-(10), C6_PP among them) or reused in another
    shape (C5_RELAY a pair where this act's is one commit)."""
    if not hasattr(prev, n):
        return False
    p, o = getattr(prev, n), getattr(own, n, None)
    if p is None:
        return False
    if isinstance(o, str):
        return isinstance(p, str)
    if isinstance(o, (tuple, list)):
        return isinstance(p, (tuple, list))
    return True


def seal_against_worklist(seal_tools, sealed):
    """(missing, extra): the worklist's SEALED tools the seal did not record, and the seal's tools the worklist does not name."""
    s, w = set(seal_tools or ()), set(sealed or ())
    return sorted(w - s), sorted(s - w)


# ================================================================================ (iv) THE LOCK PHASE AND THE STEP RECORDER'S PHASES
def phases(root, current=None):
    """(pre-seal phases, post-seal phases) from data/act_current.json's components, each component's phases in order: before `seal` the
    pre-seal, from `seal` on the post-seal, the record and the closing after them. Refuses a components list with no `lock` before `seal`."""
    if current is None:
        with open(os.path.join(root, 'data', 'act_current.json'), encoding='utf-8') as fh:
            current = json.load(fh)
    seq = [p for c in current['components'] for p in c['phases']]
    if 'seal' not in seq or 'lock' not in seq or seq.index('lock') > seq.index('seal'):
        sys.exit('### data/act_current.json: the components name no `lock` before `seal` -- the phases not read')
    k = seq.index('seal')
    return tuple(seq[:k]), tuple(seq[k:]) + tuple(p for p in ('record', 'closing') if p not in seq)


def bookkeeping_only(files, act):
    """True for a commit whose files are all the act's bookkeeping banks -- its step bank, its hashes bank, its hook's refusals -- which a
    step row cannot carry for itself (its row is written after it and committed by a later commit): b723's 2be0135c and 14bf5ec5."""
    keep = {'data/%s_steps.json' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act}
    return bool(files) and set(files) <= keep


def files_of(root, pp):
    """files_of(repo, h): the files a commit carries, by `git show --name-only` in the relay (repo 'relay') or PLACE-papers ('pp')"""
    where = dict(relay=root, pp=pp)
    return lambda repo, h: [l for l in _git(where[repo], 'show', '--name-only', '--format=', h).split(NL) if l.strip()]


def _phase_of(rows, repo, h):
    for r in rows:
        if r.get('repo') == repo and any(c.startswith(h) for c in ([r.get('commit')] + list(r.get('commits') or [])) if c):
            return r.get('phase')
    return None


def sealed_after(rows, rlog, plog, pre, files_of, act):
    """G-SEALED-AFTER-COMPONENTS: one relay row of phase `lock`; every other commit of the act (logs of (hash, subject, time)) has a row whose
    phase is pre-seal exactly where its time precedes the lock's; a bookkeeping-only commit (files_of(repo, hash)) is exempt; PLACE-papers
    carries a pre-seal commit. Returns (ok, the first breaking commit or reason)."""
    if not rows:
        return False, 'no step rows'
    locks = [r for r in rows if r.get('phase') == 'lock']
    if len(locks) != 1 or locks[0].get('repo') != 'relay':
        return False, 'lock rows %d' % len(locks)
    lt = [t for h, s, t in rlog if locks[0]['commit'].startswith(h)]
    if len(lt) != 1:
        return False, 'the lock commit not in the act`s relay log'
    lk = lt[0]
    for repo, log in (('relay', rlog), ('pp', plog)):
        for h, s, t in log:
            p = _phase_of(rows, repo, h)
            if p == 'lock':
                if repo != 'relay' or not locks[0]['commit'].startswith(h):
                    return False, '%s %s a second lock' % (repo, h[:8])
                continue
            if p is None:
                if bookkeeping_only(files_of(repo, h), act):
                    continue
                return False, '%s %s has no row' % (repo, h[:8])
            if (t < lk) != (p in pre):
                return False, '%s %s phase %r against the lock' % (repo, h[:8], p)
    if not any(_phase_of(rows, 'pp', h) in pre for h, s, t in plog):
        return False, 'no PLACE-papers commit of a pre-seal phase'
    return True, ''


# ================================================================================ (v) ROUTES READING RETIRED BANKS OR UNWRITTEN TOOL FILES
def retired_reads(text, act, tools_dir):
    """[(what, the line)]: every line of a rendered tool naming data/<act>_<retired kind> or tools/<act>_<tool>.py for a folded tool whose
    file does not exist (the fold renders it in memory) -- b722 event (6), b723 (y) and (l')."""
    out = []
    # ### a name READ by code: the bank reader's argument (rd/rdn/jl) or a path joined under tools/ (os.path.join(T, ...)), on a line that is
    # ### not a comment -- a name in a set, a plant or prose is not a read
    pat = re.compile(r'''(?:\b(?:rd|rdn|jl)\(\s*|os\.path\.join\(\s*(?:T|ROOT\s*,\s*['"]tools['"])\s*,\s*)['"](?:(%s_(?:%s)\.(?:txt|json))|(%s_(%s)\.py))['"]''' % (
        re.escape(act), '|'.join(RETIRED_KINDS), re.escape(act), '|'.join(TOOLS)))
    for i, l in enumerate((text or '').split(NL), 1):
        if l.lstrip().startswith('#'):
            continue
        for m in pat.finditer(l):
            if m.group(1):
                out.append(('retired bank %s' % m.group(1), i))
            elif not os.path.exists(os.path.join(tools_dir, m.group(2))):
                out.append(('tool file %s, not written' % m.group(2), i))
    return out


def src(tools_dir, act, tool):
    """a tool's text: tools/<act>_<tool>.py where the act wrote one (b722 and before), else the fold's render of it -- the template's
    one-line route in place of read(os.path.join(T, '<act>_<tool>.py'))"""
    p = os.path.join(tools_dir, '%s_%s.py' % (act, tool))
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            return f.read()
    return __import__('standing.fold', fromlist=['render']).render(act, tool)


def argv(tools_dir, act, tool, iso=False):
    """the run's argv after the interpreter's -X utf8: [-I?, tools/<act>_<tool>.py] where the file exists, else [tools/standing/fold.py,
    --act, <act>, <tool>] (fold.py strips --act wherever it stands); `-I` (iso) is kept off the fold route, which imports from
    tools/standing/"""
    p = os.path.join(tools_dir, '%s_%s.py' % (act, tool))
    if os.path.exists(p):
        return (['-I'] if iso else []) + [p]
    return [os.path.join(tools_dir, 'standing', 'fold.py'), '--act', act, tool]


def has_tool(tools_dir, act, tool):
    """the tool present: its file, or (a folded act) the act's sections file"""
    return os.path.exists(os.path.join(tools_dir, '%s_%s.py' % (act, tool))) or \
        __import__('standing.fold', fromlist=['has_sections']).has_sections(act)


# ================================================================================ THE ROOT ROUTE ((R334)(2), after the ten)
def committed_root(R):
    """b698_record's rootbanks rebound so the root names committed blobs alone: its reading (every named bank clean and equal to HEAD's blob,
    HEAD the remote main), its own writes (the root-banks banks, an excluded kind), and then the same reading again over the names root_banks
    gives at that moment -- a bank written or added between the first reading and the compute refuses the root. b723's root named
    data/b723_bank_hashes.json, which the hash recorder rewrote after the reading (no commit carries the hashed blob, 133004c8)."""
    first = R.rootbanks

    def rootbanks(*a):
        if not first(*a):
            return False
        s = R.root_banks_state(R.root_banks())
        bad = [r['bank'] for r in s['rows'] if not (r['status'] == 'clean' and r['equal'])]
        if bad or not s['pushed']:
            print('### THE ROOT ROUTE: AFTER ITS OWN WRITES %d NAMED BANK(S) NOT AS COMMITTED AT HEAD (%s)%s -- NO ROOT' % (
                len(bad), ', '.join(bad[:6]), '' if s['pushed'] else ' ; HEAD NOT THE REMOTE MAIN'))
            return False
        return True
    R.rootbanks = rootbanks
    return rootbanks


# ================================================================================ (vi) THE CHAIN PHASE ABOVE 450 S
def quarters(reads, first, last):
    """the chain's first half (acts first..last) cut in two where the banked walks halve: `reads` is {act: {later: n}} (the chain-half banks'
    reads, b723's); the walk per act is its `later` count, the first-parent walk act_root.py at_commit makes for a bank not at the root's
    commit. Returns ((first, cut-1), (cut, last))."""
    acts = sorted(a for a in reads if first <= a <= last)
    tot = sum(int(reads[a].get('later', 0)) for a in acts)
    run = 0
    for a in acts:
        run += int(reads[a].get('later', 0))
        if run * 2 >= tot:
            i = acts.index(a)
            return (acts[0], acts[i - 1] if i else acts[0]), (a, acts[-1])
    return (acts[0], acts[-2]), (acts[-1], acts[-1])


# ================================================================================ (vii) SUITE PARTS RUN CONCURRENTLY
PART_CMD = re.compile(r'(?:fold\.py\s+checks|_checks\.py)\b[^\n]*--part\s+(\S+)')


def process_table():
    """[(pid, command line)] of the host's python processes, read by PowerShell's Get-CimInstance (no shell pipe in the seat's command: the
    pipeline is the subprocess's own argument)."""
    ps = ("Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | ForEach-Object { '{0}`t{1}' -f $_.ProcessId, $_.CommandLine }")
    out = subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-Command', ps], capture_output=True, text=True, encoding='utf-8',
                         errors='replace').stdout
    rows = []
    for l in out.split(NL):
        if '\t' in l:
            pid, cmd = l.split('\t', 1)
            if pid.strip().isdigit():
                rows.append((int(pid.strip()), cmd.strip()))
    return rows


def others_running(table, self_pids):
    """[(pid, part)]: every process in the table running a suite part, other than the given pids (this run and its parent)."""
    return [(pid, m.group(1)) for pid, cmd in table for m in [PART_CMD.search(cmd or '')] if m and pid not in self_pids]


def refuse_concurrent_part(part):
    """b723 event (13), the author's rule at b723's close: suite parts run one at a time. Read the process table before a part starts and
    refuse while another part runs."""
    o = others_running(process_table(), {os.getpid(), os.getppid()})
    if o:
        sys.exit('### ANOTHER SUITE PART IS RUNNING (%s) -- PART %s NOT RUN: suite parts run one at a time (the author`s rule at b723`s close)' % (
            ', '.join('pid %d part %s' % x for x in o), part))
    return None


def part_guards(part, act, root, pushed, other_mode):
    """the suite's two refusals before a part reads anything, called from main's one line: (vii) another part running, (iii) a pre-push
    reading once the record is committed. Returns None or exits."""
    refuse_concurrent_part(part)
    return prepush_after_record(act, root, pushed, other_mode)


# ================================================================================ (ix) THE CARRY'S ACT-NAME SUBSTITUTION
REF = re.compile(r'\bimport\s+(b\d{3}_\w+)|\b(b\d{3}_\w+)\s+as\s+\w+|tools[/\\](b\d{3}_\w+)\.py|\b(b\d{3}_\w+)\.py\b')


def shifted_missing(src, dst, tools_dir):
    """[(line, name)]: a module or tool the carried text (dst) names that does not exist in tools/, where the source line at the same place
    named one that does -- the substitution shifted a name past what exists (b721 (p), b723 (d), b724 (d))."""
    out = []
    s_lines, d_lines = (src or '').split(NL), (dst or '').split(NL)
    for i, (a, b) in enumerate(zip(s_lines, d_lines), 1):
        if a == b:
            continue
        for m in REF.finditer(b):
            name = next(x for x in m.groups() if x)
            if not os.path.exists(os.path.join(tools_dir, name + '.py')):
                ms = [next(x for x in mm.groups() if x) for mm in REF.finditer(a)]
                if any(os.path.exists(os.path.join(tools_dir, n + '.py')) for n in ms):
                    out.append((i, name))
    return out


# ================================================================================ (x) A FIXED GRADE SENTENCE BEFORE ITS CHECK
def grade(ok, yes, no):
    """the grade sentence composed from the check's result: `yes` where ok is True, `no` where False; anything else (an unread check, None)
    refuses -- no sentence stands before its check."""
    if ok is True:
        return yes
    if ok is False:
        return no
    raise SystemExit('### A GRADE SENTENCE ASKED BEFORE ITS CHECK (the check read %r) -- NOTHING PRINTED' % (ok,))
