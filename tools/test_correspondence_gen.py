"""test_correspondence_gen.py -- the generator's four planted cases, under (R282)(4) (b672).

Each case is a planted table and planted sources (tags, print bank, grade bank, the declarations declared at the tag), run through
tools/correspondence_gen.py's regen_lines / regen_bytes with no git, no remote and no file read:
  (1) the tag moved: the kernel clause's version and commit go to the new tag; the profile and grade tokens follow the bank; the prose stays;
      a declaration the bank did not print reads NOT PRINTED AT <tag> (was <old profile> at <old pin>).
  (2) a declaration vanished: the profile token reads ABSENT AT <tag>; the pin and the status are kept.
  (3) a kernel with no print bank: the profile token reads NO PRINT BANK AT <tag>; the grade token carries UNREFRESHED.
  (4) a table already at its tag: the file's bytes identical (CRLF kept), and case (1)'s output run again is identical.
  (5) (b682, W-ORD-CORRESPONDENCE-RUNNER-BANKS) a kernel with a runner print bank at its tag, planted in the form b674, b676 and b678 banked
      it (an axioms bank beside its runner bank, in a scratch directory) and read by the generator's reader: a declaration absent from the
      kernel at the tag, and so from the bank, reads ABSENT AT <tag> and not NO PRINT BANK; a printed declaration reads the bank's verdict, the
      word NO PRINT BANK replaced by it; a declaration declared at the tag and not printed reads NOT PRINTED AT <tag> (b672's word kept).
Each case also checks that no row is gained or lost and no cell is left blank. Every check prints its expected and its read value (b682).

    python -X utf8 tools/test_correspondence_gen.py          prints the cases
    python -X utf8 tools/test_correspondence_gen.py bank [name]   also writes the print to data/<name> (default b672_gen_test.txt)
"""
import os, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import correspondence_gen as G

HEAD = '### Correspondence'
HDR = '| Claim | Kernel | Theorem (fully qualified) | Axiom profile | Status |'
SEP = '|:--|:--|:--|:--|:--|'
ANCHOR = dict(heading=HEAD, header=HDR)
C_OLD = 'a' * 7 + '1' * 33
C_NEW = 'b' * 7 + '2' * 33


def doc(rows):
    return ['# A planted document', '', HEAD, '', 'Prose above the table.', '', HDR, SEP] + rows + ['', 'Prose beneath the table.']


def ctx(tags, banks, present_set, grades):
    return dict(tags=tags, banks=banks, grades=grades, present=lambda k, c, n: (k, c[:7], n.split('.')[-1]) in present_set)


def cells_ok(lines):
    for l in lines:
        if l.startswith('|') and not G.SEP_ROW.match(l):
            if any(not G.cell(l, sp) for sp in G.spans(l)):
                return False
    return True


OUT = []


def check(name, got, want):
    ok = got == want
    OUT.append('    %-4s %s' % ('PASS' if ok else 'FAIL', name))
    OUT.append('         expected %r' % (want,))
    OUT.append('         read     %r' % (got,))
    return ok


