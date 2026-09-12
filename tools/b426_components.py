# -*- coding: utf-8 -*-
"""b426_components.py -- THE FALSIFIER RE-READ BY ADDRESS: THE COLLABORATION'S OWN SECOND-RELEASE PAPER.

### ### **THE SEARCH, THE SELECTION AND THE FETCH ARE READING (3)'S, RUN AFTER THE LOCK; THE THREE PARTS ARE
### READING (5)'S, DECIDED BY `(R38)`'S THRESHOLDS ON FIGURES THE SOURCE STATES IN ITS OWN WORDS.** ### This
### tool fits nothing, samples nothing, computes no likelihood and converts no significance: it fetches bytes,
### hashes them, writes their text to disk and quotes it.
###   --locate   the search (A1-A3), every result printed; the address by the rule; it is fetched, hashed and
###              extracted. data/b426_locate.txt, .json
###   --read     the lane's condition at its pin; the address's claim, significance and exclusion words quoted
###              from its extract; the three parts under (R38); b425's three restated; the combination both
###              ways; the routing. data/b426_the_address_read.txt, .json
###   --write    the two ordered corpus writes, each preserved verbatim with its sha256 BEFORE the edit.
###   (no flag)  the report and the expectation (L1), its two clauses apart.
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
SCRATCH = os.path.join(os.environ.get('TEMP', D), 'b426_sources')
LOC, LJSON = os.path.join(D, 'b426_locate.txt'), os.path.join(D, 'b426_locate.json')
READREC = os.path.join(D, 'b426_the_address_read.txt')
RJSON = os.path.join(D, 'b426_the_address_read.json')
NL = chr(10)
BS = chr(92)
API = 'https://export.arxiv.org/api/query?'
ABS, PDF = 'https://arxiv.org/abs/', 'https://arxiv.org/pdf/'
UA = {'User-Agent': 'relay-b426-read/1.0 (research seat; one query per three seconds)'}
CAP = 1
QUERIES = [('A1', 'ti:"DESI DR2"'),
           ('A2', 'all:"DESI" AND all:"Data Release 2" AND all:"dark energy"'),
           ('A3', 'ti:"DESI" AND ti:"cosmological constraints"')]
# ### THE ADDRESS RULE'S THREE TESTS -- reading (3) (i), (ii), (iii).
T_I = r'(?i)DESI.{0,60}(DR2|Data Release 2)|DR2.{0,40}DESI'
T_II = r'(?i)cosmolog\w*\s+constraint|cosmological\s+result|baryon\s+acoustic\s+oscillation|\bBAO\b'
T_III = r'(?i)DESI\s+Collaboration'
NS = {'a': 'http://www.w3.org/2005/Atom'}
FDOC = {'FANO': 'phase2/physics/FANO_DERIVATION_OF_LAMBDA.md', 'STORMER': 'phase2/physics/STORMER.md',
        'FD': 'phase2/physics-speculative/FORMATION_DISTANCE.md', 'REG': 'REGISTRY.md'}
PINS = {'FANO': 'b09635067c6a', 'STORMER': 'f1a08e554ab2', 'FD': '2560e1dc7462'}

# ### (R38), QUOTED FROM THE BANKED FERRY AND NEVER RETYPED FROM MEMORY.
FERRYFILE = os.path.join(D, 'b426_ferry.txt')
R38_ANCHOR = 'UNDER PRESSURE at a stated preference of three'
R38_END = 'and the act says so.'
R39_ANCHOR = '(R39) p2-d6 DOES NOT MOVE ON b425.'
R39_END = "author's to move if (R38) fires."

UNDER, FIRED_, UND = 'UNDER PRESSURE', 'FIRED', 'UNDECIDED'


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


RETRIES, BACKOFF = 8, 45


def get(url):
    """### **THE LISTING RATE-LIMITED AND THEN 503'd ON RUN 1** (`data/b426_locate_run1.txt`: three queries, three
    ### refusals). ### A patient retry is not a widened rule: the URL, the query and the cap are the face's, and only
    ### the WAITING changes. ### Every attempt and its error is printed by the caller."""
    last = None
    for k in range(RETRIES):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.status, r.read()
        except Exception as exc:
            last = exc
            print('      attempt %d/%d refused -- %s ; waiting %ds' % (k + 1, RETRIES, str(exc)[:90], BACKOFF),
                  flush=True)
            time.sleep(BACKOFF)
    raise last


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


def fold(s):
    return norm((s or '').replace('###', ' ').replace('**', '').replace('`', ''))


def qtext(text, start, end=None, cap=300):
    src, s0 = fold(text), fold(start)
    i = src.find(s0)
    if i < 0:
        return '### MISS'
    e0 = fold(end) if end else ''
    j = src.find(e0, i + len(s0)) if end else -1
    return src[i:j + len(e0)] if j > i else src[i:i + cap]


# =====================================================================================================
# ### THE THRESHOLD RULE, (R38)'S, APPLIED TO A STATED FIGURE. ### **COMPUTED FROM THE NUMBER, NEVER TYPED.**
# =====================================================================================================
def verdict_at(sigma, collaboration_own):
    """### (R38): UNDER PRESSURE at >= 3; FIRED at >= 5 from the collaboration's own paper; UNDECIDED below 3."""
    if sigma is None:
        return None
    if sigma >= 5.0 and collaboration_own:
        return FIRED_
    if sigma >= 3.0:
        return UNDER
    return UND


def weakest(vs):
    """### THE WEAKEST READING OF A SET. ### UNDECIDED < UNDER PRESSURE < FIRED."""
    order = {UND: 0, UNDER: 1, FIRED_: 2}
    vs = [v for v in vs if v]
    return min(vs, key=lambda v: order[v]) if vs else None


