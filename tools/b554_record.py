# -*- coding: utf-8 -*-
"""b554_record.py -- THE CASCADE, ACT EIGHT: SIMPLICITY_OF_RIEMANN_ZEROS TIERED; bd2ae1a RULED AND FILED; THE TWO CONFLICTS
SETTLED; READING ONE CLOSED; THE SIGN PATTERN ON THE FINE GRID; THE DETECTION REGION RE-PRICED; THE PAIRING HAZARD ENTERED;
ANOMALY 1 ROUTED: THE RECORD, UNDER (R164).
### `python tools/b554_record.py reads | bd2 | erratum | table_before | synonym_test | trail_sup_test | sup_line | readme |
### reading_one | sign_pattern | prices | simp_rows | simp_tiers | simp_block | simp_reading | stems | findings | components |
### desk | trail`
### The tool edits, the probes` launches, the worktree commands, the commits, pushes and branch commands are the seat`s.
### This file deletes nothing.
"""
import io, json, math, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP, GS, LV, EF, TRIAL, CORR = P.PP, P.GS, P.LV, P.EF, P.TRIAL, P.CORR
KER = os.path.join(DD, 'SIDE-kernel')
FIND, OT = P.FIND, P.OT
ERR = os.path.join(PP, 'ERRATA.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
RES = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
CHARTER = os.path.join(PP, 'phase2', 'method', 'THE_H2_PROGRAMME_CHARTER.md')
SIMP = os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md')
README = os.path.join(T, 'corr_row.README.md')
NL = chr(10)
rd, g, cite, append_to, guard_absent, line_of, poss, outside_bt = P.rd, P.g, P.cite, P.append_to, P.guard_absent, P.line_of, P.poss, P.outside_bt
PRIOR_RELAY = 'ed2185c0'   # ### b553`s closing housekeeping -- relay`s tip before this act
PRIOR_PP = 'e1478b6'       # ### b553`s PLACE-papers commit
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def lines_with(path, pat, text=None):
    return [i + 1 for i, l in enumerate((text if text is not None else rd(path)).split(NL)) if re.search(pat, l)]


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')


# ------------------------------------------------------------------------------ THE READS
def reads():
    L = ['b554 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    cite(L, CHARTER, 112, 120, 'THE_H2_PROGRAMME_CHARTER.md:116 -- "the `bd2ae1a` `E`-CHARACTERIZATION sitting"')
    cite(L, PATHS, 420, 420, 'PATHS_TO_THE_CRITICAL_LINE.md:420 -- the hash attributed to SIDE-lv-conservation')
    cite(L, RES, 145, 145, 'THE_RESIDUE_OF_RH.md:145 -- the era table row on bd2ae1a')
    cite(L, CENSUS, 40, 56, 'THE_KEYSTONE_CENSUS.md §1 -- the pin ancestry and the five named failures')
    cite(L, CENSUS, 243, 281, 'THE_KEYSTONE_CENSUS.md -- the v0.2 section')
    last = lines_with(ERR, r'^## E-')[-1]
    cite(L, ERR, last, len(rd(ERR).split(NL)), 'ERRATA.md -- its last entry (format)')
    cite(L, ERR, 348, 352, 'ERRATA.md -- an internal-record entry`s head (format)')
    tt = blob(ROOT, PRIOR_RELAY + ':tools/terminal_table.py')
    ttp = os.path.join(T, 'terminal_table.py')
    gp = lines_with(None, r'^def grade_cells\(', tt)[0]
    sp = lines_with(None, r'^def supersede\(', tt)[0]
    cf = lines_with(None, r"'CONFLICT' if len\(distinct\) > 1", tt)[0]
    cite(L, ttp, gp, gp + 30, 'terminal_table.py AT b553`s CLOSE, BEFORE THE EDITS: the grade parser', text=tt)
    cite(L, ttp, sp - 14, sp + 10, 'terminal_table.py AT b553`s CLOSE: the supersede rule', text=tt)
    cite(L, ttp, cf - 16, cf + 4, 'terminal_table.py AT b553`s CLOSE: the conflict test', text=tt)
    cite(L, OT, 11042, 11042, 'OPEN_TRAILS.md:11042 -- the grade the parser reads onto register5_output_holds')
    cite(L, OT, 11290, 11292, 'OPEN_TRAILS.md:11290 -- the bridge price`s head')
    cite(L, OT, 11151, 11151, 'OPEN_TRAILS.md:11151 -- W-ORD-DETECTION-REGION as priced at b547')
    cite(L, os.path.join(D, 'b553_period_fine.txt'), 1, 40, 'relay data/b553_period_fine.txt -- the two orbit results')
    cite(L, os.path.join(D, 'b553_registration_2026-09-28.txt'), 50, 80, 'relay data/b553_registration -- the derivation, sealed first')
    cite(L, os.path.join(D, 'b548_interference.txt'), 1, 21, 'relay data/b548_interference.txt -- h2, pair, rest at integer widths 30-45')
    L += ['### relay data/b548_sweep_q.jsonl at p = 7 -- the zero side Z, pair, rest and the bound B at integer widths 10-60 (keys: %s)' %
          sorted(json.loads([l for l in rd(os.path.join(D, 'b548_sweep_q.jsonl')).split(NL) if l.strip()][0]).keys()), '']
    pl = blob(EF, '81ae175:SIDEExplicitFormula/PowerLimit.lean')
    for n in ('tie_term_neg', 'rest_term_small', 'dominant_summable', 'zeroSide_eventually_neg'):
        ln = lines_with(None, r'^theorem %s\b' % n, pl)[0]
        cite(L, os.path.join(EF, 'SIDEExplicitFormula', 'PowerLimit.lean'), ln - 1, ln + 4, 'PowerLimit.lean at 81ae175 -- %s' % n, text=pl)
    for f, n in (('PairTerm.lean', 'pairTwo_factored'), ('PairTerm.lean', 'pair_bound'), ('DecayBound.lean', 'window_decay_re'), ('RestBound.lean', 'rest_bound_zeta')):
        src = blob(EF, '81ae175:SIDEExplicitFormula/' + f)
        ln = lines_with(None, r'^theorem %s\b' % n, src)[0]
        cite(L, os.path.join(EF, 'SIDEExplicitFormula', f), ln - 1, ln + 3, '%s at 81ae175 -- %s (compiled; a closed-form route reuses it)' % (f, n), text=src)
    sl = rd(SIMP).split(NL)
    cite(L, SIMP, 22, 26, 'SIMPLICITY -- the Abstract')
    cite(L, SIMP, 36, 36, 'SIMPLICITY -- Chapter 1`s title')
    cite(L, SIMP, 69, 84, 'SIMPLICITY -- spectral_cannon`s sentence and the reduction theorem')
    cite(L, SIMP, 429, 457, 'SIMPLICITY -- the Correspondence table and the kernel-audit line')
    cite(L, SIMP, 478, 492, 'SIMPLICITY -- the b397 disclosure and the b454 block')
    L += ['### SIMPLICITY_OF_RIEMANN_ZEROS.md read entire: %d lines, %d bytes (sha256 %s)' % (
        len(sl), len(open(SIMP, 'rb').read()), __import__('hashlib').sha256(open(SIMP, 'rb').read()).hexdigest()[:16])]
    put_txt('b554_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: bd2ae1a
def bd2():
    full = g(PP, 'show', '-s', '--format=%H%n%ci%n%s', 'bd2ae1a').rstrip(NL).split(NL)
    anc = subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', 'bd2ae1a', 'main']).returncode == 0
    ch = rd(CHARTER).split(NL)[115]
    L = ['b554 -- COMPONENT 1: bd2ae1a (READING (1))', '',
         '### git -C PLACE-papers show -s bd2ae1a :',
         '    hash    : %s' % full[0], '    date    : %s' % full[1], '    subject : %s' % full[2][:600],
         '### an ancestor of PLACE-papers main : %s' % anc,
         '### THE_H2_PROGRAMME_CHARTER.md:116 : %s' % ch.strip(),
         '### PATHS_TO_THE_CRITICAL_LINE.md:420 names it : %s' % ('SIDE-lv-conservation `bd2ae1a`' in rd(PATHS).split(NL)[419]),
         '### SIDE-lv-conservation resolves it : %s' % (subprocess.run(['git', '-C', LV, 'cat-file', '-e', 'bd2ae1a^{commit}'], capture_output=True).returncode == 0),
         '### SIDE-lv-conservation v0.11.0 : %s' % g(LV, 'rev-parse', 'v0.11.0^{commit}').strip()]
    out = dict(hash=full[0], date=full[1], subject=full[2], ancestor=anc, charter116=ch.strip(),
               paths420='SIDE-lv-conservation `bd2ae1a`' in rd(PATHS).split(NL)[419], v0110=g(LV, 'rev-parse', 'v0.11.0^{commit}').strip())
    put_json('b554_bd2.json', out)
    put_txt('b554_bd2.txt', L)
    print(NL.join(L))


EH = ('## E-2026-09-27-1 — PATHS_TO_THE_CRITICAL_LINE attributes the pin `bd2ae1a` to SIDE-lv-conservation; the hash is a '
      'PLACE-papers commit, the sitting record of 2026-07-25 (KEYSTONE-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)')
BDL = '*Appended 2026-09-28 by b554, under the author`s ruling `(R164)`(1), to the %s:*'


def erratum():
    guard_absent(ERR, EH)
    b = jl('b554_bd2.json')
    dep = [f for f in subprocess.run(['git', '-C', PP, 'ls-files', 'outputs'], capture_output=True, text=True).stdout.split(NL)
           if re.search(r'PATHS_TO_THE_CRITICAL_LINE|THE_RESIDUE_OF_RH|THE_KEYSTONE_CENSUS', f)]
    assert dep == [], dep
    L = ['', EH, '',
         '**Filed 2026-09-28 (b554), on the author`s ruling `(R164)`(1); found at b553 (relay `data/b553_ancestry_read.txt`). Records affected: '
         '`phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md`:420, whose flag of 2026-08-12 is repeated at `phase1.5/proofs/THE_RESIDUE_OF_RH.md`:145 '
         'and `phase2/method/THE_KEYSTONE_CENSUS.md`:48. ### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY.** None of the three is in '
         '`outputs/`; each is a keystone-class or census document of the corpus.', '',
         '**What the line says.** PATHS :420 reads *"twist ↔ the FE action w↔1/w (SIDE-lv-conservation `bd2ae1a` [UNREPRODUCIBLE-AS-CITED '
         '(2026-08-12). … The hash itself resolves nowhere: tested against all 43 local repositories, and against every branch and all 13 tags '
         'of `SIDE-lv-conservation`. …]"*: the hash attributed to SIDE-lv-conservation, and flagged as resolving nowhere.', '',
         '**What the hash is.** `git -C PLACE-papers show -s bd2ae1a` (relay `data/b554_bd2.txt`): commit `%s`, %s, subject *"%s"* -- '
         'an ancestor of PLACE-papers `main`: %s. `THE_H2_PROGRAMME_CHARTER.md`:116 names it: "the `bd2ae1a` `E`-CHARACTERIZATION sitting". '
         'The search of 2026-08-12 tested the repositories at the root of D: and every branch and tag of SIDE-lv-conservation; PLACE-papers, '
         'under `MY-DOwnloads`, was not among them.' % (b['hash'][:12], b['date'], b['subject'].split(':')[0] + ': …', b['ancestor']), '',
         '**The correction, as ruled.** The referent of `bd2ae1a` is the sitting record: the PLACE-papers commit at which the word-pairing work '
         'was reported. It is not a kernel pin. The kernel pin for the terminals that sitting reported is SIDE-lv-conservation `v0.11.0` = '
         '`%s`. Where PATHS :420 reads "SIDE-lv-conservation `bd2ae1a`", the attribution of record is: PLACE-papers `bd2ae1a` (the sitting '
         'record, 2026-07-25), the terminals at SIDE-lv-conservation `v0.11.0` = `%s`.' % (b['v0110'][:7], b['v0110'][:7]), '',
         '**Scope.** The line at :420 is not edited, and the flag of 2026-08-12 stays visible at its three sites, each of which carries an '
         'appended line pointing here. The flag`s other clauses -- the branch `word-pairing-interface` exists and is sound; no substitute pin '
         'was offered then -- stand as records of their date. No banked number, verdict or grade moves.', '',
         '*Filed by b554 (relay `data/b554_bd2.txt`). No deposited artifact is affected.*', '', '---', '']
    o = append_to(ERR, NL.join(L))
    o['line'] = line_of(ERR, EH)
    lines = {}
    for path, what, ln in ((PATHS, 'line at :420', 420), (RES, 'era table row at :145', 145), (CENSUS, 'pin ancestry of §1, at :48', 48)):
        guard_absent(path, BDL % what)
        s = (BDL % what + ' `bd2ae1a` is a PLACE-papers commit -- the E-CHARACTERIZATION sitting of 2026-07-25, which '
             '`THE_H2_PROGRAMME_CHARTER.md`:116 names -- and not a SIDE-lv-conservation pin; the terminals that sitting reported are at '
             'SIDE-lv-conservation `v0.11.0` = `%s`. The flag of 2026-08-12 above stays as written. Erratum `E-2026-09-27-1` (`ERRATA.md`:%d).'
             % (b['v0110'][:7], o['line']))
        r = append_to(path, NL.join(['', s, '']))
        r['line'] = line_of(path, BDL % what)
        r['cited_line'] = ln
        lines[os.path.basename(path)] = r
    out = dict(erratum=o, lines=lines)
    put_json('b554_erratum.json', out)
    Lp = ['b554 -- COMPONENT 1: THE ERRATUM AND THE THREE LINES, AS APPENDED', '', '### ERRATA.md:%d' % o['line']]
    Lp += ['    ' + l for l in rd(ERR).split(NL)[o['line'] - 1:o['line'] + 16]]
    for f, r in lines.items():
        Lp += ['### %s:%d (naming :%d)' % (f, r['line'], r['cited_line']), '    ' + rd({'PATHS_TO_THE_CRITICAL_LINE.md': PATHS, 'THE_RESIDUE_OF_RH.md': RES,
                                                                                       'THE_KEYSTONE_CENSUS.md': CENSUS}[f]).split(NL)[r['line'] - 1]]
    put_txt('b554_erratum.txt', Lp)
    print(NL.join(Lp))


# ------------------------------------------------------------------------------ COMPONENT 2: THE CONFLICTS
def regen():
    return subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace').returncode


def snapshot():
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    return {'%s|%s' % (r['repo'], r['name']): r['grade'] for r in rows if isinstance(r, dict) and 'name' in r}


def row_of(key):
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = t.get('rows', t) if isinstance(t, dict) else t
    r = [x for x in rows if isinstance(x, dict) and '%s|%s' % (x['repo'], x['name']) == key]
    return r[0] if r else None


R5 = 'SIDE-lv-conservation|R5_output_HilbertPolya_to_RH'
R5H = 'SIDE-explicit-formula|SIDEExplicitFormula.RegisterDepth.register5_output_holds'


def table_before():
    rc = regen()
    s = snapshot()
    put_json('b554_table_before.json', dict(rc=rc, grades=s, conflicts=sorted(k for k, v in s.items() if v == 'CONFLICT'),
                                            relay_head=g(ROOT, 'rev-parse', 'HEAD').strip(), tool_dirty=g(ROOT, 'status', '--porcelain', '--', 'tools/terminal_table.py').strip()))
    print('  before: rc %d ; rows %d ; CONFLICT %d ; tool dirty [%s]' % (rc, len(s), sum(1 for v in s.values() if v == 'CONFLICT'),
                                                                      g(ROOT, 'status', '--porcelain', '--', 'tools/terminal_table.py').strip()))


def test_against(before_file, out_name, title):
    before = jl(before_file)['grades']
    rc = regen()
    after = snapshot()
    changed = sorted(k for k in after if after[k] != before.get(k))
    gone = sorted(k for k in before if k not in after)
    cb = sorted(k for k, v in before.items() if v == 'CONFLICT')
    ca = sorted(k for k, v in after.items() if v == 'CONFLICT')
    rows = {k: row_of(k) for k in (R5, R5H)}
    out = dict(rc=rc, rows=len(after), changed={k: [before.get(k), after[k]] for k in changed}, gone=gone, conflicts_before=cb, conflicts_after=ca,
               watched={k: (dict(grade=r['grade'], cells=[(c['grade'], c['ledger'], c['line'], c['act']) for c in r['grade_cells']]) if r else None)
                        for k, r in rows.items()})
    put_json(out_name + '.json', out)
    L = ['b554 -- %s' % title, '', '### regenerated: exit %d ; rows %d (before %d) ; rows gone %s' % (rc, len(after), len(before), gone or 'NONE'),
         '### CONFLICT before (%d):' % len(cb)] + ['    ' + k for k in cb] + ['### CONFLICT after (%d):' % len(ca)] + ['    ' + k for k in ca] + [
         '### terminals whose grade changed: %s' % ({k: '%s -> %s' % tuple(v) for k, v in out['changed'].items()} or 'NONE')]
    for k, w in out['watched'].items():
        L.append('### %s : %s' % (k, w['grade'] if w else 'NO ROW'))
        L += ['      %-26s %-30s :%-6s act %s' % c for c in (w['cells'] if w else [])]
    put_txt(out_name + '.txt', L)
    print(NL.join(L))
    return out


def synonym_test():
    test_against('b554_table_before.json', 'b554_synonym', 'COMPONENT 2 (a): THE SYNONYM MAP, ITS TEST (READING (2))')
    s = snapshot()
    put_json('b554_table_mid.json', dict(grades=s, conflicts=sorted(k for k, v in s.items() if v == 'CONFLICT')))


SUPLINE = ('SUPERSEDES OPEN_TRAILS :11042 for `register5_output_holds`: TRUE-AS-STATED (b538, `register5_output_holds`) -- appended '
           '2026-09-28 by b554 under the author`s ruling `(R164)`(2)(b); the grade at :11042 belongs to the Hilbert–Pólya edge and is left '
           'to it; this line is read by `relay/tools/terminal_table.py` (its trail-line form) and carries no grade of the table`s vocabulary.')


def trail_sup_test():
    test_against('b554_table_mid.json', 'b554_trailsup_noop', 'COMPONENT 2 (b): THE TRAIL-LINE FORM BEFORE ITS LINE EXISTS (the no-op test)')


def sup_line():
    import terminal_table as TT
    guard_absent(OT, SUPLINE[:60])
    assert not TT.GRADE_RE.search(SUPLINE), 'a grade word in the line'
    o = append_to(OT, NL.join(['', SUPLINE, '']))
    o['line'] = line_of(OT, SUPLINE[:60])
    put_json('b554_supline.json', o)
    test_against('b554_table_mid.json', 'b554_trailsup', 'COMPONENT 2 (b): THE TRAIL-LINE SUPERSESSION, ITS TEST (READING (3)); the line at OPEN_TRAILS :%d' % o['line'])


RDM = [('b554 (2026-09-28), under the author`s ruling (R164)(2)(a): a synonym map is applied before the conflict test -- '
        'ENCODES-CONCLUSION -> ENCODES; ENCODES-CONCLUSION-or-SHELL (the compound `ENCODES-CONCLUSION \\ SHELL`) -> ENCODES; '
        'INTERFACES-on-named-premise -> INTERFACES. A terminal whose cells carry one grade string keeps it; cells whose mapped grades agree '
        'read the mapped grade; CONFLICT only where the mapped grades still differ. The map is printed in tools/terminal_table.py`s header.'),
       ('b554 (2026-09-28), under the author`s ruling (R164)(2)(b): a ledger line carrying "SUPERSEDES OPEN_TRAILS :N for <terminal>:" '
        'removes, for that terminal alone, the grade cells read from OPEN_TRAILS.md`s line N (the rule `supersede_trail`); the line itself '
        'carries no grade word of the table`s vocabulary.')]


def readme():
    t = rd(README)
    before = open(README, 'rb').read()
    for r in RDM:
        if poss(r) in t:
            sys.exit('### ALREADY PRESENT')
    open(README, 'ab').write((NL.join(poss(r) for r in RDM) + NL).encode('utf-8'))
    after = open(README, 'rb').read()
    put_json('b554_readme.json', dict(prefix=after.startswith(before), lines=len([l for l in rd(README).split(NL) if l.strip()]), text=[poss(r) for r in RDM]))
    print(rd(README))


# ------------------------------------------------------------------------------ COMPONENT 3: READING ONE CLOSED
R1H = '*Appended at b554 (2026-09-28) to b548`s entry (`FINDINGS.md`:5613), under `(R164)`(3) -- READING ONE CLOSED, graded READING:*'


def reading_one():
    guard_absent(FIND, R1H)
    pf = rd(os.path.join(D, 'b553_period_fine.txt'))
    reg = rd(os.path.join(D, 'b553_registration_2026-09-28.txt'))
    lc = lines_with(None, r'^### the crest orbit', pf)[0]
    lm = lines_with(None, r'mean spacing [0-9.]+ ; ratio to 4π/\(7x\)', pf)[0]
    lpr = lines_with(None, r'^### the full periods|full periods:', pf)[0]
    lp = lines_with(None, r'^### the pair orbit', pf)[0]
    ld = lines_with(None, r'THE DERIVATION, FROM THAT FORMULA ALONE', reg)[0]
    lb = lines_with(None, r'\(b\) FOR THE PAIR ORBIT', reg)[0]
    assert '5613' in str(lines_with(FIND, r'^## The bench at Q0|b548')) or True
    fh548 = [i for i in lines_with(FIND, r'^## ') if i <= 5613][-1]
    pj = jl('b553_period_fine.json')
    c, pr = pj['res']['crest'], pj['res']['pair']
    s = (R1H + ' b553`s derivation from the ladder`s printed transform (relay `data/b553_registration_2026-09-28.txt`:%d-%d, sealed before '
         'any evaluation), confirmed on the fine grid to 1 %% (relay `data/b553_period_fine.txt`), settles what b548 could not. At Q0, order 7: '
         'the pair at 16.290216 contributes a negative, monotone term across 30–60, no sign change and no oscillating dominant part '
         '(`data/b553_period_fine.txt`:%d -- min %.1f, max %.1f); the zero at 29.551761 contributes a non-oscillating part plus an oscillation '
         'whose sign changes alternate short and long, mean spacing %.5f in ln a against 4π/(7x) = %.5f, not π/γ = %.5f (:%d, :%d; its full '
         'periods within 1 %% of 8π/(7x), :%d). The positive window at 36–38 is that oscillation`s crest against the pair`s monotone term. '
         'The π/γ model was the navigator`s: the plateau piece alone, the ramp factor left out. Nothing about ζ’s zeros is claimed.'
         % (ld, lb + 3, lp, pr['vmin'], pr['vmax'], c['mean'], c['pred_mean'], math.pi / c['gamma'], lc, lm, lpr))
    o = append_to(FIND, NL.join(['', s, '']))
    o.update(line=line_of(FIND, R1H), b548_heading_line=fh548, cites=dict(derivation=[ld, lb + 3], pair=lp, crest=lc, mean=lm, periods=lpr))
    put_json('b554_reading_one.json', o)
    print(poss(s)); print(o)


# ------------------------------------------------------------------------------ COMPONENT 4: READING EIGHT
def off_terms(a):
    import b521_tail as B21
    import b514_window as B14
    import b511_families as F
    W = B21.PWindow(a, 'q', 7)
    return [((float(b), float(gg)), float(sum(W.khat(B14.gamma_of(r)).real for r in B14.images(b, gg)))) for b, gg in F.OFFQ]


def sign_pattern():
    import b511_families as F
    sweep = {int(r['a']): r for r in (json.loads(l) for l in rd(os.path.join(D, 'b548_sweep_q.jsonl')).split(NL) if l.strip()) if r['p'] == 7}
    inter = {int(r['a']): r for r in (json.loads(l) for l in rd(os.path.join(D, 'b548_interference.jsonl')).split(NL) if l.strip())}
    A = list(range(30, 61))
    assert all(a in sweep for a in A)
    X = [math.log(a) for a in A]
    OFF = {a: off_terms(float(a)) for a in A}
    ON = {a: sweep[a]['Z'] - sum(t for _, t in OFF[a]) for a in A}
    B = {a: sweep[a]['B'] for a in A}
    PAIRK = (0.9532604747946607, 16.290215720390393)
    CREST = (0.7979971571786801, 29.551761098629115)
    ctrl_on = {a: ON[a] - sum(t[2] for t in inter[a]['terms'] if t[0] == 'on') for a in A if a in inter}
    ctrl_off = {}
    for a in A:
        if a in inter:
            bk = {round(t[1], 6): t[2] for t in inter[a]['terms'] if t[0] == 'off'}
            ctrl_off[a] = max(abs(t - bk[round(k[1], 6)]) for k, t in OFF[a] if k != PAIRK)
    ctrl_pair = {a: dict(OFF[a])[PAIRK] - sweep[a]['pair'] for a in A}
    # ### the floor: max(B) of the two nodes + (h^2/8) * M, M the larger |2 f[.,.,.]| of the two nearest triples inside 30-60
    def dd2(i):
        x0, x1, x2 = X[i - 1], X[i], X[i + 1]
        f0, f1, f2 = ON[A[i - 1]], ON[A[i]], ON[A[i + 1]]
        return 2.0 * ((f2 - f1) / (x2 - x1) - (f1 - f0) / (x1 - x0)) / (x2 - x0)
    FL = []
    for i in range(len(A) - 1):
        tri = [j for j in (i, i + 1) if 1 <= j <= len(A) - 2]
        M = max(abs(dd2(j)) for j in tri)
        h = X[i + 1] - X[i]
        FL.append(dict(a0=A[i], a1=A[i + 1], h=h, M=M, interp=h * h / 8.0 * M, bnode=max(B[A[i]], B[A[i + 1]]), floor=max(B[A[i]], B[A[i + 1]]) + h * h / 8.0 * M))

    def seg_of(x):
        for i in range(len(A) - 1):
            if X[i] - 1e-15 <= x <= X[i + 1] + 1e-15:
                return i
        raise ValueError(x)

    def on_at(x):
        i = seg_of(x)
        w = (x - X[i]) / (X[i + 1] - X[i])
        return (1 - w) * ON[A[i]] + w * ON[A[i + 1]]

    def parts(x):
        o = off_terms(math.exp(x))
        return dict(off=sum(t for _, t in o), pair=dict(o)[PAIRK], crest=dict(o)[CREST], on=on_at(x), floor=FL[seg_of(x)]['floor'])

    def Q(x):
        p = parts(x)
        return p['off'] + p['on'], p['floor']
    lo, hi = X[0], X[-1]
    n = int(math.floor((hi - lo) / 0.005 + 1e-12))
    grid = [lo + 0.005 * i for i in range(n + 1)]
    if grid[-1] < hi - 1e-12:
        grid.append(hi)
    for x in X:     # ### the nodes themselves, so the floor`s segment ends are on the grid
        if not any(abs(x - y) < 1e-12 for y in grid):
            grid.append(x)
    grid = sorted(grid)
    vals = [Q(x) for x in grid]
    state = lambda q, f: 'POS' if q > f else ('NEG' if q < -f else 'UND')

    def bis(x0, x1, fn):
        f0 = fn(x0)
        for _ in range(60):
            m = 0.5 * (x0 + x1)
            fm = fn(m)
            if (fm > 0) == (f0 > 0):
                x0, f0 = m, fm
            else:
                x1 = m
            if x1 - x0 < 1e-10:
                break
        return 0.5 * (x0 + x1)
    st = [state(q, f) for q, f in vals]
    runs, start = [], grid[0]
    for i in range(1, len(grid)):
        if st[i] != st[i - 1]:
            a0, a1 = grid[i - 1], grid[i]
            if 'POS' in (st[i - 1], st[i]):
                xb = bis(a0, a1, lambda x: Q(x)[0] - Q(x)[1])
            else:
                xb = bis(a0, a1, lambda x: Q(x)[0] + Q(x)[1])
            runs.append((st[i - 1], start, xb))
            start = xb
    runs.append((st[-1], start, grid[-1]))
    pos = [(x0, x1) for s_, x0, x1 in runs if s_ == 'POS']
    und = [(x0, x1) for s_, x0, x1 in runs if s_ == 'UND']
    l36, l38 = math.log(36.0), math.log(38.0)
    contains = [(x0, x1) for x0, x1 in pos if x0 <= l36 and x1 >= l38]
    h81 = len(pos) == 1
    h82 = len(contains) >= 1 and (len(pos) == 1)
    ref1 = len(pos) >= 2
    ref2 = not any(x0 <= l36 and x1 >= l38 for x0, x1 in pos)
    # ### the crests of the 29.55 oscillation at a >= 38
    cg = [x for x in grid if x >= math.log(38.0) - 1e-12]
    cv = [dict(off_terms(math.exp(x)))[CREST] for x in cg]
    crests = []
    for i in range(1, len(cg) - 1):
        if cv[i] >= cv[i - 1] and cv[i] >= cv[i + 1]:
            a0, a1 = cg[i - 1], cg[i + 1]
            gr = (math.sqrt(5) - 1) / 2
            f = lambda x: dict(off_terms(math.exp(x)))[CREST]
            c0, c1 = a1 - gr * (a1 - a0), a0 + gr * (a1 - a0)
            for _ in range(60):
                if f(c0) > f(c1):
                    a1 = c1
                else:
                    a0 = c0
                c0, c1 = a1 - gr * (a1 - a0), a0 + gr * (a1 - a0)
                if a1 - a0 < 1e-9:
                    break
            xm = 0.5 * (a0 + a1)
            p = parts(xm)
            crests.append(dict(x=xm, a=math.exp(xm), crest=p['crest'], pair=p['pair'], others=p['off'] - p['crest'] - p['pair'], on=p['on'], Q=p['off'] + p['on'], floor=p['floor']))
    L = ['b554 -- COMPONENT 4: READING EIGHT -- THE SIGN PATTERN AT Q0, ORDER 7, ON THE FINE GRID (H8 of (R164)(4)); every line READING', '',
         '### Q(x) = OFF(x) + ON(x), x = ln a. OFF exact: the 17 off-line orbits of the Q0 bank (b511_families.OFFQ), each by the ladder`s code '
         '(b521_tail.PWindow(a, \'q\', 7), b514_window.images / gamma_of, IMPORTED). ON = Z - OFF at the integer widths 30-60, Z from '
         'data/b548_sweep_q.jsonl (p = 7), interpolated linearly in ln a.',
         '### the grid: ln 30 to ln 60 at step 0.005 with both ends and the 31 nodes: %d points; boundaries refined by bisection to 1e-10.' % len(grid), '',
         '### THE CONTROLS',
         '    ON(a) - (the sum of b548`s banked on-line terms), a = 30-45 : largest |difference| %.3e' % max(abs(v) for v in ctrl_on.values()),
         '    each fresh non-pair orbit term - its banked term, a = 30-45  : largest |difference| %.3e' % max(ctrl_off.values()),
         '    the fresh pair term - b548`s banked pair column, a = 30-60   : largest |difference| %.3e' % max(abs(v) for v in ctrl_pair.values()), '',
         '### THE FLOOR, PER INTERVAL: floor = max(B(a_i), B(a_i+1)) + (h²/8)·M, M = max |2·ON[three nodes]| over the nearest triples inside 30-60',
         '    a_i  a_i+1  h          M (2nd div. diff.)   h²M/8        max B        floor']
    L += ['    %-4d %-5d  %.6f   %.6e        %.4e   %.3e    %.4e' % (f['a0'], f['a1'], f['h'], f['M'], f['interp'], f['bnode'], f['floor']) for f in FL]
    L += ['', '### THE NODES: a, Z (banked), OFF (fresh), ON = Z - OFF, the pair, the 29.55 orbit, B (banked)']
    L += ['    %-3d  Z %+.6e  OFF %+.6e  ON %+.6e  pair %+.6e  29.55 %+.6e  B %.2e' % (a, sweep[a]['Z'], sum(t for _, t in OFF[a]), ON[a],
                                                                                    dict(OFF[a])[PAIRK], dict(OFF[a])[CREST], B[a]) for a in A]
    L += ['', '### THE SIGN PATTERN OVER 30-60 (POS: Q > floor ; NEG: Q < -floor ; UND: |Q| <= floor):']
    L += ['    %-3s  ln a %.10f - %.10f   a %.6f - %.6f' % (s_, x0, x1, math.exp(x0), math.exp(x1)) for s_, x0, x1 in runs]
    L += ['### POSITIVE INTERVALS ABOVE THE FLOOR: %d' % len(pos)] + ['    ln a [%.10f, %.10f]   a [%.6f, %.6f]' % (x0, x1, math.exp(x0), math.exp(x1)) for x0, x1 in pos]
    L += ['### UNDECIDED INTERVALS (|Q| <= floor): %d' % len(und)] + ['    ln a [%.10f, %.10f]   a [%.6f, %.6f]' % (x0, x1, math.exp(x0), math.exp(x1)) for x0, x1 in und]
    L += ['', '### THE 29.551761 CRESTS AT a >= 38, with the pair there (golden section to 1e-9 in ln a):']
    L += ['    a %.6f (ln %.8f) : 29.55 term %+.4f ; pair %+.4f ; other off-line orbits %+.4f ; ON %+.4f ; Q %+.4f ; floor %.2e' % (
        c['a'], c['x'], c['crest'], c['pair'], c['others'], c['on'], c['Q'], c['floor']) for c in crests]
    L += ['', '### H8, clause by clause:',
          '  H8.1  exactly one positive interval over 30-60 above the floor          : %s (%d)' % ('HOLDS' if h81 else 'FAILS', len(pos)),
          '  H8.2  that interval contains [ln 36, ln 38]                           : %s' % ('HOLDS' if h82 else ('FAILS -- no single interval' if not h81 else 'FAILS')),
          '  REFUTER 1  a second positive interval above the floor                 : %s' % ('fires' if ref1 else 'does not fire'),
          '  REFUTER 2  no positive interval contains 36-38                        : %s' % ('fires' if ref2 else 'does not fire'),
          '### H8 IS %s' % ('REFUTED' if (ref1 or ref2 or not h81) else 'NOT REFUTED')]
    out = dict(grid_n=len(grid), controls=dict(on=max(abs(v) for v in ctrl_on.values()), off=max(ctrl_off.values()), pair=max(abs(v) for v in ctrl_pair.values())),
               floor=FL, nodes={a: dict(Z=sweep[a]['Z'], OFF=sum(t for _, t in OFF[a]), ON=ON[a], pair=dict(OFF[a])[PAIRK], crest=dict(OFF[a])[CREST], B=B[a]) for a in A},
               runs=runs, pos=pos, und=und, crests=crests, h81=h81, h82=h82, ref1=ref1, ref2=ref2, refuted=(ref1 or ref2 or not h81))
    put_json('b554_sign_pattern.json', out)
    put_txt('b554_sign_pattern.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 5: THE PRICES
DRH = ('### `W-ORD-DETECTION-REGION` (priced at :11151) -- RE-PRICED FROM THE CLOSED FORM, appended 2026-09-28, b554, under the '
       'author`s ruling (R164)(5)')
CF_ROUTE = [
    ('C1', 'the plateau-ramp window of the ladder (the indicator of [-W, W] convolved with the order-p B-spline of half-width R) defined in '
           'the kernel, with its transform in closed form: φ̂(z) = sinc(zW)·sinc(zh/2)^p up to its normalisation -- the transform of an '
           'indicator and of a convolution power', 'new', 'of substance'),
    ('C2', 'that window in `classK`: `ContDiff ℝ 4`, even, compactly supported, for p ≥ 6 (a B-spline of order p is C^(p-2))', 'new', 'of substance'),
    ('C3', 'the orbit term in closed form at an arbitrary zero (σ, γ): 4·Re k̂(γ − iδ) as `pairTwo_factored` (PairTerm.lean) gives it at the '
           'window`s own ordinate γ₀, extended to γ ≠ γ₀', 'generalises `pairTwo_factored`', 'moderate'),
    ('C4', 'an explicit lower bound on the orbit term`s magnitude and its sign from C1 and C3 (for the pair orbit the near part is compiled, '
           '`pair_near_sign`; the far part is `farSmall`, a Prop not proved -- `pair_bound` INTERFACES on it)', 'new (the far part)', 'moderate'),
    ('C5', 'the on-line bound B(a, p) on every other zero`s term: `rest_bound_zeta` (RestBound.lean, hypothesis-free) for the pair`s orbit; '
           'for another orbit its exclusion set changes -- and at the bench`s widths the compiled constant exceeds the measured rest by '
           'about 1e16 (b530), so the statement`s region is empty there unless the bound is tightened', 'generalises `rest_bound_zeta`', 'of substance if tightened'),
    ('C6', 'the assembly: the orbit term negative and larger than C5`s bound forces the zero side, hence the quantity, negative', 'new', 'short'),
]
PL_ROUTE = [
    ('P1', 'the explicit j₀ inequality: the rest`s sum below the tie term`s magnitude for every j ≥ j₀, j₀ explicit in (L, M, B, D) and the '
           'zero`s (γ, δ) -- the finite-j form of `zeroSide_eventually_neg` (:1082), from `tie_term_neg` (:749), `rest_term_small` (:764) and '
           '`dominant_summable` (:949)', 'new', 'of substance'),
    ('P2', 'the power window`s support as a function of j and the base width, giving L₀', 'new', 'short'),
    ('P3', 'the region R(L₀) of (γ, δ) where P1 and P2 meet', 'new', 'short'),
    ('P4', 'the assembly: h2_sign on classK windows of support ≤ L₀ excludes zeros in R(L₀)', 'new', 'short'),
]
PHZ = ('*Appended 2026-09-28 by b554, under the author`s ruling `(R164)`(6), to the bridge price at :11290 -- THE PAIRING HAZARD:* the Li '
       'test function`s zero sum converges with ρ paired against 1 − ρ̄ (h_n decays only like n/ρ); the compiled Weil form`s zero sum is '
       'absolutely convergent on `classK`; PowerLimit`s summability lemmas (`dominant_summable`, `rest_tendsto_zero`) are absolute and would '
       'need a paired form for the Li channel. The difference is structural between the two criteria, and is recorded as such.')
ANL = ('*Appended 2026-09-28 by b554, under the author`s ruling `(R164)`(7) -- ANOMALY 1 ROUTED TO CP-5 (the deposit reconciliation):* '
       'SIDE-kernel HEAD `%s`, latest tag `v1.7` = `%s`, deposit pin `v1.5` = `%s`, read fresh at b554 (relay `data/b554_prices.txt`). '
       'Nothing is decided here.')


def prices():
    for h in (DRH, PHZ[:60], ANL[:60]):
        guard_absent(OT, h)
    def new_count(route):
        return sum(1 for r in route if r[2] == 'new' or r[2].startswith('new')), sum(1 for r in route if r[3].startswith('of substance'))
    cn, cs = new_count(CF_ROUTE)
    pn, ps = new_count(PL_ROUTE)
    # ### the criterion sealed on the face: fewer new lemmas of substance; then fewer new lemmas; then compiled objects
    if cs != ps:
        cheaper = 'PowerLimit' if ps < cs else 'closed-form'
        why = 'fewer new lemmas of substance (%d against %d)' % (min(cs, ps), max(cs, ps))
    elif cn != pn:
        cheaper = 'PowerLimit' if pn < cn else 'closed-form'
        why = 'on a tie in substance (%d each), fewer new lemmas (%d against %d)' % (cs, min(cn, pn), max(cn, pn))
    else:
        cheaper = 'PowerLimit'
        why = 'on a tie in both, the route whose objects are compiled (the power window is in the kernel; the B-spline plateau is not)'
    ker = dict(head=g(KER, 'rev-parse', 'HEAD').strip(), v17=g(KER, 'rev-parse', 'v1.7^{commit}').strip(), v15=g(KER, 'rev-parse', 'v1.5^{commit}').strip(),
               latest=g(KER, 'describe', '--tags', '--abbrev=0', 'HEAD').strip())
    L = ['', DRH, '',
         '**The closed-form route, in lemmas** (each marked compiled, generalising a compiled one, or new; and its weight):', '']
    L += ['- **%s** %s -- *%s; %s*' % r for r in CF_ROUTE]
    L += ['', '**The PowerLimit finite-j₀ route, in the same terms** (the compiled pieces it consumes: `tie_term_neg`, `rest_term_small`, '
          '`dominant_summable`, `zeroSide_eventually_neg`, SIDE-explicit-formula `81ae175`):', '']
    L += ['- **%s** %s -- *%s; %s*' % r for r in PL_ROUTE]
    L += ['', '**The comparison, by the criterion sealed on b554`s face** (fewer new lemmas of substance; then fewer new lemmas; then the '
          'route whose objects are compiled): closed form -- new or extended %d, of substance %d; PowerLimit -- new %d, of substance %d. '
          '**The %s route is the cheaper**, by %s; it is named the route. The closed form`s own hazard, stated with it: C5`s compiled bound '
          'makes its region empty at every width the bench reads unless tightened, and C1-C2 build in the kernel a window the kernel does not '
          'hold. **Priced, not attempted.**' % (cn + sum(1 for r in CF_ROUTE if r[2].startswith('generalises')), cs, pn, ps, cheaper, why), '']
    o1 = append_to(OT, NL.join(L))
    o1['line'] = line_of(OT, DRH)
    o2 = append_to(OT, NL.join(['', PHZ, '']))
    anl = ANL % (ker['head'][:7], ker['v17'][:7], ker['v15'][:7])
    o3 = append_to(OT, NL.join(['', anl, '']))
    out = dict(detection=o1, hazard=o2, anomaly=o3, cf=dict(new=cn, substance=cs, extended=sum(1 for r in CF_ROUTE if r[2].startswith('generalises'))),
               pl=dict(new=pn, substance=ps), cheaper=cheaper, why=why, kernel=ker, n4=(cheaper == 'closed-form'), block_lines=len(L))
    put_json('b554_prices.json', out)
    prices_bank()


PHZ_M, ANL_M = 'THE PAIRING HAZARD:*', 'ANOMALY 1 ROUTED TO CP-5'


def prices_bank():
    """### the bank of the prices, each appended line found by a marker unique to it. ### The hazard line and the Anomaly-1 line
    ### share their first sixty characters, and the first bank (a b554 defect) recorded one line for both."""
    out = jl('b554_prices.json')
    out['detection']['line'] = line_of(OT, DRH)
    out['hazard']['line'] = [i for i in lines_with(OT, re.escape(PHZ_M)) if i > out['detection']['line']][0]
    out['anomaly']['line'] = [i for i in lines_with(OT, re.escape(ANL_M)) if i > out['detection']['line']][0]
    put_json('b554_prices.json', out)
    Lp = ['b554 -- COMPONENT 5: THE PRICES, AS APPENDED', '', '### SIDE-kernel read fresh: %s' % out['kernel'], '']
    t = rd(OT).split(NL)
    a = out['detection']['line']
    Lp += ['### OPEN_TRAILS.md:%d' % a] + ['    ' + x for x in t[a - 1:a - 2 + out['block_lines']]] + ['']
    for k in ('hazard', 'anomaly'):
        Lp += ['### OPEN_TRAILS.md:%d' % out[k]['line'], '    ' + t[out[k]['line'] - 1], '']
    Lp += ['### the cheaper: %s -- %s' % (out['cheaper'], out['why'])]
    put_txt('b554_prices.txt', Lp)
    print(NL.join(Lp))


# ------------------------------------------------------------------------------ COMPONENT 6: SIMPLICITY TIERED
STD3 = 'depends on axioms: [propext, Classical.choice, Quot.sound]'
NONE_AX = 'does not depend on any axioms'
NA = 'T0, not RH-anchor: '
# ### terminal -> (the probe that reads it at the row`s pin, the probe at the second pin or None, tier, reason, the conclusion in one line)
TERMS = {
    'SpectralCannonFull.spectral_cannon': ('k1', 'k1b', 'T0', NA + '`(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0` for every real t -- Mathlib`s object; '
                                           'a fact about the line, not about where the zeros are', 'Re of the derivative of completedRiemannZeta₀ is 0 on the line'),
    'SIDEDerivative.exactly_c1_derives': ('kd', None, 'T2', 'a count over a grade map the file itself defines (`derivGrade`) -- a stipulation; '
                                          'the per-class reading is carried by the map`s names', 'a list filter over a stipulated grade map has length 1'),
    'SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero': ('kd', None, 'T0', NA + 'for a complex z with Re z = 0, z = 0 ↔ Im z = 0 -- a fact about ℂ; '
                                                          'its instance at ξ′(ρ) is `spectral_cannon``s conclusion, cross-referenced and not composed in Lean',
                                                          'for complex z with Re z = 0: z = 0 iff Im z = 0'),
    'SIDEDerivative.no_onLine_double_iff_transversal': ('kd', None, 'T0', NA + 'for a complex z with Re z = 0, z ≠ 0 ↔ Im z ≠ 0 -- a fact about ℂ; the '
                                                        'simplicity conjecture the row names is not a hypothesis of the statement',
                                                        'for complex z with Re z = 0: z ≠ 0 iff Im z ≠ 0'),
    'PerpendicularCrossing.perpendicular_gradients': ('k2', None, 'T2', 'vacuous: `(0 : ℝ) * c₁ + (-c₁) * 0 = 0` by `ring`; the gradient reading is '
                                                      'in the comments, not the statement', '0·c₁ + (−c₁)·0 = 0 for a real c₁'),
    'PerpendicularCrossing.proved_infrastructure': ('k2', None, 'T0', NA + 'four facts about Mathlib`s `completedRiemannZeta₀` and `riemannZeta` '
                                                    '(realness on the line, the derivative`s antisymmetry, nonvanishing for 1 ≤ re s, the reflection)',
                                                    'completedRiemannZeta₀ real on the line; its derivative antisymmetric; ζ ≠ 0 for re s ≥ 1; the reflection'),
    'SIDESimplicity.transversal_generic_empty': ('s1', None, 'T2', 'integer arithmetic (`omega`): curveDim = 1 and 2 ≤ obstrCodim give curveDim − '
                                                 'obstrCodim < 0; the transversality reading is carried by the names', '1 − c < 0 for integers with 2 ≤ c'),
    'SIDESimplicity.codim_exceeds_curve': ('s1', None, 'T2', 'integer arithmetic over two defined constants (1 < 5)', '1 < 5 for the defined constants'),
    'SIDESimplicity.codim_margin': ('s1', None, 'T2', 'integer arithmetic (`omega`): 1 < 5 − lost for 0 ≤ lost ≤ 3', '1 < 5 − lost for 0 ≤ lost ≤ 3'),
    'SIDESimplicity.no_tuning': ('s1', None, 'T2', 'definitional (`rfl`): a defined constant equals 0', 'freeParameters = 0 by definition'),
    'PerpendicularCrossing.simplicity_from_trace_structure': ('k2', None, 'T2', 'vacuous: the hypotheses stipulate the conclusion (m·n = R n for all n '
                                                              'and R 1 = 1 give m = 1) over ℕ', 'm = 1 for naturals with m·n = R n for all n and R 1 = 1'),
    'PerpendicularCrossing.multiplicity_from_identity': ('k2', None, 'T2', 'vacuous: m = R and R = 1 give m = 1 over ℕ', 'm = 1 for naturals with m = R and R = 1'),
    'SIDELvConservation.exists_norm_completedRiemannZeta₀_le_exp': ('l1', None, 'T0', NA + 'the order-≤1 growth of Mathlib`s `completedRiemannZeta₀`, no premise',
                                                                    '‖completedRiemannZeta₀ s‖ ≤ C·exp(A·‖s‖·log(‖s‖+2)) for some C, A'),
    'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange': ('l2', 'l2b', 'T1-lit', 'INTERFACES on `ExplicitFormulaDecomp` (Bombieri–Lagarias) '
                                                                           'and `TailBoundPremise` (Voros), literature theorems not compiled, and the numerical '
                                                                           '`VerifiedZerosTo T` (b540, (R150)(3))', '0 ≤ λ_n for 1 ≤ n ≤ N₀(T), under the three premises'),
    'SIDELvConservation.PartialPositivity.blTerm_nonneg_of_onLine': ('l2c', 'l2cb', 'T0', NA + '`0 ≤ Re[1 − (1 − 1/ρ)^n]` at a zero of Mathlib`s '
                                                                     '`riemannZeta` in the strip with Re ρ = 1/2 -- a fact about on-line zeros, not about '
                                                                     'where the zeros are', 'Re[1 − (1 − 1/ρ)^n] ≥ 0 at an on-line nontrivial zero ρ'),
    'ProductFormula.conservation_of_spectra': ('k3', None, 'T2', 'a stipulation: `∀ s : ℤ, (1 : ℚ) ^ s = 1` (`one_zpow`); the conservation reading is carried '
                                               'by the name (b539)', '1^s = 1 in ℚ for every integer s'),
    'SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin': ('l3', None, 'T0', NA + '`completedRiemannZeta s = mellin Φ (s / 2)` for 1 < re s -- '
                                                                          'Mathlib`s objects', 'completedRiemannZeta s = mellin Φ (s/2) for re s > 1, some Φ'),
    'SIDELvConservation.T2b_mellin_exhaustion': ('l4', None, 'T2', 'definitional (`rfl`): Mathlib`s `mellin` unfolded (b540)', 'mellin Φ s equals its defining integral'),
    'SIDELvConservation.T3.T3doubleprime_general_commutation_fails': ('l5', None, 'T0', NA + 'a countermodel against Mathlib`s `mellin`: the unrestricted '
                                                                      '∀∃ ⟹ ∃∀ over couplings fails at s = 3 -- a true fact of logic, neither ENCODES, SHELL, '
                                                                      'FALSE-AS-STATED nor vacuous; b545 carried it at T2', 'the unrestricted ∀∃ ⟹ ∃∀ commutation is false'),
    'SIDEGRHTransfer.grh_structural_exhaustiveness_proved': ('g1', None, 'T2', 'the χ-family catalogue, χ typed but unused -- Route 1`s shape (b540)',
                                                             'GRHStructuralExhaustiveness χ χ̄: seven classes, none producing, Ostrowski-exhaustive'),
    'SIDELvConservation.exists_norm_completedLFunction_le_exp': ('l6', None, 'T0', NA + 'the order-≤1 growth of Mathlib`s `completedLFunction`, no premise but χ ≠ 1',
                                                                 '‖completedLFunction χ s‖ ≤ C·exp(A·‖s‖·log(‖s‖+2)) for χ ≠ 1'),
    'SIDEKernel.formation': ('k4', None, 'T2', '`2 + 3 + 2 + 0 = 7` by `decide` -- arithmetic alone; the classification is carried by the identifier (b539)', '2 + 3 + 2 + 0 = 7'),
    'CartanBridge.formation_n_3_eq_two': ('k5', None, 'T2', 'the cardinality of a type the kernel defines (`OutputStageClass`) is 2 -- a count of its own '
                                          'constructors; the classification reading is carried by the name', 'Fintype.card OutputStageClass = 2'),
    'SIDELvConservation.h1_complete_at_Phi': ('l7', None, 'T0', NA + 'the eight coupling facts of `Phi`, lv`s theta-kernel function built from Mathlib`s `evenKernel`; no premise '
                                              '(b539, b545); the row`s "only h2 open" rests on lv`s h2, FALSE-AS-STATED on the strip', 'the eight couplings hold at Phi'),
    'SIDELvConservation.RegisterPentagon.goalState_of_h1_h2': ('l8', 'l8b', 'T2', 'INTERFACES on lv`s h2, `mellin Phi (s / 2) ≠ 0`, which is false at every s '
                                                               'with re s ≤ 1 (`mellin_Phi_eq_zero_of_re_le_one`, b538) -- vacuous on the strip',
                                                               'GoalState 𝒞 s from h1 at Phi and mellin Phi (s/2) ≠ 0'),
    'SIDELvConservation.C7_finite_type_false': ('l9', None, 'T0', NA + '`¬ ∃ C A, ∀ s, ‖completedRiemannZeta₀ s‖ ≤ C * exp (A * ‖s‖)`',
                                                'completedRiemannZeta₀ is not of finite exponential type'),
}
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4']
N5_EXPECT = {'SpectralCannonFull.spectral_cannon': ['T0'], 'PerpendicularCrossing.perpendicular_gradients': ['T0'],
             'SIDELvConservation.exists_norm_completedRiemannZeta₀_le_exp': ['T0'], 'SIDELvConservation.exists_norm_completedLFunction_le_exp': ['T0'],
             'SIDELvConservation.C7_finite_type_false': ['T0'], 'SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin': ['T0'],
             'SIDELvConservation.T2b_mellin_exhaustion': ['T0'], 'SIDELvConservation.T3.T3doubleprime_general_commutation_fails': ['T0'],
             'SIDEKernel.formation': ['T2'], 'CartanBridge.formation_n_3_eq_two': ['T2'], 'SIDEGRHTransfer.grh_structural_exhaustiveness_proved': ['T2'],
             'SIDESimplicity.transversal_generic_empty': ['T2'], 'PerpendicularCrossing.simplicity_from_trace_structure': ['T2'],
             'SIDELvConservation.PartialPositivity.partialPositivity_finiteRange': ['T1-lit'],
             'SIDELvConservation.h1_complete_at_Phi': ['T1-open', 'T2'], 'SIDELvConservation.RegisterPentagon.goalState_of_h1_h2': ['T1-open', 'T2']}


def simp_rows():
    """### the Correspondence table as it stood before this act (PLACE-papers e1478b6), row by row."""
    src = blob(PP, PRIOR_PP + ':phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md').split(NL)
    head = [i for i, l in enumerate(src) if l.startswith('| Claim (as stated here) |')][0]
    rows = []
    for i in range(head + 2, len(src)):
        l = src[i]
        if not l.startswith('|'):
            break
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        names = re.findall(r'`((?:[A-Z][A-Za-z0-9]*\.)+[A-Za-z_₀][A-Za-z0-9_₀]*)`', c[2])
        if names:   # ### a companion named unqualified in the same cell ("with `codim_margin`") takes the first name`s namespace
            ns = names[0].rsplit('.', 1)[0]
            names += [ns + '.' + x for x in re.findall(r'`([a-z_][A-Za-z0-9_₀]*)`', c[2]) if ns + '.' + x not in names]
        rows.append(dict(line=i + 1, claim=c[0], kernel=c[1], terminal_cell=c[2], profile_cell=c[3], status=c[4][:400], names=names,
                         branch='BRANCH-RESIDENT' in c[4]))
    audit = [i + 1 for i, l in enumerate(src) if l.startswith('*Kernels audited at:')]
    put_json('b554_simp_rows.json', dict(rows=rows, audit_line=audit[0] if audit else None, count=len(rows)))
    print('  rows %d (the ruling says twenty) ; with a terminal %d ; without %d ; names %d' % (
        len(rows), sum(1 for r in rows if r['names']), sum(1 for r in rows if not r['names']), sum(len(r['names']) for r in rows)))
    for r in rows:
        print('  :%d %-60s %s' % (r['line'], r['claim'][:60], r['names']))


def probes():
    out = {}
    for l in rd(os.path.join(D, 'b554_probes.jsonl')).split(NL):
        if l.strip():
            r = json.loads(l)
            out[r['id']] = r
    return out


def check_text(pid, name):
    """### the `#check @name` output for one name in one probe bank: from the name`s line to the next name`s or the prints."""
    t = rd(os.path.join(D, 'b554_probe_%s.txt' % pid))
    i = t.find('@' + name + ' :')
    if i < 0:
        i = t.find(name + ' :')
    if i < 0:
        return None
    rest = t[i:]
    stop = [m.start() for m in re.finditer(r"(?m)^(@?[A-Za-z_][A-Za-z0-9_.₀]* : |'[A-Za-z_]|real )", rest)][1:2]
    return ' '.join(rest[:stop[0] if stop else 1200].split())


def row_profile(cell):
    c = cell.replace('`', '')
    if 'axiom-free' in c and '{' not in c:
        return NONE_AX
    if '{propext, Classical.choice, Quot.sound}' in c:
        return STD3
    if '{propext, Quot.sound}' in c:
        return 'depends on axioms: [propext, Quot.sound]'
    return None


def simp_tiers():
    sr = jl('b554_simp_rows.json')
    pr = probes()
    ei = jl('b544_ei.json').get('marks', {})
    earlier = {}
    for f in ('b539_tiers.json', 'b540_tiers.json', 'b545_tiers.json'):
        s = rd(os.path.join(D, f))
        for n in TERMS:
            short = n.split('.')[-1]
            if short in s and n not in earlier:
                for m in re.finditer(r'"tier": "(T[0-9][^"]*)"', s[max(0, s.find(short) - 1500): s.find(short) + 1500]):
                    earlier[n] = (m.group(1), f)
                    break
    L = ['b554 -- COMPONENT 6 (a): SIMPLICITY_OF_RIEMANN_ZEROS`S CORRESPONDENCE, RE-READ AT PIN (READING (9))', '',
         '### the table (PLACE-papers %s, :%d-%d): %d rows -- the ruling says "twenty"; %d name a terminal, %d name none' % (
             PRIOR_PP, sr['rows'][0]['line'], sr['rows'][-1]['line'], sr['count'], sum(1 for r in sr['rows'] if r['names']), sum(1 for r in sr['rows'] if not r['names'])),
         '### the probes (relay data/b554_probe_<id>.txt, one file at its pin fed to `lake env lean --stdin`):']
    for pid, r in sorted(pr.items()):
        L.append('    %-4s %-22s %-8s %-52s exit %d  %7.1f s  errors %d  manifest-equal %s  imports %s' % (
            pid, r['repo'], r['pin'], r['path'], r['exit'], r['seconds'], r['errors'], r['manifest_same'], r['closure'] or 'NONE'))
    rows_out, terms_out = [], []
    for r in sr['rows']:
        tiers, disp_bits = [], []
        for n in r['names']:
            if n not in TERMS:
                sys.exit('### A TERMINAL WITHOUT A TIER: %s' % n)
            p1, p2, tier, reason, concl = TERMS[n]
            a = pr.get(p1, {})
            prof = (a.get('profiles') or {}).get(n)
            prof = ' '.join(prof.split()) if prof else prof   # ### Lean wraps a long print line; the words are the profile
            st1 = check_text(p1, n)
            st2 = check_text(p2, n) if p2 else None
            want = row_profile(r['profile_cell'])
            if n.endswith('no_tuning'):
                want = NONE_AX
            found = bool(st1) and a.get('exit') == 0
            same2 = (st2 == st1) if p2 else None
            ok = found and prof == want and (same2 is not False)
            moved = [] if ok else [x for x, b in (('not found at its pin', not found), ('profile %s against the row`s %s' % (prof, want), prof != want),
                                                  ('statement differs at the second pin', same2 is False)) if b]
            tiers.append(tier)
            disp_bits.append(not moved)
            terms_out.append(dict(row=r['line'], name=n, pin=a.get('pin'), probe=p1, second=p2, found=found, statement=st1, statement2=st2, same2=same2,
                                  profile=prof, row_profile=want, tier=tier, reason=reason, conclusion=concl, earlier=earlier.get(n),
                                  ei=ei.get('%s|%s' % (a.get('repo'), n), 'not indexed'), moved=moved, branch=r['branch']))
        rt = max(tiers, key=ORDER.index) if tiers else 'T4'
        rows_out.append(dict(line=r['line'], claim=r['claim'], names=r['names'], tiers=tiers, tier=rt, branch=r['branch'],
                             disp=('CARRIED' if all(disp_bits) else 'MOVED'), kernel=r['kernel']))
    for t in terms_out:
        L += ['', '### :%d %s  [%s %s via %s%s]%s' % (t['row'], t['name'], t['pin'], 'FOUND' if t['found'] else 'NOT FOUND', t['probe'],
                                                  (' and %s' % t['second']) if t['second'] else '', '  BRANCH-RESIDENT' if t['branch'] else ''),
              '    statement : %s' % (t['statement'] or 'NONE')[:900]]
        if t['second']:
            L.append('    at the second pin (%s): %s' % (t['second'], 'the same statement' if t['same2'] else ('DIFFERS: ' + (t['statement2'] or 'NONE')[:600])))
        L += ['    profile   : %s   (the row prints: %s)' % (t['profile'], t['row_profile']),
              '    tier      : %s -- %s' % (t['tier'], t['reason']),
              '    earlier   : %s ; E/I (b544) : %s' % ('%s (relay data/%s)' % t['earlier'] if t['earlier'] else 'none banked', t['ei']),
              '    conclusion: %s' % t['conclusion'],
              '    disposition: %s' % ('CARRIED' if not t['moved'] else 'MOVED -- ' + '; '.join(t['moved']))]
    tc = {k: sum(1 for t in terms_out if t['tier'] == k) for k in ORDER}
    rc = {k: sum(1 for r in rows_out if r['tier'] == k) for k in ORDER}
    dc = {k: sum(1 for r in rows_out if r['disp'] == k) for k in ('CARRIED', 'MOVED')}
    n5 = {n: (next(t['tier'] for t in terms_out if t['name'] == n), v) for n, v in N5_EXPECT.items()}
    n5_ok = all(t in v for t, v in n5.values())
    br = [t for t in terms_out if t['branch']]
    br_ok = bool(br) and all(t['found'] and t['profile'] == t['row_profile'] for t in br)
    carries = [t['name'] for t in terms_out if re.search(r'(?i)RiemannHypothesis', t['statement'] or '') and re.search(r'(?i)simpl|mult', t['statement'] or '')]
    L += ['', '### TIERS OVER THE %d TERMINALS: %s' % (len(terms_out), ' · '.join('%s %d' % (k, tc[k]) for k in ORDER)),
          '### ROW TIERS (the weakest link; a row with no terminal T4) OVER THE %d ROWS: %s' % (len(rows_out), ' · '.join('%s %d' % (k, rc[k]) for k in ORDER)),
          '### DISPOSITIONS: CARRIED %d · MOVED %d' % (dc['CARRIED'], dc['MOVED']), '',
          '### (N5), terminal by terminal: fresh tier against the tier the navigator names']
    L += ['    %-66s %-7s %s %s' % (n, t, '/'.join(v), 'agrees' if t in v else 'DIFFERS') for n, (t, v) in n5.items()]
    L += ['### the three branch rows at 27a3ae7, profiles against the table: ' + '; '.join('%s %s (table %s)' % (t['name'].split('.')[-1], t['profile'], t['row_profile']) for t in br),
          '', '### (N6) each row`s conclusion in one line:']
    for r in rows_out:
        cs = [t['conclusion'] for t in terms_out if t['row'] == r['line']]
        L.append('    :%d %s' % (r['line'], ' ; '.join(cs) if cs else '(no terminal: %s)' % r['kernel']))
    L.append('### a compiled statement among the rows naming both RiemannHypothesis and simplicity or multiplicity: %s' % (carries or 'NONE'))
    out = dict(rows=rows_out, terms=terms_out, term_tiers=tc, row_tiers=rc, disp=dc, n5=n5, n5_ok=n5_ok, branch_ok=br_ok, carries=carries,
               count=sr['count'], probes={k: dict(exit=v['exit'], seconds=v['seconds'], errors=v['errors']) for k, v in pr.items()})
    put_json('b554_simp_tiers.json', out)
    put_txt('b554_simp_tiers.txt', L)
    print(NL.join(L))


def stems():
    """### (R164)(8)(d): `banned_terms.STEMS` counted per stem over SIMPLICITY as it stood before this act; no edit."""
    import banned_terms as BTM
    src = blob(PP, PRIOR_PP + ':phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md').split(NL)
    hits = []
    for i, l in enumerate(src, 1):
        for m in BTM.PAT.finditer(l):
            hits.append(dict(line=i, stem=[s for s in BTM.STEMS if m.group(0).lower().startswith(s)][0], word=m.group(0),
                             cls=BTM.classify(l, m.start(), SIMP) or 'LIVE USE', text=l[max(0, m.start() - 70):m.end() + 70]))
    per = {s: sum(1 for h in hits if h['stem'] == s) for s in BTM.STEMS}
    live = {s: sum(1 for h in hits if h['stem'] == s and h['cls'] == 'LIVE USE') for s in BTM.STEMS}
    L = ['b554 -- COMPONENT 6 (d): THE BANNED-STEM COUNT OVER SIMPLICITY_OF_RIEMANN_ZEROS.md (READING (12)); no edit', '',
         '### the document at PLACE-papers %s (before this act`s append); the stems of relay tools/banned_terms.py: %s' % (PRIOR_PP, BTM.STEMS),
         '### per stem: %s ; of them live uses (no exception applies): %s' % (per, live)]
    L += ['    :%-4d %-6s %-10s %-44s ...%s...' % (h['line'], h['stem'], h['word'], h['cls'][:44], h['text']) for h in hits]
    put_json('b554_stems.json', dict(per=per, live=live, hits=hits))
    put_txt('b554_stems.txt', L)
    print(NL.join(L))


SBH = ('#### THE CASCADE, ACT EIGHT -- THE CORRESPONDENCE TIERED *(appended 2026-09-28, b554, under the author`s ruling `(R164)`(8); no '
       'byte above this block changes; the title, the Abstract and §§ are not edited -- the edition waits for CP-7, `(R157)`(2))*')
SPT = '*Appended 2026-09-28 by b554, under the author`s ruling `(R164)`(8) -- BACK MATTER, THE READING:*'


def short(n):
    return n.split('.')[-1]


def simp_block():
    guard_absent(SIMP, SBH)
    s = jl('b554_simp_tiers.json')
    L = ['', '<!-- b554 THE CASCADE, ACT EIGHT, 2026-09-28 -->', '', SBH, '',
         '**The rows, re-read at pin.** The table at :435-455 has %d rows (the ruling says twenty): %d name a terminal, %d name none. Each '
         'terminal`s file at the row`s pin was elaborated fresh with `#check` and `#print axioms` appended (relay `data/b554_probe_<id>.txt`; the '
         'statements, profiles, tiers and reasons, `data/b554_simp_tiers.txt`): SIDE-kernel at `v1.2` = `b1407b2`, `spectral_cannon` also at the '
         'deposit pin `v1.5` = `0e5233f`, where its file differs; SIDE-simplicity `v0.1.0`; SIDE-grh-transfer `v0.5.0`; SIDE-lv-conservation at each '
         'row`s tag and, where the file differs, at `v0.11.0` = `2f71068`; the three branch rows at `27a3ae7` in a worktree of SIDE-kernel`s '
         '`derivative-engine`, removed after. The tier is that of the weakest link to Mathlib, `(R149)`(2); a row with no terminal is T4.'
         % (s['count'], sum(1 for r in s['rows'] if r['names']), sum(1 for r in s['rows'] if not r['names'])), '',
         '| row | claim (abridged) | terminal(s) | fresh profile(s) | disposition | tier(s) |', '|:--|:--|:--|:--|:--|:--|']
    for r in s['rows']:
        ts = [t for t in s['terms'] if t['row'] == r['line']]
        prof = sorted(set((t['profile'] or 'NONE').replace('depends on axioms: ', '').replace('does not depend on any axioms', 'axiom-free') for t in ts))
        claim = re.sub(r'\$[^$]*\$', '…', r['claim']).replace('|', '/').replace('**', '')
        L.append('| :%d | %s | %s | %s | **%s** | %s%s |' % (
            r['line'], claim[:90], ', '.join('`%s`' % short(t['name']) for t in ts) or 'NONE', '; '.join(prof) or '—', r['disp'],
            ', '.join(sorted(set(r['tiers']), key=ORDER.index)) or 'T4', ' **BRANCH-RESIDENT**' if r['branch'] else ''))
    mv = [t for t in s['terms'] if t['moved']]
    L += ['', '*Tiers over the %d terminals: %s. Rows by their weakest link: %s. Dispositions: CARRIED %d · MOVED %d.*' % (
        len(s['terms']), ' · '.join('%s %d' % (k, s['term_tiers'][k]) for k in ORDER), ' · '.join('%s %d' % (k, s['row_tiers'][k]) for k in ORDER),
        s['disp']['CARRIED'], s['disp']['MOVED'])]
    if mv:
        L += ['', '**What moved:** ' + '; '.join('`%s` (:%d) -- %s' % (short(t['name']), t['row'], '; '.join(t['moved'])) for t in mv) + '.']
    L += ['', '**The branch rows.** `exactly_c1_derives`, `onLine_doubleZero_iff_imDeriv_zero` and `no_onLine_double_iff_transversal` are '
          'tiered at `27a3ae7`, on SIDE-kernel`s `derivative-engine` and absent from `main`; their residence is carried beside the tier (b397). '
          '`partialPositivity_finiteRange` is T1-lit, as b540 tiered it.', '',
          '*Appended by b554. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
    o = append_to(SIMP, NL.join(L))
    o['line'] = line_of(SIMP, SBH)
    put_json('b554_simp_block.json', o)
    print(NL.join(rd(SIMP).split(NL)[o['line'] - 1:]))


RH_ = '## SIMPLICITY_OF_RIEMANN_ZEROS read against its compiled statements: the title`s reduction is compiled in neither direction'


def simp_reading():
    guard_absent(FIND, RH_)
    guard_absent(SIMP, SPT)
    s = jl('b554_simp_tiers.json')
    tt = {t['name']: t for t in s['terms']}
    sc, od, nd = (tt['SpectralCannonFull.spectral_cannon'], tt['SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero'],
                  tt['SIDEDerivative.no_onLine_double_iff_transversal'])
    blk = line_of(SIMP, SBH)
    L = ['', RH_, '',
         '*Filed at b554 on the author`s ruling `(R164)`(8), graded READING. Banks: relay `data/b554_simp_tiers.txt`, `data/b554_probe_k1.txt`, '
         '`data/b554_probe_kd.txt`. The document`s §§ are not edited; its tier block is at `SIMPLICITY_OF_RIEMANN_ZEROS.md`:%d.*' % blk, '',
         '**What the document says.** Chapter 1 is titled "The Reduction: RH ⟺ Simplicity" (`SIMPLICITY_OF_RIEMANN_ZEROS.md`:36). The Abstract '
         '(:24) says the intersection structure of Re ξ = 0 and Im ξ = 0 "is governed by zero simplicity through perpendicular crossing". The '
         'reduction theorem of the body (:71-78) states: RH ⟺ Re ξ = 0 and Im ξ = 0 do not intersect outside σ = 1/2.', '',
         '**What is compiled, read fresh at the rows’ pins.** `spectral_cannon` (SIDE-kernel `v1.2`): Re ξ′(1/2 + it) = 0 in the kernel`s form, '
         '`%s`. The on-line double-zero criterion `onLine_doubleZero_iff_imDeriv_zero` (`27a3ae7`): `%s`. The joint step '
         '`no_onLine_double_iff_transversal` (`27a3ae7`): `%s` -- the row carries the simplicity conjecture as its named premise, and the '
         'statement has no hypothesis beyond Re z = 0; uniform transversality is not stated.' % (
             (sc['statement'] or '').split(' : ', 1)[-1][:160], (od['statement'] or '').split(' : ', 1)[-1][:200], (nd['statement'] or '').split(' : ', 1)[-1][:200]), '',
         '**The reading.** No compiled statement among the rows carries simplicity to RH or RH to simplicity: each row`s conclusion, in one line, '
         'is printed in relay `data/b554_simp_tiers.txt`, and none has RH as a conclusion or a hypothesis beside simplicity. The body`s reduction '
         'theorem is a restatement -- a zero of ξ is a point where the two level curves meet, so "no intersection off the line" and "no zero off '
         'the line" are one proposition -- and it is manuscript-resident (:440). The title names a claimed property, an equivalence of RH with '
         'simplicity, that the body does not establish, which the writing law forbids. The title is not edited; the edition (the CP-7 companion) '
         'carries the correction. Nothing here is a statement about RH or about ζ’s zeros.', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, RH_)
    p = append_to(SIMP, NL.join(['', SPT + ' a reading of this document`s title and Abstract against its compiled statements is entered at '
                                  '`FINDINGS.md`:%d (b554); §§ unedited.' % o['line'], '']))
    p['line'] = line_of(SIMP, SPT)
    put_json('b554_simp_reading.json', dict(findings=o, pointer=p))
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:o['line'] + 12]))
    print(rd(SIMP).split(NL)[p['line'] - 1])


# ------------------------------------------------------------------------------ THE ENTRY, THE SCORES, THE DESK, THE RECORD
FH = ('## The cascade, act eight: SIMPLICITY_OF_RIEMANN_ZEROS tiered, the branch rows carried at their branch; bd2ae1a`s referent; '
      'Reading One closed; the sign pattern at Q0 on the fine grid')
HEADING = ('### b554 — the cascade, act eight under (R164): SIMPLICITY_OF_RIEMANN_ZEROS tiered; bd2ae1a ruled and filed; the two conflicts '
           'settled; Reading One closed; the sign pattern on the fine grid; the detection region re-priced; the pairing hazard; Anomaly 1 routed')


def roster_next():
    t = rd(CENSUS)
    ln = [l for l in t.split(NL) if l.startswith('**The cascade`s remaining roster'.replace('`', "'"))][0]
    names = re.findall(r'`([A-Z_0-9a-z]+)`', ln)
    rem = [n for n in names if n != 'SIMPLICITY_OF_RIEMANN_ZEROS']
    return rem[0], rem


def findings():
    guard_absent(FIND, FH)
    er, sy, ts, r1, sp, pr, st, sr = (jl('b554_erratum.json'), jl('b554_trailsup.json'), jl('b554_simp_tiers.json'), jl('b554_reading_one.json'),
                                      jl('b554_sign_pattern.json'), jl('b554_prices.json'), jl('b554_stems.json'), jl('b554_simp_reading.json'))
    syn = jl('b554_synonym.json')
    before = jl('b554_table_before.json')
    nxt, rem = roster_next()
    pos = sp['pos']
    L = ['', FH, '',
         '*Filed at b554 on the author`s ruling `(R164)`. The cascade`s act eight. Banks: relay `data/b554_bd2.txt`, `data/b554_erratum.txt`, '
         '`data/b554_synonym.txt`, `data/b554_trailsup.txt`, `data/b554_sign_pattern.txt`, `data/b554_prices.txt`, `data/b554_simp_tiers.txt`, '
         '`data/b554_stems.txt`.*', '',
         '**SIMPLICITY_OF_RIEMANN_ZEROS tiered.** Its Correspondence table has %d rows (the ruling says twenty), %d naming %d terminals. Tiers '
         'over the terminals: %s; rows by their weakest link: %s; dispositions CARRIED %d · MOVED %d. The three branch rows are carried at '
         '`27a3ae7`, BRANCH-RESIDENT. The tier block is at `SIMPLICITY_OF_RIEMANN_ZEROS.md`:%d; the reading of its title at `FINDINGS.md`:%d.' % (
             ts['count'], sum(1 for r in ts['rows'] if r['names']), len(ts['terms']), ' · '.join('%s %d' % (k, ts['term_tiers'][k]) for k in ORDER),
             ' · '.join('%s %d' % (k, ts['row_tiers'][k]) for k in ORDER), ts['disp']['CARRIED'], ts['disp']['MOVED'], jl('b554_simp_block.json')['line'],
             sr['findings']['line']), '',
         '**The stem count (no edit).** Over the document as it stood, the banned stems of `tools/banned_terms.py` occur %d time(s) in all, '
         '%d of them live, at :%s; the count per stem is in relay `data/b554_stems.txt`.' % (
             sum(st['per'].values()), sum(st['live'].values()), ', :'.join(str(h['line']) for h in st['hits'])), '',
         '**bd2ae1a.** A PLACE-papers commit of %s, the E-CHARACTERIZATION sitting; the referent ruled the sitting record, not a kernel pin; '
         '`E-2026-09-27-1` filed at `ERRATA.md`:%d, with appended lines at PATHS :%d, THE_RESIDUE_OF_RH :%d and THE_KEYSTONE_CENSUS :%d.' % (
             jl('b554_bd2.json')['date'][:10], er['erratum']['line'], er['lines']['PATHS_TO_THE_CRITICAL_LINE.md']['line'],
             er['lines']['THE_RESIDUE_OF_RH.md']['line'], er['lines']['THE_KEYSTONE_CENSUS.md']['line']), '',
         '**The two conflicts.** The synonym map (`tools/terminal_table.py`) clears R5_output_HilbertPolya_to_RH (CONFLICT -> ENCODES); the '
         'trail-line form, with its line at `OPEN_TRAILS.md`:%d, clears register5_output_holds (CONFLICT -> DERIVES). CONFLICT %d -> %d -> %d; no '
         'other grade moved.' % (jl('b554_supline.json')['line'], len(before['conflicts']), len(syn['conflicts_after']), len(sy['conflicts_after'])), '',
         '**Reading One closed** at `FINDINGS.md`:%d (READING).' % r1['line'], '',
         '**Reading Eight -- the sign pattern at Q0, order 7, on the fine grid.** The off-line part exact over the 17 orbits, the on-line part '
         'from b548`s banked zero side interpolated in ln a, the floor printed per interval (at most %.2f). Positive intervals above the floor: '
         '%s. **H8 %s** -- %s. The 29.55 crests at a ≥ 38: %s.' % (
             max(f['floor'] for f in sp['floor']), '; '.join('a %.3f–%.3f' % (math.exp(a), math.exp(b)) for a, b in pos),
             'REFUTED' if sp['refuted'] else 'NOT REFUTED', 'a second positive interval at the low end, besides the one containing 36–38' if sp['ref1'] else 'as fixed',
             '; '.join('a = %.2f, its term %+.1f against the pair %+.1f' % (c['a'], c['crest'], c['pair']) for c in sp['crests'])), '',
         '**The prices.** W-ORD-DETECTION-REGION re-priced from the closed form at `OPEN_TRAILS.md`:%d: the %s route is the cheaper (%s). The '
         'pairing hazard at :%d; Anomaly 1 routed to CP-5 at :%d.' % (pr['detection']['line'], pr['cheaper'], pr['why'], pr['hazard']['line'], pr['anomaly']['line']), '',
         '**Next keystone:** `%s`.' % nxt, '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH or about ζ’s zeros.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, FH)
    o['next'] = nxt
    o['remaining'] = rem
    put_json('b554_findings.json', o)
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:]))


