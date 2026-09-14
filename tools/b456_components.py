# -*- coding: utf-8 -*-
"""b456_components.py -- THE ERRATA ENTRY, THE LIVE NOTE, THE PROFILE AT THE TAG, AND THE ROUTED ITEMS.

### ### **EVERY RULE IS THE LOCKED FACE'S** (`data/b456_registration_2026-09-14.txt`). ### Modes: `plan` (every write
### computed and checked, nothing written; the profile search run); `write` (the corpus writes, each diff counted);
### `report` (the record). ### **READ ONLY TOWARD EVERY KERNEL: `git show` / `git grep` only; NO `lean`, NO `lake`.**
"""
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
WRITESJ = os.path.join(D, 'b456_writes.json')
PROFJ = os.path.join(D, 'b456_profile.json')
NL = chr(10)
TODAY = '2026-09-14'
ARCREL = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rawread(p):
    with open(p, 'rb') as fh:
        return fh.read().decode('utf-8')


def norm(t):
    return t.replace(chr(13) + NL, NL)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def dump_json(path, obj):
    data = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)


def pp(rel):
    return os.path.join(PP, *rel.split('/'))


def put(rel, text_lf, crlf):
    data = (text_lf.replace(NL, chr(13) + NL) if crlf else text_lf).encode('utf-8')
    open(pp(rel) + '.tmp', 'wb').write(data)
    os.replace(pp(rel) + '.tmp', pp(rel))


# =====================================================================================================
# ### COMPONENT 1 -- THE ENTRY.
# =====================================================================================================
S1_QUOTE = 'Proved and machine-checked around the argument: the exhaustiveness of the seven-class catalogue over the places of ℚ'
S5_QUOTE = ('`structural_exhaustiveness_proved` in `Bridge/TheBridgeComplete.lean` — the seven mechanism classes are exhaustive, and cross-class '
            'exclusion shows no class produces the algebraic signature of an off-line zero. Proved unconditionally.')