def case1():
    OUT.append('### (1) THE TAG MOVED: SIDE-x v0.1.0 = `aaaaaaa` -> tag v0.2.0 at bbbbbbb; the bank prints Mod.thm with [propext]; the grade bank says INTERFACES')
    rows = ['| a claim | SIDE-x v0.1.0 = `aaaaaaa` (carried at y v0.3) | `Mod.thm` | `{propext, Classical.choice, Quot.sound}` | **DERIVES** — prose kept. |',
            '| inherited | v0.1.0 (`aaaaaaa`) | `Mod.two` | axiom-free | DERIVES |',
            '| bold pin | SIDE-x **`aaaaaaa`** (re-verified; drafted against v0.0 `ccccccc`) | `Mod.thm` | `{propext}` | DERIVES |',
            '| not printed | SIDE-x v0.1.0 = `aaaaaaa` | `Mod.np` | `{propext, Quot.sound}` | DERIVES |']
    c = ctx({'SIDE-x': ('v0.2.0', C_NEW)}, {'SIDE-x': dict(prints={'X.Mod.thm': ['propext'], 'X.Mod.two': []})},  # ### the bank prints `X.Mod.thm`
            {('SIDE-x', 'bbbbbbb', 'thm'), ('SIDE-x', 'bbbbbbb', 'two'), ('SIDE-x', 'bbbbbbb', 'np')},
            {'SIDE-x': {'X.Mod.thm': 'INTERFACES', 'X.Mod.two': 'DERIVES'}})
    L0 = doc(rows)
    L1, r = G.regen_lines(L0, ANCHOR, c, 'planted-1')
    ok = check('row 1 rewritten', L1[8], '| a claim | SIDE-x v0.2.0 = `bbbbbbb` (carried at y v0.3) | `Mod.thm` | `{propext}` | **INTERFACES** — prose kept. |')
    ok &= check('row 2 (inheriting) rewritten in its own form', L1[9], '| inherited | v0.2.0 (`bbbbbbb`) | `Mod.two` | axiom-free | DERIVES |')
    ok &= check('row 3 (a bold commit alone): the commit in place, the trailing prose and its pin kept', L1[10],
                '| bold pin | SIDE-x **`bbbbbbb`** (re-verified; drafted against v0.0 `ccccccc`) | `Mod.thm` | `{propext}` | INTERFACES |')
    ok &= check('row 4 (declared at the tag, not in the bank): NOT PRINTED AT the tag, the verified profile and its pin kept beside, the commit bare',
                L1[11], '| not printed | SIDE-x v0.2.0 = `bbbbbbb` | `Mod.np` | NOT PRINTED AT v0.2.0 (was `{propext, Quot.sound}` at v0.1.0 = aaaaaaa) | DERIVES |')
    ok &= check('lines outside the table untouched; row count equal', (L1[:8], L1[12:], len(L1)), (L0[:8], L0[12:], len(L0)))
    ok &= check('cells changed 8 (kernel, profile, status of row 1; kernel of row 2; kernel, status of row 3; kernel, profile of row 4)',
                r['counts']['CELLS CHANGED'], 8)
    ok &= check('no blank cell', cells_ok(L1), True)
    return ok, L1, c


def case2():
    OUT.append('### (2) A DECLARATION VANISHED: Mod.gone is not declared at v0.2.0')
    rows = ['| a claim | SIDE-x v0.1.0 = `aaaaaaa` | `Mod.gone` | `{propext}` | **DERIVES** — prose. |']
    c = ctx({'SIDE-x': ('v0.2.0', C_NEW)}, {'SIDE-x': dict(prints={'X.Mod.thm': ['propext']})}, set(), {'SIDE-x': {'X.Mod.gone': 'DERIVES'}})
    L1, r = G.regen_lines(doc(rows), ANCHOR, c, 'planted-2')
    ok = check('profile reads ABSENT AT v0.2.0; pin and status kept', L1[8], '| a claim | SIDE-x v0.1.0 = `aaaaaaa` | `Mod.gone` | ABSENT AT v0.2.0 | **DERIVES** — prose. |')
    ok &= check('ABSENT counted 1, by kernel', (r['counts']['ABSENT'], r['by_kernel']['SIDE-x']['ABSENT']), (1, 1))
    ok &= check('no blank cell', cells_ok(L1), True)
    return ok


