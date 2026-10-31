# -*- coding: utf-8 -*-
"""b726, (R336)(5)-(6): THE FRONT-DOOR LIST FOR THE RELEASE SITTING, ASSEMBLED AND NOT APPLIED, AND W-ORD-SILENT-SENTENCES ACTED ON IT.

  python -X utf8 tools/b726_frontdoors.py dry | bank          -> data/b726_frontdoors.txt

THE CITATION SWEEP. The record names a sweep (tools/b367_filing.py: "every hit across the five repositories searched") and has no tool for it; this
is that reading, written down: every tracked .md and .html of PLACE-papers and of every SIDE-* clone, and the six deposited descriptions of
data/b726_zenodo_read.json, each normalized (lower case, every run of non-word characters a space), searched for the sentence. THE MATCHERS, each
yield printed: M1 the whole sentence; M2 six consecutive words; M3 four consecutive words; M4 the kernel's name or a terminal the sentence names, and
within 600 characters of it four consecutive words of the sentence (the class is read from M4). M2 alone found the mathematics and not a citation
("theta(-1/tau) = sqrt(-i tau)" in papers that never name the kernel), which the first hand read showed, so a citation here must name its object.
A sentence is LOAD-BEARING when M4 hits a paper, page or deposit description; SILENT otherwise. A hit in the sentence's own repository, in a sibling
checkpoint kernel (a shared template, not a citation) or in a ledger (a ledger records; b367's reading) is printed beside and does not class.
I-12 in INSTRUMENTS (phase1.5/method/INSTRUMENTS.md :318) is the separability-legibility quadrant; W-ORD-SILENT-SENTENCES names it and gives its own
two classes, which are the classes read here. THE CONTROLS RUN FIRST: a sentence the sweep is known to find, a planted sentence it must not, and a
sentence planted into one in-memory document at the kind's own shape. SPIRAL_MAP.md is private and the relay public: its sentence is cited by line
and digest as b721 cited it, not quoted. No author's name is printed; the list refuses itself if an identifier survives. Writes nothing outside it."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
import b722_llm_line as LLM  # noqa: E402  ### its grades, its position reader and its lists, imported unedited
import b726_address_scan as SC  # noqa: E402

PP = 'D:/MY-DOwnloads/PLACE-papers'
OUT = os.path.join(D, 'b726_frontdoors.txt')
NL = '\n'
WINDOW = 600
CHECKPOINT =['SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve']
LEDGER = ('FINDINGS.md', 'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'ERRATA.md', 'REGISTRY.md', 'SPIRAL_MAP', 'archive/', 'internal/', 'meta/')
LLM_S = ("*Computational workflow assisted by various LLM instances. Mathematical content, strategies of argument, and editorial decisions are the "
         "author's.*")
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def norm(s):
    return ' '.join(re.sub(r'\W+', ' ', s.lower()).split())


def strip_html(s):
    return re.sub(r'\s+', ' ', re.sub(r'&[a-z]+;', ' ', re.sub(r'<[^>]+>', ' ', s)))


def corpus():
    """(class-free) rows (repo, path, normalized text); the class is read per sentence, the own repository depending on it"""
    rows = []
    repos = [('PLACE-papers', PP)] + [(d, 'D:/' + d) for d in sorted(os.listdir('D:/')) if d.startswith('SIDE-') and os.path.isdir('D:/%s/.git' % d)]
    for name, r in repos:
        for p in git(r, 'ls-files', '--', '*.md', '*.html').split(NL):
            f = os.path.join(r, p)
            if p and os.path.isfile(f):
                with open(f, 'rb') as h:
                    rows.append((name, p, norm(h.read().decode('utf-8', 'replace'))))
    for z in json.load(open(os.path.join(D, 'b726_zenodo_read.json'), encoding='utf-8'))['rows']:
        rows.append(('DEPOSIT', 'zenodo %s' % z['id'], norm(strip_html(z.get('description', '')))))
    return rows


def kind(repo, path, own):
    if repo == 'DEPOSIT':
        return 'deposit'
    if repo == own:
        return 'own'
    if repo in CHECKPOINT:
        return 'sibling'
    if repo == 'PLACE-papers':
        return 'ledger' if path.startswith(LEDGER) else 'paper'
    return 'page'


def shingles(sentence, w):
    t = norm(sentence).split()
    return [' '.join(t)] if len(t) <= w else [' '.join(t[i:i + w]) for i in range(len(t) - w + 1)]


def names(sentence, own):
    """what a citation of a sentence about a kernel must name: the kernel, or a terminal the sentence itself names"""
    return [norm(own)] + [x for x in re.findall(r'`([A-Za-z_][\w.]*)`', sentence) if '_' in x]


def near(txt, needles, sh, width=WINDOW):
    """M4: a name of needles, and within width characters of it four consecutive words of the sentence that are not the name itself"""
    for nd in needles:
        i = txt.find(nd)
        while i >= 0:
            win = txt[max(0, i - width):i + len(nd) + width]
            # ### a label is not the sentence's words: "checkpoint 1.2-A" sits beside every kernel's name
            s = next((x for x in sh if x in win and 'checkpoint' not in x and not any(y in x for y in needles)), None)
            if s:
                return nd, s, win[max(0, win.find(s) - 90):win.find(s) + len(s) + 90]
            i = txt.find(nd, i + 1)
    return None


def sweep(sentence, rows, own, needles=None):
    """the yields of the matchers, by kind; M4's citing hits named, with the words around them"""
    out = {}
    hits = []
    for m, w in (('M1', 10 ** 6), ('M2', 6), ('M3', 4)):
        sh = shingles(sentence, w)
        tally = {}
        for repo, path, txt in rows:
            if next((s for s in sh if s in txt), None):
                k = kind(repo, path, own)
                tally[k] = tally.get(k, 0) + 1
        out[m] = tally
    sh = shingles(sentence, 4)
    needles = needles if needles is not None else names(sentence, own)
    tally = {}
    for repo, path, txt in rows:
        k = kind(repo, path, own)
        if k == 'own':
            continue
        got = near(txt, needles, sh)
        if got:
            tally[k] = tally.get(k, 0) + 1
            if k in ('paper', 'page', 'deposit'):
                hits.append((repo, path, got[1], got[2]))
    out['M4'] = tally
    return out, hits


