# -*- coding: utf-8 -*-
"""b419_extract.py -- THE SURVEY FOR b419. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### Three components, small on purpose: the helper, the lock-versus-scan price, and the silent
### timeouts outside b418's arc. ### **NO PROBE IS COMPILED HERE** -- the survey reads the banked attempt,
### the kernel's state and the transcripts; the compile is Component 1's, after the lock.
"""
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
TD = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
OUT = os.path.join(D, 'b419_extract.txt')
POPOUT = os.path.join(D, 'b419_timeout_population.json')
LIMIT, MARGIN = 20.0, 0.5
NL = chr(10)
L, MISS = [], []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


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
say('b419_extract.py -- THE SURVEY: THE HELPER, THE LOCK AND THE SCAN, AND THE SILENT TIMEOUTS.')
rule('=')
say()

rule()
say('### READ 0 -- THE ORIENTATION CITATIONS.')
rule()
natt = read(os.path.join(D, 'b418_n_attempt.txt'))
say('  b418_n_attempt.txt present : %s ; probes banked : %d' % (bool(natt), len(re.findall(r'(?m)^### p\d\d\.lean', natt))))
quote('the fix b418 named', os.path.join(D, 'b418_components.txt'), '### ### **THE NEXT STEP, NAMED:**', 'NOT COMPILED HERE')
quote('the error b418 read', os.path.join(D, 'b418_components.txt'), 'in this toolchain `Nat.pow_succ` TAKES', '### Every')
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m418 = [int(m.group(1)) for m in re.finditer(r"(?m)^\| (\d+) \| \*\*THE GENERAL CLAUSE IS OVER-BUDGET", corr)]
say('  correspondence row 267, by b418`s marker : %s' % m418)
if m418 != [267]:
    MISS.append('b418`s row is not at 267 by its marker')
say()

rule()
say('### READ 1 -- THE KERNEL`S STATE, AND THE SEAL`S CAVEAT WITH ITS DRAFTED ANNOTATION.')
rule()
core = sorted(f for f in os.listdir(os.path.join(KERN, 'Core')) if f.endswith('.lean'))
say('  Core/ modules : %d' % len(core))
ap = read(os.path.join(KERN, 'AllPrints.lean'))
say('  AllPrints.lean : imports %d, #print lines %d' % (len(re.findall(r'(?m)^import ', ap)), len(re.findall(r'(?m)^#print axioms', ap))))
hb = subprocess.run(['git', '-C', KERN, 'show', 'HEAD:AXIOM_PRINTS.txt'], capture_output=True).stdout
say('  AXIOM_PRINTS.txt at HEAD : %d lines, sha256 %s' % (hb.count(b'\n'), hashlib.sha256(hb).hexdigest()[:16]))
say('  profile lines not saying "does not depend on any axioms" : %d'
    % len([x for x in hb.decode('utf-8', 'replace').splitlines() if x.strip() and 'does not depend on any axioms' not in x]))
seal = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
quote('the seal`s (T1.4)', seal, 'Coprime`\'s lemmas carry `propext`', 'compiled here);')
ann = read(os.path.join(D, 'b416_components.txt'))
i = ann.find('(T1.4-a, b414)')
say('  b416`s drafted annotation, verbatim from its record :')
for ln in ann[i - 10:i + 600].splitlines():
    if ln.strip().startswith('|'):
        say('      %s' % ln.strip())
if i < 0:
    MISS.append('b416`s drafted annotation is absent')
say('  the annotation already in the seal : %s' % ('(T1.4-a, b414)' in read(seal)))
say('  oleans present for FiniteSideSeal and SinglePrimeFactor : %s'
    % all(os.path.exists(os.path.join(KERN, 'build', f + '.olean')) for f in ('FiniteSideSeal', 'SinglePrimeFactor')))
say()

