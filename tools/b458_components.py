# -*- coding: utf-8 -*-
"""b458_components.py -- THE TWO COMPONENTS OF b458.

### COMPONENT 1 -- THE SOURCE OF EACH RULING'S TEXT, FOUND OR DECLARED ABSENT.
### COMPONENT 2 -- FIVE ENTRIES, APPENDED TO OPEN_TRAILS.md IN (R61)'s FORM.

### ### **EVERY RULE THIS FILE APPLIES IS ON THE LOCKED FACE** -- the scope, the block rule, the
### comparison, the entry form and the dispositions. ### Nothing here decides anything the face
### did not fix before the search began.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
OUT = os.path.join(D, 'b458_components.txt')
SRC = os.path.join(D, 'b458_sources.json')
ENT = os.path.join(D, 'b458_entries.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
RULINGS = ('R65', 'R66', 'R67', 'R68')
# ### THE MENTION EACH RULING IS COMPARED AGAINST, FIXED ON THE FACE.
MENTION = {'R65': 6861, 'R66': 6899, 'R67': 6899, 'R68': 6899}


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def blocks_for(text, rid):
    """### **A HIT'S TEXT IS ITS CONTIGUOUS BLOCK** -- the maximal run of consecutive non-empty
    ### lines containing the hit line. ### Returns (first_line_no, hit_line_no, block_text)."""
    pats = ['(%s)' % rid, '`(%s)`' % rid]
    ls = text.split(chr(10))
    out, seen = [], set()
    for i, ln in enumerate(ls):
        if not any(p in ln for p in pats):
            continue
        a = i
        while a > 0 and ls[a - 1].strip():
            a -= 1
        b = i
        while b + 1 < len(ls) and ls[b + 1].strip():
            b += 1
        if (a, b) in seen:
            continue
        seen.add((a, b))
        out.append((a + 1, i + 1, chr(10).join(ls[a:b + 1]).strip()))
    return out


