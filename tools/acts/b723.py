# -*- coding: utf-8 -*-
# b723 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R333)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline; " REPAIR <name>" after an override names the
# (R333)(2) repair it carries. Edited by the Edit tool. Carried at b723 by tools/b723_fold.py (`carry`) from tools/acts/b722.py,
# b722`s names substituted; the citation`s sections adopted from tools/b723_citation.py as landed (`adopt citation`).
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (b722`s dead routes, carried); the loader prints them and refuses any other missing name.
# Each "#⟪PENDING <tool> <names>⟫" line: the names the act has still to write (its own arms and figures, b722`s carried till
# then); the loader prints them at every load, and the seal wants every PENDING line empty.
#⟪DEAD checks ⟫
#⟪DEAD citation ⟫
#⟪DEAD closing ⟫
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,C2_HALT,C2_PRED,C2_REG,C2_SELECT,C3_RELAY,C3_RULE,C4_PRED,C4_RELAY,C6_CENSUS,C6_DRAFTS,C6_FROZEN,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
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
#⟪OVERRIDE record 292 293 REPAIR (iii)⟫
# ### b723, (R333)(2)(iii) THE LOCK ROW: the phases read from data/act_current.json's components (the author's word, Option 2: "the act's
# ### arms, phases ... read from data/act_current.json"), each component's phases in order -- before `seal` the pre-seal phases, from `seal`
# ### on the post-seal, with the record and the closing after the root, which every act's components end before. b723's Component 7 names
# ### `lock` after `gate` and before `seal`: the lock commit's row takes `lock`, a phase of its own (b722's lock commit 794b7bc7 took `gate`,
# ### event (5)); G-SEALED-AFTER-COMPONENTS reads the lock commit by that phase. Replaces the template's two literal tuples (b722's own,
# ### with `pilot` and `component 8`, stay in b722's and b721's renders).
def _phases():
    with open(os.path.join(ROOT, 'data', 'act_current.json'), encoding='utf-8') as fh:
        comps = json.load(fh)['components']
    seq = [p for c in comps for p in c['phases']]
    if 'seal' not in seq or 'lock' not in seq or seq.index('lock') > seq.index('seal'):
        sys.exit('### data/act_current.json: the components name no `lock` before `seal` -- the phases not read')
    k = seq.index('seal')
    return tuple(seq[:k]), tuple(seq[k:]) + tuple(p for p in ('record', 'closing') if p not in seq)


PRE_SEAL_PHASES, POST_SEAL_PHASES = _phases()
#⟪END⟫
#⟪OVERRIDE checks 1655 1656 REPAIR (iv)⟫
    # ### b723, (R333)(2)(iv): G-READFIRST-DIFF-BANKED RETIRED with the reader (R332)(2)(iii) retired -- it read data/<act>_readfirst_diff.txt,
    # ### the closure reader's diff, which no tool writes since (b722's event (6)); the propagation read over the suite's arms in
    # ### data/b723_standing_v130.txt (iv) finds no other arm reading a bank no longer written that is not conditional or read for its absence
#⟪END⟫
#⟪OVERRIDE record 3353 3353 REPAIR (iii)⟫
        if r.get('phase') in PRE_SEAL_PHASES and r.get('phase') not in ('gate', 'lock'):   # ### b723 (iii): the lock commit lands after the face is locked
#⟪END⟫
#⟪OVERRIDE checks 1221 1236 REPAIR (iii)⟫
def sealed_after_ok(S):
    """(R332)(2), a carry-time repair (b722's (i)): THE ACT'S STEP BANK (data/b723_steps.json, a row per commit by the record tool's step route,
    written after the commit: the repository, the commit, the phase the seat names from the record tool's STEP_PHASES) and not the commits'
    subjects. Every relay and PLACE-papers commit of the act has its row; PLACE-papers carries a component commit.
    b723, (R333)(2)(iii) THE LOCK ROW: THE LOCK COMMIT READ BY ITS PHASE. b722's arm read the lock as the face's `locked at` time and asked a
    commit's phase to be pre-seal exactly where its commit time precedes it; b722's lock commit 794b7bc7, committed after the lock block's time,
    took `gate` (a pre-seal phase) at step 26 and the arm failed at every reading (event (5)). Here the one relay row of phase `lock` names the
    lock commit, and its commit time is the lock: the lock commit's own row reads `lock`, every commit before it a pre-seal phase, every commit
    after it a post-seal one; no `lock` row, or more than one lock commit, fails."""
    rows = S['steps']
    if not rows:
        return False
    pre = S['REC'].PRE_SEAL_PHASES
    locks = AC.step_commits(rows, phase='lock')
    if len(locks) != 1 or AC.step_commits(rows, phase='lock', repo='relay') != locks:
        return False
    lt = [t for h, s, t in S['rlog'] if locks[0].startswith(h)]
    if len(lt) != 1:
        return False
    lk = lt[0]
    for repo, log in (('relay', S['rlog']), ('pp', S['plog'])):
        for h, s, t in log:
            p = _step_phase(rows, repo, h)
            if p is None:
                return False
            if p == 'lock':
                if repo != 'relay' or not locks[0].startswith(h):
                    return False
                continue
            if (t < lk) != (p in pre):
                return False
    return any(_step_phase(rows, 'pp', h) in pre for h, s, t in S['plog'])
#⟪END⟫
# ### b723, Component 7, before the lock (the Edit tool): A FOLDED ACT HAS NO TOOL FILES. v1.3.0 folded the seven close tools into
# ### tools/standing/fold.py and removed tools/b723_record.py and tools/b723_citation.py (93925aac); the template lines below read a tool's
# ### text from tools/<act>_<tool>.py or run it as `python tools/<act>_<tool>.py`, which for b723 reads nothing or fails. Each is replaced
# ### here, for b723 alone (the templates, and b721's and b722's renders, unchanged): the text from fold's render, the run through
# ### `python tools/standing/fold.py <tool> ...` (regspec's `-I` dropped there: fold.py imports itself from tools/standing/, which `-I`
# ### takes off the path), the report tool present where the act has sections. The defect is v1.3.0's, found at this close (an event).
#⟪OVERRIDE checks 455 455 REPAIR (fold)⟫
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=__import__('standing.fold', fromlist=['render']).render('b723', 'checks'),
#⟪END⟫
#⟪OVERRIDE checks 461 462 REPAIR (fold)⟫
        spans=rd('b723_carry_spans.txt'), rec_src=__import__('standing.fold', fromlist=['render']).render('b723', 'record'),
        closing_src=__import__('standing.fold', fromlist=['render']).render('b723', 'closing'),
#⟪END⟫
#⟪OVERRIDE checks 513 513 REPAIR (fold)⟫
        report=rd('b723_report.txt'), reportj=jl('b723_report.json'), report_tool=__import__('standing.fold', fromlist=['has_sections']).has_sections('b723'),
#⟪END⟫
#⟪OVERRIDE reg_gate 58 58 REPAIR (fold)⟫
    dr = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'standing', 'fold.py'), 'record', 'drycheck', REG, 'standin'], capture_output=True,
#⟪END⟫
#⟪OVERRIDE reg_gate 66 66 REPAIR (fold)⟫
    cr = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'standing', 'fold.py'), 'closing', 'dry'], capture_output=True,
#⟪END⟫
#⟪OVERRIDE regspec 277 277 REPAIR (fold)⟫
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(ROOT, 'tools', 'standing', 'fold.py'), 'record', 'commands'], capture_output=True,
#⟪END⟫
# ### b723, Component 7 (the Edit tool, before the lock): THE STANDING RUNNER ARMS OVER THIS ACT'S AXIOM STEP. The template's three runner
# ### functions carry b721's rebuild in their text (six runs, its bank's head and foot, SIDE-frobenius's halt); b723 ran five ((R333)(7), N1),
# ### rowed in data/b723_axiom_rows.json, whose free-memory figures are strings. Replaced for b723 alone; the arms' names and plants stand.
#⟪OVERRIDE checks 1126 1138⟫
def rebuild_wf_ok(S):
    """(R333)(7), b723: the workflow at each rebuild branch's tip -- the five kernels other than SIDE-frobenius carrying build-module.yml on
    main; SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's with b721's two lines (the push trigger to the branch, the
    target fixed) and nothing else, the hold kept; SIDE-kernel's tip carrying main's build-module.yml changed in the four places of its
    kdraft4_clear row and nothing else, the diff equal to that row's (the author's word (7)); no identifier of the author and no secret at
    either tip."""
    import difflib
    st = S['rebuild_state'] or {}
    fr, kn = st.get('SIDE-frobenius') or {}, st.get('SIDE-kernel') or {}
    src = read_blob(EF, 'HEAD:.github/workflows/build-module.yml') or ''
    tip = fr.get('wf_tip') or ''
    d = [x for x in difflib.unified_diff(src.split(NL), tip.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    km = read_blob('D:/SIDE-kernel', 'main:.github/workflows/build-module.yml') or ''
    kt = kn.get('wf_tip') or ''
    kd = [x for x in difflib.unified_diff(km.split(NL), kt.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    row = [r for r in (S['rebuild_rows'] or []) if r.get('kind') == 'kdraft4_clear' and r.get('kernel') == 'SIDE-kernel']
    want = [x for x in (row[-1].get('diff') or []) if x[:1] in '+-' and x[:3] not in ('+++', '---')] if row else None
    return all(v['wf_main'] for k, v in st.items() if k != 'SIDE-frobenius') and fr.get('wf_main') is False \
        and d == ['+  push: { branches: [%s] }' % K.REBUILD_BRANCH, '-      TARGET: ${{ inputs.target }}', '+      TARGET: SIDEFrobenius'] \
        and bool(kt) and bool(want) and kd == want and not any(w in (x or '').lower() for x in (tip, kt) for w in IDENT_WF) \
        and 'hold_mb: "2560"' in tip.lower()
#⟪END⟫
#⟪OVERRIDE checks 1141 1156⟫
def runner_ok(S):
    """(R333)(7), N1, b723: the axiom step read by its run ids -- one run per kernel repaired this act, five, each the worklist's B723_RUNS and
    its dispatch row's, each read once with the build exit read from its artifact: BUILDS, exit 0, no sorry warning; SIDE-frobenius's and
    SIDE-kernel's runs push-triggered; SIDE-kernel's three-place draft HALTED before its four-place draft CLEAR (the author's word (7));
    SIDE-lv-conservation not re-dispatched, its lv row reading the sorry's position; the bank's head figures equal to its rows, five axiom
    steps read success, its foot 6 OF 6 PINS."""
    t, rows = S['rebuild'] or '', S['rebuild_rows'] or []
    reads = dict((r['kernel'], r) for r in rows if r.get('kind') == 'read')
    disp = dict((r['kernel'], r) for r in rows if r.get('kind') == 'dispatch')
    runs = dict(K.B723_RUNS)
    kd = [r.get('kind') for r in rows if r.get('kernel') == 'SIDE-kernel' and (r.get('kind') or '').startswith('kdraft')]
    return sorted(reads) == sorted(disp) == sorted(runs) and all(str(reads[k]['run']) == str(runs[k]) == str(disp[k]['run']) for k in runs) \
        and all(r['verdict'] == 'BUILDS' and str(r['build_exit']) == '0' and str(r['sorry_warnings']) == '0' for r in reads.values()) \
        and sorted(k for k, r in disp.items() if r.get('via') == 'push') == ['SIDE-frobenius', 'SIDE-kernel'] and kd == ['kdraft_halt', 'kdraft4_clear'] \
        and any(r.get('kind') == 'lv' for r in rows) and 'SIDE-lv-conservation' not in disp \
        and 'COMMITTED 5 ; PUSHED 5 ; DISPATCHED 5 (six at most) ; READ 5' in t and t.count('the axiom step success') == 5 \
        and _verdict(t).startswith('THE AXIOM STEP AT 6 OF 6 PINS')
#⟪END⟫
#⟪OVERRIDE checks 1167 1167⟫
    for k, _r in K.B723_RUNS:
#⟪END⟫
#⟪OVERRIDE checks 1173 1173⟫
    return bool(mem) and all(int(r.get('free_mb') or 0) >= K.HOLD for r in mem) and order \
#⟪END⟫
# ### b723, Component 7 (the Edit tool): the corrigendum arm's event rows, written into the template as b722's fifteen; b722's record has nineteen
#⟪OVERRIDE checks 980 980⟫
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 20)) \
#⟪END⟫
# ### b723, Component 7 (the Edit tool): G-RUNNER-READ's plant named b722's lv grade, which b723's axiom bank does not carry (the plant a
# ### no-op, the arm's POS passing); the plant now a push the head did not make
#⟪OVERRIDE checks 1686 1686⟫
     lambda S: runner_ok(S), lambda S: put(S, 'rebuild', (S['rebuild'] or '').replace('COMMITTED 5 ; PUSHED 5 ;', 'COMMITTED 5 ; PUSHED 4 ;'))),
#⟪END⟫
# ### b723, Component 7 (the Edit tool), the v1.3.0 fold defect's second instance: b709's row (1) read through the carry banks of record,
# ### checks and closing, which a folded act does not write (its tools are the templates and its sections); for a folded act the diff is
# ### read in the fold bank, its row for the act's sections file
#⟪OVERRIDE checks 1005 1005 REPAIR (fold)⟫
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and (all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing'))
                                                                          or (bool(S['report_tool']) and 'tools/acts/b723.py: sections ' in (rd('b723_fold.txt') or ''))) \
#⟪END⟫
# ### b723, Component 7 (the Edit tool): G-CONVERSION-ONE's needle `def conv(` read tools/b723_c2_check.py's Dirichlet convolution
# ### conv(A, B, cut) as a second text conversion (the probe's LIVE FAIL); the needle tightened on content to the conversion's own shape, a
# ### one-argument def conv (b652_record's conv(t)), which a planted `def conv(t):` still meets
#⟪OVERRIDE checks 256 263 REPAIR (needle)⟫
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to']
    one_arg = re.compile(r'(?m)^\s*def ' + r'conv\(\s*\w+\s*\)')
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b723_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks) or one_arg.search(t):
                bad.append(f)
#⟪END⟫
# ### b723, Component 7 (the Edit tool): the closing's counter line with the repeat count beside it (Component 7 of (R333): "the counter
# ### line CLAIM n, CLOSE m, the repeat count beside it"; v9 row (83): "the closing prints the count of repeats")
#⟪OVERRIDE closing 339 340⟫
    rows = [l for n_ in ('b723_defects.txt', 'b723_events.txt') for l in (rd(n_) or '').split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    rep = sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l))
    return '### THE COUNTER ((R333)(2), the act`s events and defects together; relay data/b723_defects.txt, data/b723_events.txt): CLAIM %d, CLOSE %d ; REPEAT %d OF %d%s' % (
        c['claim'], c['close'], rep, len(rows), (' ; UNTAGGED %s' % c['untagged']) if c['untagged'] else '')
#⟪END⟫
# ### b723, Component 7 (the Edit tool): the carried item (b) named b722's orders by hand; (R333)(3)(i) writes the open orders from
# ### tools/standing/orders.py's output, its count from the worklist (G-OFFSET-POST-HOC ties it to the bank's AT HEAD foot)
#⟪OVERRIDE closing 394 395⟫
    '    (b) The open orders: %d of %d at PLACE-papers main by tools/standing/orders.py`s rule (relay data/b723_orders.txt :282), the trail`s' % (WL.ORDERS[1], WL.ORDERS[0]),
    '        open-orders line written from the tool`s output ((R333)(3)(i)), none carried by hand; beside them',
