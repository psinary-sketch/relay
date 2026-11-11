"""b753 -- (R363)(5)(vii) THE TRANSCRIPT STORE READ, data/b753_store.txt. Names, sizes, dates and no content of any session.

    python -X utf8 -u tools/b753_store.py control     the controls alone
    python -X utf8 -u tools/b753_store.py dry         composed and printed, nothing banked
    python -X utf8 -u tools/b753_store.py run         composed and banked; refuses unless this file is committed and clean

What it reads: the store's own listing (file names, sizes, last-write times; no file of it is opened); the relay's tracked tools and banks by
`git grep` for the form of a session id; the lines of the tools that name an absent id; whether each scratch folder a tool names stands; the
operating system's storage policy by a registry read. It changes nothing outside its bank.

THE RULES, each printed in the bank before its figures:
  (ID)   a session id is the 8-4-4-4-12 hexadecimal form. In tools/ every line carrying the form is a place. In data/ the form is also what
         deposit manifests and other records use for things that are no session, so a bank's CITATION KEY is the form standing (K1) after the
         word "session", (K2) before ".jsonl", or (K3) after "projects/D--/" -- and the wide yield is printed beside the keys' yield.
  (NEAR) an id absent from the store that shares its leading eight characters with a present one is printed as A NEAR TWIN, apart from the absent.
  (READER) for a tool naming an absent id, lexically, from the tool's own lines: the names assigned a path ending .jsonl (the right side
         opening with a string or os.path.join); then
         GUARDED, STOPS         an exists/isfile test of such a name, negated, with an exit or a raise on its line or the two after (quoted)
         GUARDED, GOES ON       such a test with no exit or raise beside it: the tool goes on where the file is absent -- the form (R363)(7)(viii)
                                names, an absent input that can read as an empty result (the test's line and the two after quoted, to be read)
         OPENS UNDER AN EXCEPT  an open of such a name inside a try whose except stands at the try's own indent (quoted)
         OPENS, NO GUARD        an open of such a name, no test and no try over it: the interpreter raises FileNotFoundError and the route stops
         PATH HELD, NOT OPENED  such a name is assigned and no line of the tool opens it: it is handed on (its uses quoted)
         THROUGH path_of        no such name; the tool resolves the transcript through tools/standing/chain.py's path_of, which prints ABSENT and stops
         LISTS THE FOLDER       no such name; the tool lists the folder's .jsonl files and reads whichever stand: an absent one is not missed by it
         PATH BUILT IN A CALL   no such name; a line of code carries ".jsonl" outside an assignment (quoted)
         NO TRANSCRIPT PATH     the tool names the id in a scratch path or a label alone; no line of its code carries ".jsonl"
         The classes are lexical and say what the lines show; no reader was run against an absent file by this read.
  (30)   the date a session would have left under the 30-day default: its last write plus 30 days (UTC dates).
"""
import collections
import io
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b753'
BANK = os.path.join(RELAY, 'data', '%s_store.txt' % ACT)
STORE = 'D:/claude-store/projects-D--'
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
THIS = '5a4228ab-091d-4515-b5ab-95a5e34e1e18'
UUP = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
UU = re.compile(UUP)
KEYS = (('K1', re.compile(r'\bsession (%s)' % UUP)), ('K2', re.compile(r'(%s)\.jsonl' % UUP)), ('K3', re.compile(r'projects/D--/(%s)' % UUP)))
SCR = re.compile(r'([A-Za-z]:[^\'" ]*?)?[\\/]+(%s)[\\/]+scratchpad' % UUP)
PLANTED = '00000000-0000-0000-0000-000000000000'
HOLD_ABSENT = (('f004d01d', 'tools/standing/routes/b644_record.py', 38), ('a5f76775', 'tools/b597_record.py', 32))
HOLD_SCRATCH = (('3bbc6267', 'tools/standing/fold/record.tpl', 3045), ('02c7cf38', 'tools/standing/v130.py', 40),
                ('7c29db99', 'tools/standing/v1160.py', 21), ('7c29db99', 'tools/standing/v1170.py', 24))