def case3():
    OUT.append('### (3) A KERNEL WITH NO PRINT BANK: SIDE-z at v0.2.0, the grade bank says DERIVES')
    rows = ['| a claim | SIDE-z v0.1.0 | `Z.thm` | `{propext, Quot.sound}` | **DERIVES** — prose. |',
            '| none | (none) | — | — | Manuscript-resident |']
    c = ctx({'SIDE-z': ('v0.2.0', C_NEW)}, {'SIDE-z': None}, {('SIDE-z', 'bbbbbbb', 'thm')}, {'SIDE-z': {'SIDEZ.Z.thm': 'DERIVES'}})
    L1, r = G.regen_lines(doc(rows), ANCHOR, c, 'planted-3')
    ok = check('profile NO PRINT BANK AT v0.2.0; grade DERIVES UNREFRESHED', L1[8],
               '| a claim | SIDE-z v0.2.0 | `Z.thm` | NO PRINT BANK AT v0.2.0 | **DERIVES UNREFRESHED** — prose. |')
    ok &= check('the kernel-less row untouched', L1[9], rows[1])
    ok &= check('NO PRINT BANK counted 1, by kernel', (r['counts']['NO PRINT BANK'], r['by_kernel']['SIDE-z']['NO PRINT BANK']), (1, 1))
    L2, r2 = G.regen_lines(L1, ANCHOR, c, 'planted-3 again')
    ok &= check('run again: unchanged (the cell words are idempotent)', (L2, r2['counts']['CELLS CHANGED']), (L1, 0))
    return ok


def case4(L1, c1):
    OUT.append('### (4) A TABLE ALREADY AT ITS TAG: the file`s bytes identical, CRLF kept; case (1)`s output run again identical')
    rows = ['| a claim | SIDE-x v0.2.0 = `bbbbbbb` | `Mod.thm` | `{propext}` | **INTERFACES** — prose. |',
            '| deposit | SIDE-x — **DEPOSIT-PIN `v0.1.0` = `aaaaaaa`** (concept DOI `10.5281/zenodo.1`) | `Mod.thm` | `{propext}` | **DERIVES** |',
            '| same-row | same | `Mod.thm` | `{propext}` | **DERIVES** |']
    b = '\r\n'.join(doc(rows)).encode('utf-8') + b'\r\n'
    nb, r = G.regen_bytes(b, ANCHOR, c1, 'planted-4')
    ok = check('bytes identical', nb == b, True)
    ok &= check('the deposit pin and its inheriting row HELD, counted 2', r['counts']['HELD: DEPOSIT PIN'], 2)
    L2, r2 = G.regen_lines(L1, ANCHOR, c1, 'planted-1 again')
    ok &= check('case (1)`s output run again: identical, 0 cells changed', (L2 == L1, r2['counts']['CELLS CHANGED']), (True, 0))
    return ok


