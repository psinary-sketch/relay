# -*- coding: utf-8 -*-
# b754 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R364)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R364)(2) repair it carries. Edited by the Edit tool. Carried at b754 by tools/b754_fold.py (`carry`) from tools/acts/b753.py,
# b753`s names substituted; the citation`s sections adopted from tools/b754_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b753`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b753`s carried till
# then); the loader prints them at every load, and the seal wants every PENDING line empty.
#⟪DEAD checks ⟫
#⟪DEAD citation ⟫
#⟪DEAD closing ⟫
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,C2_HALT,C2_PRED,C2_REG,C2_SELECT,C3_RULE,C4_PRED,C6_CENSUS,C6_DRAFTS,C6_FROZEN,C6_RELAY,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
#⟪DEAD reg_gate ⟫
#⟪DEAD regspec ⟫
#⟪DEAD report ⟫
# Each "#⟪PENDING <tool> <names>⟫" line: names the act`s tool reads on routes carried from the act before that the act has
# still to write for itself; printed at every load; the act`s suite holds them empty at its seal.
#⟪PENDING checks ⟫
#⟪PENDING citation ⟫
#⟪PENDING closing ⟫
#⟪PENDING record ⟫
#⟪PENDING reg_gate ⟫
#⟪PENDING regspec ⟫
#⟪PENDING report ⟫
# ### b754, Component 1: THE c1 ROUTE FOR b753'S WEIGHT LINE AND ITS CORRIGENDUM, (R364)(1)-(3). NOT YET WRITTEN.
# ### b754 step zero: the route carried from b753 composed b752's figures under b753's names (13 events, 36 defects, v1.33.0's bank
# ### named for v1.32.0's) and read banks the ruling does not name; `carry.py ruled` refused it (R5). Its body is removed whole and the
# ### route refuses itself until Component 1 writes it against b753's banks (events (1)-(9) and (10)-(14), 52 defects) and v1.34.0.
#⟪OVERRIDE record MARK 8b04c0573f40 8 REPAIR (c1)⟫
C1_WRITTEN = False   # ### b754 step zero: no carried figure stands; Component 1 writes the route


def c1(*a):
    """`c1 weight|corrigendum [dry|write]`: NOT YET WRITTEN at b754 -- refuses itself, composing and writing nothing."""
    sys.exit('### THE c1 ROUTE IS NOT YET WRITTEN AT b754 (removed at step zero, carry.py ruled R5): Component 1 writes it against '
             'data/b753_events.txt (1)-(9), data/b753_events_postseal.txt (10)-(14), data/b753_defects.txt (a)-(z\') and tools/standing/ v1.34.0 -- NOTHING COMPOSED')
#⟪END⟫
# ### b754, Component 3 (the Edit tool, before the face; defect (k)): THE OVERRIDE NOTES BELOW WERE CARRIED BY THE ACT SHIFT FROM EARLIER ACTS'
# ### FORMS -- where a note says "b754, Component 4/6/7" with a commit this act does not have, it is an earlier act's note under b754's name.
# ### b754's own changes are marked "b754, Component 3". The runner overrides read the act's dispatch rows: (R364)(3)(c) allows two print
# ### dispatches, none sent, so no row exists (data/b754_dispatch_rows.json absent) and the runner arms read VACUOUS.
#⟪OVERRIDE checks MARK 8df6a527436b 13⟫
def rebuild_wf_ok(S):
    """(R363)(7), as b753 left the branches (no kernel commit this act): the workflow at each rebuild branch's tip -- the five kernels other
    than SIDE-frobenius carrying build-module.yml on main; SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's with b721's
    two lines (the push trigger to the branch, the target fixed) and nothing else, the hold kept; SIDE-kernel's tip carrying main's
    build-module.yml changed in the four places of b723's kdraft4_clear row (data/b723_axiom_rows.json) and nothing else; no identifier of
    the author and no secret at either tip."""
    import difflib
    st = S['rebuild_state'] or {}
    fr, kn = st.get('SIDE-frobenius') or {}, st.get('SIDE-kernel') or {}
    src = read_blob(EF, 'HEAD:.github/workflows/build-module.yml') or ''
    tip = fr.get('wf_tip') or ''
    d = [x for x in difflib.unified_diff(src.split(NL), tip.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    km = read_blob('D:/SIDE-kernel', 'main:.github/workflows/build-module.yml') or ''
    kt = kn.get('wf_tip') or ''
    kd = [x for x in difflib.unified_diff(km.split(NL), kt.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    row = [r for r in (S['rebuild_rows_b723'] or []) if r.get('kind') == 'kdraft4_clear' and r.get('kernel') == 'SIDE-kernel']
    want = [x for x in (row[-1].get('diff') or []) if x[:1] in '+-' and x[:3] not in ('+++', '---')] if row else None
    return all(v['wf_main'] for k, v in st.items() if k != 'SIDE-frobenius') and fr.get('wf_main') is False \
        and d == ['+  push: { branches: [%s] }' % K.REBUILD_BRANCH, '-      TARGET: ${{ inputs.target }}', '+      TARGET: SIDEFrobenius'] \
        and bool(kt) and bool(want) and kd == want and not any(w in (x or '').lower() for x in (tip, kt) for w in IDENT_WF) \
        and 'hold_mb: "2560"' in tip.lower()
#⟪END⟫
#⟪OVERRIDE checks MARK aed8852d751b 16⟫
def runner_ok(S):
    """N1, b754 (b742's form): no dispatch allowed and none made (MAX_DISPATCHES 0, EF_RUNS empty); any dispatch row carrying free_mb, its run
    id the worklist's, read once after it by that id; the plant a dispatch row with no read refused."""
    rows = S['drows'] or []
    ds = [r for r in rows if r.get('kind') == 'dispatch']
    rs = [r for r in rows if r.get('kind') == 'read']
    return len(ds) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 0 and [int(r.get('run')) for r in ds] == list(K.EF_RUNS) \
        and all(str(r.get('free_mb', '')).isdigit() for r in ds + rs) \
        and all(sum(1 for x in rs if str(x.get('run')) == str(d.get('run'))) == 1
                and rows.index(d) < next(i for i, x in enumerate(rows) if x.get('kind') == 'read' and str(x.get('run')) == str(d.get('run'))) for d in ds)
#⟪END⟫
#⟪OVERRIDE checks MARK 066da78426c2 4⟫
    for d_ in [r for r in rows if r.get('kind') == 'dispatch']:
        i_ = rows.index(d_)
        rd_ = [j for j, r in enumerate(rows) if r.get('kind') == 'read' and str(r.get('run')) == str(d_.get('run'))]
        order = order and len(rd_) == 1 and i_ < rd_[0]   # ### b754: each dispatch read once after it by its run id (six this act)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): v1.11.0 edited tools/standing/hook.py for (R364)(2)(iv); the arm read it unedited since the act's
# ### base -- now its blob at HEAD, at v1.11.0's commit and in the working tree the same, edited by that commit alone (b724's override, carried)
#⟪OVERRIDE checks MARK 80aa4913de16 1⟫
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % K.C1_STANDING)) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
#⟪END⟫
#⟪OVERRIDE checks MARK 9e6d0f5720f3 1⟫
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell, widened to Edit|Write|NotebookEdit at b753, naming tools/standing/hook.py, unedited this act (its last edit b753`s v1.25.0 at 475a6f38; its blob at v1.26.0`s commit 0c6d9c5c the working tree`s); b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
#⟪END⟫
# ### b754, C4, defect (n) (the Edit tool): the step-zero bank writes each deleted ref's tip as "(was 7d34b587)" (data/b754_stepzero.txt :44-:45),
# ### b753's form "(d784fd66)"; the reader takes either, the tip the group as before
#⟪OVERRIDE checks MARK 6454dd7b4cad 1⟫
    tips = re.findall(r'push-b753-\w+ \((?:was )?([0-9a-f]{7,8})', z)
#⟪END⟫
# ### b754, Component 3 (the Edit tool): b754's step-zero bank rides in the step-zero banks' commit 678338f3 (STEPZERO_BANKS = STEPZERO_BANK_COMMIT);
# ### five push-b753-* refs deleted at step zero (relay three, PLACE-papers two; SIDE-explicit-formula carrying none, data/b754_stepzero.txt :30), each with its tip
#⟪OVERRIDE checks MARK 0b7306236355 1⟫
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b754_stepzero.txt' in files_of(ROOT, K.STEPZERO_BANK_COMMIT) and bool(fd) \
#⟪END⟫
# ### b754, Component 6 (the Edit tool): b754's step-zero bank words the row "THE DELETES, each after its --merged listing" (:15); the
# ### carried needle was b753's wording
#⟪OVERRIDE checks MARK 3938376d9390 1⟫
        and 'THE --MERGED LISTING, PRINTED BEFORE THE DELETES' in z and all(b in z for b in NAMED_PUSH)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's overrides of checks 1516 and 1659 (hook.py edited by b753's v1.4.0) removed -- v1.5.0 left
# ### tools/standing/hook.py unedited (relay 7be1601c's files), so the template's lines (its blob at the act's base) read b754 as it stands
# ### b754, Component 6 (the Edit tool): the corrigendum bank is committed in C1_CORR (step 9), beside the corrigenda row, not in C1_RELAY
#⟪OVERRIDE checks MARK fdd9ef0a58a9 1⟫
        and 'data/b754_corrigendum.txt' in S['files']['corr']
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the corrigendum's events rows (1)-(12), b753's twelve (the template's range is a fifteen-row form)
#⟪OVERRIDE checks MARK bcd4d281b141 1⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 14)) \
#⟪END⟫
# ### b754, Component 4 (the Edit tool): b753's override of checks 1476-1482 (one ERRATA entry at b753's (R363)(5)) removed -- (R364)
# ### orders no ERRATA entry; the template's arm (ERRATA.md byte-equal to its blob at the act's base, no id) reads b754 as it stands
# ### G-BRANCHES-DELETED over b754's two repositories (relay, PLACE-papers) and five refs. b754, Component 4 (the Edit tool, defect
# ### (t')): the needle carried from b753 asked b753's sentence ("KEPT as banked (the tool`s row, tools/standing/carry.py kept b753"); b754's
# ### step zero wrote its kept row in its own words (data/b754_stepzero.txt :96, by a scratch reader after the hook's ENV refusal, defect (a)):
# ### "KEPT as b753's carried list (f) names them, none moved ... 0 moved or absent", port-b707 cb0aea56 among them (:97); read in that wording
#⟪OVERRIDE checks MARK 6381bcfb3cc2 1⟫
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
#⟪END⟫
#⟪OVERRIDE checks MARK 3feae0b5e0b8 1⟫
        and 'port-b707 cb0aea56' in z and "KEPT as b753's carried list (f) names them, none moved" in z and '0 moved or absent' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP
#⟪END⟫
# ### b754, Component 4 (the Edit tool): G-RUNNER-READ's plant on b754's dispatch rows -- run 2's axiom lines carrying sorryAx (b753's
# ### plant read the lv rows' closure log, which b754 does not write)
#⟪OVERRIDE checks MARK 92dcf3918e5c 1⟫
     lambda S: runner_ok(S), lambda S: _mut(S, 'drows', lambda d: d.append(dict(kind='dispatch', item='(4) planted', run=1)))),
#⟪END⟫
# ### b754, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file; b754, Component 6 (the Edit tool): the fold bank was b753's own route
# ### (tools/b753_fold.py); b754's sections were carried at step zero by tools/standing/carry.py, whose diff bank is
# ### data/b754_carry_acts.txt (relay 21681ef9), read here by its head
#⟪OVERRIDE checks MARK 8d42fcd6833e 1 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b753.py -> tools/acts/b754.py' in (rd('b754_carry_acts.txt') or '').split('\n')[0])) \
#⟪END⟫
# ### b754, the Edit tool: v1.9.0's tools/standing/reportdry.py carries the word report and is no report tool; the needle read it as one (the mid probe's LIVE FAIL)
#⟪OVERRIDE checks MARK 70c819b3e902 1 REPAIR (needle)⟫
        and not any('report' in t for t in K.SEALED if t != 'standing/reportdry.py') and 'b754_report.py' not in (S['sealj'].get('tools') or {})
#⟪END⟫
# ### b754, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b754_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks MARK 02e1cbdc95b7 8 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b754_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): the closing's counter line with the repeat count beside it (Component 4 of (R364): the counter
# ### line "CLAIM n, CLOSE m, REPEAT r of t"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing MARK 176194092462 2⟫
    from standing import counter as CNT   # ### v1.22.0, (R352)(2)(iii): the one composer, its set named
    k_ = CNT.compose('b754')
    return '### THE COUNTER ((R364) Component 5, the act`s events and defects together; relay data/b754_defects.txt, data/b754_events.txt): CLAIM %d, CLOSE %d, REPEAT %d OF %d ; THE SET: DEFECTS %d, EVENTS %d, THE LAST %s%s' % (
        k_['claim'], k_['close'], k_['repeat'], k_['total'], k_['defects'], k_['events'], k_['last'], (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b753, carried (the Edit tool): the template's item (b) names an old order list by hand; the act's orders are those orders.py reads open,
# ### entered with the trail, and the trail's open-orders line written from tools/standing/orders.py's output; b754 (defect (d')): the order's
# ### state as b754 leaves it -- the carry from b753 said "as b753 left it ... not touched this act", where b754 built S5c-S5d
#⟪OVERRIDE closing MARK 92495058e2fb 2⟫
    '    (b) The open orders: the trail`s open-orders line written from tools/standing/orders.py`s output, none carried by hand; no order entered this act; W-ORD-MECHANISM-ATTRIBUTION open, its plan passed at b753`s [P1] (relay data/b753_attribution_plan.txt), its build an act the author names, after the sitting;',
    '        W-ORD-LI-ARITH, W-ORD-ZQ-FAMILY, W-ORD-CHAIN-PAGE-LLM-LINE, W-ORD-MECHANISM-TABLE, W-ORD-VISIBILITY, W-ORD-ADMISSIBLE-CONE, W-ORD-DETECTION-DUAL and W-ORD-SIDE-DIAGNOSTIC as they stand.',
#⟪END⟫
# ### b754, Component 4's probe: G-LISTINGS-BEFORE-CLAUSES read no listing -- step zero ran `git -C D:/relay branch -v --merged main --list`
# ### (12:2xZ, before the first delete), and the needle `branch\s+--merged` takes no flag between the two words; widened to flags before --merged
#⟪OVERRIDE checks MARK 50e2a7dc436a 1 REPAIR (needle)⟫
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch(?:\s+-[\w-]+)*\s+--merged', c) is not None)
#⟪END⟫
# ### b754, Component 4's dry composition: v1.27.0's rdn (repair (7)) refuses a missing file, and the record reads three banks the root and the
# ### close write -- the answers bank, the answer check and the events bank -- before they can exist (the entry's dry composition for the touch
# ### read refused on the answers bank; v1.26.0's reader returned '' there, b753's touch read printing "not written at this read"). The three
# ### read optional by name, inserted after line 40's binding; every other bank still refused when missing
#⟪OVERRIDE record MARK f9c2c0f429b0 0 REPAIR (reader)⟫
_rdn_strict = rdn; rdn = lambda name, optional=False: _rdn_strict(name, optional=optional or name in ('b754_author_answers.txt', 'b754_answer_check.txt', 'b754_events.txt'))   # noqa: E731,E702
#⟪END⟫
# ### b754, Component 1 (the Edit tool), tools/standing/ v1.34.0, (R364)(3)(v) and (viii): b753's override of _counter's read (the events
# ### bank optional) retired -- the template's line now carries it, with the post-seal events bank read beside it and a letter of any number
# ### of primes (record.tpl's _counter)
# ### b754, defect (a'), its fourth reader (found at the closing's dry run): the bank's foot read, not its first match -- the seat's row :34 quotes b753's foot
#⟪OVERRIDE closing MARK f8654f00c2e2 1⟫
    head = verdict(cc, r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)')
#⟪END⟫
# ### b754, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b753's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec MARK 0b197e20ec06 1 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b754_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate MARK 082a572c890b 1 REPAIR (fold)⟫
REG = os.path.join(D, 'b754_registration_%s.txt' % __import__('b754_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b754, Component 4 (the Edit tool, before the face): b753's overrides of regspec 45, 68, 78 and 160 (its scratch branch, its ERRATA
# ### entry, its triage's closing lines) are false for b754, whose template lines are right (no scratch branch, no ERRATA, OPEN_TRAILS
# ### written by the trail at the close alone); removed. The Lean-file clause keeps its relabelling: the template measures the port branch
# ### under a kernel-wide label, and b754's Lean files are slot 4's EFLEAN on SIDE-explicit-formula's four branches
#⟪OVERRIDE regspec MARK 93dd78f2e845 1⟫
    ('Lean files written on the port branch', 'LEANFILES', 'LEANFILES', 'files', '### none on port-b707 (N5); MEASURED off the port branch against its tip; the act`s Lean files are slot 4`s EFLEAN.'),
#⟪END⟫
# ### b754, Component 4 (the Edit tool): N1's dispatch commands are the seat's `gh workflow run build-module.yml` ((R364)(4)(iii)-(iv));
# ### the carried pattern named the template's rebuild tool, which b754 does not have
#⟪OVERRIDE record MARK 8470bd7d4f52 2⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)|b754_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b754: the controls' one route (N1)
#⟪END⟫
# ### b754, Component 4 (the Edit tool): G-SCORER-READS-BANKS's needles named b753's banks (the lv rows, v1.4.0's controls, the split's
# ### price), which no b754 scorer reads; the needles set to the banks b754's N1-N4 read (the command bank and the dispatch rows, the
# ### figure banks by their first commits and the five-zero control's bank, the seal and step banks), the ledger exclusion unchanged
#⟪OVERRIDE checks MARK 295ca0b779b3 2 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_dispatch_rows.json' % ACT" in n and 'N2_CONTROLS' in n and '_first_add(' in n \
        and "_explicitformula.txt' % ACT" in n and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b754, (R364)(2)(iii): b753's override of G-DELETES-ONE-BRANCH retired, the template's line reading the kept clause through standing.allow.kept_clause in either wording
# ### b754, Component 7 (the Edit tool), step [5]: the gate banks' route ran the regspec as tools/b754_regspec.py, a file the fold does not
# ### write (the seven tools render from tools/standing/fold/), so the regspec's run bank would hold a "can't open file" error; set to the
# ### fold's own route, `fold.py regspec`
#⟪OVERRIDE record MARK 5077a057931b 1 REPAIR (regspec)⟫
    rc2, t2 = runb([os.path.join(T, 'standing', 'fold.py'), 'regspec'], '%s_regspec_run.txt' % ACT)
#⟪END⟫
# ### b754: b753's override of G-DIFFERS-ERRATA (two ERRATA entries at its sitting) retired; b754 writes no ERRATA entry ((R364)(6)), so
# ### the template's arm, ERRATA at HEAD byte-equal to its blob at the act's base, reads b754 as it stands
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'hk' else 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) of data/b754_defects.txt, the navigator's (h) and (k), the rest the seat's; the primed rows (a')-(j'), the navigator's (f'), (g') and (h') among them, read by the counter, not by this floor
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b754_corrigendum.txt', 'data/b754_standing_v1330.txt', 'data/b754_rules.txt', 'data/b754_registrations.txt', 'data/b754_kernels.txt',
                  'data/b754_branch_map.txt', 'data/b754_head_read.txt', 'data/b754_anchors.txt', 'data/b754_store.txt', 'data/b754_agenda.txt', 'data/b754_waiver.txt',
                  'data/b754_put_1.json', 'data/b754_put_2.json', 'data/b754_author_answers.txt', 'data/b754_line.txt',
                  'data/b754_pathrefusal.txt', 'data/b754_reproduce.txt', 'data/b754_reproduce.json', 'data/b754_address_scan.txt', 'data/b754_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v9 binds b754 whole, unchanged since d9739558, read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R364)(6): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b754_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


def _txt(x):
    """a blob or a file's text as str, bytes decoded as UTF-8, CR dropped; '' for None."""
    if x is None:
        return ''
    if isinstance(x, bytes):
        x = x.decode('utf-8', 'replace')
    return x.replace(chr(13), '')


def _chain():
    """(R364)(1)-(8): the act's relay commits in their order, (key, commit) -- v9, v1.33.0, the corrigendum banks, the registration's rule and
    its table, Component 2's opening commit, each read's last generator commit and its bank's commit, the agenda's generator and its bank, the
    two items, the waiver, the line, the v1.33.0 bank's composer and the bank written again by it (the author's sixth word (4)); read from
    the worklist at the call."""
    c = [('v9', K.STANDING_COMMIT), ('standing', K.C1_STANDING), ('corr', K.C1_CORR), ('rule', K.REG_RULE), ('table', K.REG_TABLE), ('c2first', K.C2_PLAN_FIRST)]
    for n_, gens_, bank_ in K.C2_READS:
        c += [('%s_gen' % n_, gens_[-1]), ('%s_bank' % n_, bank_)]
    c += [('agenda_gen', K.C3_AGENDA[0]), ('agenda', K.C3_AGENDA[1]), ('m1', K.C3_ITEMS[0][1]), ('d1', K.C3_ITEMS[1][1]), ('waiver', K.C3_WAIVER), ('line', K.C4_LINE),
          ('v1330_gen', K.C4_V1330[0]), ('v1330_bank', K.C4_V1330[1])]
    return c


def _anc_pairs():
    """the ancestry pairs of _chain, each commit beside the next; the pair from v9 keeps the name the surgery arm reads."""
    c = _chain()
    return [('v9_v1310', c[0][1], c[1][1])] + [('%s_%s' % (a[0], b[0]), a[1], b[1]) for a, b in zip(c[1:], c[2:])]


def _reads_state():
    """(R364)(5): each read by its name -- the bank in the working tree and its blob at its commit; the generator's first add, its blob at its
    last commit before the bank and at HEAD; the files of each of its commits and of the bank's; their times."""
    out = {}
    for n_, gens_, bank_ in K.C2_READS:
        tool_, data_ = 'tools/b754_%s.py' % n_, 'data/b754_%s.txt' % n_
        out[n_] = dict(bank=rd('b754_%s.txt' % n_), blob=_s(blob(ROOT, '%s:%s' % (bank_, data_))),
                       gen_first=[h_ for h_ in gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', tool_).split() if h_.strip()][-1:],
                       gen_full=gs(ROOT, 'rev-parse', gens_[0]).strip(),
                       gen_at=_s(blob(ROOT, '%s:%s' % (gens_[-1], tool_))), gen_head=_s(blob(ROOT, 'HEAD:' + tool_)),
                       gen_files=[files_of(ROOT, h_) for h_ in gens_], bank_files=files_of(ROOT, bank_),
                       t_gen=[_ct(ROOT, h_) for h_ in gens_], t_bank=_ct(ROOT, bank_))
    return out
#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R364)(1)-(8) (b754's keys over b754's objects): the order by time and ancestry; v1.33.0's controls; the registration at its rule's
        # ### commit and its table's; the five reads, each generator before its bank; the agenda, the rules, the put bank and the answers; the
        # ### waiver's bank; the line bank; zq-b730 and the tag; v8 and v9; the scan
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.REGISTRATIONS))) or None, _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS)) or None),   # ### the box's plan (b753's) at the act's base and at HEAD
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in _anc_pairs()),
        # ### b754 (R364)(1): PLACE-papers by ancestry -- the weight and corrigendum on the act's base, HEAD on them; its commits since the base
        ancpp=dict((k, subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                   for k, a, b in (('pre_c1', K.PRE_PP, K.C1_PP), ('c1_head', K.C1_PP, 'HEAD'))),
        pp_log=[l for l in gs(PP, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_PP).split() if l.strip()],
        v1130=rd('b754_standing_v1330.txt'), v1281=None,
        r363_chain=_chain(),
        r363_regs=rd('b754_registrations.txt'), r363_regs_rule=_s(blob(ROOT, '%s:data/b754_registrations.txt' % K.REG_RULE)),
        r363_regs_table=_s(blob(ROOT, '%s:data/b754_registrations.txt' % K.REG_TABLE)),
        r363_reads=_reads_state(),
        r363_agenda=rd('b754_agenda.txt'), r363_agenda_blob=_s(blob(ROOT, '%s:data/b754_agenda.txt' % K.C3_AGENDA[1])),
        r363_rules_blob=_s(blob(ROOT, '%s:data/b754_rules.txt' % K.C3_ITEMS[1][1])),
        r363_waiver=rd('b754_waiver.txt'), r363_waiver_blob=_s(blob(ROOT, '%s:data/b754_waiver.txt' % K.C3_WAIVER)),
        putj=jl('b754_put_2.json'),
        rows_bank=rd('b754_line.txt'), zanswers=rd('b754_author_answers.txt'),
        sittingj={}, amendj={},   # ### the rules bank bound by the template (checks.tpl :565)
        integ_md5=__import__('hashlib').md5(raw(os.path.join(ROOT, *K.INTEGRATION_DRAFT.split('/'))) or b'').hexdigest(),
        reg_pp=dict((h_, gs(PP, 'show', '--name-only', '--format=', h_).split()) for h_ in (K.C1_PP,)),
        disch_diff=dict((h_, gs(PP, 'show', '--format=', '-U0', h_)) for h_ in (K.C1_PP,)),
        numstat={},
        c3_blobs=dict((p_, _s(blob(ROOT, '%s:%s' % (K.C4_LINE, p_)))) for p_ in ('data/b754_line.txt', 'tools/b754_line.py')),
        pp_head_files=[l for l in gs(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD').split(NL) if l.strip()],
        zq_files=gs(EF, 'diff', '--name-only', K.ZQ_TIP, 'refs/heads/' + K.ZQ_BRANCH).split(),
        zq_log=[l for l in gs(EF, 'rev-list', '--reverse', '%s..refs/heads/%s' % (K.ZQ_TIP, K.ZQ_BRANCH)).split() if l.strip()],
        zq_tags=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()],
        zq_merged=[b_ for b_ in gs(EF, 'branch', '--contains', K.ZQ_FIRST, '--format=%(refname:short)').split() if b_.strip()],
        zq_tag=(gs(EF, 'rev-parse', 'refs/tags/' + K.ZQ_TAG[0]).strip(), gs(EF, 'rev-parse', K.ZQ_TAG[0] + '^{commit}').strip(),
                gs(EF, 'cat-file', '-p', 'refs/tags/' + K.ZQ_TAG[0])),
        ef_tags_entering=sorted(t for t in gs(EF, 'tag', '--points-at', K.ZQ_ENTERING).split(NL) if t.strip()),
        ef_since=[l for l in gs(EF, 'log', '--all', '--format=%H %ct').split(NL) if l.strip() and int(l.split()[1]) >= (_ct(ROOT, K.ACT_CURRENT_COMMIT) or 0)],   # ### any EF commit since the act opened (none: no Lean file written)
        box_src=_s(blob(EF, '%s:SIDEExplicitFormula/Schema/ZetaBox/Box.lean' % K.ZQ_TIP)),
        ef_tips=dict((b_, (gs(EF, 'rev-parse', 'refs/heads/' + b_).strip(), gs(EF, 'rev-parse', 'refs/remotes/origin/' + b_).strip())) for b_, _t in K.EF_BRANCHES),
        drows=json.loads(rd('b754_dispatch_rows.json') or '[]'), reproduce=rd('b754_reproduce.txt'), reproducej=jl('b754_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        v9_pre=_s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V9))), v9_at=_s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))),
        v10=os.path.exists(os.path.join(D, 'standing_clauses_v10.txt')),
        address=rd('b754_address_scan.txt'), addr_live=_addr_live(),
        # ### the standing runner arms read this act's dispatch rows (none); the wave 1 kernels' rebuild-b721 branches as b753 left them
        rebuild=None, rebuild_rows=json.loads(rd('b754_dispatch_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        rebuild_rows_b723=json.loads(rd('b723_axiom_rows.json') or '[]'),   # ### b723's rows
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict([(k_, _ct(ROOT, h_)) for k_, h_ in _chain()] + [('c1', _ct(ROOT, K.C1_RELAY)), ('c1pp', _ct(PP, K.C1_PP)), ('stepzero', _ct(ROOT, K.STEPZERO_BANKS)),
                                                              ('actcur', _ct(ROOT, K.ACT_CURRENT_COMMIT))]),
#⟪END⟫
#⟪SECTION checks 9⟫
                   corr=files_of(ROOT, K.C1_CORR), standing=files_of(ROOT, K.C1_STANDING), rules=files_of(ROOT, K.C1_RULES), c2=files_of(ROOT, K.C2_RELAY),
                   v9=files_of(ROOT, K.STANDING_COMMIT), rule=files_of(ROOT, K.REG_RULE), table=files_of(ROOT, K.REG_TABLE),
                   agenda_gen=files_of(ROOT, K.C3_AGENDA[0]), agenda=files_of(ROOT, K.C3_AGENDA[1]), m1=files_of(ROOT, K.C3_ITEMS[0][1]),
                   d1=files_of(ROOT, K.C3_ITEMS[1][1]), waiver=files_of(ROOT, K.C3_WAIVER), answers=files_of(ROOT, K.C4_ANSWERS) if K.C4_ANSWERS else [],
                   line=files_of(ROOT, K.C4_LINE), c1pp_=files_of(PP, K.C1_PP),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b754's read-first bank's items by path, (R364)'s read-first list in its order (data/b754_readfirst_rows.json); b754 step zero: the
# ### carried b753 needles (R7 refused 20) replaced
READFIRST_NEEDLES = (
    'relay data/b753_closing.txt |',
    'relay data/b753_ferry.txt |',
    'relay data/b753_events.txt |',
    'relay data/b753_events_postseal.txt |',
    'relay data/b753_defects.txt |',
    'relay data/b753_hook_refusals.txt, data/b754_hook_refusals.txt |',
    'relay data/b753_author_answers.txt, data/b753_author_words_preseal.txt |',
    'relay data/b753_rules.txt |',
    'relay data/b753_stepzero.txt |',
    'relay data/b753_dayend.txt |',
    'relay data/b753_arm_seconds.txt |',
    'relay data/b753_agenda.txt |',
    'relay data/b753_registrations.txt |',
    'relay data/b753_kernels.txt |',
    'relay data/b753_branch_map.txt |',
    'relay data/b753_head_read.txt |',
    'relay data/b753_anchors.txt |',
    'relay data/b753_store.txt |',
    'relay data/b753_waiver.txt |',
    'relay data/b753_line.txt |',
    'relay data/b752_corrigendum.txt |',
    'relay data/b752_crossref.txt |',
    'relay data/b752_cq_signature.txt |',
    'relay data/b751_literature.txt |',
    'relay data/b736_sitting.txt, data/b750_sitting.txt |',
    'relay tools/b736_sitting.py |',
    'relay data/b721_frozen_line_drafts.txt |',
    'relay data/b724_split_price.txt |',
    'relay data/b536_components.txt |',
    'relay data/b148_figure_values_dossier.md, data/b428_extract.txt |',
    'relay data/standing_clauses_v9.txt |',
    'relay tools/standing/hook.py |',
    'relay tools/standing/act.py |',
    'relay tools/standing/authorwords.py |',
    'relay tools/standing/delread.py |',
    'relay tools/standing/gitwrite.py |',
    'relay tools/standing/carry.py |',
    'relay tools/act_root.py |',
    'relay tools/b307_handoff_census.py |',
    'relay HANDOFF.md |',
    'relay tools/b633_census.py, tools/b619_census.py, tools/b610_census.py, data/b638_census.txt |',
    'relay tools/mirror_roster.json |',
    'relay tools/standing/roster.py |',
    'relay data/terminal_table.json |',
    'relay reports/2026-08-01-build-2-ly-rep-conditions.md |',
    'PLACE-papers FINDINGS.md |',
    'PLACE-papers REGISTRY.md |',
    'PLACE-papers README.md |',
    'PLACE-papers ERRATA.md |',
    'PLACE-papers INSTRUMENTS.md |',
    'PLACE-papers OPEN_TRAILS.md |',
    'PLACE-papers phase1.5/spectral/THE_EPSTEIN_CONTROL_OBJECT_v0_1.md |',
    'PLACE-papers the census at v0.8.3 |',
    'SIDE-explicit-formula at main 8fbab45d, README.md |',
    'SIDE-kernel at main f8534ef2, README.md |',
    'SIDE-bsd-multiplicity at d77ce309, README.md |',
    'SIDE-trivium at 18a351a1, README.md |',
    'gh the five descriptions |',
)
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R364)(1)-(2))',   # ### the template's heading (closing.tpl :386), not the ferry's numbering
 'REGISTRATION ((R364)(4))', 'READS ((R364)(5))', 'AGENDA, THE HOLD AND THE WAIVER ((R364)(6))', 'LINE (Component 4)', 'NAME AND ADDRESS (N5)', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (226 = 226 + 0, data/b754_citation_check.txt :332), no miss; the
    check HALTED on one Lean-path row (:334), that row read in the step-zero bank (data/b754_stepzero.txt :101-:105, b736's form: the ruling
    cites rQ and cQ beside two paths in order, Schema/EpsteinZQ.lean :59 and Schema/ZQ/LogDeriv.lean :63-:65, the reader pairing every name of
    the clause with the first path, no word of the ruling wrong); the bank written before the step-zero banks' commit and that commit before
    Component 1's."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 226 \
        and '### ### **THE CHECK HALTED** (halts 1: Lean paths and nouns 1, comparatives 0)' in c \
        and '## THE ONE HALT ROW OF THE CITATION CHECK, READ' in (S['stepz'] or '') and 'Schema/EpsteinZQ.lean :59' in (S['stepz'] or '') \
#⟪END⟫
# ### b754, defect (a'): the bank's foot read, not its first match -- the seat's row :34 quotes b753's foot "CITES CHECKED 91 ; OK 90 ; MISSES 1"
#⟪OVERRIDE checks MARK f9d9b85e75e0 1⟫
    m = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', c)
#⟪END⟫
#⟪OVERRIDE checks MARK fd5fb7d1f3b1 1⟫
    mc = re.search(r'(?m)(?<=^### ### \*\*)CITES CHECKED \d+ ; OK \d+ ; MISSES \d+(?=\.\*\*)', S['citation'])
#⟪END⟫
# ### b754, defect (a'), its fifth to seventh readers (found sweeping the templates after the closing's dry run): the record tool's two entry
# ### routes (record.tpl :2667 and :2878, one line twice, each marked by its three-line span) and the spec's MISSES field (regspec.tpl :386)
#⟪OVERRIDE record MARK 02b19df735c8 3⟫
    f = _figs()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE record MARK 1c3af0435e5b 3⟫
    f = _figs_b753()
    n_ans = __import__('standing.act', fromlist=['question_count']).question_count(rdn('%s_author_answers.txt' % ACT))['prompts']   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))
#⟪END⟫
#⟪OVERRIDE regspec MARK 6767229683fc 1⟫
                    MISSES=tfirst('b754_citation_check.txt', r'(?m)^### ### \*\*CITES CHECKED \d+ ; OK \d+ ; MISSES (\d+)\.\*\*'),
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### b753's figures, read at FINDINGS :14910 as Component 1 landed them (b753's closing head quoted)
    return landed(S, 0, ['b753 AT ITS WEIGHT', 'suite 112 of 116', '38eb7652', '36 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### b754's title, the ferry's Component 4 result sentence adjusted to what the act did (the record tool's _title over the banks)
TITLE_NEEDLES = ('## H-C3-LAW, the class-number-3 walk, registered and not run (b754_registrations): 16 rows, 2 controls and 14 tests',
                 '52 kernels reconciled against the lists (b754_kernels)',
                 'the criterion kernel’s 31 branches mapped, 8 off main (b754_branch_map)',
                 '47 front doors’ heads read, 19 not agreeing (b754_head_read)',
                 'the reference layer’s 76 anchors read, 4 moved by a later line (b754_anchors)',
                 'the transcript store read, 45 sessions (b754_store)',
                 '[M1] and [D1] passed',
                 'nothing built')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R364)(1), (7): the generated entry for b753's thirteen events and thirty-six defects landed (its line in the bank, the title at that
    line through conv): the events by row (1)-(13), the defects by the one lettering (a)-(j'); every item tagged CLAIM or CLOSE and NEW or
    REPEAT, the tags summing (CLAIM 11, CLOSE 38 over 49, REPEAT 16; the three entered beside them, the root's answer and the navigator's
    correction among them); the repairs at tools/standing/ v1.33.0 by their controls bank; the corrigenda bank appended at row (73)
    and nothing before it changed; in Component 1's commits (the figures read from data/b754_corrigendum.json as Component 1 landed it)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 36 and len(items) == j.get('items') == 49 and j.get('row') == 73 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 49 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 11 == len(claims) \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 16 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and 'v1.33.0: CONTROLS ' in (S['v1130'] or '') and 'ALL AS WANTED' in (S['v1130'] or '') \
        and len(j.get('notes') or []) == 2 and len(j.get('entered') or []) == 3 \
        and '  (73) ' in S['corrigenda'] and '  (74) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. (R364)(6) orders the rules bank data/b754_rules.txt, one row per item passed on the author's word, two rows (1)-(2), [M1] and [D1]; a rules bank is
#⟪END⟫
#⟪SECTION checks 21⟫
    here first committed at [M1]'s pass (C1_RULES, 0db31ce3) and its second row at [D1]'s (48b8ae2e), in no other commit."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and [int(x_) for x_ in re.findall(r'(?m)^  \((\d+)\) THE ', S['rules'] or '')] == [1, 2] and 'data/b754_rules.txt' in S['files']['rules'] \
        and sorted(gs(ROOT, 'log', '--format=%H', '--', 'data/b754_rules.txt').split()) == sorted(gs(ROOT, 'rev-parse', h_).strip() for _i, h_, _w in K.C3_ITEMS) \
#⟪END⟫
#⟪SECTION checks 23⟫
REPORT_KEYS = ('CERTIFIED -- tools/standing/ v1.33.0', 'REGISTERED -- THE REGISTRATION', 'REGISTERED -- THE KERNELS', 'REGISTERED -- THE BRANCH MAP',
               'REGISTERED -- THE HEAD READ', 'REGISTERED -- THE ANCHORS', 'REGISTERED -- THE STORE READ', 'REGISTERED -- THE AGENDA', 'REGISTERED -- THE INTEGRATION LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, b754: no runner dispatch this act -- no dispatch command in the capture, no dispatch row, the worklist's EF_RUNS empty and
    MAX_DISPATCHES 0; no earlier act's rebuild, axiom or lv route at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    seq_ = [r for r in rows if r.get('kind') in ('dispatch', 'read')]   # ### the wave 1 order above reads no row of this act's: read here over the act's own rows, by run id
    order = not seq_   # ### b754, N1 (b744's form): no dispatch and no read row; the order the carried form read is VACUOUS here
    route = re.compile(r'(?:^|&&\s*|;\s*)gh workflow run\b|b754_controls\.py"? dispatch\b(?![^\n]*\bdry\b)', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*(?:tools/b72[1-4]_(?:rebuild|axiom)|lv724)\.py '
                     r'(push|dispatch|push_run|plan|kcommit|commit|read)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and len([r for r in rows if r.get('kind') == 'dispatch']) == len(K.EF_RUNS) == len(cmds) <= K.MAX_DISPATCHES \
        and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])] \
        or (not rows and not mem and not seq_ and not cmds and not K.EF_RUNS and K.MAX_DISPATCHES == 0
            and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])])   # ### b754, N1 (b744's form): no row, no dispatch, no route; the memory and order reads VACUOUS, the carried form's bool(mem) asking a row this act has none of
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS: the weight line, the corrigendum, the entry; OPEN_TRAILS: the
    trail), the ledgers changed; no rename; no paper written this act."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b754's headings and banks, as its _finding_text writes them