PACK_CITES = (('tools/standing/scratchfsck.py', 1, 12), ('tools/standing/v1160.py', 129, 147), ('tools/standing/v1170.py', 186, 186))
POLICY_KEY = r'Software\Microsoft\Windows\CurrentVersion\StorageSense\Parameters\StoragePolicy'
GROUP_KEY = r'SOFTWARE\Policies\Microsoft\Windows\StorageSense'
# ### the meanings are the seat's reading of the operating system's published settings, not read from this host
POLICY_MEANING = (('01', 'the cleaner switched on (1) or off (0)'), ('04', 'temporary files that programs are not using are deleted (1) or kept (0)'),
                  ('2048', 'how often it runs, in days; 0 = when free space is low'), ('256', 'days before the recycle bin is emptied'),
                  ('32', 'whether the downloads folder is cleaned (0 = never)'), ('512', 'days before the downloads folder is cleaned (0 = never)'))


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def day(t):
    return time.strftime('%Y-%m-%d', time.gmtime(t))


def leaves(t, days=30):
    return day(t + days * 86400)


def listing(store=STORE):
    """([(id, bytes, mtime)], id-named folders, other folders, other files): names, sizes and times; nothing opened."""
    sess, idd, od, of = [], 0, 0, 0
    for e in sorted(os.listdir(store)):
        p = store + '/' + e
        if os.path.isdir(p):
            if UU.fullmatch(e):
                idd += 1
            else:
                od += 1
        elif e.endswith('.jsonl') and UU.fullmatch(e[:-6]):
            st = os.stat(p)
            sess.append((e[:-6], st.st_size, st.st_mtime))
        else:
            of += 1
    return sess, idd, od, of