#⟪END⟫
#⟪OVERRIDE record 3432 3434 REPAIR (fold)⟫
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'standing', 'fold.py'), 'checks', '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = __import__('standing.fold', fromlist=['render']).render('b723', 'checks').split(NL)
#⟪END⟫
# ### b723, Component 7 (the Edit tool), the v1.3.0 fold defect's third instance: the regspec and reg_gate templates name the face by
# ### b722's date (2026-10-28) where the record and checks templates read the worklist's DATE; the face named by K.DATE in both
#⟪OVERRIDE regspec 27 27 REPAIR (fold)⟫
REG = os.path.join(ROOT, 'data', 'b723_registration_%s.txt' % K.DATE)
#⟪END⟫
#⟪OVERRIDE reg_gate 21 21 REPAIR (fold)⟫
REG = os.path.join(D, 'b723_registration_%s.txt' % __import__('b723_worklist').DATE)   # ### the gate imports no worklist of its own
#⟪END⟫
# ### b723, Component 7 (the Edit tool): the carried row read "none: OPEN_TRAILS written by the trail at the close alone"; b723 landed
# ### (R333)(3)(ii)'s three closing lines (9e098548) and the author's word (5)'s dated line (70d9c0d0) before the seal, measured here
#⟪OVERRIDE regspec 78 78⟫
    ('orders and annotations entered at OPEN_TRAILS before the seal', 'OTLINES', 'OTLINES', 'lines', '### (R333)(3)(ii) and the author`s word (5): 9e098548 and 70d9c0d0, no line rewritten; MEASURED off their numstat.'),
#⟪END⟫
# ### b723, Component 7 (the Edit tool): N1's dispatch commands are tools/b723_axiom.py's `dispatch <kernel>` route ((R333)(7)); the
# ### carried pattern named b722's rebuild tool, which b723 does not have (SIDE-frobenius's and SIDE-kernel's runs went on their pushes,
# ### read in the axiom rows bank by `via`)
#⟪OVERRIDE record 524 525⟫
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)'
                          r'|(^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b723_axiom\.py dispatch\b', re.M)
#⟪END⟫
# ### b723, Component 7 (the Edit tool): G-SCORER-READS-BANKS's needles named an earlier act's banks (the pin's rows, the derivation),
# ### which no b723 scorer reads; the needles set to the banks b723's N1-N4 read (the command bank and the axiom rows, H-SUPPORT's rule,
# ### the closed form's check, the seal and step banks), the ledger exclusion unchanged; the axiom rows' needle is the read's own form, since
# ### N1's printed label names the bank too (relay data/b723_c7_repair_controls.txt, the planted case)
#⟪OVERRIDE checks 903 904 REPAIR (needle)⟫
    return bool(n) and '_commands.json' in n and "_axiom_rows.json' % ACT" in n and '_support_rule.txt' in n and '_c2_check.txt' in n \
        and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
#⟪END⟫
# ### b723, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH read the kept branch in b722's ruling's form "port-b707 kept;", where (R333)(9)
# ### writes "kept: port-b707, …" (data/b723_ferry.txt :34), so the arm failed on the act's real deletes; both forms read as written
#⟪OVERRIDE checks 764 767 REPAIR (needle)⟫
    # ### (R332)(9) wrote "port-b707 kept;" and (R333)(9) writes "kept: port-b707, …"; allow.py's NOT-deleted reader takes neither; each read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']
             or bool(re.search(r'\bkept: [^.;]*\b%s\b' % re.escape(K.PORT_BRANCH), S['ferry']))) \
#⟪END⟫
# ### b723, Component 7 (the Edit tool): G-DELETES-ONE-BRANCH's plant replaced "the push-b722-* branches", where (R333)(9) writes "the push-b722*
# ### branches", so the plant changed nothing; set to the ruling's own words
#⟪OVERRIDE checks 1621 1621 REPAIR (plant)⟫
     lambda S: deletes_one_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace('the push-b722* branches of relay and PLACE-papers deleted by name', 'the push-b722* branches of relay and PLACE-papers kept by name'))),
#⟪END⟫
# ### b723, Component 7 (the Edit tool): the carried failures' block named b720's challenge tool (as tools/b723_challenge.py, which does not
# ### exist), its defect (m) and its commits; b723's carried failures are read off the act's own dev runs before this face
#⟪OVERRIDE checks 2036 2042 REPAIR (carried)⟫
# ### the carried failures declared on the face by name (section (0)), read off the dev runs of the seven parts before the face is written.
# ### b723's one: G-AXIOM-CLAIM, CONTRADICTED 1 on SIDE-lv-conservation's AxiomCheck.lean :8 against b721's rebuild print carrying sorryAx --
# ### b721's (u), b722's (w), b723's (c'); tools/axiom_claim.py outside (W), the bank not rewritten; the arm not edited. G-DELETES-ONE-BRANCH
# ### (repaired above, the ruling's kept clause read as written) and G-DELETE-FREE (no act tool deletes; b720's challenge tool is not b723's)
# ### pass at b723 and are not carried.
CARRIED_FAILING = ('G-AXIOM-CLAIM',)
#⟪END⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) at the seal, every one the seat's; (a')-(d') and (f')-(k') the seat's and (e') the navigator's, beyond the single letters this floor reads
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b723_corrigendum.txt', 'data/b723_standing_v130.txt', 'data/b723_fold.txt', 'data/b723_fold_run.txt',
                  'data/b723_i76.txt', 'data/b723_orders.txt', 'data/b723_orders_twenty.txt', 'data/b723_registrations.txt',
                  'data/b723_support_rule.txt', 'data/b723_zetak.txt', 'data/b723_support.txt', 'data/b723_dial_price.txt',
                  'data/b723_c2_closed_form.txt', 'data/b723_c2_check.txt', 'data/b723_axiom.txt', 'data/b723_axiom_rows.json',
                  'data/b723_split_price.txt', 'data/b723_reproduce.txt', 'data/b723_reproduce.json', 'data/b723_address_scan.txt',
                  'data/b723_author_words_preseal.txt', 'data/b723_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: b710's row (1) reads it at VERSION 7, unchanged since the act's base; v8 binds b723 whole and v9 from d9739558 ((R333)(2)(v)), each read by G-SURGERY-CARRIED
