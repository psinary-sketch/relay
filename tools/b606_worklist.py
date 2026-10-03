# -*- coding: utf-8 -*-
"""b606_worklist.py -- CP-8 ACT ONE'S WORK-LIST AS DATA, UNDER (R216)(2)-(3). ### NO WRITE.

### The eleven ceiling uses of relay data/b584_ceiling_census.txt (A_Place_to_Stand: live 11), re-derived by line with
### b584_record's own classifier (`PHRASE`, `OBJECT`, `NEGATED`, `HEDGED`, imported) at the census pin 9d11874, whose blob of
### day1/A_Place_to_Stand.md is the current version's; each with the seat's rewrite (the ceiling clause, OPEN_TRAILS :11906:
### the sentence takes the object it names) or a carry with its reason. The errata ERRATA.md addresses to the monograph, each
### sentence with its live line resolved against the current version's blob and its replacement as ERRATA (or the relay bank
### ERRATA cites) prints it, rendered in the document's own typography by RENDER (printed raw and rendered in the bank).
### Every resolution reads git blobs at their pins; nothing here writes.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
PP = 'D:/MY-DOwnloads/PLACE-papers'
CUR = 'day1/A_Place_to_Stand.md'
ED = 'day1/A_Place_to_Stand_v5_14.md'
CENSUS_PIN = '9d11874'
PRE_PP = 'cabbed7'
NL = chr(10)


def show(rev, path, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


# ================================================================================ THE PINS THE REWRITES CITE, AS THE PAGES PRINT THEM
PINS = {
    'h2_sign_iff_rh': ('SIDEExplicitFormula.B321.h2_sign_iff_rh', 'v0.2 = 5c72cad', 'ζ page node 8'),
    'ch_iff_rh': ('SIDEExplicitFormula.B321.ch_iff_rh', 'v0.1 = baed4df', 'ζ page node 7'),
    'simplicity_iff': ('SIDEExplicitFormula.Simplicity.simplicity_iff', 'v0.17 = 5a1630b', 'ζ page node 41'),
    'h2_sign_chi_iff_grh_chi': ('SIDEExplicitFormula.GRHWeil.h2_sign_chi_iff_grh_chi', 'v0.14 = 4dce7b9', 'χ page node 12'),
}

# ================================================================================ THE ELEVEN CEILING USES
# ### (id, line at v5.13, the phrase the classifier read, the sentence as it stands, the action, the new sentence or None, the reason)
USES = [
    ('U01', 31, 'proof of', 'This document presents a proof of Theorem (RH) — the Riemann Hypothesis — and the research programme from which it emerged.',
     'rewrite', 'This document presents the reduction of Theorem (RH) — the Riemann Hypothesis — to a single located clause, h2_sign, compiled '
                'equivalent to RH (h2_sign_iff_rh, SIDE-explicit-formula v0.2) and open, and the research programme from which it emerged.',
     'beyond the README ceiling (README :106-:121): "a proof of" RH; the object it names is the reduction to the located clause'),
    ('U02', 64, 'proof of', '**For the proof of RH:** Read Parts I–III in sequence (2 hours).',
     'rewrite', '**For the reduction of RH to its located clause:** Read Parts I–III in sequence (2 hours).',
     'beyond the ceiling: "the proof of RH"; the object Parts I-III carry is the reduction'),
    ('U03', 405, 'proved', 'Theorem (RH) — proved in this work — states they all lie at the crossroads.',
     'rewrite', 'Theorem (RH) — reduced in this work to a single located clause, h2_sign, equivalent to RH (h2_sign_iff_rh) and open — '
                'states they all lie at the crossroads.',
     'beyond the ceiling: RH "proved in this work"'),
    ('U04', 1272, 'proof of', 'The proof of Chapter 19, applied to each L(s, χ) individually, gives GRH.',
     'rewrite', 'The argument of Chapter 19, applied to each L(s, χ) individually, reduces GRH for χ to its located clause, h2_sign_chi, '
                'equivalent to GRH for χ (h2_sign_chi_iff_grh_chi, SIDE-explicit-formula v0.14) and open.',
     'beyond the ceiling: the argument "gives GRH"; the object compiled is the χ-instance of the clause and its equivalence'),
    ('U05', 1303, 'proof of', 'Part III assembled the proof of RH through mechanism enumeration.',
     'rewrite', 'Part III assembled the reduction of RH through mechanism enumeration, under the named premise h2, open and equivalent to '
                'RH in its Weil form (h2_sign_iff_rh).',
     'beyond the ceiling: "the proof of RH"'),
    ('U06', 1336, 'established', 'The direction established here is the reverse: from simplicity toward RH.',
     'rewrite', 'The direction argued here is the reverse: from simplicity toward RH, an edge no compiled statement carries (simplicity is '
                'a separate located clause, simplicity_iff, SIDE-explicit-formula v0.17).',
     'beyond the ceiling: the direction simplicity -> RH "established"; simplicity is a separate Prop with no compiled edge to h2_sign '
     '(SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3, chapter 1 title)'),
    ('U07', 1407, 'proves', 'Part III proves RH through mechanism enumeration: seven classes, none producing off-line zeros, exhaustive by Ostrowski.',
     'rewrite', 'Part III reduces RH through mechanism enumeration to the named premise h2: seven classes, none producing off-line zeros, '
                'exhaustive by Ostrowski.',
     'beyond the ceiling: "proves RH"'),
    ('U08', 1407, 'proves', 'Part IV proves RH from simplicity: perpendicular crossing, monotonicity, fold exclusion.',
     'rewrite', 'Part IV argues RH from simplicity: perpendicular crossing, monotonicity, fold exclusion — an edge no compiled statement '
                'carries (simplicity_iff).',
     'beyond the ceiling: "proves RH"'),
    ('U09', 1562, 'proves', '**The RH-reduction theorem.** `Integration.lean` defines the proposition `Integration.StructuralExhaustiveness` as '
                            '`∀ σ, is_xi_zero σ → σ = 1/2` — a direct restatement of RH on the σ-coordinate — and proves:',
     'carry', None,
     'within the ceiling: "proves" governs the compiled theorem printed beneath (rh_from_structural_exhaustiveness), a reduction the '
     'kernel compiles, and RH is the object of "restatement", not of "proves"'),
    ('U10', 1795, 'proof of', 'The main proof of RH (Part III) depends on the arithmetic clause alone; the geometric clause is Part IV\'s, carried by '
                              'its independent strategy.',
     'rewrite', 'The main argument for RH (Part III) depends on the arithmetic clause alone, open and equivalent to RH in its Weil form '
                '(h2_sign_iff_rh); the geometric clause is Part IV\'s, carried by its independent strategy.',
     'beyond the ceiling: "the main proof of RH"'),
    ('U11', 1946, 'Proved', '| 13 | GRH for Dirichlet L-functions | Chapter 21 | Proved (from RH via twist cancellation) |',
     'erratum', None,
     'beyond the ceiling: GRH "Proved (from RH ...)"; the same sentence is E-2026-09-25-6\'s Appendix A row 13, whose replacement '
     'governs (collision C1)'),
]

# ================================================================================ THE ERRATA ADDRESSED TO THE MONOGRAPH, BY ID
# ### every entry ERRATA.md addresses to A_Place_to_Stand, with what the seat read of its live lines (printed in the bank).
ERRATA_IDS = [
    ('E-2026-07-23-1', 'none', '§18.2 Im(ξ) -> Re(ξ): remedied in the live text at v5.9.1 (:1121 reads "is Re(ξ)")'),
    ('E-2026-07-12-1', 'none', 'deposited v5.4 axiom claims against kernel v1.1; the remedy, kernel v1.2, makes the live §25.5/§25.7 claims hold'),
    ('E-2026-07-13-1', 'none', 'the entry`s own finding 5: the live monograph is count-clean, no live site affected'),
    ('E-2026-07-18-1', 'none', 'the deposited in-file stamp; the live stamp :19 and the log :2197 agree at v5.13'),
    ('E-2026-07-27', 'none', 'the v5.13 audit-trail record; no prior claim corrected'),
    ('E-2026-08-24-1', 'none', 'REGISTRY`s Day-1 deposit lines and the record`s file list; no sentence of the monograph`s text'),
    ('E-2026-08-24-2', 'none', 'the deposited record TITLES (Zenodo metadata); no sentence of the monograph`s text'),
    ('THE PARTITION', 'none', 'the partition of ERRATA`s entries (b337); it addresses no sentence'),
    ('E-2026-09-14-1', 'none', 'the entry`s own words: "This entry corrects nothing in the monograph."'),
    ('E-2026-09-25-3', 'none', 'THE_UNCONDITIONAL_SURROUND and SIDE-lv-conservation`s record; it names the monograph`s §27.3 only as their source'),
    ('E-2026-10-01-1', 'none', 'the record descriptions of the deposit and of SIDE-kernel v1.5 (Zenodo); no sentence of the monograph`s text'),
    ('E-2026-09-22-1', 'live', 'four deposited sentences, live :68, :1793 (two), :1797; NO replacement -- disposition (ii) waits on the wave'),
    ('E-2026-09-25-1', 'live', 'ten monograph rows M-02 .. M-24, every one live; replacements in relay data/b532_rows.txt, the bank the entry cites'),
    ('E-2026-09-25-4', 'live', 'four deposited §27.3 sentences, live :1801, :1808 (two), :1814'),
    ('E-2026-09-25-5', 'live', 'nineteen sentences through §25.8; seventeen live, two deposit-only (deposited :127, :201 at v1.1.2)'),
    ('E-2026-09-25-6', 'live', 'fifteen sentences from §26.1 to the end, every one live'),
]
FIVE = [e for e, k, _w in ERRATA_IDS if k == 'live']

# ================================================================================ RENDERING (the act`s reading R-3, declared on the face)
RENDER_SUBS = [(' -- ', ' — '), ('xi-zero', 'ξ-zero'), ('sigma = 1/2', 'σ = 1/2'), ('section 27.3', '§27.3')]


def render(raw, b532=False):
    t, used = raw, []
    if b532:
        t2 = re.sub(r'(\w)`s\b', r"\1's", t)
        if t2 != t:
            used.append('backtick possessive -> apostrophe')
        t = t2
    for a, b in RENDER_SUBS:
        if a in t and (b532 or a == ' -- '):
            t = t.replace(a, b)
            used.append('%r -> %r' % (a, b))
    return t, used


def nz(s):
    return re.sub(r'\s+', ' ', s.replace('`', '').replace('*', '')).strip()


def span_re(q):
    """### the live span of an ERRATA quotation, which drops backticks and asterisks: each character may be followed by markup."""
    out = [r'[`*]*']
    for c in nz(q):
        out.append(r'\s+' if c == ' ' else re.escape(c))
        out.append(r'[`*]*')
    return re.compile(''.join(out))