def gg(pat, *paths):
    """git grep over the relay's tracked files: (exit, [(path, line, match)]). Exit 1 is no match; anything else beyond 0 is a failed read."""
    r = subprocess.run(['git', '-C', RELAY, 'grep', '-n', '-o', '-I', '-E', pat, '--'] + list(paths), capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode not in (0, 1):
        raise SystemExit('### FAILED: git grep exit %d: %s' % (r.returncode, r.stderr.strip()[:300]))
    out = []
    for l in r.stdout.split('\n'):
        p = l.split(':', 2)
        if len(p) == 3:
            out.append((p[0], int(p[1]), p[2]))
    return r.returncode, out


def group(hits, rx=UU):
    d = collections.OrderedDict()
    for f, n, m in hits:
        d.setdefault(rx.search(m).group(0), []).append((f, n))
    return d


def keyed(text):
    """[(key name, id)] for one line of a bank: the citation keys of rule (ID)."""
    return [(k, m.group(1)) for k, rx in KEYS for m in rx.finditer(text)]


def state(i, have):
    if i in have:
        return 'PRESENT'
    if any(h[:8] == i[:8] for h in have):
        return 'A NEAR TWIN'
    return 'ABSENT'


def src(rel):
    return io.open(os.path.join(RELAY, rel), encoding='utf-8', errors='replace').read().split('\n')


def reader(lines):
    """rule (READER) on a tool's lines: (class, [(line number, text)])."""
    ind = lambda s: len(s) - len(s.lstrip())
    code = lambda s: s.strip() and not s.lstrip().startswith('#')
    names, lists = [], []
    for n, l in enumerate(lines, 1):
        if '.jsonl' in l and 'listdir(' in l:
            lists.append((n, l))
            continue
        # a name is assigned a path where the right side opens with a string or os.path.join; a call that takes a path is no assignment of one
        m = re.match(r'''^\s*([A-Za-z_][\w.]*)\s*=\s*(?:[rRuU]?['"]|os\.path\.join\().*\.jsonl''', l)
        if m and m.group(1) not in names:
            names.append(m.group(1))
    if not names:
        if any(re.search(r'\bpath_of\(', l) for l in lines):
            return 'THROUGH path_of', [(n, l) for n, l in enumerate(lines, 1) if re.search(r'\bpath_of\(', l)][:2]
        if lists:
            return 'LISTS THE FOLDER', lists[:2]
        call = [(n, l) for n, l in enumerate(lines, 1) if '.jsonl' in l and code(l)]
        if call:
            return 'PATH BUILT IN A CALL', call[:3]
        return 'NO TRANSCRIPT PATH', []
    alt = '|'.join(re.escape(x) for x in names)
    guard = re.compile(r'(?:exists|isfile)\(\s*(?:%s)\b' % alt)
    opens = re.compile(r'\bopen\(\s*(?:%s)\b' % alt)
    use = re.compile(r'(?<![\w.])(?:%s)\b' % alt)
    g = [n for n, l in enumerate(lines, 1) if guard.search(l)]
    o = [n for n, l in enumerate(lines, 1) if opens.search(l)]
    if g:
        k = g[0]
        near = ' '.join(lines[k - 1:k + 2])
        stops = re.search(r'\bnot\b', lines[k - 1]) and re.search(r'sys\.exit\(|\braise\b|SystemExit', near)
        return ('GUARDED, STOPS' if stops else 'GUARDED, GOES ON'), [(n, lines[n - 1]) for n in (k, k + 1, k + 2) if n <= len(lines) and code(lines[n - 1])]
    if o:
        for k in o:
            # an except covers the open only where its try stands above the open, less indented than it, the except at the try's own indent
            tr = [n for n in range(max(1, k - 4), k) if re.match(r'^\s*try:', lines[n - 1]) and ind(lines[n - 1]) < ind(lines[k - 1])]
            if tr:
                ex = [n for n in range(k + 1, min(k + 13, len(lines) + 1)) if re.match(r'^\s*except\b', lines[n - 1]) and ind(lines[n - 1]) == ind(lines[tr[-1] - 1])]
                if ex:
                    return 'OPENS UNDER AN EXCEPT', [(k, lines[k - 1]), (ex[0], lines[ex[0] - 1])] + ([(ex[0] + 1, lines[ex[0]])] if ex[0] < len(lines) else [])
        return 'OPENS, NO GUARD', [(n, lines[n - 1]) for n in o[:2]]
    u = [(n, l) for n, l in enumerate(lines, 1) if use.search(l) and '(' in l and code(l) and not re.match(r'^\s*(?:%s)\s*=' % alt, l)]
    return 'PATH HELD, NOT OPENED', u[:2]


def scratch_of(hits):
    """{id: {path as written or None: [(file, line)]}} from the tools' lines naming <id>/scratchpad."""
    d = collections.OrderedDict()
    for f, n, m in hits:
        mm = SCR.search(m)
        if not mm:
            continue
        root = mm.group(1)
        p = (root.replace('\\\\', '/').replace('\\', '/') + '/' + mm.group(2) + '/scratchpad') if root else None
        d.setdefault(mm.group(2), collections.OrderedDict()).setdefault(p, []).append((f, n))
    return d


def short(p):
    """a scratch path printed by its role: the temp directory's harness folder, the folder under it, the id's eight characters."""
    m = re.search(r'/Temp/claude/([^/]+)/(%s)/scratchpad$' % UUP, p)
    return '<temp>/claude/%s/%s.../scratchpad' % (m.group(1), m.group(2)[:8]) if m else '<a path of another form>/%s.../scratchpad' % UU.search(p).group(0)[:8]


def policy():
    """the storage policy by a registry read: ({name: value} or None where the key is absent, group policy {..} or None)."""
    import winreg

    def rd(hive, key):
        try:
            k = winreg.OpenKey(hive, key, 0, winreg.KEY_READ)
        except OSError:
            return None
        out, i = {}, 0
        while True:
            try:
                n, v, t = winreg.EnumValue(k, i)
            except OSError:
                break
            if t == winreg.REG_DWORD:
                out[n] = v
            i += 1
        winreg.CloseKey(k)
        return out
    return rd(winreg.HKEY_CURRENT_USER, POLICY_KEY), rd(winreg.HKEY_LOCAL_MACHINE, GROUP_KEY)


def controls(sess, tool_hits):
    L, ok = ['## THE CONTROLS, printed before any figure'], [True]

    def case(what, got, want):
        good = got == want
        ok[0] = ok[0] and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    have = set(s[0] for s in sess)
    a, b = '%s/%s.jsonl' % (PROJ, THIS), '%s/%s.jsonl' % (STORE, THIS)
    case('(the store) this session`s transcript stands by both paths at one size; the planted id that no file holds reads', (os.path.isfile(a) and os.path.getsize(a) == os.path.getsize(b), THIS in have, state(PLANTED, have)), (True, True, 'ABSENT'))
    case('(the store) a session count at or above the hold`s 44, each id once', (len(sess) >= 44, len(have) == len(sess)), (True, True))
    th = set((f, n, m[:8]) for f, n, m in tool_hits)
    case('(the search) the two ids the hold read absent are found at the lines the ruling cites', [(f, n, i) in th for i, f, n in HOLD_ABSENT], [True, True])
    case('(the search) the scratch folders the ruling cites are found at their lines', [(f, n, i) in th for i, f, n in HOLD_SCRATCH], [True] * 4)
    u1, u2 = 'aaaaaaaa-1111-2222-3333-444444444444', 'bbbbbbbb-1111-2222-3333-444444444444'
    case('(rule ID) a planted bank line: a citation key found, a deposit record`s id of the same form not', (keyed('### CALL x (session %s, transcript line 5)' % u1), keyed('"bucket": "%s", "file": "D--/%s.jsonl"' % (u2, u1))), ([('K1', u1)], [('K2', u1)]))
    case('(rule NEAR) an id one group away from a present one; a present one; one sharing nothing', (state(THIS[:19] + 'ffff' + THIS[23:], have), state(THIS, have), state(u1, have)), ('A NEAR TWIN', 'PRESENT', 'ABSENT'))
    P = "S = 'C:/x/projects/D--/%s.jsonl'" % u1
    case('(rule READER) planted tools, one of each class',
         [reader(x)[0] for x in ([P, 'if not os.path.exists(S):', "    sys.exit('ABSENT')", 'for r in io.open(S):'], [P, 'if not os.path.exists(S):', '    return 10 ** 9', 'for r in io.open(S):'],
                                 [P, 'try:', '    t = io.open(S).read()', 'except OSError:', "    t = ''"],
                                 [P, 'for r in io.open(S, encoding="utf-8"):'], [P, 'rows = ER.capture(S, 1)'], ["SP = 'C:/t/%s/scratchpad'" % u1], ["p = chain.path_of('%s')" % u1],
                                 ["fs = [f for f in os.listdir(TX) if f.endswith('.jsonl')]"], ["more = ER.capture('C:/x/%s.jsonl' % sid, anc)"])],
         ['GUARDED, STOPS', 'GUARDED, GOES ON', 'OPENS UNDER AN EXCEPT', 'OPENS, NO GUARD', 'PATH HELD, NOT OPENED', 'NO TRANSCRIPT PATH', 'THROUGH path_of', 'LISTS THE FOLDER', 'PATH BUILT IN A CALL'])
    case('(rule READER) an except inside the loop over the open file guards the row`s parse and not the open',
         reader([P, 'for i, raw in enumerate(io.open(S), 1):', '    try:', '        o = json.loads(raw)', '    except Exception:', '        continue'])[0], 'OPENS, NO GUARD')
    case('(rule READER) the known instance: tools/standing/routes/b644_record.py, repaired at v1.33.0, reads', reader(src('tools/standing/routes/b644_record.py'))[0], 'GUARDED, STOPS')
    sc = scratch_of([('t.py', 1, 'C:/Users/u/AppData/Local/Temp/claude/D--/%s/scratchpad' % u1), ('t.py', 2, '\\%s\\scratchpad' % u2)])
    case('(the scratch folders) a planted path read with its root, one with no root, the planted one not standing; this session`s own standing',
         (list(sc[u1])[0], list(sc[u2])[0], os.path.isdir(list(sc[u1])[0]), os.path.isdir(os.path.join(os.environ.get('TEMP', ''), 'claude'))),
         ('C:/Users/u/AppData/Local/Temp/claude/D--/%s/scratchpad' % u1, None, False, True))
    case('(rule 30) a last write of 2026-10-12 leaves on', leaves(time.mktime((2026, 10, 12, 12, 0, 0, 0, 0, 0)) - time.timezone), '2026-11-11')
    pol = policy()
    case('(the storage policy) the registry read returns values or reads the key absent, raising nothing', pol[0] is None or isinstance(pol[0], dict), True)
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L) - 1, 'ALL AS WANTED' if ok[0] else '### NOT ALL AS WANTED'))
    return ok[0], L