def strongest(vs):
    order = {UND: 0, UNDER: 1, FIRED_: 2}
    vs = [v for v in vs if v]
    return max(vs, key=lambda v: order[v]) if vs else None


ALT = 'https://arxiv.org/search/advanced?'
ALT_FIELD = {'A1': ('title', 'DESI DR2'),
             'A2': ('all', 'DESI Data Release 2 dark energy'),
             'A3': ('title', 'DESI cosmological constraints')}


def alt_entries(html):
    """### THE LISTING'S OTHER PUBLIC INTERFACE, PARSED. ### **THE QUERY IS THE FACE'S; ONLY THE ENDPOINT CHANGES,
    ### AND THE ACT SAYS SO.** ### Returns [(id, title, authors, published)] in the page's own order."""
    out = []
    for m in re.finditer(r'arXiv:(\d{4}\.\d{4,5})</a>(.*?)(?=<li class="arxiv-result">|\Z)', html, re.S):
        aid, rest = m.group(1), m.group(2)
        t = re.search(r'<p class="title is-5 mathjax">(.*?)</p>', rest, re.S)
        a = re.search(r'<p class="authors">(.*?)</p>', rest, re.S)
        d = re.search(r'Submitted\s*</span>\s*([0-9]+\s+\w+,\s+[0-9]{4})', rest, re.S)
        strip = lambda x: norm(re.sub(r'<[^>]+>', ' ', x or ''))
        out.append((aid, strip(t.group(1) if t else ''), strip(a.group(1) if a else ''),
                    strip(d.group(1) if d else '')))
    return out


