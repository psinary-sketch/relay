# -*- coding: utf-8 -*-
"""standing/close.py -- THE CLOSE'S CORE: the head line, the suite's tally, the withheld field, neg_shown's three lists and the seal's
record, each a function of the banks it reads, the act passed at the call.

Extracted, not imported (the author's word (1)(a) of the toolset act). Provenance, each function copied and its act constants removed:
  head_line          tools/b714_closing.py head_line (:242-:290), SCORE_KEYS (:62), DEFECT_ROW (:125); each repository's main passed
                     in (the replay: the step bank's last row before the closing) or read at the remote by ls-remote (the live close)
  PART_FOOT          tools/b703_checks.py :1719
  ARM_ROW, tally     tools/b714_checks.py ARM_ROW (:1912), _combine_tally (:1915-:1944), combine's figure lines (:1969-:1974)
  withheld           tools/b714_checks.py WITHHELD (:1760) made a field read from the ruling (the class repair (4)(ii)): each entry
                     {arm, defect, cause, absent}, its condition (the file `absent` not present) read at seal time; an entry whose
                     condition fails is not withheld
  neg_shown          tools/b714_checks.py neg_shown (:1766-:1792), its three lists returned by name (the class repair (4)(vi))
  letters_of         tools/b714_record.py letters_of (:245) and tools/b703_record.py read_defect_row (:90)
  seal_record        tools/b714_checks.py seal (:1800-:1840), the record's fields rebuilt from the banks at the seal's commit
"""
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

NL = '\n'
SCORE_KEYS = (('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3'))
DEFECT_ROW = re.compile(r"^    \(([a-z]'?)\) ")
PART_FOOT = re.compile(r'### PART ([\w-]+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE) ; NEGATIVE-CONTROL '
                       r'FAILURES (\d+) ; POSITIVE-CONTROL PASSES (\d+) (\[[^\]]*\]|NONE) ; DECLARED EQ RUN (\w+) ; (\d+) s')
ARM_ROW = re.compile(r'^  (G-[\w-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+[\d.]+\s+(.*)$', re.M)
FIG_LINE = re.compile(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\. ### LIVE FAILING : (\d+) ?(\[[^\]]*\])?\.'
                      r'(?: ### WITHHELD, NOT EXERCISABLE : (\d+) ?(\[[^\]]*\])?\.)?')
CTL_LINE = re.compile(r'NEGATIVE-CONTROL FAILURES : (\d+)\. ### POSITIVE-CONTROL PASSES : (\d+) ?(\[[^\]]*\])?\.')
VERDICT_LINE = re.compile(r'VERDICT : ([^*;]+?)(?: ; WITHHELD, NOT EXERCISABLE, COUNTED NEITHER PASSING NOR FAILING: ([^*]+))?\*\*')

NegShown = collections.namedtuple('NegShown', 'shown bad withheld')


# ======================================================================== THE HEAD LINE
def ls_remote_main(repo):
    out = A.gs(repo, 'ls-remote', 'origin', 'refs/heads/main') or ''
    for l in out.split(NL):
        if '\t' in l:
            return l.split('\t')[0].strip()
    return ''


def mains_from_steps(act):
    """each repository's main as the close read it: the step bank's last row before the closing's (the record's commit), by repository."""
    out = {}
    for r in A.steps(act):
        if r.get('phase') == 'closing':
            break
        out[r.get('repo')] = r.get('commit')
    return out


def head_line(act, mains=None, events=None, rev=None):
    """the act's head line from its banks (now, or at a commit): each repository's main (passed in, or read at the remote), the suite's
    figures from the post-push tally, the root, the prompts, the scores and the defects. A main not read goes to `events`, never the line."""
    ev = [] if events is None else events
    parts = []
    for key in ('relay', 'pp'):
        name, w = A.NAMES[key], 8 if key == 'relay' else 7
        main = (mains or {}).get(key) if mains is not None else ls_remote_main(key)
        if not main:
            ev.append('%s: no main read; the head line carries none read' % name)
            parts.append('%s none read' % name)
            continue
        parts.append('%s %s' % (name, main[:w]))
    sm = FIG_LINE.search(A.rd('%s_checks_postpush.txt' % act, rev))
    suite = ('suite %s of %s' % (sm.group(2), sm.group(1))) if sm else 'suite ### NOT READ'
    try:
        root = json.loads(A.rd('%s_act_root.json' % act, rev))['root'][:16] + '…'
    except (ValueError, KeyError, TypeError):
        root = '### NOT READ'
    k = len(re.findall(r'^### PROMPT ', A.rd('%s_author_answers.txt' % act, rev), re.M))
    d = len([l for l in A.rd('%s_defects.txt' % act, rev).split(NL) if DEFECT_ROW.match(l)])
    sc = A.jl('%s_scores_close.json' % act, rev)
    keys = [x for ks in SCORE_KEYS for x in ks]
    held = sum(1 for x in keys if (sc.get(x) or [''])[0] == 'HELD')
    scores = ('scores %d of %d HELD' % (held, len(keys))) if all(x in sc for x in keys) else 'scores ### NOT READ'
    return '%s closed: %s; %s; root %s; %d prompt%s answered; %s; %d defect%s' % (act, ', '.join(parts), suite, root, k, '' if k == 1 else 's',
                                                                                 scores, d, '' if d == 1 else 's')


