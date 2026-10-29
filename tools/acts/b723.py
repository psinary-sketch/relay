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
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
#⟪DEAD reg_gate ⟫
#⟪DEAD regspec ⟫
#⟪DEAD report ⟫
# Each "#⟪PENDING <tool> <names>⟫" line: names the act`s tool reads on routes carried from the act before that the act has
# still to write for itself; printed at every load; the act`s suite holds them empty at its seal.
#⟪PENDING checks C4_STMT,C5_PP,C5_RULE,C7_RELAY,PROPAGATION_LINE,REG_C3,REG_WALK⟫
#⟪PENDING citation ⟫
#⟪PENDING closing ⟫
#⟪PENDING record C4_STMT,C5_PP,C5_RULE,C7_RELAY,INSTRUMENTS_FIRST,REG_C3,REG_WALK⟫
#⟪PENDING reg_gate ⟫
#⟪PENDING regspec REG_C3,REG_WALK⟫
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
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) at the seal, every one the seat's; (b') the navigator's, beyond the single letters this floor reads
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b723_corrigendum.txt', 'data/b723_standing_v122.txt', 'data/b723_coeffs_controls.json', 'data/b723_coeffs.txt',
                  'data/b723_walk.txt', 'data/b723_c2_statement.txt', 'data/b723_c2_price.txt', 'data/b723_instruments.txt',
                  'data/b723_instrument_entries.json', 'data/b723_reproduce.txt', 'data/b723_reproduce.json', 'data/b723_propagation.txt',
                  'data/b723_propagation_landing.json', 'data/b723_axiom_diag.txt', 'data/b723_llm_line_drafts.txt',
                  'data/b723_address_scan.txt', 'data/b723_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: v7 binds the act whole, v8 from 0ff64911 ((R333)(8))
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
        # ### (R333)(3)-(12), Component 8, the Edit tool (b722's keys over b722's objects in git at b722's suite): b722's registrations at
        # ### HEAD against their commits; the computation banks of (3)-(5); the instruments, their entries and the reproduction run (6)-(7);
        # ### v8 and the propagation read (8); the address scan (9); the axiom diagnosis (10); the LLM-contribution line (12); the ancestry each
        # ### arm reads
#⟪END⟫
#⟪SECTION checks 6⟫
        reg_b722=(_s(blob(ROOT, '%s:%s' % (K.REG_C3, K.REGISTRATIONS))), _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS))),
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('reg_c3', K.REG_C3, K.C3_RELAY), ('reg_walk', K.REG_WALK, K.C3_RELAY), ('ctl_c3', K.C2_CTL, K.C3_RELAY),
                                 ('stmt_price', K.C4_STMT, K.C4_RELAY), ('rule_entries', K.C5_RULE, K.C5_RELAY), ('v8_prop', K.STANDING_COMMIT, K.C6_RELAY))),
        coeffs=rd('b723_coeffs.txt'), coeffs_ctl=jl('b723_coeffs_controls.json'), walk=rd('b723_walk.txt'),
        c2_stmt=rd('b723_c2_statement.txt'), c2_price=rd('b723_c2_price.txt'),
        instruments=rd('b723_instruments.txt'), entries=jl('b723_instrument_entries.json'), reproduce=rd('b723_reproduce.txt'),
        reproducej=jl('b723_reproduce.json'), instr_now=read(os.path.join(PP, K.INSTRUMENTS)),
        instr_pre=_s(blob(PP, '%s:%s' % (PRE['pp'], K.INSTRUMENTS))), instr_c5=_s(blob(PP, '%s:%s' % (K.C5_PP, K.INSTRUMENTS))),
        v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))), v7=read(os.path.join(ROOT, *K.DATA_STANDING_V7.split('/'))),
        propagation=rd('b723_propagation.txt'), prop_landing=jl('b723_propagation_landing.json'), propj=json.loads(rd('b723_propagation.json') or '[]'),
        address=rd('b723_address_scan.txt'), addr_live=_addr_live(), axiom_diag=rd('b723_axiom_diag.txt'), axiom_diagj=json.loads(rd('b723_axiom_diag.json') or '[]'),
        llm=rd('b723_llm_line_drafts.txt'), llmj=jl('b723_llm_line_drafts.json'),
        # ### the standing runner arms read b722's rebuild as banked (no dispatch this act, N1): its bank, its rows, each wave 1 kernel's
        # ### rebuild-b722 branch, main and tags
        rebuild=rd('b722_rebuild.txt'), rebuild_rows=json.loads(rd('b722_rebuild_rows.json') or '[]'), rebuild_state=_rebuild_state(),
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2ctl=_ct(ROOT, K.C2_CTL), c3=_ct(ROOT, K.C3_RELAY), c4stmt=_ct(ROOT, K.C4_STMT),
               c4=_ct(ROOT, K.C4_RELAY), c5rule=_ct(ROOT, K.C5_RULE), c5=_ct(ROOT, K.C5_RELAY), c5pp=_ct(PP, K.C5_PP), v8=_ct(ROOT, K.STANDING_COMMIT),
               c6=_ct(ROOT, K.C6_RELAY), c6pp=_ct(PP, K.C6_PP), c7=_ct(ROOT, K.C7_RELAY), reg=_ct(ROOT, K.REG_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS),
               actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   c2ctl=files_of(ROOT, K.C2_CTL), c3=files_of(ROOT, K.C3_RELAY), c4stmt=files_of(ROOT, K.C4_STMT), c4=files_of(ROOT, K.C4_RELAY),
                   c5rule=files_of(ROOT, K.C5_RULE), c5=files_of(ROOT, K.C5_RELAY), c5pp=files_of(PP, K.C5_PP), v8=files_of(ROOT, K.STANDING_COMMIT),
                   c6=files_of(ROOT, K.C6_RELAY), c6pp=files_of(PP, K.C6_PP), c7=files_of(ROOT, K.C7_RELAY),