rule()
say('### READ 2 -- b414`S TWENTY-EIGHT SENTENCES, AND THE SORT THAT GOVERNS.')
rule()
b414 = read(os.path.join(D, 'b414_components.txt'))
for needle in ('GROUP A : 2', 'GROUP B : 26', 'GROUP A -- A PROOF WOULD MAKE THESE TRUE AS WRITTEN : 8',
               'GROUP B -- A PROOF WOULD LEAVE THESE EXACTLY AS THEY ARE : 20'):
    k = b414.find(needle)
    say('  %-72s line %s' % (needle, b414[:k].count(NL) + 1 if k >= 0 else '### MISS'))
say()

rule()
say('### READ 3 -- THE LOCK AND THE SCAN: THE TWO RULES, AND THE THREE ROUTES b418 NAMED.')
rule()
quote('the lock gate`s ferry gate', os.path.join(T, 'b378_lockgate.py'), "('the ferry scan (struck clauses and stems)'", NL + "    ('the handoff census'")
quote('the scan`s own doctrine', os.path.join(T, 'ferry_scan.py'), '# ### (1) ### **A HIT IS A STRING, NOT A FAULT.**', '# ### (2)')
quote('the three routes', os.path.join(D, 'b418_halt.txt'), '### WHAT WOULD LET THE ACT RESUME', '====')
say()

rule()
say('### READ 4 -- EVERY WALKER CALL IN EVERY TRANSCRIPT THAT REACHED THE LIMIT.')
rule()
pastes = []
calls = []
for fp in sorted(glob.glob(os.path.join(TD, '*.jsonl'))):
    sid = os.path.basename(fp)[:8]
    msgs = {}
    uses, results = {}, {}
    for line in io.open(fp, encoding='utf-8', errors='replace'):
        try:
            o = json.loads(line)
        except Exception:
            continue
        c = (o.get('message') or {}).get('content')
        if o.get('type') == 'user' and isinstance(c, str) and 'paste begins' in c:
            m = re.search(r'ACT (b\d+)', c)
            if m:
                pastes.append((sid, o.get('timestamp') or '', m.group(1)))
        if not isinstance(c, list):
            continue
        mid = (o.get('message') or {}).get('id') or o.get('uuid')
        for b in c:
            if b.get('type') == 'tool_use':
                msgs.setdefault(mid, []).append(b.get('name'))
                if b.get('name') == 'Grep':
                    uses[b['id']] = (o.get('timestamp'), b.get('input') or {}, mid)
            elif b.get('type') == 'tool_result' and b.get('tool_use_id') in uses:
                txt = b.get('content')
                if isinstance(txt, list):
                    txt = ' '.join(x.get('text', '') for x in txt if isinstance(x, dict))
                results[b['tool_use_id']] = (o.get('timestamp'), o.get('toolUseResult'), txt or '')
    for k, (at, inp, mid) in uses.items():
        rt, tur, txt = results.get(k, (None, None, ''))
        if not (ts(at) and ts(rt)):
            continue
        secs = (ts(rt) - ts(at)).total_seconds()
        if secs < LIMIT - MARGIN:
            continue
        tur = tur if isinstance(tur, dict) else {}
        calls.append(dict(session=sid, at=at, seconds=round(secs, 2), path=inp.get('path') or '(cwd)',
                          pattern=inp.get('pattern', ''), glob=inp.get('glob'), mode=inp.get('output_mode'),
                          numFiles=tur.get('numFiles'), timed_out='timed out' in txt,
                          empty=bool(re.search(r'^No (files|matches) found', txt.strip())),
                          siblings=len(msgs.get(mid, [])) - 1, content=(tur.get('content') or '')[:4000]))
# ### ### **THE ACT IS MAPPED BY THE RELAY'S OWN COMMITS, NOT BY PASTE TEXT** -- run 1 found act pastes in
# ### only the latest sessions, since older ferries did not open with the words this read looked for.
# ### The act under way at a call is the act of the FIRST relay commit at or after it whose subject opens
# ### with an act number; the gap to that commit is printed, so a weak mapping is visible, not hidden.
log = subprocess.run(['git', '-C', ROOT, 'log', '--format=%cI %s'], capture_output=True, text=True,
                     encoding='utf-8', errors='replace').stdout.splitlines()
