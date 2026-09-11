# -*- coding: utf-8 -*-
"""b418_extract.py -- THE SURVEY FOR b418. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **THE ACT RESUMED AFTER A DROP**, with no registration and no write on any repository; the
### reads taken before the drop are re-taken here, on disk, so nothing the face cites was only seen.
### ### **THE WALKER'S POPULATION IS READ FROM THE SESSION TRANSCRIPTS**, because the walker is the
### seat's `Grep` tool and its calls are recorded nowhere else -- with each call's duration, its
### result metadata, and whether it returned an empty result or ran to the limit.
### ### **NO RE-RUN VERDICT IS TAKEN HERE.** ### The survey lists the calls; Component 1 re-runs them
### after the lock, so no CONFIRMED or MOVED is seen before the face is sealed.
"""
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
FA = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic')
TD = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
ATREST = os.path.join(PP, 'phase1.5', 'structural', 'AT_REST.md')
CONST = os.path.join(PP, 'phase1.5', 'deep-structure', 'CONSTANCE.md')
REG = os.path.join(PP, 'REGISTRY.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
PIN_PP, PIN_RELAY = '09a1e80', '1dc9f72'
OUT = os.path.join(D, 'b418_extract.txt')
POPOUT = os.path.join(D, 'b418_walker_population.json')
NL = chr(10)
# ### THE ARC: since the last fold (b412 folded b403-b411), so b413 to b417, bounded by the pastes.
ARC = [('2513b655-f245-4a1e-8ebc-d1a4287ead2d', '2026-09-11T02:00:38', '9999'),
       ('fbe6b4b2-25ed-44b7-91cb-756e5456e21d', '2026-09-11T13:20:22', '2026-09-11T14:12:59')]

L = []
MISS = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.returncode, (r.stdout or '').strip()


def blob(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def quote(label, path, start, end=None, width=94, cap=700):
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:46]))
        say('  %-40s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = re.sub(r'\s+', ' ', src[i:j] if j > i else src[i:i + cap]).strip()
    say('  %-40s %s line %d' % (label, os.path.basename(path), src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      %s' % s)
    return seg


def ts(s):
    return datetime.strptime(s[:23], '%Y-%m-%dT%H:%M:%S.%f') if s and len(s) >= 23 else None


rule('=')
say('b418_extract.py -- THE SURVEY: THE WALKER, THE RULING, THE REPAIRS, (N), AND THE EXAMPLES.')
rule('=')
say()

# =============================================================================================
rule()
say('### READ 0 -- STEP ZERO ON RESUME, RE-TAKEN, AND THE ORIENTATION CITATIONS.')
rule()
say('  b418 files in relay before this survey (the ferry file excepted) : %d'
    % len([f for f in os.listdir(D) if f.startswith('b418_') and f not in
           ('b418_ferry.txt', 'b418_ferry_scan.txt', 'b418_census_stepzero.txt',
            'b418_faces_census_stepzero.txt', 'b418_pins_stepzero.txt', 'b418_extract.txt',
            'b418_walker_population.json')]))
for nm, repo, pin in (('relay', ROOT, PIN_RELAY), ('PLACE-papers', PP, PIN_PP),
                      ('SIDE-global-section', KERN, 'ad7dba6'),
                      ('SIDE-effects', os.path.join('D:', os.sep, 'SIDE-effects'), 'ef4cff7')):
    _rc, head = git(repo, 'rev-parse', '--short', 'HEAD')
    # ### REPAIRED AFTER RUN 1: `git()` strips the output, so the first porcelain line lost its
    # ### leading column and a fixed slice cut a letter from its path. ### The path is now taken
    # ### after the status field, whatever its width. ### Run 1 is kept as `b418_extract_run1.txt`.
    _rc, st = git(repo, 'status', '--porcelain')
    tracked = [' ' + x.split(None, 1)[-1] if len(x.split(None, 1)) == 2 else x
               for x in st.splitlines() if x.strip() and not x.startswith('??')]
    _rc, staged = git(repo, 'diff', '--cached', '--name-only')
    say('  %-20s HEAD %s (pin %s)  staged %d  tracked-modified %d %s'
        % (nm, head, pin, len([x for x in staged.splitlines() if x]), len(tracked),
           # ### REPAIRED AFTER RUN 2: run 2's repair fixed the parse and left the print's fixed
           # ### slice in place, so it cut two letters instead of one. ### Run 2 is kept too.
           [x.strip() for x in tracked]))
cl = read(os.path.join(D, 'b417_closing.txt'))
say('  b417`s defect report in its closing  : %s' % ('Component 1 — the defect report' in cl))
say('  b417`s two-readings table            : %s' % ('**reading (a)**: the sentence is right' in cl))
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m417 = [int(m.group(1)) for m in re.finditer(
    r'(?m)^\| (\d+) \| \*\*READING \(a\) WOULD LEAVE TWO DISTINCT TUPLES', corr)]
say('  correspondence row 266, by b417`s marker : %s' % m417)
if m417 != [266]:
    MISS.append('b417`s correspondence row is not at 266 by its marker')
cls = read(os.path.join(FA, 'Classes.lean'))
say('  the kernel`s classA_distinct_from_classD : %s'
    % ('theorem classA_distinct_from_classD' in cls))
say()

# =============================================================================================
rule()
say('### READ 1 -- THE WALKER. ### THE IGNORE HYPOTHESIS FIRST, THEN THE MISS, THEN THE POPULATION.')
rule()
calls = []
for sid, t0, t1 in ARC:
    fp = os.path.join(TD, sid + '.jsonl')
    uses, results = {}, {}
    for line in io.open(fp, encoding='utf-8', errors='replace'):
        try:
            o = json.loads(line)
        except Exception:
            continue
        c = (o.get('message') or {}).get('content')
        if not isinstance(c, list):
            continue
        for b in c:
            if b.get('type') == 'tool_use' and b.get('name') == 'Grep':
                uses[b['id']] = (o.get('timestamp'), o.get('version'), b.get('input') or {})
            if b.get('type') == 'tool_result' and b.get('tool_use_id') in uses:
                txt = b.get('content')
                if isinstance(txt, list):
                    txt = ' '.join(x.get('text', '') for x in txt if isinstance(x, dict))
                results[b['tool_use_id']] = (o.get('timestamp'), o.get('toolUseResult'), txt or '')
    for k, (t, ver, inp) in uses.items():
        if not (t0 <= (t or '') < t1):
            continue
        rt, tur, txt = results.get(k, (None, None, ''))
        dur = (ts(rt) - ts(t)).total_seconds() if ts(rt) and ts(t) else None
        tur = tur if isinstance(tur, dict) else {}
        calls.append(dict(session=sid[:8], at=t, version=ver, path=inp.get('path') or '(cwd)',
                          pattern=inp.get('pattern', ''), glob=inp.get('glob'),
                          mode=inp.get('output_mode') or 'files_with_matches',
                          seconds=dur, numFiles=tur.get('numFiles'),
                          numMatches=tur.get('numMatches'),
                          timed_out='timed out' in (txt or ''),
                          empty=bool(re.search(r'^No (files|matches) found', (txt or '').strip())),
                          head=(txt or '').strip().splitlines()[0][:90] if (txt or '').strip() else ''))
say('  ### **(a) THE IGNORE HYPOTHESIS, TESTED ON THE REPOSITORY`S OWN CHECK.**')
srcs = [f for f in ('.gitignore', '.ignore', '.rgignore', 'data/.gitignore', 'data/.ignore',
                    'data/.rgignore') if os.path.exists(os.path.join(ROOT, f))]
say('      ignore files ripgrep honours, present in relay : %s' % srcs)
say('      core.excludesFile : %r' % git(ROOT, 'config', '--get', 'core.excludesFile')[1])
gi = read(os.path.join(ROOT, '.gitignore'))
say('      .gitignore lines naming data/ as a pattern : %d'
    % len([x for x in gi.splitlines() if x.strip() and not x.startswith('#') and 'data' in x]))
_rc, ci = git(ROOT, 'ls-files', '-ci', '--exclude-standard')
say('      tracked files any ignore pattern matches : %d' % len([x for x in ci.splitlines() if x]))
miss417 = next((c for c in calls if 'BoundaryValueShadow' in c['pattern'] and c['session'] == 'fbe6b4b2'), None)
say()
say('  ### **(b) THE MISS, FROM THE TRANSCRIPT`S OWN METADATA.**')
if miss417:
    say('      b417`s call at %s, version %s, mode %s' % (miss417['at'], miss417['version'], miss417['mode']))
    say('      ### ### **DURATION %.2f s ; numFiles %s ; numMatches %s ; timeout text present : %s**'
        % (miss417['seconds'] or -1, miss417['numFiles'], miss417['numMatches'], miss417['timed_out']))
else:
    MISS.append('b417`s missed call is not found in the transcript')
# ### the replay taken at resume, in this session's transcript after the b418 paste
rep = None
for line in io.open(os.path.join(TD, ARC[1][0] + '.jsonl'), encoding='utf-8', errors='replace'):
    try:
        o = json.loads(line)
    except Exception:
        continue
    tur = o.get('toolUseResult')
    if (o.get('timestamp') or '') > '2026-09-11T14:12:59' and isinstance(tur, dict) \
            and tur.get('mode') == 'count' and 'b416_components.txt:14' in (tur.get('content') or ''):
        rep = tur
say('      the same query replayed at resume : numFiles %s ; numMatches %s'
    % ((rep or {}).get('numFiles'), (rep or {}).get('numMatches')))
got417 = set(re.findall(r'data\\(\S+?):\d+', (miss417 or {}).get('head', '') + ' '))
full417 = set()
for sid, _t0, _t1 in ARC[1:]:
    for line in io.open(os.path.join(TD, sid + '.jsonl'), encoding='utf-8', errors='replace'):
        if '"numFiles": 13' in line or '"numFiles":13' in line:
            try:
                o = json.loads(line)
            except Exception:
                continue
            tur = o.get('toolUseResult')
            if isinstance(tur, dict) and tur.get('numFiles') == 13 and 'b221_core_remeasured' in (tur.get('content') or ''):
                full417 = set(re.findall(r'data\\(\S+?):\d+', tur['content']))
rep_set = set(re.findall(r'data\\(\S+?):\d+', (rep or {}).get('content', '')))
existed = sorted(f for f in rep_set - full417
                 if os.path.exists(os.path.join(D, f)) and
                 datetime.utcfromtimestamp(os.path.getmtime(os.path.join(D, f))) < ts(miss417['at']))
say('      files the replay reaches and b417`s call did not, existing (by mtime) before that call : ### **%d**'
    % len(existed))
for f in existed:
    rc, out = git(ROOT, 'check-ignore', '-v', '--no-index', 'data/' + f)
    say('          %-44s repository ignore check : %s' % (f, out or 'NOT IGNORED (exit %d)' % rc))
say('  ### ### **THE WALKER WITH IGNORE RULES DISABLED COULD NOT BE RUN AS A SEPARATE BINARY**: its')
say('  ### ripgrep is embedded in the Claude Code executable and exposes no flag to this seat. ### The')
say('  ### substitute is stronger: the walker WITH its ignore rules on reaches every one of these files')
say('  ### at resume (the replay), so no ignore rule excludes them.')
say()
say('  ### **(c) THE ARC`S WALKER POPULATION** -- every `Grep` call from b413`s paste to b418`s, by transcript.')
say('      calls in the arc : %d' % len(calls))
over = [c for c in calls if 'relay' in (c['path'] or '').lower()]
say('      calls whose path is relay or under it : %d' % len(over))
say('      of those, over relay`s data records (path is relay\\data, or relay itself) : %d'
    % len([c for c in over if re.search(r'relay(\\data)?\\?$', c['path'].rstrip('\\'), re.I)
           or c['path'].lower().rstrip('\\').endswith('relay\\data')]))
say('      %-9s %-24s %-7s %-6s %-5s %-5s %-28s %s' % ('session', 'at', 'secs', 'files', 'empty', 'limit', 'path', 'pattern'))
for c in over:
    say('      %-9s %-24s %-7s %-6s %-5s %-5s %-28s %s'
        % (c['session'], c['at'][:23], '%.1f' % c['seconds'] if c['seconds'] is not None else '?',
           c['numFiles'], c['empty'], c['timed_out'] or (c['seconds'] or 0) >= 19.5,
           c['path'][-28:], c['pattern'][:60]))
json.dump(over, io.open(POPOUT, 'w', encoding='utf-8'), indent=1)
say('      written : %s' % os.path.basename(POPOUT))
say()

# =============================================================================================
rule()
say('### READ 2 -- (R35)`S TARGETS: THE SENTENCE IN THE OWNER, AND THE CITER THAT IS NOT THE OWNER.')
rule()
quote('the sentence, in the abstract', MATTER, 'Three of four formation components are universal', ':')
quote('the sentence, in section I', MATTER, 'Three of four components are universal', ':')
quote('its n2 theorem`s own hypothesis', MATTER, '**Theorem (n₂ = 3).**', NL)
b = blob(PP, PIN_PP, 'phase2/physics/MATTER_AS_ARITHMETIC.md') or b''
say('  MATTER at the starting pin %s : %d bytes, sha256 %s' % (PIN_PP, len(b), hashlib.sha256(b).hexdigest()[:16]))
say('  ### the ferry names *the two citers of the sentence*; b417 counted TWO LIVE CITERS INCLUDING THE')
say('  ### OWNER -- MATTER itself and AT_REST. ### So the citer that is not the owner is ONE:')
quote('AT_REST`s citation', ATREST, 'We proved three of four components universal', '.')
quote('AT_REST`s n2 paragraph', ATREST, '**n₂ = 3 universally.**', NL)
at = read(ATREST)
say('  AT_REST ends with a newline : %s ; last line : %r' % (at.endswith(NL), at.rstrip(NL).splitlines()[-1][:80]))
say()

# =============================================================================================
rule()
say('### READ 3 -- THE THREE REPAIRS` TARGETS, AND THE RULES THAT GOVERN EACH.')
rule()
quote('the keystone`s sentence about 43', CONST, 'Beyond 41, the lattice has gaps.', NL)
creg = [x for x in read(REG).splitlines() if 'phase1.5/deep-structure/CONSTANCE.md' in x and x.startswith('| 1.5e-1')]
say('  CONSTANCE`s registry row class : %s' % (re.search(r'\*\*(RECLASSIFIED[^*]*)\*\*', creg[0]).group(1)
                                               if creg else '(anchor miss)'))
quote('the taxonomy`s Tier C clause', TAX, '**Tier C — Cluster-synthesis.**', NL)
say('  the taxonomy carries any clause forbidding an edit to a tier : %s'
    % bool(re.search(r'(may not|must not|never) be (edited|amended|corrected)', read(TAX), re.I)))
say()
p235 = [x for x in read(REG).splitlines() if x.startswith('| p2-35 |')]
say('  registry row p2-35 present : %s' % bool(p235))
for needle in ('a three-clause currency note', 'where the lattice carries six sum-of-powers primes'):
    say('      stale figure %-52r present : %s' % (needle, bool(p235) and needle in p235[0]))
b372 = [f for f in os.listdir(D) if f.startswith(('b371_', 'b372_')) and f.endswith('.txt')]
rule_hits = [(f, x.strip()) for f in b372 for x in read(os.path.join(D, f)).splitlines()
             if 'REMOVED RATHER THAN RESTATED' in x.upper()]
say('  the stale-figure rule in b371/b372`s own records (by its words) : %d line(s)' % len(rule_hits))
for f, x in rule_hits[:3]:
    say('      %s : %s' % (f, x[:140]))
say()
hy = os.path.join(T, 'b369_hygiene.py')
say('  tools/b369_hygiene.py present : %s' % os.path.exists(hy))
refs = sorted(f for f in os.listdir(T) if f.endswith('.py') and f != 'b369_hygiene.py'
              and 'b369_hygiene' in read(os.path.join(T, f)))
say('  relay tools naming it : %d -- %s' % (len(refs), ', '.join(refs)))
say('  a retired directory anywhere in relay : %s'
    % [d for d, _s, _f in os.walk(ROOT) if '.git' not in d and 'retire' in os.path.basename(d).lower()])
live = read(os.path.join(D, 'b417_live.txt'))
say('  its last verdict, from b417`s live record : %s'
    % (re.search(r'COMPONENT 2 : (\w+)', live).group(1) if 'COMPONENT 2 :' in live else '(anchor miss)'))
say()

# =============================================================================================
rule()
say('### READ 4 -- (N): THE OPEN STATEMENT, AND WHAT THE KERNEL ALREADY SUPPLIES.')
rule()
quote('the named open statement', os.path.join(CORE, 'SinglePrimeFactor.lean'),
      'For every base `p` with `singlePrimeFactor p = true`', 'THIS IS NOT PROVED')
seal = read(os.path.join(CORE, 'FiniteSideSeal.lean'))
thms = re.findall(r'(?m)^theorem (\S+)', seal)
say('  FiniteSideSeal.lean theorems : %d -- %s' % (len(thms), ', '.join(thms)))
counting = []
for f in sorted(os.listdir(CORE)):
    if f.endswith('.lean'):
        for m in re.finditer(r'(?m)^theorem (\S+)[^:]*:[^\n]*(length|foldl|filter|List\.sum|count)', read(os.path.join(CORE, f))):
            counting.append('%s.%s' % (f[:-5], m.group(1)))
say('  Core/ theorems whose STATEMENT line names a length, foldl, filter, sum or count : %d %s'
    % (len(counting), counting[:8]))
probe = read(os.path.join(D, 'b329_axiom_probe.txt'))
for nm in ('List.all_eq_true', 'List.length_filter', 'List.filter_cons', 'List.foldl', 'Nat.mod_eq_of_lt',
           'Nat.div_mul_cancel', 'Nat.gcd'):
    hitl = [x.strip() for x in probe.splitlines() if nm in x]
    say('      b329`s axiom probe on %-22s : %s' % (nm, hitl[0][:90] if hitl else '(not probed)'))
say()

# =============================================================================================
rule()
say('### READ 5 -- THE THREE EXAMPLE SYSTEMS: WHERE EACH DOCUMENT PLACES EACH, WITH ITS CONTEXT.')
rule()
TUP = re.compile(r'\(\s*[23]\s*,\s*[23]\s*,\s*2\s*,\s*0\s*\)|Class [ABCD]\b|— (Arithmetic|Gravitational|Gauge|Information)')
for sysname in ('genetic code', 'Shannon', 'Navier'):
    say('  ### %s' % sysname)
    for rel in ('phase2/physics/MATTER_AS_ARITHMETIC.md', 'phase2/formation/COMPLEX_ANALYSIS.md'):
        src = read(os.path.join(PP, rel.replace('/', os.sep)))
        for i, ln in enumerate(src.splitlines(), start=1):
            if sysname.lower() in ln.lower():
                t = TUP.search(ln)
                say('      %-26s line %-4d tuple on line : %-12s %s'
                    % (rel.split('/')[-1][:26], i, t.group(0) if t else '-', re.sub(r'\s+', ' ', ln)[:120]))
quote('Gate 1b`s note', os.path.join(PP, 'phase2', 'formation', 'COMPLEX_ANALYSIS.md'), '> **Note (Gate 1b).**', NL)
say()

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : 6')
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if MISS else 0)
