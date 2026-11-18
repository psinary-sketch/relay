# -*- coding: utf-8 -*-
"""b760, (R370)(7) AND (8): WHICH STRUCTURE CONFINES v2.5.0 BY THE FORM OF AN EDITION (I-16, OPEN_TRAILS :11864) AND THE CLAUSES I-17 TO
I-33 AS THEY APPLY, COMPOSED FROM v2.4.0'S BYTES AS b726 WROTE v2.4.0 (tools/b726_edition.py); AND THE QUOTATION SEARCH OF b690 ROW (2) IN THE
PAPER FORM b708 RAN (data/b708_quote.json, data/b708_cut.txt).

  python -X utf8 -I -u tools/b760_edition.py dry            compose, read, score and print; nothing written
  python -X utf8 -I -u tools/b760_edition.py write          the same, then day1/Which_Structure_Confines_v2_5_0.md and data/b760_edition_diff.txt
  python -X utf8 -I -u tools/b760_edition.py quote [dry]    (8) for the edition, before its commit: data/b760_quote.json
  python -X utf8 -I -u tools/b760_edition.py cut [<pp commit>] [dry]   data/b760_cut.json and data/b760_wsc_cut.txt: each key's distance, the residues
  python -X utf8 -I -u tools/b760_edition.py late [dry]     (8)'s late search over BLOCK D of data/b759_text.txt: data/b760_late_quotes.txt
  python -X utf8 -I -u tools/b760_edition.py controls       (7)'s controls read again, the written file against the composition

THE COMPOSITION. BLOCK W of data/b760_text.txt (its sha256 equal to (R370) PATHS): 23 keys, each asserted at its line of v2.4.0 before anything is
composed -- by its line's sha256 where the block gives one (that line alone carrying it), else by its OLD standing once in the file and at that
line -- then applied (WHOLE, PART, REMOVE, PARA-BEFORE, PARA-AFTER, ROW-AFTER, INLINE-AFTER); W14 where data/b760_discharge.json reads (6) STANDS.
BLOCK V appended after v2.4.0's last line and a blank line, its fields filled: DATE (UTC, at the run), AX (run 44162171267's axioms file, read
beside data/b759_outcomes.txt :16), ORDERLINE and CLASSROW (data/b760_discharge.json), REWRITES and ADDITIONS (one row a key, this edition's
line, v2.4.0's wording, v2.5.0's wording, the key's STATUS). The line numbers of a STATUS or of BLOCK V that name this edition's own lines are
re-pinned to the edition's (I-22) by the table REPIN, every other ':N' of those texts printed with the file it names.
THE RESTATEMENT CLAUSE (I-29, OPEN_TRAILS :12192, the author's answer before b592's seal): a marked row's reading extends to an unmarked
sentence of the same edition restating the same claim, rewritten with minimal substitution, the rest unchanged, listed in the back matter with
both wordings and counted under H28b. The read is printed phrase by phrase over the unmarked sentences up to the first ERA annotation, each hit
with its disposition from the table DISPO; a hit the table does not hold refuses the write (HELD at that sentence). One substitution stands in
RESTATE, in the words W2 gives, and it is listed as a row of the rewrites table.

THE IDENTIFIERS ((R370) N5 and (7)): v2.4.0's byline (:3) and two self-citations (:164, :166) are carried as v2.4.0 carries them, W0 changing
the version and the month alone; no tool line prints them (their digests alone); the counts of the author's name, ORCID and previous address
and of github.com/ are compared between v2.4.0 and the edition, and read 0 in every added text and every bank, the words never printed. A line
that QUOTES is entered by path, line and sha256 alone; its words are neither printed nor banked.
"""
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
NL = '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
KERNEL = 'D:/SIDE-explicit-formula'
SIDE_KERNEL = 'D:/SIDE-kernel'
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b760'
V231 = 'day1/Which_Structure_Confines.md'
V24 = 'day1/Which_Structure_Confines_v2_4_0.md'
V25 = 'day1/Which_Structure_Confines_v2_5_0.md'
FAMILY = 'day1/Which_Structure_Confines.md'
V24_SHA = 'b9d5b35ac4849f3e'   # ### (R370)(7): v2.4.0's bytes, 347 lines
V24_LINES = 347
ID_LINES = (3, 164, 166)   # ### the byline and the two self-citations: never printed
TEXT = 'b760_text.txt'
TEXT_SHA = '7c8fe2f89718604a4cc13b61b6f5b94b0dcd2582044694557f2741d233ef3472'   # ### (R370) PATHS, data/b760_ferry.txt :7
DISCHARGE = 'b760_discharge.json'
RUN = '44162171267'
AXFILE = 'D:/b759-runs/ef-44162171267/build-module-44162171267/axioms.txt'   # ### b759's download of the run's axioms file, read as text
OUTCOMES = 'b759_outcomes.txt'
TAG, MAIN = 'v0.41', 'a3aad4cc'
STANDARD = {'propext', 'Classical.choice', 'Quot.sound'}
KEYS = ['W%d' % i for i in range(24) if i != 10]
BANK = os.path.join(D, 'b760_edition_diff.txt')
QBANK = os.path.join(D, 'b760_quote.json')
CBANK = os.path.join(D, 'b760_cut.json')
CTXT = os.path.join(D, 'b760_wsc_cut.txt')
LBANK = os.path.join(D, 'b760_late_quotes.txt')
LJSON = os.path.join(D, 'b760_late_quotes.json')   # ### b760 events (66): the late search's rows, quoting lines, orders and readings, for Component 5's ledger tool
BLOCK_D = 'b759_text.txt'

# ### the twelve Lean names of BLOCK W and BLOCK V at v0.41: (path under SIDEExplicitFormula/, line, fully-qualified name)
LN = (('Schema/ZQ/Continuation.lean', 221, 'SIDEExplicitFormula.Schema.ZQ.zq_continuation'),
      ('Schema/ZQ/Mechanism/NoEuler.lean', 99, 'SIDEExplicitFormula.Schema.ZQ.zq_coeff_not_multiplicative'),
      ('Schema/ZQ/Mechanism/NoEuler.lean', 112, 'SIDEExplicitFormula.Schema.ZQ.zeta_isMultiplicative_control'),
      ('Schema/ZQ/OffZero/SP4.lean', 32, 'SIDEExplicitFormula.Schema.ZQ.OffZero.zq_offline_zero'),
      ('Schema/Wide/HalfScaleControl.lean', 44, 'SIDEExplicitFormula.Schema.ZQ.zq_weil_positivity_fails'),
      ('Schema/ZQ/EF/Main.lean', 198, 'SIDEExplicitFormula.Schema.ZQ.EF.zq_explicit_formula_instance'),
      ('Schema/ZQ/EF/Main.lean', 194, 'SIDEExplicitFormula.Schema.ZQ.EF.zq_count_instance'),
      ('Schema/ZQ/Mechanism/CoeffSign.lean', 291, 'SIDEExplicitFormula.Schema.ZQ.cQ_not_nonneg'),
      ('Schema/ZQ/Mechanism/CoeffSign.lean', 301, 'SIDEExplicitFormula.Schema.ZQ.vonMangoldt_nonneg_control'),
      ('Seam.lean', 101, 'SIDEExplicitFormula.B321.h2_sign_iff_rh'),
      ('Schema/Wide/PositiveControl.lean', 124, 'SIDEExplicitFormula.Schema.Wide.pc_online'),
      ('Schema/ZetaBox/Box.lean', 21, 'SIDEExplicitFormula.Schema.ZetaBox.zeta_box'))
OTHER_LEAN = {'none_produce': ('data/b752_attribution_plan.txt', 79, 'v1.5')}   # ### W14's one name outside SIDE-explicit-formula: SIDE-kernel v1.5, cited through the plan

# ### the relay cites of BLOCK W, BLOCK V and BLOCK F, each read at relay HEAD at its line for the words it is cited for
RELAY_READS = (('data/b726_mechanisms.txt', 9, 'dropped: the Euler product'), ('data/b726_mechanisms.txt', 16, 'dropped: Ramanujan size'),
               ('data/b726_mechanisms.txt', 23, 'NO INSTANCE FOUND'), ('data/b726_mechanisms.txt', 38, 'THE BEURLING READ'),
               ('data/b726_mechanisms.txt', 39, 'NO INSTANCE FOUND'), ('data/b726_mechanisms.txt', 42, 'WHAT ROW 3 NOW STANDS ON'),
               ('data/b725_dial.txt', 4, 'zeta(s + c/2) zeta(s - c/2)'), ('data/b751_literature.txt', 37, 'S1.c  VORONIN'),
               ('data/b751_literature.txt', 42, 'S1.d  DAVENPORT AND HEILBRONN'),
               ('data/b752_attribution_plan.txt', 14, 'MechanismClass is an inductive of seven constructors'),
               ('data/b752_attribution_plan.txt', 17, 'NO CLASS OF THE SEVEN IS GIVEN A PREDICATE ON FUNCTIONS'),
               ('data/b752_attribution_plan.txt', 78, "No class of SIDE-kernel v1.5's MechanismClass"),
               ('data/b752_attribution_plan.txt', 79, 'none_produce'), ('data/b752_attribution_plan.txt', 80, 'do not meet'))

# ### I-22: the ':N' of a STATUS or of BLOCK V that names this edition's own line, by (where, the words carrying it, the keys whose lines replace it)
REPIN = (('W15', 'as :11', ('W2',)), ('W21', 're-cut at :198', ('W16',)), ('V', 'the rows at :202 to :204', ('W17', 'W19')))

# ### I-29: (id, v2.4.0's line, the words, the substitution, the keys whose claim it restates, the key whose words it takes, those words). Each
# ### a sentence of :131 left unmarked by BLOCK W that restates the sufficiency claim W7 corrects at :83 and W2 at :11 (an Euler product with
# ### the functional equation suffices), which the edition's own W12 contradicts (the shifted product keeps both, its zeros off its line);
# ### read by hand over the 23 sentences of v2.4.0's body naming the product, the bound or a correlation (scratch euler760.py, 10:1xZ).
RESTATE = (('I29-1', 131, 'every function with both a functional equation and an Euler product has all computed zeros on the critical line',
            'every function with a functional equation, an Euler product and the Ramanujan size bound has all computed zeros on the critical line',
            ('W7', 'W2'), 'W2', 'a functional equation, an Euler product and the Ramanujan size bound'),
           ('I29-2', 131, 'the Euler product is the only structural component whose presence correlates with zero confinement',
            'the Euler product with the size bound is the only structural component whose presence correlates with zero confinement',
            ('W7', 'W12'), 'W7', 'the size bound'))

