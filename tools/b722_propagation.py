# -*- coding: utf-8 -*-
"""b722_propagation.py -- THE PROPAGATION READ, standing clauses v8 row (82), (R332)(8). Written whole at b722 by the Write tool.

  read [dry]    for each object: its names printed BEFORE any search; then every hit in REGISTRY, OPEN_TRAILS, SPIRAL_MAP, FINDINGS, the
                keystones (the seven day1 papers and THE_KEYSTONE_CENSUS at its current version), the relay's tracked banks (data/), and
                for (iii) SIDE-lv-conservation's README at its main and at v0.10.0 and the deposit descriptions banked in the relay; each
                hit dated (a PLACE-papers line by `git blame` of that line; a relay bank by its act number, or its first commit where it
                carries none) and graded READS RIGHT, READS WRONG or DATED by the object's rule (printed before its hits), the hand table
                HAND overriding a rule's grade with its reason printed; a hit naming another object is printed NOT THIS OBJECT and graded
                nothing. Any hit the rule leaves UNREAD and the hand table does not grade refuses the bank. -> data/b722_propagation.txt/.json
  notes [dry]   composes the dated notes, one per READS WRONG and DATED hit, each pointing to the line it corrects, and lands them as one
                appended block in FINDINGS through b698's guarded landing (the act's ledger write); no line of any ledger is rewritten; a
                hit in a public README or a deposit's description is LISTED FOR THE RELEASE SITTING and not noted there.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b722'
PP = 'D:/MY-DOwnloads/PLACE-papers'
LV = 'D:/SIDE-lv-conservation'
LEDGERS = ['REGISTRY.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'FINDINGS.md',
           'day1/Silence_of_Foundations.md', 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md',
           'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md', 'day1/Which_Structure_Confines.md',
           'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md']
SELF = ('data/b722_ferry.txt', 'data/b722_propagation.txt', 'data/b722_propagation.json', 'data/b722_readfirst.txt',
        'data/b722_citation_check.txt', 'data/b722_citation_check.json', 'data/b722_prune_citation.txt', 'data/b722_carry_citation.txt',
        'data/b722_rules.txt', 'data/standing_clauses_v8.txt')   # ### the act's own ruling and banks: the question, not the record read

# ### THE OBJECTS ((R332)(8)): names, the correction, and the rule. `pairs`: a hit is a line carrying every needle of one pair (case-insensitive).
OBJECTS = [
    dict(key='i', what='the law "b(n0) = -2", refuted in its value clause at -40 (b720)',
         names=[('b(n0) = -2',), ('b(n0) = −2',), ('b(n₀) = -2',), ('b(n_0) = -2',), ('coefficient law',)],
         correction='relay data/b720_coeffs.txt :57 (n0(-40) = 100, b = -1/2 ; THE LAW REFUTED), its first commit the boundary; FINDINGS :11072',
         boundary_bank='data/b720_coeffs.txt', boundary_act=720,
         right=r'REFUTED|refuted|-1/2|−1/2|value clause|or -1/2|not derived|clause 2|second clause',
         instance=r'\bat (?:-|−)(?:23|15|39|20|47|35)\b|at the three|HELD at|held at|at both|H-C\d|at -20 and -47|at (?:-|−)35 and',
         rule='READS RIGHT where the line names the refutation or restricts the value (REFUTED, -1/2, "value clause", "not derived"), or states '
              'the law at a field where it holds (an instance); otherwise DATED when written before the boundary and READS WRONG after it.'),
    dict(key='ii', what='T-COUNT at Q0 named as assumed (FINDINGS :8881), against its derivation at b685-b687',
         names=[('T-COUNT', 'assum')],
         correction='relay data/b718_count_read.txt :19-:27 ("T-COUNT at Q0 is derived on the record (b685-b687, written and certified in balls, '
                    'not compiled)"; data/b687_p3_status.txt :8 "DERIVED ... not compiled"), the boundary data/b687_p3_status.txt`s first commit',
         boundary_bank='data/b687_p3_status.txt', boundary_act=687,
         right=r'DERIVED|\bderived\b|overtaken|b687_p3_status',
         other=r'\bQ1\b|-15\b|-39\b|−15|−39|at Q1|for Q1|x\^2 \+ xy \+ (?:4|10)y',
         rule='NOT THIS OBJECT where the line is about Q1 (-15 or -39), where T-COUNT is carried as an assumption and not derived; READS RIGHT '
              'where it names the derivation (DERIVED, b687_p3_status, overtaken); otherwise DATED before the boundary and READS WRONG after.'),
    dict(key='iii', what='SIDE-lv-conservation v0.10.0 named as free of sorry, against data/b721_rebuild.txt',
         names=[(k, s) for k in ('lv-conservation', 'LvConservation') for s in ('0 sorry', '0-sorry', 'no sorry', 'sorry-free', 'sorry free',
                                                                              'free of sorry', 'zero sorry', '0 sorries', 'no sorries')],
         correction='relay data/b721_rebuild.txt :54 ("6 OF 6 WAVE 1 KERNELS BUILD AT THEIR OWN PINS (ONE WITH A SORRY: SIDE-lv-conservation)") '
                    'and :22 (T3_perClass_to_combinations depends on axioms [propext, sorryAx, ...]), the boundary its first commit',
         boundary_bank='data/b721_rebuild.txt', boundary_act=721,
         right=r'one sorry|a sorry|exactly one|1 sorry|sorryAx|with a sorry|pinned at|quarantin|sorry lines|legacy',
         rule='READS RIGHT where the line names the sorry (one sorry, sorryAx, pinned, the quarantine) or names no version`s sorry count; '
              'otherwise DATED before the boundary and READS WRONG after; a hit naming another version than v0.10.0 is NOT THIS OBJECT '
              'unless it names the kernel at large.'),
]

# ### THE COPY SCREEN: a relay bank whose role is to copy or quote text standing elsewhere -- a json mirror of a text bank, a citation check,
# ### a carry, prune or repair diff, a scan file, a command or exercise log, a touch, differs or readfirst quotation, a gate, satisfiability,
# ### suite or score log, a findings/trail/report json, a desk note, a build log, a sentence or claim table, an audit or fetch copy -- states
# ### nothing of its own: its hit is printed COPY, graded where its source stands, and takes no note.
COPY = re.compile(r'(?:\.json|\.jsonl)$|_citation_check|_carry_|_prune_|_repairdiff_|_scanfile_|_commands\.|_exercise|_touch|_differs|'
                  r'_readfirst|_reg_gate|_satisfiable|_checks|_arms_prerun|_suite\.|_scores|_desk_notes|_buildlog_|_sentence|_quote|'
                  r'_census|_reads\.|_cp1b|_survey|_partners|_closing_dry|_extract|_trial_build|_axiom_claim|_sorry_|_no_sorry|_table_|'
                  r'_onecopy|_tiers|_fano|_lv_tag|_pin\.txt|_components\.txt|_same_season|^data/_b\d{3}/|^data/audit_|zenodo_listing|'
                  r'_r\d_p\d\.|_q0_lines|_q0_reread|_faces_diff|_faces_rows|_count_read|_landing\.txt|_nodes_zeta|_li_readings')

# ### THE MATCHER LINEAGE (feedback: print every matcher version's yield): v1 ran dry, unbanked, before this version.
LINEAGE = ('v1 (iii) named by "lv-conservation" AND "sorry", no copy screen: HITS 802 ((i) 119, (ii) 207, (iii) 476), NOTES 501 -- discarded as '
           'permissive, (iii) catching the sorry-quarantine record and copies taking notes ; v2 (this run) (iii) by a no-sorry phrase, the copy screen, '
           'the hand table')

# ### THE HAND TABLE: (object, path, line) -> (grade, reason), from the seat's read of each line (Read tool, by offset), printed beside the rule.
_R = 'READS RIGHT'
_HI = {   # ### object (i): (path, line) -> (grade, reason)
    'PLACE-papers:FINDINGS.md': {10858: (_R, 'the title names the n0 rule, no value'),
                                 10860: ('DATED', 'carries clause 1, b(n0) = -2, as the clause still to derive, before -40')},
    'PLACE-papers:OPEN_TRAILS.md': {16128: (_R, 'a trail head naming the law, no value'),
                                    16164: ('DATED', '"the step that remains is that the least instantiation ... has value -2", before -40'),
                                    16210: ('DATED', 'clause 1 carried as the step "named and narrowed", before -40')},
    'PLACE-papers:day1/Which_Structure_Confines.md': {190: ('NOT THIS OBJECT', 'the multiplicativity "coefficient law" of S1b'),
                                                      196: ('NOT THIS OBJECT', 'the multiplicativity "coefficient law" of S1b')},
    'relay:data/b718_author_answers.txt': {6: (_R, 'quotes FINDINGS :10858`s title'), 17: (_R, 'quotes FINDINGS :10858`s title')},
    'relay:data/b718_closing.txt': {3: (_R, 'the act`s head line naming the law, no value')},
    'relay:data/b718_derivation.txt': {1: (_R, 'a bank head naming the law'), 128: (_R, '"CLAUSE 1 (b(n0) = -2) IS NOT DERIVED"')},
    'relay:data/b718_ferry.txt': {3: (_R, 'the ruling`s head naming the act'), 47: (_R, 'the act line naming the law'),
                                  67: (_R, 'the title form naming the law')},
    'relay:data/b718_registration_2026-10-27.txt': {3: (_R, 'a registration head naming the law'), 148: (_R, 'the title form naming the law')},
    'relay:data/b719_closing.txt': {85: (_R, 'b(n0) = -2 at -20 and -47, where it holds')},
    'relay:data/b719_report.txt': {7: (_R, 'b(n0) = -2 at -20 and -47, where it holds')},
    'relay:data/b719_derivation.txt': {60: (_R, 'evaluated at five instances where it holds'), 63: (_R, '"CLAUSE 1 (b(n0) = -2) IS NOT DERIVED"')},
    'relay:data/b719_ferry.txt': {9: (_R, 'quotes FINDINGS :10858`s title'), 17: (_R, 'a heading naming the law at two fields'),
                                  37: (_R, 'names the law "from observation toward theorem"')},
    'relay:data/b719_prediction.txt': {17: (_R, 'the prediction at -20, HELD'), 26: (_R, 'the prediction at -47, HELD')},
    'relay:data/b719_registrations.txt': {39: (_R, 'PRED-20, HELD'), 41: (_R, 'PRED-47, HELD')},
    'relay:data/b720_closing.txt': {3: (_R, 'the act`s head line, the refuting act')},
    'relay:data/b720_derivation.txt': {117: (_R, 'restricts -2 to four shapes')},
    'relay:data/b720_ferry.txt': {14: ('DATED', '"THE LAW ... carried unchanged: b(n0) = -2", the ruling`s law under test, before -40'),
                                  32: (_R, 'names the law "toward a theorem"')},
    'relay:data/b720_prediction.txt': {21: (_R, 'the prediction at -35, HELD')},
    'relay:data/b720_registration_2026-10-28.txt': {3: (_R, 'a registration head, the refuting act')},
    'relay:data/b720_registrations.txt': {97: (_R, 'PRED-35, HELD')},
}
_HII = {   # ### object (ii)
    'PLACE-papers:OPEN_TRAILS.md': {14944: (_R, 'b688 reading the clause that names the count as assumed, in the derivation`s course')},
    'relay:data/b685_p3.txt': {12: (_R, 'the derivation`s own read quoting the status it set out to change')},
    'relay:data/b688_ferry.txt': {72: (_R, 'b688`s ruling on the line that names T-COUNT as assumed, after the derivation')},
    'relay:data/b688_registration_2026-10-19.txt': {85: (_R, 'reads the clause naming the count as assumed, for its strike')},
    'relay:data/b690_ferry.txt': {9: (_R, 'orders P3`s status read across lines naming the count assumed')},
    'relay:data/b700_ferry.txt': {9: (_R, 'orders P3`s status read across lines naming the count assumed')},
    'relay:data/b718_closing.txt': {101: (_R, '"as FINDINGS :8881 assumed it": attributes the assumption to :8881')},
    'relay:data/b718_report.txt': {12: (_R, '"as FINDINGS :8881 assumed it": attributes the assumption to :8881')},
    'relay:data/b718_ferry.txt': {21: (_R, '"as FINDINGS :8881 assumed it": attributes the assumption to :8881')},
    'relay:data/b719_ferry.txt': {13: ('READS WRONG', 'orders "stands on T-COUNT as assumed", against data/b718_count_read.txt :26')},
}
_HIII = {   # ### object (iii)
    'PLACE-papers:FINDINGS.md': {8311: (_R, '"no sorry stands on any kernel main": the main, not the v0.10.0 pin')},
    'PLACE-papers:SPIRAL_MAP.md': {87: ('DATED', '"T1 ... + T2 s-darkness 0-sorry" beside deposit-pin v0.10.0, T3 unnamed, before b721')},
    'relay:data/b639_deposit_description.txt': {1: (_R, '"no sorry" defines the standard three, names no version')},
    'relay:data/b640_deposit_description.txt': {1: (_R, '"no sorry" defines the standard three, names no version')},
    'relay:data/b640_deposit_description_before_repairs.txt': {1: (_R, '"no sorry" defines the standard three, names no version')},
    'relay:data/b649_closing.txt': {3: (_R, 'the arm "NO SORRY ON MAIN", the main, not the pin')},
    'relay:data/b649_ferry.txt': {140: (_R, 'the arm "NO SORRY ON MAIN", the main, not the pin')},
    'relay:data/b660_author_answers.txt': {32: (_R, '"no sorry on any kernel main", the main, not the pin')},
    'relay:data/b701_ferry.txt': {41: (_R, '"no sorry reaches main", the main, not the pin')},
    'relay:data/b714_closing.txt': {90: (_R, 'the v0.1.0 release "T1+T2 compiled 0-sorry, T3 pinned", names the pinned sorry')},
}
HAND = dict(((k, p, n), v) for k, tab in (('i', _HI), ('ii', _HII), ('iii', _HIII)) for p, rows in tab.items() for n, v in rows.items())


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def first_commit_time(path):
    out = git(ROOT, 'log', '--diff-filter=A', '--format=%ct', '--', path).split()
    return int(out[-1]) if out else None


def blame_time(path, line):
    out = git(PP, 'blame', '--porcelain', '-L', '%d,%d' % (line, line), '--', path)
    m = re.search(r'(?m)^author-time (\d+)', out)
    return int(m.group(1)) if m else None


def utc(t=None):
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(t) if t else time.gmtime())


def hits_in(repo, paths, pair):
    args = ['grep', '-n', '-I', '-i', '-F']
    first = True
    for n in pair:
        if not first:
            args.append('--and')
        args += ['-e', n]
        first = False
    out = git(repo, *(args + ['--'] + paths))
    res = []
    for l in out.split(NL):
        m = re.match(r'^([^:]+):(\d+):(.*)$', l)
        if m:
            res.append((m.group(1), int(m.group(2)), m.group(3)))
    return res


def readme_hits(pair):
    """SIDE-lv-conservation's README at main and at v0.10.0: a paragraph (blank-line block) carrying every needle."""
    res = []
    for ref in ('HEAD', 'v0.10.0'):
        t = git(LV, 'show', '%s:README.md' % ref)
        ln, block, start = 0, [], 1
        for i, l in enumerate(t.split(NL) + [''], 1):
            if l.strip():
                if not block:
                    start = i
                block.append(l)
            elif block:
                b = ' '.join(block)
                if all(n.lower() in b.lower() for n in pair):
                    res.append(('SIDE-lv-conservation:README.md@%s' % ref, start, b))
                block = []
    return res