#⟪END⟫
#⟪SECTION checks 10⟫
# ### b723's read-first bank's items by path (Component 8, the Edit tool: the carried needles were b722's items)
READFIRST_NEEDLES = ('relay data/b722_closing.txt |', 'relay data/b722_events.txt |', 'relay data/b722_defects.txt |',
                     'relay data/b722_registrations.txt |', 'relay data/b722_derivation.txt |', 'relay data/b722_offset_read.txt |',
                     'relay data/b722_offset_tier.txt |', 'relay data/b722_frozen_line.txt |', 'relay data/b722_rebuild.txt |',
                     'relay data/b718_count_read.txt |', 'PLACE-papers phase1.5/method/INSTRUMENTS.md |', 'relay data/b723_ferry.txt | whole |',
                     'relay data/b723_citation_check.txt | whole |', 'relay tools/b711_coeffs.py |', 'relay tools/e0_rule.py |',
                     'PLACE-papers day1/A_Place_to_Stand.md |', 'relay data/standing_clauses_v7.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R333)(1)-(2))', 'DISCRIMINANTS -31 AND -55 ((R333)(3))', 'FOURTEEN FIELDS ((R333)(4))', 'C2 STATEMENT ((R333)(5))',
                    'RESEARCH INSTRUMENTS ((R333)(6)-(7))', 'PROPAGATION READ (standing clauses v8 row (82), (R333)(8))', 'NAME AND ADDRESS ((R333)(9))',
                    'AXIOM STEP ((R333)(10))', 'LLM-CONTRIBUTION LINE ((R333)(12))', 'TOUCH READ (standing clauses v8)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (90 = 88 + 2; the two misses -- b711's route with C1-C3 (C3
    False), b722's closing :389-:430 beyond its end at :413 -- in the JSON bank's misses, each raised or entered before the component citing
    it); the bank written before the step-zero banks' commit and that commit before Component 1's (Component 8, the Edit tool: the carried
    78 = 75 + 3 were b722's own)."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 2 and int(m.group(1)) == 90 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 8, the Edit tool: the carried needles were b720's figures under b722's name)
    return landed(S, 0, ['b722 AT ITS WEIGHT', 'suite 112 of 116; root c6e2079dbe1c904f…', 'the closing’s 30c0b3c8', '27 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
# ### Component 8, before the lock, the Edit tool: the needles above were still b722's (defect (c')); b723's title from the record tool's _title
# ### as it prints over the banks (a scratch call writing nothing), cut at its objects
TITLE_NEEDLES = ('## the class-number-2 table at its fourteen remaining fields: 14 of 14 HELD, the value law at all eighteen by exhaustion over '
                 'Baker’s and Stark’s list', '; -31 and -55: n0 80 and 224, HELD', '; the C2 statement for Lean graded DERIVES and priced',
                 '; 68 research instruments entered as I-41 to I-108, 63 reproducing', '; the propagation read v8 and its 58 notes',
                 '; the axiom step diagnosed at five wave 1 pins')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r"(?: \(\([a-z][`'’]?\)(?:, \([a-z][`'’]?\))*\))? and the seat’s (\w+) defects? as lettered\.$", re.M)   # ### a primed letter read (defect (e`))
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R333)(2): the generated entry for b722's fifteen events and twenty-seven defects landed (its line in the bank, the title at that line
    through conv): the events by row (1)-(15), the defects by the one lettering ((a)-(z), (a`)), no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 5, CLOSE 37 over 42, REPEAT 24); the CLAIM items defects (d), (g), (i), (k) and (u); the
    three repairs at tools/standing/ v1.2.2 with their twelve cases; the corrigenda bank appended at row (42) and nothing before it changed; in
    Component 1's commit (Component 8, the Edit tool: the carried figures were b722's corrigendum's, of b720's record)."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 27 and len(items) == j.get('items') == 42 and j.get('row') == 42 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 42 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 5 and claims == ['d', 'g', 'i', 'k', 'u'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 24 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.2.2' and (j.get('repairs') or {}).get('cases') == 12 \
        and '  (42) ' in S['corrigenda'] and '  (43) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b723_rules.txt and data/b723_rules.txt, by form in (R333)(11)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    b723's does not exist (Component 8, the Edit tool: the carry's substitution named b723's twice and b722's rule (1))."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and '  (1) NOTHING EDITED AFTER THE LOCK GATE; A RESTORE IS AN EDIT.' in r1 and not re.search(r'(?m)^  \((?!1\))\d+\) ', r1) \
        and 'data/b723_rules.txt' in S['files']['c1'] and not os.path.exists(os.path.join(D, 'b723_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
# ### (b722's keys stood here until the Edit tool set b723's from tools/b723_report.py's dry print before the lock, defect (c'))
REPORT_KEYS = ('KERNEL -- THE AXIOM STEP AT FIVE WAVE 1 PINS', 'CERTIFIED -- -31 AND -55 UNDER e8c3dff4',
               'CERTIFIED -- THE FOURTEEN REMAINING CLASS-NUMBER-2 FIELDS', 'CERTIFIED -- THE C2 STATEMENT FOR LEAN',
               'REGISTERED -- THE RESEARCH INSTRUMENTS BY RULE', 'REGISTERED -- THE REPRODUCTION', 'HELD -- THE PROPAGATION READ',
#⟪END⟫
#⟪SECTION checks 24⟫
    """N1, N4, over b722's rebuild as banked (Component 8, the Edit tool: no rebuild this act, (R333)(10) reads b722's runs by their ids):
    every push, dispatch and read row of b722's with the host's free memory at or above the hold; per kernel its push before its run and its
    run before its read; b722's dispatches its worklist's cap, the refused one counted apart; and this act's command capture running no
    rebuild route at all (b722's tool or a b723 one) and no dispatch."""
#⟪END⟫
#⟪SECTION checks 25⟫
    route = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b72[12]_rebuild\.py (push|dispatch|push_run|plan)\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == K707.MAX_DISPATCHES and sum(1 for r in rows if r.get('kind') == 'dispatch_refused') == 1 \
        and bool(S['cmds']) and cmds == [] and K.MAX_DISPATCHES == 0
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-frobenius': '2'} and set(st['SIDE-frobenius']['author'].split(NL)) == {'b722 rebuild seat <b722-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS, OPEN_TRAILS and INSTRUMENTS.md), both ledgers changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
# ### (the tuple above stood at b722's headings with b723's paths until the Edit tool set it from _finding_text before the lock, defect (c'))
ENTRY_NEEDLES = ('**The corrigendum and the repairs**', '**-31 and -55**', '**The fourteen**', '**The C2 statement for Lean**',
                 '**The research instruments**', '**The propagation read**', '**The author’s name and address**',
                 '**The axiom step at five wave 1 pins**', '**The release sitting’s list**', '**The touch read**', '**The standing arms**',
                 '**The citation check**', '**The scores.**', '**Read in mutual light**', '**Carried to:**', '**Next.**',
                 'data/b723_corrigendum.txt', 'data/b723_coeffs.txt', 'data/b723_walk.txt', 'data/b723_c2_statement.txt', 'data/b723_c2_price.txt',
                 'data/b723_instruments.txt', 'data/b723_reproduce.txt', 'data/b723_propagation.txt', 'data/b723_address_scan.txt',
                 'data/b723_axiom_diag.txt', 'data/b723_llm_line_drafts.txt', 'data/b723_touch.txt', 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ()      # ### b723: no single-letter row the navigator's; (b'), (R333)(2)'s "at step zero" against the ferry's order, the navigator's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R333)(3)-(4), N2 (Component 8, the Edit tool, over b723's objects): every computation at -31 and -55 names e8c3dff4 as its registration
    (data/b723_coeffs.txt) and every computation at the fourteen names H-C2-WALK at 15cb6cc4 (data/b723_walk.txt), each registration's commit
    an ancestor of the computation's commit (C3_RELAY); b722's registrations at HEAD equal to their blob at e8c3dff4, and b716's to b722's at
    their commits; the controls (data/b723_coeffs_controls.json, with the tool) committed at C2_CTL before the figures' commit, neither figure
    bank in it, and each figure bank printing its controls before its first field; no registration bank of b723."""
    c, w = S['coeffs'] or '', S['walk'] or ''
    return 'e8c3dff4' in c and 'H-C3-31' in c and 'H-C4-55' in c and '15cb6cc4' in w and 'H-C2-WALK' in w \
        and all(S['anc'].get(k) is True for k in ('reg_c3', 'reg_walk', 'ctl_c3')) \
        and S['reg_b722'][0] is not None and S['reg_b722'][0] == S['reg_b722'][1] \
        and all(a is not None and a == b for a, b in S['reg_blobs'].values()) \
        and 'data/b723_coeffs_controls.json' in S['files']['c2ctl'] and not [x for x in S['files']['c2ctl'] if x in ('data/b723_coeffs.txt', 'data/b723_walk.txt')] \
        and _ctl_first(c, '### THE CONTROLS FIRST', '## D = -31') and _ctl_first(w, 'THE CONTROLS FIRST', '## D = -15') \
        and not os.path.exists(os.path.join(D, 'b723_registrations.txt'))
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R333)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 8, the Edit tool): tools/b723_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address read from history and held in memory -- its count 0, the author's name 0, its three controls as wanted; the
    bank's count the same; the address never printed (the tool refuses its own output where it would carry it)."""
    a = S['addr_live'] or {}
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'CONTROLS 3 OF 3 AS WANTED' in (a.get('out') or '') \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ;', S['address'] or '') is not None
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R333)(3)-(4), N3 (Component 8, the Edit tool, over b723's objects): -31 and -55 and the fourteen, each row read on its own clauses --
    the controls json all as wanted (C1 exact, C2 reproducing b711's -23, C3 the planted coefficient failing); -31 and -55 each a row HELD or
    REFUTED with its prime clause, the foot equal to the rows; the fourteen each a row, the foot's counts equal to the rows', the control row
    -15 beside them; the walk's grade at its end naming the exhaustion over the list cited and Python, not compiled; both banks in C3_RELAY."""
    c, w = S['coeffs'] or '', S['walk'] or ''
    cc = S['coeffs_ctl'] or {}
    r34 = re.findall(r'(?m)^  (H-C[34]-\d+)\s+(-\d+)\s+(HELD|REFUTED)\s+computed .* the prime clause: ', c)
    rw = re.findall(r'(?m)^  (?:H-C2-WALK|CONTROL -15)\s+(-\d+)\s+()(HELD|REFUTED|NOT SCORABLE)\s+computed ', w)
    fw = re.search(r'\*\*H-C2-WALK: (\d+) OF 14 HELD, REFUTED (\d+), NOT SCORABLE (\d+) ; THE CONTROL ROW -15 (HELD|REFUTED) ;', w)
    fc = re.search(r'\*\*n0\(-31\) = \d+, b = \S+ ; n0\(-55\) = \d+, b = \S+ ; H-C3-31 (HELD|REFUTED) ; H-C4-55 (HELD|REFUTED) ;', c)
    g = w[w.rfind('### THE GRADE: '):]
    rows14 = [r for r in rw if int(r[0]) in set(K.WALK_DISCRIMINANTS)]
    return cc.get('ok') is True and cc.get('c1') is True and len(r34) == 2 and bool(fc) and [x[2] for x in r34] == [fc.group(1), fc.group(2)] \
        and bool(fw) and len(rows14) == 14 and sum(1 for r in rows14 if r[2] == 'HELD') == int(fw.group(1)) \
        and sum(1 for r in rows14 if r[2] == 'REFUTED') == int(fw.group(2)) and [r[2] for r in rw if r[0] == '-15'] == [fw.group(4)] \
        and 'by exhaustion' in g and 'cited and not compiled' in g and 'in Python, not compiled' in g \
        and all(x in S['files']['c3'] for x in ('data/b723_coeffs.txt', 'data/b723_walk.txt'))
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R333)(5), N3 (Component 8, the Edit tool, over b723's objects): the C2 statement's text committed alone (C4_STMT, the statement bank and
    its tool) before its grade and price (C4_RELAY), the text at HEAD equal to its blob there; THE GRADE read by E0 the foot's grade (E0's
    printed reading), the scope beside the statement naming Baker and Stark, cited; the statement true as written in Python at 18 of 18; the
    price per field at 18 rows by both routes, the foot at the bank's end; no Lean file and no dispatch (the price a count)."""
    p, st = S['c2_price'] or '', S['c2_stmt'] or ''
    g = re.search(r'(?m)^  THE GRADE: (\w+) -- ', p)
    f = re.search(r'\*\*THE C2 STATEMENT: E0 (\w+) ; SCOPE BESIDE IT \(Baker 1971, Stark 1975, cited\) ; AS WRITTEN, TRUE IN PYTHON AT (\d+) OF (\d+) ;', p)
    rows = re.findall(r'(?m)^  -\d+\s+\d+\s+\| .* \| .*\s(YES|NO)$', p)
    last = [l for l in p.split(NL) if l.strip()][-1:] or ['']
    return bool(st) and _own(S['files']['c4stmt']) == ['data/b723_c2_statement.txt', 'tools/b723_c2.py'] and S['anc'].get('stmt_price') is True \
        and _s(blob(ROOT, '%s:data/b723_c2_statement.txt' % K.C4_STMT)) == _s(blob(ROOT, 'HEAD:data/b723_c2_statement.txt')) \
        and bool(g) and bool(f) and g.group(1) == f.group(1) and f.group(2) == f.group(3) == '18' and len(rows) == 18 \
        and last[0].startswith('### ### **THE C2 STATEMENT') and 'data/b723_c2_price.txt' in S['files']['c4'] \
        and 'NOTHING RUNS LEAN, NOTHING IS DISPATCHED' in p
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R333)(6), N2 (the name the frozen run list carries; Component 8, the Edit tool, over b723's instruments): the rule printed before any
    tool is named (its line before the first act-numbered tool's); the output's count in the foot equal to the entries' (I-41 on, in order);
    INSTRUMENTS.md at PLACE-papers' act base a byte prefix of the file at the entries' commit C5_PP and the file now equal to it, I-41 the first
    new head, every entry head I-41 to I-<40+m> once, each with the six fields of b618's form; each validated case's needle at its bank and
    line; the entries composed after the rule's commit (C5_RULE an ancestor of C5_RELAY)."""
    it, E = S['instruments'] or '', (S['entries'] or {}).get('entries') or []
    m = re.search(r'\*\*THE RULE`S OUTPUT: (\d+) INSTRUMENTS \((\d+) NEW, TO BE ENTERED AS I-41 TO I-(\d+)\)', it)
    L = it.split(NL)
    rule_at = next((i for i, l in enumerate(L) if l.startswith('THE RULE ((R333)(6)), printed before any tool is named')), None)
    tool_at = next((i for i, l in enumerate(L) if re.search(r'\bb\d{3}_[a-z]\w*', l)), None)
    pre, c5, now = S['instr_pre'] or '', S['instr_c5'] or '', S['instr_now'] or ''
    new = c5[len(pre):] if c5.startswith(pre) else ''
    heads = re.findall(r'(?m)^## (I-\d+) — ', new)
    n = int(m.group(1)) if m else -1
    want = ['I-%d' % i for i in range(41, 41 + n)]
    fields = all(new.count(w) >= n for w in ('**Reads.**', '**Decides.**', '**Controls.**', '**Validated case.**', '**Range limits.**', '**Entered.**'))
    needles = []
    for x in E:
        v = x.get('validated') or {}
        bl = (rd(os.path.basename(v.get('bank') or '')) or '').split(NL)
        needles.append(0 < (v.get('line') or 0) <= len(bl) and (v.get('needle') or '\0') in bl[v['line'] - 1])
    return bool(m) and rule_at is not None and tool_at is not None and rule_at < tool_at and [x.get('id') for x in E] == want \
        and int(m.group(3)) == 40 + n and bool(pre) and c5.startswith(pre) and now == c5 and heads == want and fields \
        and len(needles) == n and all(needles) and S['anc'].get('rule_entries') is True and S['files']['c5pp'] == [K.INSTRUMENTS]
#⟪END⟫
#⟪SECTION checks 36⟫
    """(R333)(8), the name the frozen run list carries (Component 8, the Edit tool, over b723's v8 and its propagation read): v8 at VERSION 8,
    v7's lines :10-:195 in it byte for byte, row (82) the quotation of the ferry's :23, its commit (STANDING_COMMIT) the one file and an
    ancestor of the propagation read's; the read's hits equal to the foot's count, UNREAD 0, its notes (each READS WRONG and DATED hit) the
    foot's figure; the notes landed in one block at FINDINGS K.PROPAGATION_LINE, the line its head, in Component 6's PLACE-papers commit alone."""
    v8, v7, p = S['v8'] or '', S['v7'] or '', S['propagation'] or ''
    L8, L7 = v8.split(NL), v7.split(NL)
    row82 = re.search(r'"(When the record corrects a statement, [^"]*)"', S['ferry'] or '')
    J = S['propj'] or []
    f = re.search(r'HITS (\d+) ; .* NOTES TO WRITE (\d+) ; UNREAD (\d+) ;', _verdict(p))
    land = ((S['prop_landing'] or {}).get('lines') or [{}])[0]
    return 'VERSION: 8' in L8[:4] and len(L8) > 195 and L8[9:195] == L7[9:195] and bool(row82) and ('      ' + row82.group(1)) in L8 \
        and 'ROWS 82 ;' in _verdict(v8) and S['files']['v8'] == [K.DATA_STANDING_V8] and S['anc'].get('v8_prop') is True \
        and _s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V8))) == v8 and bool(f) and int(f.group(1)) == len(J) and f.group(3) == '0' \
        and int(f.group(2)) == sum(1 for x in J if x.get('grade') in ('READS WRONG', 'DATED')) \
        and str(land.get('line')) == str(K.PROPAGATION_LINE) and fline(S, K.PROPAGATION_LINE) == land.get('head') and S['files']['c6pp'] == ['FINDINGS.md'] \
        and all(x in S['files']['c6'] for x in ('data/b723_propagation.txt', 'data/b723_propagation.json', 'data/b723_propagation_landing.json'))
