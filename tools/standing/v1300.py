# -*- coding: utf-8 -*-
"""standing/v1300.py -- THE CONTROLS OF v1.30.0 ((R360)(3)(i)-(xiii); b749 events (1)-(12), defects (a)-(v)), in v1290.py's form: each instance
read through the route as it stood before the repair (tools/standing/ and the act module at BASE, b749's closing relay head, read from their
blobs) and through the repaired route on disk; AS WANTED where the old route fails the instance and the new passes it. A guard is a case with
no failing side. THE COMPILE CONTROL RUNS FIRST. The free memory is read and printed before each control. Written at b750 by the Write tool;
no identifier of the author is read into any string here.

  python -X utf8 -u tools/standing/v1300.py control [answers|hook|halt|words|closingdry|n5|count|lock|permit|carry|retries|instances|version ...] [--bank]
"""
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
PP = 'D:/MY-DOwnloads/PLACE-papers'
NL = '\n'
BASE = '8ce7e3ab'   # ### b749's closing relay head (PRE_RELAY of b750): the routes before this repair
B749_SITTING = '1858213d'   # ### the [Z1] sitting block's commit (b749 component 2)
B749_PP = '91929f75'   # ### PLACE-papers at b749's close
B748_HEAD = '71bc497a'   # ### b748's closing relay head (b749's PRE_RELAY)
B749_SESSION = 'C:/Users/echo chamber/.claude/projects/D--/6151c0de-d2ec-42cf-a477-c48b99346e01.jsonl'
HOLD = 2560
SCRATCH = os.environ.get('TEMP') or tempfile.gettempdir()
for p_ in (T, S):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import carry as CA              # noqa: E402
import compilecontrol as CC     # noqa: E402
import delread as DR            # noqa: E402
import figbank as FB            # noqa: E402
import rootprompt as RPM        # noqa: E402


def _git(*a, repo=RELAY):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(ref, rel, repo=RELAY):
    return _git('show', '%s:%s' % (ref, rel), repo=repo).replace('\r', '')


def rdf(rel):
    p = os.path.join(RELAY, rel)
    return io.open(p, encoding='utf-8').read().replace('\r', '') if os.path.isfile(p) else ''


def old(rel, name):
    """tools/standing/<rel> as BASE left it, loaded from its blob under another name."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, name + '.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(show(BASE, 'tools/standing/' + rel))
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    shutil.rmtree(d, ignore_errors=True)
    return m


def iso_run(code):
    """a program run as the hook runs, `python -I`, its stdout's last line read as JSON."""
    d = tempfile.mkdtemp(dir=SCRATCH)
    p = os.path.join(d, 'iso.py')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(code)
    r = subprocess.run([sys.executable, '-I', '-X', 'utf8', p], capture_output=True, text=True, encoding='utf-8', errors='replace')
    shutil.rmtree(d, ignore_errors=True)
    try:
        return json.loads(r.stdout.strip().split(NL)[-1])
    except (ValueError, IndexError):
        return dict(error=(r.stdout + r.stderr)[-300:])


def free_line():
    import b703_checks as C3
    mb = C3.free_mb()
    return '  free %s MB at %s, the hold %d %s' % (mb, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), HOLD, 'MET' if isinstance(mb, int) and mb >= HOLD else '### NOT MET')


def case(L, cls, what, old_, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.29.0): %s -> %s' % (old_, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.30.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def guard(L, cls, what, new, holds):
    L += ['  (%s) GUARD, NO FAILING SIDE: %s' % (cls, what), '      AFTER  (v1.30.0): %s -> %s' % (new, 'HOLDS' if holds else 'DOES NOT HOLD'), '      %s' % ('AS WANTED' if holds else 'NOT AS WANTED')]
    return bool(holds)