def act_of(path):
    m = re.search(r'(?:^|/)(?:audit_)?b(\d{3})[_/]', path) or re.search(r'(?:^|/)_b(\d{3})/', path)
    return int(m.group(1)) if m else None


def grade(o, path, line, text, t_written, t_bound, before):
    if (o['key'], path, line) in HAND:
        g, why = HAND[(o['key'], path, line)]
        return g, 'HAND: ' + why
    if path.startswith('relay:') and COPY.search(path[len('relay:'):]):
        return 'COPY', 'screen: a copying or quoting bank'
    if o.get('other') and re.search(o['other'], text):
        return 'NOT THIS OBJECT', 'rule: ' + o['other'][:40]
    if re.search(o['right'], text):
        return 'READS RIGHT', 'rule: names the correction or restricts'
    if o.get('instance') and re.search(o['instance'], text):
        return 'READS RIGHT', 'rule: an instance where it holds'
    if before is None:
        return 'UNREAD', 'no date'
    return ('DATED', 'rule: written before the boundary') if before else ('READS WRONG', 'rule: written after the boundary')


def read(*a):
    t0 = time.time()
    rel_banks = [p for p in git(ROOT, 'ls-files', '--', 'data/').split(NL) if p and p not in SELF]
    L = ['%s -- (R332)(8): THE PROPAGATION READ UNDER STANDING CLAUSES v8 ROW (82), ITS OPENING RUN ON THREE OBJECTS (%s)' % (ACT, utc()), '',
         '### ROW (82) (relay data/standing_clauses_v8.txt): "When the record corrects a statement, every statement naming the same object is read,',
         '### and each that now reads wrong gets a dated note beside it; no line is rewritten."',
         '### READ: %s ; SIDE-lv-conservation README.md at HEAD and v0.10.0 (iii) ; the relay`s tracked banks under data/ (%d files, the act`s own ruling' % (
             ', '.join(LEDGERS), len(rel_banks)),
         '### and banks %s set aside as the question). GRADES: READS RIGHT ; READS WRONG ; DATED (written before the correction, carried as the' % ', '.join(SELF),
         '### record under the history clause, its note beneath) ; NOT THIS OBJECT (a name hit naming another object, graded nothing) ; COPY (a',
         '### copying or quoting bank, by the screen COPY printed below, graded where its source stands, no note).',
         '### THE COPY SCREEN: ' + COPY.pattern, '### MATCHER LINEAGE: ' + LINEAGE, '']
    J = []
    unread = 0
    for o in OBJECTS:
        tb = first_commit_time(o['boundary_bank'])
        L += ['## OBJECT (%s): %s' % (o['key'], o['what']),
              '  ITS NAMES, PRINTED BEFORE THE SEARCH: ' + ' ; '.join(' AND '.join('"%s"' % n for n in pr) for pr in o['names']),
              '  THE CORRECTION: %s ; the boundary %s (%s)' % (o['correction'], utc(tb) if tb else 'NONE', o['boundary_bank']),
              '  THE RULE: ' + o['rule']]
        seen = {}
        for pr in o['names']:
            for path, ln, text in hits_in(PP, LEDGERS, pr):
                seen.setdefault(('PLACE-papers', path, ln), text)
            for path, ln, text in hits_in(ROOT, ['data/'], pr):
                if path not in SELF:
                    seen.setdefault(('relay', path, ln), text)
            if o['key'] == 'iii':
                for path, ln, text in readme_hits(pr):
                    seen.setdefault(('kernel', path, ln), text)
        counts = {}
        for (repo, path, ln), text in sorted(seen.items(), key=lambda kv: (kv[0][0] != 'PLACE-papers', kv[0][1], kv[0][2])):
            if repo == 'PLACE-papers':
                tw = blame_time(path, ln)
                before = (tw < tb) if (tw and tb) else None
                when = utc(tw) if tw else '?'
            elif repo == 'kernel':
                tw, before, when = None, None, 'the README'
            else:
                a_ = act_of(path)
                if a_ is not None and a_ != o['boundary_act']:
                    before, when, tw = a_ < o['boundary_act'], 'b%03d' % a_, None
                else:
                    tw = first_commit_time(path)
                    before = (tw < tb) if (tw and tb) else None
                    when = utc(tw) if tw else '?'
            g, why = grade(o, '%s:%s' % (repo, path), ln, text, tw, tb, before)
            if repo == 'kernel' and g in ('READS WRONG', 'DATED'):
                g, why = g + ', LISTED FOR THE RELEASE SITTING', why + '; a public README, not noted there'
            if g == 'UNREAD':
                unread += 1
            counts[g] = counts.get(g, 0) + 1
            ex = re.sub(r'\s+', ' ', text).strip()
            J.append(dict(object=o['key'], repo=repo, path=path, line=ln, written=when, grade=g, why=why, text=ex[:400]))
            L.append('  %-12s %s:%s :%d (%s) -- %s [%s] | %s' % (g, repo, path, ln, when, g, why, ex[:230]))
        L += ['  OBJECT (%s): HITS %d ; %s' % (o['key'], len(seen), ' ; '.join('%s %d' % kv for kv in sorted(counts.items()))), '']
    tot = dict((g, sum(1 for x in J if x['grade'] == g)) for g in sorted(set(x['grade'] for x in J)))
    notes = sum(1 for x in J if x['grade'] in ('READS WRONG', 'DATED'))
    L += ['### ### **THE PROPAGATION READ: OBJECTS 3 ; HITS %d ; %s ; NOTES TO WRITE %d ; UNREAD %d ; %d s.**' % (
        len(J), ' ; '.join('%s %d' % kv for kv in tot.items()), notes, unread, int(time.time() - t0))]
    outs = [x[4:] for x in a if x.startswith('out=')]
    if outs:                                          # ### a dry run's full text to a scratch file, its count lines alone printed
        open(outs[0], 'w', encoding='utf-8').write(NL.join(L) + NL)
        print(NL.join(l for l in L if l.startswith('  OBJECT') or l.startswith('### ###') or l.startswith('  READS WRONG') or l.startswith('  DATED')))
    else:
        print(NL.join(L))
    if unread:
        print('### UNREAD %d -- NOTHING BANKED' % unread)
        return
    if 'dry' in a:
        return
    for name, data in (('%s_propagation.txt' % ACT, NL.join(L) + NL), ('%s_propagation.json' % ACT, json.dumps(J, indent=1, ensure_ascii=False) + NL)):
        p = os.path.join(D, name)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print('written data/%s_propagation.txt, .json' % ACT)