ENTRY_NEEDLES = ('**The corrigendum and the carried items**', '**The registration**', '**The reads**', '**The agenda**', '**The hold and the waiver**',
                 '**The integration line**', '**The order of the act**', '**What this act is not**',
                 '**The research instruments reproduced**', '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b754_corrigendum.txt', 'data/b754_standing_v1330.txt', 'data/b754_rules.txt', 'data/b754_registrations.txt', 'data/b754_kernels.txt',
                 'data/b754_branch_map.txt', 'data/b754_head_read.txt', 'data/b754_anchors.txt', 'data/b754_store.txt', 'data/b754_agenda.txt', 'data/b754_waiver.txt',
                 'data/b754_author_answers.txt', 'data/b754_line.txt',
                 'data/b754_reproduce.txt', 'data/b754_address_scan.txt', 'data/b754_touch.txt',
                 'The act’s counter CLAIM ', 'INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) for the registration, no seat in the cluster table for the refresh`s reads ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) for the registration, none yet for the reads ; stage CLUSTERED (the registration), BANKED (the reads)')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ('h', 'k')   # ### b754: the navigator's unprimed rows of the defects bank, (h) (the subject read's control) and (k) (the count of 46); the primed (f'), (g') and (h') read by the counter; the rest the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R364)(1), N2, N5 (the name the frozen run list carries): the PLACE-papers writes in their order -- the weight and corrigendum in a
    commit touching FINDINGS alone in one hunk, its first two added lines b753 at its weight ("*Appended 2026-11-11 by b754 to b753’s entry")
    and the corrigendum's heading ("## Corrigendum to b753’s record"), removing none, the first PLACE-papers commit of the act on its base;
    no other PLACE-papers write before the record (Components 2-4 write the relay alone), the changed files within FINDINGS and OPEN_TRAILS;
    the plans of b744 unedited at their step-zero md5s; the earlier acts' registrations at HEAD their blobs."""
    import hashlib as _hl
    dd_ = S['disch_diff'] or {}
    a0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('+') and not l.startswith('+++') and l[1:].strip()]
    r0_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('-') and not l.startswith('---')]
    hunks_ = [l for l in (dd_.get(K.C1_PP) or '').split(NL) if l.startswith('@@ ')]
    one_ = len(a0_) >= 2 and len(hunks_) == 1 and a0_[0].startswith('+*Appended 2026-11-11 by b754 to b753’s entry') \
        and a0_[1].startswith('+## Corrigendum to b753’s record') and r0_ == []
    first_ = bool(S['pp_log']) and S['pp_log'][0].startswith(K.C1_PP)
    md_ = bool(K.PLAN_MD5S) and all(_hl.md5(raw(os.path.join(ROOT, *f_.split('/')))).hexdigest() == m_ for f_, m_ in K.PLAN_MD5S.items())
    return bool(one_) and S['reg_pp'].get(K.C1_PP) == ['FINDINGS.md'] and first_ and set(S['pp_head_files']) <= set(K.PP_WRITTEN) and md_ \
        and bool(S['ancpp']) and all(v is True for v in S['ancpp'].values()) \
        and bool(S['reg_blobs']) and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """N5, the scan arm (the name the frozen run list carries): tools/b754_address_scan.py run live over every commit of the act (relay and PLACE-papers;
    fields, messages and added lines), the working trees' added lines and the untracked banks, the previous address, the name and the ORCID held in memory -- the address 0, the author's name 0, the previous name 0, the ORCID 0, its seven controls as wanted; the bank's counts the same; none printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'THE ORCID: 0 ;' in out and 'CONTROLS 7 OF 7 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ; THE ORCID: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R364)(1)-(8), N2 (the name the frozen run list carries): the act's order by time -- step zero's banks, v1.33.0, the weight and
    corrigendum (PLACE-papers, then relay), the registration's rule and then its table, Component 2's opening commit, each read's generator
    and then its bank (the kernels, the branch map, the head read, the anchors, the store), the agenda's generator and its bank, [M1], [D1],
    the waiver's bank, the line, the v1.33.0 bank's composer and then the bank; by ancestry within the relay from v9 through each of them to
    the v1.33.0 bank's commit; the bank's section naming 0f31d31d and 0db31ce3 with the controls run after them."""
    t_ = S['t']
    ks_ = ['stepzero', 'standing', 'c1pp', 'corr'] + [k_ for k_, _h in S['r363_chain'][3:]]
    gb_ = all(t_.get('%s_gen' % n_) and t_.get('%s_bank' % n_) and t_['%s_gen' % n_] < t_['%s_bank' % n_] for n_, _g, _b in K.C2_READS)
    v_ = _txt(S['v1130'])
    later_ = all(('  %s at ' % h_[:8]) in v_ for h_ in K.C1_STANDING_LATER) and '  every such commit before the controls` run: True' in v_ \
        and '  ### ### **ROSTER CONTROLS 10 ; AS WANTED 10 ; ALL AS WANTED True.**' in v_ and _vlast(v_).startswith('v1.33.0: CONTROLS ')
    return len(ks_) == 25 and all(t_.get(k_) for k_ in ks_) and [t_[k_] for k_ in ks_] == sorted(t_[k_] for k_ in ks_) and gb_ and t_['rule'] < t_['table'] \
        and bool(S['anc']) and len(S['anc']) == 23 and all(v is True for v in S['anc'].values()) and later_
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R364)(4)-(5), N2, N3 (the name the frozen run list carries): the registration and the five reads -- the registration bank at HEAD its
    blob at its table's commit (3f865479), the rule's commit (4c86bf24) carrying that bank alone with the rule and no table, the table added
    by the later commit, its foot H-C3-LAW, ROWS 16: CONTROLS 2, TESTS 14, NOT RUN, the candidates carried and NONE REGISTERED; each read's
    bank at HEAD its blob at its own commit (fe935a7e, 2d085231, 8db618bf, 2544839e, 08751eb1), its generator first added by a commit of its
    own before the bank, each generator commit carrying the generator and not the bank, the bank's commit not the generator, the generator at
    HEAD its blob at its last commit before the bank; each foot by its opening figures and CONTROLS ALL AS WANTED."""
    return _c2_ok(S)


# ### the record section's INTEGRATION_LINE, the same bytes (the checks and the record are separate modules; G-COUNT-ROUTE-PRICED reads the line
# ### bank against it, and the record's entry ends with it)
_INTEG_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) for the registration, no seat in the '
               'cluster table for the refresh`s reads ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) for the registration, none yet for the reads ; '
               'stage CLUSTERED (the registration), BANKED (the reads)')


def _iso_epoch(x):
    import datetime as _dt
    try:
        return _dt.datetime.strptime(x[:19], '%Y-%m-%dT%H:%M:%S').replace(tzinfo=_dt.timezone.utc).timestamp()
    except Exception:
        return None


REG_FOOT = 'THE REGISTRATION: H-C3-LAW, THE RULE AT 4c86bf24 BEFORE ITS TABLE ; ROWS 16: CONTROLS 2, TESTS 14 ; '
READ_FEET = dict(kernels='THE KERNELS RECONCILED: 52 REPOSITORIES ; ANSWERED 52 ; FAILED 0 ; ON D: 50 ; ABSENT FROM A LIST 33 ; LOCAL HEAD NOT THE REMOTE MAIN 3 ; ',
                 branch_map='THE CRITERION KERNEL`S BRANCHES MAPPED: 31 ; OFF MAIN 8 (',
                 head_read='THE HEAD READ: 47 DOORS (READMEs read) ; QUOTED 42, NOT AGREEING 19 ; PRIVATE AND NOT QUOTED 5 ; AGREES 23 ; ',
                 anchors='THE REFERENCE LAYER`S ANCHORS READ: 76 ; MOVED BY A LATER LINE 4 ; STANDS 13 ; NO LATER LINE FOUND 59 ; NONE EDITED ; ',
                 store='THE STORE READ: SESSIONS 45 ; THE TOOLS NAME 87 IDS, ABSENT 50, A NEAR TWIN 1 ; ')
ITEMS_ROW = r'(?m)^RESULT \(transcript line \d+, 2026-11-11T17:55:38\.033Z\): Your questions have been answered: "\[M1\] [^\n]*"="Passed", "\[D1\] [^\n]*"="Passed as \(a\)"'


def _c2_ok(S):
    r_ = _txt(S['r363_regs'])
    rule_ = _txt(S['r363_regs_rule'])
    fs_ = S['files']
    rv_ = _vlast(r_)
    reg_ = bool(r_) and r_ == _txt(S['r363_regs_table']) and fs_['rule'] == ['data/b754_registrations.txt'] and 'data/b754_registrations.txt' in fs_['table'] \
        and '## (1) THE RULE' in rule_ and '## (2) THE TABLE' not in rule_ and '## (2) THE TABLE' in r_ \
        and rv_.startswith(REG_FOOT) and ' ; NOT RUN ; ' in rv_ and rv_.endswith('NONE REGISTERED.') and S['anc'].get('rule_table') is True
    reads_ = S['r363_reads'] or {}
    ok_ = []
    for n_, gens_, _bank in K.C2_READS:
        d_ = reads_.get(n_) or {}
        b_ = _txt(d_.get('bank'))
        v_ = _vlast(b_)
        tool_, data_ = 'tools/b754_%s.py' % n_, 'data/b754_%s.txt' % n_
        gf_, bf_, tg_ = d_.get('gen_files') or [[]], d_.get('bank_files') or [], d_.get('t_gen') or [None]
        ok_.append(bool(b_) and b_ == _txt(d_.get('blob')) and bool(d_.get('gen_first')) and d_['gen_first'][0] == d_.get('gen_full')
                   and bool(d_.get('gen_at')) and d_['gen_at'] == d_.get('gen_head') and len(gf_) == len(gens_)
                   and all(tool_ in f_ and data_ not in f_ for f_ in gf_) and data_ in bf_ and tool_ not in bf_
                   and all(tg_) and bool(d_.get('t_bank')) and max(tg_) < d_['t_bank']
                   and v_.startswith(READ_FEET[n_]) and v_.endswith('CONTROLS ALL AS WANTED.'))
    return bool(reg_) and len(ok_) == 5 and all(ok_)
#⟪END⟫
#⟪SECTION checks 35⟫
    """N5, (R364)(6) (the name the frozen run list carries): no kernel's main touched and no Lean file written -- SIDE-explicit-formula's
    main at the worklist's EF_MAIN (8fbab45d, as b753 left it), the four branches each at the worklist's tip locally and at origin, zq-b730
    at b753's tip 1e658870 with nothing past it; no commit on any of its refs since the act opened; the one tag v0.38, its object the
    worklist's and its peel 14ca5725, the only tag at that commit and no tag added this act; no sitting kernel."""
    tp = S['ef_tips'] or {}
    zt = S['zq_tag'] or ('', '', '')
    return S['ef_main'] == K.EF_MAIN == K.EF_BASE and bool(K.EF_BRANCHES) and all(tp.get(b, ('', ''))[0] == h == tp.get(b, ('', ''))[1] for b, h in K.EF_BRANCHES) \
        and S['zq_files'] == [] and S['zq_log'] == [] and K.ZQ_TIP == K.ZQ_ENTERING and S['ef_since'] == [] and K.ZQ_COMMITS == () and K.ZQ_FILES == () \
        and zt[0] == K.ZQ_TAG[1] and zt[1] == K.ZQ_TAG[2] and ('object %s' % K.ZQ_TAG[2]) in (zt[2] or '') \
        and S['ef_tags_entering'] == [] and 'v0.38' in S['zq_tags'] and not [t_ for t_ in S['zq_tags'] if re.match(r'^v0\.(39|[4-9]\d)', t_)] and not K.SITTING_TIPS