def compose(gen):
    sess, idd, od, of = listing()
    have = set(s[0] for s in sess)
    _rc, tool_hits = gg(UUP, 'tools')
    _rc, data_hits = gg(UUP, 'data')
    ok, C = controls(sess, tool_hits)
    tools, wide = group(tool_hits), group(data_hits)
    tools.pop(PLANTED, None)
    L = ['%s -- (R363)(5)(vii) THE TRANSCRIPT STORE READ (%s; generator tools/%s_store.py at relay %s)' % (ACT, stamp(), ACT, gen), '',
         '### names, sizes, dates and no content: no transcript was opened by this read (the store`s listing; `git grep` over the relay`s tracked tools/ and data/;',
         '### the lines of the tools naming an absent id; one registry read). The rules stand in the generator`s head and beside each section.', ''] + C + ['']

    # --- the store
    sess.sort(key=lambda s: s[2])
    L += ['## THE STORE: %d sessions (%d bytes), the oldest last written %s ; %d folders named by a session id, %d other folder(s), %d other file(s), none opened' % (
        len(sess), sum(s[1] for s in sess), day(sess[0][2]), idd, od, of),
        '   rule (30): the last column is the last write plus 30 days, the date the session would have left under the default that stood until 2026-11-11',
        '   id        bytes         last write   would have left']
    L += ['   %s  %12d  %s   %s' % (i[:8], z, day(m), leaves(m)) for i, z, m in sess]
    due = [i for i, _z, m in sess if leaves(m) <= '2026-11-30']
    L += ['   ### would have left on or before 2026-11-11: %d ; on or before 2026-11-30: %d of %d' % (sum(1 for i, _z, m in sess if leaves(m) <= '2026-11-11'), len(due), len(sess)), '']

    # --- the tools' ids
    st = collections.Counter(state(i, have) for i in tools)
    L += ['## THE SESSION IDS THE RELAY`S TOOLS NAME: %d ids in %d places ; PRESENT %d ; ABSENT %d ; A NEAR TWIN %d (the control`s planted id, all zeros, apart)' % (
        len(tools), sum(len(v) for v in tools.values()), st['PRESENT'], st['ABSENT'], st['A NEAR TWIN'])]
    for s in ('ABSENT', 'A NEAR TWIN', 'PRESENT'):
        for i in sorted(x for x in tools if state(x, have) == s):
            pl = tools[i]
            L.append('   %s %-11s %3d place(s) in %3d file(s): %s' % (i[:8], s, len(pl), len(set(f for f, _n in pl)), ' ; '.join('%s :%d' % p for p in pl[:6]) + (' ; and %d more' % (len(pl) - 6) if len(pl) > 6 else '')))
    for i in sorted(x for x in tools if state(x, have) == 'A NEAR TWIN'):
        tw = [h for h in have if h[:8] == i[:8]][0]
        L.append('   ### NEAR TWIN %s: the tool`s id and the store`s differ in the group(s) %s; no transcript is named by it (%s)' % (
            i[:8], [k + 1 for k, (x, y) in enumerate(zip(i.split('-'), tw.split('-'))) if x != y], ' ; '.join('%s :%d' % p for p in tools[i])))
    L.append('')

    # --- the banks' citation keys
    kd, ky = collections.OrderedDict(), collections.Counter()
    seen_lines = set((f, n) for f, n, _m in data_hits)
    by_file = collections.defaultdict(list)
    for f, n in seen_lines:
        by_file[f].append(n)
    for f in sorted(by_file):
        lines = src(f)
        for n in sorted(by_file[f]):
            if n <= len(lines):
                for k, i in keyed(lines[n - 1]):
                    ky[k] += 1
                    kd.setdefault(i, []).append((f, n))
    kd.pop(PLANTED, None)
    ks = collections.Counter(state(i, have) for i in kd)
    L += ['## THE SESSION IDS THE BANKS` CITATION KEYS NAME (rule (ID)): %d ids ; PRESENT %d ; ABSENT %d ; A NEAR TWIN %d' % (len(kd), ks['PRESENT'], ks['ABSENT'], ks['A NEAR TWIN']),
          '   the matchers` yields: the form anywhere in data/ %d ids in %d places over %d files ; the keys K1 (after "session") %d, K2 (before ".jsonl") %d, K3 (after "projects/D--/") %d places' % (
              len(wide), len(data_hits), len(by_file), ky['K1'], ky['K2'], ky['K3']),
          '   ids of the form in data/ that no key names: %d (deposit records` and other records` ids, and ids in forms the keys do not take; of them in the store: %d -- listed below)' % (
              len([i for i in wide if i not in kd and i != PLANTED]), len([i for i in wide if i not in kd and i in have]))]
    for s in ('ABSENT', 'A NEAR TWIN', 'PRESENT'):
        for i in sorted(x for x in kd if state(x, have) == s):
            pl = sorted(set(kd[i]))
            L.append('   %s %-11s %5d keyed place(s) in %3d bank(s); first %s :%d%s' % (i[:8], s, len(pl), len(set(f for f, _n in pl)), pl[0][0], pl[0][1], '' if i in tools else ' ; named by no tool'))
    for i in sorted(x for x in wide if x not in kd and x in have):
        L.append('   %s PRESENT, named in data/ by no key: %d place(s), first %s :%d' % (i[:8], len(wide[i]), wide[i][0][0], wide[i][0][1]))
    both = sorted(set(i for i in list(tools) + list(kd) if state(i, have) == 'ABSENT'))
    unnamed = sorted(i for i in have if i not in tools and i not in kd)
    L += ['   ### ABSENT ids named by a tool or a key: %d (tools %d, keys %d, both %d) ; sessions of the store named by no tool and no key: %d (%s)' % (
        len(both), st['ABSENT'], ks['ABSENT'], len([i for i in both if i in tools and i in kd]), len(unnamed), ', '.join(i[:8] for i in unnamed) or '-'), '']

    # --- the readers of the absent
    rows, tally = [], collections.Counter()
    for i in sorted(x for x in tools if state(x, have) == 'ABSENT'):
        for f in sorted(set(f for f, _n in tools[i])):
            if not f.endswith(('.py', '.tpl')):
                rows.append((i, f, 'NOT A PYTHON SOURCE', []))
                tally['NOT A PYTHON SOURCE'] += 1
                continue
            c, q = reader(src(f))
            rows.append((i, f, c, q))
            tally[c] += 1
    order = ('GUARDED, GOES ON', 'OPENS UNDER AN EXCEPT', 'OPENS, NO GUARD', 'GUARDED, STOPS', 'THROUGH path_of', 'PATH HELD, NOT OPENED', 'PATH BUILT IN A CALL', 'LISTS THE FOLDER',
             'NO TRANSCRIPT PATH', 'NOT A PYTHON SOURCE')
    L += ['## WHAT EACH READER DOES WHERE ITS SESSION IS ABSENT (rule (READER); lexical, from the tool`s own lines; no reader run): %d tool files over %d absent ids' % (
        len(rows), st['ABSENT']), '   ' + ' ; '.join('%s %d' % (c, tally[c]) for c in order)]
    for c in order:
        rs = [r for r in rows if r[2] == c]
        if not rs:
            continue
        L.append('   -- %s (%d)' % (c, len(rs)))
        if c == 'NO TRANSCRIPT PATH':
            byid = collections.OrderedDict()
            for i, f, _c, _q in rs:
                byid.setdefault(i, []).append(f)
            L += ['      %s: %d file(s): %s' % (i[:8], len(fs), ', '.join(fs[:4]) + (', and %d more' % (len(fs) - 4) if len(fs) > 4 else '')) for i, fs in byid.items()]
            continue
        for i, f, _c, q in rs:
            L.append('      %s %s' % (i[:8], f))
            L += ['          :%d %s' % (n, ' '.join(t.split())[:200]) for n, t in q]
    L.append('')

    # --- the scratch folders
    _rc, sh = gg('([A-Za-z]:[^\'" ]*)?[\\\\/]+' + UUP + '[\\\\/]+scratchpad', 'tools')
    sc = scratch_of(sh)
    stand, gone, noroot = [], [], []
    for i, ps in sc.items():
        for p, pl in ps.items():
            (noroot if p is None else (stand if os.path.isdir(p) else gone)).append((i, p, pl))
    roots = collections.Counter(re.sub(r'/%s/scratchpad$' % UUP, '', p) for _i, p, _pl in stand + gone)
    L += ['## THE SCRATCH FOLDERS THE TOOLS NAME: %d ids ; paths written with a root %d: STANDS %d, GONE %d ; written with no root (a path joined at run time) %d' % (
        len(sc), len(stand) + len(gone), len(stand), len(gone), len(noroot))]
    for r, k in sorted(roots.items()):
        m = re.search(r'/Temp/claude/([^/]+)$', r)
        kids = len(os.listdir(r)) if os.path.isdir(r) else None
        L.append('   the root <temp>/claude/%s: named for %d folder(s); the root itself %s' % (m.group(1) if m else '<another form>', k, 'STANDS, holding %d entries' % kids if kids is not None else 'GONE'))
    for name, rs in (('STANDS', stand), ('GONE', gone)):
        for i, p, pl in sorted(rs):
            L.append('   %s %-6s %s ; transcript %s ; %d place(s), first %s :%d' % (i[:8], name, short(p), state(i, have), len(pl), pl[0][0], pl[0][1]))
    for i, _p, pl in sorted(noroot):
        L.append('   %s NO ROOT WRITTEN ; transcript %s ; %d place(s), first %s :%d' % (i[:8], state(i, have), len(pl), pl[0][0], pl[0][1]))
    gone_present = sorted(set(i[:8] for i, _p, _pl in gone if i in have))
    L += ['   ### scratch folders gone whose transcripts stand: %d (%s)' % (len(gone_present), ', '.join(gone_present)), '']

    # --- the hold's figures
    tA = set(i[:8] for i in tools if state(i, have) == 'ABSENT')
    gS = set(i[:8] for i, _p, _pl in gone)
    L += ['## THE SEAT`S READS DURING THE HOLD, TO REPRODUCE OR DIFFER ((R363)(5)(vii))',
          '   "44 sessions in the store on 2026-11-11": the store holds %d, this session`s (%s, begun after the store was moved) among them -- %s' % (
              len(sess), THIS[:8], 'REPRODUCED (44 and this one)' if len(sess) == 45 and THIS in have else '### DIFFERS'),
          '   "the oldest last written 2026-10-12": %s -- %s' % (day(sess[0][2]), 'REPRODUCED' if day(sess[0][2]) == '2026-10-12' else '### DIFFERS'),
          '   "f004d01d and a5f76775 absent": %s -- and ### THE HOLD`S READ WAS OF TWO; THE TOOLS NAME %d ABSENT IDS, these two among them' % (
              'REPRODUCED' if set(x[0] for x in HOLD_ABSENT) <= tA else '### DIFFERS', len(tA)),
          '   "the scratch folders of 3bbc6267, 02c7cf38 and 7c29db99 gone while their transcripts stand": %s -- and ### THE HOLD`S READ WAS OF THREE; %d NAMED FOLDERS ARE GONE, %d OF THEM WITH A TRANSCRIPT STANDING' % (
              'REPRODUCED' if set(x[0] for x in HOLD_SCRATCH) <= gS and set(x[0] for x in HOLD_SCRATCH) <= set(h[:8] for h in have) else '### DIFFERS', len(gone), len(gone_present)), '']

    # --- the temp directory read
    pol, grp = policy()
    L += ['## THE TEMP DIRECTORY READ -- A CANDIDATE AND NO FINDING ((R363)(5)(vii)): the operating system`s storage policy, read from the registry and changed by nothing',
          '   the user`s policy key: %s ; the machine`s group-policy key: %s' % ('ABSENT' if pol is None else 'PRESENT, %d numeric values' % len(pol), 'ABSENT' if grp is None else 'PRESENT: %r' % (sorted(grp.items()),))]
    if pol is not None:
        for k, meaning in POLICY_MEANING:
            L.append('   value %-5s = %-4s (the seat`s reading of the setting, not read from this host: %s)' % (k, pol.get(k, 'unset'), meaning))
        on = pol.get('01') == 1 and pol.get('04') == 1
        L.append('   ### AS THE VALUES READ: the cleaner %s, its deleting of temporary files %s, its cadence value %s' % (
            'SWITCHED ON' if pol.get('01') == 1 else 'SWITCHED OFF OR UNSET', 'ON' if pol.get('04') == 1 else 'OFF OR UNSET', pol.get('2048', 'unset')))
    else:
        on = False
    L.append('   beside it, the three pack losses the record holds (zqwork and zqwork2 on 2026-11-02, zqwork3 after them), whose cause the record holds as not established -- the lines the ruling cites:')
    for f, a, b in PACK_CITES:
        ls = src(f)
        got = [(n, ls[n - 1]) for n in range(a, min(b, len(ls)) + 1) if re.search(r'zqwork|pack|scratch', ls[n - 1], re.I)]
        L.append('      %s :%d-:%d -- %d line(s) of the range name a pack, a scratch folder or zqwork; the first: %s' % (f, a, b, len(got), ('":%d %s"' % (got[0][0], ' '.join(got[0][1].split())[:170])) if got else '### NONE'))
    L += ['   and beside the scratch folders gone: %d of the %d written with a root, %d of the gone under the temp directory.' % (
        len(gone), len(stand) + len(gone), sum(1 for _i, p, _pl in gone if '/Temp/claude/' in p)),
          '   ### THE CANDIDATE: %s. This read does not establish what removed any folder or pack: the cleaner`s own log was not read, no folder`s removal was observed,' % (
              'a cleaner switched on with temporary files in its reach is consistent with those losses and does not prove their cause' if on else
              'the cleaner as read is not switched on over temporary files; as a cause of those losses the candidate is weakened by this read and not excluded by it'),
          '   ### and the harness`s own clearing of a session`s scratch folder is a second candidate this read cannot tell from the first.', '']

    L += ['## PUT IN [D1] ((R363)(5)(vii), (7)(viii)), nothing changed by this read: no tool repaired, no folder made or removed, no setting changed.', '',
          '### ### **THE STORE READ: SESSIONS %d ; THE TOOLS NAME %d IDS, ABSENT %d, A NEAR TWIN %d ; THE BANKS` KEYS NAME %d, ABSENT %d ; READERS OF THE ABSENT %d FILES, GUARDED AND GOING ON %d ;'
          ' SCRATCH FOLDERS NAMED WITH A ROOT %d, GONE %d ; THE HOLD`S FOUR READS REPRODUCED AND TWO OF THEM UNDERSTATED ; THE TEMP DIRECTORY READ A CANDIDATE ; CONTROLS %s.**' % (
              len(sess), len(tools), st['ABSENT'], st['A NEAR TWIN'], len(kd), ks['ABSENT'], len(rows), tally['GUARDED, GOES ON'], len(stand) + len(gone), len(gone), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED')]
    return ok, L


def committed():
    rel = 'tools/%s_store.py' % ACT
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)
    return g('ls-files', '--error-unmatch', rel).returncode == 0 and not g('status', '--porcelain', '--', rel).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    if argv[:1] == ['control']:
        sess = listing()[0]
        ok, L = controls(sess, gg(UUP, 'tools')[1])
        print('\n'.join(L))
        return 0 if ok else 1
    if argv[:1] not in (['run'], ['dry']):
        raise SystemExit(__doc__)
    done, gen = committed()
    if argv[0] == 'run' and not done:
        raise SystemExit('### REFUSED: tools/%s_store.py is not committed or differs from its commit; the generator commits before its run ((R363)(5))' % ACT)
    import hold
    if hold.refuses('the transcript store read ((R363)(5)(vii))'):
        return 3
    ok, L = compose(gen)
    if argv[0] == 'run':
        if not ok:
            raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NOTHING BANKED')
        tmp = BANK + '.tmp'
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(L) + '\n')
        os.replace(tmp, BANK)
    keep = ('## ', '### ', '   ###', '   -- ', '   the ', '   "', '   value', '   beside', '   and ', '      tools/')
    sec, out = None, []
    for l in L:
        if l.startswith('   -- '):
            sec = l
        elif l.startswith('## '):
            sec = None
        rows = sec is not None and not sec.startswith(('   -- GUARDED, STOPS', '   -- NO TRANSCRIPT PATH', '   -- OPENS, NO GUARD')) and l.startswith('      ')
        if rows or l.startswith(keep) or l.startswith('  (') or l.startswith('  ###'):
            out.append(l[:260])
    print('\n'.join(out))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