# ================================================================================ (answers) (3)(i): THE ANSWERS ROUTE APPENDS
def control_answers():
    L, g, n = ['### (answers) (R360)(3)(i), b749 events (4): `record answers` APPENDS TO data/<act>_author_answers.txt AND REWRITES NO LINE ALREADY IN IT; THE SITTING BLOCK STAYS WHERE IT WAS COMMITTED'], 0, 0
    prior = show(B749_SITTING, 'data/b749_author_answers.txt')
    final = rdf('data/b749_author_answers.txt').split(NL)
    composed = final[:20]   # ### the route's rewrite at 20:08Z: the file's rows :1-:20, before the lifted Edit appended the block at :21-:28
    blk = [l for l in prior.split(NL) if l.startswith('[Z1] PASS')]
    n += 1
    g += guard(L, 'answers', 'the instance found: b749`s bank at %s carries the sitting row; the route`s rewrite (rows :1-:20 of the bank as it stands) does not' % B749_SITTING,
               'sitting row at %s :%s ; in the rewrite %s' % (B749_SITTING, prior.split(NL).index(blk[0]) + 1 if blk else '?', any(l.startswith('[Z1] PASS') for l in composed)),
               bool(blk) and not any(l.startswith('[Z1] PASS') for l in composed))
    text, k = A.answers_append(prior, composed, '2026-11-09T20:08:14Z')
    tl = text.split(NL)
    kept = tl[:len(prior.rstrip(NL).split(NL))] == prior.rstrip(NL).split(NL)
    n += 1
    g += case(L, 'answers', 'b749`s route replayed over the bank committed at %s (the root`s prompt and answer composed beside the [Z1] block)' % B749_SITTING,
              'b698`s route writes the composed lines whole: [Z1] PASS row %s, PROMPT rows %d' % ('PRESENT' if any(l.startswith('[Z1] PASS') for l in composed) else 'DROPPED', sum(1 for l in composed if l.startswith('### PROMPT '))),
              'answers_append: the bank`s %d lines kept in place %s, [Z1] PASS at :%d, appended %d, PROMPT rows %d' % (
                  len(prior.rstrip(NL).split(NL)), kept, next((i for i, l in enumerate(tl, 1) if l.startswith('[Z1] PASS')), 0), k, sum(1 for l in tl if l.startswith('### PROMPT '))),
              not any(l.startswith('[Z1] PASS') for l in composed), kept and any(l.startswith('[Z1] PASS') for l in tl) and sum(1 for l in tl if l.startswith('### PROMPT ')) == 2)
    t2, k2 = A.answers_append(text, composed, '2026-11-09T20:09:00Z')
    n += 1
    g += guard(L, 'answers', 'the route run again over its own output appends nothing and leaves the bank`s bytes as they stand', 'appended %d, bytes equal %s' % (k2, t2 == text), k2 == 0 and t2 == text)
    tpl = rdf('tools/standing/fold/record.tpl')
    n += 1
    w, b, rt = tpl.rfind('\ndef answers(*a):'), tpl.rfind('\nanswers = R.answers\n'), tpl.find('\nROUTES = dict(')
    g += guard(L, 'answers', 'the record template`s `answers` route, as ROUTES takes it, is the appending wrapper over b698`s composer (`answers = R.answers` kept at :214 for the line-keyed overrides, rebound below)',
               'the wrapper at offset %d, b698`s binding at %d, ROUTES at %d ; answers_append called %s' % (w, b, rt, 'SA.answers_append(' in tpl),
               b < w < rt and 'SA.answers_append(' in tpl)
    return L, g, n


# ================================================================================ (hook) (3)(ii): THE HOOK'S ROW (65) AND THE DESIGN'S EXCEPTIONS
HOOK_ISO = r'''
import importlib.util, json, sys
spec = importlib.util.spec_from_file_location('hook_x', %r)
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H)
p = r'D:\relay\data\b749_author_answers.txt'
R = 'D:/relay'
out = dict(locked=H.locked_bank(p, relay=R, act='b749'), exempt='data/b749_author_answers.txt' in H.lock_exempt('b749'))
out['by_design'] = H.by_design_bank(p, relay=R, act='b749') if hasattr(H, 'by_design_bank') else None
out['scan'] = H.by_design_bank(r'D:\relay\data\b749_address_scan_postlock.txt', relay=R, act='b749') if hasattr(H, 'by_design_bank') else None
out['words'] = H.by_design_bank(r'D:\relay\data\b749_author_words.txt', relay=R, act='b749') if hasattr(H, 'by_design_bank') else None
out['events'] = H.by_design_bank(r'D:\relay\data\b749_events.txt', relay=R, act='b749') if hasattr(H, 'by_design_bank') else None
print(json.dumps(out))
'''