def balance(s):
    """### a matched span keeps only the markup it closes: strip both ends, then restore a bold pair or a backtick pair the core
    ### leaves open."""
    core = s.strip('`*')
    lead, tail = s[:len(s) - len(s.lstrip('`*'))], s[len(s.rstrip('`*')):]
    if core.count('**') % 2 == 1:
        if lead.endswith('**'):
            core = '**' + core
        elif tail.startswith('**'):
            core = core + '**'
    elif lead.endswith('**') and tail.startswith('**'):
        core = '**' + core + '**'
    if core.count('`') % 2 == 1:
        if lead.endswith('`'):
            core = '`' + core
        elif tail.startswith('`'):
            core = core + '`'
    return core


MARK = re.compile(r'\*\*([^*]+?)\*\*|(?<![*\w])\*([^*\s][^*]*?)\*(?![*\w])|`([^`]+)`')


def remark(old, new):
    """### the act`s reading R-3 (declared on the face): the replacement`s words verbatim, the live sentence`s markup kept where the
    ### replacement repeats the marked words -- a bold label, an italic phrase, a backticked name -- each restoration listed."""
    used = []
    if re.fullmatch(r'\*\*[^*]+\*\*', old) and not new.startswith('**'):
        return '**' + new + '**', ['markup: the sentence bold whole, kept']
    for m in MARK.finditer(old):
        word = m.group(1) or m.group(2) or m.group(3)
        marked = m.group(0)
        if not word or marked in new:
            continue
        mm = re.search(r'(?<![`*\w])' + re.escape(word) + r'(?![`*\w])', new)
        if mm:
            new = new[:mm.start()] + marked + new[mm.end():]
            used.append('markup %s kept' % marked)
    return new, used