def case5():
    OUT.append('### (5) A KERNEL WITH A RUNNER PRINT BANK AT ITS TAG (b682): SIDE-y at v0.3.1, its banks planted in b678`s form -- b999_runner_SIDE-y_after.txt '
               '(the header`s ref built) beside b999_axioms_SIDE-y_after.txt (the raw #print axioms lines); Y.gone absent at the tag, Y.thm printed '
               '[propext], Y.np declared and not printed')
    C_Y = 'c' * 7 + '3' * 33
    with tempfile.TemporaryDirectory(prefix='b682_case5_') as tmp:
        open(os.path.join(tmp, 'b999_runner_SIDE-y_after.txt'), 'w', encoding='utf-8').write(
            'b999 -- COMPONENT 3: THE HOSTED RUNNER FOR SIDE-y, AFTER, READ BY ITS RUN ID\n\n### the dispatch: at main, the ref input %s ; the target `Y`\n'
            '### the ref built (out/ref.txt): %s leanprover/lean4:v4.29.0-rc8\n' % (C_Y, C_Y))
        open(os.path.join(tmp, 'b999_axioms_SIDE-y_after.txt'), 'w', encoding='utf-8').write(
            "'SIDEY.Y.thm' depends on axioms: [propext]\n'SIDEY.Y.other' does not depend on any axioms\n")
        named = bool(G.AX_NAME.match('b999_axioms_SIDE-y_after.txt')) and not G.BANK_NAME.match('b999_runner_SIDE-y_after.txt')
        built, prints = G.parse_bank(os.path.join(tmp, 'b999_axioms_SIDE-y_after.txt'))
    ok = check('the reader takes the axioms bank by its path form, and not the runner bank as a bank of rows', named, True)
    ok &= check('the built commit read from the companion runner bank`s header; the prints from the raw lines', (built, prints),
                (C_Y, {'SIDEY.Y.thm': ['propext'], 'SIDEY.Y.other': []}))
    rows = ['| absent | SIDE-y v0.3.0 | `Y.gone` | NO PRINT BANK AT v0.3.0 | **DERIVES UNREFRESHED** — prose. |',
            '| printed | SIDE-y v0.3.0 | `Y.thm` | NO PRINT BANK AT v0.3.0 | **DERIVES UNREFRESHED** — prose. |',
            '| not printed | SIDE-y v0.3.0 | `Y.np` | NO PRINT BANK AT v0.3.0 | DERIVES |']
    c = ctx({'SIDE-y': ('v0.3.1', C_Y)}, {'SIDE-y': dict(prints=prints)}, {('SIDE-y', 'ccccccc', 'thm'), ('SIDE-y', 'ccccccc', 'np')},
            {'SIDE-y': {'SIDEY.Y.thm': 'DERIVES', 'SIDEY.Y.np': 'DERIVES'}})
    L1, r = G.regen_lines(doc(rows), ANCHOR, c, 'planted-5')
    ok &= check('a declaration absent at the tag and from the bank reads ABSENT, not NO PRINT BANK', L1[8],
                '| absent | SIDE-y v0.3.0 | `Y.gone` | ABSENT AT v0.3.1 | **DERIVES UNREFRESHED** — prose. |')
    ok &= check('a printed declaration reads the bank`s verdict: the kernel to the tag, the profile the bank`s, UNREFRESHED dropped', L1[9],
                '| printed | SIDE-y v0.3.1 | `Y.thm` | `{propext}` | **DERIVES** — prose. |')
    ok &= check('a declaration declared and not printed reads NOT PRINTED AT the tag (b672`s word)', L1[10],
                '| not printed | SIDE-y v0.3.1 | `Y.np` | NOT PRINTED AT v0.3.1 | DERIVES |')
    ok &= check('the counts: ABSENT 1, NOT PRINTED 1, NO PRINT BANK 0', (r['counts']['ABSENT'], r['counts']['NOT PRINTED'], r['counts']['NO PRINT BANK']),
                (1, 1, 0))
    ok &= check('no blank cell', cells_ok(L1), True)
    return ok


def main():
    OUT.append('b672 -- THE CORRESPONDENCE GENERATOR`S PLANTED CASES, (R282)(4): tools/test_correspondence_gen.py over tools/correspondence_gen.py '
               '(the fifth case b682`s, under (R292)(3))')
    OUT.append('')
    OUT.append('### rows are planted cases, each check with its expected and its read value')
    ok1, L1, c1 = case1()
    res = [ok1, case2(), case3(), case4(L1, c1), case5()]
    n = sum(1 for x in res if x)
    OUT.append('')
    OUT.append('### ### **PLANTED CASES %d ; AS WANTED %d ; %s**' % (len(res), n, 'PASS' if n == len(res) else 'FAIL'))
    print('\n'.join(OUT))
    if 'bank' in sys.argv[1:]:
        rest = sys.argv[sys.argv.index('bank') + 1:]
        name = rest[0] if rest else 'b672_gen_test.txt'
        p = os.path.join(G.D, name)
        open(p + '.tmp', 'wb').write(('\n'.join(OUT) + '\n').encode('utf-8'))
        os.replace(p + '.tmp', p)
    sys.exit(0 if n == len(res) else 1)


if __name__ == '__main__':
    main()