#⟪END⟫
#⟪SECTION checks 4⟫
def _addr_live():
    """(R333)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b723_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


#⟪END⟫
#⟪SECTION checks 5⟫
        # ### (R333)(2)-(8), Component 7, the Edit tool, before the lock (b722's keys over b722's objects in git at b722's suite): the
        # ### registrations at their commit and at HEAD; the ancestry each arm reads; the orders and the twenty (3); the registrations, the rule
        # ### and the three computations (4)-(5); the closed form and its check (6); the axiom step and the split's price (7)-(8); v8 and v9;
        # ### the address scan (R332)(9); the reproduction run under the standing arm
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_now=(_s(blob(ROOT, '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))), _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS))),
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('reg_rule', K.REG_COMMIT, K.C3_PRED), ('reg_zetak', K.REG_COMMIT, K.C4_ZETAK),
                                 ('pred_onsets', K.C3_PRED, K.C4_SUPPORT), ('tool_onsets', K.C4_ONSET_TOOL, K.C4_SUPPORT),
                                 ('reg_dial', K.REG_COMMIT, K.C4_DIAL), ('v9_v130', K.STANDING_COMMIT, K.C1_V130), ('v130_orders', K.C1_V130, K.C2_RELAY),
                                 ('orders_weed', K.C2_RELAY, K.C2_REPRINT), ('reg_c5', K.REG_COMMIT, K.C5_RELAY))),
        registrations=rd('b723_registrations.txt'), support_rule=rd('b723_support_rule.txt'), zetak=rd('b723_zetak.txt'),
        support=rd('b723_support.txt'), dial=rd('b723_dial_price.txt'), closed_form=rd('b723_c2_closed_form.txt'), c2_check=rd('b723_c2_check.txt'),
        orders=rd('b723_orders.txt'), twenty=rd('b723_orders_twenty.txt'), v130=rd('b723_standing_v130.txt'), fold_bank=rd('b723_fold.txt'),
        reproduce=rd('b723_reproduce.txt'), reproducej=jl('b723_reproduce.json'),
        v9=read(os.path.join(ROOT, *K.DATA_STANDING_V9.split('/'))), v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))),
        address=rd('b723_address_scan.txt'), addr_live=_addr_live(), split=rd('b723_split_price.txt'),
        # ### the standing runner arms read THIS ACT'S axiom step ((R333)(7), N1: five runs, six at most): its bank, its rows, each wave 1
        # ### kernel's rebuild-b721 branch, main and tags (b722's carry named data/b722_rebuild.txt, which no act wrote)
        rebuild=rd('b723_axiom.txt'), rebuild_rows=json.loads(rd('b723_axiom_rows.json') or '[]'), rebuild_state=_rebuild_state(),
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c2pp=_ct(PP, K.C2_PP), reg=_ct(ROOT, K.REG_COMMIT),
               pred=_ct(ROOT, K.C3_PRED), zetak=_ct(ROOT, K.C4_ZETAK), support=_ct(ROOT, K.C4_SUPPORT), dial=_ct(ROOT, K.C4_DIAL),
               c5=_ct(ROOT, K.C5_RELAY), c6=_ct(ROOT, K.C6_RELAY), v9=_ct(ROOT, K.STANDING_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS),
               actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   c2=files_of(ROOT, K.C2_RELAY), c2pp=files_of(PP, K.C2_PP), weedpp=files_of(PP, K.C2_WEED_PP), reprint=files_of(ROOT, K.C2_REPRINT),
                   pred=files_of(ROOT, K.C3_PRED), zetak=files_of(ROOT, K.C4_ZETAK), onset_tool=files_of(ROOT, K.C4_ONSET_TOOL),
                   support=files_of(ROOT, K.C4_SUPPORT), dial=files_of(ROOT, K.C4_DIAL), c5=files_of(ROOT, K.C5_RELAY), v9=files_of(ROOT, K.STANDING_COMMIT),
                   c6=sorted(set(f for c in K.C6_AXIOM for f in files_of(ROOT, c))),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b723's read-first bank's items by path, as its step zero wrote them (Component 7, the Edit tool, before the lock: the carried needles
# ### were b722's items)
READFIRST_NEEDLES = ('relay data/b722_closing.txt |', 'relay data/b722_events.txt |', 'relay data/b722_defects.txt |',
                     'relay data/b722_axiom_diag.txt |', 'relay data/b707_onset.txt |', 'relay data/b709_grid.txt |', 'relay data/b711_list.json |',
                     'PLACE-papers FINDINGS.md | :5667 |', 'PLACE-papers FINDINGS.md | :10206 |', 'PLACE-papers OPEN_TRAILS.md | :14680 |',
                     'PLACE-papers OPEN_TRAILS.md | :16250 |', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md | :2982 |',
                     'relay data/b680_split_price.txt |', 'relay data/b723_ferry.txt | whole |', 'relay data/b723_ferry_addendum.txt | whole |',
                     'relay data/standing_clauses_v8.txt |', 'relay data/b722_steps.json |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R333)(1)-(2))', 'OPEN ORDERS ((R333)(3))', 'REGISTRATIONS ((R333)(4))',
                    'COMPUTATIONS ((R333)(5))', 'C2 CLOSED FORM ((R333)(6))', 'AXIOM STEP ((R333)(7))', 'LEDGER SPLIT ((R333)(8))',
                    'NAME AND ADDRESS ((R332)(9))', 'TOUCH READ (standing clauses v9)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (60 = 60 + 0: no miss in the banking run, the dry run's three each
    the seat's own new row, repaired before it -- data/b723_readfirst.txt :5-:8); the bank written before the step-zero banks' commit and that
    commit before Component 1's (Component 7, the Edit tool: the carried 90 = 88 + 2 were b722's own)."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 0 and int(m.group(1)) == 60 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 7, the Edit tool, before the lock: the carried needles were b720's figures under b722's name)
    return landed(S, 0, ['b722 AT ITS WEIGHT', 'suite 110 of 117; root 0d26295f7b567e20…', 'the closing’s 1607e994', '31 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### Component 7, before the lock, the Edit tool: b723's title in the ferry's Component 7 form adjusted to what the act did (the record
# ### tool's _title over the banks), cut at its objects; the carried needles were b722's
TITLE_NEEDLES = ('## the close tools at v1.3.0 and five repeat classes repaired', '; the open orders generated, 143 open, the twenty read',
                 '; H-SUPPORT at three zeros REFUTED, H-ZETAK HELD, H-DIAL carried', '; the C2 closed form written and checked post hoc',
                 '; the axiom step at 6 of 6 pins', '; the ledger split carried')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R333)(2): the generated entry for b722's nineteen events and thirty-one defects landed (its line in the bank, the title at that line
    through conv): the events by row (1)-(19), the defects by the one lettering ((a)-(z), (a`)-(e`)), no memory item; every item tagged CLAIM
    or CLOSE and NEW or REPEAT, the tags summing (CLAIM 4, CLOSE 46 over 50, REPEAT 25); the CLAIM items defects (f), (k), (w) and (x); the
    repairs at tools/standing/ v1.3.0 with their 68 cases; the corrigenda bank appended at row (43) and nothing before it changed; in
    Component 1's commit (Component 7, the Edit tool, before the lock: the carried figures were b722's corrigendum's, of b721's record)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 31 and len(items) == j.get('items') == 50 and j.get('row') == 43 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 50 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 4 and claims == ['f', 'k', 'w', 'x'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 25 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.3.0' and (j.get('repairs') or {}).get('cases') == 68 \
        and '  (43) ' in S['corrigenda'] and '  (44) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b723_rules.txt and data/b724_rules.txt, by form in (R333)(9)'s (W)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    (Component 7, the Edit tool: the line above is b722's, carried); no author's word of b723 orders a row, so neither bank exists."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and r1 == '' and not os.path.exists(os.path.join(D, 'b723_rules.txt')) and not os.path.exists(os.path.join(D, 'b724_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### b723's keys, the report sections' own heads (Component 7, the Edit tool, before the lock; b722's carried till then)
REPORT_KEYS = ('KERNEL -- THE AXIOM STEP AT THE SIX WAVE 1 PINS', 'CERTIFIED -- H-ZETAK ON Q0`S TWO ONSET WINDOWS',
               'CERTIFIED -- THE C2 CLOSED FORM, CHECKED POST HOC', 'REGISTERED -- H-SUPPORT AT Q0', 'REGISTERED -- H-DIAL',
               'REGISTERED -- THE OPEN ORDERS GENERATED', 'HELD -- THE LEDGER SPLIT',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over THIS ACT'S axiom step ((R333)(7), data/b723_axiom_rows.json; Component 7, the Edit tool): every push, dispatch and read
    row with the host's free memory at or above the hold (each figure read as an integer: the rows carry strings); per kernel run this act
    (K.B723_RUNS, five; SIDE-lv-conservation ran clean at b721 and was not re-dispatched) its push before its run and its run before its read;
    the dispatches five, at most the six N1 allows, two of them push-triggered (rowed `via` push); the capture running the axiom tool's push and
    dispatch routes, b722's rebuild tool not at all."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b723_axiom\.py (push|dispatch|kcommit|commit)\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    old = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b72[12]_rebuild\.py (push|dispatch|push_run|plan)\b', re.M)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == len(K.B723_RUNS) <= K.MAX_DISPATCHES == 6 \
        and sorted(r['kernel'] for r in rows if r.get('kind') == 'dispatch' and r.get('via') == 'push') == ['SIDE-frobenius', 'SIDE-kernel'] \
        and bool(S['cmds']) and bool(cmds) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and old.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-archimedean': '1', 'SIDE-rcurve': '1', 'SIDE-spinor': '1', 'SIDE-frobenius': '3', 'SIDE-kernel': '1'} \
        and all(set(st[k]['author'].split(NL)[:1]) == {'b723 axiom seat <b723-axiom@relay.invalid>'} for k in beyond) \
        and set(st['SIDE-frobenius']['author'].split(NL)[1:]) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS and OPEN_TRAILS; (R333)(8)'s archive-3 files not written, the
    split carried), both ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### b723's headings and banks, as its _finding_text writes them (Component 7, the Edit tool, before the lock; b722's carried till then)
ENTRY_NEEDLES = ('**The corrigendum and the repeat classes**', '**The open orders**', '**The registrations**', '**H-ZETAK**', '**H-SUPPORT**',
                 '**H-DIAL**', '**The C2 closed form**', '**The axiom step at the six pins**', '**The ledger split**',
                 '**The author’s name and address**', '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**',
                 '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b723_corrigendum.txt', 'data/b723_standing_v130.txt', 'data/b723_orders.txt', 'data/b723_orders_twenty.txt',
                 'data/b723_registrations.txt', 'data/b723_zetak.txt', 'data/b723_support.txt', 'data/b723_dial_price.txt',
                 'data/b723_c2_closed_form.txt', 'data/b723_c2_check.txt', 'data/b723_axiom.txt', 'data/b723_split_price.txt',
                 'data/b723_address_scan.txt', 'data/b723_touch.txt', 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b723: no single-letter row the navigator's; (e'), (R333)(2)'s "at step zero" against the ferry's order, the navigator's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R333)(4), N2 (Component 7, the Edit tool, over b723's objects): data/b723_registrations.txt committed alone at REG_COMMIT (its one file,
    the step bank aside), its text at HEAD its blob there, its foot naming no zero and no figure at a registered object; that commit an
    ancestor of H-SUPPORT's rule output and predictions (C3_PRED), of H-ZETAK's bank (C4_ZETAK), of H-DIAL's price (C4_DIAL) and of the closed
    form (C5_RELAY); the predictions' commit carrying the rule's bank and no onset bank, its foot ONSETS COMPUTED 0, and an ancestor of the
    onsets' commit (C4_SUPPORT), the onset tool committed before it; each figure bank printing its controls before its figures; the earlier
    acts' registrations at HEAD their blobs at their commits."""
    reg, z, s, p = S['registrations'] or '', S['zetak'] or '', S['support'] or '', S['support_rule'] or ''
    return _own(S['files']['reg']) == [K.REGISTRATIONS] and S['reg_now'][0] is not None and S['reg_now'][0] == S['reg_now'][1] \
        and 'ZEROS NAMED 0 ; FIGURES AT A REGISTERED OBJECT 0' in _verdict(reg) \
        and all(S['anc'].get(k) is True for k in ('reg_rule', 'reg_zetak', 'reg_dial', 'reg_c5', 'pred_onsets', 'tool_onsets')) \
        and 'data/b723_support_rule.txt' in S['files']['pred'] and 'data/b723_support.txt' not in S['files']['pred'] \
        and 'ONSETS COMPUTED 0' in _verdict(p) and 'data/b723_support.txt' in S['files']['support'] \
        and _ctl_first(z, '## (C1) ', '## THE zeta_K FORM AT EACH WINDOW') and _ctl_first(s, '## (C1) ', '## THE ZEROS, IN THE RULE`S ORDER') \
        and all(a is not None and a == b for a, b in S['reg_blobs'].values())
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R332)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 7, the Edit tool): tools/b723_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address and name read from history and held in memory -- the address 0, the author's name 0, the previous name 0, its
    four controls as wanted (the second name arm added at Component 1, d0ee06a8); the bank's counts the same; the address never printed."""
    a = S['addr_live'] or {}
    out = a.get('out') or ''
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'PREVIOUS NAME: 0 ;' in out and 'CONTROLS 4 OF 4 AS WANTED' in out \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ; PREVIOUS NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R333)(5), N3 (the name the frozen run list carries; Component 7, the Edit tool, over b723's objects): each registered hypothesis graded
    at its bank's end in (R333)(5)'s words, the grade the bank's last line -- H-ZETAK HELD, its controls C1 and C2 as wanted and C3 holding;
    H-SUPPORT REFUTED, C1 as wanted, its zeros three, its falsifier fired; H-DIAL carried, not run, no figure at F_c, its registration
    committed -- each bank in its own commit (C4_ZETAK, C4_SUPPORT, C4_DIAL)."""
    last = lambda t: ((t or '').rstrip(NL).split(NL) or [''])[-1]
    z, s, d = last(S['zetak']), last(S['support']), last(S['dial'])
    return z.startswith('### ### **H-ZETAK: C1 AS WANTED ; C2 AS WANTED ; C3 HOLDS ;') and z.endswith('THE HYPOTHESIS HELD ; 17 s.**') \
        and s.startswith('### ### **H-SUPPORT: C1 AS WANTED ; ZEROS 3 ;') and s.endswith('FALSIFIER FIRED ; THE HYPOTHESIS REFUTED.**') \
        and d.startswith('### ### **H-DIAL: BUILD PRICED ') and d.endswith('FIGURES AT F_c 0 ; NOT RUN ; CARRIED, ITS REGISTRATION COMMITTED.**') \
        and 'data/b723_zetak.txt' in S['files']['zetak'] and 'data/b723_support.txt' in S['files']['support'] \
        and 'data/b723_dial_price.txt' in S['files']['dial']
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R333)(6), N3 (the name the frozen run list carries; Component 7, the Edit tool, over b723's objects): the C2 closed form written as a
    derivation and its check POST HOC wherever named -- every row of the check led POST HOC, the rows the foot's count, each REPRODUCED; the
    planted e_p failing to reproduce, as wanted; the derivation's foot CHECKED POST HOC and NOT COMPILED; both banks and the check's tool in
    Component 5's commit (C5_RELAY), the registrations' commit its ancestor."""
    c, k = S['closed_form'] or '', S['c2_check'] or ''
    rows = re.findall(r'(?m)^  POST HOC  D\s+(-\d+) .*\| (REPRODUCED|DIFFERS|FAILS TO REPRODUCE)$', k)
    lead = re.findall(r'(?m)^  (\S+(?: \S+)?)\s+D\s+-\d+ \(', k)
    f = re.search(r'ROWS (\d+), REPRODUCED (\d+) ;', _verdict(k))
    return 'C1 (PLANTED e_p) FAILS, AS WANTED' in _verdict(k) and 'FAILS TO REPRODUCE, AS WANTED' in k and bool(f) \
        and int(f.group(1)) == len(rows) == len(lead) == 19 and set(lead) == {'POST HOC'} \
        and int(f.group(2)) == sum(1 for r in rows if r[1] == 'REPRODUCED') == 19 \
        and 'CHECKED POST HOC' in _verdict(c) and 'NOT COMPILED' in _verdict(c) and 'EVERY ROW IS POST HOC' in k \
        and all(x in S['files']['c5'] for x in ('data/b723_c2_closed_form.txt', 'data/b723_c2_check.txt', 'tools/b723_c2_check.py')) \
        and S['anc'].get('reg_c5') is True
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R333)(3), N2 (the name the frozen run list carries; Component 7, the Edit tool, over b723's orders): the open orders generated by
    tools/standing/orders.py (C2_RELAY, v1.3.0's commit its ancestor) -- the rule printed before the orders, each order once, the first foot
    the rows' counts at 763ae914; the controls 6 of 6 as wanted; at HEAD (after the author's word (5)'s weed, C2_REPRINT) the worklist's
    193, 143 open, 50 closed; the twenty each against its trigger, the foot's counts summing to twenty; the closing lines on OPEN_TRAILS in
    C2_PP and C2_WEED_PP, OPEN_TRAILS the one file in each."""
    o, w = S['orders'] or '', S['twenty'] or ''
    rows = re.findall(r'(?m)^  (W-ORD-[\w-]+)\s+entry :\d+\s+(OPEN|CLOSED)\s', o)
    a = re.search(r'\*\*ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', o)
    h = re.search(r'\*\*AT HEAD: ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ;', o)
    tw = re.search(r'\*\*THE TWENTY: TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) \(ACTED THIS ACT (\d+), PRICED AND NAMED (\d+)\) ; '
                   r'DISCHARGED BY READING (\d+) ; OFFERED FOR RETIRE (\d+) ;', w)
    rule, first = o.find('### THE RULE '), o.find('## THE ORDERS ')
    tg = [int(x) for x in tw.groups()] if tw else [0] * 6
    return 0 <= rule < first and bool(a) and len(set(r[0] for r in rows)) == len(rows) \
        and [int(x) for x in a.groups()] == [len(rows), sum(1 for r in rows if r[1] == 'OPEN'), sum(1 for r in rows if r[1] == 'CLOSED')] \
        and bool(h) and (int(h.group(1)), int(h.group(2)), int(h.group(3))) == tuple(K.ORDERS) and K.ORDERS[0] == len(rows) == K.ORDERS[1] + K.ORDERS[2] \
        and '**THE ORDERS` CONTROLS: CASES 6 ; AS WANTED 6 ; ALL AS WANTED.**' in o \
        and bool(tw) and tg[0] + tg[1] + tg[4] + tg[5] == 20 and tg[2] + tg[3] == tg[1] \
        and all(S['anc'].get(k) is True for k in ('v130_orders', 'orders_weed')) and 'tools/standing/orders.py' in S['files']['c2'] \
        and 'data/b723_orders_twenty.txt' in S['files']['c2'] and 'data/b723_orders.txt' in S['files']['reprint'] \
        and S['files']['c2pp'] == ['OPEN_TRAILS.md'] and S['files']['weedpp'] == ['OPEN_TRAILS.md']
#⟪END⟫
#⟪SECTION checks 36⟫
    """(R333)(2)(v), the name the frozen run list carries (Component 7, the Edit tool, over b723's v9): v9 at VERSION 9, v8's rows (1)-(82)
    in it in order line for line and v8 at HEAD its blob at the act's base; row (83) alone beyond them, its clause the ferry's own words (the
    whitespace folded); the foot ROWS 83 with v8's 82 unchanged; its commit (STANDING_COMMIT) the one file, the text at HEAD its blob there,
    an ancestor of v1.3.0's commit."""
    v9, v8 = S['v9'] or '', S['v8'] or ''
    rows = lambda t: [l for l in t.replace('\r', '').split(NL) if re.match(r'^  \(\d+\) |^      \S', l)]
    r8, r9 = rows(v8), rows(v9)
    fer = ' '.join((S['ferry'] or '').replace('’', "'").split())
    return 'VERSION: 9' in v9.replace('\r', '').split(NL)[:4] and len(r8) >= 164 and r9[:len(r8)] == r8 and len(r9) == len(r8) + 2 \
        and r9[-2].startswith('  (83) ') and r9[-1].strip().replace('’', "'") in fer and 'ROWS 83 ; v8`S ROWS 82 UNCHANGED' in _verdict(v9) \
        and S['files']['v9'] == [K.DATA_STANDING_V9] and _s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V9))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V9)) \
        and _s(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V8))) == _s(blob(ROOT, 'HEAD:' + K.DATA_STANDING_V8)) \
        and S['anc'].get('v9_v130') is True
#⟪END⟫
#⟪SECTION checks 37⟫
    """(R333)(2)(iv): no arm retired through tools/standing/arms.py this act -- the file byte-equal to its blob at the act's base, its RETIRED
    as b722 left it and arm_tags.json's retired record equal to it, none a guard; G-READFIRST-DIFF-BANKED left the arm list itself at v1.3.0
    (be821907) with the reader (R332)(2)(iii) retired; this suite's run list 116 arms, no standing arm added (Component 7, the Edit tool)."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 116 \
        and K.STANDING_ADDED == () and 'G-READFIRST-DIFF-BANKED' not in names and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R333)(7)-(8), the name the frozen run list carries (Component 7, the Edit tool, over b723's axiom step and split): the axiom step at
    6 of 6 pins -- the head COMMITTED, PUSHED, DISPATCHED and READ each the worklist's B723_RUNS (five, six at most), HALTED 0, the sixth pin
    SIDE-lv-conservation clean at b721, NO MAIN OR TAG TOUCHED; the ledger split carried whole to b724 with its price, NOTHING CUT; both banks
    in Component 6's commits (C6_AXIOM)."""
    a, sp, n = _verdict(S['rebuild']), _verdict(S['split']), len(K.B723_RUNS)
    return n == 5 and ('COMMITTED %d ; PUSHED %d ; DISPATCHED %d (six at most) ; READ %d' % (n, n, n, n)) in (S['rebuild'] or '') \
        and a.startswith('THE AXIOM STEP AT 6 OF 6 PINS (5 REPAIRED AND RUN THIS ACT, SIDE-lv-conservation CLEAN AT b721) ; HALTED 0 (none) ; RUNS 5 ;') \
        and a.endswith('NO MAIN OR TAG TOUCHED.') and sp.startswith('THE LEDGER SPLIT: CARRIED WHOLE TO b724 WITH ITS PRICE') and sp.endswith('NOTHING CUT.') \
        and all(x in S['files']['c6'] for x in ('data/b723_axiom.txt', 'data/b723_axiom_rows.json', 'data/b723_split_price.txt', 'tools/b723_axiom.py'))