acts = []
for ln in log:
    stamp, _, subj = ln.partition(' ')
    m = re.match(r'\W*(b\d{3})\b', subj)
    if m:
        acts.append((datetime.fromisoformat(stamp).astimezone(tz=None).timestamp(), m.group(1)))
acts.sort()
for c in calls:
    t = datetime.strptime(c['at'][:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=timezone.utc).timestamp()
    nxt = [a for a in acts if a[0] >= t]
    prior = sorted((p for p in pastes if p[0] == c['session'] and p[1] <= c['at']), key=lambda p: p[1])
    c['act_by_paste'] = prior[-1][2] if prior else None
    c['act'] = nxt[0][1] if nxt else '(after the last act commit)'
    c['gap_hours'] = round((nxt[0][0] - t) / 3600.0, 2) if nxt else None
    p = c['path'].lower().rstrip('\\/')
    c['scope'] = ('INSIDE RELAY' if 'relay' in p else
                  'AN ANCESTOR OF RELAY' if p in ('d:', 'd:\\', '(cwd)') else 'ELSEWHERE')
say('  act commits in the relay log : %d ; first at %s' % (len(acts), datetime.fromtimestamp(acts[0][0]).isoformat()[:19]))
relay = [c for c in calls if c['scope'] != 'ELSEWHERE']
say('  act pastes found across the transcripts : %d' % len(pastes))
say('  walker calls that reached the limit, every transcript : %d ; timeout text present : %d ; silent : %d'
    % (len(calls), len([c for c in calls if c['timed_out']]), len([c for c in calls if not c['timed_out']])))
say('  ### of those, over relay or a directory holding it (the scored population) : %d' % len(relay))
say('  ###   inside relay : %d ; an ancestor of relay : %d ; elsewhere (listed, not scored) : %d'
    % (len([c for c in calls if c['scope'] == 'INSIDE RELAY']),
       len([c for c in calls if c['scope'] == 'AN ANCESTOR OF RELAY']),
       len([c for c in calls if c['scope'] == 'ELSEWHERE'])))
say('  %-9s %-20s %-6s %-5s %-6s %-5s %-5s %-6s %-9s %-24s %s'
    % ('session', 'at (UTC)', 'secs', 'files', 'said', 'batch', 'act', 'gap h', 'scope', 'path', 'pattern'))
for c in sorted(calls, key=lambda c: c['at']):
    say('  %-9s %-20s %-6s %-5s %-6s %-5s %-5s %-6s %-9s %-24s %s'
        % (c['session'], c['at'][:19], c['seconds'], c['numFiles'], c['timed_out'], c['siblings'],
           c['act'][:5], c['gap_hours'], c['scope'][:9], c['path'][-24:], c['pattern'][:40]))
say('  ### where a paste in the call`s own session names an act, the two mappings are compared :')
for c in calls:
    if c['act_by_paste']:
        say('      %s %s : by commit %s, by paste %s -- %s' % (c['session'], c['at'][11:19], c['act'], c['act_by_paste'],
            'AGREE' if c['act'] == c['act_by_paste'] else 'DIFFER'))
json.dump(calls, io.open(POPOUT, 'w', encoding='utf-8'), indent=1)
say('  written : %s' % os.path.basename(POPOUT))
say('  ### ### **A CALL ISSUED BESIDE SIBLINGS (batch > 0) CARRIES ITS MESSAGE`S TIME, NOT ITS OWN**, so its')
say('  ### duration is an upper bound and the guard cannot be applied to it retroactively.')
say()

rule()
say('### READ 5 -- THE FOUR OPEN LISTS, AS THE RECORD LAST RESTATED THEM.')
rule()
quote('the four lists', os.path.join(PP, 'OPEN_TRAILS.md'), '**LIST 1** — the rows that cite', 'was not sent to.**')
quote('their trigger', os.path.join(PP, 'OPEN_TRAILS.md'), 'Trigger: the ruling on which test governs', '.')
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
sys.exit(1 if MISS else 0)