def frozen():
    L = open(os.path.join(D, 'b721_frozen_line.txt'), encoding='utf-8').read().split(NL)
    rows, k = [], None
    for i, l in enumerate(L):
        m = re.match(r'^## (SIDE-\S+) at v', l)
        if m:
            k = m.group(1)
        m = re.match(r'^\s+(\d+)\.(\d+)\s+EXCEEDS\s+\| (.*)$', l)
        if m:
            nxt = L[i + 1].strip() if i + 1 < len(L) else ''
            rows.append(dict(kernel=k, file='README.md', line=int(m.group(1)), sn=int(m.group(2)), text=m.group(3), bank=i + 1,
                             note=nxt if nxt and '|' not in nxt else ''))
        m = re.match(r'^\s+THE GITHUB DESCRIPTION \(.*?\): "(.*)"$', l)
        if m and 'EXCEEDS' in L[i + 1]:
            rows.append(dict(kernel=k, file='GitHub description', line=0, sn=0, text=m.group(1), bank=i + 1, note=L[i + 1].split('|', 1)[1].strip()))
    return rows


def drafts():
    L = open(os.path.join(D, 'b721_frozen_line_drafts.txt'), encoding='utf-8').read().split(NL)
    out = {}
    for k in CHECKPOINT:
        i = next(n for n, l in enumerate(L) if l.startswith('## ' + k))
        j = next(n for n in range(i + 1, len(L)) if L[n].strip().startswith('GITHUB DESCRIPTION'))
        para = ' '.join(x.strip() for x in L[i + 2:j])
        out[k] = (para, L[j + 1].strip(), i + 3, j + 2)
    i = next(n for n, l in enumerate(L) if l.startswith('## SPIRAL_MAP.md :104'))
    j = next(n for n in range(i, len(L)) if L[n].startswith('## THE DRAFTS READ'))
    out['SPIRAL'] = (' '.join(x.strip() for x in L[i + 1:j] if x.strip()), i + 2)
    return out


def readme_line(k, n):
    return git('D:/' + k, 'show', 'main:README.md').split(NL)[n - 1]