def control_hook():
    L, g, n = ['### (hook) (R360)(3)(ii), b749 events (4)-(6): THE HOOK`S ROW (65) NAMES THE ANSWERS PAIR, THE AUTHOR-WORDS BANKS AND THE POST-LOCK SCAN BANKS AS WRITTEN AFTER THE LOCK BY DESIGN, '
               'REFUSES A HAND EDIT OF THEM AND LEAVES THE TOOL`S APPEND; N4 READS THE SAME LIST'], 0, 0
    d = tempfile.mkdtemp(dir=SCRATCH)
    op = os.path.join(d, 'hook_v1290.py')
    io.open(op, 'w', encoding='utf-8', newline='\n').write(show(BASE, 'tools/standing/hook.py'))
    o = iso_run(HOOK_ISO % op)
    nw = iso_run(HOOK_ISO % os.path.join(S, 'hook.py'))
    shutil.rmtree(d, ignore_errors=True)
    rf = rdf('data/b749_hook_refusals.txt').split(NL)
    n += 1
    g += guard(L, 'hook', 'the instance: b749`s restoring Edit of its answers bank refused LOCKED at 20:09:26Z (data/b749_hook_refusals.txt :17)', rf[16][:90] if len(rf) > 16 else 'ABSENT',
               len(rf) > 16 and '| LOCKED | Edit |' in rf[16])
    n += 1
    g += case(L, 'hook', 'b749`s hand Edit of data/b749_author_answers.txt replayed as the hook runs it (`python -I`): the design list read, the refusal its own',
              'v1.29.0 under -I: lock_exempt names the answers bank %s ; locked_bank %s (refused LOCKED, the design`s exception unread: `import act` failing under -I)' % (o.get('exempt'), o.get('locked')),
              'v1.30.0 under -I: lock_exempt names it %s ; by_design_bank %s (refused BYDESIGN, row (65) naming the design list)' % (nw.get('exempt'), nw.get('by_design')),
              o.get('locked') is True and o.get('exempt') is False, nw.get('exempt') is True and nw.get('by_design') == 'data/b749_author_answers.txt')
    n += 1
    g += guard(L, 'hook', 'the author-words bank and the post-lock scan bank refused by hand the same way; the events bank, appended by the Edit tool by design, not in the list',
               'words %s ; scan %s ; events %s' % (nw.get('words'), nw.get('scan'), nw.get('events')),
               nw.get('words') == 'data/b749_author_words.txt' and nw.get('scan') == 'data/b749_address_scan_postlock.txt' and nw.get('events') is None)
    import act_close as AC
    pla = A.post_lock_appended('b749')
    n += 1
    g += guard(L, 'hook', 'the tool`s append accepted: the record`s writer refuses no bank of the design list after the lock (act_close.lock_refuses), and N4`s list (post_lock_appended) carries the whole design list',
               'lock_refuses(answers) %r ; design list in N4`s list %s' % (AC.lock_refuses('b749', 'b749_author_answers.txt')[:40], all(p in pla for p in A.by_design('b749'))),
               AC.lock_refuses('b749', 'b749_author_answers.txt') == '' and all(p in pla for p in A.by_design('b749')))
    return L, g, n


# ================================================================================ (halt) (3)(iii): A HALT QUESTION NAMES EVERY SCORE ITS ROUTES WOULD COST
def b749_halt():
    """the second halt of b749 (transcript line 5873, 20:14:55Z): the quoted question and its three ways forward, read from the transcript."""
    for i, raw in enumerate(io.open(B749_SESSION, encoding='utf-8'), 1):
        if i != 5873:
            continue
        o = json.loads(raw)
        t = ''.join(c.get('text', '') for c in (o.get('message') or {}).get('content') or [] if isinstance(c, dict) and c.get('type') == 'text')
        q = re.search(r'\n> (.*?)\n\n\*\*Ways forward', t, re.S)
        opts = re.findall(r'(?m)^\d\. \*\*(.+?)\*\* (.*)$', t)
        return (q.group(1).strip() if q else ''), [(a.rstrip('.'), b) for a, b in opts]
    return '', []


def control_halt():
    L, g, n = ['### (halt) (R360)(3)(iii), b749 events (5), (6), (12): A HALT QUESTION NAMES EVERY SCORE ITS ROUTES WOULD COST, READ FROM THE RULING`S CLAUSES BY THE COMPOSER (rootprompt.costs_unnamed, check_hand)'], 0, 0
    q, opts = b749_halt()
    cl = RPM.score_clauses(rdf('data/b749_ferry.txt'))
    n += 1
    g += guard(L, 'halt', 'the instance read from b749`s transcript line 5873 and b749`s clauses from data/b749_ferry.txt', 'question %d chars ; options %s ; clauses %s' % (
        len(q), [o[0][:30] for o in opts], sorted(cl)), len(q) > 200 and len(opts) == 3 and 'N4' in cl)
    ORP = old('rootprompt.py', 'rootprompt_v1290')
    o_has = hasattr(ORP, 'costs_unnamed')
    bad = RPM.costs_unnamed(q, opts, cl)
    n += 1
    g += case(L, 'halt', 'b749`s second halt replayed: option 1 "%s", its cost named by the seat the overcount alone' % (opts[0][0] if opts else '?'),
              'check_hand reads no option and no clause (costs_unnamed %s): the question passes with N4 unnamed' % ('DEFINED' if o_has else 'UNDEFINED'),
              'costs_unnamed: %s' % ('; '.join('option %d %s on "%s"' % (k, s, w) for k, _l, s, w in bad) or 'NONE'),
              not o_has, any(k == 1 and s == 'N4' for k, _l, s, _w in bad))
    named = [(a, b + ' N4 would read REFUTED on its clause.') if k == 0 else (a, b) for k, (a, b) in enumerate(opts)]
    bad2 = RPM.costs_unnamed(q, named, cl)
    n += 1
    g += guard(L, 'halt', 'the same option with N4 named in it carries no unnamed cost', '; '.join('option %d %s' % (k, s) for k, _l, s, _w in bad2) or 'NONE',
               not any(k == 1 for k, _l, _s, _w in bad2))
    return L, g, n