S4_QUOTE = 'it certifies exactly what it literally states. Read per conjunct: the catalogue completeness `Fintype.card MechanismClass = 7` is `decide`'
S4_ROW = 'Route 1 — structural exhaustiveness, unconditional in Lean'
ENTRY = [
    '<!-- b456 -->',
    '',
    '## E-2026-09-14-1 — The deposited descriptions say the seven-class catalogue’s exhaustiveness is machine-checked; its route terminal states something narrower (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5)',
    '',
    '**Filed 2026-09-14 (b456), on the author’s ruling (R65), from the reading banked at b455 (relay `data/b455_the_claim_and_its_terminal.txt`).',
    '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.',
    '### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**',
    '',
    '**Affected deposits.** *A Place to Stand*, Zenodo version v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — the record description; and SIDE-kernel v1.5, tag `v1.5` = commit `0e5233f` ([10.5281/zenodo.21520474](https://doi.org/10.5281/zenodo.21520474)) — the `README.md` shipped at the tag.',
    '',
    '**What the deposited words say.** The record description, in the paragraph headed *“What the manuscript establishes, and what it names as open”*, says: *“' + S1_QUOTE + '”*. The kernel README at the tag, in its list of load-bearing theorems, says: *“' + S5_QUOTE + '”*',
    '',
    '**What the route terminal states.** At `0e5233f`, `structural_exhaustiveness_proved` proves the proposition `StructuralExhaustiveness`, and that proposition is a conjunction. Its opening conjunct says that `MechanismClass` — an inductive type the same file defines, with seven constructors — has cardinality seven, `Fintype.card MechanismClass = 7`, closed by `decide`. The next says that for each of those constructors a proposition the file also defines, `produces_offline`, is false. Its last says that every nontrivial absolute value on ℚ is equivalent to the real absolute value or to a p-adic absolute value, which is Mathlib’s Ostrowski theorem. The theorem is sound and carries no hypothesis. None of its conjuncts says that the seven classes exhaust the mechanisms from which an off-line zero could arise, and none relates the classes to the places of ℚ: the count and the classification of the places stand side by side.',
    '',
    '**Why they differ.** The description writes about what the kernel checked in the manuscript’s vocabulary. In the manuscript, *the exhaustiveness of the seven-class catalogue* names a theorem about mathematics: that the catalogue covers every mechanism. In the kernel, the same words name a Lean proposition whose catalogue conjunct is the cardinality of a type the kernel itself defines. So the sentence carries both registers together. *Proved* is the manuscript’s word for the manuscript’s theorem; *machine-checked* is true of the kernel’s proposition. The sentence joins them as if the machine had checked the manuscript’s theorem. The README’s headline does the same inside its own clause. Read against these deposited words — a grade being a relation between a terminal and the claim made for it — the terminal is `NOT THE CLAIM`: sound, and strictly weaker than what the words say.',
    '',
    '**Where the deposit is precise.** The deposited monograph’s own concordance, §25.8, reads the route exactly. Its note on the route says *“' + S4_QUOTE + '”*: it reads completeness as the cardinality of the mechanism type. Against that reading the same terminal `DERIVES`, and the concordance’s table row, *“' + S4_ROW + '”*, stands as written. **This entry corrects nothing in the monograph.**',
    '',
    '**The correction, as a reading.** Where the record description and the kernel README at `v1.5` say the catalogue’s exhaustiveness is proved and machine-checked, read: *the Lean terminal `structural_exhaustiveness_proved` proves that the kernel’s mechanism type has seven members, that none of them produces the off-line signature the kernel defines, and Ostrowski’s classification of the places of ℚ; that the seven classes exhaust the mechanisms is the manuscript’s theorem, and the kernel does not check it.*',
    '',
    '**What is not corrected.** Whether the manuscript proves the catalogue’s exhaustiveness is untouched by this entry. So are every other route terminal, every grade on any row, and every figure. The deposited sentences about the route terminals’ axiom profiles are a separate matter, routed by b456 and not recorded here.',
    '',
    '**Status.** Retained at monograph v1.1.2 and SIDE-kernel v1.5, and never restated to a later line. Under (R65) the narrowing of these sentences in the live line waits on the wave, which is parked, and no Zenodo metadata is edited. A live note under (R20) beside the pin points here: in `REGISTRY.md`, after the deposit-pin table, and in `README.md`, beside the kernel line.',
    '',
    '*Filed by b456 (relay `data/b456_the_errata_and_the_note.txt`). No deposited artifact is altered.*',
    '',
    '---',
]
NOTE = ('(R20) note, b456, 2026-09-14: the route terminal `structural_exhaustiveness_proved` states that the kernel’s own mechanism type has seven '
        'members, that none of them produces the off-line signature the kernel defines, and Ostrowski’s classification of the places of ℚ, while the '
        'deposited descriptions — the monograph record v1.1.2 and the kernel README at `v1.5` — say the seven-class catalogue’s exhaustiveness is '
        'machine-checked; see `ERRATA.md`, E-2026-09-14-1.')
NUMWORDS = r'\b(one|two|three|four|five|six|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|twenty|thirty|hundred|thousand|first|second|third|fourth|fifth|sixth|eighth|ninth|tenth|single|double|triple|twice|once|dozen)\b'


def tally(text):
    t = re.sub(r'`[^`]*`', ' ', text)
    t = re.sub(r'\]\([^)]*\)', ']', t)
    t = re.sub(r'\*“[^”]*”\*', ' ', t)
    t = re.sub(r'\b10\.5281/zenodo\.\d+\b', ' ', t)
    t = re.sub(r'\bE-\d{4}-\d{2}-\d{2}-\d+\b', ' ', t)
    t = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', ' ', t)
    t = re.sub(r'\bv\d+(\.\d+)*\b', ' ', t)
    t = re.sub(r'\bb\d{3}\b', ' ', t)
    t = re.sub(r'\(R\d+\)', ' ', t)
    t = re.sub(r'§\d+(\.\d+)*', ' ', t)
    t = re.sub(r'<!--.*?-->', ' ', t)
    digits = re.findall(r'\d+', t)
    words = [w for w in re.findall(NUMWORDS, t, re.I) if w.lower() not in ('once',)] + re.findall(r'\bonce\b', t, re.I)
    # ### "one" inside "none"/"someone" is excluded by the word boundary; "single" and "once" count as tallies of occurrence.
    return digits, words


