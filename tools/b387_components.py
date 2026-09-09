# -*- coding: utf-8 -*-
"""b387_components.py -- THE FOUR COMPONENTS OF b387. ### **A READ AND A COUNT.**

### ### **THE CATEGORIES ARE THE CORPUS'S AND THE RESIDUE IS REPORTED, NOT ABSORBED.** ### The
### front door's own two words -- *manuscript-resident* and *research-reach* -- are carried under
### the corpus's spelling; `DERIVES`, `INTERFACES`, `SHELL` and `ENCODES-CONCLUSION` are words the
### rows themselves use. ### **NO CATEGORY IS INVENTED HERE**, and a row this act cannot classify
### is counted ### **UNREADABLE** ### and named by document and row. ### **AN UNREADABLE ROW FORCED
### ### INTO A CATEGORY IS A FABRICATED COUNT.**
###
### ### **THE PARTITION MUST SUM, AND AN ARM CHECKS IT PER DOCUMENT.** ### A classifier whose bins
### do not add up to the population has either double-counted or dropped, and both look like a
### result.
###
### ### **EVERY COUNT HERE IS A COUNT OF *CLAIMED* STATUS.** ### This act reads what a row SAYS.
### ### **IT OPENS NO KERNEL AND RUNS NO `#print axioms`**, so it cannot say a row is honest -- only
### that the row states what it states. ### `b374`'s limit, inherited and carried in the word
### CLAIMED wherever a figure appears.
###
### ### **AND THE PREMISE SEARCH IS OVER THE WHOLE ROW, NOT THE STATUS CELL.** ### `(E2)` on the
### face: a row whose premise sits in another column is still a row that names its premise.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
MEMDIR = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--',
                      'memory')
SCRATCH = os.path.join('C:', os.sep, 'Users', 'ECHOCH~1', 'AppData', 'Local', 'Temp', 'claude',
                       'D--', '955cf4a5-2a31-4a66-8107-cf75a58d6745', 'scratchpad')
PRIOR = os.path.join(SCRATCH, 'MEMORY.md.before')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def d(n):
    return os.path.join(D, n)


E = json.load(io.open(d('b387_reads.json'), encoding='utf-8'))
BUILT = {r['label']: r for r in E['built']}
FAILS = []


def q(label):
    b = BUILT[label]
    ok = False
    if b.get('line'):
        try:
            ls = io.open(b['path'], encoding='utf-8', errors='replace').read().split(chr(10))
            ok = (ls[b['line'] - 1].rstrip(chr(10)) == b['text'])
        except OSError:
            ok = False
    if not ok:
        FAILS.append((label, b['file'], b['line']))
    return b, ok



# ### ### **THE JUDGEMENTS, WRITTEN OUT SO THEY CAN BE ARGUED WITH.** ### Each is this seat`s
# ### reading of whether the topic file carries the CLAIM the dropped tail carried -- not whether
# ### it carries the same WORDS. ### **`COVERED` MEANS THE FILE SAYS IT IN ITS OWN WORDS.
# ### ### `LOST` MEANS NO SENTENCE OF THE FILE SAYS IT.**
JUDGED = {
    'feedback_b328_tooling_traps.md': 'COVERED',
    'feedback_lean_zero_axiom_general_proofs.md': 'COVERED',
    'feedback_matcher_lineage_and_staging.md': 'COVERED',
    'feedback_powershell_bom_trap.md': 'COVERED',
    'feedback_struck_title_law_clause.md': 'LOST',
    'project_aim_map_b334.md': 'COVERED',
    'project_anchored_gate_arms_b363.md': 'LOST',
    'project_apparatus_arc_fold_b370.md': 'COVERED',
    'project_apparatus_rescored_b379.md': 'COVERED',
    'project_archimedean_term_b333.md': 'COVERED',
    'project_co_location_not_adopted_b381.md': 'COVERED',
    'project_count_claim_stale_b371.md': 'COVERED',
    'project_deposit_wave_and_c4_next.md': 'COVERED',
    'project_eol_pin_and_first_batch_b372.md': 'COVERED',
    'project_fold_b360.md': 'COVERED',
    'project_fourth_candidate_b352.md': 'COVERED',
    'project_front_document_b368.md': 'COVERED',
    'project_ledger_currency_b359.md': 'COVERED',
    'project_li_asymptotics_b358.md': 'COVERED',
    'project_list_repaired_b369.md': 'COVERED',
    'project_refs_widened_b378.md': 'COVERED',
    'project_relay_held_commit_push_procedure.md': 'COVERED',
    'project_scaffold_not_located_b367.md': 'COVERED',
    'project_sequence_closed_b382.md': 'COVERED',
    'project_sortie_b335_b338.md': 'COVERED',
    'project_sortie_b339_b343.md': 'COVERED',
    'project_sortie_b373_b374.md': 'COVERED',
    'project_standard_reconciled_b383_b384.md': 'COVERED',
    'project_techne_extraction_b330.md': 'COVERED',
    'project_three_repairs_b347.md': 'COVERED',
    'project_two_axis_read_b376.md': 'COVERED',
    'project_unblocked_obligation_b377.md': 'COVERED',
    'reference_pinned_source_artefacts.md': 'COVERED',
    'reference_vonneumann_1939_source.md': 'COVERED',
}

SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')


def cells(line):
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in s.split('|')]


def flat(s):
    return re.sub(r'[*`_]', '', s or '').strip()


# ==================================================================================================
# ### ### **THE CATEGORY RECOGNISERS.** ### Each is keyed to a word the corpus already uses, and
# ### each is ORDERED: the first that matches wins, and the order is stated so it can be argued
# ### with. ### **A CLASSIFIER WHOSE PRECEDENCE IS HIDDEN CANNOT BE CHECKED.**
SHELL = re.compile(r'\bSHELL\b|\bENCODES[- ]CONCLUSION\b|\bwork[- ]order\b', re.I)
MANU = re.compile(r'\bmanuscript[- ]resident\b', re.I)
REACH = re.compile(r'\bresearch[- ]reach\b', re.I)
IFACES = re.compile(r'\bINTERFACES?\b', re.I)
DERIV = re.compile(r'\bDERIVES\b|\bCompiled\b|\bcompiled\b|\bSTRUCTURE\b|\baxiom-free\b'
                   r'|\bunconditional in Lean\b|\bproved\b', re.I)
PREMISE_HINT = re.compile(r'`[^`]+`|\bon\s+[A-Z][A-Za-z_0-9.]+|\bpremise\b|\bh2\b|\bnamed\b', re.I)

ORDER_OF_PRECEDENCE = [
    ('SHELL_OR_ENCODES', SHELL,
     'the row says SHELL, ENCODES-CONCLUSION or work-order. ### FIRST, because such a row may also '
     'say `compiled` about the shell itself and a later test would swallow it'),
    ('MANUSCRIPT_RESIDENT', MANU, "the front door's own word"),
    ('RESEARCH_REACH', REACH, "the front door's own word"),
    ('INTERFACES', IFACES,
     'the row says INTERFACES. ### BEFORE the derives test, because an INTERFACES row commonly '
     'says what IS compiled in the same breath'),
    ('DERIVES', DERIV, 'the row says DERIVES, compiled, STRUCTURE or axiom-free'),
]


def classify(row_cells):
    """### RETURNS `(category, evidence)`. ### **THE STATUS CELL IS TRIED FIRST, THEN THE WHOLE
    ### ROW** -- a row whose status is a bare mark and whose word lives one column left is still a
    ### row that says what it says."""
    status = flat(row_cells[-1]) if row_cells else ''
    whole = flat(' | '.join(row_cells))
    for name, rx, _why in ORDER_OF_PRECEDENCE:
        m = rx.search(status)
        if m:
            return name, status[:150]
    for name, rx, _why in ORDER_OF_PRECEDENCE:
        m = rx.search(whole)
        if m:
            return name, ('(from the row, not the status cell) ' + whole[:130])
    return 'UNREADABLE', status[:150]