# ### the restatement read's phrases (each a claim a key corrects) and the dispositions of the hits the hand read placed (v2.4.0's line, phrase)
PHRASES = (('the record', r'record is perfect'), ('both', r'both a functional equation and an euler product|both properties|both together'),
           ('confirm', r'\bconfirm\w*'), ('confining', r'does the confining|confining ingredient'), ('axiomatization', r'by axiomatization'),
           ('generic', r'\bgenerically\b'), ('violate', r'\bviolat\w*'), ('co-occur', r'co-occur'),
           ('no kernel', r'cites no kernel|not a computation this programme performed'),
           ('seven classes', r'decomposition stands|points to the same structural component'), ('n ≥ 2', r'n ≥ 2'),
           ('presence correlates', r'presence correlates with zero confinement'), ('only one present', r'only one present wherever'))
DISPO = {(28, 'both'): 'CARRIED: of ζ`s own specification, which has both; no claim about functions in general',
         (60, 'confirm'): 'CARRIED: the Davenport–Heilbronn function`s off-line zeros are a theorem (1936), the outcome it is cited as confirming',
         (131, 'the record'): 'SUBSTITUTED UNDER I-29: the predicate takes the size bound in W2`s words; with it the record holds as the sentence states',
         (131, 'confirm'): 'CARRIED: the engineered construction`s off-line zeros are a theorem',
         (131, 'presence correlates'): 'SUBSTITUTED UNDER I-29: the component takes the size bound in W7`s words; the product with the bound is present in each confined function and absent, in one part or the other, in each escaping one',
         (131, 'only one present'): 'CARRIED, ENTERED IN THE MISSES READ: necessity, which W2 keeps in the Euler product`s own terms; its "only" rested on v2.4.0`s joint treatment of the product and the bound, which W12 removes, and it restates no marked row`s claim',
         (139, 'confirm'): 'CARRIED: the examples` off-line zeros are theorems (Davenport–Heilbronn; Voronin), so of those functions the sentence holds',
         (143, 'confirm'): 'CARRIED: W14 left where the author strikes (6) -- read only when (6) is struck',
         (143, 'seven classes'): 'CARRIED: W14 left where the author strikes (6) -- read only when (6) is struck'}

CEILING = ('proof of Theorem', 'RH proved', 'certified premise', 'decomposition is correct', '*prevents*', 'confines the actors', 'correctly identifies',
           'only mechanism for zero confinement', 'doing the work', 'responsible for confining', 'confines its zeros', 'reduction machine-verified',
           'experiment confirms this', 'does the confining', 'by axiomatization')
# ### I-28: the two pages tools/chain_page.py writes and their newest node lists; a page lists every keystone naming one of its nodes
PAGES = (('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'data/b704_nodes_zeta.txt'), ('THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'data/b651_nodes_chi.txt'))
EPSTEIN_DOC = 'phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_2.md'
QUESTION = 'Which structural feature is responsible for confining zeros to the critical line?'


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def git(repo, *a, raw=False):
    r = subprocess.run(['git', '-C', repo, *a], capture_output=True)
    return r.stdout if raw else r.stdout.decode('utf-8', 'replace')


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def fsha(p):
    try:
        with open(p, 'rb') as f:
            return sha(f.read())[:16]
    except OSError:
        return 'ABSENT'


def rdrelay(path):
    return git(RELAY, 'show', 'HEAD:' + path).replace('\r', '').split(NL)


def put(path, text):
    with open(path + '.tmp', 'wb') as f:
        f.write(text.encode('utf-8'))
    os.replace(path + '.tmp', path)


def units(lines, whole=False):
    """the diff bank's units: a heading, rule, comment or table row whole, a reference line whole where asked, else b726's sentences."""
    out = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        if whole or s.startswith(('#', '|', '---', '<!--')):
            out.append(s)
        else:
            out += sents([s])
    return out


def sents(lines):
    """b726's reader: the prose sentences of lines (no table, rule, heading or comment), split at a stop before a space and a capital."""
    out = []
    for l in lines:
        s = l.strip()
        if not s or s.startswith(('|', '#', '---', '<!--')):
            continue
        out += [x.strip() for x in re.split(r'(?<=[.!?:;*)])\s+(?=[A-Z*(“])', s) if x.strip()]
    return out


# ================================================================================ THE SOURCES
def text_bank():
    with open(os.path.join(D, TEXT), 'rb') as f:
        b = f.read()
    if sha(b) != TEXT_SHA:
        die('data/%s IS NOT THE TEXT BLOCK OF (R370) PATHS (sha256 %s)' % (TEXT, sha(b)[:16]))
    return b.decode('utf-8').split(NL)


HDR = re.compile(r'^@@ (W\d+) \| :(\d+) \| ([A-Z-]+)(?: \| sha256 ([0-9a-f]{16}))?$')


def block_w(t):
    keys, i = [], 0
    while i < len(t) and not t[i].startswith('@@ BLOCK V'):
        m = HDR.match(t[i])
        if not m:
            i += 1
            continue
        k = dict(key=m.group(1), n=int(m.group(2)), kind=m.group(3), sha=m.group(4), status=None, old=None, new=None, at=i + 1)
        j = i + 1
        while j < len(t) and not t[j].startswith('@@'):
            if t[j].startswith('STATUS: ') and k['status'] is None:
                k['status'] = t[j][8:]
            elif t[j].startswith('OLD: ') and k['old'] is None:
                k['old'] = t[j][5:]
            elif t[j] == 'NEW>>':
                e = t.index('<<NEW', j)
                k['new'] = NL.join(t[j + 1:e])
                j = e
            j += 1
        keys.append(k)
        i = j
    return keys


def block_v(t):
    i = next(k for k, l in enumerate(t) if l.startswith('@@ BLOCK V'))
    if t[i + 1] != 'NEW>>':
        die('BLOCK V`S NEW>> NOT AT ITS HEAD')
    e = t.index('<<NEW', i + 1)
    return NL.join(t[i + 2:e]), i + 1


def v24():
    b = git(PP, 'show', 'HEAD:' + V24, raw=True)
    if not sha(b).startswith(V24_SHA):
        die('v2.4.0 AT PLACE-papers HEAD IS NOT (R370)(7)`S BYTES (sha256 %s)' % sha(b)[:16])
    t = b.decode('utf-8')
    if '\r' in t:
        die('v2.4.0`S BLOB CARRIES A CARRIAGE RETURN')
    L = t.split(NL)
    if L[-1] != '' or len(L) - 1 != V24_LINES:
        die('v2.4.0 IS NOT %d LINES ENDING IN A LINE END' % V24_LINES)
    return t, L[:-1]


def discharge():
    j = json.load(open(os.path.join(D, DISCHARGE), encoding='utf-8'))
    return j


def axioms():
    """run 44162171267's axioms file: continuation lines joined (a space opening each), both forms read (b760 defect (b))."""
    try:
        t = open(AXFILE, encoding='utf-8', errors='replace').read().replace('\r', '')
    except OSError:
        die('THE RUN`S AXIOMS FILE NOT READ AT ITS PLACE')
    t = re.sub(r'\n (?=\S)', ' ', t)
    return dict((m.group(1), [a.strip() for a in (m.group(2) or '').split(',') if a.strip()])
                for m in re.finditer(r"(?m)^'(.+?)' (?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)$", t))


def ids():
    import b760_address_scan as SC
    return dict(name=SC.author_name(), orcid=SC.author_orcid(), address=SC.previous_address()), SC


def idcount(text, I):
    low = text.lower()
    return dict(name=low.count(I['name'].lower()), orcid=low.count(I['orcid'].lower()), address=low.count(I['address'].lower()),
                github=low.count('github.com/'))


# ================================================================================ THE COMPOSITION
def assert_keys(keys, L, full):
    bad = []
    for k in keys:
        n = k['n']
        if n < 1 or n > len(L):
            bad.append((k['key'], 'line out of the file'))
            continue
        if k['sha']:
            ok = sha(L[n - 1]).startswith(k['sha']) and sum(1 for x in L if sha(x).startswith(k['sha'])) == 1
        elif k['old']:
            ok = k['old'] in L[n - 1] and full.count(k['old']) == 1
        else:
            ok = False
        if not ok:
            bad.append((k['key'], 'by digest' if k['sha'] else 'by OLD'))
    return bad


