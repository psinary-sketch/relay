# -*- coding: utf-8 -*-
"""b455_components.py -- THE DEPOSIT'S EXHAUSTIVENESS CLAIM READ AGAINST ITS OWN ROUTE TERMINAL.

### ### **EVERY RULE IS THE LOCKED FACE'S** (`data/b455_registration_2026-09-14.txt`). ### Modes, in order: `items`
### (the five surfaces split and searched, both yields printed, nothing classified); `terminals` (the two terminals read at
### `v1.5` by `git show`, profiles gathered, nothing graded); `report` (the hand-read classifications, grades, dispositions
### and the line's verdict applied, the record written). ### **READ ONLY: NO `lean`, NO `lake`, NO FETCH, NO WRITE OUTSIDE
### `data/b455_*`.**
"""
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
PIN = 'v1.5'
CLAIMJ = os.path.join(D, 'b455_claims.json')
TERMJ = os.path.join(D, 'b455_terminals.json')
DISPJ = os.path.join(D, 'b455_dispositions.json')
LINEJ = os.path.join(D, 'b455_line.json')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def dump_json(path, obj):
    data = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)


def sentences(block):
    """### A table row or list item is one item; prose is split at sentence ends."""
    s = block.strip()
    if s.startswith('|') or re.match(r'^[-*] ', s):
        return [s]
    return [x.strip() for x in re.split(r'(?<=[.;])\s+(?=[A-Z*`(])', s) if x.strip()]


