# -*- coding: utf-8 -*-
"""b443r_components.py -- THE COMPONENTS OF b443'S RE-ISSUE. ### **RUN AFTER THE FRESH FACE'S LOCK.**

### ### **COMPONENT 0** -- `(R55)` and `(R56)`: the stranded file's digest re-read; `reg_seal.py`'s fixtures read
### from their record. ### **COMPONENT 1** -- site (vi), ten candidates, the count at six sites. ### **COMPONENT 2**
### -- row U1's restatement DRAFTED into `data/b443r_u1_draft.md`. ### **COMPONENT 3** -- the three filings'
### texts, and the fold's span read by `b363_span.py`.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KEY = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
LED = os.path.join(PP, 'FACES_LEDGER.md')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
CC = os.path.join(D, 'b328_source_text.txt')
OUT = os.path.join(D, 'b443r_components.txt')
DRAFT = os.path.join(D, 'b443r_u1_draft.md')
STRANDED = os.path.join(D, 'b443_registration_2026-09-12.txt')
STRANDED_SHA = 'b8d4838c787d439fac5171597254be6101de340ffedffae8a96c6124d304abac'
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, MISS = [], []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('=' * 100)
    rec('  ### ### **%s -- %s**' % (n, t))
    rec('=' * 100)


def sub(t):
    rec('')
    rec('-' * 100)
    rec('  ### %s' % t)
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def wrap(s, n=84):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, clip=500, span=None):
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('      %s:%d' % (os.path.basename(path), i + 1))
            seg = ln.strip()
            if span:
                j = seg.find(needle)
                seg = seg[j:j + span]
            for c in wrap(seg[:clip], 82):
                rec('        | %s' % c)
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), needle[:50]))
    rec('      ### **NOT LOCATED** : %s' % needle[:60])
    return None


def component_0():
    head('COMPONENT 0', '(R55) AND (R56) EXECUTED')
    sha = hashlib.sha256(open(STRANDED, 'rb').read()).hexdigest()
    rec('    stranded registration : %s' % os.path.basename(STRANDED))
    rec('    sha256 now            : %s' % sha)
    rec('    sha256 on the face    : %s' % STRANDED_SHA)
    rec('    ### ### **(R55) : %s.** ### No component of this tool reads it for anything but its digest.'
        % ('UNCHANGED' if sha == STRANDED_SHA else '### BREACH -- CHANGED ###'))
    fx = read(os.path.join(D, 'b443r_seal_fixtures.txt'))
    for ln in fx.splitlines():
        if ln.strip():
            rec('    | %s' % ln.rstrip())
    diff = subprocess.run(['git', '-C', ROOT, 'diff', '--numstat', '--', 'tools/reg_seal.py'],
                          capture_output=True, text=True).stdout.strip()
    rec('    reg_seal.py numstat against HEAD (added / deleted) : %s' % diff)
    return sha == STRANDED_SHA


CANDS = [
    ('D1', 'the 1919 sieve result, as the keystone cites it', 'S2', 'IMPORT UNDER THE BAR',
     [(KEY, "Brun's sieve (1919)")],
     'No verified source holds a sieve text, so the result cannot be imported under the bar; and the '
     'keystone`s own characterization of it owes a source read (Component 3(ii)).'),
    ('D2', 'the circle method for ternary Goldbach', 'S1', 'CLASS BOUNDARY',
     [(KEY, 'the circle method (Vinogradov 1937 for ternary Goldbach; partial results for binary)')],
     'Its class is sums of three primes; milestone M4 needs a lower bound for the binary count, and the '
     'keystone`s own sentence says binary has only partial results.'),
    ('D3', 'Maynard`s bounded intervals between consecutive primes', 'S1', 'CLASS BOUNDARY',
     [(KEY, 'Maynard (2013) sharpened')],
     'A bound on intervals between consecutive primes is not a positive lower bound on the density of '
     'twin, Goldbach-pair or Sophie Germain primes -- a different statistic.'),
    ('D4', 'milestone M3, the Hardy-Littlewood asymptotic', 'S2', 'ABSENT',
     [(KEY, 'The analytic requirement is named as M3')],
     'Named as the milestone the keystone still requires; not established in the record or the verified '
     'sources.'),
    ('D5', 'milestone M4, the binary representation lower bound', 'S2', 'ABSENT',
     [(KEY, 'The analytic requirement is named as M4')],
     'Named as a milestone; not established.'),
    ('D6', 'milestone M5, the Sophie Germain sieve bound', 'S2', 'ABSENT',
     [(KEY, 'sorry  -- M5, open: requires sieve density bounds')],
     'Compiled as `sorry` with the words "M5, open".'),
    ('D7', 'the keystone`s `density_positive : True`', 'S3', 'FORM',
     [(KEY, '`density_positive : True`')],
     'A placeholder: the density clause is stipulated as `True`, and the keystone names it as the thing to '
     'replace.'),
    ('D8', 'the compiled `crt_exhaustiveness`', 'S1', 'CLASS BOUNDARY',
     [(os.path.join(D, 'b431_components.txt'), 'moduli := {L}')],
     'Its witness ranges over one modulus, a singleton (b431); the missing statement is across moduli.'),
    ('D9', 'the compiled shared-witness theorem', 'S1', 'CLASS BOUNDARY',
     [(LED, 'a theorem about a SHAPE is not a theorem about any instance of it')],
     'A theorem about the shape of the interchange, not about this instance of it; the row`s own law forbids '
     'the crossing.'),
    ('D10', 'a density lower bound across moduli in the verified sources', 'S2', 'ABSENT',
     [(LAG, 'The counting result the zero density'), (CC, 'zeros of this function are complex numbers of modulus 1')],
     'Every vocabulary hit in both sources is a zero density of an L-function or a complex modulus; none bounds '
     'a prime density from below across moduli.'),
]


def component_1():
    head('COMPONENT 1', 'THE WITNESS ARC AT SITE (vi), THE TYPE-D RESIDUE')
    sub('THE SITE`S OWN CELL, QUOTED FIRST')
    quote(LED, '**(vi) THE TYPE-D RESIDUE AT EVERY FINITE MODULUS**', clip=1100, span=1100)
    quote(LED, '### **`(vi)` — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.**', clip=500, span=500)
    rows = []
    for cid, name, step, kind, qs, why in CANDS:
        sub('%s -- %s' % (cid, name))
        ok = all(quote(p, n, clip=420, span=420) is not None for p, n in qs)
        rec('      attempted : S1 CLASS%s%s' % (' -> S2 HELD' if step in ('S2', 'S3') else '',
                                              ' -> S3 FORM' if step == 'S3' else ''))
        if not ok:
            rec('      ### **NOT QUOTABLE -- DROPPED.**')
            continue
        rec('      ### ### **FAILED AT %s -- %s.**' % (step, kind))
        for c in wrap(why, 84):
            rec('        %s' % c)
        rows.append(dict(id=cid, name=name, step=step, kind=kind, why=why,
                         quotes=[(os.path.basename(p), n) for p, n in qs]))
    sub('THE VERIFIED SOURCES` VOCABULARY HITS, EACH CLASSIFIED')
    for nm, p in (('Lagarias', LAG), ('CC', CC)):
        for i, ln in enumerate(read(p).splitlines()):
            if re.search(r'density|modul|positive proportion|sieve|twin prime|Goldbach', ln, re.I):
                why = ('a zero density of an L-function' if 'densit' in ln.lower() else
                       'a modulus of a complex number or a function' if 'modul' in ln.lower() else 'other')
                rec('      %-9s %5d  %-45s | %s' % (nm, i + 1, why, ln.strip()[:60]))
    sub('BY DESCRIPTION, UNDER THE CAP OF 4 -- a positive density lower bound across moduli, searched in the keystone')
    extra = [(i + 1, ln.strip()[:100]) for i, ln in enumerate(read(KEY).splitlines())
             if re.search(r'positive lower bound|lower bound for', ln, re.I)]
    for i, ln in extra:
        rec('      keystone %4d | %s' % (i, ln))
    rec('      ### every hit restates M3, M4 or M5, already candidates D4-D6: ### **0 FURTHER CANDIDATES.**')

    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    rec('')
    rec('    ### ### **%d CANDIDATES, %d HELD. FIRST FAILING STEPS: %s.**'
        % (len(rows), 0, '; '.join('%s %d' % kv for kv in sorted(kinds.items(), key=lambda x: (-x[1], x[0])))))

    sub('THE BOUNDARY COUNT AT SIX SITES -- FROM BANKED JSON, NEVER TYPED')
    prior = json.loads(read(os.path.join(D, 'b442_site_v.json')))
    tallies = dict(prior['tallies'])
    tallies['b443'] = kinds
    labels = dict(b424='(i)', b427='(ii)', b428='(iii)', b436='(iv)', b442='(v)', b443='(vi)')
    total = 0
    for act, t in tallies.items():
        n = sum(t.values())
        total += n
        cb = t.get('CLASS BOUNDARY', 0)
        rec('      site %-5s %-5s %2d candidates ; CLASS BOUNDARY %2d of %2d -- %s'
            % (labels[act], act, n, cb, n, 'MAJORITY' if cb * 2 > n else ('TIE' if cb * 2 == n else 'NOT A MAJORITY')))
    union5 = set().union(*[set(t) for a, t in tallies.items() if a != 'b443'])
    union6 = union5 | set(kinds)
    new = sorted(set(kinds) - union5)
    agg = {}
    for t in tallies.values():
        for k, v in t.items():
            agg[k] = agg.get(k, 0) + v
    rec('      candidates across six sites : %d' % total)
    rec('      union of kinds after five sites : %d ; after six : %d ; new at (vi) : %s'
        % (len(union5), len(union6), new))
    for k, v in sorted(agg.items(), key=lambda x: (-x[1], x[0])):
        rec('        %-28s %3d' % (k, v))
    top = sorted(kinds.items(), key=lambda x: -x[1])
    rec('    ### ### **AT SITE (vi): %s.**' % ('; '.join('%s %d' % kv for kv in top)))
    if len(union6) == 11 and not new:
        rec('    ### ### **THE ARC`S FINDING: SIX SITES, %d CANDIDATES, NO WITNESS HELD, AND THE UNION OF FAILURE KINDS STAYS AT'
            % total)
        rec('    ### ### ELEVEN -- THE SIXTH SITE ADDED NO NEW WAY TO FAIL.** The arc is checkpointed after (vi), its last site.')
    json.dump(dict(candidates=rows, tallies=tallies, total=total, union5=len(union5), union6=len(union6),
                   new_kinds=new, aggregate=agg),
              io.open(os.path.join(D, 'b443r_site_vi.json'), 'w', encoding='utf-8'), indent=1)
    return rows, kinds, tallies, agg, total, len(union6)


MISSING = [
    ('(i)', 'the clause`s quantifier', 'one owner for the quantifiers over the class and, through the explicit formula, over the zeros',
     'the quantifiers are *"UNOWNED, and they are the clause"* (b332)'),
    ('(ii)', 'the height coordinate`s enumeration', 'one argument serving every height',
     'a census that produces zeros one at a time; the coordinate *"BOUNDED BY A MEASUREMENT and not by an argument"* (b351)'),
    ('(iii)', 'the width coordinate`s union', 'one `g` serving every width',
     'Boas–Kac at each support; *"AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS"* (b353)'),
    ('(iv)', 'the prime constituent at a widened support', 'one statement uniform in the width `a` bounding `Σ_p W_p(f)` against an archimedean quantity',
     'ten values indexed by `a` (b321)'),
    ('(v)', 'the representation-dependent constant', 'one constant serving every representation the record holds',
     'Theorem 6.1`s constant *"depends on π"*, over a cuspidal class the second object is not established to belong to'),
    ('(vi)', 'the Type-D residue at every finite modulus', 'a positive global density lower bound across moduli',
     'a compiled exclusion at every finite modulus; the keystone files the density bound as *the whole of the remaining weight*'),
]


def component_2(tallies, agg, total, union6):
    head('COMPONENT 2', 'ROW U1`S RESTATEMENT -- DRAFTED, NOT APPLIED')
    led = read(LED)
    u1 = [l for l in led.splitlines() if l.startswith('| U1 ')][0]
    m = re.search(r'THE DEPOSIT’S REFUSAL GOVERNS THIS ENTRY AS IT GOVERNS THE LEDGER:.*?NO EQUIVALENCE IS COMPILED\.', u1)
    refusal = m.group(0) if m else None
    rec('    the row`s refusal located verbatim : %s' % bool(refusal))
    labels = dict(b424='(i)', b427='(ii)', b428='(iii)', b436='(iv)', b442='(v)', b443='(vi)')
    by_label = {labels[a]: t for a, t in tallies.items()}
    kinds = sorted(agg, key=lambda k: (-agg[k], k))
    D_ = ['# DRAFT — ROW U1, RESTATED IN THE CONSPIRACY KEYSTONE’S RESIDUE FORM', '',
          '*Drafted at b443 on the author’s order. **NOT APPLIED.** Row U1 in `PLACE-papers/FACES_LEDGER.md` is unedited; '
          'this text becomes anything only on the author’s word. Every count below is read from banked JSON '
          '(`b436_prior_sites.json`, `b436_candidates.json`, `b442_site_v.json`, `b443r_site_vi.json`).*', '',
          '## The row, per site: what the record holds, the missing statement, and the residue', '',
          '| site | what the record holds | the missing statement, named exactly | the residue |', '|:--|:--|:--|:--|']
    for tag, name, missing, holds in MISSING:
        D_.append('| **%s** %s | %s | %s | **%s is the whole of the remaining weight** |' % (tag, name, holds, missing, missing))
    D_ += ['', '## The witness arc’s taxonomy of failure, six sites', '',
           '| kind | ' + ' | '.join(['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)']) + ' | total |',
           '|:--|' + '--:|' * 7]
    for k in kinds:
        D_.append('| %s | %s | %d |' % (k, ' | '.join(str(by_label[s].get(k, 0)) for s in ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)']), agg[k]))
    D_.append('| **candidates** | %s | **%d** |' % (' | '.join(str(sum(by_label[s].values())) for s in ['(i)', '(ii)', '(iii)', '(iv)', '(v)', '(vi)']), total))
    D_ += ['', '**%d candidates across six sites; no witness held; %d kinds of failure.** The class boundary is the largest kind '
           'overall and the majority at four sites of six — not at site (iv) (`1` of `7`) and not at site (vi). '
           'The premise that it is the majority at every site was the navigator’s, and is withdrawn as false.' % (total, union6), '',
           '## The row’s refusal, verbatim', '', '> ' + (refusal or '### NOT LOCATED'), '',
           '---', '',
           '# DRAFT UPDATE BLOCK — ROW U1, ENTRY (v): A TRANSCRIPTION DEFECT OF THE b341 SPECIES', '',
           '*Drafted at b443 and routed for the author’s word. **NOT APPENDED.** The species is b341’s: a transcription '
           'defect in a quantity carried from the literature.*', '',
           '| row / entry | as the row writes it | as the source reads | the defect |', '|:--|:--|:--|:--|',
           '| **U1**, entry **(v)** | `S_f(n,π) = λ_n(n,π) + O(n log n)` | `S_f(n,π) = λ_n(√n,π∨) + O(√n log n)` '
           '(Lagarias math/0404394v4 Theorem 6.1, relay `data/b358_source_lagarias0404394.txt:1994`) | the Li index is `n` '
           'where the source has `√n`, the dual representation is dropped, and the error term`s argument follows; the '
           'dependence of the implied constant on `π` — the site’s content — is unaffected |', '']
    io.open(DRAFT, 'w', encoding='utf-8', newline=NL).write(NL.join(D_) + NL)
    rec('    draft written : %s (%d lines) ### **APPLIED NOWHERE.**' % (os.path.basename(DRAFT), len(D_)))
    return refusal is not None


def component_3():
    head('COMPONENT 3', 'THREE FILINGS, NONE OPENED; AND THE SPAN')
    sub('(i) THE INDEX DEFECT -- THE b341 SPECIES, QUOTED')
    quote(os.path.join(PP, 'FINDINGS.md'), '- **b341 — the two Li coefficients located', clip=400)
    rec('      ### drafted as an update block in `b443r_u1_draft.md`; row U1 unedited.')
    sub('(ii) LINE 231 -- A SENTENCE OWING A SOURCE READ')
    quote(KEY, "Brun's sieve (1919)", clip=260, span=260)
    rec('      ### **THE SEAT`S RECOLLECTION -- A RECOLLECTION, NOT A READING -- IS THAT THE 1919 RESULT IS AN UPPER BOUND.**')
    rec('      ### No verified source holds a sieve text. ### Filed as owing a source read; the keystone is not edited.')
    sub('(iii) THE FAST-RADIO-BURST TRAIL')
    quote(os.path.join(PP, 'OPEN_TRAILS.md'), '**`(R38)`** keys the lane', clip=400)
    rec('      ### trail text is written into this act`s OPEN_TRAILS record by b443r_desk_bank.py; nothing is read at any address.')
    sub('THE FOLD`S SPAN -- b363_span.py, RUN TO READ')
    before = set(os.listdir(D))
    r = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT)
    after = set(os.listdir(D))
    io.open(os.path.join(D, 'b443r_span.txt'), 'w', encoding='utf-8', newline=NL).write(r.stdout or '')
    for ln in (r.stdout or '').splitlines()[-14:]:
        rec('    | %s' % ln)
    rec('    files the span tool created in data/ : %s' % sorted(after - before))
    quote(os.path.join(PP, 'FINDINGS.md'), '## The external-grading arc — b423 through b432, folded at b434', clip=120)
    rec('    ### ### **THE TOOL`S SPAN MISSES b434`S FOLD**, whose heading its pattern does not match -- b434`s own fold')
    rec('    ### ### record printed the same defect. ### Counted from that fold, by the record`s convention that a span ends')
    rec('    ### ### before its filing act and the next begins after it: ### **b433 THROUGH b443, 11 ACTS**, against the')
    rec('    ### ### tool`s 21. ### Both figures printed; the tool is not repaired -- the instrument lane is open for')
    rec('    ### ### `reg_seal.py` alone.')


def main():
    rec('=' * 100)
    rec('b443 (re-issue) -- SITE (vi), AND THE ARC`S PRODUCT NAMED. ### COMPONENTS, RUN AFTER THE FRESH FACE`S LOCK.')
    rec('=' * 100)
    ok0 = component_0()
    rows, kinds, tallies, agg, total, union6 = component_1()
    ok2 = component_2(tallies, agg, total, union6)
    component_3()
    rec('')
    rec('=' * 100)
    rec('  ### ### **C0 stranded unchanged %s ; C1 %d candidates, 0 held, %s ; union %d ; C2 refusal verbatim %s ; MISSES %d %s**'
        % (ok0, len(rows), kinds, union6, ok2, len(MISS), MISS or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)


if __name__ == '__main__':
    main()