def research_reproduces_ok(S):
    """the standing arm G-RESEARCH-REPRODUCES (b722's (R332)(7), carried in the run list): tools/research/reproduce.py's full run banked this
    act -- one row per instrument, the rows' ids I-41 to I-108 in order; each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong
    figure graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the
    json's counts and the bank's foot the rows'; the tool at HEAD its blob at its last commit (C1_I76) and the working tree's."""
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
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (K.C1_I76, tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')
#⟪END⟫
#⟪SECTION checks 41⟫
    """standing clauses v9 (Component 7 of (R333): "the touch read of v9 banked before the root"), N4: the touch read banked as data/b723_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### b722's G-RESEARCH-REPRODUCES stands untagged beside the act shift, and G-READFIRST-DIFF-BANKED, out of the arm list at v1.3.0, stays
    # ### tagged CLOSE in the file; the closing's tally counts both apart (Component 7, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R333-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED', 'G-READFIRST-DIFF-BANKED']) \
        and tags.get('G-R329-ENTERED') == 'CLOSE' and tags.get('G-READFIRST-DIFF-BANKED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### Component 8, the Edit tool: b723's ferry names no "standing clauses v<N>" outside a file name (it names data/standing_clauses_v8.txt
    # ### and v8 by row), so the carried `7 in named` read nothing; v7 is read by its bytes below and v8 by G-SURGERY-CARRIED
    return 'RULING (R333) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from 1607e994',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### b722's standing arm, carried in the run list of 116 (Component 7, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R332)(7), carried: tools/research/reproduce.py`s full run this act -- one row per instrument I-41 to I-108, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows` (68: 64, 0, 4); the tool at its last commit 82e62fd7',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 60 = 60 OK + 0 misses, the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b722-closing (1607e994)', 'push-b722-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the close tools at v1.3.0 and five repeat classes repaired; the open orders generated, 143 open, the twenty read; H-SUPPORT at three zeros REFUTED, H-ZETAK HELD, H-DIAL carried; the C2 closed form written and checked post hoc; the axiom step at 6 of 6 pins; the ledger split carried), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R333)(1)-(2): the generated corrigendum for b722`s record, landed at FINDINGS :11401: its nineteen events and thirty-one defects, 50 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 4 CLOSE 46, REPEAT 25; v1.3.0`s repairs, 68 cases; the corrigenda bank appended at row (43)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank written this act (no b723 and no b724 rules bank; (R333)(2)(v)`s row stands in v9)',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b723's objects (Component 7, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R333)(4), N2: data/b723_registrations.txt committed alone at 9ad26421, at HEAD its blob there, naming no zero and no figure; an ancestor of H-SUPPORT`s rule output and predictions (0e91c670, no onset there, ONSETS COMPUTED 0), of H-ZETAK`s bank (23f54c74), of H-DIAL`s price (ca2c6a9d) and of the closed form (cdc46c59); the onsets (1530d2f2) after the predictions and the onset tool; each figure bank`s controls before its figures',
     lambda S: registrations_first_ok(S), lambda S: put(S, 'support_rule', (S['support_rule'] or '').replace('ONSETS COMPUTED 0', 'ONSETS COMPUTED 1'))),
    ('G-PREDICTION-FIRST', '(R332)(9)(i), N5, the scan arm: tools/b723_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, the previous name 0, four controls as wanted, the bank`s counts the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R333)(5), N3: each registered hypothesis graded at its bank`s end in (R333)(5)`s words -- H-ZETAK HELD (C1, C2 as wanted, C3 holds); H-SUPPORT REFUTED at three zeros (C1 as wanted, the falsifier fired); H-DIAL carried, not run, no figure at F_c -- each bank in its own commit',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'zetak', (S['zetak'] or '').replace('THE HYPOTHESIS HELD', 'THE HYPOTHESIS REFUTED'))),
    ('G-DERIVATION-GRADED', '(R333)(6), N3: the C2 closed form written as a derivation, NOT COMPILED; its check POST HOC wherever named -- every one of the 19 rows led POST HOC and REPRODUCED, the foot`s count the rows`; the planted e_p failing to reproduce, as wanted; both banks and the check`s tool in cdc46c59, the registrations` commit its ancestor',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'c2_check', (S['c2_check'] or '').replace('  POST HOC  D   -20 ', '  COMPUTED  D   -20 '))),
    ('G-OFFSET-POST-HOC', '(R333)(3), N2: the open orders generated by tools/standing/orders.py (709ba3eb, after v1.3.0`s be821907): the rule before the orders, each order once, the first foot the rows` (193: 147 open, 46 closed at 763ae914); the controls 6 of 6; at HEAD after the weed (9c026ef7) 193, 143 open, 50 closed; the twenty`s foot summing to twenty; OPEN_TRAILS alone in 9e098548 and 70d9c0d0',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'orders', (S['orders'] or '').replace('**AT HEAD: ORDERS 193 ; OPEN 143', '**AT HEAD: ORDERS 193 ; OPEN 144'))),
    ('G-SURGERY-CARRIED', '(R333)(2)(v): v9 at VERSION 9 -- v8`s rows (1)-(82) line for line, v8 at HEAD its blob at 1607e994; row (83) alone beyond them, its clause the ferry`s own words; the foot ROWS 83; committed alone at d9739558, at HEAD its blob there, before v1.3.0`s commit',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'v9', (S['v9'] or '').replace('  (83) ', '  (84) '))),
    ('G-ARMS-RETIRED', '(R333)(2)(iv): no arm retired through tools/standing/arms.py this act -- the file byte-equal at 1607e994, its RETIRED equal to arm_tags.json`s retired record, none a guard; G-READFIRST-DIFF-BANKED out of the arm list at v1.3.0; this suite`s run list 116 arms, no standing arm added',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R333)(7)-(8): the axiom step at 6 of 6 pins -- five runs committed, pushed, dispatched and read by their ids (six at most), HALTED 0, SIDE-lv-conservation clean at b721, no main or tag touched; the ledger split carried whole to b724 with its price, nothing cut; both in Component 6`s commits',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'split', (S['split'] or '').replace('NOTHING CUT.', 'ONE FILE CUT.'))),
    ('G-DIFFERS-ERRATA', '(R333)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal at 1553808a, no b723 differs or errata bank, the worklist naming none; the weight line and the corrigendum in Component 1`s PLACE-papers commit 763ae914, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v9 ((R333) Component 7), N4: data/b723_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R333-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and b722`s G-RESEARCH-REPRODUCES, untagged; G-READFIRST-DIFF-BANKED CLOSE in the file, out of the list; the claim arms thirty-eight; the file byte-equal at 1607e994 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, (R333)(7): the axiom step`s five runs, one per repaired wave 1 kernel, each read once by its id -- BUILDS, exit 0, no sorry; SIDE-frobenius and SIDE-kernel by push, SIDE-kernel`s halt and its four-place clear on the author`s word (7) with the diff; the lv row; the head COMMITTED 5 ; PUSHED 5 ; DISPATCHED 5 ; READ 5 and the step at 6 of 6 pins',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: the axiom step`s order and hold -- free memory at or above 2,560 MB at every push, dispatch and read; per kernel push before run before read; five dispatches, six at most, by tools/b723_axiom.py alone; no b721 or b722 rebuild route this act',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each repaired wave 1 kernel`s rebuild-b721 beyond its pin by the b723 axiom seat`s commits (one each; SIDE-frobenius three, its first two b721`s rebuild seat`s), off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the two ledgers alone (FINDINGS and OPEN_TRAILS); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b722`s trail record on OPEN_TRAILS (:16310) and its root in the chain', lambda S: '### b722 — lane two, act one hundred and forty-nine, the instruments act under (R332)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS and OPEN_TRAILS): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b722`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches in the command bank %d (N1: (R333)(7)`s five by tools/b723_axiom.py, read by their ids in data/b723_axiom.txt; -1 the command bank not yet written)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           # ### the author's word, Option 2: the --prev names computed from the worklist, no longer a hand list -- every component commit
           # ### (the worklist's C<n>_ names, its "later stages: the commits of the components") and the standing commit (landed at a component)
           # ### the previous act's worklist carries and this act's carries too; a name the previous act's alone carries reads the previous act's
           # ### (no value of this act's to read), and the registration block's REG_* names stay the previous act's, the standing arms reading them
           ) + tuple(sorted(n for n in vars(K707) if re.match(r'^(C\d+_\w+|STANDING_COMMIT)$', n) and hasattr(K, n)))
#⟪END⟫
#⟪SECTION citation 1⟫
    # ### the fill is in the bank (data/b723_ferry.txt), the transcript's text carrying the slot: the quote read from the bank
    hq = _quote(rd(p('data', 'b723_ferry.txt')) or '', '"b722 closed: relay 65430407', '", its rows')
    add('ruling (1)', 'data/b722_closing.txt :1, the head line as the ruling quotes it (the filled slot, data/b723_ferry.txt :7)', bool(hq) and hq[1:] == at(cl, 1),
        at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', '1607e994', 'data/b722_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'the head line as the public relay carries it at 1607e994, its main', bool(pub) and pub[0] == at(cl, 1) and rm.startswith('1607e994'),
        'remote main %s' % rm[:8], '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), (2)', 'events (1)-(19) and 31 defects (data/b722_events.txt, data/b722_defects.txt)', starts == list(range(1, 20)) and len(letters) == 31,
        'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'event (19) at data/b722_events.txt :103, the reading of the twenty', at(ev, 103).startswith('    (19) ') and 'the twenty' in at(ev, 103),
        at(ev, 103)[:60], '0')
    add('ferry (read first)', 'data/b722_closing.txt :469, the carried items', at(cl, 469) == '### CARRIED FORWARD.', at(cl, 469)[:30], '0')
    # ### (R333)(2): the corrigendum and the repeat classes
    add('ruling (2)', 'tools/standing/ at v1.2.2 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.2.2',
#⟪END⟫
#⟪SECTION citation 5⟫
    add('ruling (2)(v)', 'data/standing_clauses_v8.txt present, v9 not yet written', os.path.exists(p('data', 'standing_clauses_v8.txt'))
        and not os.path.exists(p('data', 'standing_clauses_v9.txt')), 'v8 present ; v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    stp = _jl('b722_steps.json')
    stp = stp if isinstance(stp, list) else (stp.get('rows') or [])
    lk = [i + 1 for i, s_ in enumerate(stp) if str(s_.get('subject', '')).startswith('b722 lock')]
    add('ruling (2)(iii)', 'b722`s steps bank: step 26 the lock commit, its phase "gate"', lk == [26] and stp[25].get('phase') == 'gate',
        'lock rows %s' % lk, '1')
    # ### the arm lives in the act's checks tool (tools/b722_checks.py), not in tools/standing/
    hk = [l for l in lines_of(p('tools', 'b722_checks.py')) if 'G-READFIRST-DIFF-BANKED' in l]
    add('ruling (2)(iv)', 'G-READFIRST-DIFF-BANKED named in tools/b722_checks.py (to retire)', bool(hk), '%d lines in b722_checks.py' % len(hk), '1')
    # ### (R333)(3): the open orders
    add('ruling (3)(i)', 'OPEN_TRAILS :16250, the ten open orders', at(ot, 16250).startswith('**The open orders:**') and at(ot, 16250).count('`W-ORD-') == 10,
        '%d orders' % at(ot, 16250).count('`W-ORD-'), '2')
    # ### (R333)(4): the registrations' sources
    add('ruling (4)(i)', 'FINDINGS :5667, sigma 0.9532604748', 'σ = 0.9532604748' in at(fi, 5667), at(fi, 5667)[:60], '3')
    add('ruling (4)(i)', 'FINDINGS :10206, the onsets 6.838396011 and 10.38532711', 'a = 6.838396011' in at(fi, 10206) and 'a = 10.38532711' in at(fi, 10206),
        at(fi, 10206)[:60], '3')
    a2 = lines_of(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'))
    add('ruling (4)(i)', 'OPEN_TRAILS-archive-2 :2982, the band zero 0.79800 + 29.5518i', 'ρ ≈ 0.79800 + 29.5518i' in at(a2, 2982), at(a2, 2982)[:60], '3')
    for f_ in ('b707_onset.txt', 'b709_grid.txt', 'b711_list.json', 'b713_list.json', 'b717_list.json'):
        add('ruling (4)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '3')
    # ### (R333)(6): the coefficient banks
    for f_ in K.COEFF_BANKS:
        add('ruling (6)', f_, os.path.exists(p(*f_.split('/'))), 'present' if os.path.exists(p(*f_.split('/'))) else 'ABSENT', '5')
    # ### (R333)(7) and the addendum's (4): the routes as b722's bank priced them
    adg = lines_of(p(*K.AXIOM_DIAG.split('/')))
    for n_, k_ in ((6, 'SIDE-kernel'), (13, 'SIDE-archimedean'), (22, 'SIDE-frobenius'), (30, 'SIDE-spinor'), (39, 'SIDE-rcurve')):
        add('ruling (7), addendum (4)', '%s :%d, %s`s route' % (K.AXIOM_DIAG, n_, k_), at(adg, n_).startswith('## %s -- run ' % k_), at(adg, n_)[:50], '6')
    add('addendum (4)', '%s :37, the six SIDESpinorLeg names not declared at the pin' % K.AXIOM_DIAG, at(adg, 37).count('SIDESpinorLeg.') == 6, '%d names' % at(adg, 37).count('SIDESpinorLeg.'), '6')
    fz = lines_of(p('data', 'b721_frozen_line.txt'))
    add('addendum (4)', 'data/b721_frozen_line.txt :84, SIDE-frobenius at its pin 2efe9f2', at(fz, 84).startswith('## SIDE-frobenius at v0.1.0 = 2efe9f2'), at(fz, 84)[:50], '6')
    # ### (R333)(8): the ledger split
    add('ruling (8)', 'OPEN_TRAILS :14680, W-ORD-LEDGER-SPLIT-RESOLVER and the cut FINDINGS :456-:6949', 'W-ORD-LEDGER-SPLIT-RESOLVER' in at(ot, 14680) and ':456-:6949' in at(ot, 14680),
        at(ot, 14680)[:60], '7')
    add('ruling (8)', 'data/b680_split_price.txt', os.path.exists(p('data', 'b680_split_price.txt')), 'present', '7')
    # ### the addendum's (1) and (3)
    stc = gr('D:/relay', 'status', '--porcelain', '--', 'data/b720_hook_refusals.txt', 'data/b721_hook_refusals.txt', 'data/b722_relay_push-b722-closing_push_out.txt',
             'data/b722_steps.json')
    for s_ in (' M data/b720_hook_refusals.txt', ' M data/b721_hook_refusals.txt', '?? data/b722_relay_push-b722-closing_push_out.txt', ' M data/b722_steps.json'):
        add('ruling (9), addendum (1)', 'git status: %s' % s_.strip(), s_.strip() in [l.strip() for l in stc.split(NL)], stc.replace(NL, ' | ')[:120], '0')
    rp = lines_of(p('data', 'b722_reproduce.txt'))
    add('addendum (3)', 'data/b722_reproduce.txt :143-:146, I-76 5293 against 6650', at(rp, 143).startswith('I-76   b544_probe_part') and '"count": 5293' in at(rp, 143)
        and "['6650']" in at(rp, 144) and 'M.enumerate_all()' in at(rp, 146), at(rp, 144)[:60], '1')
    # ### (R333)(9): the branches
#⟪END⟫
#⟪SECTION citation 6⟫
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (9)', 'the push-b722-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
#⟪END⟫
#⟪SECTION citation 9⟫
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (9)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (9)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (9)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '7')
#⟪END⟫
#⟪SECTION citation 10⟫
#⟪END⟫
#⟪SECTION citation 11⟫
    # ### b723 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b722_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R333)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool, Component 7) are the corrigendum and v1.3.0's repeat-class repairs, the open orders and the twenty, the registrations, the three
computations (H-ZETAK, H-SUPPORT, H-DIAL), the C2 closed form and its post hoc check, the axiom step at the six pins, the ledger split's price,
the name and address scan, the touch read of v9 and the standing arms, each row by its bank's verdict line or by the line its pattern names
(section_reading); (R333)'s counter line beneath the title, the repeat count beside it, and the claim arms' figure beside the suite's in the
commits section; the author's word after the seal printed from its bank (tools/act_close.py author_words_section, v5 row (74)); the carried
items for b724 ((R333)(11)). The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. Kernels written this act on their rebuild-b721 branches alone ((R333)(7)): one commit each at five pins, no main, no tag.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b724 ((R333)(11)); the open orders by tools/standing/orders.py's output and not a hand list ((R333)(3)(i))
    (Component 7, the Edit tool)."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b723 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FIFTY, THE CHECKPOINT ACT: THE CLOSE TOOLS AT v1.3.0 AND FIVE '
              'REPEAT CLASSES REPAIRED; THE OPEN ORDERS GENERATED, 143 OPEN, THE TWENTY READ; H-SUPPORT AT THREE ZEROS REFUTED, H-ZETAK HELD, '
              'H-DIAL CARRIED; THE C2 CLOSED FORM WRITTEN AND CHECKED POST HOC; THE AXIOM STEP AT 6 OF 6 PINS; THE LEDGER SPLIT CARRIED, UNDER (R333).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 7, the Edit tool; b722's sections over b722's objects not carried). A row of two
    reads its bank's verdict line by vtail; a row of three reads the line its pattern names (a bank with several verdict lines, or written by
    the Write tool without the verdict line's form)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('tools/standing/ at v1.3.0: the seven close tools folded and the repeat classes repaired, each controlled on b722`s banks',
                 'b723_standing_v130.txt'),
                ('the fold built: each tool a template and the act`s sections (tools/acts/b723.py)', 'b723_fold.txt',
                 r'(?m)^  tools/acts/b723\.py: [^\n]*'),
                ('the repeat rule, standing clauses v9 row (83): v8`s rows unchanged and the one row (d9739558)', 'standing_clauses_v9.txt',
                 r'(?m)ROWS 83 ; v8`S ROWS 82 UNCHANGED[^;]*'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE OPEN ORDERS ((R333)(3))', [
                ('tools/standing/orders.py at 763ae914, the rule printed before the orders', 'b723_orders.txt', r'(?m)\*\*ORDERS \d+ ; OPEN \d+ ; CLOSED \d+ ;'),
                ('the orders` controls', 'b723_orders.txt', r'(?m)\*\*THE ORDERS` CONTROLS:[^*]*'),
                ('the locator reading tried on the author`s ruling (3)', 'b723_orders.txt', r'(?m)\*\*THE LOCATOR READING:[^*]*'),
                ('at HEAD after the author`s word (5)`s weed', 'b723_orders.txt', r'(?m)\*\*AT HEAD:[^*]*'),
                ('the twenty of (R332)(14), each against its trigger as written', 'b723_orders_twenty.txt')]),
            ('THE REGISTRATIONS ((R333)(4))', [
                ('H-SUPPORT, H-ZETAK and H-DIAL committed alone at 9ad26421 before any figure at an object they name', 'b723_registrations.txt'),
                ('H-SUPPORT`s rule output and predictions by a commit of their own (0e91c670), before any onset', 'b723_support_rule.txt')]),
            ('THE COMPUTATIONS ((R333)(5))', [
                ('H-ZETAK: zeta_K on Q0`s two onset windows, the controls first, the grade at the end', 'b723_zetak.txt'),
                ('H-SUPPORT: the onsets at the zeros the rule named, the controls first, the grade at the end', 'b723_support.txt'),
                ('H-DIAL: the build priced, not run, carried with its registration', 'b723_dial_price.txt')]),
            ('THE C2 CLOSED FORM ((R333)(6))', [
                ('the closed form written as a derivation, not compiled', 'b723_c2_closed_form.txt'),
                ('its check against the coefficient banks of b711-b722, every row POST HOC', 'b723_c2_check.txt')]),
            ('THE AXIOM STEP ((R333)(7))', [
                ('the six wave 1 pins: five repaired and run by their ids on the rebuild-b721 branches, SIDE-lv-conservation clean at b721', 'b723_axiom.txt')]),
            ('THE LEDGER SPLIT ((R333)(8))', [
                ('the split`s budget printed before any cut', 'b723_split_price.txt')]),
            ('THE NAME AND ADDRESS ((R332)(9))', [
                ('the scan over every commit and bank of the act, the previous address and name held in memory, the counts alone', 'b723_address_scan.txt')]),
            ('THE RESEARCH INSTRUMENTS REPRODUCED (b722`s standing arm G-RESEARCH-REPRODUCES)', [
                ('tools/research/reproduce.py`s full run, one row per instrument I-41 to I-108, a planted wrong figure per run row', 'b723_reproduce.txt')]),
            ('THE TOUCH READ (standing clauses v9)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: on the rebuild-b721 branches alone ((R333)(7)) -- one commit each by the b723 axiom seat`s neutral identity at',
    '    SIDE-archimedean, SIDE-rcurve, SIDE-spinor, SIDE-frobenius and SIDE-kernel (SIDE-kernel`s fourth line on the author`s word (7), its',
    '    diff printed before the commit), each pushed and run once, read by its run id ; SIDE-lv-conservation clean at b721, not run ; no',
    '    kernel`s main touched, no tag cut (N5) ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved, the challenge branch',
    '    challenge-b720-h2-sign-iff-rh standing ; the pin-b718-de5ce8a9 branches left as banked ; port-b707 of SIDE-lv-conservation at',
    '    b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main and its deposit v0.10.0 unmoved ;',
    '    SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host, the runner dispatches',
    '    (R333)(7)`s five alone (six at most), each read by its id ; free memory read before each computation, push, dispatch and read ;',
    '    the push-b722-* branches of relay and PLACE-papers deleted at step zero by name after --merged listed them, one per command and each',
    '    its own message ; nothing vendored ; b628`s local intake bank, the navigator`s export, b671`s uncompressed points file and the',
    '    earlier acts` units files untracked ; N2: the registrations committed alone at 9ad26421 before any figure bank, H-SUPPORT`s rule',
    '    output and predictions at 0e91c670 before any onset, each tool`s controls printed before its figures ; N3: every grade at its bank`s',
    '    end, the C2 closed form`s check labelled POST HOC wherever named ; (R332)(9): no new occurrence of the author`s name or address in',
    '    anything the act wrote, committed or pushed (relay data/b723_address_scan.txt), the commits under the GitHub login and its noreply',
    '    address ; no identifier of the author in any outbound request header, URL, input or payload, or in any workflow file ; no secret',
    '    added ; the seat`s plain requests to github.com (its git reads, pushes, dispatches and run reads) the act`s outbound calls ; the',
    '    deposit route untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS (the weight line, the',
    '    corrigendum, the entry) and OPEN_TRAILS (the closing lines of (R333)(3), the trail) appended ; no paper cut, moved or renamed, the',
    '    ledger split carried whole ((R333)(8)) ; no ERRATA, FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt and the',
    '    corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.3.0 by',
    '    (R333)(2), the seven close tools folded ; data/standing_clauses_v9.txt by a commit of its own ((R333)(2)(v)) ; the hook in',
    '    D:/.claude/settings.json unedited ; the per-act tools of b698-b722 unedited ; the mirror zip written outside every repository over',
    '    the roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ;',
    '    nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R333)(13)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        the twenty of (R332)(14) each against its trigger (relay data/b723_orders_twenty.txt): W-ORD-LEDGER-SPLIT-RESOLVER acted (the',
    '        split priced and carried), five priced and named, W-ORD-PROBE-HOLD discharged by reading, W-ORD-STATUS-CELLS offered for retire',
    '        at the root`s prompt; four moved to CLOSED at HEAD by their closing lines (PROBE-HOLD, Q0-ZEROS-443, READING5-INDEPENDENCE, and',
    '        E1-CFG on the author`s word (5)).',
    '    (c) For b724, each from its bank: H-DIAL`s build as priced, its registration committed (relay data/b723_dial_price.txt); the ledger',
    '        split carried whole with its price (relay data/b723_split_price.txt); the lv sorry`s discharge, not available as stated (relay',
    '        data/b723_axiom.txt), its course the author`s at the root`s prompt; the reproduction`s NOT RUN rows I-56, I-57, I-61, I-107 (relay',
    '        data/b723_reproduce.txt); the C2 compile where the author names it from b722`s price; the report tool outside the sealed list;',
    '        the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); challenge-b720-h2-sign-iff-rh of',
    '        SIDE-explicit-formula; the pin-b718-de5ce8a9 branches as banked; the rebuild-b721 branches of the wave 1 kernels, five carrying',
    '        b723`s axiom commit.',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on main, five rebuild-b721 branches carrying b723`s axiom commit ((R333)(7)), no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b723: the standing repairs are v1.3.0's ((R333)(2), relay data/b723_standing_v130.txt, read in the corrigendum section); the
    # ### carry's diffs here (b723 carried at step zero before the fold; its tools since are the templates and tools/acts/b723.py)
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act, one commit each on '
          'the %s branches of five wave 1 kernels ((R333)(7)); SIDE-lv-conservation`s main untouched, port-b707 at b712`s tip %s, its checkout at main '
          'for this read)' % (len(ks), K.JOIN_NEW_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b723's form over b723's objects (Component 7, the Edit tool; b722's form in git at b722's record tool): the corrigendum's foot and v1.3.0's
    controls; the orders at HEAD, their controls and the twenty; the registrations and H-SUPPORT's rule; H-ZETAK, H-SUPPORT and H-DIAL at their
    feet; the C2 closed form and its check, post hoc; the axiom step; the ledger split; the reproduction run; the address scan; each by its own
    lines through _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v3 = _bfig('%s_standing_v130.txt' % ACT, r'\*\*v1\.3\.0: CONTROLS ([^;]+?) ; CASES (\d+) ; AS WANTED (\d+) ;', 'v1.3.0`s controls')
    od = _bfig('%s_orders.txt' % ACT, r'\*\*AT HEAD: ORDERS (\d+) ; OPEN (\d+) ; CLOSED (\d+) ; STATUS MOVED FROM ([0-9a-f]+) (\d+)\.\*\*', 'the orders at HEAD')
    oc = _bfig('%s_orders.txt' % ACT, r'\*\*THE ORDERS` CONTROLS: CASES (\d+) ; AS WANTED (\d+) ;', 'the orders` controls')
    tw = _bfig('%s_orders_twenty.txt' % ACT, r'\*\*THE TWENTY: TRIGGER NOT MET (\d+) ; TRIGGER MET (\d+) \(ACTED THIS ACT (\d+), PRICED AND NAMED (\d+)\) ; '
               r'DISCHARGED BY READING (\d+) ; OFFERED FOR RETIRE (\d+) ;', 'the twenty`s foot')
    rg = _bfig('%s_registrations.txt' % ACT, r"\*\*REGISTERED: ([^;]+) ; ZEROS NAMED (\d+) ; FIGURES AT A REGISTERED OBJECT (\d+) ;", 'the registrations` foot')
    sr = _bfig('%s_support_rule.txt' % ACT, r'\*\*H-SUPPORT`S RULE: ZEROS READ (\d+) ; BANKED EXCLUDED (\d+) OF (\d+) ; WITHIN REACH (\d+) ; SELECTED (\d+) ; '
               r'CONTINUES INTO -15/-39 (\w+) ; ONSETS COMPUTED (\d+)\.\*\*', 'H-SUPPORT`s rule`s foot')
    zk = _bfig('%s_zetak.txt' % ACT, r'\*\*H-ZETAK: C1 ([^;]+) ; C2 ([^;]+) ; C3 (\w+) ; rho0 ([^;]+) ; band ([^;]+) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE) ;',
               'H-ZETAK`s foot')
    sp = _bfig('%s_support.txt' % ACT, r'\*\*H-SUPPORT: C1 ([^;]+) ; ZEROS (\d+) ; ONSETS COMPUTED (\d+) ; WITHIN 0\.03 (\d+) ; BEYOND REACH (\d+) ; '
               r'FALSIFIER (FIRED|NOT FIRED) ; THE HYPOTHESIS (HELD|REFUTED|NOT SCORABLE)\.\*\*', 'H-SUPPORT`s foot')
    dl = _bfig('%s_dial_price.txt' % ACT, r'\*\*H-DIAL: BUILD PRICED \(([^)]*)\) ; FIGURES AT F_c (\d+) ; (NOT RUN|RUN) ; (CARRIED[^.]*)\.\*\*', 'H-DIAL`s foot')
    cf = _bfig('%s_c2_closed_form.txt' % ACT, r'\*\*THE C2 CLOSED FORM: WRITTEN AS A DERIVATION, (\w+) STEPS ; CHECKED POST HOC, (\d+) ROWS OF (\d+) '
               r'REPRODUCED, THE PLANTED e_p FAILING ; NOT COMPILED\.\*\*', 'the closed form`s foot')
    ck = _bfig('%s_c2_check.txt' % ACT, r'\*\*THE C2 CLOSED FORM, POST HOC: C0 AS WANTED ; C1 \(PLANTED e_p\) FAILS, AS WANTED ; ROWS (\d+), REPRODUCED (\d+) ; '
               r'FIELDS (\d+) ; NEGATIVE AT OMEGA <= 3: (\d+) ; A BAD RAMIFIED PRIME AT EVERY FIELD (True|False) ;', 'the check`s foot')
    ax = _bfig('%s_axiom.txt' % ACT, r'\*\*THE AXIOM STEP AT (\d+) OF (\d+) PINS \((\d+) REPAIRED AND RUN THIS ACT, ([^)]*)\) ; HALTED (\d+) \(([^)]*)\) ; '
               r'RUNS (\d+) ; THE lv SORRY`S DISCHARGE ([^;]*) ; NO MAIN OR TAG TOUCHED\.\*\*', 'the axiom step`s foot')
    sl = _bfig('%s_split_price.txt' % ACT, r'\*\*THE LEDGER SPLIT: (CARRIED WHOLE TO b\d{3}|LANDED)[^-]*-- (\d+) CITATION OCCURRENCES MOVED \((\d+) IN LIVE '
               r'TOOLS\), THE SPLIT ABOUT ([\d.-]+) H BEFORE A CLOSE OF ([\d.]+) H ; ([^.]*)\.\*\*', 'the split`s foot')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PREVIOUS NAME: (\d+) ; PLACES (\d+) ; CONTROLS 4 OF 4 '
               r'AS WANTED ;', 'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'),
                v130_ctl=v3[0], v130_n=len(re.findall(r'\([a-z]+\)', v3[0])), v130_cases=v3[1], v130_wanted=v3[2],
                od_n=od[0], od_open=od[1], od_closed=od[2], od_from=od[3], od_moved=od[4], oc_cases=oc[0], oc_wanted=oc[1],
                tw_not=tw[0], tw_met=tw[1], tw_acted=tw[2], tw_priced=tw[3], tw_read=tw[4], tw_retire=tw[5],
                rg_names=rg[0], rg_zeros=rg[1], rg_figs=rg[2],
                sr_read=sr[0], sr_excl=sr[1], sr_excl_of=sr[2], sr_reach=sr[3], sr_sel=sr[4], sr_cont=sr[5], sr_onsets=sr[6],
                zk_c1=zk[0], zk_c2=zk[1], zk_c3=zk[2], zk_rho0=zk[3], zk_band=zk[4], zk_grade=zk[5],
                sp_c1=sp[0], sp_zeros=sp[1], sp_onsets=sp[2], sp_within=sp[3], sp_beyond=sp[4], sp_fals=sp[5], sp_grade=sp[6],
                dl_price=dl[0], dl_figs=dl[1], dl_run=dl[2], dl_word=dl[3],
                cf_steps=cf[0], cf_rows=cf[1], cf_of=cf[2], ck_rows=ck[0], ck_rep=ck[1], ck_fields=ck[2], ck_neg=ck[3], ck_ram=ck[4],
                ax_at=ax[0], ax_of=ax[1], ax_rep=ax[2], ax_beside=ax[3], ax_halted=ax[4], ax_halted_names=ax[5], ax_runs=ax[6], ax_lv=ax[7],
                sl_word=sl[0], sl_occ=sl[1], sl_live=sl[2], sl_hours=sl[3], sl_close=sl[4], sl_cut=sl[5],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                addr=ad[0], name=ad[1], prev_name=ad[2], addr_places=ad[3],
#⟪END⟫
#⟪SECTION record 6⟫
def _axiom_kind(rows, kind):
    """(R333)(7): the axiom step's rows of one kind as banked (data/b723_axiom_rows.json: commit, push, dispatch, read and the drafts)."""
    return [r for r in rows or [] if r.get('kind') == kind]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R333): no lean process runs on this host; the runner dispatches are those of (R333)(7) alone, six at most, each read by its run id.
    From the command bank (the seat's commands, read live from the capture by the `commands` route: local lean none; the dispatch commands
    those of tools/b723_axiom.py dispatch) and the axiom step's rows (relay data/b723_axiom_rows.json: each dispatch, by command or on its
    push, and each read by its run id), against the worklist's B723_RUNS (Component 7, the Edit tool; b722's N1 read b722's runs)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = json.loads(rdn('%s_axiom_rows.json' % ACT) or '[]')
    dsp, rds = _axiom_kind(rows, 'dispatch'), _axiom_kind(rows, 'read')
    ran = sorted((r.get('kernel'), str(r.get('run'))) for r in dsp)
    want = sorted((k, str(r)) for k, r in K.B723_RUNS)
    read_ids = sorted(str(r.get('run')) for r in rds)
    by_cmd = [r for r in dsp if not r.get('via')]
    ok = bool(cm) and not seat_lean and len(ran) <= K.MAX_DISPATCHES and ran == want and read_ids == sorted(r for _k, r in want) \
        and len(disp) == len(by_cmd)
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b723_commands.json): %s; dispatch commands in the capture: %s against '
        'the rows` dispatches by command %d; the runs dispatched (relay data/b723_axiom_rows.json) %d of %d at most, equal to the worklist`s '
        'B723_RUNS: %s (%s); each read by its id: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', len(disp) if cm else 'unread', len(by_cmd), len(ran), K.MAX_DISPATCHES, ran == want,
            ', '.join('%s %s' % x for x in ran) or 'NONE', read_ids == sorted(r for _k, r in want)))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (Component 7, the Edit tool, over b723's objects; b722's chain over b722's registrations in git at b722's record tool): each figure