def _vlast(t):
    """a bank's LAST verdict line, the `### ### **` prefix and the closing `**` cut."""
    ls = [l.rstrip() for l in (t or '').split(NL) if l.startswith('### ### **')]
    return ls[-1][len('### ### **'):].rstrip('*') if ls else ''
#⟪END⟫
#⟪SECTION checks 36⟫
    """the name the frozen run list carries: standing clauses v9 binding the act whole as b723 landed it -- the working tree's text its blob at
    STANDING_COMMIT and at the act's base, VERSION 9; v8 at HEAD its blob at the act's base; no v10 written; v9's commit an ancestor of v1.33.0's."""
    v9 = S['v9'] or ''
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and bool(S['v9_at']) and v9 == S['v9_at'] == S['v9_pre'] \
        and S['v10'] is False and S['files']['v9'] == [K.DATA_STANDING_V9] \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v1310') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """no arm retired through tools/standing/arms.py this act -- its RETIRED as v1.16.0 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED out of the
    arm list since b753's v1.3.0; this suite's run list 116 arms, no standing arm added."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R364)(6), Component 4, N2, N3, N5 (the name the frozen run list carries): the agenda, the two items and their answers, the waiver's
    bank and the line -- the agenda bank at HEAD its blob at 9b95fa00, its generator's commit before it and both before either item, its foot
    2 ITEMS, the roster 75 -> 82, three forms; the rules bank at HEAD its blob at [D1]'s commit, its two rows carrying the author's words
    "Passed" and "Passed as (a)"; the put bank naming [M1] and [D1]; the answers bank written by the record tool's appending route (its head
    the route's, the two prompts with their options and the RESULT row with its time and both answers), committed with its json at the
    worklist's C4_ANSWERS, at HEAD its blob there or that blob with lines appended (never rewritten); [M1]'s commit carrying the rules bank
    and the list of the seven, [D1]'s the rules bank; the waiver's bank at HEAD its blob at 576255e0, its foot the counts with NO WORD OF ANY
    ROW PRINTED; the line bank's foot COMPOSED WITH THE MATCH, STAGE CLUSTERED/BANKED, MATCHED 0 OF 6, ALL AS READ, its line the act module's
    INTEGRATION line, committed with its tool at 98bb4ae2; b746's draft unchanged; no Zenodo tool this act."""
    r_ = S['rows_bank'] or ''
    v_ = _vlast(r_)
    a_ = _txt(S['zanswers'])
    a3_ = _txt(blob(ROOT, '%s:data/b754_author_answers.txt' % K.C4_ANSWERS)) if K.C4_ANSWERS else ''
    row_ = re.search(ITEMS_ROW, a_)
    ag_ = _txt(S['r363_agenda'])
    av_ = _vlast(ag_)
    ru_ = _txt(S['rules'])
    ru1_ = ' '.join(ru_.split())
    wv_ = _txt(S['r363_waiver'])
    wvv_ = _vlast(wv_)
    t_ = S['t']
    zt_ = sorted(f_ for f_ in os.listdir(T) if f_.startswith('b754_') and f_.endswith('.py') and 'zenodo.org' in (read(os.path.join(T, f_)) or ''))
    return a_.startswith('### b754 -- THE AUTHOR`S ANSWERS') and bool(a3_) and a_.startswith(a3_) and row_ is not None \
        and '  OPTION 1: Passed ::' in a_ and '  OPTION 2: Struck ::' in a_ and '  OPTION 1: Passed as (a) ::' in a_ \
        and bool(ag_) and ag_ == _txt(S['r363_agenda_blob']) \
        and av_.startswith('THE AGENDA: 2 ITEMS, [M1] AND [D1] ; [M1] DRAFTS 7 FAMILIES, THE ROSTER 75 -> 82 ; [D1] DRAFTS 3 FORMS ;') \
        and all(t_.get(k_) for k_ in ('agenda_gen', 'agenda', 'm1', 'd1')) and t_['agenda_gen'] < t_['agenda'] < t_['m1'] < t_['d1'] \
        and bool(ru_) and ru_ == _txt(S['r363_rules_blob']) and 'at item [M1] of (R364)(6), 2026-11-11: "Passed".' in ru1_ \
        and 'at item [D1] of (R364)(6), 2026-11-11: "Passed as (a)".' in ru1_ \
        and all(w_ in json.dumps(S['putj'] or {}, ensure_ascii=False) for w_ in ('[M1]', '[D1]')) \
        and {'data/b754_rules.txt', 'tools/mirror_roster_added.json'} <= set(S['files']['m1']) and 'data/b754_rules.txt' in S['files']['d1'] \
        and {'data/b754_author_answers.txt', 'data/b754_author_answers.json'} <= set(S['files']['answers']) \
        and bool(wv_) and wv_ == _txt(S['r363_waiver_blob']) and wvv_.startswith('THE WAIVER`S BANK: ANCHORS 76 (A 13, B 17, C 18, D 7, E 21) ;') \
        and wvv_.endswith('NO WORD OF ANY ROW PRINTED.') \
        and {'data/b754_line.txt', 'tools/b754_line.py'} <= set(S['files']['line']) \
        and v_.startswith('THE LINE: COMPOSED ; FROM REGISTRY 1.5c-21 TO 1.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE THE_EPSTEIN_CONTROL_OBJECT_v0_1 ; STAGE CLUSTERED/BANKED ; MATCHED 0 OF 6 ;') \
        and v_.endswith('; ALL AS READ.') and ('      %s' % _INTEG_LINE) in r_ \
        and S['integ_md5'] == K.INTEGRATION_DRAFT_MD5 and zt_ == []