# ======================================================================== THE SUITE'S TALLY
def part_banks(act, base, parts, rev=None):
    """[(part, its footer match, its text)] for the act's part banks data/<act>_<base>_<part>.txt; a part with no footer is (part, None, text)."""
    out = []
    for p in parts:
        t = A.rd('%s_%s_%s.txt' % (act, base, p), rev)
        m = PART_FOOT.search(t)
        out.append((p, m if (m and m.group(1) == p) else None, t))
    return out


def combine_tally(parts, W):
    """the combine's figures summed from the parts' footers, an arm in the withheld field W taken out by its row (a part written before
    the field counted it as it fell; a part written after prints the row WITHHELD and its footer left it out). Returns (arms, passing,
    failing, neg failures, pos passes, failing names, pos-pass names, withheld names)."""
    n = sum(int(m.group(2)) for _p, m, _t in parts)
    lp = sum(int(m.group(3)) for _p, m, _t in parts)
    lf = sum(int(m.group(4)) for _p, m, _t in parts)
    ng = sum(int(m.group(6)) for _p, m, _t in parts)
    pc = sum(int(m.group(7)) for _p, m, _t in parts)
    fails = sum((json.loads(m.group(5)) if m.group(5) != 'NONE' else [] for _p, m, _t in parts), [])
    defs = sum((json.loads(m.group(8)) if m.group(8) != 'NONE' else [] for _p, m, _t in parts), [])
    wh = []
    for _p, _m, t in parts:
        for r in ARM_ROW.finditer(t):
            nm, live, neg, pos, verdict = r.groups()
            if nm not in W or nm in wh:
                continue
            wh.append(nm)
            if verdict.startswith('WITHHELD'):
                continue
            if live == 'PASS':
                lp -= 1
            else:
                lf, fails = lf - 1, [f for f in fails if f != nm]
            if neg != live:
                ng -= 1
            if pos == 'PASS':
                pc, defs = pc - 1, [d for d in defs if d != nm]
    return n, lp, lf, ng, pc, fails, defs, wh


def tally_lines(parts, W, carried):
    """the combine's three figure lines (arms, controls, verdict), in the form the combine prints them."""
    n, lp, lf, ng, pc, fails, defs, wh = combine_tally(parts, W)
    deq = all(m.group(9) == 'True' for _p, m, _t in parts)
    car = [f for f in fails if f in carried]
    ok = lf == len(car) and pc == 0 and ng == 0 and deq
    return dict(arms=n, passing=lp, failing=lf, fails=fails, neg=ng, pos=pc, defs=defs, withheld=wh, lines=[
        '  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s. ### WITHHELD, NOT EXERCISABLE : %d %s.**' % (
            n, lp, lf, fails or '', len(wh), wh or ''),
        '  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (ng, pc, defs or ''),
        '  ### ### **VERDICT : %s%s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if (ok and not fails) else
                                         'EVERY ARM PASSES BUT THE CARRIED FAILURE DECLARED ON THE FACE, AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN',
                                         ' ; WITHHELD, NOT EXERCISABLE, COUNTED NEITHER PASSING NOR FAILING: %s' % ', '.join(wh) if wh else '')])


def read_tally(text):
    """the figures a combined bank prints, read back by its own lines: (arms, passing, failing, failing names, withheld, withheld names,
    neg, pos, pos names, verdict, verdict's withheld)."""
    f, c, v = FIG_LINE.search(text), CTL_LINE.search(text), VERDICT_LINE.search(text)
    lst = lambda s: json.loads(s.replace("'", '"')) if s else []
    return dict(arms=int(f.group(1)) if f else None, passing=int(f.group(2)) if f else None, failing=int(f.group(3)) if f else None,
                fails=lst(f.group(4)) if f else None, withheld=lst(f.group(6)) if (f and f.group(5)) else [],
                neg=int(c.group(1)) if c else None, pos=int(c.group(2)) if c else None, defs=lst(c.group(3)) if c else None,
                verdict=v.group(1).strip() if v else None)


CARRIED_LINE = re.compile(r'the failures declared on the face as carried \(section \(G2\)\): (\[[^\]]*\]|NONE)')


def carried_of(text):
    """the carried failures a combined bank prints as declared on its face."""
    m = CARRIED_LINE.search(text)
    return json.loads(m.group(1).replace("'", '"')) if (m and m.group(1) != 'NONE') else []