# ### special targets, by (eid, key): an override of the live span or of the replacement, each declared in the bank
SPECIAL = {
    # E-5's :1530 replacement is an elided partial (its own "..."): the parenthetical alone is replaced
    ('E-2026-09-25-5', 1530): dict(old=None, old_query='the product-formula chain (ProductFormula_Prime.lean, ProductFormula_Int.lean, ProductFormula_Rat.lean)',
                                   new_raw='the product-formula chain (ProductFormula_Int.lean, ProductFormula_Rat.lean -- the ProductFormula_Prime.lean named here is at no version of the kernel)',
                                   note='the replacement is an elided partial ("... the product-formula chain (...) ..."): its parenthetical replaces the live parenthetical, the rest of the sentence unchanged'),
    # E-5's LIVE-SOLE :125 is hard-wrapped over :125-:126; its first 125 characters are unchanged by the replacement
    ('E-2026-09-25-5', 125): dict(line=126, old_query='three compiled routes, and one open premise.',
                                  new_raw='three compiled route terminals (Route 3\'s premise RH restated, ch_iff_rh), and one open premise, RH-equivalent in its Weil form (h2_sign_iff_rh).',
                                  note='the sentence is hard-wrapped over :125-:126; the replacement agrees with it through "five identification paths, five closures, two strategies, three compiled route", so the change falls on :126 alone'),
    # E-6's Appendix H copy of "Three routes, three theorems, one conclusion." (ERRATA's "live :2219", the paragraph's lead line):
    # the sentence stands at :1607 and :2224; :1607 is E-5's, the Appendix H copy is :2224
    ('E-2026-09-25-6', 2219): dict(line=2224, only_quote='Three routes, three theorems', note='ERRATA prints "live :2219", the lead line of Appendix H`s paragraph; the sentence stands on '
                                                   ':2224 (and its §25.5 copy :1607 is E-2026-09-25-5`s)'),
    # ### E-6's M-04 kin "live :2219" for deposited :125 resolves by its text to :2225 (no override needed)
    # E-1's M-09 replacement drops the bold label "Route 3 — Conservation.", a title kept by the name-and-title exception
    ('E-2026-09-25-1', 'M-09'): dict(old_query_from='Bridge/ConservationBridge.lean defines',
                                     note='the bold label "**Route 3 — Conservation.**" is a title and carries (the name-and-title exception, OPEN_TRAILS :11934); the sentence after it is replaced'),
}