#⟪END⟫
#⟪SECTION checks 37⟫
    """(R333)(7): no arm retired this act, b722's run list of 116 binds with the one arm the ruling adds -- tools/standing/arms.py byte-equal
    to its blob at the act's base, its RETIRED as b722 left it and arm_tags.json's retired record equal to it, none a guard; this suite's run
    list 117 arms, without them, G-RESEARCH-REPRODUCES among them once (Component 8, the Edit tool: 116 before)."""
#⟪END⟫
#⟪SECTION checks 38⟫
    names = [a[0] for a in ARMS]
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 117 \
        and K.STANDING_ADDED == ('G-RESEARCH-REPRODUCES',) and names.count('G-RESEARCH-REPRODUCES') == 1
#⟪END⟫
#⟪SECTION checks 40⟫
    """(R333)(10) and (12), the name the frozen run list carries (Component 8, the Edit tool): the axiom step diagnosed at the five pins by
    b722's runs read by their ids (the bank's rows the worklist's AXIOM_RUNS, in order, each classed, each priced), the foot's classes summing
    to five and NOTHING COMMITTED, PUSHED OR DISPATCHED; the LLM-contribution line's drafts -- the controls as wanted, the foot's SAME, DIFFERS
    and ABSENT the rows' and DRAFTS their DIFFERS and ABSENT, NOTHING EDITED (the monograph at HEAD its blob at the act's base); both banks in
    Component 7's commit."""
    A, lj, ft = S['axiom_diagj'] or [], S['llmj'] or {}, _verdict(S['axiom_diag'])
    runs = [(x.get('kernel'), int(x.get('run') or 0)) for x in A]
    cl = re.findall(r'(?:TARGETS ABSENT AT THE PIN|BUILD TARGET NOT COVERING THE AXIOM FILE`S IMPORTS|STEP NOT THE PIN`S OWN|OTHER) (\d+)', ft)
    rows = lj.get('rows') or []
    g = dict((w, sum(1 for r in rows if r.get('grade') == w)) for w in ('SAME', 'DIFFERS', 'ABSENT'))
    lf = re.search(r': SAME (\d+) ; DIFFERS (\d+) ; ABSENT (\d+) ; DRAFTS (\d+) ; NOTHING EDITED ;', _verdict(S['llm']))
    mono = 'day1/A_Place_to_Stand.md'
    return runs == [(k, int(r)) for k, r in K.AXIOM_RUNS] and all(x.get('class') and x.get('price') for x in A) and len(cl) == 4 \
        and sum(int(c) for c in cl) == len(A) == 5 and 'NOTHING COMMITTED, PUSHED OR DISPATCHED' in ft \
        and all(c[2] == c[3] for c in (lj.get('controls') or [])) and len(lj.get('controls') or []) == 3 and bool(lf) \
        and [int(x) for x in lf.groups()] == [g['SAME'], g['DIFFERS'], g['ABSENT'], g['DIFFERS'] + g['ABSENT']] \
        and _s(blob(PP, 'HEAD:' + mono)) == _s(blob(PP, '%s:%s' % (PRE['pp'], mono))) \
        and all(x in S['files']['c7'] for x in ('data/b723_axiom_diag.txt', 'data/b723_axiom_diag.json', 'data/b723_llm_line_drafts.txt', 'data/b723_llm_line_drafts.json'))