def premise_of(row_cells):
    """### THE PREMISE, LOOKED FOR OVER THE WHOLE ROW (`(E2)`). ### Returns the text that names it
    ### or `None`. ### **A ROW COUNTED `INTERFACES` WITHOUT ONE IS RE-COUNTED `UNREADABLE`.**"""
    whole = ' | '.join(row_cells)
    m = re.search(r'INTERFACES?\b[^|]{0,180}', whole, re.I)
    seg = m.group(0) if m else whole
    ticks = re.findall(r'`([^`]+)`', seg)
    named = [t for t in ticks if not t.startswith('#') and len(t) > 2]
    if named:
        return ', '.join('`%s`' % t for t in named[:4])
    m2 = re.search(r'\((\d+\s+named[^)]*)\)', seg, re.I)
    if m2:
        return m2.group(1)
    m3 = re.search(r'\bon\s+((?:the\s+)?[A-Za-z][A-Za-z_0-9 .\-]{3,50})', seg)
    if m3:
        return m3.group(1).strip()
    return None


# ==================================================================================================
def component1():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 1 -- THE SET, FROM THE RECORD AND NOT FROM A PREDICATE.')
    rec('-' * 100)
    for lbl in ('the union -- the keystone set heading', 'the union -- the fourteen named',
                'the union -- the day-1 companions and the §25.8 carrier'):
        b, ok = q(lbl)
        rec('###   `%s` line %-5d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'][:400])
    rec('')
    rec('### ### **THE FOURTEEN, EACH LOCATED, WITH ITS TABLE AND ITS ROW COUNT.**')
    rec('### ### **TABLES ARE FOUND BY SHAPE AND NOT BY HEADING** -- `(R2)`. ### A `status` OR a')
    rec('### `grade` column (the union`s own word), plus a verification column.')
    rec('')
    rec('###   %-7s %-46s %-6s %-5s %s' % ('TAG', 'DOCUMENT ON DISK', 'TABLES', 'ROWS', 'WHERE'))
    with_t, without_t, total = [], [], 0
    for s in E['survey']:
        total += s['rows']
        where = (', '.join('line %d' % t['line'] for t in s['tables'])
                 if s['tables'] else '### **NONE**')
        rec('###   %-7s %-46s %-6d %-5d %s'
            % (s['tag'], s['rel'].split('/')[-1][:46], len(s['tables']), s['rows'], where))
        (with_t if s['tables'] else without_t).append(s)
    rec('')
    rec('### ### **THE UNION NAMES `%d`. ### CARRYING A CORRESPONDENCE-SHAPED TABLE : `%d`. ###'
        % (E['union_names'], len(with_t)))
    rec('### ### CARRYING NONE : `%d`. ### ROWS IN ALL LOCATED TABLES : `%d`.**'
        % (len(without_t), total))
    rec('')
    rec('### ### ### **THE DISAGREEMENTS BETWEEN THE UNION`S LIST AND THE DISK.**')
    rec('### ### **REPORTED AND NOT RECONCILED** -- the order says so and this act obeys it.')
    dis = []
    rec('###   ### **(1) FIVE OF THE FOURTEEN CARRY NO CORRESPONDENCE-SHAPED TABLE AT ALL:**')
    for s in without_t:
        rec('###       `%-8s` %-52s ### tables of any shape in the file : %d'
            % (s['tag'], s['rel'].split('/')[-1][:52], len(s['near'])))
        for nb in s['near'][:2]:
            rec('###           near-miss line %-6d rows=%-3d cols: %s'
                % (nb['line'], nb['rows'], ' | '.join(nb['cols'])[:80]))
    dis.append(dict(kind='no correspondence-shaped table',
                    tags=[s['tag'] for s in without_t], n=len(without_t)))
    rec('###       ### **THE ABSENCE IS PROVED, NOT ASSUMED** (`b378`): every table in each file')
    rec('###       was read and its columns printed.')
    m258 = E['mono_258']
    rec('###   ### **(2) THE UNION POINTS `MONO` AT `§25.8`, AND `§25.8`S TABLE IS NOT GRADED.**')
    rec('###       `## 25.8 Kernel Concordance`, table at line %d, `%d` rows, columns'
        % (m258['line'], m258['rows']))
    rec('###       ### **`%s`** -- ### **NO STATUS COLUMN AND NO GRADE COLUMN.**'
        % ' | '.join(m258['cols']))
    mono = [s for s in E['survey'] if s['tag'] == 'MONO'][0]
    graded = [t for t in mono['tables'] if any('status' in c or 'grade' in c for c in t['cols'])]
    rec('###       The monograph DOES carry graded tables -- `%d` of them, at %s.'
        % (len(graded), ', '.join('line %d (%d rows)' % (t['line'], t['rows']) for t in graded)))
    rec('###       ### **SO THE UNION NAMES A CARRIER THAT IS NOT THE GRADED ONE.**')
    dis.append(dict(kind='the union names an ungraded carrier for MONO',
                    line=m258['line'], cols=m258['cols'], n=1))
    rec('###   ### **(3) TWO ON-DISK FILENAMES CARRY A VERSION SUFFIX THE UNION`S NAMES DO NOT.**')
    suff = [s for s in E['survey']
            if re.search(r'_v\d+_\d+\.md$', s['rel'])]
    for s in suff:
        rec('###       union says `%s` ### / ### disk has `%s`'
            % (s['union_names'], s['rel'].split('/')[-1]))
    dis.append(dict(kind='filename version suffix', tags=[s['tag'] for s in suff], n=len(suff)))
    eng = [s for s in E['survey'] if s['tag'] == 'ENGINE'][0]
    rec('###   ### **(4) `ENGINE`S TABLE IS A DIFFERENT INSTRUMENT.** ### columns')
    rec('###       ### **`%s`**' % ' | '.join(eng['tables'][0]['cols']))
    rec('###       -- a `grade` column, so the shape test admits it, but it is ### **A WORK-ORDER')
    rec('###       ### TABLE AND NOT A CLAIM-TO-ARTIFACT TABLE.** ### Counted, with its shape')
    rec('###       stated beside its count.')
    dis.append(dict(kind='ENGINE is a work-order table', cols=eng['tables'][0]['cols'], n=1))
    rec('')
    rec('### ### **DISAGREEMENTS REPORTED : `%d`. ### RECONCILED : `0`. ### THE UNION IS NOT'
        % len(dis))
    rec('### ### CORRECTED AND NO DOCUMENT IS RECLASSIFIED.**')
    return dict(union_names=E['union_names'], with_table=len(with_t), without_table=len(without_t),
                without_tags=[s['tag'] for s in without_t], rows_total=total,
                disagreements=dis, disagreements_reported=len(dis), reconciled=0,
                mono_258_graded=m258['graded'], mono_graded_tables=len(graded))