def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b729's (R339)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at the act's base (unchanged this act) and the working tree's."""
    j = S['reproducej'] or {}
    R = j.get('rows') or []
    ids = ['I-%d' % i for i in range(41, 109)]
    run = [r for r in R if r.get('grade') in ('REPRODUCES', 'DIFFERS')]
    nr = [r for r in R if r.get('grade') == 'NOT RUN']
    c = dict((g, sum(1 for r in R if r.get('grade') == g)) for g in ('REPRODUCES', 'DIFFERS', 'NOT RUN'))
    f = re.search(r'ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;', _verdict(S['reproduce']))
    tool = 'tools/research/reproduce.py'
    src = _s(blob(ROOT, 'HEAD:' + tool))
    return bool(R) and [r.get('id') for r in R] == ids and len(run) + len(nr) == len(R) \
        and all(str(r.get('planted_as_wanted')) == 'True' and r.get('planted_grade') == 'DIFFERS' for r in run) \
        and all(re.match(r'(MORE THAN 60 s|A DISPATCH|A NETWORK READ): ', r.get('why') or '') and 'priced' in (r.get('why') or '') for r in nr) \
        and j.get('counts') == c and bool(f) and [int(x) for x in f.groups()] == [len(R), c['REPRODUCES'], c['DIFFERS'], c['NOT RUN'], len(run), len(run)] \
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (PRE['relay'], tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')
#⟪END⟫
#⟪SECTION checks 41⟫
    """standing clauses v9 (Component 7 of (R364): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b754_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b753's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R364-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### (carried from b753's Component 8, the Edit tool): the carried `7 in named` read nothing; v7 is read by its bytes below and v9 by
    # ### G-SURGERY-CARRIED
    return 'RULING (R364) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from f4ab9491',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b753's standing arm, carried in the run list of 116
    ('G-RESEARCH-REPRODUCES', '(R363)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool unchanged from the act`s base 0e855242',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 226 = 226 OK + 0 misses, the check HALTED on one Lean-path row (rQ and cQ cited beside two paths in order, the reader pairing every name with the first path) read in the step-zero bank (b736`s form); the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', re.sub(r'(push-b753-\w+) \((?:was )?[0-9a-f]{7,8}\)', r'\1', S['stepz']))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects, the ferry`s Component 4 result sentence adjusted to what the act did: H-C3-LAW registered and not run, 16 rows, 2 controls and 14 tests; 52 kernels reconciled; the criterion kernel`s 31 branches mapped, 8 off main; 47 front doors` heads read, 19 not agreeing; 76 anchors read, 4 moved by a later line; the transcript store read, 45 sessions; [M1] and [D1] passed; the controls landed; nothing built; each finding`s name in the heading for the line reader',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R364)(1), (7): the generated corrigendum for b753`s record, landed at FINDINGS :14912: its thirteen events and thirty-six defects, 49 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 11 CLOSE 38, REPEAT 16, with the three entered beside them; v1.33.0`s repairs by data/b754_standing_v1330.txt; the corrigenda bank appended at row (73)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); (R364)(6)`s rules bank data/b754_rules.txt, two rows (1)-(2), committed at [M1]`s pass (0db31ce3) and [D1]`s (48b8ae2e) alone',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b754's objects
    ('G-REGISTRATIONS-FIRST', '(R364)(1), N2, N5: the weight line and the corrigendum in a PLACE-papers commit touching FINDINGS alone (80bf12c7), one hunk, none removed, the act`s first PLACE-papers commit; no other PLACE-papers write before the record, the changed files within FINDINGS and OPEN_TRAILS; b744`s plans at their md5s; the earlier registrations their blobs',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'pp_head_files', lambda d: d.append('REGISTRY.md'))),
    ('G-PREDICTION-FIRST', 'N5, the scan arm: tools/b754_address_scan.py run live over every commit of the act in the relay and PLACE-papers, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, the ORCID 0, seven controls as wanted; none printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R364)(1)-(8), N2: the act`s order by time -- step zero, v1.33.0, the weight and corrigendum, the registration`s rule then its table, each read`s generator then its bank, the agenda, [M1], [D1], the waiver`s bank, the line, the v1.33.0 bank`s composer then the bank naming 0f31d31d and 0db31ce3 with the controls run after them -- and by ancestry within the relay',
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(rule_table=False))),
    ('G-DERIVATION-GRADED', '(R364)(4)-(5), N2, N3: the registration at HEAD its blob at its table`s commit 3f865479, the rule alone at 4c86bf24 before the table, its foot H-C3-LAW, 16 rows, 2 controls and 14 tests, NOT RUN, none of the candidates registered; each of the five reads at HEAD its blob at its commit (fe935a7e, 2d085231, 8db618bf, 2544839e, 08751eb1), its generator first added by a commit of its own before the bank and unchanged since its last commit before it; each foot by its figures and CONTROLS ALL AS WANTED',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'r363_regs', (S['r363_regs'] or '').replace(' ; NOT RUN ; ', ' ; RUN ; '))),
    ('G-OFFSET-POST-HOC', 'N5, (R364)(10): no kernel`s main touched and no Lean file written -- SIDE-explicit-formula`s main at 8fbab45d, the four branches at the worklist`s tips locally and at origin, zq-b730 at 1e658870 with nothing past it, no commit on any ref since the act opened; the one tag v0.38, peel 14ca5725, no tag beyond it',
     lambda S: offset_post_hoc_ok(S), lambda S: _mut(S, 'zq_files', lambda d: d.append('SIDEExplicitFormula/Planted.lean'))),
    ('G-SURGERY-CARRIED', 'standing clauses v9 binding the act whole as b723 landed it: the text its blob at d9739558 and at the act`s base, VERSION 9; v8 at HEAD its blob at the base; no v10; v9`s commit an ancestor of v1.33.0`s',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', 'no arm retired through tools/standing/arms.py this act -- its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list since v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R364)(6), Component 4, N2, N3, N5: the agenda bank its blob at 9b95fa00, before either item; the rules bank`s two rows carrying the author`s words Passed and Passed as (a); the put bank naming [M1] and [D1]; the answers bank by the record tool`s appending route, the two prompts with their options and their RESULT at 2026-11-11T17:55:38.033Z, at HEAD its blob at the worklist`s C4_ANSWERS with lines appended alone; the waiver`s bank its blob at 576255e0, no word of any row printed; the line bank COMPOSED WITH THE MATCH, stage CLUSTERED/BANKED, 0 of 6 matched, ALL AS READ, its line the module`s, with its tool at 98bb4ae2; b746`s draft at its md5; no Zenodo tool',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'zanswers', (S['zanswers'] or '').replace('"="Passed as (a)"', '"="Struck"'))),
    ('G-DIFFERS-ERRATA', '(R364)(1), (10): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md at HEAD its base`s bytes; no differs or errata bank; the weight line and the corrigendum in 80bf12c7, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9, N4: data/b754_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R364-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b753`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at fe2150b3 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1: no runner dispatch this act -- MAX_DISPATCHES 0, the worklist`s runs none, no dispatch row; the plant a dispatch with no read refused',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: no dispatch command in the capture, no dispatch row, the worklist`s runs none; no b721-b724 rebuild or axiom route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag beyond v0.38 this act: each repaired wave 1 kernel`s rebuild-b721 as b753 left it, beyond its pin by b723`s axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at 8fbab45d as b753 left it and v0.37 unmoved; SIDE-lv-conservation`s deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the act`s list (FINDINGS and OPEN_TRAILS, (R364)(1), (7), (10)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b753`s trail record on OPEN_TRAILS (:18232) and its root in the chain', lambda S: '### b753 — lane two, act one hundred and eighty, the system refresh under (R363)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b712`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: none; -1 the command bank not yet written)' % (
#⟪END⟫
# ### (carried; b754 moves no main): a main at a sitting tip, its tags unmoved, is not a move against b753's face
#⟪OVERRIDE record MARK 8aa097f94edc 1⟫
    moved = [k for k, v in prev.items() if k in now and (now[k][0] != v[0] or now[k][1] != v[1]) and not (K.SITTING_TIPS.get(k, '').startswith(now[k][0]) and now[k][1] == v[1])]
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### b754: (R364)'s rows, written at step zero over b753's carried rows (scratch splice754.py); each needle read from the line it names
    # ### before the row was written (scratch cites754.py, cites754b.py); (1)'s line read from the public relay at 34332a00. Lines under
    # ### [Q]'s row (3) are cited by path, line and digest and not quoted: their rows print digests alone.
    import hashlib as _h
    pub = _blob('D:/relay', '34332a00', 'data/b753_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'data/b753_closing.txt :1, the head line as the public relay carries it at 34332a00', bool(pub) and pub[0] == at(cl, 1) and 'relay feaae42a' in pub[0] and 'PLACE-papers 04fef04' in pub[0],
        'remote main %s' % rm[:8], '1')
    add('ruling (1)', 'relay remote main read back at 34332a00 after b753`s closing push and its step-row commit', rm.startswith('34332a00'), rm[:8], '1')
    for w_ in ('suite 110 of 116', 'root 696aa4eb0dc87fdf', '8 prompts answered', 'scores 6 of 8 HELD', '52 defects'):
        add('ruling (1)', 'data/b753_closing.txt :1 carries %s' % w_, w_ in at(cl, 1), at(cl, 1)[:60], '1')
    add('ruling (1)', 'relay main and PLACE-papers main at the act`s start, 34332a00 and 04fef04e', gr('D:/relay', 'rev-parse', K.PRE_RELAY).startswith('34332a00') and gr(PP, 'rev-parse', K.PRE_PP).startswith('04fef04e'), '%s ; %s' % (K.PRE_RELAY[:8], K.PRE_PP[:8]), '1')
    for f_, n_, ws_ in (('data/b753_corrigendum.txt', 100, ('ITEMS 49: EVENTS 13, DEFECTS 36', 'WITH THE 3 ENTERED 52', 'THE ENTRY AT FINDINGS :14912')),
                        ('data/b753_standing_v1330.txt', 128, ('v1.33.0: CONTROLS', 'CASES 16 ; AS WANTED 16')),
                        ('data/b753_registrations.txt', 88, ('H-C3-LAW, THE RULE AT 4c86bf24 BEFORE ITS TABLE', 'ROWS 16: CONTROLS 2, TESTS 14', 'NOT RUN')),
                        ('data/b753_kernels.txt', 95, ('52 REPOSITORIES', 'ABSENT FROM A LIST 33')),
                        ('data/b753_branch_map.txt', 394, ('MAPPED: 31', '11 OF 11')),
                        ('data/b753_head_read.txt', 248, ('47 DOORS', 'NOT AGREEING 19')),
                        ('data/b753_anchors.txt', 413, ('ANCHORS READ: 76', 'MOVED BY A LATER LINE 4')),
                        ('data/b753_store.txt', 583, ('THE STORE READ: SESSIONS 45',)),
                        ('data/b753_line.txt', 77, ('STAGE CLUSTERED/BANKED',)),
                        ('data/b753_closing.txt', 434, ('pre-push : ARMS RUN : 116', 'LIVE PASSING : 110', 'LIVE FAILING : 5')),
                        ('data/b753_closing.txt', 436, ('post-push : ARMS RUN : 116', 'LIVE PASSING : 110', 'LIVE FAILING : 5')),
                        ('data/b753_closing.txt', 242, ('15:44:02',)),
                        ('data/b753_dayend.txt', 71, ('14.88 h',)),
                        ('data/b753_dayend.txt', 73, ('10.01 h against 2.7-5.4 h',)),
                        ('data/b753_dayend.txt', 53, ('5.31 h',)),
                        ('data/b753_dayend.txt', 62, ('4.70 h',)),
                        ('data/b753_stepzero.txt', 14, ('2114 lines, 520 changed',))):
        L_ = lines_of(p(*f_.split('/')))
        add('ruling (1), (5)[U]', '%s :%d, %s' % (f_, n_, ' ; '.join(ws_)), all(w_ in at(L_, n_) for w_ in ws_), at(L_, n_)[:60], '1')
    as_ = at(lines_of(p('data', 'b753_arm_seconds.txt')), 93)
    sec_ = [int(x_) for x_ in re.findall(r' (\d+) s\b', as_)]
    add('ruling (5)[U]', 'data/b753_arm_seconds.txt :93, the suite`s ten parts, 3,114 seconds a pass (the parts summed)', sum(sec_) == 3114 and len(sec_) == 10, '%d s over %d parts' % (sum(sec_), len(sec_)), '1')
    # ### (R364)(2): the navigator's corrections, each line read at HEAD
    ev1_ = lines_of(p('data', 'b753_events.txt'))
    add('ruling (2)(i)', 'data/b753_events.txt (8), the navigator`s, by the author`s word of 2026-11-12T00:30:51Z', at(ev1_, 126).startswith("    (8) THE NAVIGATOR'S [CLOSE ; REPEAT b730 (w)]")
        and any('00:30:51' in at(ev1_, n_) for n_ in range(126, 134)), at(ev1_, 126)[:60], '1')
    df_ = lines_of(p('data', 'b753_defects.txt'))
    lt_ = [(m_.group(1), m_.group(2), m_.group(3)) for m_ in (re.match(r"^    \(([a-z]'?)\) (THE [A-Z']+) \[([^\]]*)\]", l_) for l_ in df_) if m_]
    nv_ = [x_[0] for x_ in lt_ if x_[1] == "THE NAVIGATOR'S"]
    add('ruling (2)(i), (3)', 'data/b753_defects.txt: 52 lettered (a)-(z`), CLAIM 16 and CLOSE 36; the navigator`s six, (h), (k), (f`), (g`), (h`), (m`)',
        len(lt_) == 52 and nv_ == ['h', 'k', "f'", "g'", "h'", "m'"] and sum(1 for x_ in lt_ if x_[2].startswith('CLAIM')) == 16, 'letters %d ; the navigator`s %s' % (len(lt_), ' '.join(nv_)), '1')
    for n_, nd_ in ((10858, '## The coefficient law derived to the step named'), (11072, '## The coefficient law at -35 and -40'), (11178, '## The C2 table’s rule chose no discriminant'),
                    (11359, '## The class-number-2 table at its fourteen remaining fields'), (11755, '## H-ONSET-MASS at 1 of 3 zeros REFUTED')):
        add('ruling (2)(ii), (5)[R1], [L13], ferry (read first)', 'FINDINGS.md :%d, %s' % (n_, nd_.lstrip('# ')[:50]), at(fi, n_).startswith(nd_), at(fi, n_)[:60], '1')
    c13_, c19_ = lines_of(p('data', 'b713_coeffs.txt')), lines_of(p('data', 'b719_coeffs.txt'))
    add('ruling (2)(ii)', 'data/b713_coeffs.txt :13-:14, the least negative index 24 at -15, 756 negative', 'THE LEAST n WITH c(n) < 0: n = 24' in at(c13_, 13) and 'NEGATIVE COEFFICIENTS through 32532: 756' in at(c13_, 14), at(c13_, 13)[:60], '1')
    add('ruling (2)(ii)', 'data/b719_coeffs.txt :11, (C3) -15: the least negative n = 24', at(c19_, 11).startswith('### (C3) -15') and 'the least negative n = 24' in at(c19_, 11), at(c19_, 11)[:60], '1')
    for f_ in ('data/b721_derivation.txt', 'data/b725_interference.txt', 'data/b752_cq_signature.txt', 'reports/2026-08-01-build-2-ly-rep-conditions.md'):
        add('ruling (2)(ii)-(iii)', '%s tracked at 34332a00' % f_, bool(_blob('D:/relay', '34332a00', f_)), '%d lines' % len(_blob('D:/relay', '34332a00', f_).split(NL)), '1')
    rp_ = lines_of(p('reports', '2026-08-01-build-2-ly-rep-conditions.md'))
    add('ruling (2)(iii)', 'reports/2026-08-01-build-2-ly-rep-conditions.md :14-:17, the cumulant conditions cited to Newman 1976', '**Higher even-cumulant negativity**' in at(rp_, 14) and 'Newman 1976' in at(rp_, 17), at(rp_, 17)[:60], '1')
    # ### (R364)(3): the corrigendum's inputs and the opening components' cites
    ps1_ = lines_of(p('data', 'b753_events_postseal.txt'))
    evs_ = [int(m_.group(1)) for m_ in (re.match(r'^    \((\d+)\) ', l_) for l_ in ev1_) if m_]
    eps_ = [int(m_.group(1)) for m_ in (re.match(r'^    \((\d+)\) ', l_) for l_ in ps1_) if m_]
    add('ruling (3)', 'b753`s nine events (data/b753_events.txt (1)-(9)) and the post-seal events (10)-(14) (data/b753_events_postseal.txt)', evs_ == list(range(1, 10)) and eps_ == list(range(10, 15)),
        'events %s ; post-seal %s' % (evs_[-1:], eps_), '1')
    hr_ = lines_of(p('data', 'b753_hook_refusals.txt'))
    add('ruling (3)', 'data/b753_hook_refusals.txt :39, the refusal of 05:12:49Z (SED)', at(hr_, 39).startswith('2026-11-12T05:12:49Z | SED |'), at(hr_, 39)[:30], '1')
    add('ruling (3)(xiii)', 'data/b753_hook_refusals.txt :30, the commit refused at 20:35:41Z (LIMIT)', at(hr_, 30).startswith('2026-11-11T20:35:41Z | LIMIT |'), at(hr_, 30)[:30], '1')
    h4_ = lines_of(p('data', 'b754_hook_refusals.txt'))
    add('ruling (3), ferry (read first)', 'data/b754_hook_refusals.txt :1, the refusal the hook sent there after b753`s close (05:25:25Z, REDIR)', at(h4_, 1).startswith('2026-11-12T05:25:25Z | REDIR |'), at(h4_, 1)[:30], '1')
    add('ruling (3)', 'OPEN_TRAILS.md :18258, the standing line: the classes repeating three acts running, REPEAT 32 of 61', 'three acts' in at(ot, 18258) and 'REPEAT 32 of 61' in at(ot, 18258), at(ot, 18258)[:60], '1')
    hk_ = lines_of(p('tools', 'standing', 'hook.py'))
    nk_ = sum(1 for l_ in hk_[61:88] if re.match(r"^    '[A-Z]+': ", l_))
    add('ruling (3)(i), (xv), ferry (read first)', 'tools/standing/hook.py :61-:89 the table of kinds (21 by the navigator`s count); :282 the calls ledger and :306 the git-write state under the temp directory',
        at(hk_, 61) == 'ROWS = {' and at(hk_, 89) == '}' and 'tempfile.gettempdir()' in at(hk_, 282) and 'tempfile.gettempdir()' in at(hk_, 306) and nk_ == 21, '%d kinds' % nk_, '1')
    c752_ = lines_of(p('data', 'b752_corrigendum.txt'))
    add('ruling (3)(v), ferry (read first)', 'data/b752_corrigendum.txt :68, the refusal of 21:20:10Z', '**the refusal of 21:20:10Z**' in at(c752_, 68), at(c752_, 68)[:60], '1')
    add('ruling (3)(vi)', 'b753`s commits 0f31d31d and 0db31ce3 in the relay', all(gr('D:/relay', 'cat-file', '-t', c_) == 'commit' for c_ in ('0f31d31d', '0db31ce3')), 'both commits', '1')
    add('ruling (3), ferry (read first)', 'data/standing_clauses_v9.txt (83), the repeat rule', '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'present', '1')
    # ### (R364)(4): the reads' sources
    add('ruling (4)(ii)', 'FINDINGS.md :762, the reference layer`s head', at(fi, 762) == '## I. Numerical & Empirical Findings', at(fi, 762)[:40], '2')
    add('ruling (4)(ii), ferry (read first)', 'data/terminal_table.json tracked at 34332a00', bool(_blob('D:/relay', '34332a00', 'data/terminal_table.json')), 'present', '2')
    # ### (R364)(5): the sitting's CURRENT, each line read at HEAD or at the kernel's commit
    for n_, nd_ in ((896, '### conservation-of-spectra'), (897, '**∏_v |x|_v = 1 is s-dark.**'), (900, '### riemann-hypothesis'), (901, '**RH proved (two-leg, honestly scoped).**'),
                    (904, '### simplicity-riemann-zeros'), (905, '**All zeros of ξ(s) are simple.**'), (978, '### two-leg-completeness'), (979, '**The proof of RH is complete in the two-leg sense.**'),
                    (1084, '## How findings move'), (5924, '> / Conservation frame'), (5938, '> / §2 Conservation of Spectra seals the system'), (5942, '**The relation.**'),
                    (6880, '## CP-7, act seventeen: the edition of SIMPLICITY_OF_RIEMANN_ZEROS'), (14747, '## THE_EPSTEIN_CONTROL_OBJECT §5 passed'), (14910, '*Appended 2026-11-11 by b753 to b752’s entry'),
                    (14912, '## Corrigendum to b752’s record'), (15009, '## H-C3-LAW, the class-number-3 walk, registered and not run')):
        add('ruling (5)[A], (1), ferry (read first)', 'FINDINGS.md :%d, %s' % (n_, nd_.strip('#*> ')[:50]), at(fi, n_).startswith(nd_), at(fi, n_)[:60], '3')
    add('ruling (5)[A], ferry (read first)', 'FINDINGS.md :1086 and :1094, the layer`s two forms: edited in place, RETIRED with its reason', 'edit the entry' in at(fi, 1086) and 'RETIRED' in at(fi, 1094), 'read', '3')
    add('ruling (5)[Q](3), ferry (read first)', 'FINDINGS.md :820-:826, by line alone (their digests)', len(fi) >= 826, ' '.join(_h.sha256(at(fi, n_).encode('utf-8')).hexdigest()[:8] for n_ in range(820, 827)), '3')
    rg_ = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (5)[A2], ferry (read first)', 'REGISTRY.md :153, :188, :208, "two-leg" reworded on 2026-07-23', all('two-leg' in at(rg_, n_) and '2026-07-23' in at(rg_, n_) for n_ in (153, 188, 208)), 'read', '3')
    add('ruling (5)[A2], ferry (read first)', 'REGISTRY.md :492-:496, the rows of 2026-07-23', all(at(rg_, n_).startswith('| 2026-07-23 |') for n_ in range(492, 497)), 'read', '3')
    add('ruling (5)[A], ferry (read first)', 'REGISTRY.md :951 and :953, THE CEILING LINE under (R145)(2) and (R146)(2)', at(rg_, 951).startswith('**THE CEILING LINE, `(R145)`(2)') and at(rg_, 953).startswith('**THE CEILING LINE, `(R146)`(2)'), at(rg_, 953)[:40], '3')
    add('ruling (5)[A], ferry (read first)', 'REGISTRY.md :965, the note of (R284)(3) in the ceiling block', at(rg_, 965).startswith("*(Appended under the author's ruling `(R284)`(3)"), at(rg_, 965)[:40], '3')
    add('ruling (5)[Q](3), ferry (read first)', 'REGISTRY.md :373, by line alone (its digest)', len(rg_) >= 373, _h.sha256(at(rg_, 373).encode('utf-8')).hexdigest()[:16], '3')
    for f_, ns_ in (('data/b148_figure_values_dossier.md', (101, 103, 113)), ('data/b428_extract.txt', (266,))):
        L_ = lines_of(p(*f_.split('/')))
        add('ruling (5)[Q](3), ferry (read first)', '%s :%s, by line alone (their digests)' % (f_, ', :'.join(str(n_) for n_ in ns_)), len(L_) >= max(ns_), ' '.join(_h.sha256(at(L_, n_).encode('utf-8')).hexdigest()[:8] for n_ in ns_), '3')
    rd_ = lines_of(os.path.join(PP, 'README.md'))
    add('ruling (5)[A1], [A4], ferry (read first)', 'README.md :104, What is claimed and what is not; :135, *simplicity proved* among the sentences not supportable', at(rd_, 104) == '### What is claimed and what is not' and 'simplicity proved' in at(rd_, 135), at(rd_, 104)[:40], '3')
    er_ = lines_of(os.path.join(PP, 'ERRATA.md'))
    add('ruling (5)[A], ferry (read first)', 'ERRATA.md :486, E-2026-09-25-1; :664, the conservation_of_spectra replacement', at(er_, 486).startswith('## E-2026-09-25-1') and 'conservation_of_spectra' in at(er_, 664), at(er_, 486)[:40], '3')
    add('ruling (5)[A], ferry (read first)', 'ERRATA.md :538 and :542, two description sentences', 'description sentence' in at(er_, 538) and 'description sentence' in at(er_, 542), 'read', '3')
    ins_ = lines_of(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'))
    for n_, nd_ in ((710, '## I-96'), (734, '## I-102'), (746, '## I-105'), (750, '## I-106'), (758, '## I-108'), (764, '## I-109')):
        add('ruling (5)[R1], ferry (read first)', 'INSTRUMENTS.md :%d, %s' % (n_, nd_[3:]), at(ins_, n_).startswith(nd_ + ' '), at(ins_, n_)[:40], '3')
    add('ruling (5)[R1]', 'data/b711_coeffs.txt :12, the least n with c(n) < 0: n = 48', 'THE LEAST n WITH c(n) < 0: n = 48' in at(lines_of(p('data', 'b711_coeffs.txt')), 12), 'read', '3')
    cq_ = lines_of(p('data', 'b752_cq_signature.txt'))
    add('ruling (5)[R2], ferry (read first)', 'data/b752_cq_signature.txt :166, the signature`s foot over n <= 3000', 'THE SIGNATURE, n <= 3000' in at(cq_, 166), at(cq_, 166)[:60], '3')
    for n_, nd_ in ((2691, '### O.8 — DESI 5-year analysis prep'), (18148, '**A candidate order beside W-ORD-ZQ-FAMILY, named and not entered:** the tighter box'),
                    (18232, '### b753 — lane two, act one hundred and eighty, the system refresh under (R363)'), (18282, '**Next:** the sitting (b754)')):
        add('ruling (5)[L], ferry (read first)', 'OPEN_TRAILS.md :%d, %s' % (n_, nd_.strip('#* ')[:50]), at(ot, n_).startswith(nd_), at(ot, n_)[:60], '3')
    add('ruling (5)[Q](3)', 'OPEN_TRAILS.md :2685, item O.7, by place alone (its heading`s digest)', at(ot, 2685).startswith('### O.7'), _h.sha256(at(ot, 2685).encode('utf-8')).hexdigest()[:16], '3')
    ep_ = lines_of(os.path.join(PP, 'phase1.5', 'spectral', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md'))
    add('ruling (5)[R3], ferry (read first)', 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md :216 section 8`s title, :218 section 9`s', at(ep_, 216).startswith('## 8. What this does not say') and at(ep_, 218).startswith('## 9. Back matter'), at(ep_, 216)[:40], '3')
    b536_ = lines_of(p('data', 'b536_components.txt'))
    add('ruling (5)[B1], ferry (read first)', 'data/b536_components.txt :12, h2_sign_iff_rh on [propext, Classical.choice, Quot.sound]', 'h2_sign_iff_rh' in at(b536_, 12) and 'depends on axioms: [propext, Classical.choice, Quot.sound]' in at(b536_, 12), at(b536_, 12)[:60], '3')
    fl_ = lines_of(p('data', 'b721_frozen_line_drafts.txt'))
    add('ruling (5)[Q], ferry (read first)', 'data/b721_frozen_line_drafts.txt :7, the record`s form of line and digest', 'cited by line and not quoted' in at(fl_, 7), at(fl_, 7)[:60], '3')
    sp_ = lines_of(p('data', 'b724_split_price.txt'))
    add('ruling SCOPE, (5)[M2], ferry (read first)', 'data/b724_split_price.txt :27, the split as priced: 11209 citation occurrences, 530 in live tools', '11209' in at(sp_, 27) and '530' in at(sp_, 27), at(sp_, 27)[:60], '3')
    add('ruling (5)[A5], [B], ferry (read first)', 'tools/b736_sitting.py :399-:467, the description route`s form, tracked at 34332a00', bool(_blob('D:/relay', '34332a00', 'tools/b736_sitting.py')), '%d lines' % len(_blob('D:/relay', '34332a00', 'tools/b736_sitting.py').split(NL)), '3')
    for k_, c_, ws_ in (('D:/SIDE-explicit-formula', '8fbab45d', ((3, '**A VENDORED KERNEL.'), (5, 'Every `.lean` body here is a byte-identical copy'), (7, 'attribution header and nothing else was changed.'),
                                                             (23, '**WHAT IS NOT CLAIMED.**'), (26, 'a push is not a verification'))),
                        ('D:/SIDE-kernel', 'f8534ef2', ((3, 'SIDE-kernel compiles, over Mathlib, the logical structure of a two-leg approach to the Riemann Hypothesis.'),)),
                        ('D:/SIDE-bsd-multiplicity', 'd77ce309', ((3, '> **⚠ SCAFFOLDING — placement skeleton over stipulated constants'),)),
                        ('D:/SIDE-trivium', '18a351a1', ((3, 'SIDE-trivium compiles an equivalence between two seven-constructor enumerations.'), (5, '    theorem trivium_theorem')))):
        rm_ = _blob(k_, c_, 'README.md').replace(chr(13), '').split(NL)
        add('ruling (5)[B], ferry (read first)', '%s README.md at %s %s' % (k_.split('/')[-1], c_, ', '.join(':%d' % n_ for n_, _w in ws_)), all(at(rm_, n_).startswith(w_) for n_, w_ in ws_),
            '%d lines' % len(rm_), '3')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    # ### b754 step zero: (R364)(1) and (3)'s counts over b753's banks, written over b753's carried rows (b752's thirteen events and thirty-six
    # ### defects); each tag read as the bank tags it, as (3) orders
    add('ruling (1), (3), ferry (read first)', 'b753`s events (1)-(9) and 52 lettered defects (data/b753_events.txt, data/b753_defects.txt)',
        starts == list(range(1, 10)) and len(letters) == 52, 'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    fi = lines_of(os.path.join(PP, 'FINDINGS.md'))
    ot = lines_of(os.path.join(PP, 'OPEN_TRAILS.md'))
    TAG_ = re.compile(r"^    \((\d+|[a-z]'?)\) THE (SEAT|AUTHOR|HOST|NAVIGATOR)'S \[(CLAIM|CLOSE) ; (NEW|REPEAT)")
    rows4_ = [l_ for l_ in ev + lines_of(p('data', 'b753_events_postseal.txt')) + dl if re.match(r"^    \((\d+|[a-z]'?)\) ", l_)]
    add('ruling (3), ferry (read first)', 'each of b753`s 52 defects and 14 events (nine and the post-seal five) tagged CLAIM or CLOSE and NEW or REPEAT as its bank tags it',
        len(rows4_) == 66 and all(TAG_.match(l_) for l_ in rows4_), 'rows %d ; tagged %d' % (len(rows4_), sum(1 for l_ in rows4_ if TAG_.match(l_))), '1')
    add('ruling (1), (3)', 'FINDINGS :%d, b753`s entry' % K.B711_ENTRY, at(fi, K.B711_ENTRY).startswith('## H-C3-LAW, the class-number-3 walk, registered and not run'), at(fi, K.B711_ENTRY)[:50], '0')
    add('ruling (1)', 'FINDINGS :%d and :%d, b752`s weight line and corrigendum (b753`s), the form b754`s follow' % (K.B711_WEIGHT, K.B711_CORRIGENDUM), at(fi, K.B711_WEIGHT).startswith('*Appended 2026-11-11 by b753') and at(fi, K.B711_CORRIGENDUM).startswith('## Corrigendum to b752'), at(fi, K.B711_WEIGHT)[:40], '0')
    add('ferry (read first)', 'OPEN_TRAILS :%d, b753`s trail record' % K.B711_TRAIL, at(ot, K.B711_TRAIL).startswith('### b753 '), at(ot, K.B711_TRAIL)[:50], '0')
    add('ruling (1)', 'OPEN_TRAILS :%d, b753`s open-orders line' % K.TRAIL_ORDERS, at(ot, K.TRAIL_ORDERS).startswith('**The open orders:**'), at(ot, K.TRAIL_ORDERS)[:50], '0')
    add('PATHS', 'the relay at D:/relay, PLACE-papers at its path', os.path.isdir('D:/relay/.git') and os.path.isdir(os.path.join(PP, '.git')), PP, '0')
    add('PATHS', 'the two shelves at D:/PLACE-phase1.5 and D:/PLACE-phase2', os.path.isdir('D:/PLACE-phase1.5') and os.path.isdir('D:/PLACE-phase2'), 'present', '0')
    add('PATHS', 'SIDE-explicit-formula at D:/SIDE-explicit-formula, SIDE-kernel at D:/SIDE-kernel', os.path.isdir('D:/SIDE-explicit-formula/.git') and os.path.isdir('D:/SIDE-kernel/.git'), 'present', '0')
    add('PATHS', 'the transcripts` store at D:/claude-store/projects-D--, behind its junction', os.path.isdir('D:/claude-store/projects-D--'), 'present' if os.path.isdir('D:/claude-store/projects-D--') else 'ABSENT', '0')
    add('ferry (read first)', 'the hook`s settings file D:/.claude/settings.json by its hash alone', bool(__import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest()), __import__('hashlib').sha256(open('D:/.claude/settings.json', 'rb').read()).hexdigest().upper()[:16], '0')
    add('ferry', 'tools/standing/ at v1.33.0 entering the act', (_blob('D:/relay', (K.C1_STANDING + '^') if K.C1_STANDING else 'HEAD', 'tools/standing/VERSION') or '').strip() == 'v1.33.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ferry', 'data/standing_clauses_v9.txt present, row (83) the repeat rule', os.path.exists(p('data', 'standing_clauses_v9.txt'))
        and '(83)' in (rd(p('data', 'standing_clauses_v9.txt')) or ''), 'v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    # ### (R364)(1): b753's export, the mirror's last
    add('ruling (1)', '%s, b753`s export' % K.MIRROR_ZIP, os.path.exists(K.MIRROR_ZIP),
        'present' if os.path.exists(K.MIRROR_ZIP) else 'ABSENT', '3')
    # ### PATHS: SIDE-explicit-formula and the other clones at the paths the worklist holds, each listed, a path absent printed absent
    add('PATHS', 'the clones at the worklist`s paths (K.KERNEL_PATHS), each present', bool(K.KERNEL_PATHS) and all(os.path.isdir(k_) for k_ in K.KERNEL_PATHS),
        '%d paths ; absent %s' % (len(K.KERNEL_PATHS), [k_ for k_ in K.KERNEL_PATHS if not os.path.isdir(k_)] or 'none'), '0')
    # ### (R364)(3), (5): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (3), (6)', 'the push-b753-* branches of %s, --merged into main before their deletes (no local branch left after them)' % repo_.split('/')[-1], sorted(mg) == sorted(names_) or not mg, ' '.join(mg) or 'NONE LEFT, DELETED AT STEP ZERO', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    # ### (R364)(3), (5): act_current alone, then b753's closing capture and tools/mirror_prevbuild.json, each committed alone
    for c_, fs_ in ((K.ACT_CURRENT_COMMIT, ['data/act_current.json']),
                    (K.STEPZERO, ['data/b753_relay_push-b753-closing_push_out.txt']),
                    (K.STEPZERO_PREVBUILD, ['tools/mirror_prevbuild.json'])):
        if fs_ == ['tools/mirror_prevbuild.json'] and not c_:   # ### b754: committed alone if it differs from HEAD's blob beyond line endings, else restored
            hb_ = gr('D:/relay', 'rev-parse', 'HEAD:tools/mirror_prevbuild.json')
            add('ruling (3)', 'tools/mirror_prevbuild.json at HEAD`s blob %s (equal, or to be committed alone after this check)' % hb_[:8], True,
                'blob %s ; HEAD %s' % (gr('D:/relay', 'hash-object', 'tools/mirror_prevbuild.json')[:8], hb_[:8]), '0')
            continue
        if not c_:
            add('ruling (3), (5)', '%s -- TO BE COMMITTED at step zero after this check' % ' '.join(fs_), True, 'after the check, as ordered', '0')
            continue
        nm_ = gr('D:/relay', 'show', '--name-only', '--format=', c_).split()
        add('ruling (3), (5)', '%s committed alone at %s' % (' '.join(fs_), c_), sorted(nm_) == sorted(fs_), ' '.join(nm_)[:80], '0')
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (3), (6)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (3), (6)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (3), (6)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '3')
#⟪END⟫
#⟪SECTION citation 10⟫
    add('ferry (read first)', 'data/b754_readfirst.txt, the readfirst bank -- TO BE WRITTEN at step zero after this check', True,
        'present' if os.path.exists(p('data', 'b754_readfirst.txt')) else 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b754 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b753_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- ABSENT, not ordered written at this act' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 3) are the corrigendum with v1.33.0's controls and the rules, the registration, the five reads, the agenda with the answers bank and the waiver's bank, the line bank, the name and address scan, the
reproduction run, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R364)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for the next act ((R364)(8)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act: none ((R364)(10): no kernel's main touched, no Lean file, no tag beyond v0.38).
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b754 ((R364)(8) and the author's words); the open orders by tools/standing/orders.py's output over the trail, not a hand list."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
import standing.faceform as FF   # ### v1.8.0, (R363)(2)(iv)(c): the outbound sentence from the one clause
TITLE_LINE = ('b754 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND EIGHTY-ONE, THE SITTING: b753 AT ITS WEIGHT; THE NAVIGATOR`S CORRECTIONS; '
              'THE CORRIGENDUM OPENING ON THE FOUR CLASSES THAT REPEATED THREE ACTS RUNNING AND ON THE POST-SEAL EVENTS BANK; THE CLOSE`S YIELD AND THE ANCHORS` KERNEL TAGS READ; '
              'THE REFERENCE LAYER`S FOUR ANCHORS AND SEVEN DOORS PUT; THE QUOTING RULE, THE RECORD`S UPKEEP, THE CENSUS`S NEXT EDITION, THE HANDOFF PAGE, THE PROJECT SET, '
              'THE UPDATE CHANNEL AND THE CARRIED LINES PUT; THE SOURCING RULES ENTERED; NOTHING BUILT AND NOTHING COMPUTED, UNDER (R364).**')   # ### b754 step zero: the ferry`s ACT line (data/b754_ferry.txt :70) as delivered, to be adjusted at Component 4 to what the act did
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (b753's sections over b753's objects not carried). A row of two reads its bank's verdict line by
    vtail; a row of three reads the line its pattern names."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.33.0: the repairs of (R364)(7), nine controls over 16 cases, each case through the route before and the route after', 'b754_standing_v1330.txt'),
                ('the two rules entered on the author`s word, [M1] and [D1]', 'b754_rules.txt', r'(?m)^b754 -- THE RULES ENTERED[^\n]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE REGISTRATION ((R364)(4))', [
                ('the class-number-3 walk registered by H-C3-LAW, the rule committed before its table, sixteen rows, not run', 'b754_registrations.txt')]),
            ('THE READS ((R364)(5))', [
                ('the kernels reconciled against the lists, one remote read per repository', 'b754_kernels.txt'),
                ('the criterion kernel`s remote branches mapped against main', 'b754_branch_map.txt'),
                ('the front doors` heads read against the registry and the descriptions', 'b754_head_read.txt'),
                ('the reference layer`s anchors read against the ledgers` later lines, none edited', 'b754_anchors.txt'),
                ('the transcript store read by names, sizes and dates', 'b754_store.txt')]),
            ('THE AGENDA, THE HOLD AND THE WAIVER ((R364)(6))', [
                ('the agenda of the two kept items, banked before either was put', 'b754_agenda.txt'),
                ('the author`s answers appended by the record tool`s route, [M1] passed and [D1] passed as (a)', 'b754_author_answers.txt',
                 r'(?m)^### b754 -- THE AUTHOR`S ANSWERS[^\n]*'),
                ('the waiver`s bank, the inventory`s counts and no word of any row', 'b754_waiver.txt'),
                ('the probe-path refusal printed before the lock gate', 'b754_pathrefusal.txt')]),
            ('THE LINE (Component 4)', [
                ('the INTEGRATION line from REGISTRY and SPIRAL_MAP with the match, stage CLUSTERED for the registration and BANKED for the reads, 0 of 6 names matched, the earlier lines read again, none rewritten', 'b754_line.txt')]),
            ('THE NAME AND ADDRESS (N5)', [
                ('the scan over every commit and bank of the act, the counts alone', 'b754_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b753`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument entered, a planted wrong figure per run row', 'b754_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written, N5`s clause as the ferry words it: ' + FF.n5_clause_of(rd('%s_ferry.txt' % ACT)) + ' ;',   # ### v1.10.0, (R363)(2)(vi): composed, not carried
    '    no kernel`s main touched ((R364)(10)) ; SIDE-explicit-formula`s main at ' + WL.EF_MAIN[:8] + ' and v0.37 unmoved ; no tag beyond v0.38 ; zq-b730 at ' + WL.ZQ_TIP[:8] + ', unmoved, no Lean file written, no merge ;',
    '    ' + str(len(WL.EF_RUNS)) + ' runner dispatches (N1: none this act) ; the rebuild-b721 branches of the wave 1 kernels as b753 left them ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ; free memory read before each suite part and computation ;',
    '    the push-b753-* branches of relay and PLACE-papers deleted at step zero by name, each after its --merged listing, one per command and each its own message ; N2: the registration`s rule committed before its table and both before any walk, each read`s generator committed before its bank, the agenda banked before either item was put, each tool`s controls before its figures, the (W) regeneration, the pre-lock dry in both modes, the pre-lock comparison and the probe-path refusal before the lock gate, the lock block in the lock commit, the scan over the staged set before every commit to its own bank ;',
    '    N3: the registration read where it stands -- a rule and its table, NOT RUN, no row said to hold or to fail, no form and no coefficient read at an unused discriminant, the candidate statements carried and none registered ; the reads print what the repositories and the documents carry ; no sentence saying a thing was deposited, published or versioned ; the entry`s INTEGRATION line read from REGISTRY and SPIRAL_MAP ;',
    '    N5 as the author`s word of 2026-11-11 reads it for the rest of the act (relay data/b754_events.txt (5)): of a private repository other than PLACE-papers, names, sizes, dates and hashes ; of PLACE-papers, the words the waiver names, counted by class in relay data/b754_waiver.txt, and what the standing tools print ; no new occurrence of the author`s name, address or ORCID in anything the act wrote, committed or pushed (relay data/b754_address_scan.txt, data/b754_address_scan_postlock.txt, data/b754_address_scan_commits.txt) ;',
    '    the commits under the GitHub login and its noreply address ; ' + FF.outbound_clause('gh reads under the GitHub login') + ' ;',
    '    nothing deposited ; no new Zenodo version ; no Zenodo call ; no draft published, the draft held at v5 ; no GitHub description written ; no README, description or anchor edited ;',
    '    on PLACE-papers main FINDINGS (the weight line, the corrigendum, the entry) and OPEN_TRAILS (the trail) ; no paper written ; no door or ledger row edited ; no paper moved or renamed ;',
    '    no FOUNDATIONS or faces page byte ; data/act_roots.txt (b754`s root) and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ;',
    '    tools/standing/ at v1.33.0 by (R364)(7), the commits after its own at which a standing tool changed named in its bank (relay data/b754_standing_v1330.txt) ; tools/mirror_roster_added.json written at [M1]`s pass ; the one settings key of [D1] written by the seat on the author`s pass (relay data/b754_rules.txt (2)) ; the per-act tools of b698-b753 unedited, act_current`s shared_edits naming [M1]`s list tools/mirror_roster_added.json alone (standing/carry.py shared) ; the mirror zip written outside every repository over the',
    '    roster read from PLACE-papers main, 75 entries and the seven of [M1], the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT, AS (R364)(8) AND THE AUTHOR`S WORDS ORDER IT**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '    (c) For the next act, the sitting, each from its bank: the root`s question on the next act, its answer in relay data/b754_author_answers.txt ; the items of (R364)(6) the author`s word carried, [C1] with its census reads, [H1], [M2], [L1] and onward, and (5)(v) and (5)(vi), the shelves` listing and the cluster export (relay data/b754_author_words_preseal.txt, data/b754_stepzero.txt) ;',
    '        the quote-versus-digest line (relay data/b726_frontdoors.txt [12]; the citation check`s found-text column; the forms of the head read and the anchors read) ; the four anchors moved by a later line, FINDINGS :901 and :979 at the head of the list, and PLACE-papers` description with them (relay data/b754_anchors.txt, data/b754_waiver.txt) ; the doors not AGREES (relay data/b754_head_read.txt) ; I-109`s cross-reference to I-106, I-108 and relay data/b711_coeffs.txt ; the Epstein document`s section 8 ; the items (R363)(8) carried ;',
    '        the navigator`s candidate statements (a)-(h), none registered, each to be reproduced with a planted error at the walk`s act (relay data/b754_registrations.txt (3)) ; the temp directory read, the hook`s ledger and git-write state beside it (tools/standing/hook.py :282, :306) ; the build of T0 then T1 in an act the author names (relay data/b753_attribution_plan.txt, b753`s [P1]) ;',
    '        the reproduction`s NOT RUN rows, each with its price (relay data/b754_reproduce.txt) ; W-ORD-VISIBILITY, CARRIED NOT CLEAN ; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads) and records.json at relay`s root',
    '        (2026-09-24, not this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); keiper-b725 at ' + WL.EF_BRANCHES[0][1][:8] + ', c2-b725 at ' + WL.EF_BRANCHES[1][1][:8] + ', detect-b729 at ' + WL.EF_BRANCHES[2][1][:8] + ' and zq-b730 at ' + WL.EF_BRANCHES[3][1][:8] + ' of',
    '        SIDE-explicit-formula, off main, zq-b730 carrying the tag v0.38 at 14ca5725 and b745`s Lean past it to 1e658870, unmoved this act; scratch-b724 of SIDE-lv-conservation; corrigendum-b723 of relay;',
    '        challenge-b720-h2-sign-iff-rh of SIDE-explicit-formula; the pin-b718-de5ce8a9 branches; the rebuild-b721 branches of the wave 1 kernels as b753 left them.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, no Lean file written, no tag beyond v0.38 ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (b735`s [41]), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b754: the standing repairs are v1.33.0's ((R364)(7), relay data/b754_standing_v1330.txt, read in the corrigendum section, the commits
    # ### after its own at which a standing tool changed named there with the controls run after them); the carry's diffs here (b754 carried at
    # ### step zero before the fold; its tools since are the templates and tools/acts/b754.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; zq-b730 of SIDE-explicit-formula at %s, unmoved this act; '
          'no Lean file written; the %s branches of the wave 1 kernels as b753 left them; port-b707 at b712`s tip %s)' % (
              len(ks), K.JOIN_NEW_TIP[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
#⟪END⟫
#⟪SECTION record 2⟫
def _trail_resolved(text):
    """b703's reader of the trail's Resolved line, its navigator letters taken with a prime: this act's navigator letter is (b`), which b703's
    `\\([a-z]\\)` cannot read (the gate's dry run, defect (e`)); otherwise as b703's."""
    m = re.search(r"^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)"
                  r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", text, re.M)
    return (m.group(2), m.group(3)) if m else None
#⟪END⟫
#⟪SECTION record 3⟫
    b754's form over b754's objects: the corrigendum's foot and v1.33.0's controls with the commits after its own and the roster's controls;
    the registration's foot; the five reads' feet (the kernels, the branch map, the head read, the anchors, the store); the agenda's foot, the
    rules bank's rows and the answers bank's RESULT row; the waiver bank's foot; the line bank's foot; the citation check; the reproduction
    run; the address scan; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter from the
    act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v5 = _bfig('%s_standing_v1330.txt' % ACT, r'\*\*v1\.33\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ; ALL AS WANTED\.\*\*', 'v1.33.0`s controls')
    later_ = re.findall(r'(?m)^  ([0-9a-f]{8}) at (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ): ', rdn('%s_standing_v1330.txt' % ACT))   # ### the commits after v1.33.0's own, named in its bank (the author's sixth word (4))
    ro_ = _bfig('%s_standing_v1330.txt' % ACT, r'\*\*ROSTER CONTROLS (\d+) ; AS WANTED (\d+) ; ALL AS WANTED True\.\*\*', 'the roster`s controls run after the later commits')
    rg_ = _bfig('%s_registrations.txt' % ACT, r'\*\*THE REGISTRATION: (H-C3-LAW), THE RULE AT ([0-9a-f]+) BEFORE ITS TABLE ; ROWS (\d+): CONTROLS (\d+), TESTS (\d+) ; '
                r'THE VALUE (\S+) AT EVERY ROW ; (NOT RUN) ; NO FORM AND NO COEFFICIENT READ AT AN UNUSED DISCRIMINANT ; CANDIDATES CARRIED \(a\)-\(([a-z])\), NONE REGISTERED\.\*\*',
                'the registration`s foot')
    kn_ = _bfig('%s_kernels.txt' % ACT, r'\*\*THE KERNELS RECONCILED: (\d+) REPOSITORIES ; ANSWERED (\d+) ; FAILED (\d+) ; ON D: (\d+) ; ABSENT FROM A LIST (\d+) ; '
                r'LOCAL HEAD NOT THE REMOTE MAIN (\d+) ; CONTROLS ALL AS WANTED\.\*\*', 'the kernels` foot')
    bm_ = _bfig('%s_branch_map.txt' % ACT, r'\*\*THE CRITERION KERNEL`S BRANCHES MAPPED: (\d+) ; OFF MAIN (\d+) \(([^)]*)\) ; MERGED (\d+) ; RESULTS OF RECORD OFF MAIN (\d+) OF (\d+) ; '
                r'PAIRS OF THE FOUR SHARING A MODULE (\d+) OF (\d+) ; THE TWIN READ: NO RELATING DECLARATION FOUND ; CONTROLS ALL AS WANTED\.\*\*', 'the branch map`s foot')
    hr_ = _bfig('%s_head_read.txt' % ACT, r'\*\*THE HEAD READ: (\d+) DOORS \(READMEs read\) ; QUOTED (\d+), NOT AGREEING (\d+) ; PRIVATE AND NOT QUOTED (\d+) ; AGREES (\d+) ; '
                r'AN OLDER WORDING THE REGISTRY REWORDED (\d+) ; NO DESCRIPTION (\d+) ; READ, NOT QUOTED, NO VERDICT OF ITS WORDING PRINTED (\d+) ; '
                r'THE DESCRIPTION DIFFERS FROM THE HEAD (\d+) ; THE HEAD DENIES A LATER SECTION (\d+) ; NO README OR NOT READ (\d+) ; THE KNOWN INSTANCE AS WANTED ; '
                r'CONTROLS ALL AS WANTED\.\*\*', 'the head read`s foot')
    an_ = _bfig('%s_anchors.txt' % ACT, r'\*\*THE REFERENCE LAYER`S ANCHORS READ: (\d+) ; MOVED BY A LATER LINE (\d+) ; STANDS (\d+) ; NO LATER LINE FOUND (\d+) ; NONE EDITED ; '
                r'CONTROLS ALL AS WANTED\.\*\*', 'the anchors` foot')
    sr_ = _bfig('%s_store.txt' % ACT, r'\*\*THE STORE READ: SESSIONS (\d+) ; THE TOOLS NAME (\d+) IDS, ABSENT (\d+), A NEAR TWIN (\d+) ; THE BANKS` KEYS NAME (\d+), ABSENT (\d+) ; '
                r'READERS OF THE ABSENT (\d+) FILES, GUARDED AND GOING ON (\d+) ; SCRATCH FOLDERS NAMED WITH A ROOT (\d+), GONE (\d+) ; '
                r'THE HOLD`S FOUR READS REPRODUCED AND TWO OF THEM UNDERSTATED ; THE TEMP DIRECTORY READ A CANDIDATE ; CONTROLS ALL AS WANTED\.\*\*', 'the store read`s foot')
    ag_ = _bfig('%s_agenda.txt' % ACT, r'\*\*THE AGENDA: (\d+) ITEMS, \[M1\] AND \[D1\] ; \[M1\] DRAFTS (\d+) FAMILIES, THE ROSTER (\d+) -> (\d+) ; \[D1\] DRAFTS (\d+) FORMS ; '
                r'NOTHING WRITTEN BEYOND THIS BANK ; CONTROLS ALL AS WANTED\.\*\*', 'the agenda`s foot')
    wv_ = _bfig('%s_waiver.txt' % ACT, r'\*\*THE WAIVER`S BANK: ANCHORS (\d+) \(A (\d+), B (\d+), C (\d+), D (\d+), E (\d+)\) ; ROWS OUTSIDE THE ANCHORS BANK (\d+) AND THE HEAD READ`S (\d+) ; '
                r'NO WORD OF ANY ROW PRINTED\.\*\*', 'the waiver bank`s foot')
    ln_ = _bfig('%s_line.txt' % ACT, r'\*\*THE LINE: (COMPOSED) ; FROM REGISTRY 1\.5c-21 TO 1\.5c-23 AND SPIRAL_MAP WITH THE MATCH ; KEYSTONE (\S+) ; STAGE (\S+) ; '
                r'MATCHED (\d+) OF (\d+) ; THE REGISTRATION CLUSTERED, THE READS BANKED \((\d+) NAMES, (\d+) SEATED\) ; THE EARLIER LINES READ AGAIN (\d+), NONE REWRITTEN ; '
                r'(ALL AS READ)\.\*\*', 'the line bank`s foot')
    reps_ = [int(x_) for x_ in re.findall(r'(?m)^  \((\d+)\) THE ', rdn('%s_rules.txt' % ACT))]   # ### the rules bank's rows, (1) at [M1] and (2) at [D1]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    m1_ = re.search(r'"\[M1\] [^\n]*?"="([^"\n]+)"', ans_)   # ### the RESULT row's word on each item, by the record tool's route
    d1_ = re.search(r'"\[D1\] [^\n]*?"="([^"\n]+)"', ans_)
    am_ = []
    cit = _bfig(K.CITATION_BANK, r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', 'the citation check')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ; PLACES (\d+) ; CONTROLS 7 OF 7 '
               r'AS WANTED ;', 'the address scan`s foot')
    # ### b754: no order entered this act ((R364) enters none)
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v1130_ctl=v5[0], v1130_cases=v5[1], v1130_wanted=v5[2], later=later_, ro_n=int(ro_[0]), ro_wanted=int(ro_[1]),
                rules_rows=reps_, repairs=len(reps_),   # ### the rules bank's rows, one per item passed on the author's word
                m1=(m1_.group(1) if m1_ else 'UNANSWERED'), d1=(d1_.group(1) if d1_ else 'UNANSWERED'),
                rg_rule=rg_[1], rg_rows=int(rg_[2]), rg_ctl=int(rg_[3]), rg_tests=int(rg_[4]), rg_value=rg_[5], rg_run=rg_[6], rg_cand=rg_[7],
                kn_n=int(kn_[0]), kn_ans=int(kn_[1]), kn_fail=int(kn_[2]), kn_d=int(kn_[3]), kn_absent=int(kn_[4]), kn_late=int(kn_[5]),
                bm_n=int(bm_[0]), bm_off=int(bm_[1]), bm_offnames=bm_[2], bm_merged=int(bm_[3]), bm_rec=(int(bm_[4]), int(bm_[5])), bm_pairs=(int(bm_[6]), int(bm_[7])),
                hr_doors=int(hr_[0]), hr_quoted=int(hr_[1]), hr_notagree=int(hr_[2]), hr_private=int(hr_[3]), hr_agrees=int(hr_[4]), hr_older=int(hr_[5]),
                hr_nodesc=int(hr_[6]), hr_noverdict=int(hr_[7]), hr_descdiff=int(hr_[8]), hr_denies=int(hr_[9]), hr_noreadme=int(hr_[10]),
                an_n=int(an_[0]), an_moved=int(an_[1]), an_stands=int(an_[2]), an_none=int(an_[3]),
                sr_sessions=int(sr_[0]), sr_ids=int(sr_[1]), sr_absent=int(sr_[2]), sr_twin=int(sr_[3]), sr_keys=int(sr_[4]), sr_keys_absent=int(sr_[5]),
                sr_readers=int(sr_[6]), sr_guarded=int(sr_[7]), sr_scratch=int(sr_[8]), sr_gone=int(sr_[9]),
                ag_items=int(ag_[0]), ag_fams=int(ag_[1]), ag_roster=(int(ag_[2]), int(ag_[3])), ag_forms=int(ag_[4]),
                wv_anchors=int(wv_[0]), wv_classes=tuple(int(x_) for x_ in wv_[1:6]), wv_rows=int(wv_[6]), wv_head=int(wv_[7]),
                ln_keystone=ln_[1], ln_stage=ln_[2], ln_matched=int(ln_[3]), ln_of=int(ln_[4]), ln_names=int(ln_[5]), ln_seated=int(ln_[6]),
                ln_earlier=int(ln_[7]), ln_ok=(ln_[8] == 'ALL AS READ'),
                amend_n=len(am_),
                cit_n=cit[0], cit_ok=cit[1], cit_miss=cit[2],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], orcid=ad[3], addr_places=ad[4],
#⟪END⟫
#⟪SECTION record 6⟫
def _ef_kind(rows, kind):
    """(R364)(3): the kernel rows of one kind as banked (data/b754_dispatch_rows.json: commit, push, dispatch, read)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R364): no lean process runs on this host; no runner dispatch this act (MAX_DISPATCHES 0, EF_RUNS empty, no dispatch row and no
    dispatch command in the capture); every row carrying free_mb; no suite part in the background. From the command bank (the seat's commands, read live from the capture by the
    `commands` route), the dispatch rows beside the worklist's EF_RUNS, and the hook's refusal bank (a suite part sent in the background
    refused BACKGROUND)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows_ = jl('%s_dispatch_rows.json' % ACT) or []
    reads_ = sorted(str(r.get('run')) for r in _ef_kind(rows_, 'read'))
    runs_ = sorted(set(reads_)) == sorted(str(x) for x in K.EF_RUNS)
    free_ = [r for r in _ef_kind(rows_, 'dispatch') + _ef_kind(rows_, 'read') if not isinstance(r.get('free_mb'), int)]
    bg_ = [l for l in rdn('%s_hook_refusals.txt' % ACT).split(NL) if '| BACKGROUND |' in l]
    bgc_ = [r['n'] for r in ((cm.get('rows') or []) if cm else []) if r.get('bg') and re.search(r'fold\.py"? checks\b|_checks\.py', r.get('cmd') or '')]
    refused_ = _ef_kind(rows_, 'dispatch_refused')
    lic_ = [r for r in _ef_kind(rows_, 'dispatch') if not str((r.get('licence') or {}).get('commit') if isinstance(r.get('licence'), dict) else r.get('licence') or '').startswith(K.STEPZERO_BANKS[:8])]
    ok = bool(cm) and not seat_lean and len(disp or []) == len(K.EF_RUNS) + len(refused_) == 0 and len(_ef_kind(rows_, 'dispatch')) == len(K.EF_RUNS) <= K.MAX_DISPATCHES == 0 \
        and runs_ and not free_ and not lic_ and not bg_ and not bgc_
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b754_commands.json): %s; dispatch commands in the capture: %s, sends refused by the host (no run): %d, against the %d N1 allows; the worklist`s runs %d, each read by its run id: %s (reads %d, a run read twice: %s); dispatch and read rows without free_mb: %s; dispatch rows not naming the licence %s: %s (relay data/b754_dispatch_rows.json); suite parts sent in the background: %s, refused BACKGROUND: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(refused_), K.MAX_DISPATCHES, len(K.EF_RUNS), runs_, len(reads_),
            ', '.join(sorted(set(x for x in reads_ if reads_.count(x) > 1))) or 'none', len(free_), K.STEPZERO_BANKS[:8], len(lic_), len(bgc_) if cm else 'unread', len(bg_)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (over b754's objects): the tools' controls before their figures banked this act, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b754_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'),
               ('data/b754_pathrefusal.txt', '## THE CONTROLS FIRST', '## THE PATHS READ'),
               ('data/b754_standing_v1330.txt', '## THE CONTROLS', '### ### **v1.33.0: CONTROLS '),
               ('data/b754_kernels.txt', '## THE CONTROLS, printed before any figure', '## THE ROWS:'),
               ('data/b754_branch_map.txt', '## THE CONTROLS, printed before any figure', '## THE BRANCHES:'),
               ('data/b754_head_read.txt', '## THE CONTROLS, printed before any figure', '## THE TABLE'),
               ('data/b754_anchors.txt', '## THE CONTROLS, printed before any figure', '## THE ANCHORS:'),
               ('data/b754_store.txt', '## THE CONTROLS, printed before any figure', '## THE STORE:'),
               ('data/b754_agenda.txt', '## THE CONTROLS, printed before any current word or draft', '## [M1] THE ARCHIVE'))
N2_REGEN = '### THE (W) REGENERATION'   # ### the regeneration printed in the face, before the lock gate
# ### N2, the registration and the reads: the rule committed alone before its table; each generator first added by a commit of its own
# ### before its bank, carrying the generator and not the bank, the bank's commit not the generator
N2_SECTIONS = ()


def _first_add(path):
    """the relay commit that first added a path (git log --diff-filter=A, the oldest), None where it is not committed."""
    hs = [h for h in g(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', path).split() if h.strip()]
    return hs[-1] if hs else None
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R364): step zero's banks, v1.33.0, the weight and corrigendum (PLACE-papers, then relay), the registration's rule and then its
    table, Component 2's opening commit, each read's generator and then its bank, the agenda's generator and its bank, [M1], [D1], the
    waiver's bank, the line, the v1.33.0 bank's composer and the bank, in that order by time; each generator (the five reads', the agenda's,
    the v1.33.0 bank's composer) first added by a commit of its own carrying it and not its bank, the bank's commit not the generator; the
    registration's rule committed alone, its blob without the table; each tool's controls before its figures; the (W) regeneration, the
    pre-lock comparison and the probe-path refusal before the lock gate; v1.33.0 an ancestor of the v1.33.0 bank's commit, and that of HEAD;
    Components 2-4 writing the relay alone."""
    chain_ = [(ROOT, K.STEPZERO_BANKS), (ROOT, K.C1_STANDING), (PP, K.C1_PP), (ROOT, K.C1_RELAY), (ROOT, K.REG_RULE), (ROOT, K.REG_TABLE), (ROOT, K.C2_PLAN_FIRST)]
    for _n, gens_, bank_ in K.C2_READS:
        chain_ += [(ROOT, gens_[-1]), (ROOT, bank_)]
    chain_ += [(ROOT, K.C3_AGENDA[0]), (ROOT, K.C3_AGENDA[1]), (ROOT, K.C3_ITEMS[0][1]), (ROOT, K.C3_ITEMS[1][1]), (ROOT, K.C3_WAIVER), (ROOT, K.C4_LINE),
               (ROOT, K.C4_V1330[0]), (ROOT, K.C4_V1330[1])]
    tm_ = [int((g(r_, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) for r_, h_ in chain_]
    order_ = all(tm_) and tm_ == sorted(tm_)
    anc_ = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C1_STANDING, K.C4_V1330[1]], capture_output=True).returncode == 0 \
        and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C4_V1330[1], 'HEAD'], capture_output=True).returncode == 0
    ppl_ = [x for x in g(PP, 'rev-list', '%s..HEAD' % K.PRE_PP).split() if x.strip()]
    disch_ = sorted(x for x in g(PP, 'show', '--name-only', '--format=', K.C1_PP).split() if x.strip()) == ['FINDINGS.md'] \
        and not [h_ for h_ in ppl_ if int((g(PP, 'log', '-1', '--format=%ct', h_) or '0').strip() or 0) < tm_[-1] and not h_.startswith(K.C1_PP)]
    files_ = lambda h_: [x for x in g(ROOT, 'show', '--name-only', '--format=', h_).split() if x.strip()]
    gens_ok_ = []
    for n_, gens_, bank_ in tuple(K.C2_READS) + (('agenda', (K.C3_AGENDA[0],), K.C3_AGENDA[1]), ('v1330_later', (K.C4_V1330[0],), K.C4_V1330[1])):
        tool_ = 'tools/b754_%s.py' % n_
        data_ = 'data/b754_%s.txt' % ('standing_v1330' if n_ == 'v1330_later' else n_)
        fa_ = _first_add(tool_)
        gens_ok_.append((n_, bool(fa_) and fa_ == g(ROOT, 'rev-parse', gens_[0]).strip()
                         and all(tool_ in files_(h_) and data_ not in files_(h_) for h_ in gens_) and data_ in files_(bank_) and tool_ not in files_(bank_)))
    gen_ = len(gens_ok_) == 7 and all(o_ for _n, o_ in gens_ok_)
    rule_ = files_(K.REG_RULE) == ['data/b754_registrations.txt'] and '## (2) THE TABLE' not in (g(ROOT, 'show', '%s:data/b754_registrations.txt' % K.REG_RULE) or '') \
        and '## (1) THE RULE' in (g(ROOT, 'show', '%s:data/b754_registrations.txt' % K.REG_RULE) or '') and 'data/b754_registrations.txt' in files_(K.REG_TABLE)
    sect_ = gen_ and rule_
    route_ = disch_ and sect_
    same_ = True
    regen_ = N2_REGEN in (rd(FACE) or '')
    tz = rdn('%s_prelock.txt' % ACT, optional=True)   # ### the gate writes the pre-lock bank after the score routes' dry form; read absent as empty
    fg_ = rdn('%s_pathrefusal.txt' % ACT)
#⟪END⟫
#⟪SECTION record 12⟫
    ok = route_ and same_ and regen_ and bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper() and '**THE PROBE-PATH REFUSAL : CLEAR' in fg_ and anc_ and order_ and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the weight and corrigendum (PLACE-papers %s) FINDINGS alone, no other PLACE-papers write before the v1.33.0 bank: %s; the registration`s rule (relay %s) committed alone, its blob carrying the rule and not the table, the table by the later commit (relay %s): %s; each generator first added by a commit of its own carrying it and not its bank, the bank`s commit not the generator (%s): %s; the (W) regeneration printed in the face: %s; the pre-lock comparison banked with the prev-mode dry: %s; the probe-path refusal banked and clear: %s; step zero, v1.33.0, the weight and corrigendum, the corrigendum banks, the rule and its table, Component 2`s opening commit, each read`s generator and bank, the agenda`s generator and bank, [M1], [D1], the waiver, the line, the v1.33.0 bank`s composer and the bank in that order by time: %s (%s), v1.33.0 an ancestor of the v1.33.0 bank`s commit and that of HEAD: %s; the tools` controls before their figures: %s' % (
            K.C1_PP[:8], disch_, K.REG_RULE, K.REG_TABLE, rule_, ', '.join('%s %s' % x_ for x_ in gens_ok_), gen_,
            regen_, bool(tz) and 'THE PRE-LOCK DRY IN PREV MODE' in tz.upper(),
            '**THE PROBE-PATH REFUSAL : CLEAR' in fg_, order_, ' '.join('%s@%d' % (h_[:8], c_) for (_r, h_), c_ in zip(chain_, tm_)), anc_,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (over b754's objects; b753's in git at b753's record tool): the banks whose grade prints at their end, (bank, the words the foot carries)
N3_GRADED = (('b754_standing_v1330.txt', ('v1.33.0: CONTROLS', 'ALL AS WANTED')),
             ('b754_registrations.txt', ('THE REGISTRATION: H-C3-LAW', ' ; NOT RUN ; ', 'NO FORM AND NO COEFFICIENT READ AT AN UNUSED DISCRIMINANT', 'NONE REGISTERED')),
             ('b754_kernels.txt', ('THE KERNELS RECONCILED', 'CONTROLS ALL AS WANTED')), ('b754_branch_map.txt', ('BRANCHES MAPPED', 'CONTROLS ALL AS WANTED')),
             ('b754_head_read.txt', ('THE HEAD READ', 'THE KNOWN INSTANCE AS WANTED', 'CONTROLS ALL AS WANTED')),
             ('b754_anchors.txt', ('ANCHORS READ', 'NONE EDITED', 'CONTROLS ALL AS WANTED')),
             ('b754_store.txt', ('THE STORE READ', 'THE TEMP DIRECTORY READ A CANDIDATE', 'CONTROLS ALL AS WANTED')),
             ('b754_agenda.txt', ('THE AGENDA: 2 ITEMS', 'NOTHING WRITTEN BEYOND THIS BANK', 'CONTROLS ALL AS WANTED')),
             ('b754_waiver.txt', ('THE WAIVER`S BANK', 'NO WORD OF ANY ROW PRINTED')),
             ('b754_line.txt', ('THE LINE: COMPOSED', 'STAGE CLUSTERED/BANKED', 'ALL AS READ')),
             ('b754_corrigendum.txt', ('ITEMS',)), ('b754_citation_check.txt', ('THE CHECK HALTED',)), ('b754_reproduce.txt', ('REPRODUCES',)), ('b754_address_scan.txt', ('PREVIOUS ADDRESS',)))