def run_locate(alt=False):
    R = ['=' * 100, 'b426 -- THE SEARCH, THE SELECTION AND THE FETCH. ### READING (3), AFTER THE LOCK.', '=' * 100,
         '  at (UTC) : %s' % utc(), '  cap : %d address' % CAP, '']
    say = R.append
    if alt:
        return run_locate_alt(R, say)
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    seen, results = {}, []
    for tag, q in QUERIES:
        url = API + urllib.parse.urlencode({'search_query': q, 'sortBy': 'relevance', 'sortOrder': 'descending',
                                            'start': 0, 'max_results': 50})
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
            title, pub = norm(e.findtext('a:title', '', NS)), norm(e.findtext('a:published', '', NS))
            summ = norm(e.findtext('a:summary', '', NS))
            authors = '; '.join(norm(a.findtext('a:name', '', NS)) for a in e.findall('a:author', NS))
            ti = bool(re.search(T_I, title))
            tii = bool(re.search(T_II, title))
            tiii = bool(re.search(T_III, authors + ' ' + title + ' ' + summ))
            say('    %-14s %s  (i)%s (ii)%s (iii)%s  %s' % (base, pub[:10], 'Y' if ti else 'n', 'Y' if tii else 'n',
                                                            'Y' if tiii else 'n', title[:76]))
            if base not in seen:
                seen[base] = dict(id=base, version=aid, title=title, published=pub, abstract=summ,
                                  authors=authors[:400], i=ti, ii=tii, iii=tiii, queries=[tag],
                                  constraints=bool(re.search(r'(?i)cosmolog\w*\s+constraint', title)))
                results.append(seen[base])
            else:
                seen[base]['queries'].append(tag)
        time.sleep(3.5)
    qual = [r for r in results if r['i'] and r['ii'] and r['iii']]
    named = sorted([r for r in qual if r['constraints']], key=lambda r: r['published'])
    rest = sorted([r for r in qual if not r['constraints']], key=lambda r: r['published'])
    chosen = (named + rest)[:CAP]
    say('')
    say('-' * 100)
    say('### THE SELECTION, BY THE RULE OF READING (3).')
    say('-' * 100)
    say('  unique results : %d ; qualifying on (i), (ii) and (iii) : %d ; of those naming cosmological constraints : %d'
        % (len(results), len(qual), len(named)))
    for r in qual:
        say('    qualifying : %-14s %s %s%s' % (r['id'], r['published'][:10],
                                                '[CONSTRAINTS] ' if r['constraints'] else '', r['title'][:74]))
    if not chosen:
        say('  ### ### ### **NOT LOCATED.** ### No result satisfies (i), (ii) and (iii); the rule is not widened.')
    else:
        say('  ### CHOSEN, BY THE RULE, CAPPED AT %d : %s' % (CAP, [r['id'] for r in chosen]))
    sources = []
    for r in chosen:
        say('')
        say('-' * 100)
        say('### THE ADDRESS %s -- %s' % (r['id'], r['title']))
        say('-' * 100)
        say('  authors, as the listing gives them (first 400 chars) : %s' % r['authors'])
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
                    text = NL.join('=== PAGE %d ===%s%s' % (k + 1, NL, (p.extract_text() or ''))
                                   for k, p in enumerate(rd.pages))
                    npages = len(rd.pages)
                else:
                    t = body.decode('utf-8', 'replace')
                    t = re.sub(r'(?is)<(script|style).*?</' + BS + '1>', ' ', t)
                    text = norm(re.sub(r'<[^>]+>', ' ', t))
                    npages = 0
                out = os.path.join(D, 'b426_source_%s%s.txt' % (slug(r['id']), '_abs' if kind == 'abs' else ''))
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
        sources.append(src)
    say('')
    say('  ### ADDRESSES CHOSEN %d ; FETCHED IN FULL %d' % (len(sources), sum(1 for s in sources
                                                                             if s.get('pdf', {}).get('sha256')
                                                                             and s.get('abs', {}).get('sha256'))))
    say('=' * 100)
    io.open(LOC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), queries=QUERIES, results=results, chosen=[r['id'] for r in chosen], sources=sources),
                   indent=1, ensure_ascii=False)
    open(LJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(LJSON + '.tmp', LJSON)
    print(NL.join(R))
    return 0 if sources else 1


def run_locate_alt(R, say):
    """### **THE DECLARED ENDPOINT REFUSED. ### THIS IS A DEVIATION AND IT IS NAMED AS ONE.** ### The three queries
    ### are the locked face's, expressed in the other interface's own syntax; the listing is the same listing and the
    ### host is one BAR 10 already permits. ### **THE RULE IS NOT WIDENED: the three tests (i), (ii), (iii) and the
    ### cap of ONE are unchanged, and every result is printed.** ### Run 1 and run 2 stay on disk with every refusal."""
    say('  ### ### **DEVIATION, DECLARED: THE API ENDPOINT `export.arxiv.org` REFUSED ALL THREE QUERIES ACROSS TWO')
    say('  ### ### RUNS AND SIXTEEN ATTEMPTS PER QUERY (429 / 503; see `b426_locate_run1.txt` and')
    say('  ### ### `b426_locate_run2.txt`). ### THE SAME QUERIES ARE PUT TO THE SAME LISTING`S OTHER PUBLIC')
    say('  ### ### INTERFACE, `arxiv.org/search/advanced`. ### THE QUERY STRINGS AND THE SELECTION RULE ARE THE')
    say('  ### ### LOCKED FACE`S; ONLY THE ENDPOINT CHANGES, AND THE STANDING DEVIATION RULE CARRIES IT.**')
    if not os.path.isdir(SCRATCH):
        os.makedirs(SCRATCH)
    seen, results = {}, []
    for tag, _q in QUERIES:
        field, term = ALT_FIELD[tag]
        url = ALT + urllib.parse.urlencode({'advanced': '', 'terms-0-operator': 'AND', 'terms-0-term': term,
                                            'terms-0-field': field, 'classification-physics_archives': 'all',
                                            'start': 0, 'size': 50})
        say('-' * 100)
        say('### %s -- the face`s %r, put as field=%s term=%r' % (tag, dict(QUERIES)[tag], field, term))
        say('-' * 100)
        try:
            st, body = get(url)
        except Exception as exc:
            say('  ### NOT FETCHED -- %s' % exc)
            continue
        h = hashlib.sha256(body).hexdigest()
        open(os.path.join(SCRATCH, '%s_alt.html' % tag), 'wb').write(body)
        html = body.decode('utf-8', 'replace')
        ents = alt_entries(html)
        say('  status %s ; bytes %d ; sha256 %s' % (st, len(body), h))
        say('  results : %d' % len(ents))
        for aid, title, authors, pub in ents:
            ti = bool(re.search(T_I, title))
            tii = bool(re.search(T_II, title))
            tiii = bool(re.search(T_III, authors + ' ' + title))
            say('    %-14s %-18s (i)%s (ii)%s (iii)%s  %s' % (aid, pub[:18], 'Y' if ti else 'n', 'Y' if tii else 'n',
                                                              'Y' if tiii else 'n', title[:72]))
            if aid not in seen:
                seen[aid] = dict(id=aid, version=aid, title=title, published=pub, abstract='', authors=authors[:400],
                                 i=ti, ii=tii, iii=tiii, queries=[tag],
                                 constraints=bool(re.search(r'(?i)cosmolog\w*\s+constraint', title)))
                results.append(seen[aid])
            else:
                seen[aid]['queries'].append(tag)
        time.sleep(3.5)
    qual = [r for r in results if r['i'] and r['ii'] and r['iii']]
    named = sorted([r for r in qual if r['constraints']], key=lambda r: r['id'])
    rest = sorted([r for r in qual if not r['constraints']], key=lambda r: r['id'])
    chosen = (named + rest)[:CAP]
    say('')
    say('-' * 100)
    say('### THE SELECTION, BY THE RULE OF READING (3), UNCHANGED.')
    say('-' * 100)
    say('  unique results : %d ; qualifying on (i), (ii) and (iii) : %d ; of those naming cosmological constraints : %d'
        % (len(results), len(qual), len(named)))
    for r in qual:
        say('    qualifying : %-14s %s%s' % (r['id'], '[CONSTRAINTS] ' if r['constraints'] else '', r['title'][:74]))
    say('  ### **THE TIE-BREAK IS THE EARLIEST SUBMISSION; THIS INTERFACE GIVES A DATE ONLY TO THE DAY, SO THE')
    say('  ### ARXIV IDENTIFIER -- WHICH IS ISSUED IN SUBMISSION ORDER -- IS USED AND SAID TO BE USED.**')
    if not chosen:
        say('  ### ### ### **NOT LOCATED.** ### No result satisfies (i), (ii) and (iii); the rule is not widened.')
    else:
        say('  ### CHOSEN, BY THE RULE, CAPPED AT %d : %s' % (CAP, [r['id'] for r in chosen]))
    sources = []
    for r in chosen:
        say('')
        say('-' * 100)
        say('### THE ADDRESS %s -- %s' % (r['id'], r['title']))
        say('-' * 100)
        say('  authors, as the listing gives them (first 400 chars) : %s' % r['authors'])
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
                    text = NL.join('=== PAGE %d ===%s%s' % (k + 1, NL, (p.extract_text() or ''))
                                   for k, p in enumerate(rd.pages))
                    npages = len(rd.pages)
                else:
                    t = body.decode('utf-8', 'replace')
                    t = re.sub(r'(?is)<(script|style).*?</' + BS + '1>', ' ', t)
                    text = norm(re.sub(r'<[^>]+>', ' ', t))
                    npages = 0
                    ab = re.search(r'(?is)Abstract:?\s*(.{80,3000}?)\s*(Comments|Subjects|Cite as)', text)
                    src_abs = norm(ab.group(1)) if ab else ''
                    r['abstract'] = src_abs
                out = os.path.join(D, 'b426_source_%s%s.txt' % (slug(r['id']), '_abs' if kind == 'abs' else ''))
                io.open(out, 'w', encoding='utf-8', newline=NL).write(text + NL)
                src[kind] = dict(url=url, status=st, bytes=len(body), sha256=h, extract=os.path.basename(out),
                                 pages=npages, chars=len(text))
                say('  %-4s %s  status %s  bytes %d  sha256 %s  -> data/%s%s'
                    % (kind, url, st, len(body), h, os.path.basename(out), ('  (%d pages)' % npages) if npages else ''))
            except Exception as exc:
                src[kind] = dict(url=url, status='NOT FETCHED', error=str(exc)[:200])
                say('  %-4s %s  ### NOT FETCHED -- %s' % (kind, url, str(exc)[:160]))
            time.sleep(3.5)
        src['abstract'] = r.get('abstract', '')
        say('  the abstract, from the abstract page :')
        for w in wrap(r.get('abstract', '') or '### NOT EXTRACTED', 94):
            say('      | %s' % w)
        sources.append(src)
    say('')
    say('  ### ADDRESSES CHOSEN %d ; FETCHED IN FULL %d' % (len(sources), sum(1 for s in sources
                                                                             if s.get('pdf', {}).get('sha256')
                                                                             and s.get('abs', {}).get('sha256'))))
    say('=' * 100)
    io.open(LOC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), queries=QUERIES, endpoint='arxiv.org/search/advanced (DEVIATION, declared)',
                        results=results, chosen=[r['id'] for r in chosen], sources=sources), indent=1, ensure_ascii=False)
    open(LJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(LJSON + '.tmp', LJSON)
    print(NL.join(R))
    return 0 if sources else 1


def lane_text(key):
    return subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + FDOC[key]], capture_output=True).stdout.decode('utf-8', 'replace')