# ================================================================================ (words) (3)(iv): "NONE RECEIVED"
B749_WORDS = ('Repair-phase edit of the act module: one repair commit after the seal, under the repair phase with its lift banked, so tools/acts/b749.py’s reader of [Z1] accepts the row as it now stands in data/b749_author_answers.txt (the PROMPT row carrying “[Z1] PASS” and the time 14:35:05Z); no bank edited; the answers route’s whole-file rewrite entered as the act’s defect, the rule for b750: the answers route appends and refuses to rewrite a bank written before the lock.')


def control_words():
    L, g, n = ['### (words) (R360)(3)(iv), b749 events (9): THE AUTHOR-WORDS BANK IS APPENDED AFTER THE ROOT BY DESIGN AND READ APART; THE RECORD`S SENTENCE IS COMPOSED AT THE CLOSE FROM THE BANK'], 0, 0
    import act_close as AC
    ev = rdf('data/b749_events.txt')
    n += 1
    g += guard(L, 'words', 'the instance: b749`s events (5) carries the author`s word on the halt verbatim, and no data/b749_author_words.txt stands', 'word in events %s ; bank %s' % (
        B749_WORDS[:40] in ev, os.path.exists(os.path.join(D, 'b749_author_words.txt'))), B749_WORDS[:40] in ev and not os.path.exists(os.path.join(D, 'b749_author_words.txt')))
    d = tempfile.mkdtemp(dir=SCRATCH)
    o_pre = AC.author_words_section('b749', d)
    n_pre = A.author_words_section('b749', d)
    n += 1
    g += case(L, 'words', 'before the root, no bank (b749`s record and trail, composed before the root)', o_pre[0][:110], n_pre[0][:110],
              'NONE RECEIVED' in o_pre[0], 'NOT YET COMPOSED' in n_pre[0].upper() and 'NONE RECEIVED' not in n_pre[0])
    io.open(os.path.join(d, 'b749_act_root.json'), 'w', encoding='utf-8', newline='\n').write('{}\n')
    io.open(os.path.join(d, 'b749_author_words.txt'), 'w', encoding='utf-8', newline='\n').write(A.words_append('', B749_WORDS, '2026-11-09T20:13:16Z', 'b749_words_src.txt'))
    n_close = A.author_words_section('b749', d)
    shutil.rmtree(d, ignore_errors=True)
    n += 1
    g += guard(L, 'words', 'at the close, b749`s word replayed into the bank by the appending route (standing.act.words_append): the sentence prints it verbatim',
               '%s ... %d lines' % (n_close[0][:70], len(n_close)), any(B749_WORDS[:60] in l for l in n_close) and 'NONE RECEIVED' not in n_close[0])
    return L, g, n


# ================================================================================ (closingdry) (3)(v): G-CLOSING-DRY-STEP
def _nf_func():
    src = rdf('tools/standing/fold/checks.tpl')
    m = re.search(r'(?ms)^def not_found_outside_design\(.*?(?=^\S)', src)
    ns = dict(re=re, NL=NL, __builtins__=__builtins__)
    if m:
        exec(m.group(0), ns)   # noqa: S102 -- the template's own function, read from its text
    return ns.get('not_found_outside_design'), bool(m)


def control_closingdry():
    L, g, n = ['### (closingdry) (R360)(3)(v), b749 events (10): THE GATE RECORD`S CLOSING DRY READS A BANK WRITTEN AFTER THE LOCK BY DESIGN AS "NOT YET WRITTEN", AND THE ARM`S PREDICATE READS THE DESIGN LIST'], 0, 0
    gate = show(BASE, 'data/b749_reg_gate.txt')
    rows = [l for l in gate.split(NL) if '): ### NOT FOUND' in l]
    fn, found = _nf_func()
    n += 1
    g += case(L, 'closingdry', 'b749`s gate record (data/b749_reg_gate.txt at %s) through the arm`s clause; its NOT FOUND rows %d: %s' % (BASE, len(rows), '; '.join(r.strip()[:80] for r in rows)),
              'closing_dry_ok wants "): ### NOT FOUND" nowhere in the record: %s' % ('): ### NOT FOUND' not in gate),
              'not_found_outside_design (the template`s, read from its text %s): %s' % (found, (fn(gate, 'b749') if fn else 'UNREAD') or 'NONE'),
              '): ### NOT FOUND' in gate, bool(fn) and fn(gate, 'b749') == [])
    planted = gate + NL + '### THE ROOT`S BANKS (relay data/b749_root_banks.txt): ### NOT FOUND'
    n += 1
    g += guard(L, 'closingdry', 'a NOT FOUND row naming a bank outside the design list still refuses (planted: the root`s banks)', (fn(planted, 'b749') if fn else ['UNREAD'])[:1],
               bool(fn) and len(fn(planted, 'b749')) == 1)
    ct = rdf('tools/standing/fold/closing.tpl')
    n += 1
    g += guard(L, 'closingdry', 'the closing template prints a design-list bank standing without its route`s head as "NOT YET WRITTEN BY ITS ROUTE", not NOT FOUND',
               'the print %s' % ('NOT YET WRITTEN BY ITS ROUTE' in ct), 'NOT YET WRITTEN BY ITS ROUTE' in ct)
    return L, g, n