def research_reproduces_ok(S):
    """(R333)(7), the standing arm G-RESEARCH-REPRODUCES (Component 8, the Edit tool): tools/research/reproduce.py's run banked -- one row per
    instrument, the rows' ids the entries' (I-41 on, in order); each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong figure
    graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the json's
    counts and the bank's foot the rows'; the tool at HEAD its blob at the run's commit (C5_RELAY) and the working tree's."""
    j = S['reproducej'] or {}
    R = j.get('rows') or []
    ids = [x.get('id') for x in ((S['entries'] or {}).get('entries') or [])]
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
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (K.C5_RELAY, tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')
#⟪END⟫
#⟪SECTION checks 41⟫
    """standing clauses v8 ((R333)(8): "The touch read of v8 is banked before the root"), N4: the touch read banked as data/b723_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
    # ### (R333)(7)'s arm, G-RESEARCH-REPRODUCES, is new and the file is outside the (W) list: it stands untagged beside the act shift and the
    # ### closing's tally counts it apart (Component 8, the Edit tool)
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R333-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED']) and tags.get('G-R329-ENTERED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    # ### Component 8, the Edit tool: b723's ferry names no "standing clauses v<N>" outside a file name (it names data/standing_clauses_v8.txt
    # ### and v8 by row), so the carried `7 in named` read nothing; v7 is read by its bytes below and v8 by G-SURGERY-CARRIED
    return 'RULING (R333) END' in f and f.rstrip().endswith(K.TAIL) and have \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from 30c0b3c8',
#⟪END⟫
#⟪SECTION checks 46⟫
    # ### (R333)(7): the standing arm the ruling adds, the run list 117 (Component 8, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R333)(7): tools/research/reproduce.py`s run -- one row per instrument I-41 on, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool sealed at its run`s commit',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 90 = 88 OK + 2 misses (each raised or entered before the component citing it), the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b722-closing (30c0b3c8)', 'push-b722-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the fourteen at 14 of 14 HELD and the value law at all eighteen by exhaustion over the cited list; -31 and -55 at n0 80 and 224, HELD; the C2 statement graded DERIVES and priced; 68 instruments, 63 reproducing; the propagation read v8 and its 58 notes; the axiom step diagnosed at five pins), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R333)(2): the generated corrigendum for b722`s record, landed at FINDINGS :11218: its fifteen events and twenty-seven defects, 42 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 5 CLOSE 37, REPEAT 24; v1.2.2`s repairs, 12 cases; the corrigenda bank appended at row (42)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); this act`s rules bank carrying (R333)(1)`s row alone, in Component 1`s commit; no b723 rules bank',
#⟪END⟫
#⟪SECTION checks 52⟫
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b723's objects (Component 8, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R333)(3)-(4), N2: every computation at -31 and -55 naming e8c3dff4 and every computation at the fourteen naming H-C2-WALK at 15cb6cc4, each an ancestor of the figures` commit 6afe03bf; b722`s registrations at HEAD their blob at e8c3dff4; the controls committed at 417ced62 before the figures, each bank printing its controls before its first field',
     lambda S: registrations_first_ok(S), lambda S: put(S, 'coeffs', (S['coeffs'] or '').replace('e8c3dff4', '00000000'))),
    ('G-PREDICTION-FIRST', '(R333)(9)(i), N5, the scan arm: tools/b723_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, three controls as wanted, the bank`s count the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R333)(3)-(4), N3: -31 and -55 each HELD or REFUTED with its prime clause, the foot the rows; the fourteen each a row, the foot`s counts the rows`, the control row -15 beside them; the controls json all as wanted; the walk`s grade at its end naming the exhaustion over the cited list in Python, not compiled',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'walk', (S['walk'] or '').replace('by exhaustion', 'by sampling'))),
    ('G-DERIVATION-GRADED', '(R333)(5), N3: the C2 statement committed with its tool at 50397f61 before its grade and price at 14190fe4, the text at HEAD its blob there; THE GRADE E0`s printed reading and the foot`s; the scope beside it citing Baker and Stark; true as written in Python at 18 of 18, priced at 18 rows; nothing runs Lean, nothing dispatched',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'c2_price', (S['c2_price'] or '').replace('  THE GRADE: ', '  A GRADE: '))),
    ('G-OFFSET-POST-HOC', '(R333)(6), N2: the instruments` rule printed before any tool is named (f52ea31b, an ancestor of 3e4415fb); the output`s count the entries` I-41 on; INSTRUMENTS.md at 2b194142 a byte prefix of the file at 4af48e1e and the file now equal to it, each head once with b618`s six fields, each validated case at its bank`s line',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'instr_now', (S['instr_now'] or '') + NL + '## I-999 — A PLANTED ENTRY')),
    ('G-SURGERY-CARRIED', '(R333)(8): v8 at VERSION 8, v7`s :10-:195 byte for byte and row (82) the ferry`s :23, alone at 0ff64911 before the propagation read; the read`s hits the foot`s 431, UNREAD 0, its notes each READS WRONG and DATED hit; landed in one block at FINDINGS :11284 in f127660c alone',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'propj', (S['propj'] or [])[:-1])),
    ('G-ARMS-RETIRED', '(R333)(7): no arm retired this act, b722`s run list of 116 binds with G-RESEARCH-REPRODUCES added -- tools/standing/arms.py byte-equal at 30c0b3c8, its RETIRED equal to arm_tags.json`s retired record, none a guard; this suite`s run list 117 arms without them',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', '(R333)(10) and (12): the axiom step diagnosed at the five pins by b722`s runs read by their ids, each classed and priced, NOTHING COMMITTED, PUSHED OR DISPATCHED; the LLM-contribution line`s controls as wanted, its SAME, DIFFERS, ABSENT and DRAFTS the rows`, the monograph unedited; both in 93f20fce',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'axiom_diag', (S['axiom_diag'] or '').replace('NOTHING COMMITTED, PUSHED OR DISPATCHED', 'A RUN DISPATCHED'))),
    ('G-DIFFERS-ERRATA', '(R333)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal at 2b194142, no b723 differs or errata bank, the worklist naming none; the weight line and the corrigendum in Component 1`s PLACE-papers commit cbb3b47f, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v8 ((R333)(8)), N4: data/b723_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R333-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and (R333)(7)`s new arm, untagged; the claim arms thirty-eight; the file byte-equal at 30c0b3c8 (outside the (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', 'N1, b722`s rebuild as banked (no rebuild this act): one run per wave 1 kernel, six, each read once with its build exit; the head`s figures equal to its rows; the one sorry printed by its axiom line and graded builds and is not complete; SIDE-frobenius`s refused dispatch, its halt with its control, and its push run on the author`s two lines',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', 'N1, N4: b722`s rebuild`s order and hold as banked -- free memory at or above 2,560 MB at every push, dispatch and read; per kernel push before run before read; b722`s cap, the refused one apart; this act`s capture running no rebuild route and no dispatch',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each wave 1 kernel`s rebuild-b722, kept, at its pin (the tagged commit, its one tag) or, SIDE-frobenius alone, two commits beyond it by b722`s neutral identity, off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the two ledgers and INSTRUMENTS.md alone ((R333)(6)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b722`s trail record on OPEN_TRAILS (:16264) and its root in the chain', lambda S: '### b722 — lane two, act one hundred and forty-eight, the table act under (R332)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and INSTRUMENTS.md): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b722`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches this act %d (N1: none; (R333)(10) reads b722`s runs by their ids; -1 the command bank not yet written)' % (
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
tool) are the corrigendum and v1.2.2's repairs, -31 and -55, the fourteen fields, the C2 statement, the research instruments and their
reproduction, the propagation read, the name and address scan, the axiom step, the LLM-contribution line, the touch read of v8 and the
standing arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R333)'s counter line beneath the title
and the claim arms' figure beside the suite's in the commits section; the author's word after the seal printed from its bank (tools/act_close.py
author_words_section, v5 row (74)); the carried items of (R333)(13) for b723. The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. No kernel written this act: the rebuild-b722 branches of the six wave 1 kernels kept as b722 left them.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b723 ((R333)(13)); b722's item (g), the federation pin closed at b722, not carried (Component 8, the Edit tool:
    the pin closed at b722 and nothing of it is this act's)."""
    return CARRIED_FIXED
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b723 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FORTY-NINE, THE INSTRUMENTS ACT: b722 AT ITS WEIGHT AND ITS '
              'CORRIGENDUM; -31 AND -55 COMPUTED UNDER THEIR REGISTRATION; THE FOURTEEN FIELDS WALKED; THE C2 STATEMENT GRADED AND PRICED; THE '
              'RESEARCH INSTRUMENTS ENTERED AND REPRODUCED; THE PROPAGATION READ UNDER v8; THE AXIOM STEP DIAGNOSED AT FIVE PINS, UNDER (R333).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 8, the Edit tool; b722's sections over b722's objects -- the C2 halt, the table
    over h = 3, 4, 5, the offset, the surgery, the frozen line -- not carried). A row of two reads its bank's verdict line by vtail; a row of
    three reads the line its pattern names (a bank written by the Write tool carries no verdict line's form)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('v1.2.2`s three repairs, each controlled on b722`s banks', 'b723_standing_v122.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE DISCRIMINANTS -31 AND -55 ((R333)(3))', [
                ('n0 and b at each under e8c3dff4, the controls first, each HELD or REFUTED with its prime clause', 'b723_coeffs.txt')]),
            ('THE FOURTEEN FIELDS ((R333)(4))', [
                ('the fourteen remaining class-number-2 fields under H-C2-WALK (15cb6cc4), the control row -15, the grade at the end', 'b723_walk.txt')]),
            ('THE C2 STATEMENT ((R333)(5))', [
                ('the statement for Lean graded by E0, true as written in Python, priced per field', 'b723_c2_price.txt')]),
            ('THE RESEARCH INSTRUMENTS ((R333)(6)-(7))', [
                ('the rule printed before any tool is named, its output entered as I-41 on', 'b723_instruments.txt'),
                ('tools/research/reproduce.py, one row per instrument, a planted wrong figure per run row', 'b723_reproduce.txt')]),
            ('THE PROPAGATION READ (standing clauses v8 row (82), (R333)(8))', [
                ('every statement naming the three corrected objects read, a dated note beside each that reads wrong', 'b723_propagation.txt')]),
            ('THE NAME AND ADDRESS ((R333)(9))', [
                ('the scan over every commit and bank of the act, the previous address held in memory, its count alone', 'b723_address_scan.txt')]),
            ('THE AXIOM STEP ((R333)(10))', [
                ('the five wave 1 pins` axiom steps diagnosed from b722`s runs by their ids, each priced, nothing dispatched', 'b723_axiom_diag.txt')]),
            ('THE LLM-CONTRIBUTION LINE ((R333)(12))', [
                ('the monograph`s line against the wave 1 papers and kernel READMEs, drafts in the relay alone', 'b723_llm_line_drafts.txt')]),
            ('THE TOUCH READ (standing clauses v8)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: none -- no kernel`s main touched, no tag cut, no Lean file written in any kernel (N5) ; the rebuild-b722 branches',
    '    of the six wave 1 kernels KEPT as b722 left them, for b723 ((R333)(11)) ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved,',
    '    the challenge branch challenge-b720-h2-sign-iff-rh standing ; the pin-b718-de5ce8a9 branches left as banked ; port-b707 of',
    '    SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main and its deposit v0.10.0',
    '    unmoved ; SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host and no runner',
    '    dispatched, the axiom step diagnosed from b722`s five runs read by their ids ((R333)(10)) ; free memory read before each suite part',
    '    and each computation ; the push-b722-* branches of relay and PLACE-papers deleted at step zero by name after --merged listed them,',
    '    one per command and each its own message ; nothing vendored ; no worktree made or removed ; b628`s local intake bank, the',
    '    navigator`s export, b671`s uncompressed points file and the earlier acts` units files untracked ; N2: every computation at -31 and',
    '    -55 naming e8c3dff4 and every computation at the fourteen naming H-C2-WALK at 15cb6cc4, the controls committed before the figures,',
    '    the instruments` rule printed before any instrument was named, the propagation names before each search ; (R333)(9): no new',
    '    occurrence of the author`s name or address in anything the act wrote, committed or pushed (relay data/b723_address_scan.txt), the',
    '    commits under the GitHub login and its noreply address ; no identifier of the author in any outbound request header, URL, input or',
    '    payload, or in any workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes) the act`s',
    '    outbound calls ; the deposit route untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS (the weight',
    '    line, the corrigendum, the propagation notes, the entry) and OPEN_TRAILS (the trail) appended, and INSTRUMENTS.md appended with I-41',
    '    on ((R333)(6)) ; no paper cut, moved or renamed ; no ERRATA, FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt',
    '    and the corrigenda bank appended ; data/act_current.json written at step zero ; data/arm_tags.json unedited ; tools/standing/ at',
    '    v1.2.2 by (R333)(2) ; data/standing_clauses_v8.txt by a commit of its own ((R333)(8)) ; tools/research/reproduce.py sealed with the',
    '    act`s tools ((R333)(7)) ; the hook in D:/.claude/settings.json unedited ; the per-act tools of b698-b722 unedited ; the mirror zip',
    '    written outside every repository over the roster read from PLACE-papers main, the builder`s state file tools/mirror_prevbuild.json',
    '    written at the build and named in (W) ; nothing of TECHNE or any patent written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R333)(13)**: ' + WL.NEXT + '.',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        W-ORD-E0-MET-CLASSK; W-ORD-README-FIGURE-SCOPE. None annotated this act.',
    '    (c) For b723, each from its bank: the axiom step`s routes as priced (relay data/b723_axiom_diag.txt); the C2 compile`s route as',
    '        priced (relay data/b723_c2_price.txt); the reproduction`s DIFFERS and NOT RUN rows (relay data/b723_reproduce.txt); the',
    '        LLM-contribution line`s drafts for the release sitting (relay data/b723_llm_line_drafts.txt); the report tool outside the sealed',
    '        list; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file (declared in their tools` heads), the zero-byte `=` and records.json at relay`s root',
    '        (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); challenge-b720-h2-sign-iff-rh of',
    '        SIDE-explicit-formula; the pin-b718-de5ce8a9 branches as banked; the rebuild-b722 branches of the six wave 1 kernels (b723`s).',
    '    (g) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written, the rebuild-b722 branches of the six wave 1 kernels kept as b722 left them, no main moved, no tag cut ; '
          'SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b723: the standing repairs are v1.2.2's ((R333)(2), relay data/b723_standing_v122.txt, read in the corrigendum section); the
    # ### carry's diffs here
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel written this act, the %s branches of the six wave 1 kernels kept as b722 pushed them ((R333)(11)); SIDE-lv-conservation`s main '
          'untouched, port-b707 at b712`s tip %s, its checkout at main for this read)' % (len(ks), K.JOIN_NEW_TIP[:8], K.REBUILD_BRANCH, K.PORT_NEW_TIP[:8]))
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
    b722's form over b722's objects in git at b722's record tool): the corrigendum's foot and v1.2.2's controls; -31 and -55 under e8c3dff4;
    the fourteen under H-C2-WALK and the walk's grade; the C2 statement's E0 grade and its price; the instruments' rule and the reproduction
    run; the propagation read and its landing; the axiom step's diagnosis; the LLM-contribution line; the address scan; each by its own lines
    through _bfig, which refuses where a bank does not carry its figure; the counter from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    v2 = _bfig('%s_standing_v122.txt' % ACT, r'\*\*v1\.2\.2: CASES (\d+), AS WANTED (\d+) ;', 'v1.2.2`s controls')
    cf = _bfig('%s_coeffs.txt' % ACT, r'\*\*n0\(-31\) = (\d+), b = (-?[\d/]+) ; n0\(-55\) = (\d+), b = (-?[\d/]+) ; H-C3-31 (HELD|REFUTED) ; '
               r'H-C4-55 (HELD|REFUTED) ;', 'the coefficients` foot')
    cc = jl('%s_coeffs_controls.json' % ACT)
    wk = _bfig('%s_walk.txt' % ACT, r'\*\*H-C2-WALK: (\d+) OF 14 HELD, REFUTED (\d+), NOT SCORABLE (\d+) ; THE CONTROL ROW -15 (HELD|REFUTED) ;', 'the walk`s foot')
    wg, = _bfig('%s_walk.txt' % ACT, r'(?m)^### THE GRADE: (the value law .*)$', 'the walk`s grade')
    e0, = _bfig('%s_c2_price.txt' % ACT, r'(?m)^  THE GRADE: (\w+) -- ', 'the C2 statement`s E0 grade')
    cp = _bfig('%s_c2_price.txt' % ACT, r'\*\*THE C2 STATEMENT: E0 (\w+) ; SCOPE BESIDE IT \(([^)]*)\) ; AS WRITTEN, TRUE IN PYTHON AT (\d+) OF (\d+) ; '
               r'PRICED: \(A\) decide as written (\S+) TO (\S+) LATTICE POINTS, UNMEASURED IN LEAN, \(B\) THE CERTIFICATE ROUTE UNDER (\S+) AT (\d+) OF '
               r'(\d+), TWO LEMMAS NAMED ;', 'the C2 price`s foot')
    ins = _bfig('%s_instruments.txt' % ACT, r'\*\*THE RULE`S OUTPUT: (\d+) INSTRUMENTS \((\d+) NEW, TO BE ENTERED AS I-(\d+) TO I-(\d+)\) ; POPULATION (\d+), '
                r'REUSED (\d+), \(S1\) (\d+), \(S2\) (\d+) ; THE NAVIGATOR`S (\d+): (\d+) IN THE OUTPUT ; UNREAD BY HAND (\d+) ;', 'the instruments` foot')
    rp = _bfig('%s_reproduce.txt' % ACT, r'\*\*ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;',
               'the reproduction run`s foot')
    rpj = jl('%s_reproduce.json' % ACT).get('rows') or []
    pg = _bfig('%s_propagation.txt' % ACT, r'\*\*THE PROPAGATION READ: OBJECTS (\d+) ; HITS (\d+) ; COPY (\d+) ; DATED (\d+) ; NOT THIS OBJECT (\d+) ; '
               r'READS RIGHT (\d+) ; READS WRONG (\d+) ; NOTES TO WRITE (\d+) ; UNREAD (\d+) ;', 'the propagation read`s foot')
    pl = (jl('%s_propagation_landing.json' % ACT).get('lines') or [{}])[0].get('line')
    ax = _bfig('%s_axiom_diag.txt' % ACT, r'\*\*THE AXIOM STEP AT FIVE PINS: TARGETS ABSENT AT THE PIN (\d+) ; BUILD TARGET NOT COVERING THE AXIOM FILE`S '
               r'IMPORTS (\d+) ; STEP NOT THE PIN`S OWN (\d+) ; OTHER (\d+) ; NOTHING COMMITTED, PUSHED OR DISPATCHED ;', 'the axiom diagnosis` foot')
    ll = _bfig('%s_llm_line_drafts.txt' % ACT, r'\*\*THE LLM-CONTRIBUTION LINE \(PLACE-papers day1/A_Place_to_Stand\.md :(\d+)\) AGAINST (\d+) WAVE 1 PAPERS '
               r'AND (\d+) KERNEL READMES: SAME (\d+) ; DIFFERS (\d+) ; ABSENT (\d+) ; DRAFTS (\d+) ; NOTHING EDITED ;', 'the LLM line`s foot')
    ad = _bfig('%s_address_scan.txt' % ACT, r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ; PLACES (\d+) ; CONTROLS 3 OF 3 AS WANTED ;',
               'the address scan`s foot')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'), v122_cases=v2[0], v122_wanted=v2[1],
                n31=cf[0], b31=cf[1], n55=cf[2], b55=cf[3], h31=cf[4], h55=cf[5], ctl_ok=bool(cc) and cc.get('ok') is True and cc.get('c1') is True,
                walk_held=wk[0], walk_refuted=wk[1], walk_unscor=wk[2], walk_ctl=wk[3], walk_grade=wg,
                e0=e0, c2_grade=cp[0], c2_scope=cp[1], c2_true=cp[2], c2_of=cp[3], c2_lo=cp[4], c2_hi=cp[5], c2_bound=cp[6], c2_under=cp[7], c2_under_of=cp[8],
                ins_n=int(ins[0]), ins_new=ins[1], ins_first=ins[2], ins_last=ins[3], ins_pop=ins[4], ins_reused=ins[5], ins_s1=ins[6], ins_s2=ins[7],
                ins_nav=ins[8], ins_nav_in=ins[9],
                rp_rows=rp[0], rp_rep=int(rp[1]), rp_diff=rp[2], rp_notrun=rp[3], rp_pw=rp[4], rp_pr=rp[5],
                rp_differs=[r['id'] for r in rpj if r.get('grade') == 'DIFFERS'], rp_notruns=[r['id'] for r in rpj if r.get('grade') == 'NOT RUN'],
                pg_obj=pg[0], pg_hits=pg[1], pg_copy=pg[2], pg_dated=pg[3], pg_other=pg[4], pg_right=pg[5], pg_wrong=pg[6], pg_notes=int(pg[7]), pg_unread=pg[8],
                pg_line=pl,
                ax_absent=ax[0], ax_cover=ax[1], ax_notown=ax[2], ax_other=ax[3],
                ll_line=ll[0], ll_papers=ll[1], ll_readmes=ll[2], ll_same=ll[3], ll_differs=ll[4], ll_absent=ll[5], ll_drafts=ll[6],
                addr=ad[0], name=ad[1], addr_places=ad[2],