def llm_rows():
    M, _g, mline, _r, sentence, byline = LLM.monograph()
    S = sentence.strip()
    if S != LLM_S:
        sys.exit('### THE MONOGRAPH`S LINE IS NOT THE RULING`S WORDS -- NOTHING WRITTEN')
    ctl = [LLM.grade(M, S)[0], LLM.grade(['x', S.replace('strategies of argument', 'proof strategies'), 'y'], S)[0], LLM.grade(['# d', 'none'], S)[0]]
    if ctl != ['SAME', 'DIFFERS', 'ABSENT']:
        sys.exit('### AN LLM CONTROL NOT AS WANTED: %r' % ctl)
    rows = []
    for rid, p in LLM.PAPERS + [('d1-3 v2.4.0', 'day1/Which_Structure_Confines_v2_4_0.md')]:
        L = open(os.path.join(PP, p), encoding='utf-8').read().split(NL)
        g, n, line = LLM.grade(L, S)
        ip = LLM.in_position(L, n)
        _after, where = LLM.end_matter_pos(L)
        rows.append(dict(kind='paper', row=rid, path=p, grade=g, line=n, text=LLM.sentence_of((line or '').strip()), where=where, ip=ip))
    for k in LLM.KERNELS:
        L = git('D:/' + k, 'show', 'main:README.md').split(NL)
        g, n, line = LLM.grade(L, S)
        head = next((i + 1 for i, l in enumerate(L) if l.strip().lower() == '## ai disclosure'), None)
        last = max(j for j in range(len(L)) if L[j].strip()) + 1
        rows.append(dict(kind='README', row=k, path=k + ' README.md at main ' + git('D:/' + k, 'rev-parse', 'main').strip()[:7], grade=g, line=n,
                         text=(line or '').strip(), where=('under its "## AI disclosure" heading (:%d)' % head) if head else
                         'at the end (after :%d), under a heading "## AI disclosure"' % last, ip=None))
    return rows, mline, ctl


def zen(rid):
    return next(z for z in json.load(open(os.path.join(D, 'b726_zenodo_read.json'), encoding='utf-8'))['rows'] if z['id'] == rid)


def item(L, n, tag, file_, line, cur, new, why=''):
    L += ['  [%d] %s' % (n, tag), '    FILE: %s' % file_, '    LINE: %s' % line, '    CURRENT: %s' % cur, '    DRAFT:   %s' % new]
    if why:
        L.append('    WHY:     %s' % why)
    L.append('')


def must(rid, words):
    if words not in strip_html(zen(rid)['description']):
        sys.exit('### RECORD %s DOES NOT CARRY %r -- NOTHING WRITTEN' % (rid, words))
    return words


KNOWN = ('Mathematical content, strategies of argument, and editorial decisions', 'computational workflow assisted by various llm instances', LLM.MONO)