def compose(fill=True):
    t = text_bank()
    keys = block_w(t)
    if [k['key'] for k in keys] != KEYS:
        die('BLOCK W`S KEYS ARE NOT W0 TO W23 LESS W10: %s' % [k['key'] for k in keys])
    for k in keys:
        if not k['status']:
            die('%s CARRIES NO STATUS' % k['key'])
        if k['kind'] != 'REMOVE' and k['new'] is None:
            die('%s CARRIES NO NEW' % k['key'])
    full, L = v24()
    bad = assert_keys(keys, L, full)
    if bad:
        die('HELD AT %s: THE KEY DOES NOT HOLD AT ITS LINE OF v2.4.0 (%s)' % (bad[0][0], bad))
    dj = discharge()
    stands = dj.get('standing') == 'STANDS' and dj.get('w14') == 'APPLY'
    # ### the discharge bank's fields are {path, line, words, sha256} (tools/b760_discharge.py): each read at its place in the text block
    fol, fcr = dj.get('orderline') or {}, dj.get('classrow') or {}
    if stands and not all(f.get('path') == 'data/' + TEXT and f.get('line') == n and f.get('words') == t[n - 1] and sha(t[n - 1]).startswith(f.get('sha256') or '-')
                          for f, n in ((fol, 294), (fcr, 298))):
        die('ORDERLINE OR CLASSROW IS NOT BLOCK F`S TEXT AT data/%s :294 AND :298' % TEXT)
    for rid, n, old, new, _by, wk, words in RESTATE:
        if not (old in L[n - 1] and full.count(old) == 1):
            die('THE RESTATEMENT %s AT v2.4.0 :%d DOES NOT STAND ONCE AT ITS LINE' % (rid, n))
        if words not in next(k['new'] for k in keys if k['key'] == wk) or words not in new:
            die('THE RESTATEMENT`S WORDS ARE NOT %s`S' % wk)
    slots = [[l] for l in L]
    applied = []
    for k in keys:
        if k['key'] == 'W14' and not stands:
            continue
        i, kd, new = k['n'] - 1, k['kind'], (k['new'] or '').split(NL)
        if kd == 'WHOLE':
            slots[i] = new
        elif kd == 'REMOVE':
            slots[i] = []
        elif kd == 'PART':
            if len(slots[i]) != 1 or slots[i][0].count(k['old']) != 1:
                die('HELD AT %s: ITS OLD NOT ONCE IN ITS LINE AT APPLICATION' % k['key'])
            slots[i] = [slots[i][0].replace(k['old'], k['new'], 1)]
        elif kd == 'INLINE-AFTER':
            if len(slots[i]) != 1 or slots[i][0].count(k['old']) != 1:
                die('HELD AT %s: ITS OLD NOT ONCE IN ITS LINE AT APPLICATION' % k['key'])
            slots[i] = [slots[i][0].replace(k['old'], k['old'] + k['new'], 1)]
        elif kd == 'PARA-BEFORE':
            slots[i] = new + [''] + slots[i]
        elif kd == 'PARA-AFTER':
            slots[i] = slots[i] + [''] + new
        elif kd == 'ROW-AFTER':
            slots[i] = slots[i] + new
        else:
            die('%s: KIND %s NOT READ BY THIS TOOL' % (k['key'], kd))
        applied.append(k['key'])
    for rid, n, old, new, _by, _wk, _w in RESTATE:
        if len(slots[n - 1]) != 1 or slots[n - 1][0].count(old) != 1:
            die('THE RESTATEMENT %s AT v2.4.0 :%d NOT ONCE IN ITS LINE AFTER THE KEYS' % (rid, n))
        slots[n - 1] = [slots[n - 1][0].replace(old, new, 1)]
    start, pos = [], 1
    for s in slots:
        start.append(pos)
        pos += len(s)
    flat = [l for s in slots for l in s]
    # ### the edition's lines a key wrote whole (owned) and the lines a key changed in part (mixed, with the key's NEW): I-29's read skips the first
    owned, mixed = set(), {}
    for k in keys:
        if k['key'] not in applied:
            continue
        s0, kd, nl = start[k['n'] - 1], k['kind'], len((k['new'] or '').split(NL))
        if kd in ('WHOLE', 'PARA-BEFORE'):
            owned.update(range(s0, s0 + nl))
        elif kd == 'PARA-AFTER':
            owned.update(range(s0 + 2, s0 + 2 + nl))
        elif kd == 'ROW-AFTER':
            owned.update(range(s0 + 1, s0 + 1 + nl))
        elif kd in ('PART', 'INLINE-AFTER'):
            mixed.setdefault(s0, []).append(k['new'])

    def eline(k):
        i, kd = k['n'] - 1, k['kind']
        if kd == 'PARA-AFTER':
            return start[i] + 2
        if kd == 'ROW-AFTER':
            return start[i] + 1
        return start[i]
    where = dict((k['key'], eline(k)) for k in keys if k['key'] in applied)
    for rid, n, *_r in RESTATE:
        where[rid] = start[n - 1]
    # ### the edition's line of each line of v2.4.0 (None where removed)
    emap = dict((n, start[n - 1]) for n in range(1, len(L) + 1) if slots[n - 1])
    vtext, vat = block_v(t)
    vraw = vtext
    date = time.strftime('%Y-%m-%d', time.gmtime())
    axl = axioms()
    st = dict((k['key'], k['status']) for k in keys)
    # ### I-22: the re-pins, each words-site asserted once
    repins = []
    for w, words, ks in REPIN:
        src = vtext if w == 'V' else st[w]
        if src.count(words) != 1:
            die('THE RE-PIN SITE %r NOT ONCE IN %s' % (words, w))
        nums = re.findall(r':(\d+)', words)
        if len(nums) != len(ks):
            die('THE RE-PIN SITE %r: %d NUMBERS AGAINST %d KEYS' % (words, len(nums), len(ks)))
        new = words
        for num, kk in zip(nums, ks):
            if int(num) != next(k['n'] for k in keys if k['key'] == kk):
                die('THE RE-PIN SITE %r: :%s IS NOT %s`S LINE OF v2.4.0' % (words, num, kk))
            new = new.replace(':' + num, ':%d' % where[kk], 1)
        if w == 'V':
            vtext = vtext.replace(words, new)
        else:
            st[w] = st[w].replace(words, new)
        repins.append((w, words, new))
    # ### the fields
    def ax_of(line):
        names = re.findall(r'`(SIDEExplicitFormula\.[^`]+)`', line)
        if not names:
            die('AN AX FIELD IN A ROW NAMING NO TERMINAL')
        got = []
        for nm in names:
            if nm not in axl:
                die('%s ABSENT FROM THE RUN`S AXIOMS FILE' % nm.split('.')[-1])
            got.append((nm, axl[nm]))
        if all(set(a) == STANDARD and len(a) == 3 for _n, a in got):
            return ('the standard three (run %s)' if len(got) == 1 else 'the standard three, each (run %s)') % RUN, got
        return '; '.join('%s: %s' % (n.split('.')[-1], ', '.join(a) or 'none') for n, a in got) + ' (run %s)' % RUN, got
    axrows = []

    def fill_ax(text, record=True):
        out = []
        for l in text.split(NL):
            if '‹AX›' in l:
                v, got = ax_of(l)
                if record:
                    axrows.append((l.split('|')[1].strip()[:70], v, got))
                l = l.replace('‹AX›', v)
            out.append(l)
        return NL.join(out)
    flat = fill_ax(NL.join(flat)).replace('‹DATE›', date).split(NL)
    vtext = fill_ax(vtext).replace('‹DATE›', date)
    for k in keys:   # ### each key's NEW as the edition prints it, for the tables and the diff bank
        k['new_f'] = fill_ax(k['new'], record=False).replace('‹DATE›', date) if k['new'] is not None else None
    if stands:
        vtext = vtext.replace('‹ORDERLINE›', fol['words']).replace('‹CLASSROW›', fcr['words'])
    else:
        vtext = NL.join(l for l in vtext.split(NL) if l.strip() not in ('‹ORDERLINE›', '‹CLASSROW›'))
    # ### the tables
    q = lambda s: ' <br> '.join(x.strip() for x in (s or '').replace('|', '¦').split(NL) if x.strip())   # noqa: E731
    rew, add = [], []
    for k in keys:
        if k['key'] not in applied:
            continue
        kd, n = k['kind'], k['n']
        if k['key'] == 'W0':
            old, new = k['old'], k['new']
        elif kd == 'PART':
            old, new = k['old'], k['new']
        elif kd in ('WHOLE', 'REMOVE'):
            old, new = L[n - 1], (k['new'] if kd == 'WHOLE' else '— (removed)')
        else:
            old, new = '—', k['new']
        new = fill_ax(new, record=False).replace('‹DATE›', date)   # ### the table carries v2.5.0's wording as the edition prints it, its fields filled
        line = (':%d' % where[k['key']]) if kd != 'REMOVE' else '— (before :%d)' % where[k['key']]
        row = (where[k['key']], '| %s | %s | %s | %s |' % (line, q(old), q(new), q(st[k['key']])))
        (add if st[k['key']].startswith('an addition') else rew).append(row)
    for rid, n, old, new, by, wk, _w in RESTATE:
        s29 = 'a restatement (I-29, OPEN_TRAILS :12192): the sentence restates the claim corrected at %s; the size bound added in the words of :%d, the rest unchanged' % (
            ' and '.join(':%d' % where[b] for b in by), where[wk])
        rew.append((where[rid], '| :%d | %s | %s | %s |' % (where[rid], q(old), q(new), q(s29))))
    head = ['| this edition\'s line | v2.4.0\'s wording | v2.5.0\'s wording | Status |', '|:--|:--|:--|:--|']
    vtext = vtext.replace('‹REWRITES›', NL.join(head + [r for _w, r in sorted(rew)])).replace('‹ADDITIONS›', NL.join(head + [r for _w, r in sorted(add)]))
    if any(c in NL.join(flat) + vtext for c in '‹›'):
        die('A FIELD LEFT UNFILLED: %s' % sorted(set(re.findall(r'‹[^›]*›', NL.join(flat) + vtext))))
    text = NL.join(flat) + NL + NL + vtext + NL
    return dict(text=text, full=full, L=L, keys=keys, applied=applied, where=where, emap=emap, repins=repins, axrows=axrows, date=date, owned=owned, mixed=mixed,
                stands=stands, dj=dj, vtext=vtext, vraw=vraw, vat=vat, rew=rew, add=add, st=st, t=t, nbody=len(flat))


