# -*- coding: utf-8 -*-
"""test_chain_page_b596.py -- THE TEST OF THE TWO GENERATOR CLAUSES b596 ADDED TO tools/chain_page.py, on the author's answers
(relay data/b596_author_answers.txt, prompt 1 before the seal, prompt 3 after the pages' first re-emission).

### (1)-(2) A LIST WITHOUT A `# backmatter:` RECORD REGENERATES BYTE FOR BYTE: b592's ζ and χ lists re-emitted from their v0.16
###   probe outputs by the generator as it stands, against each page's blob at PLACE-papers ba5f0ea (the pages before b596).
### (3) THE CHANNEL: b592's ζ list with two `# backmatter:` records appended, re-emitted from the same probe -- the page is the
###   page of (1) with one paragraph after the Correspondence table, the records' text in list order joined by one space.
### (4) THE READER: backmatter_of reads no record from b592's lists and the two records, in order, from the list of (3).
### (5) THE ENTRY TAG OF A STRUCTURE: entry_tag finds SIDEExplicitFormula.Simplicity.SimpleProportion (a `structure`) at v0.17,
###   and still finds a theorem (simplicity_iff) and a definition (allSimple) of the same file at v0.17.
### (6)-(9) b622, (R232)(4): THE SHAPE READER (`shape_of`) on the ruling's five test nodes from their pages' banked probes, its positive
###   control (each statement mutated where the reader reads it), an object, and the column's switch (`node_column`): a list without
###   the line emits as before, b602's list with it gains one head line and one shape cell per node line.
### Usage: python tools/test_chain_page_b596.py
### ### b597, (R207)(2) and the author's answer before b597's seal (relay data/b597_author_answers.txt): THE CONTROL FROZEN AT WHAT IT
### CONTROLS. Cases (1)-(4) and the suite's control arm G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA read b592's two lists and probe
### outputs by `git show` at relay 12c15c80 (their one commit), and the generator's every HEAD read is redirected for the run: the
### terminal table at relay 12c15c80 (blob 2ce26253, the blob at ac8257a5), README, REGISTRY, the keystone grep and the expected
### pages at PLACE-papers ba5f0ea. One pin per repository; tools/chain_page.py is untouched (its `git` is swapped in this file).
"""
import io
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import chain_page as C   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PRE_PP = 'ba5f0ea'
RELAY_PIN = '12c15c80'
ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
LISTS = (('b592_nodes.txt', 'b592_probe_out.txt', 'PAGE_NAME'), ('b592_nodes_chi.txt', 'b592_chi_probe_out.txt', 'DIR_PAGE_NAME'))
NL = chr(10)


