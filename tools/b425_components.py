# -*- coding: utf-8 -*-
"""b425_components.py -- THE FALSIFIER READ: THE LANE'S EQUATION OF STATE AGAINST THE SUPERNOVA RESULT.

### ### **THE SEARCH, THE SELECTION AND THE FETCH ARE READING (3)'S, RUN AFTER THE LOCK; THE TENSION IS READING
### (5)'S, DECIDED BY ITS RULE IN THE SOURCE'S OWN WORDS.** ### This tool fits nothing, samples nothing and
### computes no likelihood: it fetches bytes, hashes them, writes their text to disk and quotes it.
###   --locate    the search (Q1-Q3), every result printed; the selection by the rule; each chosen source fetched,
###               hashed and extracted; its claim and significance sentences located. data/b425_locate.txt, .json
###   --read      the lane's commitment and condition quoted at their pins; each source's claim and significance
###               quoted from its extract; the tension in three parts; the routing. data/b425_the_read.txt
###   (no flag)   the report and the expectation, its two clauses apart.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SCRATCH = os.path.join(os.environ.get('TEMP', D), 'b425_sources')
LOC, LJSON = os.path.join(D, 'b425_locate.txt'), os.path.join(D, 'b425_locate.json')
READREC = os.path.join(D, 'b425_the_read.txt')
NL = chr(10)
BS = chr(92)
API = 'https://export.arxiv.org/api/query?'
ABS, PDF = 'https://arxiv.org/abs/', 'https://arxiv.org/pdf/'
UA = {'User-Agent': 'relay-b425-read/1.0 (research seat; one query per three seconds)'}
CAP = 3
QUERIES = [('Q1', 'abs:supernova AND abs:"dark energy" AND abs:DESI'),
           ('Q2', 'abs:supernovae AND abs:"dynamical dark energy"'),
           ('Q3', 'abs:supernova AND abs:"evolving dark energy"')]
# ### THE RULE'S THREE TESTS, READ ON THE ABSTRACT'S OWN WORDS -- reading (3) (a), (b), (c).
T_A = r'(?i)supernova|' + BS + r'bSNe?' + BS + r'b|' + BS + r'bSN ?Ia' + BS + r'b|Pantheon|Union ?3|DES-?SN|DESY5'
T_B = (r'(?i)w_?\{?0\}?|w_?\{?a\}?' + BS + r'b|w0wa|dynamical dark energy|evolving dark energy|time-(varying|evolving) '
       r'dark energy|equation of state|Lambda ?CDM|ΛCDM|cosmological constant')
T_C = r'[0-9](' + BS + r'.[0-9]+)?' + BS + r's*' + BS + r'$?' + BS + r's*(' + BS + BS + r'sigma|σ|sigma)'
DR2 = r'(?i)DESI.{0,40}(DR2|Data Release 2)'
NS = {'a': 'http://www.w3.org/2005/Atom'}
FDOC = {'FANO': 'phase2/physics/FANO_DERIVATION_OF_LAMBDA.md', 'STORMER': 'phase2/physics/STORMER.md',
        'FD': 'phase2/physics-speculative/FORMATION_DISTANCE.md',
        'FDDV': 'phase1.5/spectral/FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md', 'REG': 'REGISTRY.md'}
PINS = {'FANO': 'b09635067c6a', 'STORMER': 'f1a08e554ab2', 'FD': '2560e1dc7462', 'FDDV': '75376a24677e'}


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def norm(s):
    return re.sub(r'\s+', ' ', s or '').strip()


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.status, r.read()


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def slug(aid):
    return re.sub(r'[^0-9A-Za-z.]', '_', aid)


def sentences(text):
    return [norm(s) for s in re.split(r'(?<=[.;])\s+(?=[A-Z(])', text) if s.strip()]


def run_locate():
    R = ['=' * 100, 'b425 -- THE SEARCH, THE SELECTION AND THE FETCH. ### READING (3), AFTER THE LOCK.', '=' * 100,
         '  at (UTC) : %s' % utc(), '  cap : %d sources' % CAP, '']
    say = R.append
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    seen, results = {}, []
    for tag, q in QUERIES:
        url = API + urllib.parse.urlencode({'search_query': q, 'sortBy': 'submittedDate', 'sortOrder': 'descending',
                                            'start': 0, 'max_results': 25})
        say('-' * 100)
        say('### %s -- %s' % (tag, q))
        say('-' * 100)
        try:
            st, body = get(url)
        except Exception as exc:
            say('  ### NOT FETCHED -- %s' % exc)
            continue
        h = hashlib.sha256(body).hexdigest()
        open(os.path.join(SCRATCH, '%s.xml' % tag), 'wb').write(body)
        say('  status %s ; bytes %d ; sha256 %s' % (st, len(body), h))
        root = ET.fromstring(body)
        entries = root.findall('a:entry', NS)
        say('  results : %d' % len(entries))
        for e in entries:
            aid = norm(e.findtext('a:id', '', NS)).rsplit('/abs/', 1)[-1]
            base = re.sub(r'v[0-9]+$', '', aid)
            # ### THE FULL TIMESTAMP, NOT THE DATE: run 1 cut it to the day and left "newest" tied.
            title, pub = norm(e.findtext('a:title', '', NS)), norm(e.findtext('a:published', '', NS))
            summ = norm(e.findtext('a:summary', '', NS))
            ta, tb, tc = (bool(re.search(x, title + ' ' + summ)) for x in (T_A, T_B, T_C))
            say('    %-14s %s  (a)%s (b)%s (c)%s  %s' % (base, pub, 'Y' if ta else 'n', 'Y' if tb else 'n', 'Y' if tc else 'n',
                                                     title[:84]))
            if base not in seen:
                seen[base] = dict(id=base, version=aid, title=title, published=pub, abstract=summ, a=ta, b=tb, c=tc,
                                  dr2=bool(re.search(DR2, title)), queries=[tag])
                results.append(seen[base])
            else:
                seen[base]['queries'].append(tag)
        time.sleep(3.5)
    qual = [r for r in results if r['a'] and r['b'] and r['c']]
    # ### THE FACE, READING (3): "first, A qualifying result whose title names DESI's second data release ...; then
    # ### the newest qualifying results." ### ONE such result, the newest of them, and then the newest of all the
    # ### others -- run 1 took every DR2-titled result first, in collection order, which the face does not say.
    dr2 = sorted([r for r in qual if r['dr2']], key=lambda r: r['published'], reverse=True)
    first = dr2[:1]
    rest = sorted([r for r in qual if r not in first], key=lambda r: r['published'], reverse=True)
    chosen = (first + rest)[:CAP]
    say('')
    say('-' * 100)
    say('### THE SELECTION, BY THE RULE.')
    say('-' * 100)
    say('  unique results : %d ; qualifying on (a), (b) and (c) : %d ; of those titled DESI DR2 : %d' % (len(results), len(qual), len(dr2)))
    for r in qual:
        say('    qualifying : %-14s %s %s%s' % (r['id'], r['published'], '[DR2] ' if r['dr2'] else '', r['title'][:80]))
    say('  ### CHOSEN, IN THE RULE`S ORDER, CAPPED AT %d : %s' % (CAP, [r['id'] for r in chosen]))
    if not dr2:
        say('  ### NO RESULT TITLED WITH DESI`S SECOND RELEASE APPEARED IN THE DECLARED WINDOW; THE RULE`S SECOND CLAUSE GOVERNS.')
    sources = []
    for r in chosen:
        say('')
        say('-' * 100)
        say('### SOURCE %s -- %s' % (r['id'], r['title']))
        say('-' * 100)
        src = dict(r)
        for kind, url in (('abs', ABS + r['id']), ('pdf', PDF + r['id'])):
            try:
                st, body = get(url)
                h = hashlib.sha256(body).hexdigest()
                ext = 'html' if kind == 'abs' else 'pdf'
                open(os.path.join(SCRATCH, '%s.%s' % (slug(r['id']), ext)), 'wb').write(body)
                if kind == 'pdf':
                    import pypdf
                    rd = pypdf.PdfReader(io.BytesIO(body))
                    text = NL.join('=== PAGE %d ===%s%s' % (k + 1, NL, (p.extract_text() or '')) for k, p in enumerate(rd.pages))
                    npages = len(rd.pages)
                else:
                    t = body.decode('utf-8', 'replace')
                    t = re.sub(r'(?is)<(script|style).*?</' + BS + '1>', ' ', t)
                    text = norm(re.sub(r'<[^>]+>', ' ', t))
                    npages = 0
                out = os.path.join(D, 'b425_source_%s%s.txt' % (slug(r['id']), '_abs' if kind == 'abs' else ''))
                io.open(out, 'w', encoding='utf-8', newline=NL).write(text + NL)
                src[kind] = dict(url=url, status=st, bytes=len(body), sha256=h, extract=os.path.basename(out),
                                 pages=npages, chars=len(text))
                say('  %-4s %s  status %s  bytes %d  sha256 %s  -> data/%s%s'
                    % (kind, url, st, len(body), h, os.path.basename(out), ('  (%d pages)' % npages) if npages else ''))
            except Exception as exc:
                src[kind] = dict(url=url, status='NOT FETCHED', error=str(exc)[:200])
                say('  %-4s %s  ### NOT FETCHED -- %s' % (kind, url, str(exc)[:160]))
            time.sleep(3.5)
        say('  the abstract, from the listing :')
        for w in wrap(r['abstract'], 94):
            say('      | %s' % w)
        pdft = read(os.path.join(D, src.get('pdf', {}).get('extract', '') or 'x'))
        sig = [s for s in sentences(norm(pdft)) if re.search(T_C, s) and re.search(T_B, s)]
        say('  sentences in the PDF`s text carrying a significance and the dark-energy test : %d (first 14 printed)' % len(sig))
        for s in sig[:14]:
            say('      > %s' % s[:300])
        src['sig_sentences'] = sig[:40]
        sources.append(src)
    say('')
    say('  ### SOURCES CHOSEN %d ; FETCHED IN FULL %d' % (len(sources), sum(1 for s in sources
                                                                     if s.get('pdf', {}).get('sha256') and s.get('abs', {}).get('sha256'))))
    say('=' * 100)
    io.open(LOC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), queries=QUERIES, results=results, chosen=[r['id'] for r in chosen], sources=sources),
                   indent=1, ensure_ascii=False)
    open(LJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(LJSON + '.tmp', LJSON)
    print(NL.join(R))
    return 0 if sources else 1


RJSON = os.path.join(D, 'b425_the_read.json')

# ### THE LANE, QUOTED AT ITS PINS -- readings (1) and (2). (key, label, start, end)
LANE = [('FANO', 'the assignment', '4. The equation-of-state assignment sends weight-1 elements', 'to a symmetry-breaking residual.'),
        ('FANO', 'dark energy is one orbit class', 'The dark energy is not a separate substance', '(the Hamming-distance assignment).'),
        ('FANO', 'the residual`s w, the lane`s own reach', 'The diagonal residual', 'manifests observationally.'),
        ('STORMER', 'the pending test', 'DESI 5-year', 'for DE/visible'),
        ('FD', 'THE CONDITION', '4. **DESI year-3 tests w = −1.**', 'refutes the decomposition.'),
        ('FDDV', 'the withdrawn document`s weaker sentence', 'The cosmological leg has a near-term', 'would constrain it.')]
REGROWS = [('p2-d6', r'(?m)^\| p2-d6 \|.*$'), ('the withdrawal line', r'(?m)^\| `FORMATION_DISTANCE_DARK_VARIABLE_v0_1\.md` \| 1\.5c-14 \|.*$')]

# ### THE SEAT'S READING OF EACH SOURCE, ENCODED AFTER THE LOCATE RUN WAS READ; EVERY QUOTATION IS RE-FOUND IN THE
# ### SOURCE'S OWN TEXT ON DISK BEFORE IT IS PRINTED. ('abs' = the listing's abstract, banked in b425_locate.json;
# ### 'pdf' = the PDF's extracted text.) ### (c) IS READING (5)'S RULE: FIRED on an exclusion stated in the source's
# ### words; NOT FIRED on stated consistency; UNDECIDED on a preference at a stated significance, no exclusion.
DECIDE = {
    '2609.10567': dict(
        claim=('abs', 'And the significances are', 'evolutionary dark energy dynamics.'),
        sig=('pdf', 'the evidence for dynamical dark energy model can not reach 4σ', 'only around 3σ.'),
        a=[('pdf', '(1) Chevallier-Polarski-Linder (CPL) parametrization', None), ('pdf', 'The ΛCDM model assumes a cosmological constant', None)],
        a_read='SAME QUANTITY -- the dark-energy equation of state, w(z) in five parametrizations including CPL, tested against the '
               'cosmological constant, which is the lane`s w = −1',
        verdict='UNDECIDED', deciding=('abs', 'And the significances are', 'evolutionary dark energy dynamics.'),
        why='a preference for an evolving equation of state at a stated significance, 2.1 to 3.7σ, and no sentence of the source '
            'excluding w = −1'),
    '2609.10133': dict(
        claim=('abs', 'In the context of the model with non-minimal coupling', 'over $Λ$CDM.'),
        sig=('pdf', 'ΛCDM can be excluded at 2.50σCL, with ∆AIC = 4.79', 'indicating positive evidence'),
        a=[('abs', 'providing an improved fit to the data compared to', 'parametrization.')],
        a_read='THE NULL IS THE LANE`S VALUE, THE ALTERNATIVE IS NOT A MEASURED w(z) -- the comparison is of a non-minimally '
               'coupled scalar model against ΛCDM, whose dark energy is the lane`s w = −1',
        verdict='FIRED', deciding=('abs', 'the standard model is excluded at the $2.50σ$ CL', None),
        qualifier=('abs', 'indicating a moderate preference for these models over', None),
        why='the source states, in its own word, that the standard model is EXCLUDED -- at 2.50σ CL -- and the rule reads an '
            'exclusion stated in the source`s words as FIRED; the same sentence names it a moderate preference, printed beside'),
    '2609.05321': dict(
        claim=('abs', 'the significance for time-evolving dark energy increases from', 'based on the maximum a posteriori'),
        sig=('pdf', 'points to a∼3σpreference of time-evolving dark energy over FlatΛCDM', None),
        a=[('pdf', 'Polarski-Linder (CPL) parametrization (wherew=', None), ('pdf', 'This shift is away from a cosmological constant', None)],
        a_read='SAME QUANTITY -- w = w0 + wa(1 − a) against Flat ΛCDM, a cosmological constant, the lane`s w = −1',
        verdict='UNDECIDED', deciding=('abs', 'the significance for time-evolving dark energy increases from', 'based on the maximum a posteriori'),
        why='a preference for time-evolving dark energy at a stated significance, 3.4σ to 4.0σ, and no sentence of the source '
            'excluding w = −1 -- its only uses of the word are about photometry'),
}


def lane_text(key):
    rel = FDOC[key]
    return subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True).stdout.decode('utf-8', 'replace')


def fold(s):
    return norm((s or '').replace('###', ' ').replace('**', '').replace('`', ''))


def qtext(text, start, end=None, cap=260):
    src, s0 = fold(text), fold(start)
    i = src.find(s0)
    if i < 0:
        return '### MISS'
    e0 = fold(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    return src[i:j + len(e0)] if j > i else src[i:i + cap]


def source_text(aid, where_):
    if where_ == 'abs':
        L = json.loads(read(LJSON))
        return next((r['abstract'] for r in L['results'] if r['id'] == aid), '')
    return read(os.path.join(D, 'b425_source_%s.txt' % slug(aid)))


def run_read():
    R = ['=' * 100, 'b425 -- THE FALSIFIER READ: THE LANE`S EQUATION OF STATE AGAINST THE SUPERNOVA RESULT.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    miss = []
    say('-' * 100)
    say('### THE LANE`S COMMITMENT AND ITS CONDITION, QUOTED AT THEIR PINS.')
    say('-' * 100)
    for key, lab, s, e in LANE:
        t = lane_text(key)
        blob = subprocess.run(['git', '-C', PP, 'rev-parse', 'HEAD:' + FDOC[key]], capture_output=True, text=True).stdout.strip()
        qq = qtext(t, s, e)
        miss += ['%s:%s' % (key, lab)] if qq == '### MISS' else []
        say('  %s -- %s (%s ; blob %s ; blob matches pin : %s)' % (lab, FDOC[key], key, blob[:12], blob.startswith(PINS[key])))
        for w in wrap(qq, 94):
            say('      | %s' % w)
    reg = lane_text('REG')
    for lab, pat in REGROWS:
        h = re.search(pat, reg)
        say('  REGISTRY.md -- %s :' % lab)
        for w in wrap(fold(h.group(0))[:420] if h else '### MISS', 94):
            say('      | %s' % w)
        miss += [] if h else ['REGISTRY %s' % lab]
    say('  ### The withdrawn document`s sentence does not govern: its register line reads WITHDRAWN.')
    L = json.loads(read(LJSON))
    out = []
    for aid in L['chosen']:
        dd = DECIDE.get(aid)
        src = next((s for s in L['sources'] if s['id'] == aid), {})
        say('')
        say('-' * 100)
        say('### SOURCE %s -- %s' % (aid, src.get('title', '')))
        say('-' * 100)
        say('  pdf sha256 %s ; abstract page sha256 %s' % (src.get('pdf', {}).get('sha256', '### NOT FETCHED'),
                                                           src.get('abs', {}).get('sha256', '### NOT FETCHED')))
        if not dd:
            say('  ### NO READING ENCODED FOR THIS SOURCE.')
            miss.append(aid)
            continue

        def show(label, spec):
            wh, s, e = spec
            t = qtext(source_text(aid, wh), s, e)
            if t == '### MISS':
                miss.append('%s:%s' % (aid, label))
            say('  %s (%s) :' % (label, 'the abstract' if wh == 'abs' else 'the PDF`s text'))
            for w in wrap(t, 92):
                say('      | %s' % w)
            return t
        claim = show('THE CLAIM', dd['claim'])
        sig = show('ITS STATED SIGNIFICANCE', dd['sig'])
        say('  PART (a) -- IS THE MEASURED QUANTITY THE ONE THE LANE FIXED?')
        for spec in dd['a']:
            show('    the source`s parameterization', spec)
        say('    ### %s. ### And the lane`s own reach stands beside it: the residual`s w is unspecified (FANO line 246).' % dd['a_read'])
        say('  PART (b) -- THE LANE`S CONDITION: *"Evolving dark energy refutes the decomposition"* (FORMATION_DISTANCE.md line 160),')
        say('    stating no significance.')
        say('  PART (c) -- BY READING (5)`S RULE:')
        dec = show('    the deciding sentence', dd['deciding'])
        if dd.get('qualifier'):
            show('    printed beside it, the same source`s own qualifier', dd['qualifier'])
        say('    ### ### **VERDICT [%s] : %s** -- %s.' % (aid, dd['verdict'], dd['why']))
        out.append(dict(id=aid, title=src.get('title', ''), verdict=dd['verdict'], deciding=dec, claim=claim, sig=sig,
                        a_read=dd['a_read'], same=dd['a_read'].split(' --')[0]))
    fired = [o for o in out if o['verdict'] == 'FIRED']
    say('')
    say('=' * 100)
    say('### THE TENSION, STATED.')
    say('=' * 100)
    say('  per source : %s' % ' ; '.join('%s %s' % (o['id'], o['verdict']) for o in out))
    if fired:
        say('  ### ### ### **BY THE LOCKED RULE, THE LANE`S CONDITION READS FIRED AT %d OF %d SOURCES: %s.**'
            % (len(fired), len(out), ', '.join(o['id'] for o in fired)))
        say('  ### ### **THE REGISTER ROW CARRYING THE LANE -- REGISTRY.md p2-d6 -- AND FORMATION_DISTANCE.md line 160 ARE NAMED')
        say('  ### ### AS THE AUTHOR`S TO MOVE.** ### No lane verdict is changed by this seat.')
    else:
        say('  ### No source reads FIRED by the rule.')
    say('  ### THE SOURCES DO NOT AGREE UNDER THE RULE, AND THE FACE FIXED NO RULE FOR COMBINING THEM; NONE IS APPLIED HERE.'
        if len(set(o['verdict'] for o in out)) > 1 else '  ### The sources agree under the rule.')
    say('')
    say('  ### THE SEAT`S READING, ROUTED TO THE AUTHOR AND NOT RULED:')
    say('    (1) the FIRED clause keys on a source`s own word, and the source that uses it does so at 2.50σ CL, in the sentence')
    say('        that calls the result a moderate preference -- the rule read as locked, its limit printed rather than repaired;')
    say('    (2) the selection rule`s window was the newest twenty-five results per query, so the DESI collaboration`s own')
    say('        second-release paper did not fall in it; the DESI-titled source read is a later analysis of that release;')
    say('    (3) the lane names its test as DESI year-3 (FORMATION_DISTANCE.md) and as DESI 5-year (STORMER.md), and names no')
    say('        significance at which either would decide; the corpus`s own trail O.8 keeps the five-year release open.')
    say('  ### ROUTED TO THE AUTHOR.')
    say('  anchor misses : %d %s' % (len(miss), miss))
    say('=' * 100)
    io.open(READREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), sources=out, fired=[o['id'] for o in fired], misses=miss), indent=1, ensure_ascii=False)
    open(RJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(RJSON + '.tmp', RJSON)
    print(NL.join(R))
    return 0 if not miss else 1


def main():
    Lr = []
    say = Lr.append
    rd = read(READREC)
    fails = [] if rd else ['the read record is absent']
    try:
        J = json.loads(read(RJSON))
    except Exception:
        J = dict(sources=[], fired=[], misses=['no json'])
    say('=' * 100)
    say('b425_components.py -- THE FALSIFIER READ, THE REPORT.')
    say('=' * 100)
    for o in J['sources']:
        say('  %-12s %-10s %s' % (o['id'], o['verdict'], o['title'][:70]))
    for needle in ('anchor misses : 0', 'ROUTED TO THE AUTHOR.', 'blob matches pin : True'):
        ok = needle in rd
        fails += [] if ok else [needle]
        say('  %-40s %s' % (needle, ok))
    n = len(J['sources'])
    same = [o for o in J['sources'] if o['same'] == 'SAME QUANTITY']
    und = [o for o in J['sources'] if o['verdict'] == 'UNDECIDED']
    say('')
    say('### THE EXPECTATION, ITS CLAUSES APART (R27):')
    say('  (L3) *the measured quantity is the one the lane fixed* -- ### **%s** (%d of %d read SAME QUANTITY; %s).'
        % ('MET' if len(same) == n and n else ('PARTLY MET' if same else 'REFUTED'), len(same), n,
           '; '.join('%s: %s' % (o['id'], o['same']) for o in J['sources'] if o['same'] != 'SAME QUANTITY') or 'none otherwise'))
    say('  (L3) *the condition is UNDECIDED at the result`s significance* -- ### **%s** (%d of %d UNDECIDED; FIRED at %s).'
        % ('MET' if len(und) == n and n else 'REFUTED', len(und), n, ', '.join(J['fired']) or 'none'))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b425_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(Lr) + NL)
    print(NL.join(Lr))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--locate' in sys.argv:
        sys.exit(run_locate())
    if '--read' in sys.argv:
        sys.exit(run_read())
    sys.exit(main())