NOTE_TITLE = '## The propagation read under standing clauses v8 row (82): dated notes on three corrected objects'
CORRECTS = {'i': 'the value clause is refuted at -40: n0(-40) = 100 with b = -1/2 (relay data/b720_coeffs.txt :57; FINDINGS :11072); -2 stands '
                 'at the fields where it held, not as the law',
            'ii': 'T-COUNT at Q0 is derived on the record (b685-b687, written and certified in balls, not compiled): relay data/b718_count_read.txt '
                  ':19-:27, data/b687_p3_status.txt :8',
            'iii': 'SIDE-lv-conservation at v0.10.0 builds with one sorry: T3_perClass_to_combinations depends on sorryAx (relay '
                   'data/b721_rebuild.txt :22, :54)'}


QUOTE_AT = {'i': [r'b\(n0\) = [-−]2|b\(n₀\)|b\(n_0\)', r'coefficient law'], 'ii': [r'T-COUNT[^.;]{0,40}assum', r'T-COUNT'],
            'iii': [r'0[- ]sorr|no sorr|sorry[- ]free|free of sorry|zero sorry', r'lv-conservation']}


def _quote(o, x):
    """the quotation around the first needle of the object's names, read from the line itself (the bank's excerpt stops at 400 characters);
    markdown's marks escaped, the relay's backtick apostrophe printed as one, nothing dropped."""
    src = os.path.join(PP, x['path']) if x['repo'] == 'PLACE-papers' else os.path.join(ROOT, x['path'])
    text = re.sub(r'\s+', ' ', open(src, encoding='utf-8').read().split(NL)[x['line'] - 1]).strip()
    m = None
    for pat in QUOTE_AT[o['key']]:                    # ### the most specific needle first: the claim, then the name
        m = m or re.search(pat, text, re.I)
    at = m.start() if m else 0
    s, e = max(0, at - 70), at + 110
    q = text[s:e].strip().replace('“', '"').replace('”', '"')
    q = q.replace('`', '’') if x['repo'] == 'relay' else q.replace('`', '')   # ### a relay bank`s backtick is its apostrophe; a ledger`s is code marking
    q = q.replace('*', '\\*').replace('_', '\\_')
    return ('…' if s > 0 else '') + q + ('…' if e < len(text) else '')