#⟪END⟫
#⟪SECTION record 6⟫
def _diag_rows():
    """(R333)(10): the axiom step's diagnosis as banked (data/b723_axiom_diag.json), one row per run read by its id."""
    p = os.path.join(D, '%s_axiom_diag.json' % ACT)
    return json.loads(R.rd(p)) if os.path.exists(p) else []
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R333): no lean process runs on this host and no runner is dispatched this act; (R333)(10) reads b722's runs by their ids. From the
    command bank (the seat's commands, read live from the capture by the `commands` route: local lean none, dispatches none) and the axiom
    diagnosis (each of the five runs the ruling names read by its id, each read a GET; its foot NOTHING COMMITTED, PUSHED OR DISPATCHED)
    (Component 8, the Edit tool; b722's N1 read its rebuild's dispatches)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = _diag_rows()
    read = dict((r.get('kernel'), str(r.get('run'))) for r in rows)
    want = dict((k, str(r)) for k, r in K.AXIOM_RUNS)
    foot = 'NOTHING COMMITTED, PUSHED OR DISPATCHED' in rdn('%s_axiom_diag.txt' % ACT)
    ok = bool(cm) and not seat_lean and disp == [] and K.MAX_DISPATCHES == 0 and read == want and foot
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b723_commands.json): %s; dispatch commands in the capture: %s; '
        'b722`s runs read by their ids in the axiom diagnosis (relay data/b723_axiom_diag.json), the ruling`s five: %s (%s); the diagnosis` '
        'foot NOTHING COMMITTED, PUSHED OR DISPATCHED: %s' % (
            (seat_lean or 'NONE') if cm else 'unread', (len(disp) if disp else 'NONE') if cm else 'unread', read == want,
            ', '.join('%s %s' % (k, read.get(k, 'UNREAD')) for k, _r in K.AXIOM_RUNS), foot))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2 (Component 8, the Edit tool, over b723's objects; b722's chain over b722's registrations in git at b722's record tool): each
# ### computation's bank, the registration it names and that registration's commit, an ancestor of the computation's commit
N2_COMPUTED = (('data/b723_coeffs.txt', 'e8c3dff4', 'REG_C3', 'C3_RELAY'), ('data/b723_walk.txt', '15cb6cc4', 'REG_WALK', 'C3_RELAY'))
# ### N2: each tool's controls (or its rule) before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b723_coeffs.txt', '### THE CONTROLS FIRST', '## D = -31'),
               ('data/b723_walk.txt', 'THE CONTROLS FIRST', '## D = -15'),
               ('data/b723_instruments.txt', 'THE RULE ((R333)(6)), printed before any tool is named', '## THE YIELDS'),
               ('data/b723_axiom_diag.txt', '### THE RULE, PRINTED BEFORE ANY KERNEL', '## SIDE-kernel'),
               ('data/b723_llm_line_drafts.txt', '## THE CONTROLS, BEFORE ANY DOCUMENT', '## paper d1-1'),
               ('data/b723_address_scan.txt', '## THE CONTROLS FIRST', '## THE PLACES READ'))


def _first_tool_line(text):
    """the first line naming a concrete act-numbered tool (bNNN_<name>), 1-based, or None."""
    for i, l in enumerate((text or '').split(NL), 1):
        if re.search(r'\bb\d{3}_[a-z]\w*', l):
            return i
    return None


def _names_before(text):
    """the propagation bank's objects: each `## OBJECT` section's names line before its first graded row, (object head, True|False)."""
    out = []
    for sec in re.split(r'(?m)^(?=## OBJECT )', text or '')[1:]:
        L = sec.split(NL)
        nm = next((i for i, l in enumerate(L) if 'ITS NAMES, PRINTED BEFORE THE SEARCH' in l), None)
        row = next((i for i, l in enumerate(L) if re.match(r'^  (READS RIGHT|READS WRONG|DATED|NOT THIS OBJECT|COPY)\b', l)), None)
        out.append((L[0][:24], nm is not None and row is not None and nm < row))
    return out
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R333): every computation at -31 and -55 names e8c3dff4 as its registration and every computation at the fourteen names H-C2-WALK at
    the commit that landed it (15cb6cc4), each registration's commit an ancestor of the computation's bank; b722's registrations unchanged at
    HEAD; each tool's controls print before its figures (the controls' own commit before the figures' commit); the instruments' rule prints
    before any instrument is named; each propagation object's names print before its search. From git (merge-base, the blob at HEAD against
    the registration's commit) and the banks' own lines."""
    named = [(p, n in rdn(os.path.basename(p))) for p, n, _r, _c in N2_COMPUTED]
    anc = [(p, grc(ROOT, 'merge-base', '--is-ancestor', getattr(K, r), getattr(K, c)) == 0) for p, _n, r, c in N2_COMPUTED]
    reg_same = bool(_show(ROOT, 'HEAD', K.REGISTRATIONS)) and (_show(ROOT, K.REG_C3, K.REGISTRATIONS) or '') == (_show(ROOT, 'HEAD', K.REGISTRATIONS) or '')
    ctl_commit = grc(ROOT, 'merge-base', '--is-ancestor', K.C2_CTL, K.C3_RELAY) == 0 and K.C2_CTL != K.C3_RELAY \
        and 'data/b723_coeffs_controls.json' in g(ROOT, 'show', '--name-only', '--format=', K.C2_CTL).split() \
        and not [x for x in g(ROOT, 'show', '--name-only', '--format=', K.C2_CTL).split() if x in ('data/b723_coeffs.txt', 'data/b723_walk.txt')]
#⟪END⟫
#⟪SECTION record 12⟫
    it = rdn('%s_instruments.txt' % ACT)
    rule_at = next((i for i, l in enumerate(it.split(NL), 1) if l.startswith('THE RULE ((R333)(6))')), None)
    first_tool = _first_tool_line(it)
    rule_first = rule_at is not None and first_tool is not None and rule_at < first_tool
    nb = _names_before(rdn('%s_propagation.txt' % ACT))
    ok = all(o for _p, o in named) and all(o for _p, o in anc) and reg_same and ctl_commit and all(o for _p, o in ctl) and rule_first \
        and len(nb) == 3 and all(o for _h, o in nb)
#⟪END⟫
#⟪SECTION record 13⟫
        'the computations naming their registrations (relay data/b723_coeffs.txt e8c3dff4, data/b723_walk.txt 15cb6cc4): %s; each registration`s '
        'commit an ancestor of the computation`s %s (git merge-base --is-ancestor): %s; relay data/b722_registrations.txt at HEAD equal to its blob '
        'at e8c3dff4: %s; the controls committed at %s, alone of the figures, before the figures` %s: %s; each tool`s controls or rule before its '
        'figures: %s; the instruments` rule at :%s before the first tool named at :%s: %s; each propagation object`s names before its search: %s' % (
            ', '.join('%s %s' % (os.path.basename(p), o) for p, o in named), K.C3_RELAY[:8], ', '.join('%s %s' % (os.path.basename(p), o) for p, o in anc),
            reg_same, K.C2_CTL[:8], K.C3_RELAY[:8], ctl_commit, ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl), rule_at, first_tool,
            rule_first, ', '.join('%s %s' % x for x in nb) or 'NONE READ'))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3 (Component 8, the Edit tool, over b723's objects; b722's over its table, offset and rebuild in git at b722's record tool): the banks
# ### whose grade prints at their end, (bank, the words the foot carries for its grade)
N3_GRADED = (('b723_coeffs.txt', ('H-C3-31 HELD', 'H-C4-55 HELD')), ('b723_walk.txt', ('HELD',)), ('b723_c2_price.txt', ('E0 DERIVES',)),
             ('b723_instruments.txt', ('THE RULE`S OUTPUT',)), ('b723_reproduce.txt', ('REPRODUCES',)), ('b723_propagation.txt', ('READS RIGHT', 'READS WRONG')),
             ('b723_axiom_diag.txt', ('TARGETS ABSENT AT THE PIN', 'STEP NOT THE PIN`S OWN')), ('b723_llm_line_drafts.txt', ('SAME', 'DIFFERS', 'ABSENT')))
# ### N3: a sentence calling the exhaustion compiled -- "compiled" not read with its negation (not, never, nor)
N3_COMPILED = re.compile(r'(?i)\bcompiled\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|never|nor|un)[ -]?(?:yet |been |\w+ and not )?compiled\b')
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R333): every grade prints at its end; the exhaustion of (4) is graded as Python-checked over a cited list, and no sentence of the
    entry calls it compiled; the C2 statement's grade is E0's printed reading. From the graded banks (each bank's last line its foot, the foot
    carrying its grade's words; the walk's THE GRADE after every row it grades), the walk's grade (Python, the list cited, not compiled), the
    C2 price (THE GRADE of E0's reading equal to the foot's) and the entry as composed (the findings bank's text, or the composer before it
    is written): no sentence calling anything compiled but in negation; the entry's grade word E0's."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, words in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, last[0].startswith('### ### **') and all(w in last[0] for w in words)))
    wt = rdn('%s_walk.txt' % ACT)
    g_at = wt.rfind('### THE GRADE: ')
    walk_end = g_at > 0 and g_at > wt.rfind('\n## D = ') and g_at < wt.rfind('### ### **')
#⟪END⟫
#⟪SECTION record 19⟫
    py = 'in Python, not compiled' in f['walk_grade'] and 'cited and not compiled' in f['walk_grade'] and 'by exhaustion' in f['walk_grade']
    e0_ok = f['e0'] == f['c2_grade']
#⟪END⟫
#⟪SECTION record 20⟫
    called = [s.strip()[:120] for s in sents if N3_COMPILED.search(N3_NEGATED.sub('', s))]
    graded_word = ('graded %s' % f['e0']) in text
    ok = all(o for _n, o in graded) and walk_end and py and e0_ok and not called and graded_word
#⟪END⟫
#⟪SECTION record 21⟫
        'each bank`s foot its last line carrying its grade: %s; the walk`s grade after its last row and before its foot (relay data/b723_walk.txt): '
        '%s; the exhaustion graded in Python over the list cited, not compiled: %s; the C2 statement`s grade E0`s printed reading (THE GRADE: %s, '
        'the foot E0 %s; relay data/b723_c2_price.txt): %s; the sentences of %s calling anything compiled but in negation: %s; the entry`s grade '
        'word "graded %s": %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), walk_end, py, f['e0'], f['c2_grade'], e0_ok, src, called or 'NONE', f['e0'], graded_word))
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
    # ### (R333)(9), (11), N5 (Component 8, the Edit tool): no Lean file written into any kernel -- no ref of any kernel carrying a commit made
    # ### after the act's opening commit, no .lean file changed or untracked in its tree; the rebuild-b722 branches kept, each at its tip; the
    # ### address scan's count from its bank (relay data/b723_address_scan.txt), the suite's arm recounting it live
    start = int((g(ROOT, 'log', '-1', '--format=%ct', K.ACT_CURRENT_COMMIT) or '0').strip() or 0)
    lean_w = []
    for kp in K.KERNEL_PATHS:
        if not os.path.isdir(kp):
            continue
        newest = max([int(x) for x in g(kp, 'for-each-ref', '--format=%(committerdate:unix)', 'refs/heads', 'refs/tags').split() if x.isdigit()] or [0])
        loose = [l for l in g(kp, 'status', '--porcelain', '--untracked-files=all').split(NL) if l.strip().endswith('.lean')]
        if newest > start or loose:
            lean_w.append('%s%s' % (os.path.basename(kp), ' (a commit after the act`s start)' if newest > start else ' (a .lean file in the tree)'))
    rb_kept = [k for k, _t, _p in K.WAVE1 if g('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH).strip()]
    addr = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ;', rdn('%s_address_scan.txt' % ACT))
    addr_ok = bool(addr) and addr.group(1) == '0'
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl and not lean_w \
        and len(rb_kept) == len(K.WAVE1) and addr_ok
#⟪END⟫
#⟪SECTION record 27⟫
            'the address scan (relay data/b723_address_scan.txt): PREVIOUS ADDRESS: %s; a Lean file or commit written into a kernel since the act`s '
            'opening commit (%d kernels read): %s; the branch %s kept on the six wave 1 kernels: %d of %d; ' % (
                addr.group(1) if addr else 'UNREAD', len(K.KERNEL_PATHS), lean_w or 'NONE', K.REBUILD_BRANCH, len(rb_kept), len(K.WAVE1)) +
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b723 — lane two, act one hundred and forty-nine, the instruments act under (R333): b722 at its weight, its corrigendum and three '
            'repairs; -31 and -55; the fourteen class-number-2 fields; the C2 statement for Lean graded and priced; the research instruments '
            'entered and their reproduction runner; the propagation read; the author’s name and address; the axiom step diagnosed')
#⟪END⟫
#⟪SECTION record 29⟫
def _held_word(a, b):
    """-31's and -55's readings as the title writes them: one word where they agree, both in order where they do not."""
    return a if a == b else '%s and %s' % (a, b)


#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 8 form ("the class-number-2 table at its fourteen remaining fields: <k> of 14
    HELD<, the value law at all eighteen by exhaustion over Baker's and Stark's list>; -31 and -55: n0 <n1> and <n2>, <HELD | REFUTED>; the C2
    statement for Lean graded <grade> and priced; <m> research instruments entered as I-41 to I-<40+m>, <j> reproducing; the propagation read
    v8 and its <h> notes; the axiom step diagnosed at five wave 1 pins"), the bracketed clause where the walk's grade states it; every figure
    from the banks (Component 8, the Edit tool; b722's title over b722's objects in git at b722's record tool)."""
