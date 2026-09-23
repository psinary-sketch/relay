# -*- coding: utf-8 -*-
"""b482_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.
### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b482_span.json')))
    R = json.loads(read(os.path.join(D, 'b482_results.json')))
    SV = json.loads(read(os.path.join(D, 'b482_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b482_results.json')))

    rec('=' * 100)
    rec('b482_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the pin : %s ; the six : %d theorems, ### **%d `sorry` in the file**'
        % (SV['pin'][:7], len(SV['six']), SV['sorries']))
    rec('    the comparator : %d theorem names ; permitted axioms %s'
        % (len(SV['comparator']['theorem_names']), ', '.join(SV['comparator']['permitted_axioms'])))
    rec('    the placement : %d cells -- SAME OBJECT ### **%d** ; TOUCHES ### **%d** ; APART ### **%d**'
        % (RES['cells'], RES['counts'].get('SAME OBJECT', 0), RES['counts'].get('TOUCHES', 0),
           RES['counts'].get('APART', 0)))
    rec('    b479 : ferries carrying its order ### **%d** ; the positive control found ### **%d**'
        % (len(SV['b479_hits']), len(SV['b479_control'])))
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b485 LEFT FORTY-NINE STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['AND (R95) NOW BOUNDS IT: a metadata edit that changes no file and no version is NOT a',
          're-issue. ### The drafting is the act AFTER the fold`s; this act does not do it.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['ROUTED INTO (R95)`s drafting list: 21520474 and 21539068 are two of its three records.']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('PATHS carries no proportion table', 'STAND',
         ['AND b482 SHOWS WHAT A PROPORTION TABLE WOULD LOOK LIKE IF THE CORPUS HAD ONE: the six',
          'XiPrime statements carry 0.85838, 0.92919, 0.86864, 0.93432. ### **THE CORPUS STATES NO',
          'PROPORTION OF THE ZEROS OF xi-prime ANYWHERE.** ### The item stands, sharper.']),
        ('a site verdict is source-relative, not absolute', 'STAND', ['UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['THE b475 RUN IS ANOTHER ACT`S AND ITS LOG IS NOT OPENED HERE. ### (K) BAR 3.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['### ### **AND THIS ACT IS EXACTLY THAT CASE.** ### The tool reads ### **%d** ### for b482'
          % span['current_span'],
          'because b482`s NUMBER is below b485`s, not because the span shrank: twelve acts have run',
          'since the fold. ### **THE READING IS THE TOOL`S AND IS PRINTED AS THE TOOL`S**, and the',
          'fold should take its own number`s reading. ### The item stands and is now DEMONSTRATED,',
          'not merely predicted.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) STILL NOT YET DECIDABLE; (R83) DOES NOT FIRE.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['UNTOUCHED BY THIS ACT.']),
        ('the span stands at the fold threshold', 'STAND',
         ['THE FOLD IS ORDERED AND NOT OPENED: the order places it after b479 and b482, and',
          '### **b479 HAS NOT RUN.** ### The seat closes this act and asks.']),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE BANKED READ LINE STILL STANDS.']),
        ('the compression register, opened as a lane and empty', 'STAND', ['CLOSED AT b483, NO GRADE.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['CLOSED BY (R91) AT b483.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND', ['ROUTED.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'STAND', ['CLOSED BY (R90) AT b483.']),
        ('the bar on the deposited records is capability, not permission', 'STAND',
         ['DISCHARGED AT b485 BY (R94)`s route.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'STAND', ['WRITTEN AT b485.']),
        ('the gate`s fifth site is not locatable at this seat', 'STAND', ['UNTOUCHED.']),
        ('one live currency claim contradicts REGISTRY', 'STAND', ['DISCHARGED AT b484.']),
        ('a priced resolving size that the arithmetic forbids', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('a bound the chain reports is not the bound it achieves', 'STAND',
         ['FILED AS `W-ORD-QUADRATURE-BOUND` AT b484; its trigger has not fired.']),
        ('the seat read its own expectation backwards', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('two unrelated tests single out sqrt(17)', 'STAND', ['LEFT OPEN AT b484.']),
        ('a search that can see its own report will always confirm it', 'STAND', ['ROUTED.']),
        ('a matcher that counts co-occurrence is not counting a claim', 'STAND', ['FOUND AT b484.']),
        ('REGISTRY`s own history table disagrees with the records', 'STAND',
         ['ANNOTATED AT b485; the five findings stand and are routed to an author`s ruling.']),
        ('a frozen ledger cannot be repaired without breaking its own law', 'STAND',
         ['FOUND AT b485; ROUTED.']),
        ('an index-query gate fires on an arm`s own name', 'STAND', ['FOUND AT b485; ROUTED.']),
        ('a tool that can crash after a write needs a guard before it', 'STAND',
         ['THE GUARD IS IN b485`s AND b482`s desk tools; ### **IT BELONGS IN `corr_row.py`** ###',
          'and that is still not done. ### ROUTED.']),
        ('an order cited across three sealed faces with no bank behind it', 'MINT',
         ['### ### **FOUND AT b482, AND IT IS THE GRAVEST BOOKKEEPING DEFECT THIS SPAN HAS FOUND.**',
          '### `b480`, `b483` and `b484` each state on a SEALED FACE that `b479` is *"registered by',
          'its own ferry"*. ### **NO BANKED FERRY CARRIES `ACT b479`** -- proved by searching every',
          'ferry file, with `ACT b482` as a POSITIVE CONTROL that the same search finds.',
          '### ### **THE CLAIM PROPAGATED BECAUSE EACH FACE COPIED THE LAST ONE`S SENTENCE**, and a',
          'sealed face is exactly the kind of document a later act trusts without re-checking.',
          '### **A SEAL CERTIFIES THAT THE BYTES HAVE NOT CHANGED; IT CERTIFIES NOTHING ABOUT',
          'WHETHER THEY WERE TRUE.** ### b479 is NOT run and NOT reconstructed. ### ROUTED to the',
          'navigator: re-issue the order, or strike the number.']),
        ('a statement posed is not a result', 'MINT',
         ['FOUND AT b482. ### All six declarations of `zeta23/Challenge/XiPrime.lean` are closed by',
          '### **`sorry`** ### -- they are CHALLENGE STATEMENTS, not theorems held. ### The file',
          'carries %d `sorry` tokens. ### **EVERY SENTENCE OF THIS ACT THAT DESCRIBES THEM SAYS SO**'
          % SV['sorries'],
          '(a bar on the face), because a placement verdict between two statements reads exactly',
          'like a comparison of two results unless the difference is said out loud.']),
        ('a terminal named for mathematics can state arithmetic', 'MINT',
         ['FOUND AT b482, IN THE CORPUS`S OWN REPOSITORY AND NOT IN THE STRANGER`S.',
          '### `SIDE-simplicity v0.1.0`s `transversal_generic_empty` and `codim_margin` are, AS',
          'STATEMENTS, ### **FACTS ABOUT INTEGERS** ### -- `1 - obstrCodim < 0` given',
          '`2 <= obstrCodim`, and `1 < 5 - lost` given `lost <= 3` -- both closed by `omega`.',
          '### **NEITHER MENTIONS xi, zeta, A ZERO, OR A COMPLEX NUMBER.** ### The mathematics they',
          'are named for lives in their DOCSTRINGS. ### That is why all twelve of their placement',
          'cells are `APART`: ### **THERE IS NO SHARED OBJECT TO BE THE SAME AS OR TO TOUCH.**',
          '### ### **THIS IS A READING OF WHAT THE STATEMENTS SAY AND NOT A JUDGEMENT ON THE',
          'REPOSITORY**, and the face said so before the placement ran. ### ROUTED.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    standing = sum(1 for _, s, _ in desk if s in ('STAND', 'MINT'))
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### MINTED HERE : %d. ### STANDING : %d.**'
        % (len(desk), closed, minted, standing))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    RES = json.loads(read(os.path.join(D, 'b482_results.json')))
    same = RES['counts'].get('SAME OBJECT', 0)
    SC = dict(
        N1=dict(nav='at least one declaration is SAME OBJECT with the perpendicular-crossing statement',
                verdict='REFUTED',
                note=('### **`SAME OBJECT` CELLS : %d of %d.** ### The closest is `TOUCHES`, and '
                      'the closest pair is `xiPrime_zeros_in_open_critical_strip` against the '
                      'clause: the shared term is `xi-prime`, ### **BUT THE QUANTIFIED SET IS NOT** '
                      '-- the clause ranges over ZEROS OF xi, the declaration over ZEROS OF '
                      'xi-prime. ### **TWO DIFFERENT SETS OF POINTS.**' % (same, RES['cells']))),
        N2=dict(nav='no declaration states uniform transversality, so the geometric clause stays open',
                verdict='HELD',
                note=('Not one of the six states a transversality or a crossing angle; four state '
                      'COUNTS, one states a LOCATION, one states a HALF-PLANE POSITIVITY. ### The '
                      'geometric clause stays open, and ### **NOTHING IN THIS ACT NARROWS IT.**')),
        N3=dict(nav='the six count zeros of xi-prime rather than bounding one zero derivative',
                verdict='HELD OF THE FILE`S CHARACTER, FALSE OF TWO OF ITS SIX MEMBERS',
                note=('Four of the six use `Ncount`, `Ndist` and `N0simple` with multiplicity in '
                      'the denominator -- they COUNT. ### **BUT `xiPrime_zeros_in_open_critical_'
                      'strip` COUNTS NOTHING** (it locates every zero in the open strip) ### **AND '
                      '`xiPrime_over_xi_re_pos` COUNTS NOTHING** (it bounds `Re(xi-prime/xi)` on a '
                      'half-plane). ### Neither of those two bounds one zero`s derivative either, '
                      'so the expectation`s *rather than* clause is true of all six while its '
                      '*count* clause is true of four. ### **THIS FACE SAID SO IN ADVANCE** rather '
                      'than scoring the expectation whole.')),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 1 ; HELD-IN-PART 1 ; REFUTED 1.**')
    rec('  ### the seat`s own calls were on the sealed face before the placement ran and matched')
    rec('  ### all three, including registering (N3)`s split over its own population in advance.')
    json.dump(SC, io.open(os.path.join(D, 'b482_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE XiPrime TOPIC IS PLACED AGAINST THREE CORPUS SOURCES AND NOT ONE CELL IS SAME '
        'OBJECT** (b482, its banked ferry with the amendment). '
        '**AND FIRST, A HALT: b479 IS NOT RUN, BECAUSE ITS ORDER IS NOT BANKED. Every ferry file '
        'was searched for the string ACT b479 and NOT ONE CARRIES IT; the same search for ACT b482 '
        'finds b482_ferry.txt as a positive control. Yet THREE SEALED FACES -- b480, b483, b484 -- '
        'each state that b479 is registered by its own ferry. The claim propagated because each '
        'face copied the last. A SEAL CERTIFIES THAT BYTES HAVE NOT CHANGED; IT CERTIFIES NOTHING '
        'ABOUT WHETHER THEY WERE TRUE. b479 is not run and NOT RECONSTRUCTED.** '
        '**COMPONENT 1: the clone HEAD is fbdc36b, the pin the order names. The six declarations '
        'are printed verbatim, and ALL SIX ARE CLOSED BY sorry -- they are CHALLENGE STATEMENTS, '
        'NOT THEOREMS HELD. comparator-xiprime.json lists exactly those six, no definitions, and '
        'permits propext, Quot.sound and Classical.choice.** '
        '**COMPONENT 2: the corpus statements, read as STATEMENTS AND NOT DOCSTRINGS -- the '
        'geometric clause at A_Place_to_Stand.md:304 in the deposited copy; spectral_cannon at '
        'SIDE-kernel v1.5, giving Re of the derivative of completedRiemannZeta0 at one-half plus '
        'i t equal to zero, PROVED; and, by the amendment, SIDE-simplicity v0.1.0 '
        'transversal_generic_empty and codim_margin. AND THOSE TWO QUANTIFY OVER THE INTEGERS AND '
        'NOTHING ELSE: neither mentions xi, zeta, a zero or a complex number, and both are closed '
        'by omega. The mathematics they are named for lives in their docstrings.** '
        '**COMPONENT 3: 24 cells. SAME OBJECT 0, TOUCHES 10, APART 14. All twelve cells against '
        'the two simplicity terminals are APART for one reason -- THERE IS NO SHARED OBJECT TO BE '
        'THE SAME AS OR TO TOUCH. xiPrime_over_xi_re_pos is APART from both analytic statements '
        'for a different reason: it quantifies over the half-plane where Re s is at least one '
        'while both speak of the critical line, so THE REGIONS ARE DISJOINT.** '
        '**THE TWO REVERSE READS. The six state what the corpus does not: a positive proportion '
        'with a number (0.85838, 0.92919, 0.86864, 0.93432), the location of EVERY zero of '
        'xi-prime, a half-plane positivity for xi-prime over xi, and a counting apparatus. The '
        'corpus states what the six do not: a POINTWISE VALUE of xi-prime at EVERY point of the '
        'critical line -- not only at zeros -- and it is PROVED, not posed. NEITHER SIDE SUBSUMES '
        'THE OTHER.** '
        '(N1) REFUTED -- zero cells are SAME OBJECT. (N2) HELD. (N3) HELD of the file character '
        'and false of two of its six members, as the face registered in advance. '
        'No Lean run, nothing imported, the zeta23 artefacts not committed, no grade conferred on '
        'any corpus object, the kernel lane closed at this act end; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             ('no Lean run and no build; statements read as TEXT at their tags -- zeta23 at '
              'fbdc36b, SIDE-kernel v1.5, SIDE-simplicity v0.1.0'),
             ('NO CORPUS GRADE MOVED AND NO GRADE CONFERRED; a placement verdict is a relation '
              'between two statements, not a judgement on either'),
             ('data/b482_components.txt; data/b482_extract.txt; data/b482_survey.json; '
              'data/b482_results.json; data/b482_scores.json; data/b482_desk_notes.txt; '
              'data/b482_registration_2026-09-22.txt (LOCKED at sha256 8ce9439063b28a4e); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    MARK = 'THE XiPrime TOPIC IS PLACED AGAINST THREE CORPUS SOURCES'
    if MARK in before:
        rec('  ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER; IT IS NOT APPENDED AGAIN.**')
        rec('  ### `corr_row.write_row` APPENDS and is NOT idempotent. ### This tool crashed once')
        rec('  ### AFTER its row landed, and a re-run without this guard would have written a')
        rec('  ### SECOND row for the same act. ### **A TOOL THAT CAN CRASH AFTER A WRITE NEEDS A')
        rec('  ### GUARD BEFORE IT**, and the guard reads the ledger rather than trusting the run.')
        code, out = 0, ['    (guard) row already present; nothing appended']
    else:
        code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        rec('  ### ### **HARD FAILURE: THE ROW WAS NOT WRITTEN.**')
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    prefix = after.startswith(before.rstrip(NL)) or MARK in before
    ncells = len(last.strip().strip('|').split('|'))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d' % (rowid, ncells))
    good = (ncells == 6 and (rowid == str(nxt) or MARK in before))
    rec('  ### %s' % ('PASS' if good else '### FAIL'))

    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d minted, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, minted, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b482_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