def notes(*a):
    """composes one note per READS WRONG and DATED hit of data/b722_propagation.json (a kernel README's hit listed for the release sitting,
    not noted), and lands them as one block appended to FINDINGS through b698's guarded landing; no line is rewritten. `dry` prints."""
    import b722_record as REC
    J = json.load(open(os.path.join(D, '%s_propagation.json' % ACT), encoding='utf-8'))
    obj = dict((o['key'], o) for o in OBJECTS)
    noted = [x for x in J if x['grade'] in ('READS WRONG', 'DATED')]
    listed = [x for x in J if 'RELEASE SITTING' in x['grade']]
    L = [NOTE_TITLE, '',
         'Row (82) of the standing clauses v8 (relay data/standing_clauses_v8.txt), its opening run at b722 under `(R332)`(8): when the record '
         'corrects a statement, every statement naming the same object is read, and each that now reads wrong gets a dated note beside it; no '
         'line is rewritten. The read (relay data/b722_propagation.txt) graded %d hits over REGISTRY, OPEN_TRAILS, SPIRAL_MAP, FINDINGS, the '
         'keystones and the relay`s banks; the %d below are its READS WRONG and DATED, each note dated 2026-10-28 and pointing to the line it '
         'corrects; DATED marks a line true or carried when written and overtaken since.' % (len(J), len(noted)), '']
    for k in ('i', 'ii', 'iii'):
        xs = [x for x in noted if x['object'] == k]
        if not xs:
            continue
        L += ['**Object (%s), %s.** The correction: %s.' % (k, obj[k]['what'], CORRECTS[k]), '']
        for x in xs:
            where = ('%s :%d' % (x['path'], x['line'])) if x['repo'] == 'PLACE-papers' else ('relay %s :%d' % (x['path'], x['line']))
            L.append('- **%s** (written %s; %s, noted 2026-10-28): "%s" -- %s.' % (
                where, x['written'], x['grade'], _quote(obj[k], x),
                'overtaken by the correction above' if x['grade'] == 'DATED' else 'reads wrong against the correction above'))
        L.append('')
    L += ['**Listed for the release sitting** (a public README or deposit description, not noted here): %s.' % (
        '; '.join('%s :%d (%s)' % (x['path'], x['line'], x['grade']) for x in listed) or 'none'), '',
          '*Filed at b722 under `(R332)`(8): generated by relay `tools/b722_propagation.py` notes from data/b722_propagation.json, written whole '
          'at b722; no line of any ledger is rewritten.*']
    text = NL + NL.join(L) + NL
    REC.land([('FINDINGS.md', NOTE_TITLE, text)], '%s_propagation_landing.json' % ACT, 'propagation', entry=None, dry='dry' in a)
    print('  NOTES %d ; LISTED %d' % (len(noted), len(listed)))


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(read=read, notes=notes).get(route)
    if fn is None:
        sys.exit('usage: b722_propagation.py read [dry]')
    fn(*sys.argv[2:])