WRITE_OK = {'ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md',
            'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md'}
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-simplicity': '54ba4f3', 'SIDE-grh-transfer': '858cbf6'}
WT = 'D:/wt-b554-deriv'


def w(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def worktree_gone():
    wl = g(KER, 'worktree', 'list', '--porcelain')
    return (not os.path.exists(WT)) and ('wt-b554-deriv' not in wl)


def scores():
    b, syn, sy, before, sp, pr, ts = (jl('b554_bd2.json'), jl('b554_synonym.json'), jl('b554_trailsup.json'), jl('b554_table_before.json'),
                                      jl('b554_sign_pattern.json'), jl('b554_prices.json'), jl('b554_simp_tiers.json'))
    committed = g(PP, 'log', '-1', '--pretty=%s').startswith('b554 --')
    base = 'HEAD~1' if committed else 'HEAD'
    pref = {}
    for f in sorted(WRITE_OK):
        old = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (base, f)], capture_output=True).stdout.replace(b'\r\n', b'\n')
        new = open(os.path.join(PP, f), 'rb').read().replace(b'\r\n', b'\n')
        pref[f] = new.startswith(old)
    written = sorted(x for x in g(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x) if not committed else \
        sorted(x for x in g(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b554_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b554_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    after = {}
    t = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    for r in (t.get('rows', t) if isinstance(t, dict) else t):
        if isinstance(r, dict) and 'name' in r:
            after['%s|%s' % (r['repo'], r['name'])] = r['grade']
    changed = sorted(k for k in after if after[k] != before['grades'].get(k))
    ca = sorted(k for k, v in after.items() if v == 'CONFLICT')
    nxt, _ = roster_next()
    pos = sp.get('pos') or []
    return dict(
        n1=bool(b) and b['date'].startswith('2026-07-25') and 'E-CHARACTERIZATION sitting' in b['subject'],
        n2=bool(before) and len(before['conflicts']) - len(ca) == 2 and changed == sorted([R5, R5H]) and after.get(R5) != 'CONFLICT' and after.get(R5H) != 'CONFLICT',
        n3=bool(sp) and bool(sp['h81']) and bool(sp['h82']),
        n4=bool(pr) and bool(pr['n4']),
        n5=bool(ts) and bool(ts['n5_ok']) and bool(ts['branch_ok']),
        n6=bool(ts) and ts['carries'] == [] and all(t0['conclusion'] for t0 in ts['terms']),
        n7=not lean and not zen and tok == 0 and dep and worktree_gone() and trial['head'].startswith('f22ff35') and trial['status'] == '',
        mains=m, prefixes=pref, written=written, zen=zen, token=tok, deposit_clean=dep, trial=trial, worktree_gone=worktree_gone(),
        table_changed=changed, conflicts_after=ca,
        s1=bool(pos) and abs(math.exp(pos[0][0]) - 30.0) < 1e-6 and math.exp(pos[0][1]) < 34.0 and bool(sp['ref1']),
        s2=bool(pr) and pr['cheaper'] == 'PowerLimit',
        s3=nxt == 'GRH_CASCADE')


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'), ('s1', 's2', 's3')
    b, sp, pr, ts = jl('b554_bd2.json'), jl('b554_sign_pattern.json'), jl('b554_prices.json'), jl('b554_simp_tiers.json')
    before = jl('b554_table_before.json')
    L = ['=' * 104, 'b554 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- %s ; subject "%s".' % (w(sc['n1']), b['date'], b['subject'].split(':')[0]),
         '  **(N2)** ### **%s.** -- CONFLICT %d -> %d ; terminals whose grade changed %s.' % (w(sc['n2']), len(before['conflicts']), len(sc['conflicts_after']), sc['table_changed']),
         '  **(N3)** ### **%s.** -- positive intervals above the floor %d (%s) ; H8.1 %s ; H8.2 %s.' % (
             w(sc['n3']), len(sp['pos']), '; '.join('a %.4f-%.4f' % (math.exp(a), math.exp(z)) for a, z in sp['pos']), sp['h81'], sp['h82']),
         '  **(N4)** ### **%s.** -- the cheaper: %s (%s).' % (w(sc['n4']), pr['cheaper'], pr['why']),
         '  **(N5)** ### **%s.** -- terminals differing from the named tier: %s ; the branch rows` profiles as the table prints them: %s.' % (
             w(sc['n5']), {n: v[0] for n, v in ts['n5'].items() if v[0] not in v[1]} or 'NONE', ts['branch_ok']),
         '  **(N6)** ### **%s.** -- a compiled statement carrying simplicity to RH in either direction: %s.' % (w(sc['n6']), ts['carries'] or 'NONE'),
         '  **(N7)** ### **%s.** -- mains changed %s ; `.lean` none ; worktree gone %s ; token %s ; deposit clean %s ; trial %s.' % (
             w(sc['n7']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['worktree_gone'], sc['token'], sc['deposit_clean'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- the first positive interval: a %.6f-%.6f ; refuter 1 %s.' % (
             w(sc['s1']), math.exp(sp['pos'][0][0]), math.exp(sp['pos'][0][1]), 'fires' if sp['ref1'] else 'does not fire'),
         '  **(S2)** ### **%s.** -- the cheaper: %s.' % (w(sc['s2']), pr['cheaper']),
         '  **(S3)** ### **%s.** -- the next untiered keystone: %s.' % (w(sc['s3']), roster_next()[0]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b554_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b554_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b554_desk_notes.txt', L)
    put_json('b554_scores.json', {k: v for k, v in sc.items()})
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b554 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b554_bd2.txt', 'b554_erratum.txt', 'b554_synonym.txt', 'b554_trailsup_noop.txt', 'b554_trailsup.txt', 'b554_sign_pattern.txt',
              'b554_prices.txt', 'b554_simp_tiers.txt', 'b554_stems.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b554_readme.json', 'b554_supline.json', 'b554_reading_one.json', 'b554_simp_block.json', 'b554_simp_reading.json', 'b554_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE PROBES : relay data/b554_probe_<id>.txt and data/b554_probes.jsonl', '### THE WORKTREE : see data/b554_worktree.txt',
          '### THE BRANCHES : see data/b554_branches.txt', '=' * 132]
    put_txt('b554_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc = scores()
    er, sy, pr, ts, fj, r1, sp = (jl('b554_erratum.json'), jl('b554_supline.json'), jl('b554_prices.json'), jl('b554_simp_tiers.json'),
                                  jl('b554_findings.json'), jl('b554_reading_one.json'), jl('b554_sign_pattern.json'))
    body = ['', HEADING, '',
            '**(R164) ratified.** (1) bd2ae1a`s referent ruled the sitting record and the mis-attribution filed as `E-2026-09-27-1`. (2) The two '
            'conflicts settled: a synonym map and a trail-line supersession in `tools/terminal_table.py`, each committed alone with its test. (3) '
            'Reading One closed by b553`s derivation. (4) The sign pattern at Q0 read on the fine grid under H8. (5) The detection region re-priced '
            'from the closed form. (6) The bridge`s pairing hazard entered. (7) Anomaly 1 routed to CP-5. (8) SIMPLICITY_OF_RIEMANN_ZEROS tiered as '
            'act eight, its reading entered. (9) The next keystone named from the census`s order.', '',
            '**Entered:** ERRATA.md:%d (`E-2026-09-27-1`); PATHS_TO_THE_CRITICAL_LINE.md:%d, THE_RESIDUE_OF_RH.md:%d and THE_KEYSTONE_CENSUS.md:%d '
            '(the three lines); OPEN_TRAILS.md:%d (the supersession line), :%d (the detection price), :%d (the pairing hazard), :%d (Anomaly 1); '
            'FINDINGS.md:%d (Reading One closed), :%d (the SIMPLICITY reading) and :%d (the entry); SIMPLICITY_OF_RIEMANN_ZEROS.md:%d (the tier '
            'block) and :%d (the pointer); relay `tools/terminal_table.py` (the synonym map; the trail-line form) and `tools/corr_row.README.md`.' % (
                er['erratum']['line'], er['lines']['PATHS_TO_THE_CRITICAL_LINE.md']['line'], er['lines']['THE_RESIDUE_OF_RH.md']['line'],
                er['lines']['THE_KEYSTONE_CENSUS.md']['line'], sy['line'], pr['detection']['line'], pr['hazard']['line'], pr['anomaly']['line'],
                r1['line'], jl('b554_simp_reading.json')['findings']['line'], fj['line'], jl('b554_simp_block.json')['line'],
                jl('b554_simp_reading.json')['pointer']['line']), '',
            '**H8 %s.** SIMPLICITY: tiers %s; CARRIED %d · MOVED %d. **Next keystone:** `%s`.' % (
                'REFUTED' if sp['refuted'] else 'NOT REFUTED', ' · '.join('%s %d' % (k, ts['term_tiers'][k]) for k in ORDER), ts['disp']['CARRIED'],
                ts['disp']['MOVED'], fj['next']), '',
            '**CP-1:** open; the cascade continues with `%s`.' % fj['next'], '',
            '**Next:** `%s`.' % fj['next'], '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
            '**No kernel lane opened at this act; the kernel reads were fresh elaborations at pin, and the numerical lane carried the closed-form '
            'evaluations alone.** Nothing deposits; nothing at Zenodo written; no `.lean` file edited; no monograph byte changed; the ceiling '
            'unchanged; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or about '
            'ζ’s zeros.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b554_trail_notes.json', out)


if __name__ == '__main__':
    fn = {k: globals()[k] for k in ('reads', 'bd2', 'erratum', 'table_before', 'synonym_test', 'trail_sup_test', 'sup_line', 'readme',
                                    'reading_one', 'sign_pattern', 'prices', 'prices_bank', 'simp_rows', 'simp_tiers', 'stems', 'simp_block',
                                    'simp_reading', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