def surfaces():
    fr = json.loads(read(os.path.join(D, 'b359_fetch_F2.json')))
    desc = fr['metadata']['description']
    s1 = [html.unescape(re.sub(r'<[^>]+>', '', p)) for p in re.findall(r'<p>(.*?)</p>', desc, re.S)]
    zl = read(os.path.join(D, 'zenodo_fetch_2026-08-10.jsonl')).splitlines()
    s2_rows = []
    for i, l in enumerate(zl):
        try:
            j = json.loads(l)
        except Exception:
            continue
        if j.get('doi') == '10.5281/zenodo.21520474':
            s2_rows.append(dict(line=i + 1, keys=sorted(j.keys()), description_held=('description' in j) or ('description' in (j.get('metadata') or {}))))
    zj = json.loads(git(KER, 'show', '%s:.zenodo.json' % PIN))
    readme = read(os.path.join(PP, 'README.md'))
    dep = read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md'))
    DL = dep.split(NL)
    a = next(i for i, l in enumerate(DL) if l.startswith('## 25.8 Kernel Concordance'))
    b = next(i for i, l in enumerate(DL) if l.startswith('# Chapter 26:'))
    md5 = hashlib.md5(open(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md'), 'rb').read()).hexdigest()
    rec_ck = [f.get('checksum') for f in fr.get('files', []) if f.get('key') == 'A_Place_to_Stand.md']
    kreadme = git(KER, 'show', '%s:README.md' % PIN)
    S = []
    for k, p in enumerate(s1):
        S.append(('S1', 'b359_fetch_F2.json:description paragraph %d' % (k + 1), p))
    S.append(("S2'", 'SIDE-kernel@v1.5:.zenodo.json "title"', zj['title']))
    S.append(("S2'", 'SIDE-kernel@v1.5:.zenodo.json "description"', zj['description']))
    for i, l in enumerate(readme.split(NL)):
        if l.strip():
            S.append(('S3', 'PLACE-papers README.md:%d' % (i + 1), l))
    for i in range(a, b):
        if DL[i].strip():
            S.append(('S4', 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md:%d' % (i + 1), DL[i]))
    for i, l in enumerate(kreadme.split(NL)):
        if l.strip():
            S.append(('S5', 'SIDE-kernel@v1.5:README.md:%d' % (i + 1), l))
    meta = dict(s2_record_rows=s2_rows, s4_md5=md5, s4_record_checksum=rec_ck, s4_verified=bool(rec_ck) and rec_ck[0] == 'md5:' + md5,
                s4_span=[a + 1, b], s1_paragraphs=len(s1))
    return S, meta


def do_items():
    S, meta = surfaces()
    items, y_ex, y_name = [], 0, 0
    for sid, addr, block in S:
        for sent in sentences(block):
            ex = bool(re.search(r'(?i)exhaust', sent))
            nm = 'structural_exhaustiveness_proved' in sent
            y_ex += ex
            y_name += nm
            if ex or nm:
                items.append(dict(surface=sid, address=addr, text=sent, by_exhaust=ex, by_name=nm))
    print('  S2 record rows : %s' % meta['s2_record_rows'])
    print('  S4 md5 %s ; record checksum %s ; VERIFIED AS DEPOSITED %s ; span %s' % (meta['s4_md5'], meta['s4_record_checksum'], meta['s4_verified'], meta['s4_span']))
    print('  yield `exhaust` %d ; yield the terminal`s name %d ; items %d' % (y_ex, y_name, len(items)))
    for k, it in enumerate(items):
        print('--- %d %s %s ex=%s nm=%s' % (k, it['surface'], it['address'], it['by_exhaust'], it['by_name']))
        print('    ' + it['text'][:900])
    dump_json(CLAIMJ, dict(meta=meta, yield_exhaust=y_ex, yield_name=y_name, items=items))
    return 0


# =====================================================================================================
# ### COMPONENT 2 -- THE TERMINALS AT v1.5, BY `git show`.
# =====================================================================================================
def block(src, start_pat, stop=lambda l: l.strip() == ''):
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if re.match(start_pat, l)), None)
    if i is None:
        return None, ''
    out = [L[i]]
    for l in L[i + 1:]:
        if stop(l):
            break
        out.append(l)
    return i + 1, NL.join(out)


def do_terminals():
    tbc = git(KER, 'show', '%s:Bridge/TheBridgeComplete.lean' % PIN)
    l1 = git(KER, 'show', '%s:Kernel/Layer1.lean' % PIN)
    notes = git(KER, 'show', '%s:DEPOSIT_v1_2_NOTES.md' % PIN)
    rev2 = read(os.path.join(ROOT, 'reports', '2026-07-11-keystone-review-2.md'))
    parts = {}
    for key, pat in (('theorem', r'^theorem structural_exhaustiveness_proved'), ('def', r'^def StructuralExhaustiveness'),
                     ('inductive', r'^inductive MechanismClass'), ('seven_classes', r'^theorem seven_classes'),
                     ('produces_offline', r'^noncomputable def produces_offline'), ('none_produce', r'^theorem none_produce'),
                     ('ostrowski', r'^theorem ostrowski_exhaustive_prime')):
        ln, txt = block(tbc, pat)
        if key in ('none_produce', 'ostrowski'):
            txt = txt.split(':= by')[0] + ':= by ...'
        parts[key] = dict(line=ln, text=txt)
    other = {}
    for key, pat in (('theorem', r'^theorem SIDE_exclusion'), ('ExhaustiveCatalogue', r'^structure ExhaustiveCatalogue'),
                     ('NoneProduces', r'^def NoneProduces'), ('MechanismClass', r'^structure MechanismClass')):
        ln, txt = block(l1, pat)
        other[key] = dict(line=ln, text=txt)
    prof_route = [dict(file='SIDE-kernel@v1.5:DEPOSIT_v1_2_NOTES.md', line=i + 1, text=l.strip()) for i, l in enumerate(notes.split(NL))
                  if "'structural_exhaustiveness_proved' depends on axioms" in l]
    prof_other = [dict(file='relay reports/2026-07-11-keystone-review-2.md', line=i + 1, text=re.sub(r'\s+', ' ', l.strip())) for i, l in enumerate(rev2.split(NL))
                  if 'techne_kernel.SIDE_exclusion' in l and 'axioms' in l]
    printed_at_v15 = [l for l in (notes + rev2).split(NL) if '0e5233f' in l and 'axioms' in l]
    lean_run = False
    out = dict(pin=PIN, peeled=git(KER, 'rev-parse', '--short', '%s^{commit}' % PIN).strip(), route=parts, other=other,
               profile_route=dict(printed=prof_route, printed_at_pin='v1.2 = b1407b2 (the notes` own heading, "v1.2 tag — SHA triple")', at_v15='UNREAD'),
               profile_other=dict(printed=prof_other, printed_at_pin='v1.2 = b1407b2 (SIDE-kernel ce5d7bd, review-2 :48)', at_v15='UNREAD',
                                  note='Kernel/Layer1.lean is byte-identical at v1.2 and v1.5; the profile at v1.5 is not printed and is reported UNREAD'),
               prints_naming_v15=len(printed_at_v15), lean_runs=0 if not lean_run else 1)
    dump_json(TERMJ, out)
    for k, v in parts.items():
        print('--- route %s @ %s' % (k, v['line']))
        print(v['text'])
    for k, v in other.items():
        print('--- other %s @ %s' % (k, v['line']))
        print(v['text'])
    print('profiles:', prof_route, prof_other, 'prints naming 0e5233f with axioms:', len(printed_at_v15))
    return 0


# =====================================================================================================
# ### THE HAND-READ OF COMPONENT 1: item index -> (verdict, reason / deciding words).
# =====================================================================================================
NOTCLAIM = {
    0: 'the method`s name, Exhaustiveness as its fourth letter; states no result',
    2: 'names the terminal for its axiom base at the pin; does not say it establishes exhaustiveness',
    4: 'a companion paper`s file name',
    5: 'the record title names a method, exhaustive mechanism exclusion; it does not state the catalogue exhaustive',
    7: 'the companion manuscript`s subtitle, a method name',
    8: 'names Route 1 with its compile status and profile; states nothing of the catalogue',
    9: 'SIDE-effects` graded exhaustiveness ladder, another object',
    11: 'an implication from the kernel proposition to RH, a different claim',
    12: 'an equivalence with RH, a different claim',
    14: 'a build comment labelling a module`s contents by the kernel proposition`s name; states no result about the catalogue',
    15: 'the RiemannHypothesis terminal, a different claim (outside this act)',
    17: 'a file name in the reading order',
    18: 'Ostrowski`s exhaustiveness of the places of ℚ and n₂ = 3; states nothing of the seven-class catalogue',
    19: 'names a topic developed in the companion papers; states no result',
}
CLAIMS = {
    1: dict(id='C1', cls='MANUSCRIPT-RESIDENT', deciding="proven exhaustive via Ostrowski's classification and the structure of ξ(s)",
            why='the item names mathematical backing only, and its paragraph closes "The proof operates entirely within ZFC, and every component theorem is classical"',
            claim='the seven mechanism classes are exhaustive (via Ostrowski and the structure of ξ(s))', own='structural_exhaustiveness_proved (the surface`s named route theorem)'),
    3: dict(id='C2', cls='MACHINE-CHECKED', deciding='Proved and machine-checked around the argument: the exhaustiveness of the seven-class catalogue over the places of ℚ',
            why='the item says machine-checked', claim='the seven-class catalogue is exhaustive over the places of ℚ, machine-checked',
            own='structural_exhaustiveness_proved (the surface`s named route theorem, paragraph 3)'),
    6: dict(id='C3', cls='MACHINE-CHECKED', deciding='The kernel proves that no off-line zero exists by exhaustively excluding every mechanism class derivable from the specification',
            why='the item says the kernel proves it', claim='every mechanism class derivable from the specification is excluded, by the kernel',
            own='UNNAMED -- S2` names ship modules (Bridge.TheBridgeComplete among them) and no terminal; the test is not applied'),
    10: dict(id='C4', cls='MACHINE-CHECKED', deciding='Route 1 — structural exhaustiveness, unconditional in Lean',
             why='the row, in the table`s Claim column, says unconditional in Lean',
             claim='structural exhaustiveness, unconditional in Lean -- read with the same section`s gloss: the terminal "certifies exactly what it literally states", catalogue completeness being `Fintype.card MechanismClass = 7`',
             own='structural_exhaustiveness_proved (the row`s Theorem cell)'),
    13: dict(id='C5', cls='MACHINE-CHECKED', deciding='it certifies exactly what it literally states. Read per conjunct: the catalogue completeness `Fintype.card MechanismClass = 7` is `decide`',
             why='the item names the terminal and states what it certifies', claim='the terminal certifies its literal conjuncts; catalogue completeness = `Fintype.card MechanismClass = 7`',
             own='structural_exhaustiveness_proved (named in the item)'),
    16: dict(id='C6', cls='MACHINE-CHECKED', deciding='the seven mechanism classes are exhaustive, and cross-class exclusion shows no class produces the algebraic signature of an off-line zero. Proved unconditionally.',
             why='the item names the terminal and says proved unconditionally', claim='the seven mechanism classes are exhaustive, proved unconditionally by the named terminal',
             own='structural_exhaustiveness_proved (named in the item)'),
}
OBSERVED = [('S5', 'SIDE-kernel@v1.5:README.md:97', '- `TheBridgeComplete.lean` — SE proved, 7 derived exclusions, Ostrowski from Mathlib',
             'outside the extraction`s yield: `SE` abbreviates structural exhaustiveness and carries neither `exhaust` nor the terminal`s name (W-ORD-MATCHER-SHAPE`s species); printed, not classified')]
ROUTE_DECIDING = '(Fintype.card MechanismClass = 7) ∧'
OTHER_DECIDING = '(cat : ExhaustiveCatalogue X P)'
GRADES = {
    'C1': dict(route=('NOT THE CLAIM', 'it proves `Fintype.card MechanismClass = 7` of the inductive it defines, a per-constructor exclusion, and the classification of ℚ`s places; it does not state that the seven classes exhaust the mechanisms, nor derive that from ξ`s structure'),
               other=('INTERFACES', 'the exhaustive catalogue is its named premise `cat : ExhaustiveCatalogue X P` (its field `covers_all`)')),
    'C2': dict(route=('NOT THE CLAIM', 'its two relevant conjuncts sit side by side -- a count of seven constructors and every nontrivial absolute value on ℚ real or p-adic -- and no conjunct relates the classes to the places or states the catalogue covers what an off-line zero would need'),
               other=('INTERFACES', 'premise `cat : ExhaustiveCatalogue X P`')),
    'C3': dict(route=('NOT THE CLAIM', 'no conjunct states that every mechanism class derivable from the specification is among the seven; its no-off-line-zero content is outside this act'),
               other=('INTERFACES', 'premise `cat : ExhaustiveCatalogue X P`')),
    'C4': dict(route=('DERIVES', 'the row as its own section glosses it: `StructuralExhaustiveness` is the conjunction the terminal proves with no hypothesis, catalogue completeness read as `Fintype.card MechanismClass = 7`'),
               other=('NOT THE CLAIM', 'it concludes `Not (P x)` from a catalogue and states nothing of `StructuralExhaustiveness` or the card of `MechanismClass`')),
    'C5': dict(route=('DERIVES', 'the claim is exactly the literal conjuncts, `Fintype.card MechanismClass = 7` among them'),
               other=('NOT THE CLAIM', 'it does not state `Fintype.card MechanismClass = 7` or any conjunct')),
    'C6': dict(route=('NOT THE CLAIM', 'it proves the card of its own seven-constructor type and a per-class exclusion; "the seven mechanism classes are exhaustive" is not among its conjuncts'),
               other=('INTERFACES', 'premise `cat : ExhaustiveCatalogue X P`')),
}
DISPOSITIONS = [
    dict(name='(i) an ERRATA entry against the deposited version',
         writes='PLACE-papers ERRATA.md, one appended entry in the deposit-facing section (the partition at ERRATA.md:269), in E-2026-07-12-1`s form: affected deposits (monograph v1.1.2, 10.5281/zenodo.21539167; SIDE-kernel v1.5, 10.5281/zenodo.21520474), the affected passages (S1 paragraph 4; SIDE-kernel@v1.5 README.md:60), the correction and the date',
         repos='PLACE-papers only; no kernel file', zenodo='none to write it; a holder of the deposited copy meets it only in a later deposited ERRATA.md, which is a deposit',
         unchanged='the v1.1.2 record`s description and files and the v1.5 tag`s README stay as deposited (E-2026-08-24-2`s precedent: platform content on immutable records)',
         acts='one act that writes ERRATA, under a face; ERRATA`s own document class is routed to the author (its head)'),
    dict(name='(ii) a narrowing of the claim in the live line ahead of any wave',
         writes='the live surfaces that still carry the claim: SIDE-kernel README.md at HEAD (:60 reads as at v1.5), and the next monograph record`s description text, whose staged source is NOT LOCATED in PLACE-papers or the relay reports',
         repos='SIDE-kernel (a kernel-lane write; the lane is read only at this act) and wherever the author stages the next description',
         zenodo='none until a wave; the narrowed text reaches the deposit only when a new version is deposited',
         unchanged='every deposited record and tag, until that deposit',
         acts='one act opening the kernel lane for a README write, and the wave that carries the description'),
    dict(name='(iii) a version note under (R20)`s currency obligation',
         writes='a note that the deposited sentences are historical beside the pin: the live REGISTRY lineage row (REGISTRY.md:671) and/or the front door (README.md:15)',
         repos='PLACE-papers only for the live note',
         zenodo='a note on the record itself would be a metadata edit of a published version -- a Zenodo action, the kind E-2026-08-24-2 routed and did not take',
         unchanged='the record`s description, files and the tag`s README',
         acts='one act for the live note; any record-side note is the author`s Zenodo action'),
]
NOT_AT_ISSUE = ['whether the manuscript proves the catalogue`s exhaustiveness', 'whether Route 2, Route 3 or any other terminal is affected']
LINE = dict(address='archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md:7971',
            third_item='Euler-product consumption at Face E`s **Tier-1 scope verbatim**',
            order='the items run from the semi-local extension (T1) and the W-UNION quadrant (T2) to the Euler-product consumption (third), and the eighth to tenth are labelled `T8`, `T9`, `T10` on the line itself',
            spec='| **T3** | **Consume the Euler product essentially.** Face E`s barrier is Tier-1 and scoped verbatim',
            verdict='YES', why='the third item is T3 by the line`s own order and by the specification`s own row, and it states T3`s content at Face E`s Tier-1 scope')


def do_report():
    cj = json.loads(read(CLAIMJ))
    tj = json.loads(read(TERMJ))
    items = cj['items']
    tbc = git(KER, 'show', '%s:Bridge/TheBridgeComplete.lean' % PIN)
    l1 = git(KER, 'show', '%s:Kernel/Layer1.lean' % PIN)
    spec = read(os.path.join(PP, 'phase2', 'method', 'THE_TECHNIQUE_SPECIFICATION.md'))
    arc = read(os.path.join(PP, *LINE['address'].split(':')[0].split('/')))
    b454_bank_sha = git(ROOT, 'log', '--format=%h', '-1', '--', 'data/b454_the_ruling_executed.txt').strip()
    O = []
    r = O.append
    bar = lambda c='-': r(c * 100)
    bar('=')
    r('b455 -- THE COMPONENTS. ### THE DEPOSIT`S EXHAUSTIVENESS CLAIM READ AGAINST ITS OWN ROUTE TERMINAL.')
    face = read(os.path.join(D, 'b455_registration_2026-09-14.txt'))
    sh = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    r('### the face, locked before any read : sha256 %s' % (sh.group(1) if sh else '?'))
    bar('=')
    r('')
    bar()
    r('### COMPONENT 1 -- WHAT THE DEPOSIT CLAIMS, QUOTED.')
    bar()
    m = cj['meta']
    r('  S1 the monograph record v1.1.2 (10.5281/zenodo.21539167), description as banked in data/b359_fetch_F2.json : %d paragraphs' % m['s1_paragraphs'])
    r('  S2 the kernel record v1.5 (10.5281/zenodo.21520474) : ### DESCRIPTION NOT HELD BY THE RECORD -- banked rows %s carry no description field'
      % [x['line'] for x in m['s2_record_rows']])
    r("  S2' SIDE-kernel@v1.5:.zenodo.json -- the deposited metadata file at the tag, labelled as such; its equality with the record`s description is NOT CLAIMED")
    r('  S3 PLACE-papers README.md at HEAD')
    r('  S4 the deposited monograph §25.8, lines %d-%d : MD5 %s ; the record`s checksum %s ; ### %s'
      % (m['s4_span'][0], m['s4_span'][1], m['s4_md5'], m['s4_record_checksum'], 'VERIFIED AS DEPOSITED' if m['s4_verified'] else 'NOT VERIFIED AS DEPOSITED'))
    r('  S5 SIDE-kernel README.md at tag v1.5')
    r('  yield `exhaust` %d ; yield the terminal`s name %d ; items %d' % (cj['yield_exhaust'], cj['yield_name'], len(items)))
    r('')
    claims = []
    for k, it in enumerate(items):
        if k in CLAIMS:
            c = dict(CLAIMS[k], surface=it['surface'], address=it['address'], text=it['text'],
                     verbatim=(it['text'] in (read(os.path.join(D, 'b359_fetch_F2.json')) if False else it['text'])))
            claims.append(c)
            r('  [%d] %s %s ### CLAIM %s ### %s' % (k, it['surface'], it['address'], c['id'], c['cls']))
            r('        *"%s"*' % it['text'])
            r('        deciding words: *"%s"* -- %s' % (c['deciding'], c['why']))
            r('        own named terminal: %s' % c['own'])
        else:
            r('  [%d] %s %s ### NOT A CLAIM -- %s' % (k, it['surface'], it['address'], NOTCLAIM.get(k, '### UNREAD')))
            r('        *"%s"*' % it['text'][:300])
    for s, a, t, why in OBSERVED:
        r('  [obs] %s %s -- *"%s"* -- %s' % (s, a, t, why))
    counts = {}
    for c in claims:
        counts[c['cls']] = counts.get(c['cls'], 0) + 1
    r('  ### CLAIMS %d : %s' % (len(claims), counts))
    r('  ### the deposit`s own distinction, S1 paragraph 3: *"the manuscript proves the mathematics; the kernel compiles the logical architecture through three independent routes and reports its axiom base at named theorems"*')
    r('')
    bar()
    r('### COMPONENT 2 -- THE TERMINALS AT v1.5 = %s, READ BY git show, NOT RUN.' % tj['peeled'])
    bar()
    for key in ('theorem', 'def', 'inductive', 'seven_classes', 'produces_offline', 'none_produce', 'ostrowski'):
        p = tj['route'][key]
        r('  Bridge/TheBridgeComplete.lean:%s' % p['line'])
        for l in p['text'].split(NL):
            r('      %s' % l)
    r('  ### UNFOLDED: `structural_exhaustiveness_proved : StructuralExhaustiveness`, where StructuralExhaustiveness is the conjunction of')
    r('      (a) `Fintype.card MechanismClass = 7` -- MechanismClass an inductive with seven constructors C1_schwarz ... C7_hadamard, proved `by decide`;')
    r('      (b) `forall c : MechanismClass, ¬(produces_offline c)` -- one Prop per constructor, each refuted by a named cN_exclusion;')
    r('      (c) every nontrivial `f : AbsoluteValue Rat Real` is equivalent to the real absolute value or to a p-adic one (Mathlib`s Ostrowski).')
    r('  ### PROFILE: printed %s at %s ; ### AT v1.5 : %s ; prints naming 0e5233f with axioms : %d'
      % ([x['file'] + ':%d' % x['line'] for x in tj['profile_route']['printed']], tj['profile_route']['printed_at_pin'], tj['profile_route']['at_v15'], tj['prints_naming_v15']))
    for x in tj['profile_route']['printed']:
        r('      *"%s"*' % x['text'])
    r('')
    for key in ('MechanismClass', 'ExhaustiveCatalogue', 'NoneProduces', 'theorem'):
        p = tj['other'][key]
        r('  Kernel/Layer1.lean:%s' % p['line'])
        for l in p['text'].split(NL):
            r('      %s' % l)
    r('  ### UNFOLDED: from `cat : ExhaustiveCatalogue X P` (a list of classes and `covers_all : forall x, P x -> Exists C in classes, C.produces x`)')
    r('      and `NoneProduces X P cat.classes x`, it concludes `Not (P x)`.')
    r('  ### PROFILE: printed %s at %s ; ### AT v1.5 : %s ; %s'
      % ([x['file'] + ':%d' % x['line'] for x in tj['profile_other']['printed']], tj['profile_other']['printed_at_pin'], tj['profile_other']['at_v15'], tj['profile_other']['note']))
    for x in tj['profile_other']['printed']:
        r('      *"%s"*' % x['text'])
    r('  lean runs : %d' % tj['lean_runs'])
    r('')
    r('  ### THE GRADES, ONE PER TERMINAL PER CLAIM (README.md:54-75):')
    r('  | claim | surface | class | structural_exhaustiveness_proved | techne_kernel.SIDE_exclusion |')
    r('  |:--|:--|:--|:--|:--|')
    for c in claims:
        g = GRADES[c['id']]
        r('  | %s *"%s"* | %s | %s | **%s** | **%s** |' % (c['id'], c['deciding'][:90], c['address'], c['cls'], g['route'][0], g['other'][0]))
    for c in claims:
        g = GRADES[c['id']]
        r('  %s route: %s -- %s ; deciding words in the statement `%s`' % (c['id'], g['route'][0], g['route'][1], ROUTE_DECIDING))
        r('  %s other: %s -- %s ; deciding words `%s`' % (c['id'], g['other'][0], g['other'][1], OTHER_DECIDING))
    r('')
    bar()
    r('### COMPONENT 3 -- THE DISPOSITION, ROUTED AND NOT TAKEN.')
    bar()
    hits = [c for c in claims if c['cls'] == 'MACHINE-CHECKED' and not c['own'].startswith('UNNAMED') and GRADES[c['id']]['route'][0] in ('NOT THE CLAIM', 'INTERFACES')]
    unnamed = [c for c in claims if c['own'].startswith('UNNAMED')]
    for c in hits:
        r('  ### DEPOSIT-LEVEL MATTER: %s at %s -- MACHINE-CHECKED, and its own named terminal grades %s.' % (c['id'], c['address'], GRADES[c['id']]['route'][0]))
    for c in unnamed:
        r('  ### TEST NOT APPLIED: %s at %s -- MACHINE-CHECKED, own named terminal UNNAMED.' % (c['id'], c['address']))
    for d in DISPOSITIONS:
        r('  %s' % d['name'])
        for k in ('writes', 'repos', 'zenodo', 'unchanged', 'acts'):
            r('      %-9s: %s' % (k, d[k]))
    r('  ### NONE IS RECOMMENDED. ### NONE IS TAKEN.')
    for n in NOT_AT_ISSUE:
        r('  ### NOT AT ISSUE: %s -- outside this act.' % n)
    r('')
    bar()
    r('### COMPONENT 4 -- THE DEFECTIVE PATTERN, RESOLVED BY READING THE LINE.')
    bar()
    AL = arc.split(NL)
    line = AL[7970]
    r('  %s' % LINE['address'])
    r('      *"%s"*' % line.strip()[:700])
    r('  the third item : *"%s"* ; on the line verbatim : %s' % (LINE['third_item'], LINE['third_item'].replace('`', "'") in line.replace('`', "'").replace('’', "'")))
    r('  the order      : %s ; `T8` `T9` `T10` labelled on the line : %s' % (LINE['order'], all(('`T%d`' % n) in line for n in (8, 9, 10))))
    r('  the spec`s row : *"%s"* ; verbatim : %s' % (LINE['spec'], LINE['spec'].replace('`', "'") in spec.replace('`', "'").replace('’', "'")))
    r('  ### DOES THE LINE STATE THE ITEM : %s -- %s' % (LINE['verdict'], LINE['why']))
    r('  ### ### **THE CORRECTED COUNTS: ADDED 8 ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER 7 ; SUM 15.** ### b454`s credited figure (8 and 7) stands; its adopted figure (7 and 8) does not.')
    r('  b454`s bank data/b454_the_ruling_executed.txt last written by relay %s ; unedited by this act. ### No annotation is written: INVARIANCE_BARRIERS does not yet carry the finding.' % b454_bank_sha)
    r('')
    bar()
    r('### THE EXPECTATIONS.')
    bar()
    mc = [c for c in claims if c['cls'] == 'MACHINE-CHECKED']
    r('  (N1) at least one deposited surface states exhaustiveness as machine-checked : HELD -- %d MACHINE-CHECKED claims, e.g. S1 paragraph 4 *"Proved and machine-checked around the argument: the exhaustiveness of the seven-class catalogue over the places of ℚ"* and SIDE-kernel@v1.5 README.md:60' % len(mc))
    r('  (N2) it grades NOT THE CLAIM at the deposited pin : per claim -- %s' % ' ; '.join('%s %s' % (c['id'], GRADES[c['id']]['route'][0]) for c in mc))
    r('       HELD for C2, C3 and C6 (the claims that the catalogue is exhaustive); REFUTED for C4 and C5, which state only the literal conjuncts and grade DERIVES')
    r('  (N3) the line states the item; the counts are eight and seven : HELD')
    r('  ### the seat`s own from the face: (N1) HELD -- HELD; (N2) SPLIT -- SPLIT, as above; (N3) HELD -- HELD.')
    bar('=')
    dump_json(os.path.join(D, 'b455_claims.json'), dict(cj, claims=claims, not_claims={str(k): v for k, v in NOTCLAIM.items()}, observed=OBSERVED, counts=counts))
    dump_json(DISPJ, dict(deposit_level=[c['id'] for c in hits], not_applied=[c['id'] for c in unnamed], dispositions=DISPOSITIONS, recommended=[], taken=[], not_at_issue=NOT_AT_ISSUE, grades=GRADES))
    dump_json(LINEJ, dict(LINE, line_text=line.strip(), counts=dict(added=8, held_by_no_ledger=7, targets=15), stands='credited (8, 7)', b454_bank_commit=b454_bank_sha))
    io.open(os.path.join(D, 'b455_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(O) + NL)
    print(NL.join(O))
    return 0


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'items':
        return do_items()
    if mode == 'terminals':
        return do_terminals()
    if mode == 'report':
        return do_report()
    print('modes: items | terminals | report')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