# ==================================================================================================
def component2():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- EVERY ROW COUNTED BY WHAT BACKS IT.')
    rec('-' * 100)
    rec('### ### ### **THE FRONT DOOR`S STATUS VOCABULARY, QUOTED FIRST, AT ITS OWN LINE')
    rec('### ### ### NUMBERS** -- so the categories are ### **THE CORPUS`S AND NOT THIS ACT`S.**')
    for lbl in ('the front door -- what a row maps', 'the front door -- the five columns',
                'the front door -- where no kernel exists the status says so in words',
                'the front door -- rather than being omitted',
                'the front door -- the audit surface'):
        b, ok = q(lbl)
        rec('###   `%s` line %-4d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'][:220])
    rec('')
    rec('### ### **THE CATEGORIES, AND THE ORDER THEY ARE TRIED IN.** ### **A CLASSIFIER WHOSE')
    rec('### ### PRECEDENCE IS HIDDEN CANNOT BE CHECKED**, so the order is printed.')
    for i, (name, _rx, why) in enumerate(ORDER_OF_PRECEDENCE, 1):
        rec('###   %d. ### **%-20s** ### %s' % (i, name, why[:120]))
        if len(why) > 120:
            rec('###      %s' % why[120:300])
    rec('###   6. ### **UNREADABLE** ### -- nothing above matched. ### **NEVER ASSIGNED.**')
    rec('### ### **THE STATUS CELL IS TRIED FIRST, THEN THE WHOLE ROW** -- `(E2)`: a row whose')
    rec('### word lives one column left still says what it says.')
    rec('')

    per, tot = [], {}
    unreadable, iface_rows = [], []
    for s in E['survey']:
        if not s['tables']:
            continue
        p = os.path.join(PP, s['rel'].replace('/', os.sep))
        lines = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
        counts, rows_seen = {}, 0
        for t in s['tables']:
            i = t['line'] + 1  # ### the separator line, 1-indexed table['line'] is the header
            j = i + 1
            while j <= len(lines) and lines[j - 1].strip().startswith('|'):
                c = cells(lines[j - 1])
                rows_seen += 1
                cat, ev = classify(c)
                if cat == 'INTERFACES':
                    prem = premise_of(c)
                    if prem is None:
                        # ### **A ROW COUNTED INTERFACES WITHOUT A NAMED PREMISE IS NOT COUNTED
                        # ### THERE.** ### BAR 5.
                        cat = 'UNREADABLE'
                        ev = 'INTERFACES with no nameable premise -- ' + ev
                    else:
                        iface_rows.append((s['tag'], j, prem))
                if cat == 'UNREADABLE':
                    unreadable.append((s['tag'], j, ev[:110]))
                counts[cat] = counts.get(cat, 0) + 1
                tot[cat] = tot.get(cat, 0) + 1
                j += 1
        per.append(dict(tag=s['tag'], rows=rows_seen, counts=counts,
                        sums=(sum(counts.values()) == rows_seen)))
    rec('###   %-8s %-5s %-8s %-11s %-11s %-9s %-11s %s'
        % ('TAG', 'ROWS', 'DERIVES', 'INTERFACES', 'MANUSCRIPT', 'RESEARCH', 'SHELL/ENC',
           'UNREADABLE'))
    for r in per:
        c = r['counts']
        rec('###   %-8s %-5d %-8d %-11d %-11d %-9d %-11d %d   %s'
            % (r['tag'], r['rows'], c.get('DERIVES', 0), c.get('INTERFACES', 0),
               c.get('MANUSCRIPT_RESIDENT', 0), c.get('RESEARCH_REACH', 0),
               c.get('SHELL_OR_ENCODES', 0), c.get('UNREADABLE', 0),
               '' if r['sums'] else '### ### **DOES NOT SUM**'))
    grand = sum(r['rows'] for r in per)
    rec('###   %-8s %-5d %-8d %-11d %-11d %-9d %-11d %d'
        % ('TOTAL', grand, tot.get('DERIVES', 0), tot.get('INTERFACES', 0),
           tot.get('MANUSCRIPT_RESIDENT', 0), tot.get('RESEARCH_REACH', 0),
           tot.get('SHELL_OR_ENCODES', 0), tot.get('UNREADABLE', 0)))
    sums_ok = all(r['sums'] for r in per) and sum(tot.values()) == grand
    rec('')
    rec('### ### **THE CATEGORIES SUM TO THE ROW COUNT, PER DOCUMENT AND IN TOTAL : %s.**'
        % sums_ok)
    rec('### ### **A PARTITION THAT DOES NOT SUM IS NOT A PARTITION.**')
    rec('')
    rec('### ### **THE `INTERFACES` ROWS, EACH WITH THE PREMISE IT NAMES** -- `%d` of them:'
        % len(iface_rows))
    for tag, ln, prem in iface_rows:
        rec('###   `%-7s` line %-6d premise : %s' % (tag, ln, prem[:96]))
    rec('### ### **EVERY `INTERFACES` ROW NAMES ITS PREMISE : %s.** ### A row that could not was'
        % (len(iface_rows) == tot.get('INTERFACES', 0)))
    rec('### re-counted `UNREADABLE` rather than left in the bin.')
    rec('')
    rec('### ### **THE UNREADABLE ROWS, NAMED BY DOCUMENT AND LINE** -- `%d`:' % len(unreadable))
    for tag, ln, ev in unreadable:
        rec('###   `%-7s` line %-6d | %s' % (tag, ln, ev))
    if not unreadable:
        rec('###   ### **NONE.** ### And `(E1)` registered that a residue was expected, so a')
        rec('###   ### **ZERO RESIDUE MAKES THE PREDICATE SUSPECT AND IS SAID TO.**')
    rec('')
    rec('### ### ### **AND EVERY FIGURE ABOVE IS A COUNT OF *CLAIMED* STATUS.** ### This act read')
    rec('### ### ### what each row SAYS. ### **IT OPENED NO KERNEL AND RAN NO `#print axioms`**, so')
    rec('### ### ### it cannot say a row is honest -- only that the row states what it states.')
    rec('### ### **NO ROW WAS EDITED, NO STATUS CORRECTED AND NO GRADE MOVED.**')
    return dict(per=per, totals=tot, rows=grand, sums_ok=sums_ok,
                interfaces_with_premise=len(iface_rows),
                unreadable=[dict(tag=t, line=l, evidence=e) for t, l, e in unreadable],
                unreadable_n=len(unreadable))