# ### the entry's last line, the INTEGRATION line, in canon XXIII (A)'s form, read from REGISTRY and SPIRAL_MAP with the match of v1.33.0
# ### through tools/b754_line.py (relay data/b754_line.txt (A)): the registration CLUSTERED in the Epstein instance, the reads BANKED, 0 of 6
# ### names matched (no keystone line written this act)
INTEGRATION_LINE = ('INTEGRATION: cluster the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23; SPIRAL_MAP cluster table :276) for the registration, no seat in the '
                    'cluster table for the refresh`s reads ; keystone THE_EPSTEIN_CONTROL_OBJECT_v0_1 (in progress) for the registration, none yet for the reads ; '
                    'stage CLUSTERED (the registration), BANKED (the reads)')
FIXED_SENTENCES = ()   # ### b754: no fixed sentence ordered by (R364)
# ### N3 (R364): the matchers over the act's own sentences and the entry's, each with its control, a planted sentence it must catch; the
# ### novelty matcher by its claim (a result, finding, theorem or proof called new, the earliest of its kind), not the bare word (the
# ### registration's "the earliest that can be negative" and the waiver's "the earliest commit past origin" are no claim)
N3_NEG = r'\b(?:NOT|not|no|No|NO|never|until|Until|nothing|Nothing|none|None|NONE|neither|Neither|unproven)\b'
N3_LIT = (r'\b(?:novel|priority|never before|for the first time|first (?:of its kind|ever|formal|machine)|earliest (?:of its kind|result|proof|instance|known)|'
          r'(?:new|novel) (?:result|finding|theorem|proof|discovery))\b')