# ======================================================================== THE WITHHELD FIELD, CONDITION-BOUND
def withheld_entries(spec, rev=None, exists=None):
    """the ruling's withheld field read at seal time: [(arm, reason)] for each entry whose condition holds (its file `absent` not present,
    in the tree now or at a commit); an entry whose condition fails is not withheld. `exists` may be passed for a constructed control."""
    def present(rel):
        if exists is not None:
            return exists(rel)
        if rev is not None:
            return A.blob(rev, rel) is not None
        return os.path.exists(os.path.join(A.RELAY, *rel.split('/')))
    out = []
    for e in spec or []:
        if not present(e['absent']):
            out.append((e['arm'], 'defect %s: %s (%s absent at the seal)' % (e['defect'], e['cause'], e['absent'])))
    return out


# ======================================================================== neg_shown, ITS THREE LISTS
def neg_shown(arms, banks, withheld):
    """an arm's NEG control shown failing on its mutated copy, read from the pre-run's exercise banks: `arms` [(arm, part)], `banks`
    {part: exercise json}, `withheld` [(arm, reason)] the field's entries whose condition holds. An arm with no row, whose mutated copy
    passed, or whose plant or predicate raised, is not shown; an arm in `withheld` whose mutated copy passed is withheld. Returns NegShown
    (shown, bad, withheld), each a list, read by name by every caller."""
    wl = dict(withheld)
    shown, bad, wh = [], [], []
    for n, p in arms:
        j = banks.get(p) or {}
        e = (j.get('exercise') or {}).get(n)
        if j.get('mode') != 'prerun':
            bad.append((n, 'part %s: no pre-run exercise bank (mode %s)' % (p, j.get('mode'))))
        elif e is None:
            bad.append((n, 'part %s: no row in the pre-run' % p))
        elif e.get('pos') and n in wl:
            wh.append((n, wl[n]))
        elif e.get('pos'):
            bad.append((n, 'the mutated copy PASSED'))
        elif e.get('pos_raised') or not e.get('shown_failing'):
            bad.append((n, 'the mutated copy raised: %s' % e.get('pos_raised')))
        else:
            shown.append(n)
    return NegShown(shown, bad, wh)


def exercise_banks(act, parts, rev=None):
    return dict((p, A.jl('%s_exercise_%s.json' % (act, p), rev)) for p in parts)


def arms_of(banks, parts):
    """[(arm, part)] the arms the parts' exercise banks carry, in part order."""
    return [(n, p) for p in parts for n in ((banks.get(p) or {}).get('exercise') or {})]


# ======================================================================== THE LETTERS AND THE SEAL'S RECORD
def read_defect_row(L, i):
    """one lettered defect row of a defects bank, its continuation lines joined: '(x) HEAD', the row's text to its first full stop."""
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
        j += 1
    m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
    return m.group(0)[:-1] if m else None


def letters_of(text):
    L = (text or '').replace('\r', '').split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


PREV_KEYS = ('pass_on_prev', 'fail_as_prev', 'diverge', 'not_run_by_prev')


def seal_record(act, parts, rev, defects_rev, withheld_spec):
    """the seal's record rebuilt from the banks: the sealed tools' sha256 at the seal's commit `rev` (the seal hashed the working tree, and
    the seal's commit is the first to carry what it hashed), and apart at the record's own relay head; the letters and the defects' sha256
    of the defects bank at `defects_rev`; neg_shown's count and the withheld field from the pre-run's exercise banks at `rev`; the runs on
    the previous act's banks. Returns (the rebuilt fields, the record as written)."""
    rec = A.jl('%s_seal_hashes.json' % act)
    head = rec.get('relay_head')
    tools, at_head = {}, {}
    for t in rec.get('tools') or {}:
        b = A.blob(rev, 'tools/' + t)
        tools[t] = A.sha256_bytes(b) if b is not None else None
        h = A.blob(head, 'tools/' + t) if head else None
        at_head[t] = A.sha256_bytes(h) if h is not None else None
    dtext = A.rd('%s_defects.txt' % act, defects_rev)
    banks = exercise_banks(act, parts, rev)
    ns = neg_shown(arms_of(banks, parts), banks, withheld_entries(withheld_spec, rev=rev))
    prev_run = {}
    for p in sorted(set(p for _n, p in arms_of(banks, parts))):
        j = A.jl('%s_prevrun_exercise_%s.json' % (act, p), rev)
        if j:
            prev_run[p] = dict((k, len(v)) for k, v in j.items() if k in PREV_KEYS)
    got = dict(tools=tools, tools_at_head=at_head, letters=letters_of(dtext), defects_sha256=A.sha256_bytes(dtext.encode('utf-8')), neg_shown=len(ns.shown),
               bad=ns.bad, withheld=[dict(arm=n, reason=w) for n, w in ns.withheld], prev_run=prev_run)
    return got, rec