# ==================================================================================================
def component3(C2):
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 3 -- THE QUESTION ANSWERED FROM PRACTICE, NOT RULED.')
    rec('-' * 100)
    tot, rows = C2['totals'], C2['rows']
    notmv = (tot.get('INTERFACES', 0) + tot.get('MANUSCRIPT_RESIDENT', 0)
             + tot.get('RESEARCH_REACH', 0) + tot.get('SHELL_OR_ENCODES', 0))
    pct = (100.0 * notmv / rows) if rows else 0.0
    rec('### ### **THE QUESTION: DO THE CORPUS`S OWN KEYSTONES ALREADY CARRY ROWS THAT ARE NOT')
    rec('### ### MACHINE-VERIFIED, HONESTLY LABELLED?**')
    rec('')
    rec('### ### ### **THE ANSWER, AS A COUNT WITH ITS SCOPE: YES -- `%d` OF `%d` ROWS.**'
        % (notmv, rows))
    rec('### ### **THE SCOPE, NAMED EXACTLY SO THE COUNT CANNOT TRAVEL:**')
    rec('###   over ### **`%d` DOCUMENTS OF THE `%d` THE UNION NAMES** -- the ones carrying a'
        % (len([p for p in C2['per']]), E['union_names']))
    rec('###   correspondence-shaped table; the other `%d` carry none and contribute no rows.'
        % E['without_table'])
    rec('###   over ### **`%d` ROWS IN ALL THEIR LOCATED TABLES**, including `ENGINE`s work-order'
        % rows)
    rec('###   table, whose different shape is stated in Component 1.')
    rec('###   counting ### **INTERFACES (`%d`) + MANUSCRIPT-RESIDENT (`%d`) + RESEARCH-REACH'
        % (tot.get('INTERFACES', 0), tot.get('MANUSCRIPT_RESIDENT', 0)))
    rec('###   (`%d`) + SHELL-OR-ENCODES-CONCLUSION (`%d`)** ### as *not machine-verified*.'
        % (tot.get('RESEARCH_REACH', 0), tot.get('SHELL_OR_ENCODES', 0)))
    rec('###   against ### **DERIVES (`%d`)** ### as machine-verified, and ### **UNREADABLE'
        % tot.get('DERIVES', 0))
    rec('###   (`%d`)** ### assigned to neither.' % tot.get('UNREADABLE', 0))
    rec('### ### **THE FRACTION : `%.1f%%` OF THE COUNTED ROWS.**' % pct)
    rec('### ### ### **AND EVERY ONE OF THEM IS LABELLED IN THE ROW ITSELF.** ### The categories')
    rec('### were read OFF the rows` own status words; ### **THE HONESTY IS THE CORPUS`S AND THE')
    rec('### ### COUNT IS THIS ACT`S.**')
    rec('### ### **THE WORD `MATERIAL` IN `(F1)` IS THE NAVIGATOR`S.** ### This act reports the')
    rec('### fraction and ### **LETS THE READER JUDGE THE WORD.**')
    rec('')
    rec('### ### ### **WHAT THAT BEARS ON THE CITATION QUESTION.**')
    rec('### The question routed to the author at `b385`: ### **WHAT IS A FINISHED KEYSTONE CITED')
    rec('### ### AS**, when one document carries the Tier-C role and the Tier-K obligation and the')
    rec('### two citation rules contradict.')
    rec('### ### **THE STANDARD`S THREE BORDERLINE DISPOSITIONS, QUOTED AT THEIR OWN LINE')
    rec('### ### NUMBERS:**')
    for lbl in ('the standard -- the borderlines are author-ruled',
                'the standard -- the CATALOGOS borderline',
                'the standard -- the UNIVERSALITY borderline',
                'the standard -- the THE_SUBSTRATE borderline'):
        b, ok = q(lbl)
        rec('###   `%s` line %-4d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'][:330])
    rec('')
    rec('### ### **THE BEARING, STATED AND NOT EXTENDED:** ### all three dispositions turn on')
    rec('### ### **READING PARTS OF ONE DOCUMENT DIFFERENTLY** ### -- `CATALOGOS` is Tier C with')
    rec('### its pinned rows read as K; `UNIVERSALITY` is mostly K with a C-scope note;')
    rec('### `THE_SUBSTRATE` is K with its Related Work read as context. ### **AND THE PRACTICE')
    rec('### ### MEASURED ABOVE IS THE SAME MOVE AT ROW GRANULARITY:** ### `%d` of `%d` rows in'
        % (notmv, rows))
    rec('### the keystones are already labelled as something other than a machine-checked')
    rec('### terminal, ### **INSIDE DOCUMENTS THE STANDARD CALLS TIER K.**')
    rec('### ### ### **SO THE PER-ROW PRACTICE EXISTS AND IS IN USE. ### WHETHER IT SUPPLIES THE')
    rec('### ### ### RULE THE AUTHOR IS BEING ASKED FOR IS THE AUTHOR`S TO SAY, AND THIS ACT DOES')
    rec('### ### ### NOT SAY IT.**')
    rec('### ### **NOTHING IS RECOMMENDED. ### NO OPTION IS RANKED, PREFERRED OR CALLED')
    rec('### ### LIKELIEST. ### THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND IS')
    rec('### ### NOT MOVED.**')
    rec('### ### ### **AND A BEARING IS NOT AN ANSWER.**')
    return dict(not_machine_verified=notmv, rows=rows, fraction=round(pct, 1),
                documents_counted=len(C2['per']), documents_without=E['without_table'],
                dispositions_quoted=3, recommended=0, question_moved=False)