def blob(spec):
    r = subprocess.run(['git', '-C', C.PP, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def relay_blob(path):
    r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (RELAY_PIN, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def _frozen_git(repo, *a):
    """### the generator's own `git`, every HEAD read redirected: relay HEAD -> 12c15c80, PLACE-papers HEAD -> ba5f0ea."""
    a = list(a)
    r = repo.replace(chr(92), '/')
    if a[:1] == ['show'] and len(a) > 1 and a[1].startswith('HEAD:'):
        if r == ROOT.replace(chr(92), '/'):
            a[1] = RELAY_PIN + a[1][4:]
        elif r == C.PP:
            a[1] = PRE_PP + a[1][4:]
    elif r == C.PP and a[:1] == ['grep'] and 'HEAD' in a:
        a[a.index('HEAD')] = PRE_PP
    return _GIT(repo, *a)


_GIT = C.git


def pinned_lists():
    """### b592's two lists and probe outputs written from relay 12c15c80 into a fresh directory, under their own names."""
    d = tempfile.mkdtemp()
    out = []
    for ln, pn, page in LISTS:
        lb, pb = relay_blob('data/' + ln), relay_blob('data/' + pn)
        if lb is None or pb is None:
            return None
        lp, pp = os.path.join(d, ln), os.path.join(d, pn)
        open(lp, 'wb').write(lb)
        open(pp, 'wb').write(pb)
        out.append((lp, pp, getattr(C, page)))
    return out


def regen(nodes, probe):
    C.git = _frozen_git
    try:
        rc, page, _meta, log = C.build(nodes, tempfile.mkdtemp(), probe)
    finally:
        C.git = _GIT
    return rc, (page.encode('utf-8') if rc == 0 and page is not None else None)


def control():
    """### THE ARM G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA: each list re-emitted frozen, against its page at ba5f0ea."""
    import g_chain_page as GCP
    pl = pinned_lists()
    if pl is None:
        return [dict(ok=False, rc=-1, list=x[0], first_diff=None, committed_bytes=0, regenerated_bytes=0) for x in LISTS]
    res = []
    for lp, pp, page in pl:
        rc, got = regen(lp, pp)
        com = blob('%s:%s' % (PRE_PP, page))
        ok, at = GCP.compare(com, got)
        res.append(dict(ok=ok, rc=rc, list=os.path.basename(lp), first_diff=at, committed_bytes=len(com or b''), regenerated_bytes=len(got or b'')))
    return res


def main():
    res = []
    print('### pins: relay %s (the lists, the probes, the terminal table blob %s) ; PLACE-papers %s (pages, README, REGISTRY, keystones)' % (
        RELAY_PIN, subprocess.run(['git', '-C', ROOT, 'rev-parse', '--short=8', RELAY_PIN + ':data/terminal_table.json'],
                                  capture_output=True).stdout.decode().strip(), PRE_PP))
    (zl, zp, _zn), (cl, cp, _cn) = pinned_lists()
    rc1, z = regen(zl, zp)
    res.append(('(1) b592 ζ list, no record: byte for byte against the page at %s' % PRE_PP, rc1 == 0 and z == blob('%s:%s' % (PRE_PP, C.PAGE_NAME))))
    rc2, c = regen(cl, cp)
    res.append(('(2) b592 χ list, no record: byte for byte against the page at %s' % PRE_PP, rc2 == 0 and c == blob('%s:%s' % (PRE_PP, C.DIR_PAGE_NAME))))
    d = tempfile.mkdtemp()
    tl = os.path.join(d, 'b592_nodes.txt')
    src = io.open(zl, encoding='utf-8').read()
    io.open(tl, 'w', encoding='utf-8', newline=NL).write(src.rstrip(NL) + NL + '# backmatter: first record, its words' + NL + '# backmatter: second record.' + NL)
    rc3, t = regen(tl, zp)
    want = (z or b'') + (NL + 'first record, its words second record.' + NL).encode('utf-8')
    res.append(('(3) two records: the page of (1) with one paragraph after the Correspondence table', rc3 == 0 and z is not None and t == want))
    res.append(('(4) the reader: no record from b592`s lists; the two, in order, from the list of (3)',
                C.backmatter_of(zl) == [] and C.backmatter_of(cl) == [] and C.backmatter_of(tl) == ['first record, its words', 'second record.']))
    rel = 'SIDEExplicitFormula/Simplicity.lean'
    e = [C.entry_tag(rel, n) for n in ('SimpleProportion', 'simplicity_iff', 'allSimple')]
    res.append(('(5) the entry tag of a structure, a theorem and a definition of Simplicity.lean: %s' % e,
                all(x == ('v0.17', '5a1630b') for x in e)))
    # ### b622, (R232)(4): THE SHAPE READER AND THE COLUMN. (6) the ruling's five test nodes read from their pages' banked probes (b602's at
    # ### v0.20, b603's at v0.21); (7) the positive control: each statement mutated where the reader reads it, every read must move off its
    # ### shape; (8) an object reads —; (9) the switch: no list of b592's, b602's or b603's carries the column's line, and b602's list with
    # ### the line added emits b602's page with one head line and one shape cell on each node line, nothing else.
    zc = C.parse(io.open(os.path.join(D, 'b602_probe_out.txt'), encoding='utf-8').read().replace(chr(13), ''))[0]
    cc = C.parse(io.open(os.path.join(D, 'b603_chi_probe_out.txt'), encoding='utf-8').read().replace(chr(13), ''))[0]
    five = [(zc, 'SIDEExplicitFormula.KeiperSign.liCoeff_one_pos', 'FINITE', '∀ (n : ℕ), 0 < SIDEExplicitFormula.LiWeil.LiCoeff n'),
            (zc, 'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'UNIVERSAL', '0 < 1 ↔ 0 < 2'),
            (zc, 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh', 'UNIVERSAL', 'Filter.Tendsto f l₁ l₂'),
            (zc, 'SIDEExplicitFormula.Simplicity.exceptional_mass_le_third', 'DENSITY', None),
            (cc, 'SIDEExplicitFormula.Schema.Family.family_theorem', 'FAMILY', None)]
    got = [C.shape_of(n, cs) for cs, n, _w, _m in five]
    res.append(('(6) the five test nodes read %s' % got, got == [w for _c, _n, w, _m in five]))

    def mutated(cs, n, stmt):
        m = dict(cs)
        m[n] = dict(cs[n], statement=stmt)
        return C.shape_of(n, m)
    ex, fam = five[3][1], five[4][1]
    pos = [mutated(cs, n, 'theorem %s : %s' % (n, s)) for cs, n, _w, s in five[:3]]
    pos.append(mutated(zc, ex, zc[ex]['statement'].replace('Zeta23.Ncount', 'Zeta23.Mcount').replace('Zeta23.N0simple', 'Zeta23.M0simple')))
    pos.append(mutated(cc, fam, cc[fam]['statement'].replace('∀ χ ∈ SIDEExplicitFormula.Schema.Family.family q,', '∀ (m : ℕ),')))
    res.append(('(7) the positive control: the five statements mutated where the reader reads them read %s, none its unmutated shape' % pos,
                all(p != w for p, (_c, _n, w, _m) in zip(pos, five))))
    ob = [C.shape_of('riemannZeta', zc), C.shape_of('SIDEExplicitFormula.Schema.Family.familyConfig', cc)]
    res.append(('(8) an object reads —: riemannZeta and familyConfig read %s' % ob, ob == ['—', '—']))
    d2 = tempfile.mkdtemp()
    tl2 = os.path.join(d2, 'b602_nodes_zeta.txt')
    io.open(tl2, 'w', encoding='utf-8', newline=NL).write(io.open(os.path.join(D, 'b602_nodes_zeta.txt'), encoding='utf-8').read().replace(chr(13), '').rstrip(NL)
                                                         + NL + C.COLUMN_MARK + NL)
    r0 = C.build(os.path.join(D, 'b602_nodes_zeta.txt'), tempfile.mkdtemp(), os.path.join(D, 'b602_probe_out.txt'))
    r1 = C.build(tl2, tempfile.mkdtemp(), os.path.join(D, 'b602_probe_out.txt'))
    p0, p1 = (r0[1] or ''), (r1[1] or '')
    cells_pat = r' — shape: (FINITE|BOUNDED|UNIVERSAL|LIMIT|DENSITY|FAMILY|UNCLASSIFIED|—)(?= — premises: )'
    stripped = re.sub(cells_pat, '', p1.replace(NL + C.SHAPE_KEY + NL, '', 1))
    nshape = len(re.findall(cells_pat, p1))
    nnodes = len(r0[2]['order']) if r0[0] == 0 else -1
    switch = [C.node_column(x) for x in (zl, cl, os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(D, 'b603_nodes_chi.txt'))]
    res.append(('(9) the switch: off on b592`s, b602`s and b603`s lists %s, on with its line; the page with it is the page without it, one head '
                'line and %d shape cells on %d node lines added' % (switch, nshape, nnodes),
                r0[0] == 0 and r1[0] == 0 and not any(switch) and C.node_column(tl2) and stripped == p0 and nshape == nnodes
                and p1.count(C.SHAPE_KEY) == 1 and p0.count(C.SHAPE_KEY) == 0))
    # ### b627, (R237)(3): THE BOUNDED WORD. (10) the rung's nodes from b626's probe at v0.22: rh_upto (a definition, ∀ ρ under
    # ### |ρ.im| ≤ T) and rh_upto_platt (read through rh_upto) read BOUNDED; (11) the word in the column's order between FINITE and
    # ### UNIVERSAL and named by the key line, with the UNIVERSAL control -- the height pair, rh_upto with its bound removed, and rh_upto
    # ### with a bound that mentions the variable, each reading UNIVERSAL.
    rc_ = C.parse(io.open(os.path.join(D, 'b626_probe_out.txt'), encoding='utf-8').read().replace(chr(13), ''))[0]
    up, upp, pair = ('SIDEExplicitFormula.PlattRung.%s' % s for s in ('rh_upto', 'rh_upto_platt', 'forall_rh_upto_iff_rh'))
    got10 = [C.shape_of(n, rc_) for n in (up, upp)]
    res.append(('(10) rh_upto and rh_upto_platt read %s' % got10, got10 == ['BOUNDED', 'BOUNDED']))
    st = rc_[up]['statement']
    ctl = [C.shape_of(pair, rc_), mutated(rc_, up, st.replace(' → |ρ.im| ≤ T', '')), mutated(rc_, up, st.replace('|ρ.im| ≤ T', '|ρ.im| ≤ ρ.re'))]
    res.append(('(11) the word between FINITE and UNIVERSAL, named by the key; the UNIVERSAL control (the pair, the bound removed, a bound '
                'mentioning ρ) reads %s' % ctl, 'BOUNDED' in C.SHAPES and C.SHAPES.index('BOUNDED') == C.SHAPES.index('FINITE') + 1
                == C.SHAPES.index('UNIVERSAL') - 1 and 'BOUNDED for a quantifier' in C.SHAPE_KEY and ctl == ['UNIVERSAL'] * 3
                and '|ρ.im| ≤ T' in st))
    for name, ok in res:
        print('  %-120s %s' % (name, 'PASS' if ok else 'FAIL'))
    ok = all(x for _n, x in res)
    print('### %s' % ('ALL PASS' if ok else 'NOT ALL PASS'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
