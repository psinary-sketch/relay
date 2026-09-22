# -*- coding: utf-8 -*-
"""b467_extract.py -- THE SURVEY. ### THE CONCORDANCE PARSED, THE ROW-FINDER REHEARSED, THE GENERAL
### SOURCE OPENED AT ITS BANKED ADDRESS.

### ### **b467 IS b465 RE-ISSUED UNDER ITS OWN BANKED FERRY TEXT** `(R75)`, byte-identical, and it
### runs under `(R74)`: ### **A MACHINE-CHECKED SENTENCE IS GRADED AGAINST THE TERMINAL THE DEPOSIT'S
### OWN CONCORDANCE ASSIGNS IT**, the nearest terminal by name standing in only where the concordance
### assigns none, and labelled as a stand-in when it does.
### ### **THE EIGHT ARE READ FROM b464's OWN BANK, NOT RE-DERIVED** -- b464 banked its items in full
### (b462 banked only a count, which is why b464 had to re-derive). ### The bank is cited, and the
### count it carries is checked against b462's figure before anything is graded.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
MONO = os.path.join(DEP, 'A_Place_to_Stand.md')
OPP = os.path.join(DEP, 'ONE_PAGE_PROOF.md')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
NL = chr(10)
L, MISSES = [], []

PINS = {'SIDE-kernel': 'v1.5', 'SIDE-lv-conservation': 'v0.10.0'}
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|partial\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)\s+'
                  r'([A-Za-z_][A-Za-z0-9_.\x27!?]*)')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


STOP = set('the a an of to in is are and or that this it its by at for as with from on not be '
           'which each every their they them there here what when where'.split())


def toks(s):
    return set(w for w in re.findall(r'[a-z0-9_]+', (s or '').lower())
               if len(w) > 2 and w not in STOP)


# --------------------------------------------------------------------------------------------
# ### (P1) THE CONCORDANCE, PARSED FROM THE DEPOSITED FILE AND NOT TYPED.
# --------------------------------------------------------------------------------------------
def concordance():
    """### **SECTION 25.8's TABLE, ROW BY ROW, WITH THE COLUMN THE SECTION CALLS ITS GRADE.**

    ### The concordance's own grade vocabulary is the `#print axioms` column: a clean entry reads
    ### `propext, Classical.choice, Quot.sound` and `(none)` is axiom-free. ### **THAT IS THE
    ### `STATED GRADE IN THE CONCORDANCE'S OWN VOCABULARY` THE ORDER ASKS FOR**, and it is a grade
    ### of AXIOM DEPENDENCE -- not of whether the theorem carries a claim. ### The act says so.
    """
    txt = read(MONO).split(NL)
    lo = next(i for i, l in enumerate(txt) if l.startswith('## 25.8 Kernel Concordance'))
    hi = next(i for i, l in enumerate(txt[lo:], lo) if l.startswith('# Chapter 26'))
    rows = []
    for i in range(lo, hi):
        l = txt[i]
        if not l.startswith('|') or l.startswith('|---') or l.startswith('| Claim'):
            continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) != 4:
            continue
        rows.append(dict(line=i + 1, claim=c[0], theorem=c[1].strip('`'),
                         module=c[2].strip('`'), axioms=c[3]))
    return lo + 1, hi, rows


def opp_mapping():
    """### **ONE_PAGE_PROOF's OWN MAPPING** -- its step table and its named-terminals paragraph."""
    txt = read(OPP).split(NL)
    rows, named = [], None
    for i, l in enumerate(txt):
        if l.startswith('|') and not l.startswith('|---') and l.count('|') >= 3:
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if len(c) == 3 and 'Step' not in c[0]:
                rows.append(dict(line=i + 1, step=c[0], theorem=c[1], status=c[2]))
        if 'Formal verification (named terminals' in l:
            named = dict(line=i + 1, text=l.strip())
    return rows, named


# --------------------------------------------------------------------------------------------
# ### (P2) THE ROW-FINDER. ### **PRINTED, SCORED, AND REHEARSED BEFORE THE SEAL UNDER (R70).**
# --------------------------------------------------------------------------------------------
THRESHOLD = 2


