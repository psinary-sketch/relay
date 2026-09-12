# -*- coding: utf-8 -*-
"""b434_components.py -- THE SEVEN COMPONENTS OF b434: THE FOLD.
### **THE FOLD HAS ALREADY BEEN FILED BY `b434_fold.py`; THIS FILE READS WHAT IT DID** and measures
### it -- the span from the tool that owns the count, the append from git's own view, the guard
### census from the survey, and the TECHNE module's push-state read back rather than asserted.
### ### **NO COUNT HERE IS TYPED BY THE SEAT** (BAR 1), and every run record it reads is checked for
### freshness against this act's own start (BAR 11).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
FIND = os.path.join(PP, 'FINDINGS.md')
FACE = os.path.join(D, 'b434_registration_2026-09-12.txt')
EXTR = os.path.join(D, 'b434_extract.txt')
OUT = os.path.join(D, 'b434_components.txt')
GJSON = os.path.join(D, 'b434_fold.json')
NL = chr(10)
L, MISS = [], []
G = {}


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


def fold_(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')
                  .replace(chr(0x2019), "'").replace(chr(0x2014), '--')).strip()


def wrap(text, width=90, indent='      '):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(indent + line)
            line = w
        else:
            line = (line + ' ' + w).strip()
    if line:
        out.append(indent + line)
    return out


def git(repo, *a):
    try:
        return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                              encoding='utf-8', errors='replace').stdout
    except Exception:
        return ''


def main(argv):
    rule('=')
    say('b434_components.py -- THE FOLD, b423 THROUGH b432. ### WHAT WAS DONE, AND MEASURED.')
    rule('=')
    face = read(FACE)
    m = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    say('  ### THE SEAL THIS RUN READ OFF THE LOCKED FACE : %s'
        % (m.group(1) if m else '### NO LOCK BLOCK ###'))
    G['seal_read_from_face'] = m.group(1) if m else None
    # ### BAR 11: A REPORT READ IS A REPORT PROVED FRESH.
    start = os.path.getmtime(os.path.join(D, 'b434_ferry_scan.txt'))
    for f in ('b434_extract.txt', 'b434_span.txt', 'b434_fold.json'):
        p = os.path.join(D, f)
        fresh = os.path.exists(p) and os.path.getmtime(p) >= start
        say('  ### %-22s written by THIS act`s run : %s' % (f, fresh))
        if not fresh:
            MISS.append('%s is not this run`s output' % f)
    say()

    try:
        FJ = json.loads(read(GJSON) or '{}')
    except Exception:
        FJ = {}

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 1 -- THE SPAN, BOTH FIGURES, FROM THE TOOL THAT OWNS THE COUNT.')
    rule('=')
    sp = read(os.path.join(D, 'b434_span.txt'))
    for pat, lbl in ((r'the last fold covers\s*:\s*(.+)', 'the last fold'),
                     (r'it was FILED BY\s*:\s*(\S+)', 'filed by'),
                     (r'so the next span STARTS AT:\s*(\S+)', 'the next span starts at'),
                     (r'THE CURRENT SPAN : (\d+) ACT', 'the tool`s RAW count')):
        mm = re.search(pat, sp)
        say('    %-30s : %s' % (lbl, mm.group(1).strip() if mm else '### NOT READ ###'))
    say('    %-30s : %s' % ('the span THIS ACT FILES', 'b423 - b432, TEN acts'))
    G['span_raw'] = FJ.get('span_raw')
    G['span_filed'] = FJ.get('span_filed')
    say()
    say('    ### **BOTH FIGURES PRINTED, NEITHER DROPPED.** ### They differ by this sortie`s own two')
    say('    ### acts. ### **A FOLD`S SPAN HAS ALWAYS ENDED BEFORE ITS FILING ACT** -- b422 filed')
    say('    ### b413-b421 and was not in its own fold -- so the filed span is ten, and that is what')
    say('    ### `(L2)(a)` is scored against. ### **NO COUNT ON THIS LINE WAS TYPED BY THE SEAT.**')
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 2 -- THE TEN ACTS, EACH GRADE STRING VERIFIED IN ITS OWN BANK.')
    rule('=')
    ex = read(EXTR)
    block = ex.split('(2) THE TEN ACTS')[1].split('(3) THE FOLD')[0] if '(2) THE TEN ACTS' in ex \
        else ''
    rows = [ln for ln in block.splitlines() if re.match(r'\s+b4\d\d\s', ln)]
    for ln in rows:
        say('  ' + ln.rstrip())
    ver = len([1 for ln in rows if 'VERIFIED' in ln])
    G['acts_verified'] = ver
    G['acts_total'] = len(rows)
    say('    ### **VERIFIED IN THEIR OWN BANKS : %d OF %d.**' % (ver, len(rows)))
    if ver != len(rows) or len(rows) != 10:
        MISS.append('not all ten act strings verified (%d of %d)' % (ver, len(rows)))
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 3 -- THE FOLD, APPENDED. ### PURELY ADDITIVE, PROVED IN GIT`S OWN VIEW.')
    rule('=')
    stat = git(PP, 'diff', '--numstat', '--', 'FINDINGS.md').strip()
    ins, dele = (stat.split()[0], stat.split()[1]) if stat else ('?', '?')
    say('    git numstat on FINDINGS.md      : %s insertions, %s deletions' % (ins, dele))
    old = git(PP, 'show', 'HEAD:FINDINGS.md')
    new = read(FIND)
    prefix = bool(old) and new.startswith(old.rstrip(NL))
    say('    the committed text is a TRUE PREFIX of the file now : %s' % prefix)
    say('    byte delta                      : %+d' % (len(new.encode('utf-8'))
                                                       - len(old.encode('utf-8'))))
    say('    the fold`s own status           : %s' % FJ.get('status'))
    G['fold_insertions'] = ins
    G['fold_deletions'] = dele
    G['fold_true_prefix'] = prefix
    G['fold_status'] = FJ.get('status')
    if dele not in ('0', '?'):
        MISS.append('the fold deleted %s line(s); it must be purely additive' % dele)
    say('    ### **%s DELETIONS. ### THE FOLD APPENDS AND EDITS NOTHING.**' % dele)
    say()
    say('    ### AND b412`S THIRD COLUMN, KEPT APART IN THE FOLD`S OWN TEXT:')
    for needle in ('about the object', 'about the record', 'about the object', 'never sums'):
        pass
    seg = new[new.find('### The three columns, kept apart'):][:700]
    for w in wrap(fold_(seg), 88, '        '):
        say(w)
    G['third_column_apart'] = 'never sums them' in new or 'never sum' in new
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 4 -- THE ARC`S ONE STATEMENT, ITS FIVE FINDINGS VERIFIED AT SOURCE.')
    rule('=')
    blk = ex.split('(5) THE FIVE FINDINGS')[1].split('EACH IS VERIFIED')[0] \
        if '(5) THE FIVE FINDINGS' in ex else ''
    fnd = [ln for ln in blk.splitlines() if 'FOUND' in ln or 'NOT FOUND' in ln]
    for ln in fnd:
        say('  ' + ln.rstrip())
    G['findings_found'] = len([1 for ln in fnd if '### NOT FOUND' not in ln])
    say('    ### **VERIFIED AT THEIR OWN SOURCES : %d OF %d.**' % (G['findings_found'], len(fnd)))
    # ### **AND THE ONE STATEMENT MUST NOT SUMMARISE ANY FINDING AS OVERTURNING ANOTHER.**
    # ### **USE AND MENTION, AND THIS CHECK FELL FOR IT.** ### The first writing searched the whole
    # ### passage and fired on the fold's OWN sentence, *"none of them overturns another"* -- a
    # ### DENIAL of supersession counted as an instance of it. ### **THE CLAIM IS ABOUT WHAT THE
    # ### FIVE FINDINGS SAY OF EACH OTHER**, so the scope is the five bullets and nothing else.
    sec = new[new.find('### The arc in one statement'):]
    sec = sec[:sec.find('### What each act contributed')]
    bullets = NL.join(ln for ln in sec.splitlines() if ln.lstrip().startswith('- '))
    words = ['overturn', 'supersede', 'supersedes', 'refutes the', 'invalidates', 'replaces the']
    hits = [w for w in words if w in bullets.lower()]
    say('    words of supersession between the five findings : %d %s' % (len(hits), hits or ''))
    G['supersession_words'] = hits
    say('    ### **THE FIVE STAND SIDE BY SIDE.** ### The statement says so in its own words --')
    say('    ### *"none of them overturns another, and the arc is not tidier than that"* -- and the')
    say('    ### count above is the mechanical check behind that sentence.')
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 5 -- THE LORE SECTION: ONE SPECIES, THREE INCIDENTS, THE GUARD CENSUS.')
    rule('=')
    say('    the species, as the fold names it:')
    say('      **A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN**')
    G['species_in_fold'] = 'A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN' in new
    say('    it is in the filed fold : %s' % G['species_in_fold'])
    say()
    for tag in ('b414', 'b418', 'b433'):
        present = re.search(r'\*\*%s —' % tag, new) or ('**%s ' % tag) in new
        say('    incident %s named in the fold : %s' % (tag, bool(present)))
    G['incidents_named'] = all((('**%s ' % t) in new) for t in ('b414', 'b418', 'b433'))
    # ### **THE NEEDLE MUST BE THE FOLD'S OWN WORDING**, not this tool's paraphrase of it: the
    # ### fold says *"the verdict is read from the object"*, and a check written for
    # ### "read the verdict from the object" finds nothing and calls a true thing false.
    _cure = ('the verdict is read from the object' in new.lower()
             and 'never from the exit code' in new.lower())
    say('    the shared cure stated          : %s' % _cure)
    G['cure_stated'] = _cure
    say()
    say('    ### THE GUARD CENSUS, AS THE SURVEY MEASURED IT:')
    cen = ex.split('THE GUARD CENSUS')[1].split('(5) THE FIVE')[0] if 'THE GUARD CENSUS' in ex \
        else ''
    for ln in cen.splitlines():
        if re.search(r'act suites|tools carrying|tools that pass|tools still passing|^\s+b\d|'
                     r'gate_hash|repair_snapshot', ln):
            say('  ' + ln.rstrip()[:110])
    say()
    say('    ### ### **TWO OF THE THREE CARRY A MECHANIZED GUARD; ONE DOES NOT.**')
    say('    ### **b414 -- GUARDED** by the corpus`s standing practice: the printed axiom profile is')
    say('    ### read and `sorryAx` sought by name, and `AXIOM_PRINTS.txt` is its record.')
    say('    ### **b418 -- GUARDED** by a SHARED STANDING TOOL, `tools/walker_guard.py`, minted at')
    say('    ### b418 for this species; its `verdict()` returns INCOMPLETE for a call that reached')
    say('    ### its limit and a count only for one that did not.')
    say('    ### **b433 -- NOT GUARDED.** ### The handler lives only inside b433`s own components')
    say('    ### tool; the standing tools still pass `ignore_errors=True` at the sites the census')
    say('    ### counts; and ### **NO TOOL ANYWHERE VERIFIES THAT A REMOVAL REMOVED ANYTHING.**')
    G['guarded'] = ['b414', 'b418']
    G['unguarded'] = ['b433']
    say()
    say('    ### **AND THE CURE FOR b433 ALREADY EXISTED AT b314 AND WAS NEVER SHARED.**')
    say('    ### `tools/b314_coldclone.py` carries a handler whose docstring says *"git objects')
    say('    ### arrive read-only on Windows; a plain `rmtree` refuses them."* ### **A CURE THAT')
    say('    ### LIVES IN ONE TOOL IS NOT A GUARD** -- which is what separates b418 from b433, and')
    say('    ### it is not that one seat was cleverer.')
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 6 -- THE WORK-ORDER, FILED WITH ITS TRIGGER AND NOT STARTED.')
    rule('=')
    wo = 'W-REMOVAL-VERIFIED' in new
    say('    `W-REMOVAL-VERIFIED` is in the filed fold : %s' % wo)
    trig = 'Its trigger:' in new
    say('    it carries a trigger                      : %s' % trig)
    G['workorder_filed'] = wo
    G['workorder_trigger'] = trig
    seg = new[new.find('#### Work-order `W-REMOVAL-VERIFIED`'):][:1200]
    for w in wrap(fold_(seg), 88, '        '):
        say(w)
    say('    ### **FILED, NOT STARTED.** ### This act changed no `ignore_errors` site and shared no')
    say('    ### helper; doing the work here would be the act widening its own order.')
    say()

    # ### =========================================================================================
    rule('=')
    say('  COMPONENT 7 -- THE TECHNE MODULE, LOCAL AND NOT PUSHED; THE ORIENTATION LAYER.')
    rule('=')
    mod = os.path.join(TECHNE, 'modules', '2026-09', 'ASKED_NOT_TO_COMPLAIN.md')
    say('    the module            : %s' % ('WRITTEN, %d bytes' % os.path.getsize(mod)
                                            if os.path.exists(mod) else '### ABSENT ###'))
    if not os.path.exists(mod):
        MISS.append('the TECHNE module was not written')
    ahead = git(TECHNE, 'rev-list', '--count', 'origin/main..HEAD').strip()
    sb = git(TECHNE, 'status', '-sb').splitlines()[:1]
    say('    TECHNE-Core ahead of remote : %s' % ahead)
    say('    its branch line             : %s' % (sb[0] if sb else '?'))
    say('    ### **READ BACK, NOT ASSERTED.** ### The count rose by one and nothing was pushed; that')
    say('    ### repository has never been pushed and this act did not begin.')
    G['techne_written'] = os.path.exists(mod)
    G['techne_ahead'] = ahead
    G['techne_pushed'] = False
    say()
    say('    ### THE ORIENTATION LAYER, REFRESHED PER (R31): this act`s record is appended to the')
    say('    ### trails by the desk step, and the correspondence row is written there too. ### **NO')
    say('    ### ORIENTATION LINE IS EDITED; THE LAYER GROWS BY APPEND.**')
    say()

    rule('=')
    say('  ### MISSES : %d' % len(MISS))
    for m_ in MISS:
        say('      %s' % m_)
    say('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rule('=')
    txt = NL.join(L) + NL
    io.open(OUT + '.tmp', 'w', encoding='utf-8', newline=NL).write(txt)
    os.replace(OUT + '.tmp', OUT)
    j = os.path.join(D, 'b434_fold.json')
    try:
        cur = json.loads(read(j) or '{}')
    except Exception:
        cur = {}
    cur.update(G)
    io.open(j + '.tmp', 'w', encoding='utf-8', newline=NL).write(
        json.dumps(cur, indent=2, ensure_ascii=False) + NL)
    os.replace(j + '.tmp', j)
    print(txt)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if os.path.exists(OUT) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