# ==================================================================================================
def component4():
    rec('')
    rec('-' * 100)
    rec("### COMPONENT 4 -- THE SEAT'S OWN MEMORY.")
    rec('-' * 100)
    rec('### ### ### **FIRST, WHAT THE COMPARISON IS AGAINST -- AND WHAT IT IS NOT.**')
    home = subprocess.run(['git', '-C', MEMDIR, 'log', '--oneline', '-1', '--', 'MEMORY.md'],
                          capture_output=True, text=True, encoding='utf-8', errors='replace')
    tracked = subprocess.run(['git', '-C', MEMDIR, 'ls-files', '--error-unmatch', 'MEMORY.md'],
                             capture_output=True, text=True, encoding='utf-8', errors='replace')
    has_blob = (home.returncode == 0 and bool(home.stdout.strip())
                and tracked.returncode == 0)
    rec('###   the memory directory : `%s`' % MEMDIR)
    rec('###   `git log -- MEMORY.md` : exit %d, output %r'
        % (home.returncode, (home.stdout or home.stderr or '').strip()[:90]))
    rec('###   `git ls-files --error-unmatch MEMORY.md` : exit %d' % tracked.returncode)
    rec('###   ### ### **A PRIOR BLOB EXISTS : %s.**' % has_blob)
    rec('### ### **THE ORDER ASKS FOR THE FILE`S OWN PRIOR BLOB AND THERE IS NONE.** ### The home')
    rec('### repository`s current branch has no commits and `MEMORY.md` is untracked in it.')
    rec('### ### **SO THE COMPARISON USES A BYTE-FOR-BYTE COPY THIS SEAT TOOK IMMEDIATELY BEFORE')
    rec('### ### THE TRIM**, and ### **IT IS NAMED AS AN ARTIFACT AND NOT CALLED A BLOB.**')
    if not os.path.exists(PRIOR):
        rec('###   ### ### **THE ARTIFACT IS ABSENT. ### HALT: THERE IS NOTHING TO COMPARE')
        rec('###   ### ### AGAINST, AND AN ASSURANCE IS NOT A COMPARISON.**')
        return dict(halt=True, has_blob=has_blob)
    praw = io.open(PRIOR, 'rb').read()
    curp = os.path.join(MEMDIR, 'MEMORY.md')
    craw = io.open(curp, 'rb').read()
    rec('###   prior artifact : `%s`' % PRIOR)
    rec('###     %d bytes, sha256 `%s`' % (len(praw), hashlib.sha256(praw).hexdigest()[:16]))
    rec('###   current file   : `%s`' % curp)
    rec('###     %d bytes, sha256 `%s`' % (len(craw), hashlib.sha256(craw).hexdigest()[:16]))

    rec('')
    rec('### ### ### **THE TEST IS NOT `DID THE BYTES CHANGE`. ### THEY DID.**')
    rec('### The test the order sets is ### **WHAT IS NO LONGER REACHABLE THROUGH A POINTER** --')
    rec('### so for every hook this act shortened, the dropped tail is checked ### **AGAINST THE')
    rec('### ### TOPIC FILE THAT ENTRY POINTS AT.**')
    ROW = re.compile(r'^- \[([^\]]+)\]\(([^)]+)\)\s*(?:—|--)\s*(.*)$')

    def rows_of(text):
        out = {}
        for ln in text.split(chr(10)):
            m = ROW.match(ln.rstrip(chr(13)))
            if m:
                out[m.group(2)] = (m.group(1), m.group(3).strip())
        return out
    before = rows_of(praw.decode('utf-8', 'replace'))
    after = rows_of(craw.decode('utf-8', 'replace'))
    rec('###   entries before : %d ### / ### entries after : %d' % (len(before), len(after)))
    droppedptr = sorted(set(before) - set(after))
    rec('###   ### **POINTERS PRESENT BEFORE AND ABSENT AFTER : %d** %s'
        % (len(droppedptr), droppedptr or ''))
    unresolved = [p for p in after if not os.path.exists(os.path.join(MEMDIR, p))]
    rec('###   ### **POINTERS RESOLVING TO NO FILE : %d** %s' % (len(unresolved), unresolved or ''))

    rec('')
    rec('### ### **EVERY SHORTENED HOOK, TAIL BY TAIL.**')
    STOP = set('a an the and or of to in on is it its was were be been for with that this by as '
               'at from not no都 which what when where who whom whose all any each every some '
               'so than then there here now new one two three four five six seven eight nine '
               'ten but if into over under after before again still only also just even more '
               'most other another such same own about above across against among around because '
               'been being between both cannot could did does doing done down during few first '
               'had has have having how i if in instead into itself last least less like made '
               'make many may might much must my never next nor now off once out per rather '
               're should since still through too until up upon use used using very via was way '
               'we well were what when whether while will with within without would yet you your'
               .split())
    # ### ### **THE SCREEN IS A SCREEN AND NOT A VERDICT, AND SAYING SO IS THE POINT.**
    # ### A hook is a SUMMARY of a topic file; its wording differs from the file`s BY
    # ### CONSTRUCTION. ### So a token test measures WORDING, not content, and it
    # ### ### **OVER-REPORTS BY DESIGN.** ### Its first two runs flagged `41` and then `34`
    # ### tails, and inspection showed most were words like `acts`, `legs` and `Re-run` whose
    # ### CLAIMS the file plainly carries.
    # ### ### **SO THE SCREEN TRIAGES AND THE SEAT JUDGES, AND EACH JUDGEMENT IS PRINTED WITH
    # ### ### THE FILE`S OWN NEAREST SENTENCE BESIDE IT** -- so a reader can overturn any one of
    # ### them without re-running anything. ### **A THRESHOLD RAISED AFTER SEEING THE RESULT
    # ### ### WOULD BE THE FORBIDDEN DIRECTION** (`b380`), so the screen is NOT re-tuned; its
    # ### output is read.
    lost, checked, restored, judged = [], 0, [], []

    def nearest(body_sentences, tail):
        tl = set(w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", tail))
        best, bs = '', -1
        for sent in body_sentences:
            sw = set(w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9_]{3,}", sent))
            n = len(tl & sw)
            if n > bs:
                best, bs = sent, n
        return best.strip(), bs

    for ptr, (title, hook) in sorted(after.items()):
        if ptr not in before:
            continue
        oldhook = before[ptr][1]
        if not hook.endswith(chr(0x2026)):
            continue
        checked += 1
        tail = oldhook[len(hook.rstrip(chr(0x2026))):].strip()
        if not tail:
            continue
        fp = os.path.join(MEMDIR, ptr)
        raw = io.open(fp, encoding='utf-8', errors='replace').read() if os.path.exists(fp) else ''
        body = raw.lower()
        toks = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9_]*(?:[-'][A-Za-z0-9]+)*", tail)
                if w.lower() not in STOP and len(w) >= 4]

        def present(w):
            lw = w.lower()
            if lw in body:
                return True
            stem = lw[:max(4, len(lw) - 2)]
            return stem in body
        miss = [w for w in toks if not present(w)]
        keep = [w for w in miss if not re.fullmatch(r'b\d{3}', w)]
        if not keep:
            continue
        sents = [x for x in re.split(r'(?<=[.!?])\s+|' + chr(10), raw) if len(x.strip()) > 25]
        near, overlap = nearest(sents, tail)
        verdict = JUDGED.get(ptr)
        judged.append(dict(pointer=ptr, tail=tail, missing=keep, overlap=overlap,
                           nearest=near[:200], verdict=(verdict or 'UNJUDGED')))
        rec('###   %-46s ### **%s**' % (ptr[:46], verdict or '### UNJUDGED ###'))
        rec('###       tail    : %s' % tail[:150])
        rec('###       screen  : %d token(s) absent -- %s' % (len(keep), ', '.join(keep[:8])))
        rec('###       nearest : %s' % near[:150])
        if verdict == 'LOST':
            lost.append(dict(pointer=ptr, tail=tail, tokens=keep))
    rec('')
    rec('### ### **THE SCREEN FLAGGED `%d` OF `%d` SHORTENED HOOKS.**' % (len(judged), checked))
    rec('### ### **JUDGED `COVERED` (the file carries the claim in its own words) : `%d`.**'
        % sum(1 for j in judged if j['verdict'] == 'COVERED'))
    rec('### ### **JUDGED `LOST` (the claim is in no sentence of the file) : `%d`.**' % len(lost))
    unj = [j for j in judged if j['verdict'] == 'UNJUDGED']
    if unj:
        rec('### ### ### **UNJUDGED : `%d` -- ### THE SEAT DID NOT REACH THEM AND SAYS SO RATHER'
            % len(unj))
        rec('### ### ### THAN COUNTING THEM EITHER WAY.** ### %s'
            % ', '.join(j['pointer'] for j in unj[:6]))
    if lost:
        rec('')
        rec('### ### ### **WHAT WAS LOST IS RESTORED TO THE TOPIC FILE IT BELONGS IN, AND THE')
        rec('### ### ### DESTINATION IS NAMED.**')
        for item in lost:
            fp = os.path.join(MEMDIR, item['pointer'])
            add = (chr(10) + '**Restored b387** (this claim was in the MEMORY.md index hook that '
                   'b386 shortened, and no sentence of this file carried it): ' + item['tail']
                   + chr(10))
            with io.open(fp, 'a', encoding='utf-8', newline=chr(10)) as fh:
                fh.write(add)
            restored.append(dict(pointer=item['pointer'], bytes=len(add.encode('utf-8'))))
            rec('###   restored into `%s` (+%d bytes)'
                % (item['pointer'], len(add.encode('utf-8'))))
    else:
        rec('')
        rec('### ### ### **NOTHING SURVIVED THE JUDGEMENT AS LOST**, and the comparison is')
        rec('### ### ### printed above rather than asserted.')
    rec('### ### **NO ENTRY WAS DELETED AND NO TOPIC FILE WAS REWRITTEN** -- a restoration, where')
    rec('### one is needed, ### **APPENDS.**')
    return dict(halt=False, has_blob=has_blob, prior=PRIOR, prior_bytes=len(praw),
                current_bytes=len(craw), entries_before=len(before), entries_after=len(after),
                pointers_dropped=len(droppedptr), pointers_unresolved=len(unresolved),
                hooks_checked=checked, lost=lost, lost_n=len(lost), restored=restored,
                judged=judged,
                judged_covered=sum(1 for j in judged if j['verdict'] == 'COVERED'),
                screen_flagged=len(judged))


def main():
    rec('=' * 100)
    rec("b387 -- WHAT THE KEYSTONES' TABLES ACTUALLY CARRY. ### THE FOUR COMPONENTS.")
    rec('=' * 100)
    C1 = component1()
    C2 = component2()
    C3 = component3(C2)
    C4 = component4()
    rec('')
    rec('=' * 100)
    rec('### THE FOUR COMPONENTS, SUMMED.')
    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s' % (len(FAILS), FAILS or ''))
    rec('### ### **THE UNION NAMES %d ; %d CARRY A TABLE ; %d CARRY NONE ; %d DISAGREEMENTS '
        'REPORTED, %d RECONCILED**'
        % (C1['union_names'], C1['with_table'], C1['without_table'],
           C1['disagreements_reported'], C1['reconciled']))
    rec('### ### **ROWS COUNTED : %d ; CATEGORIES SUM : %s ; UNREADABLE : %d**'
        % (C2['rows'], C2['sums_ok'], C2['unreadable_n']))
    rec('### ### **NOT MACHINE-VERIFIED : %d OF %d (%.1f%%), EVERY ONE LABELLED IN ITS OWN ROW**'
        % (C3['not_machine_verified'], C3['rows'], C3['fraction']))
    rec('### ### **BORDERLINE DISPOSITIONS QUOTED : %d ; RECOMMENDED : %d ; THE QUESTION MOVED : '
        '%s**' % (C3['dispositions_quoted'], C3['recommended'], C3['question_moved']))
    rec('### ### **MEMORY: PRIOR BLOB EXISTS : %s ; HOOKS CHECKED : %d ; LOST : %d ; POINTERS '
        'UNRESOLVED : %d**'
        % (C4.get('has_blob'), C4.get('hooks_checked'), C4.get('lost_n'),
           C4.get('pointers_unresolved')))
    rec('### ### **NO CLASS RULED. ### NO ROW EDITED. ### NO GRADE MOVED. ### NO TABLE TOUCHED.')
    rec('### ### NO KERNEL OPENED. ### THE UNION NOT CORRECTED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b387_components_notes', LINES)
    out = dict(C1=C1, C2=C2, C3=C3, C4=C4, reread_failures=FAILS,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(d('b387_components.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    ok = (not FAILS and C2['sums_ok'] and not C4.get('halt')
          and C4.get('pointers_unresolved') == 0 and C4.get('pointers_dropped') == 0)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