# ================================================================================ THE READS AND THE SCORES
def kernel_reads(C):
    L_ = []
    peel = git(KERNEL, 'rev-parse', TAG + '^{commit}').strip()[:8]
    pt = [l.strip() for l in git(KERNEL, 'show', MAIN + ':print_targets.txt').replace('\r', '').split(NL) if l.strip()]
    misses = []
    for path, line, fq in LN:
        src = git(KERNEL, 'show', '%s:SIDEExplicitFormula/%s' % (MAIN, path)).replace('\r', '').split(NL)
        short = fq.split('.')[-1]
        pat = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(?:theorem|lemma|def|abbrev|instance)\s+' + re.escape(short) + r"(?![\w'.])")
        dl = next((i for i, l in enumerate(src, 1) if pat.match(l)), None)
        ok = dl == line and fq in pt
        L_.append('  %-44s %s :%d -- declared at :%s ; among print_targets.txt %s -> %s' % (short, path, line, dl, fq in pt, 'AS WANTED' if ok else 'MISS'))
        if not ok:
            misses.append(short)
    # ### every Lean name the edition's added texts carry, and every kernel path and line they print: the keys' NEW and BLOCK V as the block
    # ### gives it, not the filled tables, whose v2.4.0 column carries v2.4.0's own cites
    added = NL.join((k['new'] or '') for k in C['keys']) + NL + C['vraw']
    shorts = set(fq.split('.')[-1] for _p, _l, fq in LN)
    fqs = set(fq for _p, _l, fq in LN)
    # ### a Lean name: a backticked word in snake case (a lower-case letter or digit, an underscore, a lower-case letter), no file's name;
    # ### placed where it is one of the twelve by its full name or by a dotted tail of it, or the plan's one
    named = sorted(n for n in set(re.findall(r'`([A-Za-z][A-Za-z0-9_.\']*)`', added))
                   if re.search(r'[a-z0-9]_[a-z]', n) and not re.search(r'\.(md|txt|lean|py|json)$', n))
    unplaced = [n for n in named if n not in OTHER_LEAN and not any(fq == n or fq.endswith('.' + n) for fq in fqs)]
    cites = set()
    for m in re.finditer(r'([A-Za-z0-9_/]+\.lean) :(\d+)((?:, :\d+)*)', added):
        for x in [m.group(2)] + re.findall(r':(\d+)', m.group(3)):
            cites.add((m.group(1), int(x)))
    have = set((p, l) for p, l, _f in LN)
    cmiss = [c for c in sorted(cites) if not any(p == c[0] or p.endswith('/' + c[0]) for p, l in have if l == c[1])]
    L_ += ['  v0.41 peels to %s, main of the block %s: %s' % (peel, MAIN, 'AS WANTED' if peel == MAIN else 'MISS'),
           '  print_targets.txt at %s: %d lines, %d distinct' % (MAIN, len(pt), len(set(pt))),
           '  the Lean names the added texts carry in backticks: %d (%s) ; outside the twelve and the plan`s one: %s' % (len(named), ', '.join(n.split('.')[-1] for n in named), unplaced or 'none'),
           '  the kernel paths and lines the added texts print: %d ; not among the twelve`s: %s' % (len(cites), cmiss or 'none')]
    # ### none_produce: through the plan; read at SIDE-kernel v1.5 where its clone stands (path and line alone)
    for nm, (bank, ln, tag) in OTHER_LEAN.items():
        pl = rdrelay(bank)
        okp = len(pl) >= ln and nm in pl[ln - 1]
        at = ''
        if os.path.isdir(SIDE_KERNEL):
            g = git(SIDE_KERNEL, 'grep', '-n', '-E', r'^\s*theorem\s+%s\b' % nm, tag, '--', '*.lean').strip().split(NL)
            at = '; at SIDE-kernel %s: %s' % (tag, ', '.join(':'.join(x.split(':')[1:3]) for x in g if x) or 'NOT FOUND')
        L_.append('  %s (SIDE-kernel %s): named at relay %s :%d %s%s' % (nm, tag, bank, ln, 'AS WANTED' if okp else 'MISS', at))
        if not okp:
            misses.append(nm)
    return L_, misses + (['v0.41 peel'] if peel != MAIN else []) + unplaced + ['%s :%d' % c for c in cmiss]


RELAY_CITE = re.compile(r'(?<![A-Za-z0-9_./-])((?:data|tools)/[A-Za-z0-9_./-]*[A-Za-z0-9_-]\.(?:txt|py|json|md))`?((?:,? ?(?:and )?;? ?`?:\d+(?:[–-]:\d+)?)*)')


def relay_reads(C):
    L_, miss = [], []
    for p, n, nd in RELAY_READS:
        l = rdrelay(p)
        ok = len(l) >= n and nd in l[n - 1]
        L_.append('  relay %s :%d carries %r -> %s' % (p, n, nd, 'AS WANTED' if ok else 'MISS'))
        if not ok:
            miss.append('%s :%d' % (p, n))
    added = NL.join((k['new'] or '') for k in C['keys']) + NL + C['vraw']
    seen = 0
    for m in RELAY_CITE.finditer(added):
        l = rdrelay(m.group(1))
        nums = [int(x) for x in re.findall(r':(\d+)', m.group(2))]
        seen += 1
        if not l or len(l) < 2:
            miss.append(m.group(1))
        for x in nums:
            if x > len(l) or not l[x - 1].strip():
                miss.append('%s :%d' % (m.group(1), x))
    L_.append('  every relay cite of the added texts read at HEAD: %d cites, each line present and not blank: %s' % (seen, 'AS WANTED' if not miss else miss))
    return L_, miss


def restatement_read(C):
    """I-29's read: each phrase over the unmarked sentences of the edition up to its first ERA annotation; each hit with its disposition."""
    tl = C['text'].split(NL)
    era = next(i for i, l in enumerate(tl, 1) if l.startswith('### ERA ANNOTATION'))
    inv = dict((e, n) for n, e in C['emap'].items())
    hits, unknown, beside = [], [], {}
    for i, l in enumerate(tl[:era - 1], 1):
        if i in C['owned']:
            continue
        n24 = inv.get(i)
        for s in sents([l]) if not l.lstrip().startswith('|') else [l]:
            if any(s in m for m in C['mixed'].get(i, [])):
                continue
            for key, pat in PHRASES:
                if re.search(pat, s, re.I):
                    d = DISPO.get((n24, key))
                    if d and 'struck' in d and C['stands']:
                        d = None
                    hits.append((i, n24, key, d))
                    if not d:
                        unknown.append((i, n24, key))
    for l in tl[era - 1:]:
        for key, pat in PHRASES:
            if re.search(pat, l, re.I):
                beside[key] = beside.get(key, 0) + 1
    return hits, unknown, beside


def score(C):
    cl, tl = C['L'], C['text'].split(NL)
    cut_a, cut_b = cl.index('## Symbols'), tl.index('## Symbols')
    a, b = sents(cl[:cut_a]), sents(tl[:cut_b])
    bset = set(b)
    stands = sum(1 for s in a if s in bset)
    rows = []
    ruled = removed_s = 0
    for k in C['keys']:
        if k['key'] not in C['applied'] or k['n'] > cut_a:
            continue
        kd = k['kind']
        o = sents([k['old']]) if kd in ('PART',) else sents([cl[k['n'] - 1]]) if kd in ('WHOLE', 'REMOVE') else []
        nw = sents((k['new'] or '').split(NL)) if kd != 'REMOVE' else []
        if kd == 'INLINE-AFTER':
            o = []
        rows.append((k['key'], kd, len(o), len(nw)))
        if C['st'][k['key']].startswith('an addition') and k['key'] != 'W1':
            ruled += len(nw)
        if 'ruled addition' in C['st'][k['key']]:
            ruled += len(nw)
            removed_s += len(o)
        if kd == 'REMOVE':
            removed_s += len(o)
    removals = sum(1 for k in C['keys'] if k['key'] in C['applied'] and k['n'] <= cut_a and (k['kind'] == 'REMOVE' or 'removal' in C['st'][k['key']].split(':')[0]))
    d = len(b) - len(a)
    bound = 0 + removals + ruled + 1
    body = tl[:cut_b]
    ceil = [(w, sum(l.replace(QUESTION, '').count(w) for l in body)) for w in CEILING]
    stems = [(i, m.group(0)) for i, l in enumerate(tl, 1) for m in re.finditer(r'\b(gap|blind)\w*', l, re.I)]
    return dict(body_cur=len(a), body_new=len(b), stands=stands, rows=rows, ruled=ruled, removals=removals, removed_s=removed_s, d=d, bound=bound,
                ceil_hits=[(w, n) for w, n in ceil if n], stems=stems, back_cur=len(sents(cl[cut_a:])), back_new=len(sents(tl[cut_b:])),
                q_in=sum(1 for l in body if QUESTION in l))


def h28a():
    out = []
    for f in ('b558_cp1b.json', 'b558_editions.json'):
        t = open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
        out.append((f, t.count('Which_Structure_Confines')))
    return out


def node_pattern(listpath):
    """tools/chain_page.py keystones()'s pattern over a node list's short names, read at relay HEAD (b592's and b629's guards kept)."""
    sn = set()
    for l in rdrelay(listpath):
        if l.strip() and not l.startswith(('#', '@')):
            sn.add(l.split(' | ')[0].strip().split('.')[-1])
    plain = sorted(s for s in sn if re.fullmatch(r'[a-z]+|[A-Z]+', s))
    rest = sorted(s for s in sn if s not in plain)
    alts = [r'\b(' + '|'.join(re.escape(s) for s in rest) + r')\b'] if rest else []
    alts += [r'(`' + re.escape(s) + r'`|[A-Za-z0-9_]\.' + re.escape(s) + r'\b)' for s in plain]
    return re.compile('|'.join(alts)), len(sn)


def page_clause(C):
    """I-28: for each page, the nodes v2.4.0 and the edition name, whether the page lists the paper, and whether it lists the Epstein
    document v0.2 (a later keystone naming its nodes): the page's Placement read against what a regeneration would add."""
    out = []
    epi = git(PP, 'show', 'HEAD:' + EPSTEIN_DOC)
    for page, lp in PAGES:
        pat, n = node_pattern(lp)
        pg = git(PP, 'show', 'HEAD:' + page)
        out.append(dict(page=page, list=lp, nodes=n, v24=sorted(set(m.group(0) for m in pat.finditer(C['full']))),
                        v25=sorted(set(m.group(0) for m in pat.finditer(C['text']))), lists_family='Which_Structure_Confines' in pg,
                        epstein_names=bool(pat.search(epi)), lists_epstein=EPSTEIN_DOC in pg,
                        last=git(PP, 'log', '-1', '--format=%h', '--', page).strip()))
    return out


def identifiers(C, I, bank_text=''):
    a24 = idcount(C['full'], I)
    a25 = idcount(C['text'], I)
    added = NL.join((k['new'] or '') + NL + (k['old'] or '') for k in C['keys']) + NL + C['vtext'] + NL + NL.join(r[3] for r in RESTATE)
    a_add = idcount(added, I)
    a_bank = idcount(bank_text, I) if bank_text else None
    ok = a24 == a25 and not any(a_add.values()) and (a_bank is None or not any(a_bank.values()))
    return ok, a24, a25, a_add, a_bank