# ================================================================================ (n5) (3)(vi): THE N5 MATCHER ON THE ZENODO BANKS ALONE
def control_n5():
    L, g, n = ['### (n5) (R360)(3)(vi), b749 defects (l), (q), (t): N5 READS A RELEASE, A NEW VERSION, A PUBLISH OR A REPOSITORY EDIT FROM THE ZENODO BANKS ALONE; "THE DRAFT HELD AT v5" NAMES NO ZENODO OBJECT'], 0, 0
    ent = _git('show', '%s:FINDINGS.md' % B749_PP, repo=PP).replace('\r', '').split(NL)
    line = ent[14527] if len(ent) > 14527 else ''
    tpl0 = show(BASE, 'tools/standing/fold/record.tpl')
    n += 1
    g += case(L, 'n5', 'b749`s entry`s "Carried to" line (PLACE-papers %s FINDINGS :14528, "...the draft held at v5.") and the N5 sentence the template composes beside it' % B749_PP,
              'record.tpl`s N5 sentence joins the worklist`s DRAFT to the monograph`s: "the deposit route untouched (draft %%s, v5, unpublished)" %s' % ('draft %s, v5, unpublished' in tpl0),
              'zenodo_requests over the line: writes %d, releases %d; the template`s sentence reads the Zenodo banks (%s)' % (
                  len(A.zenodo_requests('b749', texts={'FINDINGS :14528': line})['writes']), len(A.zenodo_requests('b749', texts={'FINDINGS :14528': line})['releases']),
                  'standing.act.zenodo_requests' in rdf('tools/standing/fold/record.tpl')),
              'draft %s, v5, unpublished' in tpl0 and 'held at v5' in line,
              not A.zenodo_requests('b749', texts={'FINDINGS :14528': line})['releases'] and not A.zenodo_requests('b749', texts={'FINDINGS :14528': line})['writes']
              and 'draft %s, v5, unpublished' not in rdf('tools/standing/fold/record.tpl'))
    rows = json.loads(show(BASE, 'data/b749_commands.json') or '{}').get('rows') or []
    r65 = next((r for r in rows if r.get('n') == 65), {})
    old_hit = bool(re.search(r'\bgh\s+release\b|/actions/newversion|/actions/publish|zenodo\.org/api|\bgh\s+repo\s+edit\b', r65.get('cmd') or ''))
    z = A.zenodo_requests('b749')
    n += 1
    g += case(L, 'n5', 'b749`s capture row 65 (a read-only git grep for "zenodo.org/api", 14:04:03Z) beside b749`s Zenodo banks',
              'the seat`s matcher over every captured command: row 65 %s' % ('READ AS A RELEASE' if old_hit else 'not read'),
              'the Zenodo banks alone (%s): write requests %s ; releases %s ; row 65 unread' % (', '.join(z['banks']), ', '.join('%s :%d %s' % (b, i, m) for b, i, m, _t in z['writes']) or 'NONE',
                                                                                              len(z['releases'])),
              old_hit, any(m == 'DELETE' for _b, _i, m, _t in z['writes']) and not z['releases'])
    return L, g, n


# ================================================================================ (count) (3)(vii): THE QUESTION COUNT
def control_count():
    L, g, n = ['### (count) (R360)(3)(vii), b749 defect (u), events (6): QUESTIONS COUNTED FROM THE COMPOSED PROMPTS` ROWS, THE SITTING ROWS READ APART'], 0, 0
    t = rdf('data/b749_author_answers.txt')
    o = len(re.findall(r'^### PROMPT |^\[Z\d+\] ', t, re.M))
    c = A.question_count(t)
    n += 1
    g += case(L, 'count', 'b749`s answers bank as it stands (two prompts put, the [Z1] block at the foot)', 'b749`s module (tools/acts/b749.py :669): %d' % o,
              'question_count: prompts %d (counted), calls %d, sitting rows %d (read apart)' % (c['prompts'], c['calls'], c['sitting']), o != 2, c['prompts'] == 2 and c['sitting'] == 1)
    am = rdf('tools/acts/b750.py')
    n += 1
    g += guard(L, 'count', 'the act module`s four counters read the standing count', 'question_count calls %d ; the old regex %d' % (am.count("question_count(rdn('%s_author_answers.txt' % ACT))['prompts']"),
                                                                                                  am.count("r'^### PROMPT |^\\[Z\\d+\\] '")), am.count("question_count(rdn('%s_author_answers.txt' % ACT))['prompts']") == 4)
    return L, g, n