def main(mode):
    t0 = time.time()
    name, user, addr = SC.author_name(), SC.previous_username(), SC.previous_address()
    rows = corpus()
    # ### THE CONTROLS, BEFORE ANY SENTENCE
    known, known_needle, known_doc = KNOWN
    k_y, k_h = sweep(known, rows, own='NONE', needles=[known_needle])
    planted = 'the amber lantern of the seventh quarter turn certifies every residue beneath the northern threshold of sigma'
    p_y, p_h = sweep(planted, rows, own='SIDE-archimedean')
    kind_s = 'Lean 4 kernel — the Archimedean / √ **identification** of sigma = 1/2.'
    q_y, q_h = sweep(kind_s, [('PLACE-papers', 'planted.md', norm('as SIDE-archimedean writes: ' + kind_s + ' and going on'))], own='SIDE-archimedean')
    c1 = any(h[0] == 'PLACE-papers' and h[1] == known_doc for h in k_h)
    c2 = not p_h and not any(v for v in p_y.values())
    c3 = len(q_h) == 1
    if not (c1 and c2 and c3):
        sys.exit('### A SWEEP CONTROL NOT AS WANTED (%r %r %r) -- NOTHING WRITTEN' % (c1, c2, c3))
    F = frozen()
    if len(F) != 23:
        sys.exit('### THE FROZEN LINE`S EXCEEDS ROWS READ %d, NOT 7 + 7 + 9 -- NOTHING WRITTEN' % len(F))
    for f in F:
        f['y'], f['hits'] = sweep(f['text'], rows, f['kernel'])
    loaded = [f for f in F if f['hits']]
    silent = [f for f in F if not f['hits']]
    Dr = drafts()
    spiral = open(os.path.join(PP, 'SPIRAL_MAP.md'), encoding='utf-8').read().split(NL)[103]
    lr, mline, ctl = llm_rows()
    L = ['b726 -- (R336)(5)-(6): THE FRONT-DOOR LIST FOR THE RELEASE SITTING, ASSEMBLED AND NOT APPLIED (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### By tools/b726_frontdoors.py. Nothing here is applied: no README, GitHub description, Zenodo record or kernel main is touched. Every draft is for the author`s sitting, whose words',
         '### govern. Corpus: %d documents (PLACE-papers and every SIDE-* clone, .md and .html, tracked; six deposited descriptions read anonymously, data/b726_zenodo_read.json).' % len(rows),
         '### THE CLASSES (W-ORD-SILENT-SENTENCES, OPEN_TRAILS :16593): LOAD-BEARING -- cited by a paper, page or deposit description, found by the sweep; SILENT -- cited by nothing. The class is',
         '### read from M4 (the kernel`s name or a terminal the sentence names, within 600 characters four consecutive words of the sentence, the label "checkpoint" not counted); M1 (the whole sentence),',
         '### M2 (six) and M3 (four) print their yields beside. M2 classed 4 at the first run, and the hand read refused it: "theta(-1/tau) = sqrt(-i tau)" is the classical formula, in papers that name no',
         '### kernel. M4 with the label counted classed 5, by "checkpoint 1.2-A"; that too was read and tightened. Hits in the own repository, a sibling checkpoint kernel and a ledger (the ledgers,',
         '### SPIRAL_MAP, archive/, internal/, meta/) do not class.',
         '### THE NAMING NOTE: INSTRUMENTS :318`s I-12 is the separability-legibility quadrant, a two-run classing of spaces; the order names I-12 and gives its own two classes, and those are read here.', '',
         '## THE CONTROLS, BEFORE ANY SENTENCE',
         '  (C1) a sentence the sweep is known to find, the monograph`s LLM line, at day1/A_Place_to_Stand.md :%d, the sentence`s second half beside its first as the name: found -- AS WANTED (M4 yields %r)' % (mline, k_y['M4']),
         '  (C2) a planted sentence it must not find ("%s"): 0 at M1, M2, M3 and M4 -- AS WANTED' % planted,
         '  (C3) a sentence of the kind, README 3.1, planted beside its kernel`s name in one in-memory paper: found once -- AS WANTED', '',
         '## THE YIELDS, EVERY EXCEEDS SENTENCE (kernel, line | M1 | M2 | M3 | M4 by kind; M4 classes)']
    for f in F:
        L.append('  %-16s %-8s | M1 %s | M2 %s | M3 %s | M4 %s' % (f['kernel'], ':%d.%d' % (f['line'], f['sn']) if f['line'] else 'DESC', f['y']['M1'], f['y']['M2'], f['y']['M3'], f['y']['M4']))
    n = 0
    L += ['', '## PART A -- THE LOAD-BEARING SENTENCES, AT THE HEAD OF THE LIST (%d); repaired at the release sitting' % len(loaded), '']
    for f in loaded:
        n += 1
        para = 'the README paragraph of PART B for %s' % f['kernel'] if f['line'] else Dr[f['kernel']][1]
        item(L, n, 'LOAD-BEARING', '%s %s' % (f['kernel'], f['file']), ':%d, sentence %d (relay data/b721_frozen_line.txt :%d)' % (f['line'], f['sn'], f['bank']) if f['line'] else 'the one line (relay data/b721_frozen_line.txt :%d)' % f['bank'],
             f['text'], para, 'cited at: ' + ' ; '.join('%s %s' % (h[0], h[1]) for h in f['hits'][:6]) + (' (+%d)' % (len(f['hits']) - 6) if len(f['hits']) > 6 else '') + '. ' + f['note'])
    L += ['## PART B -- THE DRAFTS OF data/b721_frozen_line_drafts.txt', '']
    for k in CHECKPOINT:
        n += 1
        item(L, n, 'README PARAGRAPH', k + ' README.md', ':3 (the line under the title; the sentences of PARTS A and F go with it)', readme_line(k, 3), Dr[k][0], 'relay data/b721_frozen_line_drafts.txt :%d' % Dr[k][2])
        n += 1
        d = next((f['text'] for f in F if f['kernel'] == k and not f['line']), None)
        if d is None:
            d = re.search(r'THE GITHUB DESCRIPTION \(gh repo view psinary-sketch/%s\): "(.*)"' % k, open(os.path.join(D, 'b721_frozen_line.txt'), encoding='utf-8').read()).group(1)
        item(L, n, 'GITHUB DESCRIPTION', k + ' GitHub description', 'the one line', d, Dr[k][1], 'relay data/b721_frozen_line_drafts.txt :%d' % Dr[k][3])
    n += 1
    item(L, n, 'THE SENTENCE FOR THE DOCUMENT`S NEXT EDITION', 'PLACE-papers SPIRAL_MAP.md', ':104', '[private; cited by line and digest as at b721, not quoted in the public relay: sha256 %s]' % hashlib.sha256(spiral.encode('utf-8')).hexdigest()[:16],
         Dr['SPIRAL'][0], 'relay data/b721_frozen_line_drafts.txt :%d. The ruling asks the current words; the file is private and the relay public, so the digest stands for them; the words are at the line.' % Dr['SPIRAL'][1])
    L += ['## PART C -- THE DEPOSITED RECORDS (no Zenodo record is edited this act; read at data/b726_zenodo_read.json)', '']
    lv = zen('21539068')
    n += 1
    item(L, n, 'THE lv DESCRIPTION`S "ZERO SORRY", IN THE WORDS OF E-2026-10-29-1', 'Zenodo 10.5281/zenodo.21539068 (SIDE-lv-conservation v0.10.0), description', 'the sentence at relay data/b724_release_list.txt :8',
         '#print axioms at the named terminals — all report {propext, Classical.choice, Quot.sound}, zero custom axioms, zero sorry.',
         '#print axioms at the named terminals — all report {propext, Classical.choice, Quot.sound}, zero custom axioms; one `sorry`, at T3_perClass_to_combinations, a statement false as stated whose negation the kernel proves (ERRATA E-2026-10-29-1).',
         'relay data/b724_release_list.txt :11-:13; ERRATA.md :1006; data/b724_lv.txt.')
    n += 1
    item(L, n, 'THE MAY RECORD, ITS CURRENCY NOTE ((R20), REGISTRY.md :879)', 'Zenodo 10.5281/zenodo.19938917 (A Place To Stand v1.0.2, 2026-05-01), description, a note at the head', 'the head; the title and "%s" stand beneath it' % must('19938917', 'The result follows without new axioms'),
         zen('19938917')['title'],
         'HISTORICAL RECORD. This version is superseded by v1.1.2 (10.5281/zenodo.21539167), which states the result as a reduction of the Riemann Hypothesis to the single located clause h2, named open. The title and the description below are as deposited on 2026-05-01: their claim of a proof is not supported, and the Riemann Hypothesis stays open.',
         'REGISTRY.md :416 reads it superseded; the record itself carries no note. (R20): no third state.')
    n += 1
    item(L, n, 'THE MAY RECORD, ITS CURRENCY NOTE ((R20), REGISTRY.md :879)', 'Zenodo 10.5281/zenodo.19937590 (SIDE-kernel v1.1, 2026-05-01), description, a note at the head', 'the head; the sentence beneath it stands as deposited',
         must('19937590', 'The kernel proves that no off-line zero exists by exhaustively excluding every mechanism class derivable from the specification.'),
         'HISTORICAL RECORD. This version is superseded by v1.5 (10.5281/zenodo.21520474). The description below is as deposited on 2026-05-01: the kernel does not prove that no off-line zero exists. Its Route 3 premise is the Riemann Hypothesis restated (ERRATA E-2026-09-25-1), and the Riemann Hypothesis stays open.',
         'The current record 21520474 carries E-2026-09-25-1 in its own first lines; the May record carries nothing.')
    n += 1
    tc = 'Companion (RH proof, pure mathematics): A Place To Stand, concept DOI 10.5281/zenodo.19675355'
    item(L, n, 'THE T7 COMPANION LINE', 'Zenodo 10.5281/zenodo.21436282 (T₇ Matched-Arc CMB Search), description', 'the sentence before CONTENTS', must('21436282', tc) + ' — the T₇ cosmology is Phase-2 speculative physics, explicitly not load-bearing for the Riemann Hypothesis.',
         'Companion (the SIDE reduction of the Riemann Hypothesis to a single located clause, pure mathematics): A Place To Stand, concept DOI 10.5281/zenodo.19675355 — the T₇ cosmology is Phase-2 speculative physics, explicitly not load-bearing for the Riemann Hypothesis.',
         'The words of the current monograph record`s own title (21539167).')
    n += 1
    item(L, n, 'THE WAVE 1 DESCRIPTION, ITS CURRENCY NOTE', 'Zenodo 10.5281/zenodo.21539167 (A Place To Stand v1.1.2), description, a note at the foot', 'the foot; "%s" stands above it' % must('21539167', 'The proof operates entirely within ZFC'),
         '(no note)', 'CURRENCY. This record is the citable deposit at manuscript v5.10.2. The live line stands ahead of it at v5.18 and is not deposited; counts and kernel figures here are frozen at the deposit. The clause h2 stays open, and the Riemann Hypothesis is not proved here. h2_sign is equivalent to Mathlib`s RiemannHypothesis, both directions compiled (h2_sign_iff_rh, SIDE-explicit-formula).'.replace('`', "'"),
         'README.md :164 (the deposit note) and :106-:121 (the ceiling).')
    n += 1
    item(L, n, 'THE WAVE 1 DESCRIPTION, ITS CURRENCY NOTE', 'Zenodo 10.5281/zenodo.21520474 (SIDE-kernel v1.5), description, a note at the foot', 'the foot; "%s" stands above it' % must('21520474', 'The proof enumerates the seven mechanism classes'),
         '(no note)', 'CURRENCY. This record is the citable deposit at SIDE-kernel v1.5 = 0e5233f. The live kernel line names SIDE-explicit-formula beside it and is not deposited. Where the text above says "the proof", it names the argument under the named premise, which stays open.',
         'REGISTRY.md :416 and README.md :164.')
    n += 1
    item(L, n, 'THE WAVE 1 DESCRIPTION, ITS CURRENCY NOTE', 'Zenodo 10.5281/zenodo.21539068 (SIDE-lv-conservation v0.10.0), description, a note at the foot', 'the foot; item above carries the "zero sorry" word',
         '(no note)', 'CURRENCY. This record is the citable deposit at v0.10.0 = 93c27ec. The live arm stands ahead of it and is not deposited.', 'REGISTRY.md :102.')
    L += ['## PART D -- THE SIDE-cosmo ERROR BAR (the kernel not touched; head %s)' % git('D:/SIDE-cosmo', 'rev-parse', 'main').strip()[:7], '']
    ag = git('D:/SIDE-cosmo', 'show', 'main:AGENTS.md').split(NL)
    rd = git('D:/SIDE-cosmo', 'show', 'main:README.md').split(NL)
    n += 1
    item(L, n, 'THE TWO PLANCK REFERENCES, RECONCILED', 'SIDE-cosmo AGENTS.md', ':158', ag[157].strip(),
         '8. **Planck reference reconciled.** One citation stands across deposit, README and Phase 2 papers: Planck 2018 (arXiv 1807.06209), Ω_b h² = 0.02237 ± 0.00015, H₀ = 67.36, so Ω_b = 0.04930 ± 0.00059. The older 0.04897 ± 0.0031 is superseded.',
         'The reconciliation was settled and not applied here: PLACE-papers archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md :3084, :3090. A sweep of PLACE-papers and SIDE-cosmo finds 0.04897 at AGENTS :158 alone outside those ledger lines.')
    n += 1
    item(L, n, 'THE DEVIATION THE ERROR BAR GIVES', 'SIDE-cosmo README.md', ':38', rd[37].strip(), rd[37].strip().replace('0.13σ', '0.14σ'),
         '(4/81 - 0.04930) / 0.00059 = 0.14 (0.1405); the loom`s :3084 reads 0.13-0.14 and its :3118 0.14. AGENTS.md :23 carries the same figure. The identification stays PERMITTED, a single-shot, not derived from cosmology (phase1.5/method/THE_SUBSTRATE.md :59).')
    n += 1
    item(L, n, 'THE SAME FIGURE', 'SIDE-cosmo AGENTS.md', ':23', 'Class A predicts 0.04938; Planck 2018 measures 0.04930 ± 0.00059; deviation 0.13σ.', 'Class A predicts 0.04938; Planck 2018 measures 0.04930 ± 0.00059; deviation 0.14σ.', 'as the row above')
    if '0.13σ' not in rd[37] or 'deviation 0.13σ' not in ag[22]:
        sys.exit('### SIDE-cosmo`S FIGURE NOT AT ITS LINE -- NOTHING WRITTEN')
    differ = [r for r in lr if r['grade'] != 'SAME']
    L += ['## PART E -- THE LLM LINE ((R336)(6)): %d PAPERS AND %d KERNEL READMES READ AGAINST day1/A_Place_to_Stand.md :%d; CONTROLS %r AS WANTED' % (sum(1 for r in lr if r['kind'] == 'paper'), len(LLM.KERNELS), mline, ctl),
          '  THE MONOGRAPH`S WORDS: ' + LLM_S,
          '  THE POSITION: after the bibliography, before the colophon; a README under its "## AI disclosure" heading.',
          '  READ: SAME %d ; DIFFERS %d ; ABSENT %d.' % tuple(sum(1 for r in lr if r['grade'] == g) for g in ('SAME', 'DIFFERS', 'ABSENT')), '']
    for r in lr:
        if r['grade'] == 'SAME':
            L.append('  SAME %s at :%s (%s)' % (r['row'], r['line'], r['path']))
    L.append('')
    for r in differ:
        n += 1
        pos = 'in place of :%d' % r['line'] if r['line'] and (r['ip'] and r['ip'][0] or r['kind'] == 'README') else r['where'] + (', the line at :%d left for the sitting`s word' % r['line'] if r['line'] else '')
        item(L, n, 'THE LLM LINE, ' + r['grade'], r['path'], (':%d' % r['line']) if r['line'] else 'none', r['text'] or '(no line of the kind)', LLM_S, 'position: ' + pos)
    n += 1
    L += ['## PART G -- THE EDITION OF (R336)(4)', '']
    item(L, n, 'THE BYLINE AND TWO SELF-CITATIONS OF WHICH STRUCTURE CONFINES v2.4.0', 'PLACE-papers day1/Which_Structure_Confines_v2_4_0.md', ':3 and its References` two self-citations', '**The author** | v2.4.0, October 2026; The author. ...',
         'the byline and citations of day1/Which_Structure_Confines.md :3, :142, :144, as they stand there, with the version v2.4.0', '(R336)(8) bars any identifier of the author from what this act writes, so the edition carries neither; the sitting sets them. Not quoted here.')
    L += ['## PART F -- THE SILENT SENTENCES, CARRIED WITH THEIR NOTES (%d): cited by nothing; not repaired for a citation`s sake, but each falls with its README paragraph or description in PART B' % len(silent), '']
    for f in silent:
        L += ['  %s %s %s | %s' % (f['kernel'], f['file'], ':%d.%d' % (f['line'], f['sn']) if f['line'] else '(the one line)', f['text']), '    NOTE: %s' % (f['note'] or '(the bank`s row carries none)')]
    L += ['', '### ### **THE FRONT-DOOR LIST: %d ITEMS ; %d LOAD-BEARING AND %d SILENT OF %d EXCEEDS ; THE LLM LINE READ AT %d PAPERS AND %d READMES, %d DIFFERING ; SWEEP CONTROLS 3 OF 3 AS WANTED ; ASSEMBLED AND NOT APPLIED ; %d s.**' % (
        n, len(loaded), len(silent), len(F), sum(1 for r in lr if r['kind'] == 'paper'), len(LLM.KERNELS), len(differ), int(time.time() - t0))]
    t = NL.join(L) + NL
    if SC.count(t, name) or SC.count(t, user) or SC.count(t, addr):
        sys.exit('### AN IDENTIFIER OF THE AUTHOR IN THE LIST -- NOTHING WRITTEN')
    print(t if mode == 'bank' else NL.join(L[:12 + 25 + 2]) + NL + L[-1])
    for f in loaded:
        for h in f['hits'][:8]:
            print('LOADED', f['kernel'], f['line'], f['sn'], h[1], '|', h[2], '|', h[3])
    if mode == 'bank':
        with open(OUT + '.tmp', 'wb') as h:
            h.write(t.encode('utf-8'))
        os.replace(OUT + '.tmp', OUT)
        print('written data/b726_frontdoors.txt')


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') not in ('dry', 'bank'):
        sys.exit(__doc__)
    main(sys.argv[1])