CONTENT = [
    ('a the affected deposits by DOI', lambda e: '10.5281/zenodo.21539167' in e and '10.5281/zenodo.21520474' in e),
    ('b the two deposited sentences verbatim', lambda e: S1_QUOTE in e and S5_QUOTE in e),
    ('c the terminal unfolded, conjunct by conjunct', lambda e: 'Fintype.card MechanismClass = 7' in e and '`produces_offline`' in e and 'Ostrowski theorem' in e and '0e5233f' in e),
    ('d the two registers', lambda e: 'the sentence carries both registers together' in e and 'manuscript’s vocabulary' in e),
    ('e §25.8 precise, quoted, DERIVES against it', lambda e: S4_QUOTE in e and 'reads completeness as the cardinality of the mechanism type' in e and '`DERIVES`' in e),
    ('f NOT THE CLAIM against the deposited words', lambda e: '`NOT THE CLAIM`' in e),
    ('g the correction as a reading', lambda e: '**The correction, as a reading.**' in e),
    ('h what is not corrected', lambda e: 'Whether the manuscript proves the catalogue’s exhaustiveness is untouched by this entry' in e),
    ('i status: retained, the wave under (R65), the note', lambda e: 'Retained at monograph v1.1.2 and SIDE-kernel v1.5' in e and '(R65)' in e and 'A live note under (R20)' in e),
    ('j no deposit action, nothing at Zenodo', lambda e: 'NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.' in e),
]


# =====================================================================================================
# ### COMPONENT 3 -- THE PROFILE.
# =====================================================================================================
ROUTES = ('structural_exhaustiveness_proved', 'SpectralCannonFull.spectral_cannon', 'ConservationBridge.riemann_hypothesis')
PRINT = re.compile(r"'(%s)' (depends on axioms|does not depend on any axioms)" % '|'.join(re.escape(r) for r in ROUTES))


def profile_search():
    out = dict(tag=[], elsewhere=[], elsewhere_scanned=[])
    for ln in git(KER, 'grep', '-n', '-I', '-E', r"depends on axioms|does not depend on any axioms", 'v1.5').splitlines():
        _t, f, n, txt = ln.split(':', 3)
        if PRINT.search(txt):
            blob = git(KER, 'show', 'v1.5:%s' % f).split(NL)
            heading = next((blob[k] for k in range(int(n) - 1, -1, -1) if blob[k].startswith('#')), '')
            out['tag'].append(dict(file=f, line=int(n), text=txt.strip(), heading=heading.strip(), printed_against_0e5233f='0e5233f' in NL.join(blob[max(0, int(n) - 30):int(n) + 5]) or 'v1.5' in heading))
    roots = [(os.path.join(ROOT, 'reports'), 'relay/reports'), (D, 'relay/data'), (PP, 'PLACE-papers'), (KER, 'SIDE-kernel working tree')]
    for root, label in roots:
        p = subprocess.run(['grep', '-rn', '-I', '-E', "'(structural_exhaustiveness_proved|SpectralCannonFull\\.spectral_cannon|ConservationBridge\\.riemann_hypothesis)' (depends on axioms|does not depend on any axioms)",
                            '--exclude-dir=.git', '--exclude-dir=.lake', '.'], cwd=root, capture_output=True, text=True, encoding='utf-8', errors='replace')
        out['elsewhere_scanned'].append(label)
        for ln in p.stdout.splitlines():
            f, n, txt = ln.split(':', 2)
            if re.search(r'b45[456]_', f):
                continue
            try:
                win = norm(rawread(os.path.join(root, f))).split(NL)
            except Exception:
                win = []
            i = int(n) - 1
            near = NL.join(win[max(0, i - 25):i + 25])
            out['elsewhere'].append(dict(where=label, file=f.lstrip('./'), line=int(n), text=txt.strip()[:160], names_0e5233f_or_v15_nearby=('0e5233f' in near or 'v1.5' in near)))
    art_tag = [x for x in out['tag'] if x['printed_against_0e5233f']]
    art_else = [x for x in out['elsewhere'] if x['names_0e5233f_or_v15_nearby'] and not x['where'].startswith('SIDE-kernel')]
    out['verdict'] = 'PRESENT' if art_tag else ('PRESENT ELSEWHERE' if art_else else 'ABSENT')
    out['statements'] = [
        dict(address='archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md:1690',
             words='`offLine_of_codim_two` profile `{propext, Classical.choice, Quot.sound}`, C₆-model neighbours unmoved', kind='a statement of a run, for a non-route terminal, receipt a check script'),
        dict(address=ARCREL + ':9145', words='verified unmoved at the deposit `v1.5` = `0e5233f`', kind='a statement that profiles were verified, with no output'),
        dict(address='PLACE-papers README.md:15', words='route terminals re-profiled clean at the v1.5 enactment', kind='the front door`s statement'),
        dict(address='data/b359_fetch_F2.json (monograph record v1.1.2, description)', words='All route terminals report {propext, Classical.choice, Quot.sound}', kind='the record`s statement'),
    ]
    out['disposition'] = dict(
        name='print and bank the route terminals` profiles at the tag',
        what='a kernel-lane act runs the tag`s own check scripts (AxiomCheck_*.lean) against a checkout of 0e5233f and banks the printed #print axioms output beside the pin',
        needs='a lane that permits a build and a lean run (this lane is read only); the tag`s README gives about five minutes with cached Mathlib and about two hours cold',
        zenodo='none to bank the output in the relay or PLACE-papers; to ship it inside the deposit needs a new kernel version, which is a deposit',
        unchanged='the tag, the records, and the front door`s and the record`s sentences until the output is read',
        taken=False)
    return out