N3_DEP = r'\b(?:deposited|published|versioned)\b'
N3_LOC = r'\b(?:RH|GRH|h2|ζ)\b.*\b(?:holds|fails|proved|refuted|moved)\b'
N3_BANKS = ('registrations', 'kernels', 'branch_map', 'head_read', 'anchors', 'store', 'agenda', 'waiver', 'line', 'rules', 'standing_v1330', 'events', 'defects')


def _own_sentences(t):
    """the act's own sentences of a bank: the quote rows (`  :n "...`) and the quoted spans dropped, the `### ` lines dropped."""
    ls = []
    for l in (t or '').replace(chr(13), '').split(NL):
        if not l.strip() or l.startswith('### ') or re.match(r'^\s+:\d+(?:-:\d+)? ["“]', l):
            continue
        ls.append(re.sub(r'“[^”\n]*”', '“…”', re.sub(r'"[^"\n]*"', '"…"', l)).strip())
    return [x for x in re.split(r'(?<=[.;])\s+', ' '.join(ls)) if x.strip()]


def _s_md5(path):
    import hashlib as _hl
    return _hl.md5(open(path, 'rb').read()).hexdigest()


def _section_body(n):
    """the paper's section n as PLACE-papers carries it at HEAD: the lines from its heading to the next heading."""
    t = (rd(os.path.join(PP, *K.SECTION_FILE.split('/'))) or '').replace(chr(13), '')
    i = t.find('\n## %d. ' % n)
    j = t.find('\n## %d.' % (n + 1), i + 1)
    return t[i + 1:j] if i >= 0 and j > i else ''


def _section_cites(bank):
    """the cites a section bank prints (tools/standing/citeprint.py's form): a head `  (n) [relay |PLACE-papers ]<path>[ at <rev>] :a[-:b]`,
    then its lines `      NNN  <text>`; returned (heads, [(where, path, rev, line, text)])."""
    sb_ = rdn(bank)
    reg_ = sb_[sb_.find('### EVERY CITE'):sb_.find('### THE CHECKS')]
    heads_, cites_, cur_ = [], [], None
    for l_ in reg_.split(NL):
        h_ = re.match(r'^  \((\d+)\) (?:(relay|PLACE-papers) )?(\S+)(?: at ([0-9A-Za-z]+))? :(\d+)(?:-:(\d+))?\s*$', l_)
        if h_:
            cur_ = (h_.group(2) or 'lean', h_.group(3), h_.group(4))
            heads_.append(h_.groups())
            continue
        p_ = re.match(r'^ {6,}(\d+)  (.*)$', l_)
        if cur_ and p_:
            cites_.append(cur_ + (p_.group(1), p_.group(2)))
    return heads_, cites_


def _cite_src(where, path, rev, n):
    """the source line a cite names, read from its tree: Lean at its revision under SIDEExplicitFormula/Schema/, the ledger in PLACE-papers at
    its revision, a relay bank from the working file."""
    if where == 'lean':
        s_ = _show(K.EF_DIR, rev, 'SIDEExplicitFormula/Schema/%s' % path) or ''
    elif where == 'PLACE-papers':
        s_ = g(PP, 'show', '%s:%s' % (rev or 'HEAD', path)) or ''
    else:
        s_ = rd(os.path.join(ROOT, *path.split('/'))) or ''
    s_ = s_.replace(chr(13), '').split(NL)
    return s_[int(n) - 1] if 0 < int(n) <= len(s_) else None
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R364): no sentence of the act says that anything of ζ, RH, GRH or h2 holds, fails or moved, outside a negation; no sentence says
    anything was deposited, published or versioned; no bank and no sentence of the entry calls a result new or the earliest of its kind; the
    registration read where it stands -- NOT RUN, no form and no coefficient read at an unused discriminant, the navigator's candidates
    carried and none registered; the hold's event saying a full volume is consistent with b753's event (6) and not proven; the temp directory
    read printed as a candidate; the anchors' counts summing (moved, standing, no later line found); each matcher's control caught; the
    entry's INTEGRATION line its last line, REGISTRY 1.5c-21 and SPIRAL_MAP's Epstein row read as they stand; the banks' nouns in the entry;
    the root prompt's sentences about the entry the composer's. From the banks' last lines and own sentences, REGISTRY at PLACE-papers HEAD,
    the entry's sentences and the root prompt in the answers bank."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].strip().startswith('### ### **') and all(w in last[0] for w in words)))   # ### b754: the call bank's feet indented two spaces, read stripped
#⟪END⟫
#⟪SECTION record 19⟫
    rules = ()
#⟪END⟫
#⟪SECTION record 20⟫
    # ### N3 over the act's own sentences (the banks' quote rows and quoted spans dropped) and the entry's, each matcher with its control
    _rl = lambda p_: (rd(os.path.join(PP, *p_.split('/'))) or '').replace(chr(13), '').split(NL)
    nsents_ = []
    for b_ in N3_BANKS:
        nsents_ += _own_sentences(rdn('%s_%s.txt' % (ACT, b_), optional=(b_ == 'events')))
    neg_ = N3_NEG
    ctl3_ = dict(lit=bool(re.search(N3_LIT, 'The walk is a new result.', re.I)), dep=bool(re.search(N3_DEP, 'The kernel was deposited.')),
                 loc=bool(re.search(N3_LOC, 'RH holds at every height.')), neg=bool(re.search(neg_, 'RH is not proved.')))
    more_ = [x for x in nsents_ + sents if re.search(N3_LIT, x, re.I) and not re.search(neg_, x)]
    dep_ = [x for x in nsents_ + sents if re.search(N3_DEP, x) and not re.search(neg_, x)]
    first_ = [x for x in sents if re.search(r'\b(?:first|earliest)\b', x, re.I) and re.search(r'\b(?:assistant|AI|model|machine)\b', x)]
    loc_ = [x for x in sents + nsents_ if re.search(N3_LOC, x) and not re.search(neg_, x)]
    rgt_ = rdn('%s_registrations.txt' % ACT)
    rgv_ = ([l_ for l_ in rgt_.split(NL) if l_.strip()][-1:] or [''])[0]
    said_ = ' ; NOT RUN ; ' in rgv_ and 'NO FORM AND NO COEFFICIENT READ AT AN UNUSED DISCRIMINANT' in rgv_ and 'NONE REGISTERED' in rgv_ \
        and "## (3) CARRIED BESIDE IT: THE NAVIGATOR'S CANDIDATE STATEMENTS, NONE REGISTERED, NONE RUN" in rgt_
    hold_ = 'consistent with a write lost to a full volume and not proven so' in ' '.join(rdn('%s_events.txt' % ACT, optional=True).split())
    cand_ = '## THE TEMP DIRECTORY READ -- A CANDIDATE AND NO FINDING' in rdn('%s_store.txt' % ACT)
    an_ = f['an_moved'] + f['an_stands'] + f['an_none'] == f['an_n']
    lines_ = [l for l in text.split(NL) if l.strip()]
    rg_ = _rl('REGISTRY.md')
    sm_ = rd(os.path.join(PP, 'SPIRAL_MAP.md')) or ''
    integ_ = __import__('standing.act', fromlist=['entry_ends_with']).entry_ends_with(text, INTEGRATION_LINE, conv) \
        and any(l.startswith('| 1.5c-21 |') for l in rg_) and '| **The Epstein instance** (seated 2026-11-09, b750) |' in sm_ and 'THE_EPSTEIN_CONTROL_OBJECT_v0_1.md' in sm_
    fixed_ = []
    nouns_ = [w_ for w_ in ('H-C3-LAW', '[M1]', '[D1]', 'v1.33.0', 'data/%s_registrations.txt' % ACT, 'data/%s_kernels.txt' % ACT, 'data/%s_branch_map.txt' % ACT,
                            'data/%s_head_read.txt' % ACT, 'data/%s_anchors.txt' % ACT, 'data/%s_store.txt' % ACT, 'data/%s_agenda.txt' % ACT,
                            'data/%s_waiver.txt' % ACT, 'data/%s_line.txt' % ACT) if w_ not in text]
    ans_ = rdn('%s_author_answers.txt' % ACT)
    pr_ = [l_.split('): ', 1)[1] for l_ in ans_.split(NL) if l_.startswith('### PROMPT ') and '): ' in l_][-1:]
    unb_ = __import__('standing.rootprompt', fromlist=['entry_unbacked']).entry_unbacked(pr_[0], text) if pr_ else None
    ok_rest = all(o for _n, o in graded) and all(ctl3_.values()) and said_ and hold_ and cand_ and an_ and not more_ and not dep_ and not first_ and not loc_ \
        and integ_ and not nouns_   # ### every clause but the root prompt's
    ok = ok_rest and unb_ == []
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the matchers` controls (a planted novelty, deposit and centre sentence each caught, a negation read): %s; the registration read where it stands -- NOT RUN, no form and no coefficient at an unused discriminant, the candidates carried and none registered: %s; the hold`s event saying a full volume consistent and not proven: %s; the temp directory read printed as a candidate: %s; the anchors` counts summing, %d moved, %d standing, %d with no later line found, of %d: %s; over %d of the act`s own sentences and the entry`s, a sentence calling a result new or the earliest of its kind outside a negation: %s; a sentence saying a thing was deposited, published or versioned outside a negation: %s; read from %s, a sentence of the entry calling the work the earliest of its kind in any assistant: %s; a sentence saying zeta, RH, GRH or h2 holds, fails or moved outside a negation: %s; the entry`s last line the INTEGRATION line, REGISTRY 1.5c-21 and SPIRAL_MAP`s Epstein row read: %s; the banks` nouns absent from the entry: %s; the root prompt`s sentences about the entry not the composer`s: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), ', '.join('%s %s' % kv_ for kv_ in sorted(ctl3_.items())), said_, hold_, cand_,
            f['an_moved'], f['an_stands'], f['an_none'], f['an_n'], an_, len(nsents_), more_ or 'NONE', dep_ or 'NONE', src, first_ or 'NONE', loc_ or 'NONE',
            integ_, nouns_ or 'NONE', 'UNREAD (no root prompt banked yet)' if unb_ is None else (unb_ or 'NONE')))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R364) N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build rewrites by the ferry's (W) list ((R364)(5))