# ### bank of a registered object and the commit that landed it, the registrations' commit an ancestor of it and the bank absent at it
N2_REGISTERED = (('data/b723_support_rule.txt', 'C3_PRED'), ('data/b723_zetak.txt', 'C4_ZETAK'), ('data/b723_support.txt', 'C4_SUPPORT'),
                 ('data/b723_dial_price.txt', 'C4_DIAL'))
# ### N2: each tool's controls (or its rule) before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b723_support_rule.txt', 'THE RULE (data/b723_registrations.txt', 'THE ZEROS IN DECREASING'),
               ('data/b723_zetak.txt', '## (C1) ', '## THE zeta_K FORM AT EACH WINDOW'),
               ('data/b723_support.txt', '## (C1) THE BANKED ONSETS', '## THE ZEROS, IN THE RULE`S ORDER'),
               ('data/b723_c2_check.txt', '## (C0) ', '## THE ROWS, EACH POST HOC'),
               ('data/b723_orders.txt', '## THE CONTROLS ((R333)(3)(i))', '## THE ORDERS ('),
               ('data/b723_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R333): the registrations committed before any figure bank -- data/b723_registrations.txt alone at its commit, that commit an ancestor
    of every commit landing a figure bank of a registered object and none of those banks at it, the registrations at HEAD equal to that blob;
    H-SUPPORT's rule output and predictions by a commit of their own before any onset; each tool's controls print before its figures. From
    git (the commits' files, merge-base, the blob at HEAD against the registrations' commit) and the banks' own lines."""
    reg_files = g(ROOT, 'show', '--name-only', '--format=', K.REG_COMMIT).split()
    reg_alone = reg_files == [K.REGISTRATIONS]
    reg_same = bool(_show(ROOT, 'HEAD', K.REGISTRATIONS)) and (_show(ROOT, K.REG_COMMIT, K.REGISTRATIONS) or '') == (_show(ROOT, 'HEAD', K.REGISTRATIONS) or '')
    anc = [(p, getattr(K, c) != K.REG_COMMIT and grc(ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, getattr(K, c)) == 0
            and not _show(ROOT, K.REG_COMMIT, p)) for p, c in N2_REGISTERED]
    pred_files = g(ROOT, 'show', '--name-only', '--format=', K.C3_PRED).split()
    pred_first = pred_files == ['data/b723_support_rule.txt'] and K.C3_PRED != K.C4_SUPPORT \
        and grc(ROOT, 'merge-base', '--is-ancestor', K.C3_PRED, K.C4_SUPPORT) == 0 and not _show(ROOT, K.C3_PRED, 'data/b723_support.txt')
#⟪END⟫
#⟪SECTION record 12⟫
    ok = reg_alone and reg_same and all(o for _p, o in anc) and pred_first and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the registrations` commit %s carrying %s alone: %s; at HEAD equal to its blob there: %s; that commit an ancestor of each figure bank`s '
        'commit, the bank absent at it: %s; H-SUPPORT`s rule output by its own commit %s (%s), before the onsets` %s: %s; each tool`s controls '
        'or rule before its figures: %s' % (
            K.REG_COMMIT[:8], K.REGISTRATIONS, reg_alone, reg_same, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in anc),
            K.C3_PRED[:8], ', '.join(pred_files) or 'unread', K.C4_SUPPORT[:8], pred_first,
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (Component 7, the Edit tool, over b723's objects; b722's over its walk and price in git at b722's record tool): the banks whose
# ### grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b723_support_rule.txt', ('ONSETS COMPUTED 0',)), ('b723_zetak.txt', ('THE HYPOTHESIS HELD',)),
             ('b723_support.txt', ('THE HYPOTHESIS REFUTED',)), ('b723_dial_price.txt', ('NOT RUN', 'CARRIED')),
             ('b723_c2_closed_form.txt', ('CHECKED POST HOC', 'NOT COMPILED')), ('b723_c2_check.txt', ('POST HOC', 'REPRODUCED')),
             ('b723_axiom.txt', ('THE AXIOM STEP AT',)), ('b723_split_price.txt', ('CARRIED WHOLE', 'NOTHING CUT')),
             ('b723_orders.txt', ('AT HEAD: ORDERS',)), ('b723_reproduce.txt', ('REPRODUCES',)))
# ### N3: a sentence calling the closed form compiled -- "compiled" not read with its negation (not, never, nor) -- or new
N3_COMPILED = re.compile(r'(?i)\bcompiled\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|un)[ -]?(?:yet |been |\w+ and not )?compiled\b')
N3_NEW = re.compile(r'(?i)\bnew\b')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R333): every grade prints at its end; the C2 closed form's check is labelled POST HOC wherever it is named; no sentence of the entry
    calls it compiled or new. From the graded banks (each bank's last line its foot, the foot carrying its grade's words), the check's rows
    (each led POST HOC, their count the foot's and the closed form's), and the entry as composed (the findings bank's text, or the composer
    before it is written): every sentence naming the closed form and its check carrying POST HOC; none calling it compiled but in negation,
    none calling it new."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
    lead = re.findall(r'(?m)^  (\S+(?: \S+)?)  D\s+-\d+ ', rdn('%s_c2_check.txt' % ACT))
    rows_ph = bool(lead) and all(x == 'POST HOC' for x in lead)