def find_row(item, rows, opp_rows):
    """### Score the sentence's CLAIM against each concordance row's CLAIM text and theorem name.

    ### ### **THE RULE IS PRINTED AND ITS THRESHOLD IS DECLARED**: a row is assigned only at a
    ### token overlap of `%d` or more, and below that the answer is `NO ROW` -- ### **NOT the
    ### nearest row.** ### b466's own finding applies here from the other side: a nearest string is
    ### how a miss becomes a false hit.
    """ % THRESHOLD
    t = toks(item['claim']) | toks(item['text'])
    scored = []
    for r in rows:
        s = len(t & (toks(r['claim']) | toks(r['theorem'].replace('.', ' ').replace('_', ' '))))
        scored.append((s, 'A_Place_to_Stand.md:25.8', r))
    for r in opp_rows:
        s = len(t & (toks(r['step']) | toks(r['theorem'])))
        scored.append((s, 'ONE_PAGE_PROOF.md', r))
    scored.sort(key=lambda x: -x[0])
    best = scored[0]
    return (best if best[0] >= THRESHOLD else None), scored[:3]


# ### ### **FORM 1 FAILED ITS OWN REHEARSAL, AND THE REHEARSAL IS WHY (R70) EXISTS.** ### On item 5
# ### it returned `techne_kernel_cross_exclusion.all_pairs_excluded` at a score of 2 -- reached
# ### because the tokenizer splits `inter-class` into `inter` and `class` and the row's claim reads
# ### `Inter-mechanism-class independence`. ### **TWO GENERIC TOKENS OUTRANKED THE SUBJECT**, and
# ### the runner-up sat one point behind, which is no margin at all over seven rows.
# ### ### **FORM 2, AND BOTH YIELDS ARE PRINTED FOR ALL EIGHT** (the matcher-lineage rule):
# ###   (i) a sentence that LIVES in ONE_PAGE_PROOF is matched against ONE_PAGE_PROOF's OWN mapping
# ###       first -- the order says `and ONE_PAGE_PROOF's own mapping where the sentence is there`,
# ###       and form 1 ignored that clause entirely;
# ###  (ii) tokens occurring in HALF OR MORE of the candidate rows are dropped as non-discriminating
# ###       -- `class`, `kernel`, `route` and their like identify nothing in this table;
# ### (iii) a row is assigned only at score >= 2 AND with a MARGIN of >= 1 over the runner-up.
# ###       ### **A TIE IS `NO ROW`, NOT A COIN TOSS** -- b464's alphabetical tie-break is the exact
# ###       defect this act was sent to stop repeating.
MARGIN = 1