# =====================================================================================================
# ### COMPONENT 4 -- THE ROUTED ITEMS.
# =====================================================================================================
def i1_block(arc_line):
    i = arc_line.find('Euler-product consumption at Face E')
    j = arc_line.find('verbatim**', i)
    words = arc_line[i:j + len('verbatim**')] if i >= 0 and j >= 0 else ''
    return words, NL.join(['', '<!-- b456 ERA ANNOTATION, %s -->' % TODAY, '',
                           '### ERA ANNOTATION (%s, b456) — bearing on the T3 Tier-1 scope' % TODAY, '',
                           '> %s' % words, '',
                           '*Provenance: `%s:7971`, a ledger line before b450 — the third item of its `T1`–`T10` list, and so `T3` by the line’s own order and by `THE_TECHNIQUE_SPECIFICATION.md:34`; decided at b455, added under `(R63)(b)` as amended by `(R64)(2)`. **This note states a later finding and edits no argument above it.** No claim in this document moves.*' % ARCREL, ''])


I3_OLD, I3_NEW = 'held-branch work', 'merged-branch work'


def i3_block(original):
    return NL.join(['', '<!-- b456 CURRENCY ANNOTATION, %s -->' % TODAY, '',
                    '#### **CURRENCY ANNOTATION** *(%s, b456; existing text preserved apart from the state term named here)*' % TODAY, '',
                    '> ### **1 LINE: A STATE TERM b454’S TABLE DID NOT NAME, ON A LINE `(R63)(a)` NAMED.** *The line as it stood, preserved verbatim:*', '',
                    '> - line `145` (`SIDE-lv-conservation` branch `word-pairing-interface`; fast-forward, tip `5a14205` on `main`’s first-parent line; state term `%s` → `%s`) — *%s*' % (I3_OLD, I3_NEW, original), '',
                    '> ### **WHY.** *`(R63)(a)`, as amended by `(R64)(1)`, named this line as calling a merged branch held; b454 changed the first such term on it and left this one, and b456 completes it. Only the state term changed; no line was removed; no grade, claim or correspondence row moved.*', ''])