#⟪END⟫
#⟪SECTION record 19⟫
    rows_ok = rows_ph and len(lead) == int(f['ck_rows']) and f['ck_rows'] == f['ck_rep']
    foot_ok = f['cf_rows'] == f['ck_rows'] == f['cf_of']
#⟪END⟫
#⟪SECTION record 20⟫
    called = [s.strip()[:120] for s in sents if N3_COMPILED.search(N3_NEGATED.sub('', s))]
    cf_s = [s for s in sents if re.search(r'(?i)closed form', s)]
    unlabelled = [s.strip()[:120] for s in cf_s if re.search(r'(?i)\bcheck', s) and not re.search(r'(?i)post hoc', s)]
    newer = [s.strip()[:120] for s in cf_s if N3_NEW.search(s)]
    ok = all(o for _n, o in graded) and rows_ok and foot_ok and not called and not unlabelled and not newer
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the check`s rows each led POST HOC (relay data/b723_c2_check.txt), %d, equal to '
        'its foot`s %s and the closed form`s %s of %s: %s; the sentences of %s naming the closed form`s check without POST HOC: %s; calling '
        'anything compiled but in negation: %s; calling the closed form new: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), len(lead), f['ck_rows'], f['cf_rows'], f['cf_of'], rows_ok and foot_ok, src,
            unlabelled or 'NONE', called or 'NONE', newer or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫


# ### (R333)(1), N4: the banks the close appends to by design after the lock, each read apart -- the step bank (a row per commit), this tool's
# ### hashes bank (a line per bank it writes) and the hook's refusals (a line per refusal); and the mirror's previous-build record, which the
# ### mirror build at [23] rewrites by the ferry's (W) list ((R333)(11))
N4_APPENDED = ('data/%s_steps.json' % ACT, 'data/%s_bank_hashes.json' % ACT, 'data/%s_hook_refusals.txt' % ACT, 'tools/mirror_prevbuild.json')


def _post_lock_edits():
    """the lock's time from the face (its `locked at (UTC)` line), the lock commit (the first relay commit at or after it, carrying the face),
    the relay commits after that one, and among the files they touch, and the working tree's changes, those that are the face, under tools/, or
    an act bank tracked at the lock commit -- less N4_APPENDED."""
    face = rd(FACE) or ''
    m = re.search(r'locked at \(UTC\) : (\S+)', face)
    lock = _iso_epoch(m.group(1)) if m else None
    out = dict(lock=lock, lock_iso=m.group(1) if m else None, lock_commit=None, after=[], edited=[], dirty=[])
    if lock is None:
        return out
    rows = [l.split(' ', 1) for l in g(ROOT, 'log', '--reverse', '--format=%H %ct', '%s..HEAD' % K.PRE_RELAY).split(NL) if l.strip()]
    face_rel = os.path.relpath(FACE, ROOT).replace(os.sep, '/')
    lc = next((h for h, ct in rows if int(ct) >= lock and face_rel in g(ROOT, 'show', '--name-only', '--format=', h).split()), None)
    out['lock_commit'] = lc
    if lc is None:
        return out
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
    # ### (R333)(1), N4: no bank, face or tool edited after the lock gate, a restore counting as an edit (Component 8, the Edit tool; b722's
    # ### arm read the drafts and the rebuild branches) -- read from git, not from end states: every relay commit after the lock commit, its
    # ### files against the face, tools/ and the act's banks tracked at the lock commit; the working tree's changes to them besides
    me = _post_lock_edits()
    lock_ok = me['lock'] is not None and not me['edited'] and not me['dirty']
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and lock_ok
#⟪END⟫
#⟪SECTION record 24⟫
        'the lock at %s, its commit %s; the commits after it (relay) %d, touching the face, a tool or a bank tracked at the lock commit: %s; the '
        'working tree`s changes to them: %s; appended by design and read apart: %s; ' % (
            me['lock_iso'] or 'NOT LOCKED', (me['lock_commit'] or 'none')[:8], len(me['after']), me['edited'] or 'NONE', me['dirty'] or 'NONE',
            ', '.join(N4_APPENDED)) +
#⟪END⟫
#⟪SECTION record 25⟫
    # ### (R333)(7), (11), N5 (Component 7, the Edit tool): no kernel's main touched and no tag cut -- every ref of every kernel carrying a
    # ### commit made after the act's opening commit is the rebuild-b721 branch of a kernel of (R333)(7) at the commit banked for it
    # ### (K.REBUILD_COMMITS), and those five are all there; no .lean file changed or untracked in a kernel's tree; the rebuild-b721
    # ### branches kept; the address scan's count from its bank (relay data/b723_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    rb_want = dict(K.REBUILD_COMMITS)
    lean_w, rb_new = [], []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        kn = os.path.basename(kp)
        refs = [l.split() for l in g(kp, 'for-each-ref', '--format=%(refname) %(objectname) %(committerdate:unix)', 'refs/heads', 'refs/tags').split(NL)
                if l.strip()]
        for r_ in refs:
            if len(r_) == 3 and r_[2].isdigit() and int(r_[2]) > start:
                if r_[0] == 'refs/heads/' + K.REBUILD_BRANCH and kn in rb_want and r_[1].startswith(rb_want[kn]):
                    rb_new.append(kn)
                else:
                    lean_w.append('%s %s (a commit after the act`s start)' % (kn, r_[0]))
        if [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]:
            lean_w.append('%s (a .lean file in the tree)' % kn)
    rb_ok = sorted(set(rb_new)) == sorted(rb_want)
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w and rb_ok \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b723_address_scan.txt): PREVIOUS ADDRESS: %s; a commit after the act`s opening commit on any ref of a '
            'kernel other than the banked %s commits, or a .lean file in a kernel`s tree (%d kernels read): %s; the %s commits banked at their '
            'branches: %s (%s); the branch kept on the six wave 1 kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', K.REBUILD_BRANCH, len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, rb_ok,
                ', '.join(sorted(set(rb_new))) or 'NONE', len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b723 — lane two, act one hundred and fifty, the checkpoint act under (R333): b722 at its weight and its corrigendum; the close '
            'tools at v1.3.0 and the repeat classes; the open orders generated and the twenty read; the registrations; H-ZETAK, H-SUPPORT and '
            'H-DIAL; the C2 closed form, checked post hoc; the axiom step at the six pins; the ledger split priced')