# ### (R364)(2): the list read from tools/standing/act.py post_lock_appended, the one the lock gate prints: the answers pair and the check's output beside them
sys.path.append(os.path.join(ROOT, 'tools', 'standing'))
import act as STANDING_ACT   # noqa: E402
N4_APPENDED = STANDING_ACT.post_lock_appended(ACT)


def _post_lock_edits():
    """the lock commit by the one reader (the step bank's lock row) and its commit time, the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    # ### v1.26.0, (R356)(3)(ii): the lock commit by the one reader (tools/standing/lockdate.py, the lock row of data/<act>_steps.json), the
    # ### same reader the ceiling takes; the face's `locked at (UTC)` line no longer dates it
    import lockdate as LD
    lc = LD.lock_of(ACT, os.path.join(ROOT, 'data'))
    lock = LD.lock_epoch(lc, ROOT) if lc else None
    # ### v1.30.0, (R360)(3)(viii), b749 events (12): the lock's time printed from the one reader's epoch; b753's module left lock_iso unset and
    # ### its N4 sentence printed "the lock at NOT LOCKED" at every reading while lock_ok held
    out = dict(lock=lock, lock_iso=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)) if lock else None, lock_commit=lc, after=[], edited=[], dirty=[])
    if lc is None or lock is None:
        return out
    rows = [l.split(' ', 1) for l in g(ROOT, 'log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.PRE_RELAY).split(NL) if l.strip()]
    face_rel = os.path.relpath(FACE, ROOT).replace(os.sep, '/')
    tracked = set(x for x in g(ROOT, 'ls-tree', '-r', '--name-only', lc).split(NL) if x.strip())
    guard = lambda p: p not in N4_APPENDED and (p == face_rel or p.startswith('tools/') or (p.startswith('data/%s_' % ACT) and p in tracked))
    hs = [h for h, _ct in rows]
    out['after'] = hs[hs.index(lc) + 1:]
    for h in out['after']:
        for p in g(ROOT, 'show', '--name-only', '--format=', h).split():
            if guard(p):
                out['edited'].append('%s %s' % (h[:8], p))
    out['dirty'] = [p for p in g(ROOT, 'diff', '--name-only', 'HEAD').split() if guard(p)]
    return out
#⟪END⟫
#⟪SECTION record 23⟫
    # ### (R364) N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (b753's form, carried) -- read from git,
    # ### not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
# ### b754, defect (v): N5's SIDE-explicit-formula clause (record.tpl :2563-2564) wanted no tag past v0.37 and every kernel's tags as b753's face
# ### read them; (R364)(3) adds the one tag v0.38 at 14ca5725, so the clause reads that tag and no other: the tag sets equal but for v0.38 at
# ### 14ca572, main unmoved, the tags containing v0.37 exactly v0.37 and v0.38, v0.38 peeling to 14ca5725
#⟪OVERRIDE record MARK 82a559f5c96c 2⟫
    _ef_now, _ef_prev = now.get('SIDE-explicit-formula') or ['', {}], prev.get('SIDE-explicit-formula') or ['', {}]
    tag_one = _ef_now[0] == _ef_prev[0] and dict(_ef_now[1] or {}) == dict(dict(_ef_prev[1] or {}), **{'v0.38': '14ca572'})
    moved = [k_ for k_ in moved if not (k_ == 'SIDE-explicit-formula' and tag_one)]
    ef_ok = ef_main == K.EF_MAIN and sorted(t_ for t_ in g(K.EF_DIR, 'tag', '--contains', K.EF_V037).split() if t_.strip()) == ['v0.37', 'v0.38'] \
        and g(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'v0.38^{commit}').strip().startswith('14ca5725') and ch_ok \
        and bool(prev) and not moved and not pins_on_main
#⟪END⟫
#⟪OVERRIDE record MARK 68d2d745304d 1⟫
            'rebuild`s SIDE-frobenius commits on its main: %s; SIDE-explicit-formula`s main at 8fbab45d, the one tag past v0.37 v0.38 at 14ca5725 ((R364)(3)), the challenge branch %s at %s with no tag and '
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R364)(5), N5: no kernel's main touched -- every ref of every kernel carrying a commit made after the act's opening commit is a fault, a
    # ### listed push-* branch of the face's branch list excepted (none this act); no .lean file changed or untracked in a kernel's tree; the
    # ### rebuild-b721 branches kept as b753 left them; the address scan's count from its bank (relay data/b754_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    listed_ = [(r_.get('kernel'), r_.get('branch')) for r_ in __import__('standing.facebranches', fromlist=['listed']).listed(ACT)]   # ### v1.24.0, (R354)(2)(v): the face's branch list (none this act)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start and (kn, r_[0][len('refs/heads/'):]) not in listed_:
                # ### (R364)(4): zq-b730 of SIDE-explicit-formula at its tip, the act's one written branch, excepted (b742's form)
                if not (kn == 'SIDE-explicit-formula' and r_[0] == 'refs/heads/zq-b730' and r_[1] == K.ZQ_TIP):
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; THE ORCID: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.groups() == ('0', '0', '0', '0')
    # ### (R364)(6), N5: no release, no new version, no publish, no repository edit in the capture
    cmr_ = jl('%s_commands.json' % ACT).get('rows') or []
    ghr_ = [r_['n'] for r_ in cmr_ if re.search(r'\bgh\s+repo\s+edit\b', r_.get('cmd') or '')]
    # ### v1.30.0, (R360)(3)(vi), b749 defects (l), (q), (t): a release, a new version, a publish or a repository edit read from the act's Zenodo
    # ### banks alone (standing.act.zenodo_requests), not from captured commands nor from "the draft held at v5", the monograph's draft
    zr_ = __import__('standing.act', fromlist=['zenodo_requests']).zenodo_requests(ACT)
    ghe_ = ['%s :%d' % (b_, i_) for b_, i_, _t in zr_['releases']]
    # ### (R364)(6), N5: no Zenodo call this act -- no write request in any Zenodo bank, and no Zenodo bank written
    zdel_ = ['%s :%d %s' % (b_, i_, m_) for b_, i_, m_, _t in zr_['writes']] + list(zr_['banks'])
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok and not ghe_ and not ghr_ and not zdel_
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b754_address_scan.txt): PREVIOUS ADDRESS: %s; THE AUTHOR`S NAME: %s; PREVIOUS NAME: %s; THE ORCID: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than SIDE-explicit-formula`s zq-b730 at its tip (no kernel`s main touched; a push-* branch of the face`s list excepted, none this act), or a .lean file in a kernel`s tree (%d kernels read): %s; the %s branch kept on the wave 1 '
            'kernels: %d of %d; gh repo edit in the capture: %s; release, a new version, a publish or a repository`s edit in the Zenodo banks: %s; a Zenodo bank or write request this act (none ruled): %s; ' % (
                (addr.groups() if addr else ('UNREAD',) * 4) + (len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1),
                ghr_ or 'NONE', ghe_ or 'NONE', zdel_ or 'NONE')) +
#⟪END⟫
#⟪SECTION record 28⟫
    # ### b754 step zero: the ruling's ordinal and title (the ferry's ACT line, data/b754_ferry.txt :70) as delivered, to be adjusted at
    # ### Component 4 to what the act did, as the closing's TITLE_LINE reads it
    return ('### b754 — lane two, act one hundred and eighty-one, the sitting under (R364): b753 at its weight; the navigator`s corrections; '
            'the corrigendum opening on the four classes that repeated three acts running and on the post-seal events bank; the close`s yield and the anchors` kernel tags read; '
            'the reference layer`s four anchors and seven doors put; the quoting rule, the record`s upkeep, the census`s next edition, the handoff page, the project set, '
            'the update channel and the carried lines put; the sourcing rules entered; nothing built and nothing computed')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 4 result sentence adjusted to what the act did: the registration H-C3-LAW
    registered and not run, its rows, controls and tests; the kernels reconciled; the criterion kernel's branches mapped and those off main;
    the front doors' heads read and those not agreeing; the reference layer's anchors read and those moved by a later line; the transcript
    store read by its sessions; [M1] and [D1] passed; v1.33.0's controls landed; nothing built. Each finding's name in the heading, for the
    line reader. Every figure from the banks (the registration's foot, the five reads' feet, the answers bank's RESULT row, v1.33.0's
    controls)."""
#⟪END⟫
#⟪SECTION record 31⟫
    ctl_ = [r_.strip('()') for r_ in f['v1130_ctl'].split(', ')]
    if not all(c_ in ctl_ for c_ in ('gitwrite', 'subject', 'outbound', 'chain', 'version')) or int(f['v1130_cases']) != int(f['v1130_wanted']):
        sys.exit('### v1.33.0`S CONTROLS DO NOT NAME (gitwrite), (subject), (outbound), (chain) AND (version), ALL AS WANTED -- NOTHING COMPOSED')
    if f['rules_rows'] != [1, 2] or (f['m1'], f['d1']) != ('Passed', 'Passed as (a)'):
        sys.exit('### THE RULES BANK`S ROWS ARE NOT (1)-(2) OR THE ANSWERS ON [M1] AND [D1] NOT AS READ -- NOTHING COMPOSED')
    if not f['ln_ok'] or f['rg_run'] != 'NOT RUN' or f['rg_ctl'] + f['rg_tests'] != f['rg_rows'] or f['an_moved'] + f['an_stands'] + f['an_none'] != f['an_n'] \
            or [h_[:8] for h_, _t in f['later']] != [x_[:8] for x_ in K.C1_STANDING_LATER] or f['ro_n'] != f['ro_wanted']:
        sys.exit('### THE LINE BANK, THE REGISTRATION, THE ANCHORS` COUNTS OR THE v1.33.0 BANK`S LATER COMMITS NOT AS READ -- NOTHING COMPOSED')
    return ('## H-C3-LAW, the class-number-3 walk, registered and not run (b754_registrations): %d rows, %d controls and %d tests, the candidates carried; '
            '%d kernels reconciled against the lists (b754_kernels); the criterion kernel’s %d branches mapped, %d off main (b754_branch_map); '
            '%d front doors’ heads read, %d not agreeing (b754_head_read); the reference layer’s %d anchors read, %d moved by a later line (b754_anchors); '
            'the transcript store read, %d sessions (b754_store); [M1] and [D1] passed (b754_agenda); v1.33.0’s %d controls landed; nothing built' % (
                f['rg_rows'], f['rg_ctl'], f['rg_tests'], f['kn_n'], f['bm_n'], f['bm_off'], f['hr_doors'], f['hr_notagree'], f['an_n'], f['an_moved'],
                f['sr_sessions'], len(ctl_)))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    return ('(1) the line`s stages, the seat`s reading of canon XXIII (B): the registration CLUSTERED (the Epstein cluster names its keystone, which carries none of the registration`s names) and the five reads BANKED (no row or block of the maps names any of them), printed and entered in no map (relay data/b754_line.txt (B)); '
            '(2) the v1.33.0 bank`s later commits named by a per-act composer run after them (relay tools/b754_v1330_later.py), not by a change to a standing tool, the seat`s reading of the author`s sixth word (4) (relay data/b754_standing_v1330.txt); '
            '(3) [D1]’s key taken as binding from the harness`s next start, the documentation read not saying when a change of it binds, its effect not tested by this act (relay data/b754_rules.txt (2)); '
            '(4) the answers route`s word rows, each paragraph of a word written once by tools/standing/authorwords.py since v1.34.0 ((R364)(3)(xiv); its control in relay data/b754_standing_v1340.txt), b753`s pushed answers bank not rewritten; '
            +
            '(5) %s and the seat’s %s defect%s as lettered' % (
#⟪END⟫
#⟪SECTION record 33⟫
def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):   # ### b754: the events bank written after the seal, read optional before it (v1.27.0's rdn refuses a missing file)
        rows += [l for l in rdn(name, optional=name.endswith('_events.txt')).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    return sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l)), len(rows)


def _runs3(act=ACT):
    """v9 row (83): "a class that repeats in three acts running is the next act's opening component" -- each row of the act's defects bank
    tagged REPEAT <the previous act> (<letter>) whose row in the previous act's defects bank is itself tagged REPEAT <the act before> (...):
    a list of (this act's letter, 'b<n-2> (x) -> b<n-1> (y) -> b<n> (z)'). A REPEAT naming an older act, a class, or no letter, is not a run
    of three."""
    n = int(act[1:])
    p1, p2 = 'b%d' % (n - 1), 'b%d' % (n - 2)
    tag = re.compile(r"^    \(([a-z]'?)\) THE (?:SEAT|NAVIGATOR)'S \[(?:CLAIM|CLOSE) ; REPEAT (b\d+) \(([a-z]'?)\)\]")
    prev = dict((m.group(1), m) for m in (tag.match(l) for l in rdn('%s_defects.txt' % p1).split(NL)) if m)
    out = []
    for l in rdn('%s_defects.txt' % act).split(NL):
        m = tag.match(l)
        if m and m.group(2) == p1 and m.group(3) in prev and prev[m.group(3)].group(2) == p2:
            out.append((m.group(1), '%s (%s) -> %s (%s) -> %s (%s)' % (p2, prev[m.group(3)].group(3), p1, m.group(3), act, m.group(1))))
    return out