#⟪END⟫
#⟪SECTION record 31⟫
    law = (', the value law at all eighteen by exhaustion over Baker’s and Stark’s list'
           if 'holds at all eighteen' in f['walk_grade'] and 'by exhaustion' in f['walk_grade'] else '')
    return ('## The class-number-2 table at its fourteen remaining fields: %s of 14 HELD%s; -31 and -55: n0 %s and %s, %s; the C2 statement for '
            'Lean graded %s and priced; %d research instruments entered as I-%s to I-%d, %d reproducing; the propagation read v8 and its %d notes; '
            'the axiom step diagnosed at five wave 1 pins' % (
                f['walk_held'], law, f['n31'], f['n55'], _held_word(f['h31'], f['h55']), f['e0'], f['ins_n'], f['ins_first'],
                40 + f['ins_n'], f['rp_rep'], f['pg_notes']))
#⟪END⟫
#⟪SECTION record 32⟫
    # ### the navigator's letter this act is (b'), primed: the reader takes a letter with its prime (the gate's dry run, defect (e'))
    letters = ', '.join(re.match(r"^\(([a-z][`']?)\)", r).group(0) for r in nav)
    why = (': the probe enumerates every repository without a cited pin at its HEAD, so its count moves with the kernels -- its entry’s range '
           'limits say so' if f['rp_differs'] == ['I-76'] else ', each read in its entry')
    return ('(1) the instruments by the rule, not by the navigator’s list: %d entered, the navigator’s %s beside the output, %s of them in it, '
            'choosing nothing (relay data/b723_instruments.txt); (2) the reproduction run %s of %s REPRODUCES, DIFFERS %s (%s%s), NOT RUN %s '
            '(%s, each with its reason and price) (relay data/b723_reproduce.txt); (3) the C2 statement graded %s with its scope -- that the list is '
            'complete is Baker (1971) and Stark (1975), cited and not compiled -- and priced by two routes, where the compile lives the author’s '
            'word (relay data/b723_c2_price.txt); (4) the axiom step at five pins: targets absent at the pin %s, the step not the pin’s own %s, each '
            'route priced on its rebuild-b722 branch for %s, nothing dispatched (relay data/b723_axiom_diag.txt); (5) the LLM-contribution line: '
            'SAME %s, DIFFERS %s, ABSENT %s, %s drafts for the release sitting, nothing in a paper or README edited (relay '
            'data/b723_llm_line_drafts.txt); (6) the propagation read’s %s READS WRONG and %s DATED hits noted at FINDINGS :%s, no line rewritten; '
            '(7) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); (8) %s and the seat’s %s defect%s as '
            'lettered' % (
                f['ins_n'], f['ins_nav'], f['ins_nav_in'], f['rp_rep'], f['rp_rows'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none', why,
                f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['e0'], f['ax_absent'], f['ax_notown'], K.NEXT_ACT, f['ll_same'],
                f['ll_differs'], f['ll_absent'], f['ll_drafts'], f['pg_wrong'], f['pg_dated'], f['pg_line'],
#⟪END⟫
#⟪SECTION record 33⟫
def _diag_line():
    """the axiom diagnosis by kernel, as its json banks it: `<kernel> <class>` for each of the five runs."""
    return '; '.join('%s %s' % (r.get('kernel'), r.get('class')) for r in _diag_rows()) or 'unread'


#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 8, the Edit tool, over b723's objects;
    b722's composer over b722's objects kept below as _finding_text_b722, not called, and in git at b722's record tool)."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    cut = jl('%s_coeffs_controls.json' % ACT).get('cut')
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The fourteen class-number-2 fields left after b722 hold H-C2-WALK through %s by b711’s route -- %s of 14 HELD, the control row -15 %s -- '
         'so the value law at the least negative index stands at all eighteen by exhaustion over the list Baker and Stark proved complete, '
         'checked in Python over that list as cited and not compiled; -31 and -55, under e8c3dff4, read n0 %s and %s with b = %s and %s, '
         'H-C3-31 %s and H-C4-55 %s; the C2 statement for Lean is graded %s by E0 with its scope beside it, true as written in Python at %s of %s '
         'fields, and priced by two routes; %d research instruments are entered as I-%s to I-%d in b618’s form, %d of them reproducing their '
         'banked figure; the propagation read under standing clauses v8 writes %d dated notes; and the axiom step at five wave 1 pins is '
         'diagnosed from b722’s runs by their ids, nothing dispatched.' % (
             cut, f['walk_held'], f['walk_ctl'], f['n31'], f['n55'], f['b31'], f['b55'], f['h31'], f['h55'], f['e0'], f['c2_true'], f['c2_of'],
             f['ins_n'], f['ins_first'], 40 + f['ins_n'], f['rp_rep'], f['pg_notes']), '',
         '*Filed at b723 on the author’s ruling `(R333)`; %d question%s put before the root. Banks: relay `data/b723_corrigendum.txt`, '
         '`data/b723_standing_v122.txt`, `data/b723_coeffs.txt`, `data/b723_walk.txt`, `data/b723_c2_statement.txt`, `data/b723_c2_price.txt`, '
         '`data/b723_instruments.txt`, `data/b723_reproduce.txt`, `data/b723_propagation.txt`, `data/b723_address_scan.txt`, '
         '`data/b723_axiom_diag.txt`, `data/b723_llm_line_drafts.txt`, `data/b723_touch.txt`, `data/b723_standing_figures.txt`, '
         '`data/b723_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum and the repairs** ((R333)(1)-(2), `%s`, `%s`): b722 entered at its weight (FINDINGS :%s); the corrigendum of '
         'b722’s %s events and %s defects, %s items each CLAIM or CLOSE and NEW or REPEAT -- CLAIM %s, CLOSE %s, %s repeats -- at FINDINGS '
         ':%s, the corrigenda bank appended at row (%s); tools/standing/ at %s with the three repairs (the seal’s list from the seal bank; USED '
         'by discriminant and principal form; the closure reader retired, the hand list of record), %s cases, %s as wanted (relay '
         'data/b723_standing_v122.txt).' % (
             K.C1_RELAY[:8], K.C1_PP[:8], f['weight'], f['corr_events'], f['corr_defects'], f['corr_items'], f['corr_claim'], f['corr_close'],
             f['corr_repeat'], f['corr_line'], f['corr_row'], f['ver'], f['v122_cases'], f['v122_wanted']), '',
         '**-31 and -55** ((R333)(3), N2, `%s`, `%s`): under their registration at `%s` (H-C3-31 and H-C4-55, relay data/b722_registrations.txt '
         'section (5), read unchanged); the controls first, committed before any figure -- the recursion at zeta’s series returning von Mangoldt, '
         '-23 reproducing b711’s bank, a planted coefficient failing to reproduce, each as wanted: %s; then through %s by b711’s route: '
         'n0(-31) = %s, b = %s and n0(-55) = %s, b = %s, each row on its own clauses with the prime clause -- H-C3-31 %s, H-C4-55 %s (relay '
         'data/b723_coeffs.txt).' % (
             K.C2_CTL[:8], K.C3_RELAY[:8], K.REG_C3[:8], f['ctl_ok'], cut, f['n31'], f['b31'], f['n55'], f['b55'], f['h31'], f['h55']), '',
         '**The fourteen** ((R333)(4), N2, N3, `%s`): under H-C2-WALK at `%s`, the fourteen fields through %s by the same route and controls: '
         '%s of 14 HELD, REFUTED %s, NOT SCORABLE %s, the control row -15 %s; the grade at its end, as banked: “%s” (relay data/b723_walk.txt).' % (
             K.C3_RELAY[:8], K.REG_WALK[:8], cut, f['walk_held'], f['walk_refuted'], f['walk_unscor'], f['walk_ctl'], f['walk_grade']), '',
         '**The C2 statement for Lean** ((R333)(5), N3, `%s`, `%s`): the text committed alone before its grade (relay data/b723_c2_statement.txt); '
         'graded by E0 (relay tools/e0_rule.py, unedited) %s, its one hypothesis a domain condition, the scope beside it (%s); as written, true '
         'in Python at %s of %s; priced per field -- (A) decide as written, %s to %s lattice points, unmeasured in Lean; (B) the certificate '
         'route under %s operations at %s of %s, two general lemmas named and not proved; where the compile lives the author’s word (relay '
         'data/b723_c2_price.txt).' % (
             K.C4_STMT[:8], K.C4_RELAY[:8], f['e0'], f['c2_scope'], f['c2_true'], f['c2_of'], f['c2_lo'], f['c2_hi'], f['c2_bound'], f['c2_under'],
             f['c2_under_of']), '',
         '**The research instruments** ((R333)(6)-(7), N2, `%s`, `%s`, `%s`): the rule printed before any tool was named; its output %d of a '
         'population of %s act-numbered tools (%s reused, (S1) %s, (S2) %s), every one read by hand; the navigator’s %s printed beside it, %s in '
         'the output, choosing nothing (relay data/b723_instruments.txt). Entered at INSTRUMENTS.md :%d onward as I-%s to I-%d in b618’s form -- '
         'reads, decides, controls, the validated case with its bank and line, range limits, entered with its act and its OPEN_TRAILS or bank '
         'line -- nothing above I-41 edited. The runner tools/research/reproduce.py, sealed with the act’s tools, each instrument imported '
         'unedited: %s rows, %d REPRODUCES, %s DIFFERS (%s), %s NOT RUN (%s, each with its reason and price), the planted wrong figure '
         'differing as wanted at %s of %s (relay data/b723_reproduce.txt); the standing arm G-RESEARCH-REPRODUCES joins, the run list 117.' % (
             K.C5_RULE[:8], K.C5_RELAY[:8], K.C5_PP[:8], f['ins_n'], f['ins_pop'], f['ins_reused'], f['ins_s1'], f['ins_s2'], f['ins_nav'],
             f['ins_nav_in'], K.INSTRUMENTS_FIRST, f['ins_first'], 40 + f['ins_n'], f['rp_rows'], f['rp_rep'], f['rp_diff'],
             ', '.join(f['rp_differs']) or 'none', f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr']), '',
         '**The propagation read** ((R333)(8), N2, `%s`, `%s`, `%s`): standing clauses v8, v7 with row (82), landed by a commit of its own; its '
         'opening run on %s objects, each object’s names printed before its search: %s hits -- COPY %s, DATED %s, NOT THIS OBJECT %s, READS RIGHT '
         '%s, READS WRONG %s, unread %s -- and %d dated notes at FINDINGS :%s, each pointing to the line it corrects, no line rewritten (relay '
         'data/b723_propagation.txt).' % (
             K.STANDING_COMMIT[:8], K.C6_RELAY[:8], K.C6_PP[:8], f['pg_obj'], f['pg_hits'], f['pg_copy'], f['pg_dated'], f['pg_other'],
             f['pg_right'], f['pg_wrong'], f['pg_unread'], f['pg_notes'], f['pg_line']), '',
         '**The author’s name and address** ((R333)(9), N5): git’s global user.email the GitHub noreply form; user.name set to the account '
         'login on the author’s answer and printed by its kind alone; the scan over every commit and bank of the act, the previous address read '
         'from history and held in memory: PREVIOUS ADDRESS: %s, the author’s name %s, over %s places, its controls as wanted (relay '
         'data/b723_address_scan.txt).' % (f['addr'], f['name'], f['addr_places']), '',
         '**The axiom step at five wave 1 pins** ((R333)(10), N1, `%s`): b722’s runs read by their ids, GETs alone, each step log and artifact '
         'read and its cause classed -- %s: targets absent at the pin %s, the build target not covering the axiom file’s imports %s, the step '
         'not the pin’s own %s, other %s; a repair route priced per kernel on its rebuild-b722 branch, the dispatches %s’s; nothing committed, '
         'pushed or dispatched (relay data/b723_axiom_diag.txt).' % (
             K.C7_RELAY[:8], _diag_line(), f['ax_absent'], f['ax_cover'], f['ax_notown'], f['ax_other'], K.NEXT_ACT), '',
         '**The release sitting’s list** ((R333)(12), `%s`): the LLM-contribution line quoted from the monograph’s end matter (:%s), and %s wave 1 '
         'papers and %s kernel READMEs read against it -- SAME %s, DIFFERS %s, ABSENT %s; %s drafts in the monograph’s words and position, nothing '
         'in a paper or README edited (relay data/b723_llm_line_drafts.txt).' % (
             K.C7_RELAY[:8], f['ll_line'], f['ll_papers'], f['ll_readmes'], f['ll_same'], f['ll_differs'], f['ll_absent'], f['ll_drafts']), '',
         '**The touch read** (standing clauses v8): each object this entry names looked up and marked AGREES or DIFFERS by hand before the root '
         '(relay data/b723_touch.txt). The act’s counter CLAIM %d, CLOSE %d.' % (f['claim'], f['close']), '',
         '**The standing arms**: the four figures at b723 -- %s, %s, %s, %s -- against b722’s %s, %s, %s, %s, read by b706’s tool over b706’s '
         'roster (relay data/b723_standing_figures.txt); one standing arm added by the ruling, G-RESEARCH-REPRODUCES.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs10']['correspondence'], f['figs10']['readme'], f['figs10']['partners'], f['figs10']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at step zero, %s OK, %s missed, each miss raised before the component '
         'citing it; %d answer check%s before the root.' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** ((R204)(3)(ii)-(iii)): the computation and its price meet at the C2 statement -- the fourteen read here and '
         'the four read before make the eighteen its list names, and its price is counted on those same n0; the instruments and the propagation '
         'read meet at the record -- each instrument found by its entry and run again against its bank, each corrected statement read again '
         'where it stands and noted beside it.', '',
         '**Carried to:** %s, each from its bank: the axiom step repaired on the rebuild-b722 branches and dispatched at the pins (relay '
         'data/b723_axiom_diag.txt); the C2 compile at the route the author names (relay data/b723_c2_price.txt); the drafts for the release '
         'sitting (relay data/b723_llm_line_drafts.txt); the instruments not reproducing here, each with its entry; the draft held at v5.' % (
             K.NEXT_ACT), '',
         '**Next.** %s.' % K.next_line(), '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _finding_text_b722():
    """b722's form over b722's objects, kept for the record and not called (Component 8)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 8, the Edit tool, over b723's objects; b722's composer over b722's objects kept below as _trail_text_b722,
    not called, and in git at b722's record tool)."""
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R333) ratified.** (1) b722 at its weight. (2) The corrigendum and three repairs, v1.2.2. (3) -31 and -55. (4) The fourteen '
             'class-number-2 fields. (5) The C2 statement for Lean, graded and priced. (6) The research instruments entered. (7) Their '
             'reproduction runner. (8) Standing clauses v8 and the propagation read. (9) The author’s name and address. (10) The axiom step '
             'diagnosed. (11) Step zero. (12) The release sitting’s list, drafts alone. (13) The next act.', '',
             '**Entered:** FINDINGS.md:%s (b722’s weight), :%s (the corrigendum), :%s (the propagation notes), :%s (the entry); INSTRUMENTS.md '
             ':%d (I-41 to I-%d); this record.' % (
                 f['weight'], f['corr_line'], f['pg_line'], fj.get('entry_line'), K.INSTRUMENTS_FIRST, 40 + f['ins_n']), '',
             '**-31 and -55:** under `%s`, n0 %s and %s, b %s and %s, H-C3-31 %s, H-C4-55 %s (relay data/b723_coeffs.txt).' % (
                 K.REG_C3[:8], f['n31'], f['n55'], f['b31'], f['b55'], f['h31'], f['h55']), '',
             '**The fourteen:** under H-C2-WALK at `%s`, %s of 14 HELD, the control row -15 %s; the value law at all eighteen by exhaustion over '
             'the list cited, in Python, not compiled (relay data/b723_walk.txt).' % (K.REG_WALK[:8], f['walk_held'], f['walk_ctl']), '',
             '**The C2 statement:** graded %s by E0, true as written in Python at %s of %s, priced by two routes, the compile’s route the author’s '
             'word (relay data/b723_c2_statement.txt, data/b723_c2_price.txt).' % (f['e0'], f['c2_true'], f['c2_of']), '',
             '**The instruments:** I-%s to I-%d entered (INSTRUMENTS.md :%d); reproduced %d of %s, DIFFERS %s (%s), NOT RUN %s (%s) (relay '
             'data/b723_reproduce.txt); G-RESEARCH-REPRODUCES in the run list, 117.' % (
                 f['ins_first'], 40 + f['ins_n'], K.INSTRUMENTS_FIRST, f['rp_rep'], f['rp_rows'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none',
                 f['rp_notrun'], ', '.join(f['rp_notruns']) or 'none'), '',
             '**The propagation read:** v8 at `%s`; %s hits, %d notes at FINDINGS :%s (relay data/b723_propagation.txt).' % (
                 K.STANDING_COMMIT[:8], f['pg_hits'], f['pg_notes'], f['pg_line']), '',
             '**The axiom step:** %s; routes priced for %s (relay data/b723_axiom_diag.txt).' % (_diag_line(), K.NEXT_ACT), '',
             '**The release sitting’s list:** SAME %s, DIFFERS %s, ABSENT %s, %s drafts (relay data/b723_llm_line_drafts.txt).' % (
                 f['ll_same'], f['ll_differs'], f['ll_absent'], f['ll_drafts']), '',
             '**The author’s name and address:** PREVIOUS ADDRESS: %s (relay data/b723_address_scan.txt).' % f['addr'], '',
             '**The standing line:** relay data/standing_clauses_v8.txt from `%s`; the touch read relay data/b723_touch.txt; the act’s counter '
             'CLAIM %d, CLOSE %d.' % (K.STANDING_COMMIT[:8], f['claim'], f['close']), '',
             '**Act root:** b723 `%s` (previous `%s`, b722’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b723_author_answers.txt).' % (
                 n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The standing clauses:** relay data/standing_clauses_v8.txt; tools/standing/ at %s (relay data/b723_standing_v122.txt); the standing '
             'report tool (relay data/b723_report.txt).' % f['ver'], '']
    aw = AC.author_words_section(ACT)   # ### the author's word after the seal, from its bank, verbatim
    rows_ += ['**' + aw[0][4:].rstrip(':') + ':**'] + ['> ' + l[4:] if l.startswith('    ') else '> ' + l for l in aw[1:]] + ['']
    rows_ += ['**The kernels:** no kernel’s main written, no tag cut, no Lean file written into any kernel; the rebuild-b722 branches of the '
              'six wave 1 kernels kept for %s; port-b707 at %s, kept, its tag %s at it; SIDE-faces-join at %s with its one tag %s; no lean process '
              'on this host, nothing dispatched, b722’s runs read by their ids.' % (
                  K.NEXT_ACT, K.PORT_NEW_TIP[:8], K.LV_TAG, K.JOIN_NEW_TIP[:8], K.JOIN_TAG[0]), '',
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
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1: none -- (R333)(10) reads b722`s runs by their ids; MEASURED off the command bank (each dispatch route run at a command`s head).'),
    ('runner runs read by their ids for the axiom step', 'AXRUNS', 'AXRUNS', 'runs', '### (R333)(10), N1: b722`s five, none new; MEASURED off data/b723_axiom_diag.json against the worklist`s AXIOM_RUNS.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked ((R333)(11)); MEASURED off the twelve kernels` refs/heads/pin-b723*.'),
    ('rebuild branches cut on a kernel', 0, 0, 'branches', '### none this act: b722`s rebuild-b722 branches kept for b723 ((R333)(11)).'),
    ('rebuild-b722 branches kept on the wave 1 kernels', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### (R333)(11): the six, as b722 left them; MEASURED off the six kernels` refs/heads.'),
    ('rebuild-b722 branches standing at their origins', 'RBPUSHED', 'RBPUSHED', 'branches', '### as b722 pushed them; MEASURED off each kernel`s refs/remotes/origin/rebuild-b722.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### b722`s, unchanged: SIDE-frobenius`s two (the workflow copied verbatim; the author`s two lines); none this act; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b723*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### none: each branch at its pin or carrying b722`s workflow alone; MEASURED off each branch against its pin.'),
    ('Lean files written in any kernel', 0, 0, 'files', '### N5: no Lean file in any kernel.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R333)(11): relay push-b722-closing, push-b722-preroot, push-b722-record; PLACE-papers push-b722-preroot, push-b722-record; each local, by name, after --merged listed it (data/b723_stepzero.txt :58-:61).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written on a kernel branch', 0, 0, 'files', '### none this act (N5).'),
    ('workflow files on a kernel branch beyond its pin', 'RBWF', 'RBWF', 'files', '### b722`s, unchanged: SIDE-frobenius`s rebuild branch alone; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act, (R333) ordering no REGISTRY write.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat 2b194142..HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R333)(2): FINDINGS :11218.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R333)(2): one row, b722`s.'),
    ('dated propagation notes landed at FINDINGS, in one block', 1, 1, 'blocks', '### (R333)(8), v8 row (82): FINDINGS :11284 (f127660c); no line rewritten.'),
    ('research instruments entered at INSTRUMENTS.md', 'ENTRIES', 'ENTRIES', 'entries', '### (R333)(6): I-41 on, appended at :490 (4af48e1e), nothing above I-41 edited; MEASURED off data/b723_instrument_entries.json.'),
    ('reproduction rows, one per instrument', 'REPROWS', 'REPROWS', 'rows', '### (R333)(7): tools/research/reproduce.py; MEASURED off data/b723_reproduce.json.'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R333)(3)-(12): -31 and -55, the fourteen, the C2 price, the instruments, the reproduction, the propagation read, the address scan, the axiom diagnosis, the LLM line; MEASURED off the banks present.'),
    ('registrations read unchanged from their commit', 5, 5, 'registrations', '### (R333)(3)-(4), N2: b716`s, b718`s, b719`s, b720`s and b722`s at their commits, b722`s at e8c3dff4, blob for blob at HEAD.'),
    ('registrations named by the computations, each an ancestor of the figures', 'REGS', 'REGS', 'commits', '### (R333)(3)-(4), N2: e8c3dff4 for -31 and -55, H-C2-WALK at 15cb6cc4 for the fourteen; MEASURED off the ancestry to 6afe03bf.'),
    ('banks holding a figure at a registered discriminant before its registration', 'PREREG', 'PREREG', 'banks', '### N2: none; MEASURED off each figure bank`s first commit against e8c3dff4.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean statements of the table written or compiled', 0, 0, 'statements', '### N1, N3: the exhaustion Python-checked over a cited list, not compiled; the C2 statement graded by E0 and priced, not compiled.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R333)(2): tools/standing/ to v1.2.2 -- VERSION changed, readfirst.py, sealcheck.py, used.py and v122.py new; MEASURED off the worklist`s lists (tools/research/reproduce.py, (R333)(7), sealed with the act`s tools, outside them).'),
    ('arms out of the suite`s run list by b722`s retirement', 'RETIRED', 'RETIRED', 'arms', '### b722`s RETIRED, carried unchanged; MEASURED off tools/standing/arms.py.'),
    ('arms retired this act', 0, 0, 'arms', '### none: the run list 117 with (R333)(7)`s arm.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 2, 2, 'banks', '### data/act_current.json at step zero ((R333)(11)) and data/standing_clauses_v8.txt by a commit of its own (0ff64911, (R333)(8)); data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### (R333)(11): the 2,560 MB hold read before each suite part and each computation; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 1, 1, 'arms', '### (R333)(7): G-RESEARCH-REPRODUCES, the run list 117.'),
    ('new occurrences of the author`s name or previous address', 'ADDRESS', 'ADDRESS', 'occurrences', '### (R333)(9)(i), N5: PREVIOUS ADDRESS 0; MEASURED off data/b723_address_scan.txt (the address never printed).'),
    ('banks, faces or tools edited after the lock gate', 0, 0, 'edits', '### (R333)(1), N4: a restore an edit; a correction found after the lock stands as an event.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs and b722`s run reads ((R333)(10)).'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.REG_C3, c], capture_output=True).returncode == 0 \
            and c != K.REG_C3

    def anc(a, b):
        return subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b], capture_output=True).returncode == 0
    # ### N2 (Component 8, the Edit tool): the figure banks of (3)-(4), each first committed after b722's registrations (e8c3dff4)
    fig_banks = [p for p in ('data/b723_coeffs.txt', 'data/b723_coeffs.json', 'data/b723_coeffs_controls.json', 'data/b723_walk.txt', 'data/b723_walk.json')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([c for c in (K.REG_C3, K.REG_WALK) if anc(c, K.C3_RELAY)]),
                    AXRUNS=jcount('b723_axiom_diag.json', lambda j: len([x for x in j if (x.get('kernel'), int(x.get('run') or 0)) in set((k, int(r)) for k, r in K.AXIOM_RUNS)])),
                    ENTRIES=jcount('b723_instrument_entries.json', lambda j: len(j.get('entries') or [])),
                    REPROWS=jcount('b723_reproduce.json', lambda j: len(j.get('rows') or [])),
                    ADDRESS=tfirst('b723_address_scan.txt', r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;'),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('coeffs', 'walk', 'c2_price', 'instruments', 'reproduce', 'propagation', 'address_scan', 'axiom_diag',
                                               'llm_line_drafts') if os.path.exists(os.path.join(ROOT, 'data', 'b723_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'AXRUNS', 'ENTRIES', 'REPROWS', 'ADDRESS', 'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b723_registration_2026-10-28.txt -- b723, THE INSTRUMENTS ACT: b722 AT ITS WEIGHT AND ITS CORRIGENDUM; "
                             "-31 AND -55 COMPUTED UNDER THEIR REGISTRATION; THE FOURTEEN FIELDS WALKED; THE C2 STATEMENT GRADED AND PRICED; "
                             "THE RESEARCH INSTRUMENTS ENTERED AND REPRODUCED; THE PROPAGATION READ UNDER v8; THE AXIOM STEP DIAGNOSED AT "
                             "FIVE PINS, UNDER (R333)"),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b722's standing report (tools/b722_report.py) by diff and its lines rewritten at Component 8: b722's lines (the rebuild, the
table over h = 3, 4, 5, the C2 halt, the predictions, the offset, the frozen line) read banks this act does not write, and are not carried;
the lines are b723's: the axiom step diagnosed from b722's runs by their ids (KERNEL), -31 and -55, the fourteen fields and the C2 statement
(CERTIFIED -- Python-checked, not compiled, N3), the research instruments and their reproduction (REGISTERED), and the propagation notes,
the LLM line's drafts and the draft (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ### b723's lines (Component 8, the Edit tool), each from the record tool's figures over b723's banks
    # ------------------------------------------------------------------ KERNEL: THE AXIOM STEP ((R333)(10)), b722's runs read by their ids
    # ------------------------------------------------------------------ (N1: no lean on the host, no dispatch)
    sk = seat('%s_axiom_diag.txt' % ACT, '**THE AXIOM STEP AT FIVE PINS')
    keys['AXIOM'] = ('KERNEL -- THE AXIOM STEP AT FIVE WAVE 1 PINS, diagnosed from b722`s runs read by their ids: targets absent at the pin %s, '
                     'the build target not covering the axiom file`s imports %s, the step not the pin`s own %s, other %s; each route priced, '
                     'nothing committed, pushed or dispatched; the repair b723`s. SOURCE %s.' % (
                         f['ax_absent'], f['ax_cover'], f['ax_notown'], f['ax_other'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: -31 AND -55 ((R333)(3)); THE FOURTEEN ((R333)(4)); THE C2
    # ------------------------------------------------------------------ STATEMENT ((R333)(5)) -- Python-checked, not compiled (N3)
    sc = seat('%s_coeffs.txt' % ACT, '**n0(-31) = ')
    keys['COEFFS'] = ('CERTIFIED -- -31 AND -55 UNDER e8c3dff4: n0(-31) = %s, b = %s, H-C3-31 %s; n0(-55) = %s, b = %s, H-C4-55 %s; the controls '
                      'first, each row with its prime clause; exact, Python-checked, not compiled (N3). SOURCE %s.' % (
                          f['n31'], f['b31'], f['h31'], f['n55'], f['b55'], f['h55'], sc['text']))
    seats.append(sc)
    sw = seat('%s_walk.txt' % ACT, '**H-C2-WALK: ')
    keys['WALK'] = ('CERTIFIED -- THE FOURTEEN REMAINING CLASS-NUMBER-2 FIELDS UNDER H-C2-WALK (15cb6cc4): %s of 14 HELD, REFUTED %s, NOT '
                    'SCORABLE %s, the control row -15 %s; %s. SOURCE %s.' % (
                        f['walk_held'], f['walk_refuted'], f['walk_unscor'], f['walk_ctl'], f['walk_grade'][:300].rstrip('.'), sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    s2 = seat('%s_c2_price.txt' % ACT, '**THE C2 STATEMENT: ')
    keys['C2'] = ('CERTIFIED -- THE C2 STATEMENT FOR LEAN: E0 %s (the scope beside it: %s); as written, true in Python at %s of %s; priced per '
                  'field, the certificate route under %s at %s of %s; nothing compiled, nothing dispatched. SOURCE %s.' % (
                      f['c2_grade'], f['c2_scope'], f['c2_true'], f['c2_of'], f['c2_bound'], f['c2_under'], f['c2_under_of'], s2['text']))
    seats.append(s2)
    # ------------------------------------------------------------------ REGISTERED: THE RESEARCH INSTRUMENTS ((R333)(6)) AND THEIR
    # ------------------------------------------------------------------ REPRODUCTION ((R333)(7))
    si = seat('%s_instruments.txt' % ACT, '**THE RULE`S OUTPUT: ')
    keys['INSTR'] = ('REGISTERED -- THE RESEARCH INSTRUMENTS BY RULE: %s entered at PLACE-papers INSTRUMENTS.md as I-%s to I-%s in b618`s form '
                     '(the population %s, reused %s; the navigator`s %s, %s in the output). SOURCE %s.' % (
                         f['ins_n'], f['ins_first'], f['ins_last'], f['ins_pop'], f['ins_reused'], f['ins_nav'], f['ins_nav_in'], si['text']))
    seats.append(si)
    sr = seat('%s_reproduce.txt' % ACT, '**ROWS ')
    keys['REPRO'] = ('REGISTERED -- THE REPRODUCTION (tools/research/reproduce.py): %s rows, REPRODUCES %s, DIFFERS %s (%s), NOT RUN %s (%s), '
                     'the planted wrong figures as wanted %s of %s. SOURCE %s.' % (
                         f['rp_rows'], f['rp_rep'], f['rp_diff'], ', '.join(f['rp_differs']) or 'none', f['rp_notrun'],
                         ', '.join(f['rp_notruns']) or 'none', f['rp_pw'], f['rp_pr'], sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ HELD: THE PROPAGATION NOTES; THE DRAFTS; THE DRAFT
    sg = seat('%s_propagation.txt' % ACT, '**THE PROPAGATION READ: ')
    keys['PROP'] = ('HELD -- THE PROPAGATION READ (standing clauses v8 row (82)): %s objects, %s hits, %s reading wrong and %s dated; %s notes '
                    'landed at FINDINGS :%s, no line rewritten. SOURCE %s.' % (
                        f['pg_obj'], f['pg_hits'], f['pg_wrong'], f['pg_dated'], f['pg_notes'], f['pg_line'], sg['text']))
    seats.append(sg)
    sh = seat('%s_ferry.txt' % ACT, 'THE DRAFT stands at v5, HELD')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits; the LLM-contribution line`s %s drafts for the release sitting '
                    '(SAME %s, DIFFERS %s, ABSENT %s), in the relay alone, nothing edited. SOURCE %s.' % (
                        K.DRAFT, f['ll_drafts'], f['ll_same'], f['ll_differs'], f['ll_absent'], sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['AXIOM']), ('CERTIFIED', ['COEFFS', 'WALK', 'C2']), ('REGISTERED', ['INSTR', 'REPRO']), ('HELD', ['PROP', 'HELD'])]
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