def controls(C, I):
    L_ = ['## THE CONTROLS ((R370)(7)), PRINTED BEFORE THE COMMIT']
    L_.append('  v2.4.0: the blob at PLACE-papers HEAD %s ; the working file %s ; v2.3.1: the blob %s ; the working file %s' % (
        sha(git(PP, 'show', 'HEAD:' + V24, raw=True))[:16], fsha(os.path.join(PP, V24)), sha(git(PP, 'show', 'HEAD:' + V231, raw=True))[:16], fsha(os.path.join(PP, V231))))
    kl, km = kernel_reads(C)
    rl, rm = relay_reads(C)
    L_ += ['  THE LEAN NAMES AT %s = %s (path and line alone; no kernel line printed):' % (TAG, MAIN)] + kl
    L_ += ['  THE RELAY CITES AT HEAD:'] + rl
    ok, a24, a25, a_add, _b = identifiers(C, I)
    L_.append('  THE IDENTIFIERS, counted (never printed): v2.4.0 %s ; the edition %s ; the added texts %s -> %s' % (a24, a25, a_add, 'AS WANTED' if ok else 'REFUSED'))
    tl = C['text'].split(NL)
    by = [3, C['emap'][164], C['emap'][166]]
    eq = [sha(tl[by[0] - 1]) == sha(C['L'][2].replace('v2.4.0, October 2026', 'v2.5.0, November 2026', 1)),
          sha(tl[by[1] - 1]) == sha(C['L'][163]), sha(tl[by[2] - 1]) == sha(C['L'][165])]
    L_.append('  THE BYLINE AND THE TWO SELF-CITATIONS, by digest alone: the edition`s :%d, :%d, :%d against v2.4.0`s :3 (W0 applied), :164, :166 -> %s' % (
        by[0], by[1], by[2], 'EQUAL' if all(eq) else 'NOT EQUAL %s' % eq))
    return L_, km + rm + ([] if ok else ['identifiers']) + ([] if all(eq) else ['byline'])


# ================================================================================ THE PRINT AND THE BANK
def report(C, I, s, ctl_lines, ctl_miss, rr):
    hits, unknown, beside = rr
    L_ = ['%s -- (R370)(7): WHICH STRUCTURE CONFINES v2.5.0 AGAINST v2.4.0, SENTENCE BY SENTENCE, ITS FIELDS, ITS READS AND ITS SCORES (%s)' % (ACT, utc()), '',
          '### by tools/b760_edition.py from v2.4.0`s bytes (PLACE-papers HEAD, sha256 %s, %d lines) and BLOCK W and BLOCK V of data/%s (sha256 %s); the edition sha256 %s, %d lines.' % (
              sha(C['full'])[:16], len(C['L']), TEXT, TEXT_SHA[:16], sha(C['text'])[:16], len(C['text'].split(NL)) - 1),
          '### v2.4.0 and v2.3.1 unedited. The byline (:3) and the two self-citations (:164, :166) are carried and not printed here: W0`s words alone.',
          '### (6) %s: W14 %s ; ORDERLINE and CLASSROW %s.' % ('STANDS' if C['stands'] else 'STRUCK', 'APPLIED' if C['stands'] else 'NOT APPLIED',
                                                             'filled from data/b760_discharge.json' if C['stands'] else 'empty')]
    # ### the offset, I-22
    off, prev = [], None
    for n in range(1, len(C['L']) + 1):
        e = C['emap'].get(n)
        o = None if e is None else e - n
        if o != prev:
            off.append('from v2.4.0 :%d %s' % (n, 'removed' if o is None else ('%+d' % o)))
            prev = o
    r0 = next((i for i, l in enumerate(C['L'], 1) if l.startswith('## References')), 0)
    refs = (r0, next((i for i, l in enumerate(C['L'], 1) if i > r0 and l.startswith('## ')), 0) if r0 else 0)
    L_ += ['### THE OFFSET (I-22): ' + ' ; '.join(off) + '. Every line the back matter`s rows name is the edition`s own.', '',
           '## THE KEYS, EACH ASSERTED AT ITS LINE OF v2.4.0 BEFORE COMPOSITION, THEN APPLIED (key | v2.4.0 line | kind | how asserted | the edition`s line | Status)']
    for k in C['keys']:
        how = 'by digest %s' % k['sha'] if k['sha'] else 'by OLD, once in the file'
        L_.append('  %s | :%d | %s | %s | %s | %s' % (k['key'], k['n'], k['kind'], how, (':%d' % C['where'][k['key']]) if k['key'] in C['where'] else 'NOT APPLIED', C['st'][k['key']]))
    L_ += ['', '## THE CHANGES, SENTENCE BY SENTENCE (- v2.4.0 ; + v2.5.0; a table row whole)']
    for k in C['keys']:
        if k['key'] not in C['applied']:
            continue
        kd, n = k['kind'], k['n']
        L_.append('  %s (v2.4.0 :%d, %s, the edition`s :%d):' % (k['key'], n, kd, C['where'][k['key']]))
        if n in ID_LINES:
            L_ += ['    - %s' % k['old'], '    + %s' % k['new'], '    (the line`s other words not printed: the byline, carried)']
            continue
        old = k['old'] if kd in ('PART', 'INLINE-AFTER') else C['L'][n - 1] if kd in ('WHOLE', 'REMOVE') else ''
        if kd in ('INLINE-AFTER', 'PARA-BEFORE', 'PARA-AFTER', 'ROW-AFTER'):
            L_.append('    (added %s v2.4.0 :%d%s)' % ('before' if kd == 'PARA-BEFORE' else 'after', n, (', after the words "%s"' % k['old']) if kd == 'INLINE-AFTER' else ''))
            old = ''
        whole = refs[0] < n < refs[1]   # ### a reference is printed by its line, not split at its initials
        for x in units([old], whole):
            L_.append('    - ' + x)
        for x in units((k['new_f'] or '').split(NL), whole):
            L_.append('    + ' + x)
        if kd == 'REMOVE':
            L_.append('    + (removed)')
    for rid, n, old, new, by, wk, _w in RESTATE:
        L_ += ['  %s (v2.4.0 :%d, the restatement clause, the edition`s :%d): the claim %s correct, restated; minimal substitution in %s`s words' % (
            rid, n, C['where'][rid], ' and '.join(by), wk), '    - ' + old, '    + ' + new]
    L_ += ['', '## THE FIELDS',
           '  DATE: %s (UTC, at the run)' % C['date'],
           '  AX (run %s`s axioms file, %s; data/%s :16 reads it: %s):' % (RUN, 'its lines read', OUTCOMES, rdrelay('data/' + OUTCOMES)[15].strip()[:140])]
    for row, v, got in C['axrows']:
        L_.append('    %s -> %s %s' % (row, v, ['%s %s' % (n.split('.')[-1], a) for n, a in got]))
    L_ += ['  ORDERLINE and CLASSROW: %s' % ('data/b760_discharge.json`s orderline and classrow, BLOCK F :294 and :298' if C['stands'] else 'empty, (6) struck'),
           '  REWRITES: %d rows (%d keys and %d restatement) ; ADDITIONS: %d rows ; no Status cell blank: %s' % (
               len(C['rew']), len(C['rew']) - len(RESTATE), len(RESTATE), len(C['add']), all(r.rstrip(' |').split('|')[-1].strip() for _w, r in C['rew'] + C['add']))]
    L_ += ['  THE RE-PINS (I-22): ' + ' ; '.join('%s %r -> %r' % r for r in C['repins'])]
    others = []
    sites = [w for _k, w, _ks in REPIN]
    for src, txt in [('V', C['vraw'])] + [(k['key'], k['status']) for k in C['keys']]:
        for w in sites:
            txt = txt.replace(w, '')
        for m in re.finditer(r'(?<![A-Za-z0-9]):(\d+)', txt):
            before = txt[max(0, m.start() - 160):m.start()]
            mk = re.findall(r'(OPEN_TRAILS|[A-Za-z0-9_/.-]+\.(?:lean|txt|md|json)|v2\.4\.0|arXiv|README|this edition)', before)
            others.append('%s:%s %s' % (src, m.group(1), mk[-1] if mk else 'NONE'))
    L_.append('  EVERY OTHER `:N` OF A STATUS OR OF BLOCK V, WITH THE FILE IT NAMES (the last named before it): %d -- %s' % (len(others), ' ; '.join(others)))
    L_ += ['', '## THE READS'] + ctl_lines
    L_ += ['', '## THE RESTATEMENT CLAUSE (I-29, OPEN_TRAILS :12192): EACH CORRECTED CLAIM`S PHRASES OVER THE UNMARKED SENTENCES UP TO THE FIRST ERA ANNOTATION']
    for i, n24, key, d in hits:
        L_.append('  the edition`s :%d (v2.4.0 :%s) | %s | %s' % (i, n24, key, d or '### NOT PLACED'))
    L_.append('  beyond, in the dated entries (the history clause, I-20 and I-30: carried): %s' % (beside or 'none'))
    L_.append('  HITS %d ; PLACED %d ; NOT PLACED %d%s' % (len(hits), len(hits) - len(unknown), len(unknown), (' -- HELD AT THE EDITION`S :%d' % unknown[0][0]) if unknown else ''))
    a28 = h28a()
    pg = page_clause(C)
    ok_b = s['d'] <= s['bound']
    ok_c = not s['stems'] and not s['ceil_hits']
    L_ += ['', '## THE SCORES',
           '  H28a: MOVED-IN-MEANING rows 0 (no CP-1b work-list carries this document: %s) ; each addition cites its source by bank and line or by terminal (the reads above) -- %s' % (
               ', '.join('data/%s %d mentions' % x for x in a28), 'HELD, VACUOUS on the work-list`s rows and carried on the ruled additions' if not any(n for _f, n in a28) else 'READ BY HAND'),
           '  H28b (I-21): body sentences %d against %d (the back matter %d against %d, counted beside); difference %+d against the bound %d (CREDIT 0, removals %d, ruled citations %d, one version line) -- %s' % (
               s['body_new'], s['body_cur'], s['back_new'], s['back_cur'], s['d'], s['bound'], s['removals'], s['ruled'], 'HELD' if ok_b else 'REFUTED'),
           '    per key in the body (key, kind, v2.4.0`s sentences, v2.5.0`s): %s ; the restatement 0 sentences moved' % ', '.join('%s %s %d->%d' % r for r in s['rows']),
           '  H28c: live banned stems in the whole file %d ; sentences beyond the ceiling %d by the list %s (the question at :22 struck from the count and carried, %d line) -- %s' % (
               len(s['stems']), len(s['ceil_hits']), list(CEILING), s['q_in'], 'HELD' if ok_c else 'REFUTED %s %s' % (s['stems'], s['ceil_hits'])),
           '  STANDS: %d of %d sentences of v2.4.0`s body carried unchanged; the keys and the %d restatements changed the rest as listed' % (s['stands'], s['body_cur'], len(RESTATE)),
           '  THE PAGE CLAUSE (I-28), each page by tools/chain_page.py keystones()`s pattern over its newest node list at relay HEAD: ' + ' ; '.join(
               '%s (%s, %d nodes, last written at PLACE-papers %s): v2.4.0 names %s, the edition names %s ; the page lists the paper %s ; it lists %s %s, which names its nodes %s' % (
                   p['page'], p['list'], p['nodes'], p['last'], p['v24'] or 'none', p['v25'] or 'none', p['lists_family'], EPSTEIN_DOC, p['lists_epstein'], p['epstein_names'])
               for p in pg),
           '    %s' % ('A REGENERATION WOULD ADD THE EDITION TO A PAGE`S PLACEMENT; NEITHER PAGE IS ON (R370)(13)`S (W) LIST, AND EACH ALREADY OMITS A LATER KEYSTONE NAMING ITS NODES, SO NEITHER IS REGENERATED BY THIS ACT: ENTERED IN THE MISSES READ FOR THE AUTHOR'
                          if any(p['v25'] and not p['lists_family'] for p in pg) else 'the edition names no node of either page, so neither page is regenerated'),
           '  N3 READ: the edition equals v2.4.0 with BLOCK W applied and BLOCK V appended, but for %d substitutions of the restatement clause, each listed in its rewrites table -- REFUTED BY THOSE ROWS, printed' % len(RESTATE),
           '  NOT DEPOSITED; committed to PLACE-papers beside v2.4.0 and v2.3.1, each unedited']
    # ### HELD at a sentence the form cannot place (I-29's read), a control's miss, or a sentence beyond the ceiling (H28c); H28a and H28b print
    # ### as scored ((R370)(7): "H28a, H28b and H28c <as scored>")
    held = unknown or ctl_miss or not ok_c
    L_ += ['', '### ### **WHICH STRUCTURE CONFINES v2.5.0: %s ; KEYS %d OF 23 HOLDING, %d APPLIED ; H28a HELD ; H28b %s (%+d AGAINST %d) ; H28c %s ; I-29 %d SUBSTITUTED, %d NOT PLACED ; CONTROLS MISSES %d ; NOT DEPOSITED.**' % (
        ('HELD AT %s' % (('the edition`s :%d' % unknown[0][0]) if unknown else ctl_miss[0] if ctl_miss else 'the scores')) if held else 'COMPOSED BESIDE v2.4.0 AND v2.3.1, EACH UNEDITED',
        len(C['keys']), len(C['applied']), 'HELD' if ok_b else 'REFUTED', s['d'], s['bound'], 'HELD' if ok_c else 'REFUTED', len(RESTATE), len(unknown), len(ctl_miss))]
    return L_, held