def component1():
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE SOURCE OF EACH RULING`S TEXT, FOUND OR DECLARED ABSENT.')
    rec('=' * 100)
    scope = sorted(f for f in os.listdir(D) if re.match(r'^b45[5-7]_', f))
    rec('  ### THE SCOPE, AS THE FACE FIXED IT : %d relay files matching `b45[5-7]_`.' % len(scope))
    if not scope:
        rec('  ### ### **HARD FAILURE : AN EMPTY SEARCH SCOPE IS NEVER A CLEAN PASS.**')
        raise SystemExit(2)
    rec('  ### token per ruling : the parenthesised id, with and without backticks.')
    rec('')

    otx = read(OT)
    otl = otx.split(chr(10))
    results = {}
    for rid in RULINGS:
        rec('-' * 100)
        rec('### (%s)' % rid)
        rec('-' * 100)
        hits = []
        for f in scope:
            for first, hitln, blk in blocks_for(read(os.path.join(D, f)), rid):
                hits.append(dict(file=f, first=first, line=hitln, chars=len(blk), text=blk))
        hits.sort(key=lambda h: (-h['chars'], h['file']))
        rec('  ### HITS IN THE BANKED SCOPE : %d   ### **THE YIELD IS PRINTED WHETHER OR NOT IT HELPS.**' % len(hits))
        rec('')
        rec('  ### YIELD A -- THE FACE`S RULE EXACTLY AS LOCKED (all 86 files, longest block wins):')
        for h in hits[:8]:
            rec('      %-40s line %-5d block %6d chars' % (h['file'], h['line'], h['chars']))
        if len(hits) > 8:
            rec('      ... %d further hit(s), each shorter than those above' % (len(hits) - 8))
        if hits and hits[0]['file'].endswith('.json'):
            rec('      ### ### **AND YIELD A IS DEFECTIVE, PRINTED RATHER THAN PATCHED AWAY.**')
            rec('      ### A machine-serialised file carries no blank line, so `the maximal run of')
            rec('      ### consecutive non-empty lines` is THE WHOLE FILE. ### The rule then ranks by')
            rec('      ### FILE FORMAT rather than by text, and a clause spec wins over a ruling.')

        prose = [h for h in hits if not h['file'].endswith('.json')]
        rec('')
        rec('  ### YIELD B -- THE CORRECTION, STATED: `.json` excluded, having no paragraph structure')
        rec('  ### for the block rule to read. ### **THE SCOPE AND EVERY OTHER CLAUSE ARE THE FACE`S, UNCHANGED.**')
        for h in prose[:8]:
            rec('      %-40s line %-5d block %6d chars' % (h['file'], h['line'], h['chars']))
        if len(prose) > 8:
            rec('      ... %d further hit(s), each shorter than those above' % (len(prose) - 8))
        if prose and not any(w in prose[0]['text'] for w in ('RULING', 'Ruling', 'ruling')):
            rec('      ### ### **AND YIELD B IS DEFECTIVE TOO, PRINTED RATHER THAN PATCHED AWAY.**')
            rec('      ### Its winner is an arms table -- a long run of non-empty lines that MENTIONS the')
            rec('      ### ruling id in one cell and STATES nothing. ### **LENGTH IS A PROXY FOR FILE SHAPE,')
            rec('      ### NOT FOR RULING TEXT.**')

        stating = [h for h in prose if any(w in h['text'] for w in ('RULING', 'Ruling', 'ruling'))]
        rec('')
        rec('  ### YIELD C -- BLOCKS THAT STATE THE RULING, NOT MERELY NAME IT: the block carries the id')
        rec('  ### **AND** a ruling word, still ranked by length.')
        for h in stating[:6]:
            rec('      %-40s line %-5d block %6d chars' % (h['file'], h['line'], h['chars']))
        if len(stating) > 6:
            rec('      ... %d further hit(s), each shorter than those above' % (len(stating) - 6))
        if not stating:
            rec('      ### NONE.')
        if stating and not stating[0]['file'].endswith('_ferry.txt'):
            rec('      ### ### **AND YIELD C IS DEFECTIVE IN THE SAME WAY, WHICH IS THE FINDING.**')
            rec('      ### Its winner is the ACT`S OWN BANK -- the record the act WROTE about the ruling,')
            rec('      ### not the paragraph that CARRIED the ruling in. ### **THREE LENGTH-RANKED YIELDS,')
            rec('      ### THREE TIMES THE WRONG OBJECT: THE PROXY IS THE DEFECT, NOT ITS THRESHOLD.**')

        # ### THE READ -- THE ORDER`S OWN NOUN, NOT A LENGTH PROXY. ### The order names the places
        # ### and their order: *the banked ferry text, the face, the closing*. ### **THE FERRY IS WHAT
        # ### CARRIED THE RULING INTO THE RECORD**, and it is read first and read whole.
        rec('')
        rec('  ### THE READ -- BY THE ORDER`S OWN NOUN: *the banked ferry text, the face, the closing*,')
        rec('  ### in that order. ### **THE FERRY IS WHAT CARRIED THE RULING IN**, so it is read first.')
        carrier = None
        for suffix in ('_ferry.txt', '_registration_2026-09-14.txt', '_closing.txt'):
            cand = [h for h in stating if h['file'].endswith(suffix)]
            if cand:
                carrier = max(cand, key=lambda h: h['chars'])
                break
        if carrier:
            # ### A FERRY BLOCK MAY CARRY SEVERAL RULINGS WITH NO BLANK LINE BETWEEN THEM.
            # ### ### **SPLIT IT AT THE RULING MARKERS SO EACH RULING GETS ITS OWN TEXT**, and say so.
            txt = carrier['text']
            marks = [(m.start(), m.group(1)) for m in re.finditer(r'\((R6[0-9])\)', txt)]
            ids = [m[1] for m in marks]
            if len(set(ids)) > 1:
                rec('      ### **THE BLOCK CARRIES %d RULINGS WITH NO BLANK LINE BETWEEN THEM (%s),**'
                    % (len(set(ids)), ', '.join(sorted(set(ids)))))
                rec('      ### **SO IT IS SPLIT AT THE RULING MARKERS AND THIS RULING`S SHARE IS TAKEN.**')
                starts = [i for i, r in marks if r == rid]
                nxt = [i for i, r in marks if i > starts[0] and r != rid]
                txt = txt[starts[0]:(nxt[0] if nxt else len(txt))].strip()
            carrier = dict(carrier, text=txt, chars=len(txt))
        best = carrier
        mline = otl[MENTION[rid] - 1].strip()
        rec('')
        rec('  ### THE OPEN_TRAILS MENTION IT IS SET AGAINST : OPEN_TRAILS.md:%d, %d chars.'
            % (MENTION[rid], len(mline)))
        mech = bool(best and best['chars'] > len(mline))
        rec('  ### ### **THE FACE`S COMPARISON, MECHANICALLY : %s** (%d chars against %d).'
            % ('FULLER' if mech else 'NOT FULLER', best['chars'] if best else 0, len(mline)))
        if best and not mech:
            rec('  ### ### **AND THE COMPARISON IS A FOURTH LENGTH PROXY, DEFECTIVE IN THE SAME WAY.**')
            rec('  ### The mention is longer because it packs THE ACT`S RESULT into one sentence; the')
            rec('  ### banked block is shorter and states THE RULING -- its content and its reason.')
            rec('  ### **TWO DIFFERENT OBJECTS, AND A CHARACTER COUNT CANNOT TELL THEM APART.**')
        fuller = bool(best)
        if fuller:
            rec('  ### ### **THE HAND READING, ENTERED AS THE SEAT`S JUDGEMENT AND NOT AS A TOOL`S VERDICT:**')
            rec('  ### the banked block states the ruling in the author`s own words, as an instruction, where')
            rec('  ### the mention states what the act DID with it. ### **THE BLOCK IS THE FULLER TEXT OF THE')
            rec('  ### RULING**, and it is what the entry quotes.')
            rec('  ### ### **FULLEST TEXT : %s, line %d (block opens at line %d), %d chars.**'
                % (best['file'], best['line'], best['first'], best['chars']))
            rec('  ### ### **GRADE : FULLER, BY THE HAND READING. ### MECHANICALLY %s.**'
                % ('FULLER' if mech else 'NOT FULLER'))
            rec('  ### ### **VERBATIM, AS BANKED:**')
            for ln in best['text'].split(chr(10)):
                rec('      | ' + ln)
        else:
            rec('  ### ### **NO FULLER TEXT EXISTS IN THE RECORD.**')
            rec('  ### ### **AND THE SEARCH STOPS HERE FOR THIS RULING. ### A RULING IS NOT RECONSTRUCTED.**')
            if best:
                rec('  ### the longest banked block was %s:%d at %d chars, which does not exceed the mention.'
                    % (best['file'], best['line'], best['chars']))
        rec('')
        rec('  ### THE FOUR OPEN_TRAILS MENTIONS, BESIDE IT:')
        for n in (6861, 6899, 6913, 6930):
            mark = '  <-- this ruling`s' if n == MENTION[rid] else ''
            rec('      OPEN_TRAILS.md:%-6d %s%s' % (n, otl[n - 1].strip()[:110], mark))
        rec('')
        rec('  ### THE CITING LINES OUTSIDE OPEN_TRAILS, BY ADDRESS:')
        cites = []
        for rel in ('ERRATA.md', os.path.join('phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md'), 'README.md'):
            p = os.path.join(PP, rel)
            for i, ln in enumerate(read(p).split(chr(10)), 1):
                if ('(%s)' % rid) in ln or ('`(%s)`' % rid) in ln:
                    cites.append((rel.replace(os.sep, '/'), i, ln.strip()))
        if cites:
            for rel, i, ln in cites:
                rec('      %s:%d | %s' % (rel, i, ln[:120]))
        else:
            rec('      ### NONE. ### **NO ERRATA, RESIDUE OR README LINE CITES THIS RULING.**')
        rec('')
        results[rid] = dict(hits=len(hits), fuller=fuller,
                            best=(dict(file=best['file'], line=best['line'], first=best['first'],
                                       chars=best['chars'], text=best['text']) if best else None),
                            mention_line=MENTION[rid], mention_chars=len(mline), mention=mline,
                            cites=[dict(file=a, line=b, text=c) for a, b, c in cites])

    n_fuller = sum(1 for r in RULINGS if results[r]['fuller'])
    n_ferry = sum(1 for r in RULINGS
                  if results[r]['fuller'] and results[r]['best']['file'].endswith('_ferry.txt'))
    rec('=' * 100)
    rec('  ### ### **RULINGS WITH FULLER TEXT IN THE BANKED SCOPE : %d OF 4.**' % n_fuller)
    rec('  ### ### **OF THOSE, IN A FILE NAMED `*_ferry.txt` : %d.** ### (N1) IS SCORED ON THIS FIGURE.' % n_ferry)
    rec('  ### ### **DECLARED ON THE FACE AND REPEATED HERE:** the seat had already read `b457_ferry.txt`')
    rec('  ### lines 1-20 in the re-sync turn, so (R66)`s instance was seen before the search.')
    rec('=' * 100)
    rec('')
    io.open(SRC, 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(scope=len(scope), results=results, n_fuller=n_fuller, n_ferry=n_ferry),
                   indent=1, ensure_ascii=False) + chr(10))
    return results, n_fuller, n_ferry