def _errata_bullets(E, eid):
    a = next(i for i, l in enumerate(E) if l.startswith('## ' + eid + ' '))
    b = next(i for i in range(a + 1, len(E)) if E[i].startswith('## '))
    out = []
    for i in range(a, b):
        m = re.match(r'^- \*\*(.*?)\*\* \((.*?)\): \*"(.*)"\*\s*$', E[i])
        if not m:
            continue
        rep = None
        for k in range(i + 1, min(i + 4, b)):
            mm = re.match(r'^  - replacement: \*"(.*)"\*\s*$', E[k])
            if mm:
                rep = mm.group(1)
                rep_line = k + 1
        live = re.search(r'live :(\d+)', m.group(1))
        dep = re.search(r'A_Place_to_Stand\.md:(\d+) at v1\.1\.2', m.group(1))
        out.append(dict(eid=eid, err_line=i + 1, rep_line=rep_line, head=m.group(1), section=m.group(2), quote=m.group(3), raw=rep,
                        errata_live=int(live.group(1)) if live else None, deposited=int(dep.group(1)) if dep else None,
                        label=(re.match(r'(D-\d+[a-z]?)', m.group(1)) or [None, None])[1] if eid == 'E-2026-09-25-4' else None))
    return out


def targets():
    """### every erratum sentence, resolved: its live line and exact span in the current version, its replacement raw and rendered."""
    E = lines_of(show('HEAD', 'ERRATA.md'))
    M = lines_of(show('HEAD', CUR))
    T = []
    for eid in ('E-2026-09-25-4', 'E-2026-09-25-5', 'E-2026-09-25-6'):
        T += _errata_bullets(E, eid)
    rows = json.load(io.open(os.path.join(ROOT, 'data', 'b532_rows.json'), encoding='utf-8'))['rows']
    e1 = next(i for i, l in enumerate(E) if l.startswith('## E-2026-09-25-1 '))
    for r in rows:
        if not r['id'].startswith('M-') or r['verdict'] != 'RESTS':
            continue
        el = next((i + 1 for i in range(e1, len(E)) if E[i].startswith('  - `%s`:' % r['id'])), None)
        T.append(dict(eid='E-2026-09-25-1', err_line=el, rep_line=None, head=r['id'], section=r['section'], quote=r['text'], raw=r['replacement'],
                      errata_live=None, deposited=None, label=r['id'], b532=True))
    for i, l in enumerate(E):
        m = re.match(r'^\| `A_Place_to_Stand\.md:(\d+)` \| \*“(.*?)”\* \|', l)
        if m:
            T.append(dict(eid='E-2026-09-22-1', err_line=i + 1, rep_line=None, head='A_Place_to_Stand.md:%s' % m.group(1), section='the table',
                          quote=m.group(2), raw=None, errata_live=None, deposited=int(m.group(1)), label=None))
    NM = [nz(l) for l in M]
    out = []
    for k, t in enumerate(T, 1):
        key = (t['eid'], t['label'] if t['eid'] == 'E-2026-09-25-1' else t['errata_live'])
        sp = SPECIAL.get(key, {})
        if 'only_quote' in sp and not t['quote'].startswith(sp['only_quote']):
            sp = {}
        q = t['quote']
        if 'old_query_from' in sp:
            q = q[q.index(sp['old_query_from'].split('/')[0]):] if sp['old_query_from'].split('/')[0] in q else q
            q = q[q.index('Bridge/'):]
        if 'old_query' in sp:
            q = sp['old_query']
        hits = [n for n, l in enumerate(NM, 1) if nz(q) in l]
        if 'line' in sp:
            hits = [sp['line']] if nz(q) in NM[sp['line'] - 1] else []
        line = hits[0] if len(hits) >= 1 else None
        old = None
        if line:
            m = span_re(q).search(M[line - 1])
            old = balance(m.group(0)) if m else None
        raw = sp.get('new_raw', t['raw'])
        new, used = (render(raw, t.get('b532', False)) if raw else (None, []))
        if new and old:
            new, mk = remark(old, new)
            used += mk
        out.append(dict(t, key=str(key[1]), hits=hits, line=line, query=q, old=old, raw_used=raw, new=new, render=used, note=sp.get('note')))
    return out


def ids():
    """### each target gets an id: <E-short>-<n> in ERRATA order (E1 by its M-row id)."""
    short = {'E-2026-09-22-1': 'E22', 'E-2026-09-25-1': 'E1', 'E-2026-09-25-4': 'E4', 'E-2026-09-25-5': 'E5', 'E-2026-09-25-6': 'E6'}
    T = targets()
    n = {}
    for t in T:
        s = short[t['eid']]
        n[s] = n.get(s, 0) + 1
        t['id'] = '%s-%s' % (s, t['label']) if s == 'E1' else '%s-%02d' % (s, n[s])
    return T


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    for t in ids():
        print(t['id'], t['eid'], 'ERR:%s' % t['err_line'], 'live', t['line'], t['hits'], 'old', 'OK' if t['old'] else '### NONE',
              '| new', 'NONE' if t['new'] is None else 'ok', t['render'])