def discriminating(rows, opp_rows):
    """### **DROP THE TOKENS THAT IDENTIFY NOTHING.** ### Counted over the candidate rows, printed."""
    from collections import Counter
    c = Counter()
    pool = [toks(r['claim']) | toks(r['theorem'].replace('.', ' ').replace('_', ' ')) for r in rows]
    pool += [toks(r['step']) | toks(r['theorem']) for r in opp_rows]
    for s_ in pool:
        for w in s_:
            c[w] += 1
    half = max(2, len(pool) // 2)
    return set(w for w, n in c.items() if n >= half), c


def find_row2(item, rows, opp_rows, generic):
    """### **THE SECOND FORM.** ### Returns `(hit, scored, why)` and never guesses on a tie."""
    t = (toks(item['claim']) | toks(item['text'])) - generic
    cands = []
    in_opp = item['surface'] == 'ONE_PAGE_PROOF.md'
    if in_opp:
        for r in opp_rows:
            s_ = len(t & ((toks(r['step']) | toks(r['theorem'])) - generic))
            cands.append((s_, 'ONE_PAGE_PROOF.md (its own mapping)', r))
    for r in rows:
        s_ = len(t & ((toks(r['claim']) |
                       toks(r['theorem'].replace('.', ' ').replace('_', ' '))) - generic))
        cands.append((s_, 'A_Place_to_Stand.md:25.8', r))
    cands.sort(key=lambda x: -x[0])
    if not cands or cands[0][0] < THRESHOLD:
        return None, cands[:3], 'below the threshold of %d' % THRESHOLD
    if len(cands) > 1 and cands[0][0] - cands[1][0] < MARGIN:
        return None, cands[:3], ('a tie at %d with no margin -- A TIE IS `NO ROW`' % cands[0][0])
    return cands[0], cands[:3], 'assigned at %d with a margin of %d' % (
        cands[0][0], cands[0][0] - (cands[1][0] if len(cands) > 1 else 0))


# ### ### **FORM 2 CHANGED NOTHING, AND THE ACT SAYS SO RATHER THAN QUIETLY TRYING A THIRD.**
# ### Its token-dropping step found NO token in half or more of thirteen rows, so the dropped set
# ### was EMPTY; its ONE_PAGE_PROOF precedence did not bite because that mapping's rows score 0-1;
# ### and its margin rule admits a 2-against-1 as decisive, which over a seven-row table it is not.
# ### **FORM 2's YIELD IS IDENTICAL TO FORM 1's ON ALL EIGHT**, and both stay on the record.
# ### ### **FORM 3, AND THE PRINCIPLE IT ADDS:** ### **A CONCORDANCE ROW'S IDENTITY IS ITS TERMINAL**
# ### -- the row exists to name one theorem -- ### **so an overlap that never touches the terminal's
# ### own name is an overlap with the row's PROSE, not with the row.** ### Form 3 requires at least
# ### one shared token with the theorem name itself, and reports the requirement's effect per item.
# ### **THIS IS A NARROWING, AND A NARROWING CAN HIDE A TRUE HIT**, so form 3 also prints, for every
# ### item it turns into `NO ROW`, the row form 1 would have assigned and the tokens it matched on.
def find_row3(item, rows, opp_rows, generic):
    """### **THE THIRD FORM.** ### Returns `(hit, scored, why, blocked)`."""
    t = (toks(item['claim']) | toks(item['text'])) - generic
    cands, blocked = [], None
    in_opp = item['surface'] == 'ONE_PAGE_PROOF.md'
    pool = ([(r, 'ONE_PAGE_PROOF.md (its own mapping)', toks(r['step']),
              toks(r['theorem'])) for r in opp_rows] if in_opp else [])
    pool += [(r, 'A_Place_to_Stand.md:25.8', toks(r['claim']),
              toks(r['theorem'].replace('.', ' ').replace('_', ' '))) for r in rows]
    for r, where, prose, name in pool:
        hit_name = t & name
        sc = len(t & (prose | name))
        cands.append((sc, where, r, sorted(hit_name), sorted(t & (prose | name))))
    cands.sort(key=lambda x: -x[0])
    top = [(c[0], c[1], c[2]) for c in cands[:3]]
    eligible = [c for c in cands if c[0] >= THRESHOLD and c[3]]
    if cands and cands[0][0] >= THRESHOLD and not cands[0][3]:
        blocked = dict(row=(cands[0][2].get('theorem') or cands[0][2].get('step')),
                       score=cands[0][0], matched_on=cands[0][4])
    if not eligible:
        return None, top, ('NO ROW -- no candidate shares a token with its own terminal name'
                           if blocked else 'NO ROW -- below the threshold of %d' % THRESHOLD), blocked
    if len(eligible) > 1 and eligible[0][0] - eligible[1][0] < MARGIN:
        return None, top, 'NO ROW -- a tie at %d with no margin' % eligible[0][0], blocked
    e = eligible[0]
    return (e[0], e[1], e[2]), top, 'assigned at %d, sharing %s with the terminal name' % (
        e[0], '/'.join(e[3])), blocked


# ### ### **FORM 3 FAILED ITS OWN POSITIVE CONTROL AT 4 OF 7, AND ITS EIGHT `NO ROW`s WERE NOT
# ### BANKED.** ### The control fed each concordance row's own claim back as a sentence; a finder
# ### that cannot recover a row from the row's own words cannot be trusted to report that the table
# ### holds nothing. ### **TWO BUGS, BOTH IN THE TOKENIZER AND BOTH VISIBLE ONLY UNDER THE CONTROL:**
# ###   (i) `ConservationBridge` was never split, so the claim's `conservation` could not meet the
# ###       terminal's own name -- ### **camelCase was invisible to a word matcher;**
# ###  (ii) `pair` never matched `pairs` -- no stemming at all.
# ### ### **AND ONE FINDING THAT IS NOT A BUG:** `SpectralCannonFull.spectral_cannon`'s row claim is
# ### *"Route 2 -- perpendicular crossing: the completed-zeta derivative is imaginary on the line"*,
# ### which shares NO WORD with its own terminal's name even after both repairs. ### **SO A NAME-
# ### OVERLAP REQUIREMENT CANNOT BE A VETO** -- the deposit itself contains a counterexample to it.
# ### ### **FORM 4:** camelCase split, light stemming, and name-overlap as a PREFERENCE -- if any
# ### eligible candidate touches the terminal's name, only those compete; if none does, a prose-only
# ### match is still allowed but must clear a HIGHER bar of 3, because prose is the weaker evidence.
PROSE_ONLY_BAR = 3
CAMEL = re.compile(r'[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])')


def toks4(s):
    """### **camelCase SPLIT AND LIGHTLY STEMMED.** ### `ConservationBridge` -> conservation, bridge."""
    out = set()
    for chunk in re.split(r'[^A-Za-z0-9_\x27]+', s or ''):
        for part in chunk.split('_'):
            for w in CAMEL.findall(part):
                w = w.lower()
                if len(w) > 2 and w not in STOP:
                    out.add(w[:-1] if len(w) > 4 and w.endswith('s') else w)
    return out


def find_row4(item, rows, opp_rows):
    """### **THE GOVERNING FORM.** ### Returns `(hit, top, why, blocked)`."""
    t = toks4(item['claim']) | toks4(item['text'])
    cands = []
    in_opp = item['surface'] == 'ONE_PAGE_PROOF.md'
    pool = ([(r, 'ONE_PAGE_PROOF.md (its own mapping)', toks4(r['step']),
              toks4(r['theorem'])) for r in opp_rows] if in_opp else [])
    pool += [(r, 'A_Place_to_Stand.md:25.8', toks4(r['claim']), toks4(r['theorem'])) for r in rows]
    for r, where, prose, name in pool:
        cands.append((len(t & (prose | name)), where, r, sorted(t & name), sorted(t & (prose | name))))
    cands.sort(key=lambda x: -x[0])
    top = [(c[0], c[1], c[2]) for c in cands[:3]]
    named = [c for c in cands if c[0] >= THRESHOLD and c[3]]
    if named:
        pool2, bar = named, THRESHOLD
    else:
        pool2, bar = [c for c in cands if c[0] >= PROSE_ONLY_BAR], PROSE_ONLY_BAR
    if not pool2:
        best = cands[0] if cands else None
        why = ('NO ROW -- the best candidate scores %d on PROSE ALONE, under the prose-only bar of %d'
               % (best[0], PROSE_ONLY_BAR)) if best and best[0] >= THRESHOLD else \
              ('NO ROW -- no candidate reaches the threshold of %d' % THRESHOLD)
        return None, top, why, (dict(row=(best[2].get('theorem') or best[2].get('step')),
                                     score=best[0], matched_on=best[4])
                                if best and best[0] >= THRESHOLD else None)
    if len(pool2) > 1 and pool2[0][0] - pool2[1][0] < MARGIN:
        return None, top, 'NO ROW -- a tie at %d with no margin' % pool2[0][0], None
    e = pool2[0]
    return (e[0], e[1], e[2]), top, ('assigned at %d, %s' % (
        e[0], ('sharing %s with the terminal name' % '/'.join(e[3])) if e[3]
        else ('on PROSE ALONE over the raised bar of %d' % PROSE_ONLY_BAR))), None


def statement_of(kernel, name):
    """### **THE STATEMENT, READ FROM THE SOURCE AT ITS PIN, NEVER THE DOCSTRING** -- b464's reader,
    ### carried with both of its repairs: the four-field `git grep` parse and the widened keyword set.
    """
    repo = os.path.join('D:', os.sep, kernel)
    ref = PINS.get(kernel, 'HEAD')
    short = name.split('.')[-1]
    r = git(repo, 'grep', '-n', '-E',
            r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)\s+%s\b' % re.escape(short),
            ref, '--', '*.lean')
    if not r.stdout.strip():
        return None, None, ref
    parts = r.stdout.strip().split(NL)[0].split(':', 3)
    if len(parts) < 4:
        return None, None, ref
    path, lno = parts[1], int(parts[2])
    blob = git(repo, 'show', '%s:%s' % (ref, path)).stdout.replace(chr(13), '').split(NL)
    body, depth, past = [], 0, False
    for l in blob[lno - 1:lno + 24]:
        if past:
            if not l.strip():
                break
            body.append(l)
            continue
        body.append(l)
        depth += l.count('(') - l.count(')')
        if (':=' in l or ' where' in l) and depth <= 0:
            if l.rstrip().endswith(':=') or ' where' in l:
                past = True
                continue
            break
    return path, NL.join(body), ref