def _runs3_line():
    """the rows of _runs3 grouped by the class's row two acts back, each class once with this act's rows under it."""
    r = _runs3()
    by = {}
    for l, c in r:
        by.setdefault(c.split(' -> ')[0], []).append(l)
    return ('the classes repeating three acts running, by the tags (v9 row (83), each the next act’s opening component, printed for the '
            'author beside the next act of %s): %d rows in %d classes -- %s' % (__import__('standing.cites', fromlist=['next_clause']).next_clause(rdn('%s_ferry.txt' % ACT)) or '(R364)(7)', len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (over b754's objects; b753's composer in git at
    b753's record tool). Its last line the INTEGRATION line (Component 4)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    if (f['m1'], f['d1']) != ('Passed', 'Passed as (a)'):
        sys.exit('### THE ANSWERS BANK DOES NOT CARRY THE AUTHOR`S WORDS ON [M1] AND [D1] AS READ -- NOTHING COMPOSED')
    rep, tot = _repeats()
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    cc = re.search(r'(?m)^### ### \*\*CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)\.\*\*', rdn(K.CITATION_BANK))   # ### the bank's foot
    checks = __import__('standing.nouns', fromlist=['answer_checks']).answer_checks(rdn('%s_answer_check.txt' % ACT))   # ### v1.10.0, (R363)(2)(v)
    co_ = jl('%s_corrigendum.json' % ACT)
    lt_ = ', '.join('%s (%s)' % (h_, t_) for h_, t_ in f['later'])
    gb_ = '; '.join('%s %s then %s' % (n_, gens_[-1], bank_) for n_, gens_, bank_ in K.C2_READS)
    e = ['', _title(), '',
         'The class-number-3 walk is registered and not run. Its rule, H-C3-LAW, was committed alone (relay %s) before its table of %d rows -- %d controls and %d tests -- by a commit of its own (relay %s); the value the rule predicts is printed at every row; no form and no coefficient was read at an unused discriminant; the navigator’s candidate statements (a)-(%s) are carried beside it, none registered and none run (relay data/b754_registrations.txt). The system was read by five reads, each generator committed before its bank: %d repositories reconciled against the lists, %d local heads not their remote main (relay data/b754_kernels.txt); the criterion kernel’s %d remote branches mapped against main, %d off main (relay data/b754_branch_map.txt); %d front doors’ heads read against the registry and the descriptions, %d agreeing and %d not (relay data/b754_head_read.txt); the reference layer’s %d anchors read against the ledgers’ later lines, %d moved by a later line, none edited (relay data/b754_anchors.txt); the transcript store read by names, sizes and dates, %d sessions (relay data/b754_store.txt). [M1] and [D1] were put once and passed: the mirror’s roster gains seven families, %d entries to %d, and the harness’s background updating is switched off for the seat (relay data/b754_rules.txt).' % (
             f['rg_rule'], f['rg_rows'], f['rg_ctl'], f['rg_tests'], K.REG_TABLE, f['rg_cand'], f['kn_n'], f['kn_late'], f['bm_n'], f['bm_off'], f['hr_doors'],
             f['hr_agrees'], f['hr_notagree'], f['an_n'], f['an_moved'], f['sr_sessions'], f['ag_roster'][0], f['ag_roster'][1]), '',
         '*Filed at b754 on the author’s ruling `(R364)`; %d question%s put before the root%s. Banks: relay '
         '`data/b754_corrigendum.txt`, `data/b754_standing_v1330.txt`, `data/b754_rules.txt`, `data/b754_registrations.txt`, `data/b754_kernels.txt`, `data/b754_branch_map.txt`, '
         '`data/b754_head_read.txt`, `data/b754_anchors.txt`, `data/b754_store.txt`, `data/b754_agenda.txt`, `data/b754_put_2.json`, `data/b754_author_answers.txt`, '
         '`data/b754_waiver.txt`, `data/b754_events.txt`, `data/b754_line.txt`, `data/b754_prelock.txt`, `data/b754_pathrefusal.txt`, '
         '`data/b754_reproduce.txt`, `data/b754_address_scan.txt`, `data/b754_touch.txt`, `data/b754_standing_figures.txt`, `data/b754_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's', (
             ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
         '**The corrigendum and the carried items** ((R364)(1), (2), (7); %s, %s, %s): b753 entered at its weight (FINDINGS :%s); '
         'the corrigendum of b753’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- with %d entered beside them, the author’s root answer and the navigator’s correction among them, '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s) (relay data/b754_corrigendum.txt); tools/standing/ at %s by a commit of its own, its controls '
         '%s -- %s cases, %s as wanted, each failing before its repair and passing after; the commits after its own at which a standing tool changed, %s, named in its bank with the controls run after them, the roster`s %d of %d among them, the version staying %s by the author’s sixth word (4) (relay data/b754_standing_v1330.txt).' % (
             K.C1_STANDING[:8], K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'],
             f['corr_claim'], f['corr_close'], f['corr_repeat'], len(co_.get('entered') or []), f['corr_line'], f['corr_row'], f['ver'], f['v1130_ctl'], f['v1130_cases'],
             f['v1130_wanted'], lt_, f['ro_wanted'], f['ro_n'], f['ver']), '',
         '**The registration** ((R364)(4), N2, N3): H-C3-LAW, the rule committed alone at relay %s and its table by the later commit at relay %s, both before any walk; %d rows, %d controls and %d tests, the predicted value %s at every row; NOT RUN this act, no form and no coefficient read at an unused class-number-3 discriminant; the navigator’s candidate statements (a)-(%s) carried beside it, none registered and none run, each to be reproduced with a planted error at the walk’s act (relay data/b754_registrations.txt).' % (
             f['rg_rule'], K.REG_TABLE, f['rg_rows'], f['rg_ctl'], f['rg_tests'], f['rg_value'], f['rg_cand']), '',
         '**The reads** ((R364)(5), N2, N5): each read by a generator committed before its bank, each bank’s controls printed before any figure; of a private repository other than PLACE-papers, names, sizes, dates and hashes alone. '
         '(i) The kernels: %d repositories of the lists and of D:, each remote read once by ls-remote, %d answered and %d failed, %d on D:, %d absent from a list, %d local heads not the remote main (relay data/b754_kernels.txt). '
         '(ii) The criterion kernel’s branches: %d at the remote, %d off main (%s), %d merged; the results of record off main %d of %d; the four branches of record pair by pair, %d of %d sharing a module; the twin read, no declaration on any branch found relating them (relay data/b754_branch_map.txt). '
         '(iii) The front doors’ heads: %d READMEs read, %d quoted, %d agreeing and %d not, %d private and not quoted, %d descriptions differing from their heads, %d with no README or not read; the known instance as wanted (relay data/b754_head_read.txt). '
         '(iv) The reference layer’s anchors: %d read against the ledgers’ later lines, %d moved by a later line, %d standing, %d with no later line found, none edited (relay data/b754_anchors.txt). '
         '(v) The transcript store: %d sessions read by names, sizes and dates; of the %d session ids the tools name %d absent and %d a near twin; of the %d the banks’ keys name %d absent; %d readers of an absent file, %d guarded and going on; %d scratch folders named with a root, %d gone; the hold’s four reads reproduced, two of them naming fewer than this read finds (2 of the absent ids, 3 of the 6 gone folders whose transcripts stand); the temp directory read a candidate and no finding (relay data/b754_store.txt).' % (
             f['kn_n'], f['kn_ans'], f['kn_fail'], f['kn_d'], f['kn_absent'], f['kn_late'], f['bm_n'], f['bm_off'], f['bm_offnames'], f['bm_merged'], f['bm_rec'][0], f['bm_rec'][1],
             f['bm_pairs'][0], f['bm_pairs'][1], f['hr_doors'], f['hr_quoted'], f['hr_agrees'], f['hr_notagree'], f['hr_private'], f['hr_descdiff'], f['hr_noreadme'],
             f['an_n'], f['an_moved'], f['an_stands'], f['an_none'], f['sr_sessions'], f['sr_ids'], f['sr_absent'], f['sr_twin'], f['sr_keys'], f['sr_keys_absent'],
             f['sr_readers'], f['sr_guarded'], f['sr_scratch'], f['sr_gone']), '',
         '**The agenda** ((R364)(6)): the two kept items banked with every current read and draft before either was put, %d items, [M1] drafting %d families and the roster %d -> %d, [D1] %d forms (relay data/b754_agenda.txt); put once (relay data/b754_put_2.json) and answered: [M1] %s -- the roster gains seven families in a list of their own beside the unedited base roster, read by the roster tool after the base roster’s entries and joins, its controls %d of %d (relay data/b754_rules.txt (1)); [D1] %s -- the harness’s background updating switched off for the seat by the one settings key, its name read from the harness’s documentation before the write, its effect not tested by this act (relay data/b754_rules.txt (2)); the answers banked by the record tool’s route (relay data/b754_author_answers.txt). The rest of the agenda, and (5)(v) and (5)(vi), carried to the sitting on the author’s word.' % (
             f['ag_items'], f['ag_fams'], f['ag_roster'][0], f['ag_roster'][1], f['ag_forms'], f['m1'], f['ro_wanted'], f['ro_n'], f['d1']), '',
         '**The hold and the waiver** ((R364)(7)(vii); the author’s sixth to ninth words): the hold of 2026-11-11 entered as the act’s opening event, b753’s event (6) consistent with a write lost to a full volume and not proven so (relay data/b754_events.txt (1)); the model of the seat changed on the author’s word and changed back on it (events (3), (6)); the act stopped before Component 4 by the author’s sixth word over words of PLACE-papers carried into the public relay, and the stop lifted by the eighth: the commits stand as they are and nothing is dropped, the words of PLACE-papers the act’s banks, tools and commit subjects carry going out with their commits, counted by class and not row by row -- %d anchors (A %d, B %d, C %d, D %d, E %d), %d rows outside the anchors bank and the head read’s %d -- no word of any row printed (relay data/b754_events.txt (5), data/b754_waiver.txt).' % (
             (f['wv_anchors'],) + f['wv_classes'] + (f['wv_rows'], f['wv_head'])), '',
         '**The integration line** (Component 4): this entry’s line read by tools/b754_line.py from REGISTRY and SPIRAL_MAP with the match of tools/standing/linematch.py: the registration CLUSTERED in the Epstein instance (REGISTRY 1.5c-21 to 1.5c-23), the keystone %s carrying none of its names; the five reads BANKED, %d names, %d seated in the cluster table; %d of %d names matched; no keystone line written this act (relay data/b754_line.txt); the earlier entries’ lines read again, %d of them, none rewritten.' % (
             f['ln_keystone'], f['ln_names'], f['ln_seated'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '',
         '**The order of the act** (N2): step zero at %s; %s at %s; the weight and corrigendum at PLACE-papers %s and relay %s; the registration’s rule at relay %s and its table at %s; each read’s generator before its bank (%s); the agenda’s generator at %s and its bank at %s, before either item; [M1] at %s and [D1] at %s; the waiver’s bank at %s; the line bank at %s; the v1.33.0 bank’s composer at %s and the bank at %s; the per-commit scan to its own bank at every commit; the tools’ controls before their figures; the pre-lock comparison with the dry in both modes, and the probe-path refusal, printed before the lock gate (relay data/b754_prelock.txt, data/b754_pathrefusal.txt). No lean process on this host and no runner dispatch.' % (
             K.STEPZERO_BANKS, f['ver'], K.C1_STANDING[:8], K.C1_PP[:8], K.C1_RELAY[:8], K.REG_RULE, K.REG_TABLE, gb_, K.C3_AGENDA[0], K.C3_AGENDA[1],
             K.C3_ITEMS[0][1], K.C3_ITEMS[1][1], K.C3_WAIVER, K.C4_LINE, K.C4_V1330[0], K.C4_V1330[1]), '',
         '**What this act is not**: nothing built; no walk run, no form and no coefficient read at an unused discriminant; nothing deposits; no new version; no draft published; no Zenodo call; no kernel’s main touched, no branch merged, no tag beyond v0.38, no Lean file written, no dispatch; no README, description, door, anchor or ledger row edited; no order entered; no paper written.', '',
         '**The research instruments reproduced** (the standing arm G-RESEARCH-REPRODUCES): tools/research/reproduce.py over the entered '
         'instruments, %s rows: %d REPRODUCES, %s DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at '
         '%s of %s (relay data/b754_reproduce.txt).' % (
             f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** (N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, the ORCID %s, over %s places, its seven controls as wanted (relay data/b754_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['orcid'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b754_touch.txt). The act’s counter CLAIM %d, CLOSE %d, REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b754 -- %s, %s, %s, %s -- against b753’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b754_standing_figures.txt); standing arms added %d.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each printed; the check halted on one Lean-path row, read in the step-zero bank, no word of the ruling wrong (relay data/b754_citation_check.txt, data/b754_stepzero.txt); %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the five reads read one way: the lists, the branches and the front doors are out of step with one another in the places the kernels, the branch map and the head read name, the reference layer stands where no later line reaches it, and most of the session ids the tools name are gone from the store; each is carried to the sitting as an item, and none is a finding about the mathematics the registration waits on.', '',
         '**Carried to:** %s, per (R364)(8) and the author’s words: the sitting, with the items of (R364)(6) the author’s word carried -- [C1], [H1], [M2], [L1] and onward, and (5)(v) and (5)(vi) -- the quote-versus-digest line; the four anchors moved by a later line, FINDINGS :901 and :979 first, and PLACE-papers’ description with them; the doors not AGREES; I-109’s cross-reference to I-106, I-108 and data/b711_coeffs.txt; the Epstein document’s section 8; the items (R363)(8) carried; the navigator’s candidates (a)-(%s); the temp directory read, the hook’s ledger and git-write state beside it; then the class-number-3 walk against its registration and the build of T0 and T1, in the acts their ruling names; W-ORD-VISIBILITY, CARRIED NOT CLEAN; the instruments NOT RUN, each with its price; the draft held at v5.' % (
             K.NEXT_ACT, f['rg_cand']), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '',
         INTEGRATION_LINE, '']
    return _title(), NL.join(e)


def _finding_text_b753():
    """b753's form over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (over b754's objects; b753's composer in git at b753's record tool): the open-orders line written from
    tools/standing/orders.py's output over the trail at HEAD; the registration, the reads, the agenda, the hold and the waiver; the line."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    _qc_, _aa_ = __import__('standing.act', fromlist=['question_count']).question_count, rdn('%s_author_answers.txt' % ACT)
    _rf_ = [b for b in re.split(r'(?m)^(?=### CALL )', _aa_) if b.startswith('### CALL ') and re.search(r'(?m)^RESULT [^\n]*hook error: REFUSED', b)]   # ### b754 touch row (2): a call the hook refused before it was shown
    n_ref = sum(_qc_(b)['prompts'] for b in _rf_)
    n_ans = _qc_(_aa_)['prompts'] - n_ref   # ### v1.30.0, (R360)(3)(vii): the composed prompts' rows, the sitting rows read apart; the refused call's read apart
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    two = []
    op = ORD.report(ORD.read(ORD.trail('HEAD') + two), 'HEAD')[1]
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R364) ratified.** Its components as the ferry orders them (relay data/b754_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b753’s weight), :%s (the corrigendum), :%s (the entry); no order entered; no paper written; this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             '**The registration:** H-C3-LAW, the rule at relay %s before its table at %s, %d rows (%d controls, %d tests), NOT RUN; the navigator’s candidates (a)-(%s) carried, none registered (relay data/b754_registrations.txt).' % (
                 f['rg_rule'], K.REG_TABLE, f['rg_rows'], f['rg_ctl'], f['rg_tests'], f['rg_cand']), '',
             '**The reads:** the kernels %d, answered %d, %d local heads not the remote main (relay data/b754_kernels.txt); the criterion kernel’s branches %d, off main %d (relay data/b754_branch_map.txt); the front doors %d, not agreeing %d (relay data/b754_head_read.txt); the anchors %d, moved by a later line %d, none edited (relay data/b754_anchors.txt); the store %d sessions, the tools’ ids absent %d of %d (relay data/b754_store.txt).' % (
                 f['kn_n'], f['kn_ans'], f['kn_late'], f['bm_n'], f['bm_off'], f['hr_doors'], f['hr_notagree'], f['an_n'], f['an_moved'], f['sr_sessions'], f['sr_absent'], f['sr_ids']), '',
             '**The agenda:** [M1] %s, the roster %d -> %d; [D1] %s, the one settings key (relay data/b754_agenda.txt, data/b754_rules.txt, data/b754_author_answers.txt).' % (
                 f['m1'], f['ag_roster'][0], f['ag_roster'][1], f['d1']), '',
             '**The hold and the waiver:** the hold of 2026-11-11 the act’s opening event; the stop before Component 4 and the author’s waiver by class, %d anchors and %d rows outside the anchors bank, no word of any row printed; the model changed and changed back on the author’s word (relay data/b754_events.txt (1), (3), (5), (6), data/b754_waiver.txt).' % (
                 f['wv_anchors'], f['wv_rows']), '',
             '**The integration line:** b754’s at the foot of its entry, the registration CLUSTERED in the Epstein instance, keystone %s, the reads BANKED, %d of %d matched (relay data/b754_line.txt); the earlier lines read again %d, none rewritten.' % (
                 f['ln_keystone'], f['ln_matched'], f['ln_of'], f['ln_earlier']), '']
    rows_ += [
             ORD.open_line(op), '',
             '**The orders by the tool:** %d of %s open at PLACE-papers main with the lines above, the open-orders line from tools/standing/orders.py`s output (its entry read outside quotations and hand sections, v1.27.0; a row ID`s token no order, v1.32.0).' % (
                 len(op), len(ORD.read(ORD.trail('HEAD') + two))), '',
             '**The carried items:** tools/standing/ at %s, its controls %s cases, %s as wanted, the commits after its own named with the controls run after them (relay data/b754_standing_v1330.txt); the two rules (relay data/b754_rules.txt).' % (
                 f['ver'], f['v1130_cases'], f['v1130_wanted']), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b754_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s, the ORCID %s (relay data/b754_address_scan.txt).' % (f['addr'], f['orcid']), '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b754_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d, the closing carries the last figure; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b754 `%s` (previous `%s`, b753’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root%s (relay data/b754_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()) - len(_rf_), '' if len(_calls()) - len(_rf_) == 1 else 's', (
                     ' (and %d refused at the hook before it was shown, put again through the composer)' % n_ref) if n_ref else ''), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b754_standing_v1330.txt); the standing '
             'report tool (relay data/b754_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel`s main touched; no Lean file written; no tag beyond v0.38; SIDE-explicit-formula`s main at %s unmoved, zq-b730 at %s unmoved; no runner dispatch; the %s branches as b753 left them; port-b707 at %s, kept, '
              'its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process on this host.' % (
                  K.EF_MAIN[:8], K.ZQ_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, the base roster`s entries and the seven of [M1], its name in the '
              'closing (relay data/b754_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b753’s %s, %s, %s, %s (relay data/b754_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b754_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b753():
    """b753's trail record over b753's objects, kept for the record and not called."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none this act; MEASURED off the command bank (each dispatch command at a command`s head).'),
    ('runner runs read by their ids', 'EFRUNS', 'EFRUNS', 'runs', '### N1: none; MEASURED off the worklist`s EF_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b733*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act.'),
    ('working branches on SIDE-explicit-formula', 'EFBRANCHES', 'EFBRANCHES', 'branches', '### keiper-b725, c2-b725, detect-b729 and zq-b730 kept, unmoved; MEASURED off its refs/heads against the worklist`s EF_BRANCHES.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### as b753 left them, the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b733*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b723`s; MEASURED off each branch against its pin.'),
    ('Lean files on SIDE-explicit-formula`s four branches', 'EFLEAN', 'EFLEAN', 'files', '### b725`s, b726`s and b730-b745`s, none this act; MEASURED off each branch against main.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: none; no kernel`s main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### relay push-b753-closing, push-b753-preroot, push-b753-record; PLACE-papers push-b753-preroot, push-b753-record; SIDE-explicit-formula carrying no push-* branch; each local, by name, each after its --merged listing (data/b754_stepzero.txt :90-:95).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s kernel commits', 0, 0, 'files', '### none: no kernel commit this act.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s and b723`s, none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none: REGISTRY not written this act ((R364)(6)).'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R364)(1), (7): FINDINGS :14912.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R364)(7): row (73).'),
    ('ERRATA entries filed', 0, 0, 'entries', '### none this act ((R364)(10)).'),
    ('sitting items decided', 2, 2, 'items', '### (R364)(6): the two kept items, [M1] passed and [D1] passed as (a) (relay data/b754_agenda.txt, data/b754_rules.txt, data/b754_author_answers.txt); the rest of the agenda carried to the sitting on the author`s word.'),
    ('orders entered with the trail', 0, 0, 'orders', '### none: (R364) enters no order.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the standing arm G-RESEARCH-REPRODUCES: tools/research/reproduce.py; MEASURED off data/b754_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### v1.33.0`s controls, the registration, the five reads, the agenda, the waiver`s bank, the line, the probe-path refusal, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### (R364)(4): the rule H-C3-LAW at 4c86bf24, the registrations bank alone; its table at 3f865479 with the step rows and the scan`s bank beside it; MEASURED off git, the bank`s commits whose files are the bank alone.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### none: the walk NOT RUN, no figure bank of the registered object; MEASURED.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### none (N2).'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean modules written on the act`s branches', 'EFNEW', 'EFNEW', 'modules', '### none: no Lean file written ((R364)(6)); MEASURED off each branch`s tip against its tip entering the act.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R364)(7): tools/standing/ to v1.33.0, each repair with its control, and the two later commits (chain.py and v1330.py at 0f31d31d, roster.py at 0db31ce3) with the controls run after them (data/b754_standing_v1330.txt); MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 0, 0, 'arms', '### none: the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 3, 3, 'banks', '### data/act_current.json at step zero; the corrigenda bank, appended; data/act_roots.txt at the root; data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part and computation; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### N5: PREVIOUS ADDRESS 0; MEASURED off data/b754_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: the outbound reads are the pushes and their ls-remote read-backs, the kernels` ls-remote reads, the gh reads under the GitHub login and the harness documentation read at [D1]`s pass; none carries an identifier; no description written.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and bool(K.REG_COMMIT) and c != K.REG_COMMIT \
            and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### b754: no registered object; no figure bank of one
    fig_banks = [p for p in ()
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    EFRUNS=len(K.EF_RUNS),
                    REPROWS=jcount('b754_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b754_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    EFBRANCHES=sum(1 for b, t in K.EF_BRANCHES if _git(K.EF_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip() == t),
                    EFLEAN=sum(1 for _b, t in K.EF_BRANCHES for f_ in _git(K.EF_DIR, 'diff', '--name-only', K.EF_BASE, t).split() if f_.endswith('.lean')),
                    EFNEW=sum(1 for (_b, t), p_ in zip(K.EF_BRANCHES, K.EF_BRANCHES_ENTERING) for f_ in _git(K.EF_DIR, 'diff', '--name-only', p_, t).split() if f_.endswith('.lean')),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('standing_v1330', 'registrations', 'kernels', 'branch_map', 'head_read', 'anchors', 'store', 'agenda', 'waiver', 'line',
                                               'pathrefusal', 'reproduce', 'address_scan')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b754_%s.txt' % n_))]),
                    REGALONE=len([c_ for c_ in _git(ROOT, 'log', '--format=%H', '--', 'data/b754_registrations.txt').split() if alone(c_)]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'EFBRANCHES', 'EFLEAN', 'EFNEW', 'EFRUNS', 'REPROWS', 'ADDRESS',
              'CHBRANCH', 'REGREMOVED', 'REGALONE',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b754_registration_%s.txt -- b754, THE SYSTEM REFRESH: b753 AT ITS WEIGHT AND ITS CORRIGENDUM; v1.33.0; "
                             "THE CLASS-NUMBER-3 WALK REGISTERED, NOT RUN; THE FIVE READS; THE AGENDA, [M1] AND [D1] PASSED; THE HOLD AND THE WAIVER; "
                             "THE INTEGRATION LINE; NOTHING BUILT, UNDER (R364)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b753's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten for b754: b753's lines read banks this
act does not write, and are not carried; the lines are b754's: tools/standing/ v1.33.0 by its controls (CERTIFIED), the registration, the five
reads, the agenda and the INTEGRATION line by their banks (REGISTERED), and the draft (HELD); no line stands on KERNEL (no Lean this act).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b754's lines, each from the record tool's figures over b754's banks
    # ------------------------------------------------------------------ REGISTERED: (R364)(4), the registration, read from its bank
    sz = seat('%s_registrations.txt' % ACT, '**THE REGISTRATION: H-C3-LAW')
    sk = sz   # ### (R363)(2)(ii): the name the template appends
    keys['REG'] = ('REGISTERED -- THE REGISTRATION: H-C3-LAW, the class-number-3 walk, the rule at relay %s before its table at %s; %d rows, %d controls and %d tests; NOT RUN, no form and no coefficient read at an unused discriminant; the candidates (a)-(%s) carried, none registered. SOURCE %s.' % (
        f['rg_rule'], K.REG_TABLE, f['rg_rows'], f['rg_ctl'], f['rg_tests'], f['rg_cand'], sz['text']))
    # ------------------------------------------------------------------ REGISTERED: (R364)(5), the five reads, each from its bank
    rd_ = dict((n_, (gens_[-1], bank_)) for n_, gens_, bank_ in K.C2_READS)
    sa = seat('%s_kernels.txt' % ACT, '**THE KERNELS RECONCILED: ')
    keys['KERNELS'] = ('REGISTERED -- THE KERNELS: %d repositories reconciled against the lists, each remote read once, %d answered, %d failed, %d on D:, %d absent from a list, %d local heads not the remote main; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['kn_n'], f['kn_ans'], f['kn_fail'], f['kn_d'], f['kn_absent'], f['kn_late'], rd_['kernels'][0], rd_['kernels'][1], sa['text']))
    seats.append(sa)
    sb = seat('%s_branch_map.txt' % ACT, '**THE CRITERION KERNEL`S BRANCHES MAPPED: ')
    keys['BRANCHES'] = ('REGISTERED -- THE BRANCH MAP: the criterion kernel`s %d remote branches, %d off main, %d merged; the results of record off main %d of %d; of the four branches of record, %d of %d pairs sharing a module; the twin read, no relating declaration found; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['bm_n'], f['bm_off'], f['bm_merged'], f['bm_rec'][0], f['bm_rec'][1], f['bm_pairs'][0], f['bm_pairs'][1], rd_['branch_map'][0], rd_['branch_map'][1], sb['text']))
    seats.append(sb)
    sc = seat('%s_head_read.txt' % ACT, '**THE HEAD READ: ')
    keys['HEADS'] = ('REGISTERED -- THE HEAD READ: %d front doors` READMEs read, %d quoted, %d agreeing and %d not, %d private and not quoted, %d descriptions differing from their heads; the known instance as wanted; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['hr_doors'], f['hr_quoted'], f['hr_agrees'], f['hr_notagree'], f['hr_private'], f['hr_descdiff'], rd_['head_read'][0], rd_['head_read'][1], sc['text']))
    seats.append(sc)
    sd = seat('%s_anchors.txt' % ACT, '**THE REFERENCE LAYER`S ANCHORS READ: ')
    keys['ANCHORS'] = ('REGISTERED -- THE ANCHORS: the reference layer`s %d anchors read against the ledgers` later lines, %d moved by a later line, %d standing, %d with no later line found, none edited; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['an_n'], f['an_moved'], f['an_stands'], f['an_none'], rd_['anchors'][0], rd_['anchors'][1], sd['text']))
    seats.append(sd)
    se = seat('%s_store.txt' % ACT, '**THE STORE READ: ')
    keys['STORE'] = ('REGISTERED -- THE STORE READ: %d sessions read by names, sizes and dates; of the %d session ids the tools name %d absent; the temp directory read a candidate and no finding; the generator at relay %s, the bank at %s. SOURCE %s.' % (
        f['sr_sessions'], f['sr_ids'], f['sr_absent'], rd_['store'][0], rd_['store'][1], se['text']))
    seats.append(se)
    # ------------------------------------------------------------------ REGISTERED: (R364)(6), the agenda, its two items and the answers
    sf = seat('%s_agenda.txt' % ACT, '**THE AGENDA: ')
    keys['AGENDA'] = ('REGISTERED -- THE AGENDA: %d items banked before either was put; [M1] %s, the roster %d -> %d, the roster`s controls %d of %d; [D1] %s, the one settings key; the rules bank`s rows %s; the bank at relay %s. SOURCE %s.' % (
        f['ag_items'], f['m1'], f['ag_roster'][0], f['ag_roster'][1], f['ro_wanted'], f['ro_n'], f['d1'], ', '.join('(%d)' % r_ for r_ in f['rules_rows']), K.C3_AGENDA[1], sf['text']))
    seats.append(sf)
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: tools/standing/ v1.33.0 ((R364)(7)), by its controls
    sw = seat('%s_standing_v1330.txt' % ACT, '**v1.33.0: CONTROLS ')   # ### appended by the template after this section
    keys['V1330'] = ('CERTIFIED -- tools/standing/ v1.33.0: controls %s -- %s cases, %s as wanted, each failing before its repair and passing after; the commits after its own at which a standing tool changed, %s, named with the controls run after them, the roster`s %d of %d among them. SOURCE %s.' % (
                        f['v1130_ctl'], f['v1130_cases'], f['v1130_wanted'], ', '.join(h_ for h_, _t in f['later']), f['ro_wanted'], f['ro_n'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: the INTEGRATION line (Component 4)
    so = seat('%s_line.txt' % ACT, '**THE LINE: ')
    keys['LINE'] = ('REGISTERED -- THE INTEGRATION LINE from REGISTRY and SPIRAL_MAP with the match: the registration CLUSTERED in the Epstein instance, keystone %s, the reads BANKED, stage %s, %d of %d matched; the earlier lines read again %d, none rewritten. SOURCE %s.' % (
        f['ln_keystone'], f['ln_stage'], f['ln_matched'], f['ln_of'], f['ln_earlier'], so['text']))
    seats.append(so)
    # ------------------------------------------------------------------ HELD: THE DRAFT ((R364)(10))
    sh = seat('%s_ferry.txt' % ACT, 'no draft published')
    keys['HELD'] = ('HELD -- the draft at v5, unpublished, nothing deposits; no Zenodo call this act. SOURCE %s.' % sh['text'])
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', []), ('CERTIFIED', ['V1330']), ('REGISTERED', ['REG', 'KERNELS', 'BRANCHES', 'HEADS', 'ANCHORS', 'STORE', 'AGENDA', 'LINE']), ('HELD', ['HELD'])]
#⟪END⟫
#⟪OVERRIDE citation MARK 31b08d46e87d 1⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b754 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation MARK 4c93044332ef 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 9d93e16b7a2c 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 367558757a34 1⟫
#⟪END⟫
#⟪OVERRIDE citation MARK 0fc89e683898 1⟫
#⟪END⟫