def plan():
    W = {}
    # C1
    er_raw = rawread(pp('ERRATA.md'))
    er = norm(er_raw)
    entry = NL.join(ENTRY)
    digits, words = tally(entry)
    content = [(n, bool(f(entry))) for n, f in CONTENT]
    W['c1'] = dict(ok=(not digits and not words and all(v for _, v in content) and 'E-2026-09-14' not in er), digits=digits, words=words, content=content,
                   crlf=(chr(13) + NL) in er_raw, heading=ENTRY[2])
    # C2
    reg_raw, rd_raw = rawread(pp('REGISTRY.md')), rawread(pp('README.md'))
    RL, ML = norm(reg_raw).split(NL), norm(rd_raw).split(NL)
    reg_anchor = RL[677].startswith('| ### **relay formal modules, `W-ATTEMPT-2`**') and RL[678] == '' and RL[679].startswith('### **PHASE 1.2 — FROZEN**')
    rd_anchor = ML[14].startswith('**Kernel:** [SIDE-kernel](https://github.com/psinary-sketch/SIDE-kernel) — cited by named terminal') and ML[15].startswith('**Federation:**')
    W['c2'] = dict(note=NOTE, registry_anchor=reg_anchor, readme_anchor=rd_anchor, reg_crlf=(chr(13) + NL) in reg_raw, rd_crlf=(chr(13) + NL) in rd_raw,
                   one_sentence=NOTE.count('. ') == 0 and NOTE.endswith('.'), tally=tally(NOTE))
    # C4
    arc = norm(rawread(pp(ARCREL))).split(NL)
    words, blk = i1_block(arc[7970])
    inv_raw = rawread(pp('phase1.5/method/INVARIANCE_BARRIERS.md'))
    res_raw = rawread(pp('phase1.5/proofs/THE_RESIDUE_OF_RH.md'))
    RS = norm(res_raw).split(NL)
    l145 = RS[144]
    W['c4'] = dict(
        I1=dict(words=words, words_on_line=bool(words) and words in arc[7970], absent_before='bearing on the T3 Tier-1 scope' not in inv_raw, crlf=(chr(13) + NL) in inv_raw, verdict='COMPLETE'),
        I2=dict(address='phase1.5/method/EXHAUSTIVENESS_LICENSE.md:9', text=norm(rawread(pp('phase1.5/method/EXHAUSTIVENESS_LICENSE.md'))).split(NL)[8], verdict='LEFT',
                why='a state-term change on the head`s dated version line, which (R63)(a)`s eight lines did not name; it needs the author`s ruling, and the line records the state as of its own date'),
        I3=dict(parts=[dict(address='phase1.5/proofs/THE_RESIDUE_OF_RH.md:145', original=l145, ok=l145.count(I3_OLD) == 1 and '| ### **one cited pin fails** |' in l145, verdict='COMPLETE',
                            why='a line (R63)(a) named; its remaining state term, preserved in an appended currency annotation'),
                       dict(address='phase1.5/proofs/THE_RESIDUE_OF_RH.md:127-130', lines=RS[126:130], verdict='LEFT',
                            why='status cells reading HELD-BRANCH on lines (R63)(a)`s eight did not name; changing them changes state terms the author has not ruled')],
                crlf=(chr(13) + NL) in res_raw, verdict='PARTLY COMPLETED'),
    )
    W['c3'] = profile_search()
    return W, dict(er=er, RL=RL, ML=ML, blk=blk, RS=RS, inv=norm(inv_raw))


def removed_zero(pre, post, edited):
    pl = set(post.split(NL))
    return all(l in pl or (l in edited and l in post) for l in pre.split(NL))


def numstat(rel):
    o = git(PP, 'diff', '--numstat', '--', rel).strip()
    return o.split()[:2] if o else ['0', '0']


def do_write():
    W, X = plan()
    diffs = []
    if W['c1']['ok']:
        post = X['er'].rstrip(NL) + NL + NL + NL.join(ENTRY) + NL
        put('ERRATA.md', post, W['c1']['crlf'])
        diffs.append(dict(doc='ERRATA.md', removed_zero=removed_zero(X['er'], post, []), numstat=numstat('ERRATA.md')))
    else:
        print('  ### COMPONENT 1 HALTS: %s' % W['c1'])
    if W['c2']['registry_anchor']:
        RL = X['RL'][:678] + ['', NOTE] + X['RL'][678:]
        post = NL.join(RL)
        put('REGISTRY.md', post, W['c2']['reg_crlf'])
        diffs.append(dict(doc='REGISTRY.md', removed_zero=removed_zero(NL.join(X['RL']), post, []), numstat=numstat('REGISTRY.md')))
    if W['c2']['readme_anchor']:
        ML = X['ML'][:15] + [NOTE] + X['ML'][15:]
        post = NL.join(ML)
        put('README.md', post, W['c2']['rd_crlf'])
        diffs.append(dict(doc='README.md', removed_zero=removed_zero(NL.join(X['ML']), post, []), numstat=numstat('README.md')))
    i1 = W['c4']['I1']
    if i1['words_on_line'] and i1['absent_before']:
        post = X['inv'].rstrip(NL) + NL + X['blk'].rstrip(NL) + NL
        put('phase1.5/method/INVARIANCE_BARRIERS.md', post, i1['crlf'])
        diffs.append(dict(doc='phase1.5/method/INVARIANCE_BARRIERS.md', removed_zero=removed_zero(X['inv'], post, []), numstat=numstat('phase1.5/method/INVARIANCE_BARRIERS.md')))
    p145 = W['c4']['I3']['parts'][0]
    if p145['ok']:
        RS = list(X['RS'])
        RS[144] = p145['original'].replace(I3_OLD, I3_NEW)
        post = NL.join(RS).rstrip(NL) + NL + i3_block(p145['original']).rstrip(NL) + NL
        pre = NL.join(X['RS'])
        put('phase1.5/proofs/THE_RESIDUE_OF_RH.md', post, W['c4']['I3']['crlf'])
        diffs.append(dict(doc='phase1.5/proofs/THE_RESIDUE_OF_RH.md', removed_zero=removed_zero(pre, post, [p145['original']]), numstat=numstat('phase1.5/proofs/THE_RESIDUE_OF_RH.md')))
    W['diffs'] = diffs
    dump_json(WRITESJ, dict((k, v) for k, v in W.items() if k != 'c3'))
    dump_json(PROFJ, W['c3'])
    for d in diffs:
        print('  diff %-45s numstat +%s -%s removed-zero %s' % (d['doc'], d['numstat'][0], d['numstat'][1], d['removed_zero']))
    return 0