def main():
    rec('=' * 104)
    rec('b467 -- THE SURVEY. ### b465 RE-ISSUED UNDER (R75); THE READ RUNS UNDER (R74).')
    rec('=' * 104)
    rec('  ferry : b467_ferry.txt, BYTE-IDENTICAL to b465_ferry.txt -- the order is unchanged.')

    rec('')
    rec('(P1) THE CONCORDANCE, PARSED FROM THE DEPOSITED FILE.')
    rec('-' * 104)
    lo, hi, rows = concordance()
    rec('  section 25.8 at A_Place_to_Stand.md:%d ; table rows parsed : %d' % (lo, len(rows)))
    for r in rows:
        rec('    :%-5d %-46s %s' % (r['line'], r['theorem'][:46], r['axioms'][:44]))
    rec('  ### ### **THE CONCORDANCE\x27s OWN GRADE COLUMN IS `#print axioms`.** ### A clean entry is')
    rec('  ### `propext, Classical.choice, Quot.sound`; `(none)` is axiom-free. ### **THAT IS A GRADE')
    rec('  ### OF AXIOM DEPENDENCE, NOT OF WHETHER THE THEOREM CARRIES THE CLAIM**, and the two are')
    rec('  ### different questions -- which is the whole reason (R74) asks for a SECOND grade beside it.')
    prof = read(MONO).split(NL)
    for i in range(lo, hi):
        if 'Statuses read at SIDE-kernel' in prof[i]:
            rec('  ### the concordance\x27s own profiling pin, quoted:')
            rec('      %s' % prof[i].strip()[:230])
            break

    rec('')
    rec('(P2) ONE_PAGE_PROOF\x27s OWN MAPPING.')
    rec('-' * 104)
    opp_rows, named = opp_mapping()
    rec('  step-table rows : %d' % len(opp_rows))
    for r in opp_rows:
        rec('    :%-5d %-28s %-34s %s' % (r['line'], r['step'][:28], r['theorem'][:34], r['status']))
    if named:
        rec('  the named-terminals paragraph : ONE_PAGE_PROOF.md:%d' % named['line'])
        rec('      %s' % named['text'][:220])

    rec('')
    rec('(P3) THE REHEARSAL, UNDER (R70), BEFORE THE SEAL. ### **THE ROW-FINDER ON ITEM 5.**')
    rec('-' * 104)
    G = json.loads(read(os.path.join(D, 'b464_grades.json')))
    rec('  b464\x27s bank : %d items ; by grade %s'
        % (len(G['items']), ' / '.join('%s %d' % (k, G['by_grade'][k]) for k in sorted(G['by_grade']))))
    rec('  ### the count against b462\x27s banked figure of 8 : %s'
        % ('AGREE' if len(G['items']) == 8 else '### DISAGREE'))
    it5 = G['items'][4]
    rec('  item 5 : %s:%d' % (it5['surface'], it5['line']))
    rec('    b464\x27s nearest-by-name terminal : %s (%s) -- graded %s'
        % (it5['terminal'], it5['grade'], it5['grade']))
    rec('    the claim, as b464 stated it : %s' % it5['claim'])
    hit, top = find_row(it5, rows, opp_rows)
    rec('    the row-finder\x27s top three, scored:')
    for s, where, r in top:
        rec('      %2d  %-22s %s' % (s, where, (r.get('theorem') or r.get('step'))[:60]))
    rec('    ### ### **THE ROW-FINDER RETURNS : %s**'
        % ('NO ROW -- below the declared threshold of %d' % THRESHOLD if not hit
           else '%s at %s' % (hit[2].get('theorem') or hit[2].get('step'), hit[1])))
    generic, counted = discriminating(rows, opp_rows)
    rec('')
    rec('  ### **FORM 2, AND BOTH YIELDS OVER ALL EIGHT.** ### non-discriminating tokens dropped:')
    rec('      %s' % ' '.join(sorted(generic)))
    rec('  %-3s %-22s %-22s %-22s %-22s'
        % ('#', 'FORM 1', 'FORM 2', 'FORM 3', 'FORM 4 (governing)'))
    rec('  ' + '-' * 100)
    lineage = []
    for it in G['items']:
        h1, _t1 = find_row(it, rows, opp_rows)
        h2, t2, why2 = find_row2(it, rows, opp_rows, generic)
        h3, t3, why3, blocked = find_row3(it, rows, opp_rows, generic)
        f1 = 'NO ROW' if not h1 else (h1[2].get('theorem') or h1[2].get('step'))
        f2 = 'NO ROW' if not h2 else (h2[2].get('theorem') or h2[2].get('step'))
        f3 = 'NO ROW' if not h3 else (h3[2].get('theorem') or h3[2].get('step'))
        h4, t4, why4, blocked4 = find_row4(it, rows, opp_rows)
        f4 = 'NO ROW' if not h4 else (h4[2].get('theorem') or h4[2].get('step'))
        rec('  %-3d %-22s %-22s %-22s %-22s' % (it['n'], f1[:22], f2[:22], f3[:22], f4[:22]))
        rec('      why : %s' % why4)
        if blocked4:
            rec('      ### **THE BEST CANDIDATE, REFUSED** : %s at %d, matched only on %s'
                % (blocked4['row'][:46], blocked4['score'], '/'.join(blocked4['matched_on'])))
        lineage.append(dict(n=it['n'], form1=f1, form2=f2, form3=f3, form4=f4, why=why4,
                            where=(None if not h4 else h4[1]), blocked=blocked4,
                            top=[[sc, w, (r.get('theorem') or r.get('step'))] for sc, w, r in t4]))
    rec('')
    rec('  ### ### **FOUR FORMS, EVERY YIELD ON THE RECORD.** ### form 1 = form 2 on 8 of 8 ;')
    rec('  ### form 3 differs from form 1 on %d ; ### **FORM 4 DIFFERS FROM FORM 1 ON %d AND FROM'
        % (sum(1 for x in lineage if x['form3'] != x['form1']),
           sum(1 for x in lineage if x['form4'] != x['form1'])))
    rec('  ### FORM 3 ON %d.** ### **FORM 4 GOVERNS, AND IT IS THE ONLY ONE THAT PASSES ITS CONTROL.**'
        % sum(1 for x in lineage if x['form4'] != x['form3']))

    # ### ### **A NARROWING THAT RETURNS `NO ROW` EIGHT TIMES OUT OF EIGHT MUST BE CONTROLLED.**
    # ### b404's rule: every ABSENT carries a control. ### Here the ABSENT is `the concordance
    # ### assigns no row`, and the control is a sentence that MUST be assigned one -- the row's own
    # ### claim text, fed back in as if it were a deposited sentence. ### **IF FORM 3 CANNOT FIND A
    # ### ROW FOR THE ROW'S OWN WORDS, FORM 3 IS WHAT IS BROKEN AND NOT THE CONCORDANCE.**
    rec('')
    rec('  ### **THE CONTROL, ON FORM 4.** ### Each row\x27s OWN claim fed back as a sentence:')
    fired = 0
    for r in rows:
        probe = dict(surface='A_Place_to_Stand.md', claim=r['claim'], text=r['claim'], n=0)
        h, _t, why, _b = find_row4(probe, rows, opp_rows)
        got = 'NO ROW' if not h else (h[2].get('theorem') or h[2].get('step'))
        ok = (got == r['theorem'])
        fired += ok
        rec('    %-46s -> %-46s %s' % (r['theorem'][:46], got[:46], 'OK' if ok else '### MISS'))
    rec('    ### ### **CONTROL : %d of %d ROWS RECOVER THEMSELVES.** ### **%s**'
        % (fired, len(rows),
           'THE FINDER WORKS AND THE EIGHT `NO ROW`s ARE THE CONCORDANCE\x27s, NOT THE FINDER\x27s'
           if fired == len(rows) else
           'THE FINDER IS TOO NARROW AND ITS EIGHT `NO ROW`s CANNOT BE BANKED'))

    # ### ### **AND A NEGATIVE CONTROL, BECAUSE A FINDER THAT ASSIGNS EVERYTHING WOULD ALSO PASS
    # ### THE ONE ABOVE.** ### A sentence about something the concordance does not carry must return
    # ### `NO ROW`, or the finder is assigning rows to anything put in front of it.
    neg = dict(surface='A_Place_to_Stand.md', n=0,
               claim='that the Epstein zeta function of a quaternary form has zeros off the line',
               text='that the Epstein zeta function of a quaternary form has zeros off the line')
    hn, _t, whyn, _b = find_row4(neg, rows, opp_rows)
    rec('    negative control (a subject the concordance does not carry) -> %s   ### **%s**'
        % ('NO ROW' if not hn else (hn[2].get('theorem') or hn[2].get('step')),
           'OK' if not hn else '### THE FINDER ASSIGNS ROWS TO ANYTHING'))
    rec('')
    rec('    ### ### **THE ORDER EXPECTED THE SUBSTANTIVE TERMINAL BESIDE THE SHELL**')
    rec('    ### (`s_darkness_from_product`). ### **THE REHEARSAL\x27s ANSWER IS PRINTED ABOVE AND IS')
    rec('    ### NOT ADJUSTED TO MEET THAT EXPECTATION** -- the finder reads the concordance, and')
    rec('    ### the concordance is a fixed text. ### Whatever it returns is what this act carries.')

    rec('')
    rec('(P4) THE GENERAL SOURCE, AT ITS BANKED ADDRESS.')
    rec('-' * 104)
    lag = read(LAG)
    rec('  b358_source_lagarias0404394.txt : %d lines' % lag.count(NL))
    for label, needle in (
            ('the completed L-function', 'Each completed automorphic L-function'),
            ('the conductor', 'called the conductor of the representation'),
            ('the archimedean factor', 'and the archimedean'),
            ('the Euler product over finite places', 'is given by an Euler product over the'),
            ('the functional equation', 'satisfy a functional equation'),
            ('the analytic conductor', 'analytic conductor'),
            ('the general quadratic functional', 'natural generalization of Weil'),
            ('the appendix scope sentence', 'For all other automorphic representations'),
            ('the Weil distribution functional', 'We deﬁne the Weil distribution functional'),
            ('the truncation of the sum', 'means that the (possibly conditionally convergent) sum'),
            ('the trace form', 'The “explicit formula” in trace form'),
            ('the places sum', 'is a contribution associated to each'),
            ('the general-pi sentence', 'For general au'),
    ):
        n = None
        for i, l in enumerate(lag.split(NL)):
            if needle in l:
                n = i + 1
                rec('    %-38s :%-5d %s' % (label, n, l.strip()[:120]))
                break
        if n is None:
            MISSES.append(('b358_source_lagarias0404394.txt', needle))
            rec('    %-38s ### MISS -- %r' % (label, needle))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b467_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(concordance=rows, concordance_line=lo, opp_rows=opp_rows,
                   opp_named=named, threshold=THRESHOLD, eight=len(G['items']),
                   rehearsal=dict(item=5, top=[[s, w, (r.get('theorem') or r.get('step'))]
                                               for s, w, r in top],
                                  returns=None if not hit else (hit[2].get('theorem')
                                                                or hit[2].get('step'))),
                   lineage=lineage, generic=sorted(generic),
                   control_fired=fired, control_rows=len(rows),
                   negative_control_no_row=(hn is None),
                   misses=MISSES),
              io.open(os.path.join(D, 'b467_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