# ================================================================================ (lock) (3)(viii): THE LOCK PRINT
def control_lock():
    L, g, n = ['### (lock) (R360)(3)(viii), b749 events (12): THE SEALED MODULE`S N4 SENTENCE PRINTS THE LOCK FROM THE ONE READER (lockdate), NOT "NOT LOCKED"'], 0, 0
    import lockdate as LD
    lc = LD.lock_of('b749', D)
    ep = LD.lock_epoch(lc, RELAY) if lc else None
    sc = json.loads(rdf('data/b749_scores_close.json') or '{}').get('N4') or ['', '']
    o_src = show(BASE, 'tools/acts/b749.py')
    n_src = rdf('tools/acts/b750.py')
    iso = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ep)) if ep else None
    n += 1
    g += case(L, 'lock', 'b749`s N4 sentence (data/b749_scores_close.json) and its lock by the one reader (%s)' % ((lc or '?')[:8]),
              'lock_iso=None in _post_lock_edits %s ; the sentence prints "%s"' % ('lock_iso=None' in o_src, re.search(r'the lock at [^,]+', sc[1]).group(0) if re.search(r'the lock at [^,]+', sc[1]) else '?'),
              'lock_iso from the reader`s epoch %s ; b749`s lock reads %s (the commit`s own time %s)' % ("time.gmtime(lock)" in n_src, iso, _git('log', '-1', '--format=%cI', lc or 'HEAD').strip()),
              'the lock at NOT LOCKED' in sc[1] and 'lock_iso=None' in o_src, "lock_iso=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock))" in n_src and bool(iso))
    return L, g, n


# ================================================================================ (permit) (3)(ix) and (retries) (3)(xi): RULES, READ FROM THE RULES BANK
def _rule(k):
    t = rdf('data/b750_rules.txt')
    m = re.search(r'(?ms)^\(%d\) (.*?)(?=^\(\d+\) |\Z)' % k, t)
    return m.group(1).strip() if m else ''


def control_permit():
    L, g, n = ['### (permit) (R360)(3)(ix), b749 defect (j): A RULING`S PERMISSION FOR A DATED NOTE NAMES THE FACTS THE NOTE MUST CARRY AND LETS IT CARRY THE ACT`S CITED FACTS BESIDE THEM (THE NAVIGATOR`S, CLAIM, NEW)'], 0, 0
    df = rdf('data/b749_defects.txt').split(NL)
    n += 1
    g += guard(L, 'permit', 'the instance: b749`s (j), the d1-1 note longer than (R359)(2)(v) permitted', df[15][:100] if len(df) > 15 else 'ABSENT', len(df) > 15 and df[15].lstrip().startswith('(j)'))
    r = _rule(9)
    n += 1
    g += guard(L, 'permit', 'the rule banked (data/b750_rules.txt (9)), the navigator`s beside the seat`s', r[:110] or 'ABSENT', 'NAVIGATOR' in r.upper() and 'cited facts' in r)
    return L, g, n


def control_retries():
    L, g, n = ['### (retries) (R360)(3)(xi), b749 events (1), (2), (11), REPEAT: EACH RETRY AN EVENT WITH ITS TIMINGS; A COMMAND THE HOST MOVES TO THE BACKGROUND SENT WITH THE LIMIT THE TOOL PRINTS, THE MOVE AN EVENT'], 0, 0
    ev = rdf('data/b749_events.txt').split(NL)
    inst = [ev[i][:90] for i in (3, 4, 25) if len(ev) > i]
    n += 1
    g += guard(L, 'retries', 'the instances: b749 events (1), (2), (11)', ' | '.join(inst), len(inst) == 3 and all(x.lstrip().startswith(('(1)', '(2)', '(11)')) for x in inst))
    r = _rule(11)
    n += 1
    g += guard(L, 'retries', 'the rule banked (data/b750_rules.txt (11))', r[:110] or 'ABSENT', 'retry' in r and 'background' in r)
    r3 = _rule(3)
    n += 1
    g += guard(L, 'retries', 'the halt rule banked beside it (data/b750_rules.txt (3), (R360)(3)(iii))', r3[:110] or 'ABSENT', 'halt question' in r3.lower() and 'score' in r3.lower())
    return L, g, n


# ================================================================================ (carry) (3)(x): THE CARRY REFUSES THE ROWS THE RULING DOES NOT NAME
def _carried(act, prev, pprev, ref_prev):
    """the act module as `carry acts` wrote it: the previous act's module under the carry's table -- the act names and the ruling numbers shifted
    (b750's table, tools/b750_carry.py SUBS: b749 -> b750, b748 -> b749, R359 -> R360, R358 -> R359); `ruled` is given the act names alone, as
    its CLI gives them."""
    r = int(act[1:]) - 390   # ### the ruling's number: (R360) for b750, (R359) for b749
    full = (('b%d' % int(prev[1:]), 'b%d' % int(act[1:])), ('b%d' % int(pprev[1:]), 'b%d' % int(prev[1:])), ('R%d' % (r - 1), 'R%d' % r), ('R%d' % (r - 2), 'R%d' % (r - 1)))
    src = show(ref_prev, 'tools/acts/%s.py' % prev)
    return CA.substitute(src, full), src, full[:2]