def do_plan():
    W, X = plan()
    print('  C1 ok %s digits %s words %s content %s' % (W['c1']['ok'], W['c1']['digits'], W['c1']['words'], W['c1']['content']))
    print('  C2 anchors registry %s readme %s ; one sentence %s ; note tally %s' % (W['c2']['registry_anchor'], W['c2']['readme_anchor'], W['c2']['one_sentence'], W['c2']['tally']))
    c3 = W['c3']
    print('  C3 verdict %s ; tag prints %s ; elsewhere hits %d ; with 0e5233f/v1.5 nearby %s' % (c3['verdict'], [(x['file'], x['line'], x['heading'], x['printed_against_0e5233f']) for x in c3['tag']],
                                                                                         len(c3['elsewhere']), [(x['where'], x['file'], x['line']) for x in c3['elsewhere'] if x['names_0e5233f_or_v15_nearby']]))
    print('  C4 I1 %s ; I3 145 ok %s' % ({k: v for k, v in W['c4']['I1'].items()}, W['c4']['I3']['parts'][0]['ok']))
    return 0


def do_report():
    W = json.loads(norm(rawread(WRITESJ)))
    P = json.loads(norm(rawread(PROFJ)))
    face = norm(rawread(os.path.join(D, 'b456_registration_2026-09-14.txt')))
    sh = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    O = []
    r = O.append
    bar = lambda c='-': r(c * 100)
    bar('=')
    r('b456 -- THE COMPONENTS. ### THE ERRATA ENTRY, THE LIVE NOTE, AND THE ROUTED ANNOTATIONS COMPLETED.')
    r('### the face, locked before any write : sha256 %s' % (sh.group(1) if sh else '?'))
    r('### RULING (R65), the author`s, ratified by the paste, entered: dispositions (i) and (iii), not (ii); no Zenodo metadata edited; nothing deposits.')
    bar('=')
    r('')
    bar()
    r('### COMPONENT 1 -- THE ERRATA ENTRY, AS WRITTEN (ERRATA.md, appended).')
    bar()
    c1 = W['c1']
    r('  tally rule: digits %s ; number words %s ; required content %s ; written %s' % (c1['digits'], c1['words'], ' '.join('%s=%s' % (n.split()[0], v) for n, v in c1['content']), c1['ok']))
    for l in ENTRY:
        r('    ' + l)
    r('')
    bar()
    r('### COMPONENT 2 -- THE LIVE NOTE UNDER (R20), INSERTED IN BOTH PLACES, NO EXISTING LINE CHANGED.')
    bar()
    c2 = W['c2']
    r('  REGISTRY.md: a blank line and the note after the deposit-pin table`s last row (was :678) ; anchor held %s' % c2['registry_anchor'])
    r('  README.md  : the note as a new line after the kernel line (:15), inside its paragraph ; anchor held %s' % c2['readme_anchor'])
    r('    ' + c2['note'])
    r('')
    bar()
    r('### COMPONENT 3 -- THE PROFILE AT THE DEPOSITED TAG.')
    bar()
    r('  the tag`s printed route-terminal profile lines (v1.5 = 0e5233f, git grep):')
    for x in P['tag']:
        r('    %s:%d | %s | under %r | printed against 0e5233f : %s' % (x['file'], x['line'], x['text'], x['heading'], x['printed_against_0e5233f']))
    r('  the check scripts at the tag are inputs (AxiomCheck_ROUTE1A_C6.lean, AxiomCheck_ROUTE1A_C7.lean, AxiomCheck_V3B.lean, AxiomCheck_v1_3.lean), not artefacts.')
    r('  elsewhere scanned: %s ; printed route-terminal profile lines found %d ; any beside 0e5233f or v1.5 : %s'
      % (', '.join(P['elsewhere_scanned']), len(P['elsewhere']), [(x['where'], x['file'], x['line']) for x in P['elsewhere'] if x['names_0e5233f_or_v15_nearby']]))
    for x in P['elsewhere']:
        r('    %s %s:%d | %s' % (x['where'], x['file'], x['line'], x['text'][:110]))
    r('  ### ### **VERDICT : %s**' % P['verdict'])
    r('  the statements, printed apart as statements and not as output:')
    for s_ in P['statements']:
        r('    %s -- *"%s"* -- %s' % (s_['address'], s_['words'], s_['kind']))
    if P['verdict'] == 'ABSENT':
        d = P['disposition']
        r('  ### SECOND DEPOSIT-LEVEL MATTER: the front door`s "re-profiled clean at the v1.5 enactment" and the record`s "All route terminals report')
        r('  ### {propext, Classical.choice, Quot.sound}" rest on a run whose output was not shipped at the tag or banked elsewhere.')
        r('  its disposition, priced and NOT TAKEN: %s -- %s ; needs: %s ; zenodo: %s ; unchanged: %s' % (d['name'], d['what'], d['needs'], d['zenodo'], d['unchanged']))
    r('  lean runs : 0')
    r('')
    bar()
    r('### COMPONENT 4 -- THE ROUTED ITEMS.')
    bar()
    c4 = W['c4']
    r('  COMPLETED:')
    r('    I1 INVARIANCE_BARRIERS -- the T3 Tier-1 scope: an era annotation appended, quoting *"%s"* from %s:7971 ; %s' % (c4['I1']['words'], ARCREL, c4['I1']['verdict']))
    p = c4['I3']['parts'][0]
    r('    I3 %s -- `%s` -> `%s`, the line as it stood preserved in an appended currency annotation ; %s (%s)' % (p['address'], I3_OLD, I3_NEW, p['verdict'], p['why']))
    r('  LEFT:')
    r('    I2 %s -- *"%s"* -- %s' % (c4['I2']['address'], c4['I2']['text'], c4['I2']['why']))
    q = c4['I3']['parts'][1]
    r('    I3 %s -- %s' % (q['address'], q['why']))
    for l in q['lines']:
        r('        %s' % l[:140])
    r('  ### BY ITEM: I1 COMPLETED ; I2 LEFT ; I3 PARTLY COMPLETED (:145 completed, :127-:130 left).')
    r('')
    bar()
    r('### EVERY WRITE, AS A DIFF COUNT.')
    bar()
    for d in W['diffs']:
        r('  %-45s numstat +%s -%s ; LINES REMOVED 0 BY b454`S PREDICATE : %s' % (d['doc'], d['numstat'][0], d['numstat'][1], d['removed_zero']))
    r('')
    bar()
    r('### THE EXPECTATIONS.')
    bar()
    r('  (N1) the profile artefact is ABSENT at the deposited tag : %s -- verdict %s' % ('HELD' if P['verdict'] == 'ABSENT' else 'REFUTED', P['verdict']))
    r('  (N2) two of the three routed annotations complete without a ruling : REFUTED -- one item completed whole (I1), one in part (I3, :145), one left (I2)')
    r('  ### the seat`s own from the face: (N1) HELD -- HELD; (N2) REFUTED AS STATED -- REFUTED.')
    r('  ### ENTERED AS THE SEAT`S: the spec carried from b455 kept the clause "annotations written by this act, cap 0", which the face`s reading (4)')
    r('  ### contradicts; the audit read it jointly satisfiable because the act`s other clauses do not reach it. The face governs; the stamped record is not re-run.')
    bar('=')
    io.open(os.path.join(D, 'b456_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(O) + NL)
    print(NL.join(O))
    return 0


def main(argv):
    mode = argv[0] if argv else ''
    if mode == 'plan':
        return do_plan()
    if mode == 'write':
        return do_write()
    if mode == 'report':
        return do_report()
    print('modes: plan | write | report')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