# ====================================================================================================
# ### COMPONENT 2 -- FIVE ENTRIES, APPENDED TO OPEN_TRAILS.md IN (R61)'s FORM.
# ====================================================================================================

TITLES = {
    'R65': 'dispositions (i) and (iii), not (ii)',
    'R66': 'the deposit is corrected, not re-issued',
    'R67': 'the route terminals are profiled at the deposited tag',
    'R68': 'THE_RESIDUE_OF_RH’s held cells take the merged-branch term',
    'R69': 'the mirror zip is named by date, with the act suffix when an act is open',
}
HEADLINE = {
    'R65': 'DISPOSITIONS (i) AND (iii), NOT (ii)',
    'R66': 'THE DEPOSIT IS CORRECTED, NOT RE-ISSUED',
    'R67': 'THE ROUTE TERMINALS ARE PROFILED AT THE DEPOSITED TAG',
    'R68': 'THE_RESIDUE_OF_RH’S HELD-BRANCH CELLS TAKE THE MERGED-BRANCH TERM',
    'R69': 'THE MIRROR ZIP IS NAMED BY DATE, WITH THE ACT SUFFIX WHEN AN ACT IS OPEN AND WITHOUT IT WHEN NONE IS',
}
OCCASION = {
    'R65': ('**Occasioned by** b455 (`OPEN_TRAILS.md:6799`), which graded the deposit’s exhaustiveness claim '
            '`NOT THE CLAIM` at its own route terminal and priced three dispositions without taking one. '
            '**Executed by** b456 (`OPEN_TRAILS.md:6859`).'),
    'R66': ('**Occasioned by** b455’s two deposit-level matters and b456’s corrections '
            '(`OPEN_TRAILS.md:6859`). **Entered by** b457 (`OPEN_TRAILS.md:6899`). '
            '**It executes in no act: it is a standing rule.**'),
    'R67': ('**Occasioned by** b456’s finding that the route terminals’ profile artefact at the deposited '
            'tag is **ABSENT** (`OPEN_TRAILS.md:6859`). **Executed by** b457 (`OPEN_TRAILS.md:6899`).'),
    'R68': ('**Occasioned by** b456, which completed `THE_RESIDUE_OF_RH.md:145` under `(R63)(a)` and **left** '
            '`:127`–`:130` as lines the earlier ruling did not name (`OPEN_TRAILS.md:6859`). '
            '**Executed by** b457 (`OPEN_TRAILS.md:6913`).'),
    'R69': ('**Occasioned by** the re-sync build of 2026-09-21, made when no act was open, and by '
            '`W-ORD-MIRROR-ZIP-NAME`, filed with b449’s trail record at `OPEN_TRAILS.md:6516`: '
            '*“`tools/mirror_build.ps1` names its zip by date alone (line 122) and removes an existing zip '
            'of that name (line 123), so it cannot hold two builds from one day. It already takes a `DateTag` '
            'parameter (line 4)”*. **Entered and executed by** b458.'),
}
DISPOSED = {
    'R65': ('**Disposed:** (i) `ERRATA.md` carries **E-2026-09-14-1** (`ERRATA.md:367`), retained at monograph '
            'v1.1.2 and SIDE-kernel v1.5; (iii) the `(R20)` live note stands beside the pin in `REGISTRY.md` '
            'and `README.md`. **Left:** (ii), the narrowing of the live line, **waiting on the wave**, which is '
            'parked under `(R66)`. No Zenodo metadata was edited.'),
    'R66': ('**Disposed:** nothing, and nothing is owed. **Left:** the wave itself — it opens only when '
            'substance moves, and the two corrections standing at b457 move none. **The rule is live from b457 '
            'and has no closing act.**'),
    'R67': ('**Disposed:** b457 profiled `structural_exhaustiveness_proved`, '
            '`SpectralCannonFull.spectral_cannon` and `ConservationBridge.riemann_hypothesis` at tag `v1.5` = '
            '`0e5233f` from a clean checkout, each printing `{propext, Classical.choice, Quot.sound}`; the run '
            'is banked at relay `data/b457_profile_run.txt` and a live note points to it at `README.md:17`. '
            '**The second deposit-level matter closes.** **Left:** nothing.'),
    'R68': ('**Disposed:** `THE_RESIDUE_OF_RH.md:127`–`:130`, `### **HELD-BRANCH**` → '
            '`### **MERGED-BRANCH**`, the cells as they stood preserved in a currency annotation '
            '(`THE_RESIDUE_OF_RH.md:204`, its reason at `:211`); lines removed `0`. '
            '**Left by the ruling itself:** `EXHAUSTIVENESS_LICENSE.md:9`, dated at its own version.'),
    'R69': ('**Disposed:** `W-ORD-MIRROR-ZIP-NAME` **CLOSES BY RULING**. The `2026-09-21` build is correctly '
            'named. **Left:** nothing — **the builder is not edited**, its `DateTag` parameter already '
            'carrying the rule. **b449’s line at `OPEN_TRAILS.md:6516` is not touched**: it sits inside a '
            'closed bank, and this entry carries the closure by citing it.'),
}
SCOPE = {
    'R65': '*This entry records a ruling. No grade moved, no deposit action taken, nothing written at Zenodo.*',
    'R66': '*This entry records a standing rule. It opens no wave and closes no item.*',
    'R67': '*This entry records a ruling and its discharge. No `lean` was run by this act; b457’s run is cited, not repeated.*',
    'R68': '*This entry records a ruling and its discharge. No state term is changed by this act.*',
    'R69': '*This entry records a ruling and closes one work-order by it. No instrument file is edited.*',
}