def control_carry():
    L, g, n = ['### (carry) (R360)(3)(x), b749 defects (b), (d), (g), (k), b750 step-zero (d): THE CARRY PRINTS EVERY ROW IT BRINGS BESIDE THE RULING AND REFUSES THE ONES IT DOES NOT NAME (R5); '
               'SHARED_EDITS FROM THE ACT`S OWN LIST'], 0, 0
    OCA = old('carry.py', 'carry_v1290')
    for act, prev, pprev, ref, wl_ref, pwl_ref in (('b749', 'b748', 'b747', B748_HEAD, BASE, B748_HEAD), ('b750', 'b749', 'b748', BASE, None, BASE)):
        carried, src, subs = _carried(act, prev, pprev, ref)
        wl = rdf('tools/%s_worklist.py' % act) if wl_ref is None else show(wl_ref, 'tools/%s_worklist.py' % act)
        pwl = show(pwl_ref, 'tools/%s_worklist.py' % prev)
        fer = show(BASE, 'data/b749_ferry.txt') if act == 'b749' else rdf('data/b750_ferry.txt')
        _Lo, ro = OCA.ruled(carried, src, wl, pwl, fer, subs)
        Ln, rn = CA.ruled(carried, src, wl, pwl, fer, subs)
        r5 = [r for r in rn if r[0] == 'R5']
        n += 1
        g += case(L, 'carry', '%s`s module as `carry acts` wrote it (tools/acts/%s.py at %s, the act names substituted) beside %s`s ruling' % (act, prev, ref, act),
                  'v1.29.0`s ruled: refused %d (%s)' % (len(ro), ', '.join('%s %s' % r[:2] for r in ro) or 'NONE'),
                  'v1.30.0`s ruled: refused %d, R4 %d, R5 %d (%s)' % (len(rn), sum(1 for r in rn if r[0] == 'R4'), len(r5), '; '.join('%s: %s' % (r[1], r[2][:90]) for r in r5) or 'NONE'),
                  bool(set(r[1] for r in r5) - set(r[1] for r in ro)), bool(r5))
        L.append('      let through by v1.29.0 and refused by v1.30.0: %s' % (', '.join(sorted(set(r[1] for r in r5) - set(r[1] for r in ro))) or 'NONE'))
    se = A.shared_edits('b749', B748_HEAD, BASE)
    try:
        carried_se = json.loads(show('1178e7e3', 'data/act_current.json') or '{}').get('shared_edits')
    except ValueError:
        carried_se = None
    n += 1
    g += case(L, 'carry', 'b749`s data/act_current.json shared_edits (defect (k))', 'carried from b748`s file at 1178e7e3: %s' % (carried_se,),
              'shared_edits(b749, %s..%s): %s' % (B748_HEAD, BASE, se or '[]'), bool(carried_se), se == [])
    return L, g, n


# ================================================================================ (instances) (3)(xii): THE DELETE READER AND THE INSTANCES PRINTED
def _old_delete_shape():
    src = show(BASE, 'tools/b698_record.py')
    ns = dict(re=re)
    for pat in (r'(?m)^QUOTED = .*$', r'(?m)^SHELL_VAR = .*$', r'(?ms)^def delete_shape\(.*?(?=^\S)'):
        m = re.search(pat, src)
        exec(m.group(0), ns)   # noqa: S102 -- b698's reader, read from its blob
    return ns['delete_shape']