def edition(mode):
    I, _SC = ids()
    C = compose()
    s = score(C)
    cl, cm = controls(C, I)
    rr = restatement_read(C)
    L_, held = report(C, I, s, cl, cm, rr)
    bank_text = NL.join(L_) + NL
    ok, *_r, a_bank = identifiers(C, I, bank_text)
    if any(a_bank.values()):
        die('AN IDENTIFIER IN THE DIFF BANK %s' % a_bank)
    print(bank_text)
    if mode == 'dry':
        print('### DRY: nothing written; the edition`s lines 1-14, the byline`s :3 withheld:')
        for i, l in enumerate(C['text'].split(NL)[:14], 1):
            print('  :%d %s' % (i, '<the byline, not printed>' if i == 3 else l[:160]))
        return
    if held:
        die('HELD -- THE EDITION NOT WRITTEN; data/b760_edition_diff.txt NOT WRITTEN (the print above stands for it)')
    if os.path.exists(os.path.join(PP, V25)):
        die('%s ALREADY STANDS' % V25)
    b24, b231 = fsha(os.path.join(PP, V24)), fsha(os.path.join(PP, V231))
    put(os.path.join(PP, V25), C['text'])
    put(BANK, bank_text)
    print('written %s (%d lines, sha256 %s) and data/b760_edition_diff.txt (%d lines) ; the line ends LF ; v2.4.0`s working file %s -> %s, v2.3.1`s %s -> %s' % (
        V25, len(C['text'].split(NL)) - 1, sha(C['text'])[:16], len(L_), b24, fsha(os.path.join(PP, V24)), b231, fsha(os.path.join(PP, V231))))


def controls_again():
    I, _SC = ids()
    C = compose()
    cl, cm = controls(C, I)
    print(NL.join(cl))
    p = os.path.join(PP, V25)
    on = open(p, 'rb').read() if os.path.exists(p) else b''
    same = on.replace(b'\r\n', b'\n') == C['text'].encode('utf-8')
    print('  THE WRITTEN FILE AGAINST THE COMPOSITION AT THIS RUN (the date the same day): %s ; its sha256 %s, LF %s' % (
        'EQUAL' if same else 'DIFFERS', sha(on)[:16], b'\r\n' not in on))
    print('### ### **THE CONTROLS: MISSES %d ; THE FILE %s.**' % (len(cm), 'EQUAL' if same else 'DIFFERS'))


# ================================================================================ (8): THE QUOTATION SEARCH, b708'S PAPER FORM
def pieces(span):
    s = span.strip()
    if s.startswith('|'):
        return [c.strip() for c in s.strip('|').split('|') if len(c.strip()) >= 24]
    return [x.strip() for x in re.split(r'(?<=[.!?:;*)])\s+(?=[A-Z*(“])', s) if len(x.strip()) >= 24]


def wide(p):
    segs = [x.strip() for x in re.split(r'[,;:()\[\]“”"*`—–|#]+', p) if len(x.strip().split()) >= 4]
    return (max(segs, key=len) if segs else p).lower().strip()


def ggrep(repo, pats, icase):
    a = ['git', '-C', repo, 'grep', '-n', '-z', '-F', '-I']
    if icase:
        a.append('-i')
    for p in pats:
        a += ['-e', p]
    r = subprocess.run(a + ['HEAD', '--'], capture_output=True)
    if r.returncode not in (0, 1):
        die('git grep IN %s EXITED %d' % (repo, r.returncode))
    out = []
    for rec in r.stdout.decode('utf-8', 'replace').split(NL):
        f = rec.split('\0')
        if len(f) >= 3 and f[0].startswith('HEAD:') and f[1].isdigit():
            out.append((f[0][5:], int(f[1]), '\0'.join(f[2:])))
        elif len(f) == 2 and f[0].startswith('HEAD:') and re.match(r'^\d+:', f[1]):
            n, txt = f[1].split(':', 1)
            out.append((f[0][5:], int(n), txt))
    return out


def search(rows, own_of, live, family):
    """each row's two needles over PLACE-papers' tree and the relay's at HEAD; hits classed, words kept in memory alone."""
    t0 = time.time()
    ex = sorted(set(r['needle'] for r in rows))
    wd = sorted(set(r['wide'] for r in rows))
    H = {}
    for repo, tag in ((PP, 'pp'), (RELAY, 'relay')):
        H[tag] = (ggrep(repo, ex, False), ggrep(repo, wd, True))
    faces = set(p for p in git(RELAY, 'ls-files', '-z', '--', '*.md').split('\0') if p)
    from subject import LIVE_LEDGERS
    for r in rows:
        r['hits'], r['hits_wide'], r['own'] = [], [], []
        for tag in ('pp', 'relay'):
            for shape, hl in (('hits', H[tag][0]), ('hits_wide', H[tag][1])):
                for path, ln, text in hl:
                    if not ((r['needle'] in text) if shape == 'hits' else (r['wide'] in text.lower())):
                        continue
                    if tag == 'pp' and own_of(r, path, ln):
                        r['own'].append(dict(path=path, line=ln, sha256=sha(text)[:16]))
                        continue
                    if tag == 'pp':
                        cls = ('family' if family(r, path) else 'copy' if path.startswith(('archive/', 'outputs/')) else 'ledger' if path in LIVE_LEDGERS
                               else 'live' if path in live else 'other')
                        name = path
                    else:
                        cls = 'face' if path in faces else 'relay record'
                        name = 'relay:' + path
                    r[shape].append(dict(path=name, line=ln, sha256=sha(text)[:16], cls=cls))
    return time.time() - t0, len(faces)


# ### the seat's hand read of each live line the search found (scratch qread760.py, 10:2xZ, every line printed through mask760 and read
# ### whole): what the line carries, in the seat's words, never the line's; printed beside the order or the residue, banked in the JSON
READINGS = {
    ('day1/Spectral_Inertness.md', 97): 'v2.4.0 :43 byte for byte: the theorem with the two words W4`s STATUS names, the claim W4 corrects',
    ('day1/A_Place_to_Stand.md', 1096): 'the same theorem stated with the two words W4`s STATUS names, the claim W4 corrects; an edition of a family whose newest file in the tree is v5_17',
    ('day1/A_Place_to_Stand_v5_14.md', 1092): 'as day1/A_Place_to_Stand.md :1096, an earlier edition',
    ('day1/A_Place_to_Stand_v5_15.md', 1093): 'as day1/A_Place_to_Stand.md :1096, an earlier edition',
    ('day1/A_Place_to_Stand_v5_16.md', 1094): 'as day1/A_Place_to_Stand.md :1096, an earlier edition',
    ('day1/A_Place_to_Stand_v5_17.md', 1095): 'as day1/A_Place_to_Stand.md :1096, the family`s newest edition in the tree',
    ('SPIRAL_MAP.md', 543): 'a table row carrying W-ORD-ZQ-OFFLINE-ZERO`s discharge sentence ((R353)(2)), which v2.4.0 :95 also carried; the claim stands, W8 restating it at v0.41; the row is b759`s C9a and C9b',
    ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 626): 'its own dated note of b743 under (R353)(4)(A), parallel to v2.4.0 :95, carrying the same discharge sentence; the claim stands, W8 restating it at v0.41',
    ('README.md', 108): 'its own dated note of b750 under (R360)(2)[B2], parallel to v2.4.0 :97 and closing with the same sentence; the claim stands, W9 removing a note whose content the subsection states',
}