def source_text(aid, where_):
    if where_ == 'abs':
        L = json.loads(read(LJSON))
        return next((r['abstract'] for r in L['results'] if r['id'] == aid), '')
    return read(os.path.join(D, 'b426_source_%s.txt' % slug(aid)))


# =====================================================================================================
# ### THE SEAT'S READING OF THE ADDRESS, ENCODED AFTER THE LOCATE RUN WAS READ. ### EVERY QUOTATION IS
# ### RE-FOUND IN THE SOURCE'S OWN TEXT ON DISK BEFORE IT IS PRINTED, AND EVERY FIGURE IS THE SOURCE'S.
# =====================================================================================================
DECIDE = {
    '2503.14738': dict(
        claim=('abs', 'This solution is preferred over', 'depending on which SNe sample is used.'),
        sig=('pdf', 'The significance of rejection of', 'without any SNe.'),
        excl=('abs', 'Unless there is an unknown systematic error', 'offers a possible solution.'),
        excl_note=('pdf', 'is not excluded at 95%.', None),
        a=[('pdf', 'we will primarily use the so-called Chevallier', 'parametrization of eq. (9).'),
           ('pdf', 'the ΛCDM limit ( w0 = −1, wa = 0) lies at their intersection.', None)],
        a_read='SAME QUANTITY -- the dark-energy equation of state `w(a)` in the Chevallier-Polarski-Linder '
               'parametrization, tested against the ΛCDM limit `w0 = −1, wa = 0`, which IS the lane`s `w = −1`',
        low=2.8, high=4.2, excludes=False,
        figure_where='the abstract: *"the preference for a dynamical dark energy model over ΛCDM ranges from '
                     '2.8-4.2σ depending on which SNe sample is used"*; the body gives the same range term by term, '
                     '*"2.8σ, 3.8σ and 4.2σ ... and 3.1σ for DESI+CMB without any SNe"*',
        why='at the range`s LOW end the condition reads UNDECIDED and at its HIGH end UNDER PRESSURE, so the '
            'collaboration`s own paper SPANS (R38)`s three-sigma threshold; and FIVE SIGMA IS NOT REACHED AT EITHER '
            'END, so (R38)`s FIRED clause is not reached by the one source that could reach it alone'),
}

# ### b425's THREE, RE-SCORED UNDER (R38) FROM b425's OWN BANKED FIGURES. ### (id, low, high, where the figures
# ### are stated). ### **THE FIGURES ARE NOT RE-FETCHED AND NOT RE-DERIVED; they are b425's banked quotations.**
B425 = [('2609.10567', 2.1, 3.7, 'the abstract: "the significances are 2.1~3.7 sigma"'),
        ('2609.10133', 2.50, 2.50, 'the abstract: "the standard model is excluded at the 2.50 sigma CL"'),
        ('2609.05321', 3.4, 4.0, 'the abstract: "increases from 3.4 sigma to 4.0 sigma"')]


def span(low, high, own):
    """### A SOURCE STATING A RANGE IS READ AT BOTH ENDS, AND SPANNING IS RECORDED AS SPANNING."""
    a, b = verdict_at(low, own), verdict_at(high, own)
    return a, b, (a != b)