#⟪END⟫
#⟪SECTION record 29⟫
def _support_lists():
    """H-SUPPORT's falsifier as its bank prints it: (the zeros it fired at, the zeros beyond reach)."""
    t = rdn('%s_support.txt' % ACT)
    a = re.search(r'(?m)^THE FALSIFIER .*: FIRED at \[([^\]]*)\]', t)
    b = re.search(r'(?m)^BEYOND REACH, NO ONSET COMPUTED .*: \[([^\]]*)\]', t)
    return ([x.strip(" '") for x in a.group(1).split(',') if x.strip()] if a else [],
            [x.strip(" '") for x in b.group(1).split(',') if x.strip()] if b else [])


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 7 form ("the close tools at v1.3.0 and <r> repeat classes repaired; the open
    orders generated, <o> open, the twenty read; H-SUPPORT at <z> zeros <HELD | REFUTED | carried>, H-ZETAK <HELD | REFUTED>, H-DIAL <HELD |
    REFUTED | carried>; the C2 closed form written and checked post hoc; the axiom step at <j> of 6 pins; the ledger split <landed | carried>"),
    every figure from the banks (Component 7, the Edit tool; b722's title over b722's objects in git at b722's record tool)."""
#⟪END⟫
#⟪SECTION record 31⟫
    dial = 'carried' if f['dl_run'] == 'NOT RUN' and f['dl_word'].startswith('CARRIED') else f['dl_run']
    return ('## The close tools at %s and %s repeat classes repaired; the open orders generated, %s open, the twenty read; H-SUPPORT at %s zeros '
            '%s, H-ZETAK %s, H-DIAL %s; the C2 closed form written and checked post hoc; the axiom step at %s of %s pins; the ledger split %s' % (
                f['ver'], num_word(f['v130_n']), f['od_open'], num_word(int(f['sp_zeros'])), f['sp_grade'], f['zk_grade'], dial, f['ax_at'],
                f['ax_of'], 'carried' if f['sl_word'].startswith('CARRIED') else 'landed'))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letters, primed where they are: the reader takes a letter with its prime (b723's gate dry run, defect (e'))
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    fired, beyond = _support_lists()
    return ('(1) the open orders by tools/standing/orders.py`s rule, %s of %s open at PLACE-papers main, the trail’s open-orders line written '
            'from its output, none carried by hand; its controls print after its output, not before (relay data/b723_orders.txt); (2) the twenty '
            'against their triggers as written: %s met, %s acted and %s priced and named, %s discharged by reading, %s offered for retire (relay '
            'data/b723_orders_twenty.txt); (3) H-SUPPORT %s at %s zeros, the falsifier fired at %s; %s beyond reach, not counted as a firing; its successor registered at '
            '%s (relay data/b723_support.txt); H-ZETAK %s; H-DIAL priced and carried, its registration committed (relay data/b723_dial_price.txt); '
            '(4) the C2 closed form written as a derivation and checked post hoc, %s of %s rows reproduced, not compiled, the compile where the '
            'author names it (relay data/b723_c2_check.txt); (5) the axiom step at %s of %s pins, %s runs each read by its id, the lv sorry’s '
            'discharge %s -- the author’s choice at the root’s prompt (relay data/b723_axiom.txt); (6) the ledger split %s with its price, nothing '
            'cut (relay data/b723_split_price.txt); (7) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); '
            '(8) %s and the seat’s %s defect%s as lettered' % (
                f['od_open'], f['od_n'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'], f['tw_retire'], f['sp_grade'], f['sp_zeros'],
                ', '.join(fired) or 'none', ', '.join(beyond) or 'none', K.NEXT_ACT, f['zk_grade'], f['ck_rep'], f['ck_rows'], f['ax_at'],
                f['ax_of'], f['ax_runs'], f['ax_lv'].lower(), f['sl_word'].lower(),
#⟪END⟫
#⟪SECTION record 33⟫
def _axiom_line():
    """the axiom step's runs as its rows bank them: `<kernel> <run> <verdict>` for each read."""
    rows = json.loads(rdn('%s_axiom_rows.json' % ACT) or '[]')
    return ', '.join('%s %s %s' % (r.get('kernel'), r.get('run'), r.get('verdict')) for r in _axiom_kind(rows, 'read')) or 'unread'


def _repeats(act=ACT):
    """v9 row (83): the repeat count beside the counter -- the rows of the act's defects and events banks (as _counter reads them) tagged
    REPEAT after their CLAIM or CLOSE, and the rows read."""
    rows = []
    for name in ('%s_defects.txt' % act, '%s_events.txt' % act):
        rows += [l for l in rdn(name).split(NL) if re.match(r"^    \((?:[a-z]'?|\d+)\) ", l)]
    return sum(1 for l in rows if re.search(r'\[(?:CLAIM|CLOSE) ; REPEAT\b', l)), len(rows)


def _runs3(act=ACT):
    """v9 row (83): "a class that repeats in three acts running is the next act's opening component" -- each row of the act's defects bank
    tagged REPEAT <the previous act> (<letter>) whose row in the previous act's defects bank is itself tagged REPEAT <the act before> (...):
    a list of (this act's letter, 'b<n-2> (x) -> b<n-1> (y) -> b<n> (z)'). A REPEAT naming an older act, or no letter, is not a run of three."""
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
            'author beside (R333)(11)’s naming of b724): %d rows in %d classes -- %s' % (len(r), len(by), '; '.join(
                '%s as %s' % (k, ', '.join('(%s)' % x for x in v)) for k, v in sorted(by.items())) or 'none'))


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 7, the Edit tool, over b723's objects;
    b722's composer over b722's objects kept below as _finding_text_b722, not called, and in git at b722's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    rep, tot = _repeats()
    fired, beyond = _support_lists()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    dial = 'carried' if f['dl_run'] == 'NOT RUN' and f['dl_word'].startswith('CARRIED') else f['dl_run']
    e = ['', _title(), '',
         'The close tools stand at %s, each folded into one template with the act’s sections beside it and %s repeat classes repaired, their '
         'controls %s of %s as wanted; the open orders are generated from the record by tools/standing/orders.py, %s of %s open at PLACE-papers '
         'main, and the twenty of (R332)(14) are read against their triggers as written; H-SUPPORT, its rule and predictions committed before '
         'any onset, is %s at its %s zeros -- %s onsets computed, %s within 0.03, %s beyond reach -- while H-ZETAK is %s at Q0’s two onset '
         'windows and H-DIAL is priced and %s with its registration committed; the C2 closed form is written as a derivation and checked post '
         'hoc against %s banked rows, %s reproduced, not compiled; the axiom step stands at %s of %s wave 1 pins, %s runs each read by its id; '
         'and the ledger split is %s with its price.' % (
             f['ver'], num_word(f['v130_n']), f['v130_wanted'], f['v130_cases'], f['od_open'], f['od_n'], f['sp_grade'], num_word(int(f['sp_zeros'])),
             f['sp_onsets'], f['sp_within'], f['sp_beyond'], f['zk_grade'], dial, f['ck_rows'], f['ck_rep'], f['ax_at'], f['ax_of'], f['ax_runs'],
             f['sl_word'].lower()), '',
         '*Filed at b723 on the author’s ruling `(R333)`; %d question%s put before the root. Banks: relay `data/b723_corrigendum.txt`, '
         '`data/b723_standing_v130.txt`, `data/b723_orders.txt`, `data/b723_orders_twenty.txt`, `data/b723_registrations.txt`, '
         '`data/b723_support_rule.txt`, `data/b723_zetak.txt`, `data/b723_support.txt`, `data/b723_dial_price.txt`, '
         '`data/b723_c2_closed_form.txt`, `data/b723_c2_check.txt`, `data/b723_axiom.txt`, `data/b723_split_price.txt`, '
         '`data/b723_reproduce.txt`, `data/b723_address_scan.txt`, `data/b723_touch.txt`, `data/b723_standing_figures.txt`, '
         '`data/b723_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repeat classes** ((R333)(1)-(2), `%s`, `%s`, `%s`): b722 entered at its weight (FINDINGS :%s); the '
         'corrigendum of b722’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- '
         'at FINDINGS :%s, the corrigenda bank appended at row (%s); tools/standing/ at %s: the seven close tools folded into templates with the '
         'act’s sections, the pipe-free reader, the lock row, G-READFIRST-DIFF-BANKED retired and the seal’s list from SEALED, its controls %s '
         '-- %s cases, %s as wanted (relay data/b723_standing_v130.txt); standing clauses v9 at `%s`, v8 with row (83), a class repeating in '
         'three acts running the next act’s opening component.' % (
             K.C1_RELAY[:8], K.C1_PP[:8], K.C1_V130[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'],
             f['corr_close'], f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v130_ctl'], f['v130_cases'], f['v130_wanted'],
             K.STANDING_COMMIT[:8]), '',
         '**The open orders** ((R333)(3), `%s`, `%s`, `%s`): the generator’s rule printed before its output; at PLACE-papers main %s orders, '
         '%s open, %s closed, %s moved from `%s` by the three closing lines of (R333)(3)(ii) and the dated line of the author’s word (5) (relay '
         'data/b723_orders.txt :282); its controls %s of %s as wanted, printed after '
         'its output; the locator reading tried on the author’s word and broken by the record, the rule as ruled earlier standing (`%s`); '
         'the trail’s open-orders line written from the tool’s output, none carried by hand. The twenty of (R332)(14), each against its '
         'trigger as written: not met %s, met %s (acted %s, priced and named %s), discharged by reading %s, offered for retire %s (relay '
         'data/b723_orders_twenty.txt).' % (
             K.C2_RELAY[:8], K.C2_PP[:8], K.C2_WEED_PP[:8], f['od_n'], f['od_open'], f['od_closed'], f['od_moved'], f['od_from'], f['oc_wanted'],
             f['oc_cases'], K.C2_LOCATOR[:8], f['tw_not'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'], f['tw_retire']), '',
         '**The registrations** ((R333)(4), N2, `%s`, `%s`): %s committed alone before any figure at an object they name, zeros named %s, '
         'figures %s (relay data/b723_registrations.txt); H-SUPPORT’s rule printed first and its output, each a*_pred, by a commit of its own '
         'before any onset -- %s off-line zeros read, the banked %s of %s excluded by name, %s within reach, %s selected, onsets computed %s '
         '(relay data/b723_support_rule.txt).' % (
             K.REG_COMMIT[:8], K.C3_PRED[:8], f['rg_names'], f['rg_zeros'], f['rg_figs'], f['sr_read'], f['sr_excl'], f['sr_excl_of'],
             f['sr_reach'], f['sr_sel'], f['sr_onsets']), '',
         '**H-ZETAK** ((R333)(5)(i), N3, `%s`): the Dedekind zeta of Q(sqrt -23) at Q0’s two onset windows, the controls first -- C1 %s, C2 %s, '
         'C3 %s, beside and forced -- then rho0 %s and the band %s: %s (relay data/b723_zetak.txt).' % (
             K.C4_ZETAK[:8], f['zk_c1'], f['zk_c2'], f['zk_c3'], f['zk_rho0'], f['zk_band'], f['zk_grade']), '',
         '**H-SUPPORT** ((R333)(5)(ii), N3, `%s`): onsets by b707’s route on b709’s ladder at the %s zeros its rule named, C1 %s; onsets '
         'computed %s, within 0.03 %s, beyond reach %s; the falsifier fired at %s: %s; %s beyond reach, consistent with the refutation and not '
         'counted as a firing, on the author’s ruling; the products (beta - 1/2) a* printed beside, POST HOC and not a test, no law fitted, '
         'their successor registered at %s (relay data/b723_support.txt).' % (
             K.C4_SUPPORT[:8], f['sp_zeros'], f['sp_c1'], f['sp_onsets'], f['sp_within'], f['sp_beyond'], ', '.join(fired) or 'none',
             f['sp_grade'], ', '.join(beyond) or 'none', K.NEXT_ACT), '',
         '**H-DIAL** ((R333)(5)(iii), `%s`): its build priced (%s), figures at F_c %s, %s; %s (relay data/b723_dial_price.txt).' % (
             K.C4_DIAL[:8], f['dl_price'], f['dl_figs'], f['dl_run'].lower(), f['dl_word'].lower()), '',
         '**The C2 closed form** ((R333)(6), N3, `%s`): written as a derivation in %s steps, the coefficient of log(Z_Q/2) read from log zeta_K '
         'at the bad prime powers (relay data/b723_c2_closed_form.txt); checked POST HOC, the form written knowing the banks, against %s rows '
         'over %s fields of b711-b722, %s reproduced, the planted e_p failing as wanted, negative b(n) at Omega(n) <= 3: %s, a bad ramified '
         'prime at every field: %s (relay data/b723_c2_check.txt); not compiled, the compile carried to where the author names it.' % (
             K.C5_RELAY[:8], f['cf_steps'].lower(), f['ck_rows'], f['ck_fields'], f['ck_rep'], f['ck_neg'], f['ck_ram']), '',
         '**The axiom step at the six pins** ((R333)(7), N1, `%s`): repaired on the %s branches by b722’s priced route, one commit each by the '
         'seat’s neutral identity, one run per kernel read by its id, %s runs of six at most -- %s; %s (its axiom step’s prints read there, '
         'the build carrying its sorry); halted %s; the axiom step at %s of %s '
         'pins; the lv sorry’s discharge %s, its choice put to the author at the root’s prompt; no kernel’s main touched and no tag cut (relay '
         'data/b723_axiom.txt).' % (
             ', '.join(c[:8] for c in K.C6_AXIOM), K.REBUILD_BRANCH, f['ax_runs'], _axiom_line(), f['ax_beside'], f['ax_halted'], f['ax_at'],
             f['ax_of'], f['ax_lv'].lower()), '',
         '**The ledger split** ((R333)(8)): its budget printed before any cut -- %s citation occurrences to move, %s of them in live tools, the '
         'split about %s h before a close of %s h -- and so %s with its price; %s, no ledger rewritten (relay data/b723_split_price.txt).' % (
             f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close'], f['sl_word'].lower(), f['sl_cut'].lower()), '',
         '**The research instruments reproduced** (`%s`): tools/research/reproduce.py over the entered instruments, %s rows: %d REPRODUCES, %s '
         'DIFFERS, %s NOT RUN (%s, each with its reason and price), the planted controls as wanted at %s of %s; I-76 read at b544’s pins '
         '(relay data/b723_reproduce.txt, data/b723_i76.txt).' % (
             K.C1_I76[:8], f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The author’s name and address** ((R332)(9), N5): the scan over every commit and bank of the act: PREVIOUS ADDRESS: %s, the '
         'author’s name %s, the previous name %s, over %s places, its four controls as wanted (relay data/b723_address_scan.txt).' % (
             f['addr'], f['name'], f['prev_name'], f['addr_places']), '',
         '**The touch read** (standing clauses v9): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b723_touch.txt). The act’s counter CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (f['claim'], f['close'], rep, tot,
                                                                                                    _runs3_line()), '',
         '**The standing arms**: the four figures at b723 -- %s, %s, %s, %s -- against b722’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b723_standing_figures.txt); standing arms added %d, G-READFIRST-DIFF-BANKED retired at v1.3.0.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins'], len(K.STANDING_ADDED)), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the hypotheses and the closed form meet at the banks -- H-SUPPORT reads onsets at '
         'heights its rule chose before any was computed, the closed form reads b(n) at fields whose banks it was written knowing, and each '
         'says which it is; the orders and the repeat classes meet at the record -- an order is open by the trail’s own latest line, a class '
         'repeats by the corrigendum’s tags, and neither is carried by hand.', '',
         '**Carried to:** %s, each from its bank: H-SUPPORT’s successor, registered there (relay data/b723_support.txt); H-DIAL’s build (relay '
         'data/b723_dial_price.txt); the C2 compile where the author names it (relay data/b723_c2_closed_form.txt); the lv sorry’s discharge '
         'on the author’s choice (relay data/b723_axiom.txt); the ledger split with its price (relay data/b723_split_price.txt); the instruments '
         'NOT RUN, each with its price; the draft held at v5.' % K.NEXT_ACT, '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b722():
    """b722's form over b722's objects, kept for the record and not called (Component 8)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 7, the Edit tool, over b723's objects; b722's composer over b722's objects kept below as _trail_text_b722,
    not called, and in git at b722's record tool); its open-orders line written from tools/standing/orders.py's output ((R333)(3)(i))."""
    import standing.orders as ORD
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rep, tot = _repeats()
    fired, beyond = _support_lists()
    op_line = ORD.open_line(ORD.report(ORD.read(ORD.trail('HEAD')), 'HEAD')[1])
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R333) ratified.** Its components as the ferry orders them (relay data/b723_ferry.txt), each read below from its bank.', '',
             '**Entered:** FINDINGS.md:%s (b722’s weight), :%s (the corrigendum), :%s (the entry); this record.' % (
                 f['weight'], f['corr_line'], fj.get('entry_line')), '',
             op_line, '',
             '**The orders by the tool:** %s of %s open at PLACE-papers main, %s closed, the line above from tools/standing/orders.py`s output; its '
             'controls %s of %s; the twenty met %s, acted %s, priced %s, discharged by reading %s, offered for retire %s (relay data/b723_orders.txt, '
             'data/b723_orders_twenty.txt).' % (
                 f['od_open'], f['od_n'], f['od_closed'], f['oc_wanted'], f['oc_cases'], f['tw_met'], f['tw_acted'], f['tw_priced'], f['tw_read'],
                 f['tw_retire']), '',
             '**The hypotheses:** registered at `%s`; H-ZETAK %s (relay data/b723_zetak.txt); H-SUPPORT %s at %s zeros, the falsifier fired at %s; '
             '%s beyond reach, not counted as a firing (relay data/b723_support_rule.txt, data/b723_support.txt); H-DIAL priced, %s, %s (relay data/b723_dial_price.txt).' % (
                 K.REG_COMMIT[:8], f['zk_grade'], f['sp_grade'], f['sp_zeros'], ', '.join(fired) or 'none', ', '.join(beyond) or 'none',
                 f['dl_run'].lower(), f['dl_word'].lower()), '',
             '**The C2 closed form:** written as a derivation; checked POST HOC, %s of %s rows reproduced; not compiled (relay '
             'data/b723_c2_closed_form.txt, data/b723_c2_check.txt).' % (f['ck_rep'], f['ck_rows']), '',
             '**The axiom step:** %s of %s pins; %s runs, each read by its id: %s; the lv sorry’s discharge %s, the author’s choice at the root’s '
             'prompt (relay data/b723_axiom.txt).' % (f['ax_at'], f['ax_of'], f['ax_runs'], _axiom_line(), f['ax_lv'].lower()), '',
             '**The ledger split:** %s with its price, %s (relay data/b723_split_price.txt).' % (f['sl_word'].lower(), f['sl_cut'].lower()), '',
             '**The instruments reproduced:** %d of %s, DIFFERS %s, NOT RUN %s (%s) (relay data/b723_reproduce.txt).' % (
                 f['rp_rep'], f['rp_rows'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b723_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v9.txt from `%s`; the touch read relay data/b723_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d; REPEAT %d of %d; %s.' % (K.STANDING_COMMIT[:8], f['claim'], f['close'], rep, tot, _runs3_line()), '',
             '**Act root:** b723 `%s` (previous `%s`, b722’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b723_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v9.txt; tools/standing/ at %s (relay data/b723_standing_v130.txt); the standing '
             'report tool (relay data/b723_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written and no tag cut; one commit each on the %s branches of %d wave 1 kernels by the seat’s '
              'neutral identity, each run read by its id; port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with its one tag %s; no '
              'lean process on this host.' % (
                  K.REBUILD_BRANCH, len(K.REBUILD_COMMITS), K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
              '**The mirror:** the export made after this root in the b670 form over the roster read from PLACE-papers main, its name in the '
              'closing (relay data/b723_closing.txt).', '',
              '**The standing arms:** the four figures %s, %s, %s, %s against b722’s %s, %s, %s, %s (relay data/b723_standing_figures.txt).' % (
                  f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                  f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
              '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
              '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
              '**Defects** (relay data/b723_defects.txt): %s.' % ('; '.join(_letters_now()) or 'none'), '',
              '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
              '**Next:** %s.' % K.next_line(), '']
    return NL.join(rows_)


def _trail_text_b722():
    """b722's trail record over b722's objects, kept for the record and not called (Component 8)."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: (R333)(7)`s by tools/b723_axiom.py dispatch, SIDE-frobenius`s and SIDE-kernel`s runs on their pushes; MEASURED off the command bank (each dispatch route run at a command`s head).'),
    ('runner runs read by their ids for the axiom step', 'AXRUNS', 'AXRUNS', 'runs', '### (R333)(7), N1: five, six at most, each read by its id; MEASURED off data/b723_axiom_rows.json against the worklist`s B723_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked; MEASURED off the twelve kernels` refs/heads/pin-b723*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act: b721`s rebuild-b721 branches carry (R333)(7)`s repair.'),
    ('rebuild-b721 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### (R333)(7): the six; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b721 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### each push read back; MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b721`s and b722`s beside this act`s five, one per kernel of (R333)(7); MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b723*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### beyond the pins, b721`s and b722`s; MEASURED off each branch against its pin.'),
    ('Lean files written by this act`s rebuild commits', 'RBLEANACT', 'RBLEANACT', 'files', '### none: print_targets.txt at four kernels, SIDE-kernel`s workflow; MEASURED off the five commits` files.'),
    ('Lean files written on any kernel`s main', 0, 0, 'files', '### N5: no main touched.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R333)(9): relay push-b722-closing, push-b722-preroot, push-b722-record; PLACE-papers push-b722-preroot, push-b722-record; each local, by name, after --merged listed it (data/b723_stepzero.txt :70-:76).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written by this act`s rebuild commits', 'RBWFACT', 'RBWFACT', 'files', '### (R333)(7) and the author`s word (7): SIDE-kernel`s build-module.yml in four places on its rebuild-b721 branch; MEASURED off the five commits` files.'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b721`s, b722`s and this act`s; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R333) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat from the act`s first PLACE-papers head (1553808a) to HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R333)(2): FINDINGS :11401.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R333)(2): one row, b722`s.'),
    ('the open orders generated from the record', 'ORDERS', 'ORDERS', 'orders', '### (R333)(3)(i): tools/standing/orders.py at PLACE-papers main; MEASURED off data/b723_orders.txt :282.'),
    ('open orders at PLACE-papers main', 'OPENORDERS', 'OPENORDERS', 'orders', '### MEASURED off data/b723_orders.txt :282, the trail`s line written from the tool`s output.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### the root answer`s (c): tools/research/reproduce.py; MEASURED off data/b723_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R333)(3)-(8): the orders, H-SUPPORT`s rule, H-ZETAK, H-SUPPORT, H-DIAL`s price, the C2 check, the axiom step, the split`s price, the reproduction, the address scan; MEASURED off the banks present.'),
    ('registrations committed alone', 'REGALONE', 'REGALONE', 'commits', '### (R333)(4), N2: data/b723_registrations.txt at 9ad26421, alone; MEASURED off the commit`s files.'),
    ('figure banks of a registered object first committed after the registrations', 'REGS', 'REGS', 'banks', '### (R333)(4)-(5), N2: H-SUPPORT`s rule, H-ZETAK, H-SUPPORT, H-DIAL`s price; MEASURED off the ancestry from 9ad26421.'),
    ('banks holding a figure at a registered object before its registration', 'PREREG', 'PREREG', 'banks', '### N2: none; MEASURED off each figure bank`s first commit against 9ad26421.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean statements of the C2 closed form written or compiled', 0, 0, 'statements', '### N3: written as a derivation and checked POST HOC, not compiled.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R333)(2): tools/standing/ to v1.3.0 -- the seven close tools folded, the pipe-free reader, the lock row, the seal`s list from SEALED; MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by retirement', 'RETIRED', 'RETIRED', 'arms', '### tools/standing/arms.py RETIRED, unchanged; MEASURED off it.'),
    ('arms left the arm list this act', 1, 1, 'arms', '### (R333)(2)(iv): G-READFIRST-DIFF-BANKED, at v1.3.0 (be821907); the run list 116.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 2, 2, 'banks', '### data/act_current.json at step zero and data/standing_clauses_v9.txt by a commit of its own (d9739558, (R333)(2)(v)); data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### the 2,560 MB hold read before each suite part, computation, push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### none: the run list 116.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R332)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b723_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### (R333)(1), N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs, the dispatches and the run reads ((R333)(7)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_COMMIT, c], capture_output=True).returncode == 0 \
            and c != K.REG_COMMIT

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### N2 (Component 7, the Edit tool): the figure banks of (4)-(5), each first committed after the registrations (9ad26421)
    fig_banks = [p for p in ('data/b723_support_rule.txt', 'data/b723_zetak.txt', 'data/b723_support.txt', 'data/b723_dial_price.txt')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([p for p in fig_banks if after_reg(first_add(p))]),
                    REGALONE=1 if alone(K.REG_COMMIT) else 0,
                    AXRUNS=jcount('b723_axiom_rows.json', lambda j: len([x for x in j if x.get('kind') == 'read'
                                                                          and (x.get('kernel'), int(x.get('run') or 0)) in set((k, int(r)) for k, r in K.B723_RUNS)])),
                    REPROWS=jcount('b723_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b723_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
                    ORDERS=tfirst('b723_orders.txt', r'\*\*AT HEAD: ORDERS (\d+) ;'),
                    OPENORDERS=tfirst('b723_orders.txt', r'\*\*AT HEAD: ORDERS \d+ ; OPEN (\d+) ;'),
                    RBWFACT=sum(1 for k_, c_ in K.REBUILD_COMMITS for f_ in _git('D:/' + k_, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split()
                                if f_.startswith('.github/workflows/')),
                    RBLEANACT=sum(1 for k_, c_ in K.REBUILD_COMMITS for f_ in _git('D:/' + k_, 'diff-tree', '--no-commit-id', '--name-only', '-r', c_).split()
                                  if f_.endswith('.lean')),
                    OTLINES=sum(int((_git(K.PP, 'show', '--numstat', '--format=', c_, '--', 'OPEN_TRAILS.md').split() or ['0'])[0])
                                for c_ in (K.C2_PP, K.C2_WEED_PP)),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('orders', 'support_rule', 'zetak', 'support', 'dial_price', 'c2_check', 'axiom', 'split_price', 'reproduce',
                                               'address_scan') if os.path.exists(os.path.join(ROOT, 'data', 'b723_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'RBWFACT', 'RBLEANACT', 'AXRUNS', 'REPROWS', 'ADDRESS', 'ORDERS', 'OPENORDERS',
              'REGALONE', 'OTLINES', 'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b723_registration_%s.txt -- b723, THE CHECKPOINT ACT: b722 AT ITS WEIGHT AND ITS CORRIGENDUM; THE CLOSE TOOLS "
                             "AT v1.3.0 AND THE REPEAT CLASSES; THE OPEN ORDERS GENERATED AND THE TWENTY READ; H-SUPPORT, H-ZETAK AND H-DIAL UNDER "
                             "THEIR REGISTRATIONS; THE C2 CLOSED FORM CHECKED POST HOC; THE AXIOM STEP AT THE SIX PINS; THE LEDGER SPLIT PRICED, "
                             "UNDER (R333)" % K.DATE),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b722's standing report by the fold (tools/standing/fold/report.tpl) and its lines rewritten at Component 7: b722's lines (the
axiom diagnosis, -31 and -55, the fourteen, the C2 statement, the instruments, the propagation read) read banks this act does not write, and
are not carried; the lines are b723's: the axiom step at the six pins, each run by its id (KERNEL), H-ZETAK and the C2 closed form checked
POST HOC, not compiled (CERTIFIED), H-SUPPORT under its rule, H-DIAL priced, the open orders generated and the instruments reproduced
(REGISTERED), and the ledger split and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b723's lines (Component 7, the Edit tool), each from the record tool's figures over b723's banks
    # ------------------------------------------------------------------ KERNEL: THE AXIOM STEP ((R333)(7)), each run read by its id
    # ------------------------------------------------------------------ (N1: no lean on the host, six dispatches at most)
    sk = seat('%s_axiom.txt' % ACT, '**THE AXIOM STEP AT ')
    keys['AXIOM'] = ('KERNEL -- THE AXIOM STEP AT THE SIX WAVE 1 PINS: %s of %s (%s repaired and run this act on rebuild-b721, %s, its axiom '
                     'step`s prints read, the build carrying its sorry); %s runs, '
                     'each read by its id: %s; halted %s; the lv sorry`s discharge %s; no main or tag touched. SOURCE %s.' % (
                         f['ax_at'], f['ax_of'], f['ax_rep'], f['ax_beside'], f['ax_runs'], REC._axiom_line(), f['ax_halted'], f['ax_lv'].lower(),
                         sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: H-ZETAK ((R333)(5)(i)); THE C2 CLOSED FORM ((R333)(6)),
    # ------------------------------------------------------------------ checked POST HOC, not compiled (N3)
    sz = seat('%s_zetak.txt' % ACT, '**H-ZETAK: ')
    keys['ZETAK'] = ('CERTIFIED -- H-ZETAK ON Q0`S TWO ONSET WINDOWS: C1 %s, C2 %s, C3 %s; rho0 %s, the band %s; THE HYPOTHESIS %s. SOURCE %s.' % (
        f['zk_c1'], f['zk_c2'], f['zk_c3'], f['zk_rho0'], f['zk_band'], f['zk_grade'], sz['text']))
    seats.append(sz)
    sw = seat('%s_c2_check.txt' % ACT, '**THE C2 CLOSED FORM, POST HOC: ')   # ### appended by the template after this section
    keys['C2'] = ('CERTIFIED -- THE C2 CLOSED FORM, CHECKED POST HOC: written as a derivation in %s steps; %s rows over %s fields, %s reproduced, '
                  'the planted e_p failing as wanted; not compiled. SOURCE %s.' % (
                      f['cf_steps'].lower(), f['ck_rows'], f['ck_fields'], f['ck_rep'], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: H-SUPPORT ((R333)(4)-(5)(ii)); H-DIAL ((R333)(5)(iii));
    # ------------------------------------------------------------------ THE OPEN ORDERS ((R333)(3)(i)); THE INSTRUMENTS REPRODUCED
    fired, beyond = REC._support_lists()
    ss = seat('%s_support.txt' % ACT, '**H-SUPPORT: ')
    keys['SUPPORT'] = ('REGISTERED -- H-SUPPORT AT Q0`S OFF-LINE ZEROS, its rule committed before any onset: %s zeros, onsets computed %s, within '
                       '0.03 %s, beyond reach %s (%s); the falsifier fired at %s; THE HYPOTHESIS %s. SOURCE %s.' % (
                           f['sp_zeros'], f['sp_onsets'], f['sp_within'], f['sp_beyond'], ', '.join(beyond) or 'none', ', '.join(fired) or 'none',
                           f['sp_grade'], ss['text']))
    seats.append(ss)
    sd = seat('%s_dial_price.txt' % ACT, '**H-DIAL: ')
    keys['DIAL'] = ('REGISTERED -- H-DIAL: its build priced (%s), figures at F_c %s, %s; %s. SOURCE %s.' % (
        f['dl_price'], f['dl_figs'], f['dl_run'].lower(), f['dl_word'].lower(), sd['text']))
    seats.append(sd)
    so = seat('%s_orders.txt' % ACT, '**AT HEAD: ORDERS ')
    keys['ORDERS'] = ('REGISTERED -- THE OPEN ORDERS GENERATED by tools/standing/orders.py at PLACE-papers main: %s orders, %s open, %s closed; '
                      'its controls %s of %s; the twenty met %s, discharged by reading %s, offered for retire %s. SOURCE %s.' % (
                          f['od_n'], f['od_open'], f['od_closed'], f['oc_wanted'], f['oc_cases'], f['tw_met'], f['tw_read'], f['tw_retire'], so['text']))
    seats.append(so)
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('REGISTERED -- THE RESEARCH INSTRUMENTS REPRODUCED (tools/research/reproduce.py): %s rows, REPRODUCES %s, DIFFERS %s, NOT RUN '
                     '%s (%s), the planted controls as wanted %s of %s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_rep'], f['rp_diff'], f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr'],
                         sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE LEDGER SPLIT ((R333)(8)); THE DRAFT
    sl = seat('%s_split_price.txt' % ACT, '**THE LEDGER SPLIT: ')
    keys['SPLIT'] = ('HELD -- THE LEDGER SPLIT: %s with its price, %s citation occurrences to move (%s in live tools), about %s h before a close '
                     'of %s h; %s. SOURCE %s.' % (
                         f['sl_word'].lower(), f['sl_occ'], f['sl_live'], f['sl_hours'], f['sl_close'], f['sl_cut'].lower(), sl['text']))
    seats.append(sl)
    sh = seat('%s_ferry.txt' % ACT, 'v5')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['AXIOM']), ('CERTIFIED', ['ZETAK', 'C2']), ('REGISTERED', ['SUPPORT', 'DIAL', 'ORDERS', 'REPRO']), ('HELD', ['SPLIT', 'HELD'])]
#⟪END⟫
#⟪OVERRIDE citation 47 47⟫
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b723 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
#⟪END⟫
#⟪OVERRIDE citation 146 146⟫
#⟪END⟫
#⟪OVERRIDE citation 151 151⟫
#⟪END⟫
#⟪OVERRIDE citation 153 153⟫
#⟪END⟫
#⟪OVERRIDE citation 155 155⟫
#⟪END⟫