def stands(r, shape):
    """the matched words stand in the key's own NEW (whitespace-normalized; the wide shape case-insensitive): the hit quotes no changed sentence."""
    nw = ' '.join((r.get('new') or '').split())
    if shape == 'hits':
        return ' '.join(r['needle'].split()) in nw
    return ' '.join(r['wide'].split()) in nw.lower()


LATE_READINGS = {
    ('internal/TECHNE_ELEMENTS.md', 392): 'says of the Epstein family as a whole that its zeros wander off the critical line, the claim C4 sharpened to class number above 1 in A Place to Stand v5_17 :609',
    ('phase1.5/spectral/CONSERVATION_REFINED.md', 16): 'presents the Epstein family as a controlled experiment whose zeros wander off the critical line, of the family as a whole: the claim C4 sharpened to class number above 1',
    ('phase2/method/THE_DAY1_IMPLICATIONS.md', 40): 'a table cell quoting C4`s OLD whole within quotation marks, attributed to A_Place_to_Stand by chapter; a paper the registry does not name, so no order under (8)`s live-paper rule: entered in the misses read',
    ('day1/Which_Structure_Confines_v2_4_0.md', 95): 'v2.4.0`s dated note of b743, its discharge sentence closing with the clause C9b`s NEW keeps whole; v2.4.0 stands unedited, v2.5.0 re-cutting the note at W8',
    ('day1/Which_Structure_Confines_v2_5_0.md', 419): 'v2.5.0`s rewrites table, its row for W8 quoting v2.4.0 :95`s wording as the form of an edition lists it',
    ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_7.md', 626): 'its own dated note of b743, the discharge sentence closing with the clause C9b`s NEW keeps whole; the edition search`s W-ORD-RECUT-QUOTE-W8 already names the line',
    ('phase2/method/THE_EULER_SPECIFICATION.md', 469): 'its own dated note of b743 under (R353)(4)(A), the discharge sentence closing with the clause C9b`s NEW keeps whole; a paper the registry does not name',
}


def hit_lines(r, where=None, readings=None):
    """a row's distinct hits: a live paper's, a face's, a ledger's and an untracked-class line each by path, line and sha256 (a live or face hit
    marked as an order or as a residue whose words stand in the key's NEW -- v2.5.0's for the edition's search, b759's re-cut line for the late
    search (b760 events (66)) -- the seat's reading beside); the family's, the copies' and the relay's records counted by class (their places
    stand in the JSON bank where one is written)."""
    where = where or ('v2.5.0`s %s' % r['key'])
    readings = READINGS if readings is None else readings
    hs = {}
    for shape in ('hits', 'hits_wide'):
        for h in r[shape]:
            k = (h['path'], h['line'], h['sha256'], h['cls'])
            hs[k] = hs.get(k, True) and stands(r, shape)
    out = []
    for h, st in sorted(hs.items()):
        if h[3] not in ('live', 'face', 'ledger', 'other'):
            continue
        tag = '' if h[3] not in ('live', 'face') else (' -- residue, its words standing in %s: no order' % where if st else
                                                      ' -- residue%s' % (' and order W-ORD-RECUT-QUOTE-%s' % r['key'] if h[3] == 'live' else ''))
        out.append('      %s :%d [%s] %s%s' % (h + (tag,)))
        if (h[0], h[1]) in readings:
            out.append('        the seat`s reading: %s' % readings[(h[0], h[1])])
    hs = sorted(hs)
    cnt = {}
    for h in hs:
        if h[3] not in ('live', 'face', 'ledger', 'other'):
            cnt[h[3]] = cnt.get(h[3], 0) + 1
    if cnt:
        out.append('      counted: ' + ' ; '.join('%s %d' % x for x in sorted(cnt.items())))
    return out


def summarize(rows):
    allh = [h for r in rows for h in r['hits'] + r['hits_wide']]
    by = {}
    for h in allh:
        by.setdefault(h['cls'], set()).add((h['path'], h['line']))
    res = sorted(by.get('live', set()) | by.get('face', set()))
    orders = {}
    for r in rows:
        for shape in ('hits', 'hits_wide'):
            st = stands(r, shape)
            for h in r[shape]:
                h['stands_in_v250'] = st
                if h['cls'] == 'live' and not st:
                    orders.setdefault(r['key'], set()).add((h['path'], h['line']))
    return by, res, orders


def quote_rows():
    t = text_bank()
    keys = block_w(t)
    full, L = v24()
    rows = []
    for k in keys:
        if k['kind'] not in ('WHOLE', 'PART', 'REMOVE'):
            continue
        n = k['n']
        if n in ID_LINES:
            rows.append(dict(key=k['key'], line_no=n, line=k['old'], line_withheld=True, line_sha256=sha(L[n - 1])[:16], needle=k['old'], wide=k['old'].lower(), new=k['new']))
            continue
        span = k['old'] if k['kind'] == 'PART' else L[n - 1]
        for p in pieces(span):
            rows.append(dict(key=k['key'], line_no=n, line=L[n - 1], needle=p, wide=wide(p), new=k['new'] or ''))
    for rid, n, old, new, by, _wk, _w in RESTATE:
        rows.append(dict(key=rid, line_no=n, line=L[n - 1], needle=old, wide=wide(old), new=new))
    return rows, L


def quote(dry):
    rows, L = quote_rows()
    bad = [(r['key'], r['line_no']) for r in rows if r['needle'] not in r['line'] or r['wide'] not in r['line'].lower()]
    if bad:
        die('A NEEDLE DOES NOT STAND IN ITS OWN LINE %s' % bad)
    import subject as S
    live, fig = S.live_papers('HEAD', PP)
    live = set(live)
    lines_changed = sorted(set(r['line_no'] for r in rows))
    own_of = lambda r, path, ln: path == V24 and ln in lines_changed   # noqa: E731
    secs, nfaces = search(rows, own_of, live, lambda r, p: S.family_of(p) == FAMILY)
    by, res, orders = summarize(rows)
    at = utc()
    head = git(PP, 'rev-parse', 'HEAD').strip()
    L_ = ['%s -- (R370)(8): THE QUOTATION SEARCH OF b690 ROW (2), b708`S PAPER FORM, OVER THE LINES OF %s THAT A WHOLE, PART OR REMOVE KEY CHANGES (%s)' % (ACT, V24, at), '',
          '### PLACE-papers HEAD %s, its live papers by tools/standing/subject.py live_papers (%d, the four ledgers and the archived and deposited copies out),' % (head[:8], len(live)),
          '### the relay HEAD %s, its faces its tracked Markdown pages (%d; its banks are records, counted beside). Each changed line split into its' % (git(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), nfaces),
          '### sentences (a table row into its cells), each piece of 24 characters or more an exact needle, its longest clause of four words or more a',
          '### case-insensitive needle; v2.4.0 :3 needled by W0`s OLD alone, the line withheld. A hit is printed by path, line and sha256; its words are not.',
          '### Classes: live (a live paper: a residue and an order W-ORD-RECUT-QUOTE-<key>), face (a residue), family (the paper`s own editions, v2.3.1 and',
          '### v2.4.0`s other lines), copy, ledger, other (tracked, no live paper), relay record. Rows: key | v2.4.0 line | exact hits | wide hits | own.',
          '### Every live or face hit is a residue (data/b690_rules.txt :9-:10, "Every hit is entered as a residue with the quoting line"); a live hit is an',
          '### order where its matched words do not stand in the key`s own NEW -- (8): "a live paper that quotes a changed sentence" -- and a residue alone',
          '### where they do (the words the edition keeps). The seat`s hand read of each live line (scratch qread760.py, through mask760) printed beside it.', '']
    for r in rows:
        L_.append('  %s :%-3d | %d | %d | own %d | %r' % (r['key'], r['line_no'], len(r['hits']), len(r['hits_wide']), len(r['own']), r['needle'][:70]))
        L_ += hit_lines(r)
    L_ += ['', '### BY CLASS, DISTINCT LINES: ' + ' ; '.join('%s %d' % (c, len(v)) for c, v in sorted(by.items())) if by else '### BY CLASS: no hit outside the changed lines',
           '### THE RESIDUES (live and face), each entered in data/b760_cut.json: %s' % ('; '.join('%s :%d' % x for x in res) or 'NONE'),
           '### THE ORDERS (a live paper quoting a changed sentence, not edited): %s' % ('; '.join('W-ORD-RECUT-QUOTE-%s: %s' % (k, ', '.join('%s :%d' % x for x in sorted(v))) for k, v in sorted(orders.items())) or 'NONE'),
           '### ### **LINES CHANGED %d ; NEEDLES %d IN TWO SHAPES ; QUOTING LINES %d ; ORDERS %d ; SEARCHED IN %.1f s BEFORE THE EDITION`S COMMIT.**' % (
               len(lines_changed), len(rows), len(res), len(orders), secs)]
    print(NL.join(L_))
    if dry:
        return
    if git(PP, 'log', '--format=%h', '-1', '--', V25).strip():
        die('THE EDITION IS COMMITTED: THE SEARCH STANDS BEFORE ITS COMMIT OR NOT AT ALL')
    j = dict(at=at, act=ACT, document=V25, source=V24, base=head, relay=git(RELAY, 'rev-parse', 'HEAD').strip(), live_papers=len(live), faces=nfaces, seconds=round(secs, 1),
             rows=rows, quoting=[list(x) for x in res], orders=dict((k, [list(x) for x in sorted(v)]) for k, v in orders.items()),
             readings=['%s :%d -- %s' % (p, n, w) for (p, n), w in sorted(READINGS.items())],
             by_class=dict((c, len(v)) for c, v in by.items()), text=L_)
    I, _SC = ids()
    a = idcount(json.dumps(j, ensure_ascii=False), I)
    if any(a.values()):
        die('AN IDENTIFIER IN THE QUOTE BANK %s' % a)
    put(QBANK, json.dumps(j, ensure_ascii=False, indent=1) + NL)
    print('written data/b760_quote.json (%d rows)' % len(rows))