def control_instances():
    L, g, n = ['### (instances) (R360)(3)(xii), b749 defects (n), (o), (p), (v), events (3), (7), (8), refusals (a), (e), (i), (r), (s): THE CAPTURE`S DELETE READER TAUGHT THE TOOL`S ROUTE; THE INSTANCES PRINTED'], 0, 0
    ods = _old_delete_shape()
    rows = json.loads(show(BASE, 'data/b749_commands.json') or '{}').get('rows') or []
    tool = [r for r in rows if re.match(r'^python -X utf8 -u tools/standing/commit\.py (?:relay|pp) delete \S+$', (r.get('cmd') or '').strip())]
    o_names = [x for r in tool for x in ods(r['cmd'])[0]]
    n_names = [x for r in tool for x in DR.delete_shape(r['cmd'])[0]]
    n += 1
    g += case(L, 'instances', 'b749`s five step-zero deletes through the tool (capture rows %s)' % ', '.join(str(r['n']) for r in tool),
              'b698`s delete_shape: %d names' % len(o_names), 'delread.delete_shape: %d names (%s), chained after %s' % (len(n_names), ', '.join(n_names), [DR.chained_after(r['cmd']) for r in tool]),
              len(tool) == 5 and not o_names, len(n_names) == 5 and not any(DR.chained_after(r['cmd']) for r in tool))
    progs = [r for r in rows if (r.get('cmd') or '').lstrip().startswith('python') and ods(r['cmd'])[0] and 'commit.py' not in (r.get('cmd') or '').split('\n')[0]]
    n += 1
    g += case(L, 'instances', 'b749`s one-line programs quoting a delete in their test strings (capture rows %s)' % ', '.join(str(r['n']) for r in progs),
              'b698`s delete_shape reads deletes in them: %s' % ['%s %s' % (r['n'], ods(r['cmd'])[:2]) for r in progs][:2],
              'delread.delete_shape: %s' % ['%s %s' % (r['n'], DR.delete_shape(r['cmd'])[0]) for r in progs][:2], bool(progs), bool(progs) and not any(DR.delete_shape(r['cmd'])[0] for r in progs))
    n += 1
    g += guard(L, 'instances', 'a plain `git branch -d` and `git push origin --delete` still read, quoted names unquoted', '%s ; %s' % (
        DR.delete_shape('git -C D:/relay branch -d "push-x"')[0], DR.delete_shape('cd D:/relay && git push origin --delete push-y')[0]),
        DR.delete_shape('git -C D:/relay branch -d "push-x"')[0] == ['push-x'] and DR.delete_shape('cd D:/relay && git push origin --delete push-y')[0] == ['push-y'])
    df = rdf('data/b749_defects.txt').split(NL)
    ev = rdf('data/b749_events.txt').split(NL)
    inst = [('(o) the ferry route', df, 20), ('(p) the range moved after the face', df, 21), ('(v) the gate`s words', df, 27), ('events (8) the step-rows words', ev, 20)]
    for what, src, i in inst:
        n += 1
        g += guard(L, 'instances', 'printed: b749 %s' % what, (src[i].strip()[:110] if len(src) > i else 'ABSENT'), len(src) > i and bool(src[i].strip()))
    rf = [l for l in rdf('data/b749_hook_refusals.txt').split(NL) if l.strip()]
    n += 1
    g += guard(L, 'instances', 'printed: b749`s hook refusals, data/b749_hook_refusals.txt, by kind', '%d rows: %s' % (len(rf), ', '.join('%s %d' % (k, sum(1 for l in rf if '| %s |' % k in l)) for k in ('PIPE', 'READ', 'SED', 'REDIR', 'LOCKED'))),
               len(rf) == 18)
    return L, g, n


def control_version():
    L, g, n = ['### (version) (R360)(3)(xiii): THE STANDING VERSION PRINTED AND ITS CONTROLS TALLIED'], 0, 0
    ver = open(os.path.join(S, 'VERSION'), encoding='utf-8').read().strip()
    o = show(BASE, 'tools/standing/VERSION').strip()
    n += 1
    g += case(L, 'version', 'tools/standing/VERSION', o, ver, o == 'v1.29.0', ver == 'v1.30.0')
    return L, g, n


CONTROLS = dict(answers=control_answers, hook=control_hook, halt=control_halt, words=control_words, closingdry=control_closingdry, n5=control_n5,
                count=control_count, lock=control_lock, permit=control_permit, carry=control_carry, retries=control_retries, instances=control_instances,
                version=control_version)
ORDER = ('answers', 'hook', 'halt', 'words', 'closingdry', 'n5', 'count', 'lock', 'permit', 'carry', 'retries', 'instances', 'version')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.30.0, (R360)(3)(i)-(xiii): THE ANSWERS ROUTE APPENDING, THE HOOK`S ROW (65) AND THE DESIGN LIST, A HALT QUESTION NAMING ITS COSTS, '
           'THE AUTHOR`S WORDS COMPOSED AT THE CLOSE, THE CLOSING DRY`S DESIGN BANKS, N5 ON THE ZENODO BANKS, THE QUESTION COUNT, THE LOCK PRINT, THE PERMISSION RULE, THE CARRY`S R5 AND '
           'SHARED_EDITS, THE RETRIES RULE, THE DELETE READER AND THE INSTANCES, THE VERSION (%s)' % (act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
           '', '## THE CONTROLS',
           '  the bank is its controls: the compile control first, then each repair`s instances through both routes; the free memory read before each; written through tools/standing/figbank.py', '',
           '### THE COMPILE CONTROL, BEFORE ANY FIGURE ((R345)(2)(i), carried):'] + CC.lines(CC.check(act)) + [
           '', '### each case through both routes, the route before read from %s' % BASE, '']
    tg = tn = 0
    per = []
    for k in names:
        out.append(free_line())
        try:
            L, g, c = CONTROLS[k]()
        except (Exception, SystemExit) as e:  # noqa: BLE001
            L, g, c = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
        out += L + ['']
        tg, tn = tg + g, tn + c
        per.append('(%s) %d of %d' % (k, g, c))
    out.append('### per repair: %s' % ' ; '.join(per))
    out.append('### ### **v1.30.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        r = FB.write(os.path.join(D, '%s_standing_v1300.txt' % act), NL.join(out))
        print('written data/%s_standing_v1300.txt (figbank: %s)' % (act, r['why']))


if __name__ == '__main__':
    main(sys.argv[1:])