def run_read():
    R = ['=' * 100, 'b426 -- THE FALSIFIER RE-READ BY ADDRESS, UNDER (R38).', '=' * 100, '  at (UTC) : %s' % utc(), '']
    say = R.append
    miss = []
    ferry = read(FERRYFILE)
    say('-' * 100)
    say('### (R38) AND (R39), QUOTED FROM THE BANKED FERRY.')
    say('-' * 100)
    r38 = qtext(ferry, R38_ANCHOR, R38_END, cap=600)
    r39 = qtext(ferry, R39_ANCHOR, R39_END, cap=700)
    for lab, q in (('(R38), the condition', r38), ('(R39), the register note', r39)):
        if q == '### MISS':
            miss.append(lab)
        say('  %s :' % lab)
        for w in wrap(q, 94):
            say('      | %s' % w)
    say('  ### THE THRESHOLDS, READ OFF THAT TEXT AND APPLIED AS NUMBERS: UNDER PRESSURE at >= 3 sigma ;')
    say('  ### FIRED at >= 5 sigma from the collaboration`s own paper or two independent analyses each at 5 ;')
    say('  ### UNDECIDED below 3 sigma. ### A SOURCE`S OWN WORD IS QUOTED AND NEVER GOVERNS.')

    say('')
    say('-' * 100)
    say('### THE LANE`S COMMITMENT AND ITS CONDITION, AT THEIR PINS.')
    say('-' * 100)
    for key, lab, s, e in (('FANO', 'the assignment', '4. The equation-of-state assignment sends weight-1 elements',
                            'to a symmetry-breaking residual.'),
                           ('FANO', 'the residual`s w, the lane`s own reach', 'The diagonal residual',
                            'manifests observationally.'),
                           ('STORMER', 'the pending test', 'DESI 5-year', 'for DE/visible'),
                           ('FD', 'THE CONDITION', '4. **DESI year-3 tests w = −1.**', 'refutes the decomposition.')):
        t = lane_text(key)
        blob = subprocess.run(['git', '-C', PP, 'rev-parse', 'HEAD:' + FDOC[key]], capture_output=True,
                              text=True).stdout.strip()
        qq = qtext(t, s, e)
        miss += ['%s:%s' % (key, lab)] if qq == '### MISS' else []
        say('  %s -- %s (%s ; blob %s ; blob matches pin : %s)' % (lab, FDOC[key], key, blob[:12],
                                                                   blob.startswith(PINS[key])))
        for w in wrap(qq, 94):
            say('      | %s' % w)

    L = json.loads(read(LJSON))
    out = []
    for aid in L['chosen']:
        dd = DECIDE.get(aid)
        src = next((s for s in L['sources'] if s['id'] == aid), {})
        say('')
        say('=' * 100)
        say('### THE ADDRESS %s -- %s' % (aid, src.get('title', '')))
        say('=' * 100)
        say('  pdf sha256 %s' % src.get('pdf', {}).get('sha256', '### NOT FETCHED'))
        say('  abstract page sha256 %s' % src.get('abs', {}).get('sha256', '### NOT FETCHED'))
        say('  the collaboration named in the listing`s author field : %s'
            % bool(re.search(T_III, src.get('authors', '') + ' ' + src.get('title', ''))))
        if not dd:
            say('  ### NO READING ENCODED FOR THIS ADDRESS.')
            miss.append(aid)
            continue

        def show(label, spec, indent='  '):
            wh, s, e = spec
            t = qtext(source_text(aid, wh), s, e, cap=420)
            if t == '### MISS':
                miss.append('%s:%s' % (aid, label))
            say('%s%s (%s) :' % (indent, label, 'the listing`s abstract' if wh == 'abs' else 'the PDF`s text'))
            for w in wrap(t, 92):
                say('%s    | %s' % (indent, w))
            return t

        say('  THE STATED PREFERENCE :')
        claim = show('    the paper`s own sentence', dd['claim'], '  ')
        say('  ITS STATED SIGNIFICANCE :')
        sig = show('    the paper`s own figure', dd['sig'], '  ')
        say('  ITS OWN WORDS ON WHETHER A COSMOLOGICAL CONSTANT IS EXCLUDED :')
        if dd.get('excl'):
            exc = show('    the paper`s own closing sentence', dd['excl'], '  ')
            say('    ### **THE WORD IT USES IS `CHALLENGED`, NOT `EXCLUDED`.** ### The stem *exclud* occurs %d time(s)'
                % len(re.findall(r'(?i)exclud', source_text(aid, 'pdf'))))
            say('    ### in the PDF`s text and NONE of them says the cosmological constant is excluded; the nearest is a')
            say('    ### figure caption whose subject the text layer drops, printed here rather than paraphrased:')
            if dd.get('excl_note'):
                show('      the caption fragment, as the text layer renders it', dd['excl_note'], '  ')
        else:
            exc = ''
            say('      ### **ABSENT** -- %s' % dd.get('excl_absent', 'no sentence of the source speaks to exclusion'))
        say('')
        say('  PART (a) -- IS THE MEASURED QUANTITY THE ONE THE LANE FIXED?')
        for spec in dd['a']:
            show('    the paper`s parameterization', spec, '  ')
        say('    ### %s. ### And the lane`s own reach stands beside it: the residual`s w is unspecified (FANO line 246).'
            % dd['a_read'])
        say('  PART (b) -- WHAT THE CONDITION NOW SAYS, UNDER (R38):')
        say('    the lane`s sentence is unchanged -- *"Evolving dark energy refutes the decomposition"*')
        say('    (FORMATION_DISTANCE.md line 160) -- and (R38) supplies the thresholds it never stated.')
        say('  PART (c) -- AT THE PAPER`S OWN FIGURE, BY (R38)`S THRESHOLDS:')
        lo, hi = dd['low'], dd['high']
        va, vb, sp = span(lo, hi, True)
        say('    the figures the paper states : %s to %s sigma  (%s)' % (lo, hi, dd['figure_where']))
        say('    at the LOW end  %-5s sigma -> %s' % (lo, va))
        say('    at the HIGH end %-5s sigma -> %s' % (hi, vb))
        say('    ### ### **VERDICT [%s] : %s** -- %s' % (aid, (('SPANNING %s / %s' % (va, vb)) if sp else va),
                                                          dd['why']))
        out.append(dict(id=aid, title=src.get('title', ''), low=lo, high=hi, low_verdict=va, high_verdict=vb,
                        spanning=sp, claim=claim, sig=sig, exclusion=exc, a_read=dd['a_read'],
                        same=dd['a_read'].split(' --')[0], collaboration=True))

    say('')
    say('=' * 100)
    say('### b425`S THREE SOURCES, RESTATED BESIDE THE ADDRESS AND RE-SCORED UNDER (R38).')
    say('=' * 100)
    b425j = json.loads(read(os.path.join(D, 'b425_the_read.json')) or '{"sources": []}')
    prior = []
    for aid, lo, hi, where in B425:
        old = next((s['verdict'] for s in b425j['sources'] if s['id'] == aid), '### NOT IN b425`S RECORD')
        va, vb, sp = span(lo, hi, False)
        say('  %-12s b425 read %-10s  figures %s to %s sigma  (%s)' % (aid, old, lo, hi, where))
        say('               under (R38): low -> %-14s high -> %-14s %s'
            % (va, vb, '### SPANNING' if sp else ''))
        prior.append(dict(id=aid, b425=old, low=lo, high=hi, low_verdict=va, high_verdict=vb, spanning=sp))
    say('  ### **AND THE ONE b425 READ `FIRED` ON ITS OWN WORD READS %s UNDER (R38)**, because (R38) keys on the'
        % next(p['high_verdict'] for p in prior if p['id'] == '2609.10133'))
    say('  ### threshold and 2.50 sigma is below three. ### **A SOURCE`S OWN WORD IS QUOTED AND NEVER GOVERNS.**')

    say('')
    say('=' * 100)
    say('### THE COMBINATION, BOTH WAYS, AND THE RULE`S OWN DIVERGENCE.')
    say('=' * 100)
    allv_low = [o['low_verdict'] for o in out] + [p['low_verdict'] for p in prior]
    allv_high = [o['high_verdict'] for o in out] + [p['high_verdict'] for p in prior]
    anyclause = strongest(allv_high)
    weakclause = weakest(allv_low)
    say('  the set read at address : %d source(s) -- the collaboration`s own paper and b425`s three.'
        % (len(out) + len(prior)))
    say('  ### CLAUSE 1, *"from any source read at address"*, read at each source`s strongest end : ### **%s**'
        % anyclause)
    say('  ### CLAUSE 2, *"combined by the WEAKEST reading, not the strongest"*, at each source`s weakest end : ### **%s**'
        % weakclause)
    diverge = (anyclause != weakclause)
    if diverge:
        say('  ### ### ### **THE TWO CLAUSES OF (R38) DO NOT AGREE ON THIS SET.** ### The divergence is the RULE`S')
        say('  ### ### and not the set`s, and it is printed rather than repaired.')
        say('  ### ### **THE COMBINED READING CARRIED IS THE WEAKEST: %s** -- the ruling`s own last sentence on' % weakclause)
        say('  ### ### combination governs combination. ### **THE DIVERGENCE IS ROUTED TO THE AUTHOR, UNRULED.**')
    else:
        say('  ### The two clauses agree on this set : ### **%s**' % weakclause)
    say('')
    say('  ### ### **FIRED REQUIRES FIVE SIGMA. ### NO SOURCE IN THIS SET STATES FIVE SIGMA AT EITHER END,')
    say('  ### ### SO (R38)`S FIRED CLAUSE IS NOT REACHED AND `p2-d6` DOES NOT MOVE.**'
        if FIRED_ not in allv_high else
        '  ### ### **(R38)`S FIRED CLAUSE IS REACHED; THE REGISTER ROW IS NAMED AS THE AUTHOR`S TO MOVE.**')
    say('  ### No lane verdict is changed by this seat.')
    say('  anchor misses : %d %s' % (len(miss), miss))
    say('=' * 100)
    io.open(READREC, 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    d = json.dumps(dict(at=utc(), address=out, prior=prior, any_clause=anyclause, weakest_clause=weakclause,
                        diverge=diverge, fired=(FIRED_ in allv_high), misses=miss), indent=1, ensure_ascii=False)
    open(RJSON + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(RJSON + '.tmp', RJSON)
    print(NL.join(R))
    return 0 if not miss else 1


# =====================================================================================================
# ### THE TWO ORDERED CORPUS WRITES. ### **PRESERVE FIRST, WITH A SHA256, THEN EDIT, THEN READ BACK.**
# =====================================================================================================
FDPATH = os.path.join(PP, 'phase2', 'physics-speculative', 'FORMATION_DISTANCE.md')
REGPATH = os.path.join(PP, 'REGISTRY.md')
FD_LINE160 = ('4. **DESI year-3 tests w = −1.** The 14 = 7 × 2 decomposition requires w = −1 exactly. '
              'Evolving dark energy refutes the decomposition.')
FD_APPEND = ('   **Threshold clause, appended 2026-09-11 (b426) under author ruling `(R38)`, the sentence above kept:** '
             'the condition reads **UNDER PRESSURE** at a stated preference of three sigma or more from any source read '
             'at address; **FIRED** at five sigma from the collaboration\'s own paper or from two independent analyses '
             'each at five; **UNDECIDED** below three. A source\'s own word is quoted and never governs, and disagreeing '
             'sources are combined by the **weakest** reading, not the strongest. *(Read at b426: `relay/data/b426_the_address_read.txt`.)*')
REG_STATUS_OLD = '| p2-d6 | Formation Distance Synthesis | `phase2/physics-speculative/FORMATION_DISTANCE.md` | v0.2 | ◻ | READY | 2,015 | TBD |'


def preserve(tag, text):
    p = os.path.join(D, 'b426_preserved_%s.txt' % tag)
    if not os.path.exists(p):
        io.open(p, 'w', encoding='utf-8', newline=NL).write(
            'b426 -- %s, PRESERVED VERBATIM BEFORE ANY EDIT.%s  preserved at (UTC) : %s%s  sha256 : %s%s%s%s'
            % (tag, NL, utc(), NL, hashlib.sha256(text.encode('utf-8')).hexdigest(), NL, NL, text + NL))
    return p


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


def run_write():
    R = ['=' * 100, 'b426 -- THE TWO ORDERED CORPUS WRITES. ### (R38) AND (R39). ### PRESERVE FIRST.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    fails = []
    try:
        J = json.loads(read(RJSON))
    except Exception:
        J = dict(fired=None)
    say('  the read`s combined verdict : any-clause %s ; weakest-clause %s ; FIRED reached : %s'
        % (J.get('any_clause'), J.get('weakest_clause'), J.get('fired')))
    if J.get('fired'):
        say('  ### **FIRED IS REACHED -- THE REGISTER ROW IS THE AUTHOR`S TO MOVE AND THIS SEAT STILL DOES NOT MOVE IT.**')

    # ---- (a) FORMATION_DISTANCE.md, per (R38)
    say('')
    say('-' * 100)
    say('### (a) FORMATION_DISTANCE.md LINE 160 -- (R38)`S CLAUSE APPENDED, THE SENTENCE KEPT.')
    say('-' * 100)
    fd = read(FDPATH)
    lines = fd.split(NL)
    p = preserve('fd_line160', FD_LINE160)
    say('  preservation record written before the edit : %s (%s)' % (os.path.exists(p), os.path.basename(p)))
    idx = [i for i, ln in enumerate(lines) if ln.strip() == FD_LINE160]
    say('  line 160 located by its own text : %s (1-indexed %s)' % (bool(idx), [i + 1 for i in idx]))
    if not idx:
        say('  ### HARD FAILURE -- the sentence is not in the file; nothing written.')
        fails.append('fd anchor')
    elif FD_APPEND in fd:
        say('  ### THE CLAUSE IS ALREADY PRESENT -- NOTHING WRITTEN.')
    else:
        i = idx[0]
        new = lines[:i + 1] + [FD_APPEND] + lines[i + 1:]
        write_bytes(FDPATH, NL.join(new))
        back = read(FDPATH)
        bl = back.split(NL)
        ok = (bl[i] == FD_LINE160 and bl[i + 1] == FD_APPEND
              and back.replace(NL + FD_APPEND, '', 1) == fd and len(bl) == len(lines) + 1)
        say('  lines before %d, after %d ; line 160 byte-identical : %s ; the pin`s text is the new text less the'
            % (len(lines), len(bl), bl[i] == FD_LINE160))
        say('  one inserted line : %s' % (back.replace(NL + FD_APPEND, '', 1) == fd))
        say('  ### %s' % ('PASS' if ok else '### FAIL ###'))
        if not ok:
            fails.append('fd write')
    fd2 = read(FDPATH)
    say('  the clause present exactly once : %s' % (fd2.count(FD_APPEND) == 1))
    say('  the kept sentence present exactly once : %s' % (fd2.count(FD_LINE160) == 1))

    # ---- (b) REGISTRY.md p2-d6, per (R39)
    say('')
    say('-' * 100)
    say('### (b) REGISTRY.md p2-d6 -- THE STATUS CELL GAINS A NOTE; EVERY OTHER CELL BYTE-IDENTICAL.')
    say('-' * 100)
    reg = read(REGPATH)
    rows = [ln for ln in reg.split(NL) if ln.startswith('| p2-d6 |')]
    say('  the row found : %s' % bool(rows))
    if not rows:
        say('  ### HARD FAILURE -- the p2-d6 row is absent; nothing written.')
        fails.append('reg anchor')
        rows = ['']
    p2 = preserve('registry_p2d6', rows[0])
    say('  preservation record written before the edit : %s (%s)' % (os.path.exists(p2), os.path.basename(p2)))
    old = rows[0]
    cells = old.strip().strip('|').split('|')
    say('  cells : %d ; the status cell (6 of 8) reads : %r' % (len(cells), cells[5].strip() if len(cells) > 5 else ''))
    note = REG_NOTE(J)
    if NOTEMARK in reg:
        say('  ### THE NOTE IS ALREADY PRESENT -- NOTHING WRITTEN.')
    elif len(cells) == 8 and cells[5].strip() == 'READY':
        newcells = list(cells)
        newcells[5] = ' READY %s ' % note
        new_row = '|' + '|'.join(newcells) + '|'
        write_bytes(REGPATH, reg.replace(old, new_row, 1))
        back = read(REGPATH)
        rows2 = [ln for ln in back.split(NL) if ln.startswith('| p2-d6 |')]
        c2 = rows2[0].strip().strip('|').split('|') if rows2 else []
        same = [k for k in range(8) if k != 5 and len(c2) == 8 and c2[k] == cells[k]]
        ok = (len(c2) == 8 and len(same) == 7 and NOTEMARK in back
              and len(back.split(NL)) == len(reg.split(NL))
              and c2[5].strip().startswith('READY'))
        say('  cells byte-identical other than the status cell : %d of 7' % len(same))
        say('  the status cell still begins READY : %s ; line count unchanged : %s'
            % (bool(c2) and c2[5].strip().startswith('READY'), len(back.split(NL)) == len(reg.split(NL))))
        say('  ### %s' % ('PASS' if ok else '### FAIL ###'))
        if not ok:
            fails.append('registry write')
    else:
        say('  ### HARD FAILURE -- the row`s shape is not the one this act read at survey; nothing written.')
        fails.append('registry shape')
    reg2 = read(REGPATH)
    say('  the note present exactly once : %s' % (reg2.count(NOTEMARK) == 1))
    say('  the register sentence (the row`s title cell) unchanged : %s'
        % ('| p2-d6 | Formation Distance Synthesis |' in reg2))
    say('')
    say('  ### ### **WRITES ORDERED : 2. ### FAILURES : %d %s**' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b426_writes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(R) + NL)
    print(NL.join(R))
    return 1 if fails else 0


NOTEMARK = '**NOTE (b426, `(R39)`)'


def REG_NOTE(J):
    return (NOTEMARK + ':** the lane\'s falsification condition is **under active test**. `(R38)` supplies the '
            'thresholds the condition never stated; at b425 three independent analyses state a preference for an '
            'evolving equation of state at 2.1–4.0σ and **none reaches (R38)\'s five-sigma FIRED threshold**; at b426 '
            'the collaboration\'s own second-release paper was read by address. **Combined reading under `(R38)`: '
            '%s** (its "any source" clause reads %s on the same set — the rule\'s own divergence, routed to the author '
            'unruled). **The row does not move, the register sentence is unchanged, and it is the author\'s to move if '
            '`(R38)` fires.** *(relay `data/b426_the_address_read.txt`.)*'
            % (J.get('weakest_clause') or 'NOT COMPUTED', J.get('any_clause') or 'NOT COMPUTED'))


def main():
    Lr = []
    say = Lr.append
    rd = read(READREC)
    fails = [] if rd else ['the read record is absent']
    try:
        J = json.loads(read(RJSON))
    except Exception:
        J = dict(address=[], prior=[], misses=['no json'])
    say('=' * 100)
    say('b426_components.py -- THE FALSIFIER RE-READ BY ADDRESS, THE REPORT.')
    say('=' * 100)
    for o in J.get('address', []):
        say('  ADDRESS  %-12s %s to %s sigma  low %-14s high %-14s  %s'
            % (o['id'], o['low'], o['high'], o['low_verdict'], o['high_verdict'], o['title'][:52]))
    for p in J.get('prior', []):
        say('  b425     %-12s %s to %s sigma  low %-14s high %-14s  (b425 read %s)'
            % (p['id'], p['low'], p['high'], p['low_verdict'], p['high_verdict'], p['b425']))
    say('  ### any-clause %s ; weakest-clause %s ; the two diverge : %s ; FIRED reached : %s'
        % (J.get('any_clause'), J.get('weakest_clause'), J.get('diverge'), J.get('fired')))
    for needle in ('anchor misses : 0', 'blob matches pin : True', 'No lane verdict is changed by this seat.'):
        ok = needle in rd
        fails += [] if ok else [needle]
        say('  %-56s %s' % (needle, ok))
    A = J.get('address', [])
    n = len(A)
    same = [o for o in A if o['same'] == 'SAME QUANTITY']
    excl = [o for o in A if o.get('excludes')]
    inband = [o for o in A if o['low'] >= 3.0 and o['high'] <= 4.0]
    lo = [o['low'] for o in A]
    hi = [o['high'] for o in A]
    say('')
    say('### THE EXPECTATION, ITS CLAUSES APART (R27). ### **AND EACH CLAUSE`S OWN HALVES ARE PRINTED APART TOO,')
    say('### BECAUSE THEY DO NOT AGREE AND A SINGLE WORD OVER THEM WOULD BE AN AVERAGE.**')
    say('  (L1) *the collaboration`s paper states a preference between three and four sigma and excludes nothing*')
    say('       -- half one, *between three and four sigma* : ### **%s** (the paper states %s-%s sigma; a range '
        'wholly inside 3-4 sigma at %d of %d).'
        % ('MET' if (n and len(inband) == n) else 'REFUTED', min(lo) if lo else '-', max(hi) if hi else '-',
           len(inband), n))
    say('       -- half two, *excludes nothing*            : ### **%s** (%d of %d state an exclusion of the '
        'cosmological constant; the word the paper uses is CHALLENGED).'
        % ('MET' if (n and not excl) else 'REFUTED', len(excl), n))
    say('  (L1) *so the lane reads UNDER PRESSURE and not FIRED*')
    say('       -- half one, *UNDER PRESSURE*              : ### **%s** under the clause the act carries (the '
        'weakest reading: %s); ### **%s** under the ruling`s other clause (any source at address: %s).'
        % ('MET' if J.get('weakest_clause') == UNDER else 'REFUTED', J.get('weakest_clause'),
           'MET' if J.get('any_clause') == UNDER else 'REFUTED', J.get('any_clause')))
    say('       -- half two, *and not FIRED*               : ### **%s** (FIRED reached : %s; five sigma is not '
        'stated at either end of any source in the set).'
        % ('MET' if not J.get('fired') else 'REFUTED', J.get('fired')))
    say('  ### ### **AND THE PART (a) READING, WHICH THE EXPECTATION DID NOT NAME:** %d of %d read SAME QUANTITY.'
        % (len(same), n))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b426_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(Lr) + NL)
    print(NL.join(Lr))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--locate' in sys.argv:
        sys.exit(run_locate('--alt' in sys.argv))
    if '--read' in sys.argv:
        sys.exit(run_read())
    if '--write' in sys.argv:
        sys.exit(run_write())
    sys.exit(main())