def cut(commit, dry):
    q = json.load(open(QBANK, encoding='utf-8'))
    t = text_bank()
    keys = block_w(t)
    full, L = v24()
    p = os.path.join(PP, V25)
    now = (git(PP, 'show', '%s:%s' % (commit, V25)) if commit else open(p, encoding='utf-8').read()).replace('\r', '')
    i = now.find('<!-- b760 (R370)')
    body_now = now[:i] if i > 0 else now
    norm = lambda s: ' '.join((s or '').split())   # noqa: E731
    nb, nn = norm(full), norm(body_now)
    rows = []
    for k in keys:
        kd = k['kind']
        if kd in ('WHOLE', 'PART', 'REMOVE'):
            st = k['old'] if kd == 'PART' else L[k['n'] - 1]
            shown = k['old'] if k['n'] in ID_LINES else st
            rows.append(dict(key=k['key'], line=k['n'], kind=kd, change=True, base=norm(st) in nb, now=norm(st) in nn, text=shown[:110] if k['n'] not in ID_LINES else shown))
        else:
            piece = max(re.split(r'‹[^›]*›', k['new']), key=len)   # ### a field (DATE, AX) filled at the write: the NEW read by its longest field-free piece
            rows.append(dict(key=k['key'], line=k['n'], kind=kd, change=False, base=norm(piece) in nb, now=norm(piece) in nn, text=k['new'][:110]))
    for rid, n, old, new, *_r in RESTATE:
        rows.append(dict(key=rid, line=n, kind='RESTATEMENT', change=True, base=norm(old) in nb, now=norm(old) in nn, text=old[:110]))
    before = sum(1 for r in rows if r['change'] and r['base'])
    after = sum(1 for r in rows if r['change'] and r['now'])
    added = sum(1 for r in rows if not r['change'] and r['now'])
    res = q.get('quoting') or []
    L_ = ['%s -- COMPONENT 4, (R370)(7) AND (8): THE EDITION OF %s AS A CUT, ITS DISTANCE, ITS RESIDUES (%s)' % (ACT, FAMILY.replace('.md', ''), utc()), '',
          '### the cut: BLOCK W`s keys and the %d restatements of I-29 applied to v2.4.0`s bytes in the new file %s; v2.4.0 and v2.3.1 unedited.' % (len(RESTATE), V25),
          '### the base v2.4.0 at PLACE-papers HEAD (sha256 %s) ; now %s, its body before the b760 back matter (which lists both wordings).' % (sha(full)[:16], ('%s:%s' % (commit, V25)) if commit else 'the working file'),
          '### THE DISTANCE BY THE b670 METHOD: each changed text searched whitespace-normalized at the base and now, the row met where it no longer stands;',
          '### each added text met where it stands now. Rows: key | v2.4.0 line | kind | at the base | now | the text (v2.4.0 :3 by W0`s words alone):']
    for r in rows:
        L_.append('  %-6s :%-3d | %-12s | base %-5s | now %-5s | %s' % (r['key'], r['line'], r['kind'], r['base'], r['now'], r['text']))
    L_ += ['', '### THE RESIDUES (data/b690_rules.txt row (2); data/b760_quote.json, two shapes, the search run before the edition`s commit at %s): each quoting line,' % q.get('at'),
           '### file :line -- a live paper`s an order W-ORD-RECUT-QUOTE-<key>, a face`s carried; none written:']
    L_ += ['  %s :%d' % (f, n) for f, n in res] or ['  NONE']
    L_ += ['', '### THE ORDERS: %s' % ('; '.join('W-ORD-RECUT-QUOTE-%s: %s' % (k, ', '.join('%s :%d' % tuple(x) for x in v)) for k, v in sorted((q.get('orders') or {}).items())) or 'NONE'),
           '### ### **THE DISTANCE BY THE b670 METHOD: BEFORE %d, AFTER %d ; ADDITIONS STANDING %d OF %d ; QUOTING LINES %d ENTERED AS RESIDUES ; ORDERS %d.**' % (
               before, after, added, sum(1 for r in rows if not r['change']), len(res), len(q.get('orders') or {}))]
    print(NL.join(L_))
    if dry:
        return
    I, _SC = ids()
    j = dict(at=utc(), document=V25, base=(commit + '^') if commit else '', before=before, after=after, residues=res, held=[], orders=q.get('orders') or {}, rows=rows)
    for txt in (NL.join(L_), json.dumps(j, ensure_ascii=False)):
        a = idcount(txt, I)
        if any(a.values()):
            die('AN IDENTIFIER IN THE CUT BANK %s' % a)
    put(CTXT, NL.join(L_) + NL)
    put(CBANK, json.dumps(j, ensure_ascii=False, indent=1) + NL)
    print('written data/b760_wsc_cut.txt and data/b760_cut.json')


CHDR = re.compile(r'^@@ (C\d+[a-z]?) \| (\S+\.md) :(\d+) \| (\S+)$')


def late(dry):
    t = open(os.path.join(D, BLOCK_D), encoding='utf-8').read().replace('\r', '').split(NL)
    i0 = next(i for i, l in enumerate(t) if l.startswith('@@ BLOCK D'))
    keys = []
    for i in range(i0, len(t)):
        m = CHDR.match(t[i])
        if m and i + 1 < len(t) and t[i + 1].startswith('OLD: '):
            keys.append(dict(key=m.group(1), path=m.group(2), n=int(m.group(3)), kind=m.group(4), old=t[i + 1][5:],
                             new=t[i + 2][5:] if i + 2 < len(t) and t[i + 2].startswith('NEW: ') else ''))
    if len(keys) != 14:
        die('BLOCK D CARRIES %d KEYS, NOT 14' % len(keys))
    import subject as S
    live, _fig = S.live_papers('HEAD', PP)
    live = set(live)
    rows = []
    for k in keys:
        ps = pieces(k['old']) or [k['old'].strip()]
        for p in ps:
            rows.append(dict(key=k['key'], line_no=k['n'], path=k['path'], line=k['old'], needle=p, wide=wide(p), new=k['new']))
    own_of = lambda r, path, ln: path == r['path'] and ln == r['line_no']   # noqa: E731
    # ### a row's family is its own key's paper: another edition of that paper is not a quotation of it
    secs, nfaces = search(rows, own_of, live, lambda r, p: S.family_of(p) == S.family_of(r['path']))
    by, res, orders = summarize(rows)
    at = utc()
    L_ = ['%s -- (R370)(8): THE LATE SEARCH -- THE FOURTEEN OLD LINES OF (R369)(9) (data/b759_text.txt BLOCK D), NEEDLED IN b708`S PAPER FORM (%s)' % (ACT, at), '',
          '### LATE: b759 replaced these lines at (R369)(9) with no quotation search (the navigator`s (vii), data/b760_ferry.txt :9); this search runs',
          '### after their replacement, at PLACE-papers HEAD %s and the relay HEAD %s. The live papers by tools/standing/subject.py live_papers (%d);' % (
              git(PP, 'rev-parse', '--short=8', 'HEAD').strip(), git(RELAY, 'rev-parse', '--short=8', 'HEAD').strip(), len(live)),
          '### the relay`s faces its tracked Markdown pages (%d). Each OLD split into its sentences (a short OLD whole), each an exact needle, its longest' % nfaces,
          '### clause of four words or more a case-insensitive one. A hit is printed by path, line and sha256 alone. Classes as data/b760_quote.json.', '']
    for r in rows:
        L_.append('  %s %s :%d | %d | %d | own %d | %r' % (r['key'], r['path'], r['line_no'], len(r['hits']), len(r['hits_wide']), len(r['own']), r['needle'][:70]))
        L_ += hit_lines(r, 'b759`s NEW of %s (%s :%d, as re-cut)' % (r['key'], r['path'], r['line_no']), LATE_READINGS)
    L_ += ['', '### BY CLASS, DISTINCT LINES: ' + (' ; '.join('%s %d' % (c, len(v)) for c, v in sorted(by.items())) or 'none'),
           '### THE QUOTING LINES (live and face): %s' % ('; '.join('%s :%d' % x for x in res) or 'NONE'),
           '### THE ORDERS (each a live paper`s line, not edited): %s' % ('; '.join('W-ORD-RECUT-QUOTE-%s: %s' % (k, ', '.join('%s :%d' % x for x in sorted(v))) for k, v in sorted(orders.items())) or 'NONE'),
           '### ### **THE LATE SEARCH: KEYS 14 ; NEEDLES %d IN TWO SHAPES ; QUOTING LINES %d ; ORDERS %d ; %.1f s ; LATE, AFTER b759`S REPLACEMENT.**' % (len(rows), len(res), len(orders), secs)]
    print(NL.join(L_))
    if dry:
        return
    j = dict(at=at, act=ACT, source='data/b759_text.txt BLOCK D', late=True, base=git(PP, 'rev-parse', 'HEAD').strip(),
             relay=git(RELAY, 'rev-parse', 'HEAD').strip(), live_papers=len(live), faces=nfaces, seconds=round(secs, 1), rows=rows,
             quoting=[list(x) for x in res], orders=dict((k, [list(x) for x in sorted(v)]) for k, v in orders.items()),
             readings=['%s :%d -- %s' % (p, n, w) for (p, n), w in sorted(LATE_READINGS.items())],
             by_class=dict((c, len(v)) for c, v in by.items()))
    I, _SC = ids()
    a = idcount(NL.join(L_) + json.dumps(j, ensure_ascii=False), I)
    if any(a.values()):
        die('AN IDENTIFIER IN THE LATE BANK %s' % a)
    put(LBANK, NL.join(L_) + NL)
    put(LJSON, json.dumps(j, ensure_ascii=False, indent=1) + NL)
    print('written data/b760_late_quotes.txt and data/b760_late_quotes.json (%d rows)' % len(rows))


def main(argv):
    mode = argv[0] if argv else ''
    dry = 'dry' in argv[1:]
    if mode in ('dry', 'write'):
        edition(mode)
    elif mode == 'quote':
        quote(dry)
    elif mode == 'cut':
        c = next((a for a in argv[1:] if re.match(r'^[0-9a-f]{7,40}$', a)), None)
        cut(c, dry)
    elif mode == 'late':
        late(dry)
    elif mode == 'controls':
        controls_again()
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