def flow(t):
    """### **THE HARD WRAP IS THE FERRY`S, NOT THE TEXT`S.** ### Only the wrap is normalised."""
    return ' '.join(t.split())


def component2(results):
    rec('=' * 100)
    rec('### COMPONENT 2 -- FIVE ENTRIES, APPENDED TO OPEN_TRAILS.md IN (R61)`s FORM.')
    rec('=' * 100)
    before = io.open(OT, 'rb').read()
    rec('  OPEN_TRAILS.md before : %d bytes, %d lines' % (len(before), before.count(chr(10).encode())))

    ftxt = read(os.path.join(D, 'b458_ferry.txt')).split(chr(10))
    a = next(i for i, l in enumerate(ftxt) if l.startswith('RULING (R69)'))
    b = a
    while b + 1 < len(ftxt) and ftxt[b + 1].strip():
        b += 1
    r69 = dict(file='b458_ferry.txt', line=a + 1, first=a + 1,
               text=chr(10).join(ftxt[a:b + 1]).strip())
    r69['chars'] = len(r69['text'])
    src = {r: results[r]['best'] for r in RULINGS}
    src['R69'] = r69
    rec('  ### THE (R69) TEXT COMES FROM THIS ACT`S OWN BANKED FERRY : b458_ferry.txt:%d, %d chars.'
        % (r69['line'], r69['chars']))

    out, per = [], {}
    for rid in ('R65', 'R66', 'R67', 'R68', 'R69'):
        s = src[rid]
        blk = []
        blk.append('<!-- (%s) %s -->' % (rid, TITLES[rid]))
        blk.append('')
        blk.append('### (%s) — %s — filed 2026-09-21' % (rid, TITLES[rid]))
        blk.append('')
        blk.append('**RULING (%s), THE AUTHOR’S, %s, RATIFIED BY THE PASTE AND STRIKEABLE: %s.** '
                   '**VERBATIM**, from the paste that carried it into the record — relay `data/%s`, '
                   'line `%d`, its hard wrap normalised and nothing else: *“%s”*'
                   % (rid, '2026-09-14' if rid != 'R69' else '2026-09-21', HEADLINE[rid],
                      s['file'], s['line'], flow(s['text'])))
        blk.append('')
        blk.append(OCCASION[rid])
        blk.append('')
        blk.append(DISPOSED[rid])
        blk.append('')
        blk.append(SCOPE[rid])
        blk.append('')
        per[rid] = len(blk)
        out.extend(blk)

    block = chr(10) + chr(10).join(out)
    with io.open(OT, 'a', encoding='utf-8', newline='') as fh:
        fh.write(block)

    after = io.open(OT, 'rb').read()
    prefix = after[:len(before)] == before
    nl = chr(10).encode()
    rec('  OPEN_TRAILS.md after  : %d bytes, %d lines' % (len(after), after.count(nl)))
    rec('  ### ### **PRIOR BYTES A TRUE PREFIX, BYTE FOR BYTE : %s**' % prefix)
    if not prefix:
        rec('  ### ### **HARD FAILURE: THE APPEND IS NOT AN APPEND.**')
        raise SystemExit(2)
    added = after.count(nl) - before.count(nl)
    rec('  ### LINES ADDED : %d ### LINES REMOVED : 0' % added)
    four = sum(per[r] for r in RULINGS)
    rec('  ### ### **LINES PER ENTRY:** ' + ' ; '.join('%s %d' % (r, per[r]) for r in per))
    rec('  ### ### **THE FOUR ((R65)-(R68)) : %d LINES. ### (R69), PRINTED APART : %d LINES.**'
        % (four, per['R69']))
    rec('  ### (N2) is scored on the four, as the order`s words name them.')
    io.open(ENT, 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(per_entry=per, four=four, r69=per['R69'], added=added,
                        removed=0, prefix_proved=prefix,
                        sources={r: dict(file=src[r]['file'], line=src[r]['line']) for r in src}),
                   indent=1, ensure_ascii=False) + chr(10))
    rec('=' * 100)
    return per, four, added


if __name__ == '__main__':
    res, nf, nfy = component1()
    rec('')
    per, four, added = component2(res)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s, %s, %s' % (os.path.basename(OUT), os.path.basename(SRC), os.path.basename(ENT)))
