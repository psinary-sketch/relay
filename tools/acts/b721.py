# -*- coding: utf-8 -*-
# b721 -- THE ACT`S SECTIONS OF THE SEVEN CLOSE TOOLS ((R333)(2)(i), tools/standing/fold.py), READ AS TEXT, NOT IMPORTED.
# Each block opens with a line "#⟪SECTION <tool> <n>⟫" (the act`s own lines, verbatim, at the template`s slot n of that tool)
# or "#⟪OVERRIDE <tool> <first> <last>⟫" (the act`s lines in place of the template`s lines first..last) and closes with the line
# "#⟪END⟫"; " NOEOL" before the closing mark: the last line has no newline. Edited by the Edit tool. Built at b723 by
# tools/b723_fold.py from tools/b721_<tool>.py.
# Each "#⟪DEAD <tool> <names>⟫" line: the names the act`s tool reads through its worklist alias that the worklist lacks, on
# routes the act never ran (the tool as carried); the loader prints them and refuses any other missing name.
#⟪DEAD checks ⟫
#⟪DEAD citation ⟫
#⟪DEAD closing ⟫
#⟪DEAD record B710_TRAIL,B713_ONSETS_RELAY,B713_PRED_RELAY,MAX_PORT_DISPATCHES,PORT_FILE,PORT_LINE⟫
#⟪DEAD reg_gate ⟫
#⟪DEAD regspec ⟫
#⟪DEAD report ⟫
#⟪SECTION checks 1⟫
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'de' else 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) at the seal, (d) and (e) the navigator's, every other the seat's
#⟪END⟫
#⟪SECTION checks 2⟫
REQUIRED_BANKS = ('data/b721_corrigendum.txt', 'data/b721_registrations.txt', 'data/b721_standing_v121.txt',
                  'data/b721_derivation.txt', 'data/b721_offset_pred.txt', 'data/b721_offset_read.txt', 'data/b721_offset_tier.txt',
                  'data/b721_surgery_carry.txt', 'data/b721_frozen_line.txt', 'data/b721_frozen_line_drafts.txt',
                  'data/b721_rebuild.txt', 'data/b721_rebuild_rows.json', 'data/b721_touch.txt',
#⟪END⟫
#⟪SECTION checks 3⟫
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### (R331)(3): a shared bank by version, outside the act's prefix, named apart
#⟪END⟫
#⟪SECTION checks 4⟫
#⟪END⟫
#⟪SECTION checks 5⟫
        regs_new=rd('b721_registrations.txt'),
        # ### (R331)(3)-(4), N2: the registrations at each of their four commits (the rule alone; the halt; rule (4); the predictions)
        regs_at=dict((k, _s(blob(ROOT, '%s:%s' % (c, K.REGISTRATIONS_NEW)))) for k, c in (('c2reg', K.C2_REG), ('halt', K.C2_HALT), ('rule4', K.C3_RULE),
                                                                                        ('pred', K.C2_PRED))),
#⟪END⟫
#⟪SECTION checks 6⟫
#⟪END⟫
#⟪SECTION checks 7⟫
                 for k, a, b in (('reg_select', K.C2_REG, K.C2_SELECT), ('select_halt', K.C2_SELECT, K.C2_HALT), ('halt_rule4', K.C2_HALT, K.C3_RULE),
                                 ('rule4_deriv', K.C3_RULE, K.C3_RELAY), ('deriv_tool', K.C3_RELAY, K.C3_PREDICT_TOOL),
                                 ('tool_pred', K.C3_PREDICT_TOOL, K.C2_PRED), ('pred_offset', K.C2_PRED, K.C4_PRED), ('offset_read', K.C4_PRED, K.C4_RELAY),
                                 ('read_surgery', K.C4_RELAY, K.C5_RELAY), ('surgery_frozen', K.C5_RELAY, K.C6_FROZEN))),
        derivation=rd('b721_derivation.txt'), offset_pred=rd('b721_offset_pred.txt'), offset=rd('b721_offset_read.txt'), offset_tier=rd('b721_offset_tier.txt'),
        surgery=rd('b721_surgery_carry.txt'),
        # ### (R331)(7): the frozen line, its drafts and the rebuild (its bank, its rows, each wave 1 kernel's branch, main and tags)
        frozen=rd('b721_frozen_line.txt'), drafts=rd('b721_frozen_line_drafts.txt'),
        rebuild=rd('b721_rebuild.txt'), rebuild_rows=json.loads(rd('b721_rebuild_rows.json') or '[]'), rebuild_state=_rebuild_state(),
#⟪END⟫
#⟪SECTION checks 8⟫
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2reg=_ct(ROOT, K.C2_REG), c2halt=_ct(ROOT, K.C2_HALT), c2pred=_ct(ROOT, K.C2_PRED),
               c3rule=_ct(ROOT, K.C3_RULE), c3=_ct(ROOT, K.C3_RELAY), c4pred=_ct(ROOT, K.C4_PRED), c4=_ct(ROOT, K.C4_RELAY), c5=_ct(ROOT, K.C5_RELAY),
               c6=_ct(ROOT, K.C6_RELAY), reg=_ct(ROOT, K.REG_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS), actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
#⟪END⟫
#⟪SECTION checks 9⟫
                   c2reg=files_of(ROOT, K.C2_REG), c2select=files_of(ROOT, K.C2_SELECT), c2halt=files_of(ROOT, K.C2_HALT),
                   c2picker=files_of(ROOT, K.C2_PICKER), c2pred=files_of(ROOT, K.C2_PRED), c3rule=files_of(ROOT, K.C3_RULE),
                   c3=files_of(ROOT, K.C3_RELAY), c3tool=files_of(ROOT, K.C3_PREDICT_TOOL), c4pred=files_of(ROOT, K.C4_PRED), c4=files_of(ROOT, K.C4_RELAY),
                   c5=files_of(ROOT, K.C5_RELAY), c6frozen=files_of(ROOT, K.C6_FROZEN), c6drafts=files_of(ROOT, K.C6_DRAFTS),
                   c6census=files_of(ROOT, K.C6_CENSUS), c6five=files_of(ROOT, K.C6_REBUILD_5), c6=files_of(ROOT, K.C6_RELAY),
#⟪END⟫
#⟪SECTION checks 10⟫
READFIRST_NEEDLES = ('relay data/b720_closing.txt |', 'relay data/b720_events.txt | whole', 'relay data/b720_defects.txt | :11 (e), :12 (f)',
                     'relay data/b720_registrations.txt |', 'relay data/b720_coeffs.txt | :57', 'relay data/b720_derivation.txt | :95-:121',
                     'relay data/b720_offset_price.txt | :1-:30 (whole) |', 'relay data/b720_pin.txt | :1-:66 (whole) |',
                     'relay data/b719_registrations.txt | :46-:59', 'relay data/b719_surgery.txt | :22', 'relay data/b716_registrations.txt (ii) at dc5e808f |',
                     'PLACE-papers REGISTRY.md :711-:745 |', 'PLACE-papers REGISTRY.md :1096-:1135', 'relay data/b721_ferry.txt | whole |',
                     'relay data/b721_citation_check.txt | whole |', 'relay data/act_roots.txt | :98 |', 'relay data/b716_federation_pin_price.txt | :1-:60 |',
                     'PLACE-papers SPIRAL_MAP.md | :104', 'relay data/standing_clauses_v7.txt |')
#⟪END⟫
#⟪SECTION checks 11⟫
CLOSING_SECTIONS = ('CORRIGENDUM ((R331)(1)-(2))', 'C2 TABLE ((R331)(3))', 'TABLE OVER h = 3, 4, 5 ((R331)(4))', 'OFFSET, POST HOC ((R331)(5))',
                    'SURGERY ((R331)(6))', 'FROZEN LINE ((R331)(7))', 'TOUCH READ (standing clauses v7)')
#⟪END⟫
#⟪SECTION checks 12⟫
    """the citation check's bank: every cite checked, OK and misses summing (78 = 75 + 3; the three misses -- b711's route with C1-C3 (C3
    absent), the federation pin's W-ORD entries (none: the pin named in trails, never as an order), b720's derivation :122-:125 beyond its end
    -- in the JSON bank's misses, each raised or entered before the component citing it); the bank written before the step-zero banks' commit
    and that commit before Component 1's (Component 8, the Edit tool: b720's figures 62 and 1 were b720's own)."""
#⟪END⟫
#⟪SECTION checks 13⟫
        and int(m.group(3)) == len(S['cit_misses']) == 3 and int(m.group(1)) == 78 \
#⟪END⟫
#⟪SECTION checks 14⟫
    # ### (Component 8, the Edit tool: b720's needles were b719's figures under b720's name)
    return landed(S, 0, ['b720 AT ITS WEIGHT', 'suite 111 of 116; root b5a76ed924905059…', 'the closing’s 8834a5b6', '29 defects'])
#⟪END⟫
#⟪SECTION checks 15⟫
TITLE_NEEDLES = ('## the C2 table at the discriminants its rule would choose: none -- every class-number-2 field’s least negative index at -2 '
                 'or -1/2, the halt proved', '; the table over h = 3, 4, 5 written and checked, two predictions registered (n0 = 80 at -31, 224 '
                 'at -55)', '; the offset’s post hoc rows, H-OFFSET refuted on its own first rows, and 0 new pairs registered', '; the surgery carried',
                 '; the frozen line’s statements quoted, its drafts for the release sitting', '; 6 of 6 wave 1 kernels build at their own pins, one '
                 'with a sorry', '; the federation pin closed')
#⟪END⟫
#⟪SECTION checks 16⟫
                      r'(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$', re.M)
#⟪END⟫
#⟪SECTION checks 17⟫
    """(R331)(2): the generated entry for b720's fifteen events and twenty-nine defects landed (its line in the bank, the title at that line
    through conv): the events by row (1)-(15), the defects by the one lettering ((a)-(z), (a`)-(c`)), no memory item; every item tagged CLAIM
    or CLOSE and NEW or REPEAT, the tags summing (CLAIM 2, CLOSE 42 over 44, REPEAT 28); the CLAIM items defects (e) and (f); the three repairs
    at tools/standing/ v1.2.1 with their thirteen cases; event (12)'s cause read again; the corrigenda bank appended at row (41) and nothing
    before it changed; in Component 1's commit."""
#⟪END⟫
#⟪SECTION checks 18⟫
        and len(lets) == len(dfs) == 29 and len(items) == j.get('items') == 44 and j.get('row') == 41 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 44 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 2 and claims == ['e', 'f'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 28 \
#⟪END⟫
#⟪SECTION checks 19⟫
        and (j.get('repairs') or {}).get('version') == 'v1.2.1' and (j.get('repairs') or {}).get('cases') == 13 \
        and 'not the listing' in (j.get('event12_cause') or '') \
        and '  (41) ' in S['corrigenda'] and '  (42) ' not in S['corrigenda'] \
#⟪END⟫
#⟪SECTION checks 20⟫
    worklist's SEALED naming no report tool. This act's rules banks (data/b721_rules.txt and data/b722_rules.txt, by form in (R331)(9)) are
#⟪END⟫
#⟪SECTION checks 21⟫
    b722's does not exist (Component 8, the Edit tool: b720's arm wanted neither)."""
#⟪END⟫
#⟪SECTION checks 22⟫
        and '  (1) NO FIGURE BEFORE ITS REGISTRATION.' in r1 and not re.search(r'(?m)^  \((?!1\))\d+\) ', r1) \
        and 'data/b721_rules.txt' in S['files']['c1'] and not os.path.exists(os.path.join(D, 'b722_rules.txt')) \
#⟪END⟫
#⟪SECTION checks 23⟫
REPORT_KEYS = ('KERNEL -- THE REBUILD AT EACH WAVE 1 KERNEL`S OWN PIN', 'CERTIFIED -- THE TABLE OVER CYCLIC h = 3, 4, 5 AT OMEGA 1-6',
               'CERTIFIED -- THE C2 RULE`S OUTPUT NONE', 'REGISTERED -- THE h = 3 AND h = 4 PREDICTIONS',
               'REGISTERED -- THE TABLE`S PREDICTIONS AT THE FOURTEEN UNUSED', 'HELD -- THE OFFSET, POST HOC', 'HELD -- THE FROZEN LINE',
#⟪END⟫
#⟪SECTION checks 24⟫
    """(R331)(7)(iii), N1, N4: the rebuild's order and hold -- every push, dispatch and read row with the host's free memory at or above the
    hold; per kernel its push before its run and its run before its read; six runs at most (dispatches and the push run), the refused one
    counted apart; the plan printed before the first push; each push and dispatch by its own command."""
#⟪END⟫
#⟪SECTION checks 25⟫
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and REBUILD_ROUTE.search(r['cmd'])]
    plan_ts = _first_ts(S['cmds'], lambda c: re.search(r'b721_rebuild\.py plan\b', c) is not None)
    push_ts = _first_ts(S['cmds'], lambda c: re.search(r'b721_rebuild\.py push\b', c) is not None)
#⟪END⟫
#⟪SECTION checks 26⟫
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == K.MAX_DISPATCHES and sum(1 for r in rows if r.get('kind') == 'dispatch_refused') == 1 \
        and bool(cmds) and all(len(REBUILD_ROUTE.findall(r['cmd'])) == 1 for r in cmds) \
        and plan_ts is not None and push_ts is not None and plan_ts < push_ts
#⟪END⟫
#⟪SECTION checks 27⟫
        and beyond == {'SIDE-frobenius': '2'} and set(st['SIDE-frobenius']['author'].split(NL)) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
#⟪END⟫
#⟪SECTION checks 28⟫
    """N5: PLACE-papers' changed files on main within the two ledgers (K.PP_WRITTEN: FINDINGS and OPEN_TRAILS), both changed; no rename."""
#⟪END⟫
#⟪SECTION checks 29⟫
ENTRY_NEEDLES = ('**The corrigendum and the repairs**', '**The C2 table’s test**', '**The table over h = 3, 4, 5 and two predictions**',
                 '**The offset, post hoc**', '**The surgery**', '**The frozen line**', '**The rebuild**', '**The federation pin, closed**',
                 '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**', '**Read in mutual light**',
                 '**Carried to:**', '**Next.**', 'data/b721_registrations.txt', 'data/b721_derivation.txt', 'data/b721_offset_read.txt',
                 'data/b721_offset_tier.txt', 'data/b721_surgery_carry.txt', 'data/b721_frozen_line_drafts.txt', 'data/b721_rebuild.txt',
                 'data/b721_touch.txt', 'The act’s counter CLAIM ')
#⟪END⟫
#⟪SECTION checks 30⟫
NAV_LETTERS = ('d', 'e')      # ### (d) event (12)'s cause as (R331)(1)-(2) names it, (e) (R331)(2)'s "at step zero" against the ferry's order; every other the seat's
#⟪END⟫
#⟪SECTION checks 31⟫
    """(R331)(3)(i), N2: data/b721_registrations.txt committed ALONE at C2_REG with the rule only (section (1)), before any discriminant is named
    -- no walk, no output, no prediction in the bank as committed there; the select tool committed alone after it and before its output
    (C2_SELECT); each later section added by a commit of the bank alone, the old bytes a prefix of the new (the halt at C2_HALT, rule (4) at
    C3_RULE, the predictions at C2_PRED), HEAD's bank equal to the predictions' commit; b716's, b718's, b719's and b720's registrations read
    unchanged from their commits (blob for blob at HEAD); the order by ancestry."""
    r = S['regs_at']
    z, h, r4, p = (r.get(k) or '' for k in ('c2reg', 'halt', 'rule4', 'pred'))
    t = S['regs_new'] or ''
    return S['files']['c2reg'] == [K.REGISTRATIONS_NEW] and S['files']['c2select'] == ['tools/b721_select.py'] \
        and _own(S['files']['c2halt']) == [K.REGISTRATIONS_NEW] and _own(S['files']['c3rule']) == [K.REGISTRATIONS_NEW] \
        and _own(S['files']['c2pred']) == [K.REGISTRATIONS_NEW] \
        and '## (1) THE RULE' in z and '## (2)' not in z and 'THE WALK' not in z \
        and h.startswith(z) and r4.startswith(h) and p.startswith(r4) and t == p and len(z) < len(h) < len(r4) < len(p) \
        and '## (2) THE RULE\'S OUTPUT: NONE' in h and '## (4) THE RULE FOR (R331)(4)\'S PREDICTIONS' in r4 and '## (5)' not in r4 \
        and len(S['reg_blobs']) == 4 and all(a is not None and a == b for a, b in S['reg_blobs'].values()) \
        and all(S['anc'].get(k) is True for k in ('reg_select', 'select_halt', 'halt_rule4'))
#⟪END⟫
#⟪SECTION checks 32⟫
    """(R331)(4), N2: the h = 3 and h = 4 predictions by rule (4) -- the rule committed (C3_RULE) before either discriminant is named, the
    prediction tool committed alone (C3_PREDICT_TOOL) before it ran, its print entered by a commit of the bank alone (C2_PRED): H-C3-31 n0 80,
    b -2 and H-C4-55 n0 224, b -2, each the model's own n0 beside the table's, each with its falsifier; nothing at -31 or -55 computed this
    act: no coefficient bank of b721 and no later commit touching the registrations."""
    p = S['regs_at'].get('pred') or ''
    r4 = S['regs_at'].get('rule4') or ''
    return all(S['anc'].get(k) is True for k in ('rule4_deriv', 'deriv_tool', 'tool_pred')) \
        and S['files']['c3tool'] == ['tools/b721_predict34.py'] and '-31' not in r4 and '-55' not in r4 \
        and 'H-C3-31' in p and 'n0 = 80 = 2^4 . 5' in p and 'b(80) = -2' in p and 'H-C4-55' in p and 'n0 = 224 = 2^5 . 7' in p and 'b(224) = -2' in p \
        and p.count('THE SAME n0') == 2 and 'FALSIFIER H-C3-31' in p and 'FALSIFIER H-C4-55' in p \
        and not [n for n in os.listdir(D) if n.startswith(('b721_coeffs', 'b721_prediction'))] \
        and gs(ROOT, 'log', '--format=%h', K.C2_PRED + '..HEAD', '--', K.REGISTRATIONS_NEW) == ''
#⟪END⟫
#⟪SECTION checks 33⟫
    """(R331)(3), N2: the C2 table tested -- HALTED AT (i), PROVED: the registrations' section (2) printing the controls first (S1-S3 as wanted),
    the walk over the eighteen class-number-2 fields each passed over or USED, the output NONE, the walk carried to |D| < 5000 finding no other
    field, and the positive control (the picker fires with only -2 excluded); no discriminant registered for a coefficient and no coefficient
    bank of this act; the halt carried to b722."""
    h = S['regs_at'].get('halt') or ''
    walk = re.findall(r'(?m)^  -(\d+)\s+(USED|n0 \d+)', h)
    return 'THE CONTROLS FIRST, ALL AS WANTED' in h and len(walk) == 18 and sum(1 for _d, x in walk if x == 'USED') == 3 \
        and 'THE OUTPUT: NONE.' in h and '|D| < 5000' in h and 'THE POSITIVE CONTROL' in h and 'carried to b722' in h \
        and h.find('THE CONTROLS FIRST') < h.find('THE WALK') < h.find('THE OUTPUT: NONE') \
        and not [n for n in os.listdir(D) if n.startswith('b721_coeffs')] and K.NEW_DISCRIMINANTS == ()
#⟪END⟫
#⟪SECTION checks 34⟫
    """(R331)(4), N3: the table over h = 3, 4, 5 -- checks (1) and (2) each before its step and AS WANTED, the table at Omega 1-6, check (4) at
    -23, -39 and -47 before any use of the table and AS WANTED; THE GRADE after the last step and in the foot, the foot's reading of check (4)
    the check's own; in Component 3's commit, after rule (4)'s and before the prediction tool's."""
    t = S['derivation'] or ''
    v = _verdict(t)
    c = re.findall(r'(?m)^## CHECK \((\d)\).* -- (AS WANTED|NOT AS WANTED)$', t)
    c4 = t[t.find('## CHECK (4)'):t.find('## THE GRADE')]
    return [x for x, _w in c] == ['1', '2'] and all(w == 'AS WANTED' for _x, w in c) and t.find('## CHECK (2)') < t.find('## STEP (3)') < t.find('## CHECK (4)') \
        and 'NOT AS WANTED' not in c4 and 'AS WANTED' in c4 and t.rfind('## THE GRADE') > t.rfind('## CHECK (4)') \
        and v.startswith('CHECKS (1) (2) (4): ALL AS WANTED ; PLANTS: ALL FAIL AS WANTED') and '-23, -39, -47 READ BY IT AS WANTED' in v \
        and 'OMEGA 1-6' in v and S['anc'].get('rule4_deriv') is True and S['anc'].get('deriv_tool') is True \
        and 'data/b721_derivation.txt' in S['files']['c3']
#⟪END⟫
#⟪SECTION checks 35⟫
    """(R331)(5), N3: the seventeen banked pairs under H-OFFSET -- delta_pred written from r and n*_pred alone and committed (C4_PRED) before any
    n* was read; every row of the read labelled POST HOC (seventeen), the plant refusing first, the foot's figures equal to the rows (HELD 3,
    REFUTED 14) and the grade POST HOC; the tier: the next pairs by r(rho) <= 0.05 chosen, no delta_pred formed, carried; no onset or pairs bank
    of this act; the read and the tier in Component 4's commit, after the prediction's."""
    t, pr, ti = S['offset'] or '', S['offset_pred'] or '', S['offset_tier'] or ''
    rows = re.findall(r'(?m)^  (POST HOC )?\| .*\| (HELD|REFUTED)$', t)
    return len(rows) == 17 and all(ph for ph, _v in rows) and sum(1 for _p, v in rows if v == 'HELD') == 3 \
        and 'POST HOC 17: HELD 3, REFUTED 14, NOT SCORABLE 0' in _verdict(t) and t.find('## THE PLANT') < t.find('## THE ROWS') \
        and 'ALL POST HOC' in _verdict(pr) and 'NO n* READ' in _verdict(pr) and 'CARRIED' in _verdict(ti) and 'delta_pred FORMED AT 0' in _verdict(ti) \
        and S['anc'].get('offset_read') is True and 'data/b721_offset_pred.txt' in S['files']['c4pred'] \
        and all(x in S['files']['c4'] for x in ('data/b721_offset_read.txt', 'data/b721_offset_tier.txt')) \
        and not [n for n in os.listdir(D) if n.startswith(('b721_onset', 'b721_pairs'))]
#⟪END⟫
#⟪SECTION checks 36⟫
    """(R331)(6): the surgery under H-SHAPE carried, not started -- its bank (b718's price against the budget after (5)) in Component 5's commit
    alone; H-SHAPE read unchanged in b719's registrations; no surgery tool and no operated-unit bank of this act; the next act's line naming
    the surgery."""
    b719 = (S['reg_blobs'].get('data/b719_registrations.txt') or (None, None))[1] or ''
    return 'H-SHAPE' in b719 and 'THE SURGERY CARRIED, NOT STARTED' in _verdict(S['surgery']) and _own(S['files']['c5']) == ['data/b721_surgery_carry.txt'] \
        and 'surgery' in K.NEXT and not [n for n in os.listdir(D) if n.startswith('b721_operated')] \
        and not [f for f in os.listdir(T) if f.startswith('b721_surgery')]
#⟪END⟫
#⟪SECTION checks 37⟫
    """(R331), the ferry: no arm retired this act, b720's run list of 116 binds -- tools/standing/arms.py byte-equal to its blob at the act's
    base, its RETIRED as b720 left it and arm_tags.json's retired record equal to it, none a guard; this suite's run list 116 arms, without
    them."""
#⟪END⟫
#⟪SECTION checks 38⟫
#⟪END⟫
#⟪SECTION checks 39⟫
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(a[0] for a in ARMS) and len(ARMS) == 116
#⟪END⟫
#⟪SECTION checks 40⟫
    """b719's price of the count law's route, read unchanged: data/b719_count_route_price.txt byte-equal to its blob at the act's base, its
    verdict the price and NOTHING BUILT; no count tool and no count bank of this act."""
    t = S['count_route'] or ''
    return bool(t) and S['count_route_now'] == S['count_route_pre'] and _verdict(t).startswith('THE ROUTE PRICED: 19,852 UNIT BANDS AT Q0') and 'NOTHING BUILT' in _verdict(t) \
        and not [f for f in os.listdir(T) if f.startswith('b721_count')] and not [n for n in os.listdir(D) if n.startswith('b721_count')]
#⟪END⟫
#⟪SECTION checks 41⟫
    """standing clauses v7, N4: the touch read banked as data/b721_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
#⟪END⟫
#⟪SECTION checks 42⟫
#⟪END⟫
#⟪SECTION checks 43⟫
    return bool(tags) and shift == (['G-R331-ENTERED'], ['G-R329-ENTERED']) and tags.get('G-R329-ENTERED') == 'CLOSE' \
#⟪END⟫
#⟪SECTION checks 44⟫
    return 'RULING (R331) END' in f and f.rstrip().endswith(K.TAIL) and have and 7 in named \
#⟪END⟫
#⟪SECTION checks 45⟫
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from ef648cb9',
#⟪END⟫
#⟪SECTION checks 46⟫
#⟪END⟫
#⟪SECTION checks 47⟫
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 78 = 75 OK + 3 misses (each raised or entered before the component citing it), the bank before the step-zero commit and that before Component 1`s',
#⟪END⟫
#⟪SECTION checks 48⟫
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b720-closing (8834a5b6)', 'push-b720-closing'))),
#⟪END⟫
#⟪SECTION checks 49⟫
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the C2 rule choosing none, the halt proved; the table over h = 3, 4, 5 and the predictions at -31 and -55; the offset post hoc, 0 new pairs; the surgery carried; the frozen line and its drafts; 6 of 6 wave 1 kernels building, one with a sorry; the federation pin closed), compared after case-folding the article alone',
#⟪END⟫
#⟪SECTION checks 50⟫
    ('G-CORRIGENDUM-ENTERED', '(R331)(2): the generated corrigendum for b720`s record, landed at FINDINGS :11110: its fifteen events and twenty-nine defects, 44 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 2 CLOSE 42, REPEAT 28; event (12)`s cause the branch and the push in one message, not the listing; v1.2.1`s repairs, 13 cases; the corrigenda bank appended at row (41)',
#⟪END⟫
#⟪SECTION checks 51⟫
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); this act`s rules bank carrying (R331)(1)`s row alone, in Component 1`s commit; no b722 rules bank',
#⟪END⟫
#⟪SECTION checks 52⟫
    ('G-REGISTRATIONS-FIRST', '(R331)(3)(i), N2: data/b721_registrations.txt committed alone at 54be7b0b with the rule only, before any discriminant; the select tool alone at cdb59caa before it ran; the rule`s output (2), rule (4) and the predictions (5) each by a commit of the bank alone, each the last`s bytes extended, HEAD`s equal to the last; b716`s to b720`s registrations at their commits blob for blob at HEAD',
     lambda S: registrations_first_ok(S), lambda S: _mut(S, 'regs_at', lambda d: d.update(c2reg=(d.get('c2reg') or '') + NL + '  PRED-35: n0(-35) = 135'))),
    ('G-PREDICTION-FIRST', '(R331)(4), N2: the h = 3 and h = 4 predictions by rule (4) (5febd903, naming neither discriminant), the predict tool alone at be19ff52 before it ran, the predictions at e8c3dff4: H-C3-31 n0 80, b -2 and H-C4-55 n0 224, b -2, the model naming the same n0, each with its falsifier; no coefficient bank of b721 and no later commit of the registrations',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'anc', lambda d: d.update(tool_pred=False))),
    ('G-COEFFS-LAW', '(R331)(3), N2: the C2 table`s test HALTED AT (i), PROVED -- the registrations` section (2): the controls first, the walk over the eighteen class-number-2 fields (3 USED), the output NONE, the walk to |D| < 5000 finding no other, the positive control; no coefficient bank of b721, no discriminant registered; carried to b722',
     # ### event (8), before the seal, the Edit tool: the carried plant mutated b720's coefficient bank (no key this act); the plant now the halt's output
     lambda S: coeffs_law_ok(S), lambda S: _mut(S, 'regs_at', lambda d: d.update(halt=(d.get('halt') or '').replace('THE OUTPUT: NONE.', 'THE OUTPUT: -84.')))),
    ('G-DERIVATION-GRADED', '(R331)(4), N3: the table over h = 3, 4, 5 at Omega 1-6 -- checks (1) and (2) before their steps, check (4) at -23, -39 and -47 before any use, each AS WANTED; THE GRADE after the last check and in the foot; in Component 3`s commit b5e232af, after rule (4)`s and before the predict tool`s',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'derivation', (S['derivation'] or '').replace('## THE GRADE', '## A GRADE'))),
    ('G-OFFSET-POST-HOC', '(R331)(5), N3: the seventeen under H-OFFSET POST HOC -- delta_pred committed at 0ee39dc6 before any n* read; every row of the read POST HOC, the plant refusing first, HELD 3, REFUTED 14; the tier 53 chosen, 0 formed, carried; the read and the tier at 3482af9b; no onset or pairs bank of b721',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'offset', (S['offset'] or '').replace('POST HOC', 'AT ONCE'))),
    ('G-SURGERY-CARRIED', '(R331)(6): the surgery under H-SHAPE (965cb8e8) carried, not started -- data/b721_surgery_carry.txt alone in Component 5`s commit bddd46f1; H-SHAPE in b719`s registrations at its commit; no surgery tool and no operated-unit bank of b721; the next act`s line naming it',
     lambda S: surgery_carried_ok(S), lambda S: _mut(S, 'reg_blobs', lambda d: d.update({'data/b719_registrations.txt': (None, '')}))),
    ('G-ARMS-RETIRED', 'the ferry: no arm retired this act, b720`s run list of 116 binds -- tools/standing/arms.py byte-equal to its blob at 8834a5b6, its RETIRED equal to arm_tags.json`s retired record, none a guard; this suite`s run list 116 arms without them',
#⟪END⟫
#⟪SECTION checks 53⟫
    ('G-COUNT-ROUTE-PRICED', 'b719`s price of the count law`s route read unchanged (data/b719_count_route_price.txt byte-equal at 8834a5b6, its verdict NOTHING BUILT); no count tool and no count bank of b721',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'count_route', (S['count_route'] or '').replace('NOTHING BUILT', 'A TOOL BUILT'))),
    ('G-DIFFERS-ERRATA', '(R331)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal at b826da8c, no b721 differs or errata bank, the worklist naming none; the weight line and the corrigendum in Component 1`s PLACE-papers commit af7d8f3b, FINDINGS the one file there',
#⟪END⟫
#⟪SECTION checks 54⟫
    ('G-TOUCH-READ', 'standing clauses v7, N4: data/b721_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
#⟪END⟫
#⟪SECTION checks 55⟫
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the one act shift (G-R331-ENTERED in the suite, G-R329-ENTERED CLOSE in the file), the claim arms thirty-eight; the file byte-equal at 8834a5b6 (outside (R331)(9)`s (W) list)',
#⟪END⟫
#⟪SECTION checks 56⟫
    ('G-RUNNER-READ', '(R331)(7)(iii), N1: the rebuild read by its run ids -- one run per wave 1 kernel, six, each read once with its build exit; the head`s figures equal to its rows; the one sorry printed by its axiom line and graded builds and is not complete; SIDE-frobenius`s refused dispatch, its halt with its control, and its push run on the author`s two lines',
#⟪END⟫
#⟪SECTION checks 57⟫
    ('G-RUNNER-GATE', '(R331)(7)(iii), N1, N4: the rebuild`s order and hold -- free memory at or above 2,560 MB at every push, dispatch and read; per kernel push before run before read; six runs at most, the refused one apart; the plan before the first push; one push or dispatch per command',
#⟪END⟫
#⟪SECTION checks 58⟫
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each wave 1 kernel`s rebuild-b721 at its pin (the tagged commit, its one tag) or, SIDE-frobenius alone, two commits beyond it by the seat`s neutral identity, off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
#⟪END⟫
#⟪SECTION checks 59⟫
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the two ledgers and the merged document alone ((R330)(3)(ii)); no rename (N5)',
#⟪END⟫
#⟪SECTION checks 60⟫
    ('G-PRIOR-CLOSED-PUSHED', 'b720`s trail record on OPEN_TRAILS (:16218) and its root in the chain', lambda S: '### b720 — lane two, act one hundred and forty-seven, the decomposition act under (R330)' in S['ot']
#⟪END⟫
#⟪SECTION checks 61⟫
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and the merged keystone): beyond %s' % (
#⟪END⟫
#⟪SECTION checks 62⟫
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b720`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches this act %d (N1: (R331)(7)(iii)`s rebuild alone, six at most)' % (
#⟪END⟫
#⟪SECTION checks 63⟫
           'C1_RELAY', 'C1_PP', 'C2_REG', 'C2_PRED', 'C2_CTL', 'C2_RELAY', 'C3_RELAY', 'C4_REG', 'C4_RELAY', 'C5_REG', 'C5_RELAY', 'C6_RELAY')
#⟪END⟫
#⟪SECTION citation 1⟫
    hq = _quote(text, '"b720 closed: relay 6d7cb5f7', '; 29 defects"')
    add('ruling (1)', 'data/b720_closing.txt :1, the head line as the ruling quotes it', bool(hq) and hq[1:] + '; 29 defects' == at(cl, 1),
        at(cl, 1)[:120], '1')
    add('ruling (1)', 'the counter CLAIM 2, CLOSE 42 (data/b720_closing.txt :5)', at(cl, 5).endswith('CLAIM 2, CLOSE 42'), at(cl, 5)[-30:], '1')
    st = _jl('b720_steps.json').get('rows') or []
    r38 = [r for r in st if (r.get('commit') or '').startswith('8834a5b6')]
    add('ruling (1)', 'the closing commit 8834a5b6 at step 38, pushed and read back', len(st) == 38 and len(r38) == 1 and r38[0].get('phase') == 'closing'
        and (_remote_heads('D:/relay').get('refs/heads/main') or '').startswith('8834a5b6'), 'rows %d ; 8834a5b6 %s ; remote main %s' % (
            len(st), [r.get('phase') for r in r38], (_remote_heads('D:/relay').get('refs/heads/main') or '')[:8]), '1')
    cf = [l for l in cl if '(R330)(2) : THE CLAIM ARMS PASSING' in l]
    add('ruling (1)', 'the suite 111 of 116 and the claim arms 36 of 38 on both runs (data/b720_closing.txt)', len(cf) == 2 and all(
        '36 OF 38' in l and '111 OF 116' in l for l in cf), '%d lines' % len(cf), '1')
    rl = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    rb = lines_of(p('data', 'b720_root_banks.txt'))
    add('ruling (1)', 'the root b5a76ed9 over 103 banks, chained from 09e524a7 (data/act_roots.txt, data/b720_root_banks.txt)',
        bool(rl) and rl[-1][0] == 'b720' and rl[-1][1].startswith('b5a76ed9') and rl[-1][2].startswith('09e524a7') and any(re.search(r'\b103\b', l) for l in rb),
        'last row %s' % ' '.join(x[:8] for x in (rl[-1] if rl else [])), '1')
    ch = [l for l in lines_of(p('data', 'b720_checks_postpush_standing-b3.txt')) if 'THE ACT-ROOT CHAIN`S PART B' in l]
    add('ruling (1)', 'the root recomputed equal (the post-push chain part, b720 AGREE)', bool(ch) and 'b720 AGREE' in ch[0] and 'DIFFER' not in ch[0], '%d line' % len(ch), '1')
    sc = _jl('b720_scores_close.json')
    add('ruling (1)', 'N5 REFUTED at the close (data/b720_scores_close.json), event (12)', (sc.get('N5') or [''])[0] == 'REFUTED',
        str((sc.get('N5') or [''])[0]), '1')
#⟪END⟫
#⟪SECTION citation 2⟫
#⟪END⟫
#⟪SECTION citation 3⟫
    tags = [m.group(1) for m in (re.search(r'\[(CLAIM|CLOSE) ; ', l) for l in ev if re.match(r'^    \(\d+\) ', l)) if m]
    e12 = [l for l in ev if l.startswith('    (12) ')]
    add('ruling (1)', 'event (12): the scorer counting git branch --list as a write', bool(e12) and 'git branch --list' in ' '.join(ev[ev.index(e12[0]):ev.index(e12[0]) + 9]),
        (e12 or [''])[0][:80], '1')
#⟪END⟫
#⟪SECTION citation 4⟫
    add('ruling (1), (2)', 'the counter over 29 defects and 15 events, each tagged (data/b720_defects.txt, data/b720_events.txt)',
        len(letters) == 29 and starts == list(range(1, 16)) and len(tags) == 15, 'letters %d ; events %s ; tagged %d' % (len(letters), starts[-1:], len(tags)), '1')
    mi = lines_of(p('data', 'b720_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-28-b720.zip, 74 files, CLEAN on all three clauses with the root line (data/b720_mirror.txt)',
        any('mirror-refresh-2026-10-28-b720.zip' in l for l in mi) and any('files 74' in l for l in mi) and any(l.endswith('Act root: b720 ' + K.B714_ROOT) for l in mi)
        and any('CLEAN ON ALL THREE CLAUSES' in l for l in mi), 'zip %s' % os.path.exists(K.MIRROR_ZIP), '1')
    add('ruling (1)', 'the FINDINGS entry at :11072 carrying the author`s title wording', at(fi, 11072).startswith('## The coefficient law at -35 and -40')
        and 'the law’s value clause REFUTED at -40 (b = -1/2), its prime clause HELD at both' in at(fi, 11072), at(fi, 11072)[:80], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :16218', at(ot, 16218).startswith('### b720 — lane two, act one hundred and forty-seven'), at(ot, 16218)[:80], '1')
    co = lines_of(p('data', 'b720_coeffs.txt'))
    for needle in ('n0(-35) = 135, b = -2 ; n0(-40) = 100, b = -1/2', 'H-DECOMP HELD', 'PRED-35 HELD, PRED-40 HELD', 'FORCED 2 APART'):
        add('ruling (1)', 'data/b720_coeffs.txt :57: %s' % needle, needle in at(co, 57), at(co, 57)[:90], '1')
    dv = lines_of(p('data', 'b720_derivation.txt'))
    for n, needle in ((103, '## THE GRADE'), (107, 'THEOREM, WITH ITS HYPOTHESES'), (109, 'those of value -2 are R . R . R . R, R^2 . R . S, R^2 . S^2, S^3 . R'),
                      (109, 'R^2 . R^2 (-1/2)'), (114, 'THE STEP THAT REMAINS THERE, NAMED'), (118, 'Clause 2 holds at the seven'),
                      (120, 'THE -2 OF BOTH CONFIGURATIONS A THEOREM IN C2 AT OMEGA 4')):
        add('ruling (1)', 'data/b720_derivation.txt :%d: %s' % (n, needle), needle in at(dv, n), at(dv, n)[:90], '1')
    rd_ = run_numstat('D:/MY-DOwnloads/PLACE-papers', 'b92bb70a', '5872b897', 'REGISTRY.md')
    add('ruling (1)', 'REGISTRY appended at 5872b897, 0 lines removed', bool(rd_) and rd_[1] == 0, 'added %s removed %s' % (rd_ or ('-', '-')), '1')
    chl = rd(p('data', 'b720_challenge.txt')) or ''
    add('ruling (1)', 'the challenge file ELABORATES, run 40651875792 (data/b720_challenge.txt)', 'ELABORATES' in chl and '40651875792' in chl, 'the bank', '1')
    pn = lines_of(p('data', 'b720_pin.txt'))
    add('ruling (1)', 'the pin at 1 of 6 eligible (data/b720_pin.txt :7)', at(pn, 7).startswith('THE PIN AT 1 OF 6 ELIGIBLE'), at(pn, 7)[:60], '1')
    add('ruling (1)', 'defect (e) at data/b720_defects.txt :11, a CLAIM', at(dl, 11).startswith("    (e) THE SEAT'S [CLAIM ; NEW]"), at(dl, 11)[:60], '1')
    add('ruling (1)', 'b716`s registration (ii) at dc5e808f', '(ii)' in _blob('D:/relay', 'dc5e808f', 'data/b716_registrations.txt'), 'the blob at dc5e808f', '1')
    # ### (R331)(2): the corrigendum's sources and the three repairs' objects
    add('ruling (2)', 'tools/standing/ at v1.2.0 entering the act (tools/standing/VERSION); v1.2.1 to be written by (2)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.2.0',
#⟪END⟫
#⟪SECTION citation 5⟫
    ck = rd(p('tools', 'b720_checks.py')) or ''
    add('ruling (2)(i)', 'G-FINDINGS-ENTRY and G-ENTRY-TITLE-FORM, two claim arms, and the author`s answers bank (data/b720_author_answers.txt)',
        'G-FINDINGS-ENTRY' in ck and 'G-ENTRY-TITLE-FORM' in ck and os.path.exists(p('data', 'b720_author_answers.txt')),
        'tools/b720_checks.py', '1')
    add('ruling (2)(ii)', 'the one-git-write rule (tools/rule_arms.py, G-RULE-ONE-GIT-WRITE)', 'ONE-GIT-WRITE' in (rd(p('tools', 'rule_arms.py')) or ''), 'tools/rule_arms.py', '1')
    add('ruling (2)(iii)', 'the MANIFEST control`s reference a86c9429 (tools/b720_worklist.py RECUT_MERGE), stale from b716 to b720 (events: b716-b719 and b720 (15))',
        "RECUT_MERGE = 'a86c9429" in (rd(p('tools', 'b720_worklist.py')) or '') and any(l.startswith('    (15) ') and 'NOT AS WANTED' in ' '.join(ev[ev.index(l):ev.index(l) + 4]) for l in ev),
        'tools/b720_worklist.py', '1')
    add('ruling (2)(iii)', '(R328)(7)`s toolset diff (data/b718_carry_standing.txt)', os.path.exists(p('data', 'b718_carry_standing.txt')), 'present', '1')
    # ### (R331)(3): the C2 table and b711's route
#⟪END⟫
#⟪SECTION citation 6⟫
    add('ruling (3)', 'b711`s route (tools/b711_coeffs.py) through the cut 32532 with its controls C1-C3', '32532' in src and all(c_ in src for c_ in ('C1', 'C2', 'C3'))
        and bool(re.search(r'\bC1\b', src)) and bool(re.search(r'\bC3\b', src)), 'C1 %s ; C3 %s' % (bool(re.search(r'\bC1\b', src)), bool(re.search(r'\bC3\b', src))), '2')
    add('ruling (3)', 'the cut 32532 in b720`s coefficients (data/b720_coeffs.txt)', any('32532' in l for l in co), 'the bank', '2')
    add('ruling (3)(i)', 'the C2 table of data/b720_derivation.txt (step (6), the table of 20 rows)', any(l.startswith('## STEP (6)') for l in dv) and 'the table of 20 rows' in ' '.join(dv),
        'the bank', '2')
    # ### (R331)(4): the step at h > 2 and the three checks
    add('ruling (4)', 'data/b720_derivation.txt :113: -23 (C3), -39 (C4) and -47 (C5)', 'At -23 (C3), -39 (C4) and -47 (C5)' in at(dv, 113), at(dv, 113)[:80], '3')
    add('ruling (4)', 'b719`s step (1), its turns (data/b719_derivation.txt)', any(l.startswith('## STEP (1)') for l in lines_of(p('data', 'b719_derivation.txt'))), 'the bank', '3')
    # ### (R331)(5): the offset
    op = lines_of(p('data', 'b720_offset_price.txt'))
    add('ruling (5)', 'data/b720_offset_price.txt: the seventeen banked pairs, post hoc (:11)', 'THE SEVENTEEN BANKED PAIRS, POST HOC' in at(op, 11), at(op, 11)[:80], '4')
    r19 = lines_of(p('data', 'b719_registrations.txt'))
    add('ruling (5)', 'H-OFFSET`s falsifier at r(rho) <= 0.05 (data/b719_registrations.txt :53)', 'r(rho) <= 0.05' in at(r19, 53), at(r19, 53)[:80], '4')
    add('ruling (5)(ii)', 'b709`s route (tools/b709_pairs.py)', os.path.exists(p('tools', 'b709_pairs.py')), 'present', '4')
    # ### (R331)(6): the surgery
    add('ruling (6)', 'H-SHAPE at 965cb8e8 (data/b719_registrations.txt)', 'H-SHAPE' in _blob('D:/relay', '965cb8e8', 'data/b719_registrations.txt'), 'the blob at 965cb8e8', '5')
    add('ruling (6)', 'b718`s price (data/b718_surgery_price.txt)', os.path.exists(p('data', 'b718_surgery_price.txt')), 'present', '5')
    add('ferry (read first)', 'data/b719_surgery.txt :22', 'H-SHAPE REGISTERED AT 965cb8e8' in at(lines_of(p('data', 'b719_surgery.txt')), 22),
        at(lines_of(p('data', 'b719_surgery.txt')), 22)[:80], '5')
    # ### (R331)(7): the frozen line -- each wave 1 kernel's pin, its Mathlib, its workflow; the four statements at their tags
    for k_, tag_, short_ in K.WAVE1:
        kp = 'D:/' + k_
        c_ = gr(kp, 'rev-parse', '--verify', '--quiet', tag_ + '^{commit}')
        man = _blob(kp, tag_, 'lake-manifest.json')
        add('ruling (7)', '%s %s = %s, its own lake-manifest.json at the pin' % (k_, tag_, short_), c_.startswith(short_) and 'mathlib' in man,
            '%s ; manifest %d bytes' % (c_[:12], len(man)), '6')
    for k_, nm_ in K.CHECKPOINT_STATEMENTS:
        tag_ = dict((a_, b_) for a_, b_, _c in K.WAVE1)[k_]
        fs = _decl_files('D:/' + k_, tag_, nm_)
        add('ruling (7)(i)', '%s declared at %s %s' % (nm_, k_, tag_), len(fs) == 1, ', '.join(fs) or 'NOT FOUND', '6')
    add('ruling (7)(iii)', 'SIDE-explicit-formula`s workflow file (.github/workflows/build-module.yml at main)', bool(_blob(K.EF_DIR, 'main', '.github/workflows/build-module.yml')),
        'present at main', '6')
    sml = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (7)(ii)', 'SPIRAL_MAP :104`s sentence (SPIRAL_MAP.md :104, the Phase 1.2 checkpoint kernels)', 'The Phase 1.2 checkpoint kernels' in at(sml, 104), at(sml, 104)[:80], '6')
    rg = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ferry (read first)', 'REGISTRY`s PHASE 1.2 -- FROZEN block (REGISTRY.md :711)', 'PHASE 1.2 — FROZEN' in at(rg, 711), at(rg, 711)[:60], '6')
    add('ferry (read first)', 'REGISTRY`s attribute block at 5872b897', bool(_blob('D:/MY-DOwnloads/PLACE-papers', '5872b897', 'REGISTRY.md')), 'the blob at 5872b897', '6')
    # ### (R331)(8): the federation pin at its banked state
    pj = ' '.join(pn)
    add('ruling (8)', 'SIDE-effects builds at de5ce8a9 (b718`s run, data/b720_pin.txt :9)', 'SIDE-effects' in at(pn, 9) and 'BUILDS' in at(pn, 9), at(pn, 9)[:70], '7')
    add('ruling (8)', 'SIDE-simplicity builds; SIDE-grh-transfer, SIDE-kernel, SIDE-trivium and SIDE-lv-conservation break; SIDE-interfaces on a missing Kernel.lean',
        tuple(K.PIN_BUILDS) == ('SIDE-simplicity',) and set(K.PIN_HELD) == {'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium'}
        and 'SIDE-interfaces/Kernel.lean' in pj, 'the bank and the worklist', '7')
    lvb = gr('D:/SIDE-lv-conservation', 'rev-parse', 'pin-b718-de5ce8a9^')
    add('ruling (8)', 'SIDE-lv-conservation`s bump branch cut from main (its parent d38f3e8c)', lvb.startswith('d38f3e8c'), lvb[:12], '7')
    add('ruling (8)', 'its port at cb0aea56, tag v0.14.0, built at de5ce8a9 (b712)', gr('D:/SIDE-lv-conservation', 'rev-parse', 'v0.14.0^{commit}').startswith('cb0aea56')
        and 'de5ce8a9' in (rd(p('data', 'b712_closing.txt')) or ''), 'v0.14.0 %s' % gr('D:/SIDE-lv-conservation', 'rev-parse', 'v0.14.0^{commit}')[:8], '7')
    a15 = rd(p('data', 'b715_author_answers.txt')) or ''
    add('ruling (8)', 'the author`s answer at b715: each kernel`s pin the revision its own lake-manifest.json carries (data/b715_author_answers.txt)',
        'each kernel’s pin is the revision its own lake-manifest.json carries' in a15, 'the bank', '7')
    wo = [i + 1 for i, l in enumerate(ot) if re.search(r'THE ORDER \*\*`W-ORD-[A-Z0-9-]*(PIN|FEDERATION|BUMP|MATHLIB)', l) and 'PROSE-PINS' not in l and 'STATEMENT-PIN' not in l]
    add('ruling (8)', 'W-ORD entries for the federation pin in OPEN_TRAILS, to be annotated CLOSED', bool(wo), 'orders found %s (the pin named in trails :16056, :16124, :16142, '
        'never as an order)' % (wo or 'NONE'), '7')
    # ### (R331)(9): the carried files and branches
#⟪END⟫
#⟪SECTION citation 7⟫
        add('ruling (9)', 'the push-b720-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
#⟪END⟫
#⟪SECTION citation 8⟫
    add('ruling (9)', 'b720`s closing capture untracked and its step-38 row uncommitted', '?? data/b720_relay_push-b720-closing_push_out.txt' in stc
#⟪END⟫
#⟪SECTION citation 9⟫
    add('ruling (9)', 'port-b707 kept (SIDE-lv-conservation, at cb0aea56)', gr('D:/SIDE-lv-conservation', 'rev-parse', 'port-b707').startswith('cb0aea56'), 'local', '0')
#⟪END⟫
#⟪SECTION citation 10⟫
    r20 = lines_of(p('data', 'b720_registrations.txt'))
    for n, needle in ((7, 'a hand reading at -40 preceded this bank'), (24, "## THE SEAT'S DECLARATION"), (32, 'the row says so'), (79, '## H-RR'),
                      (97, 'PRED-35: n0(-35) = 135')):
        add('ferry (read first)', 'data/b720_registrations.txt :%d: %s' % (n, needle), needle in at(r20, n), at(r20, n)[:80], '0')
    add('ferry (read first)', 'data/b720_derivation.txt (:95-:125)', len(dv) >= 125, 'the bank has %d lines; :95-:%d read, :%d-:125 beyond its end' % (
        len(dv), len(dv), len(dv) + 1), '0')
    add('ferry (read first)', 'data/b719_registrations.txt :46-:59, H-OFFSET', 'H-OFFSET, POST HOC' in at(r19, 46) and 'THE ORDER IT SERVES' in at(r19, 59), at(r19, 46)[:60], '0')
    add('ferry (read first)', 'data/b720_defects.txt (f)', at(dl, 12).startswith("    (f) THE SEAT'S [CLAIM ; NEW]"), at(dl, 12)[:50], '0')
#⟪END⟫
#⟪SECTION citation 11⟫
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
#⟪END⟫
#⟪SECTION citation 12⟫
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R331)(2))' % (v, v), True, 'absent, as ordered', '0')
#⟪END⟫
#⟪SECTION closing 1⟫
tool) are the corrigendum and v1.2.1's repairs, the C2 table (the rule's output NONE), the table over h = 3, 4, 5 and its predictions, the
offset post hoc and its tier, the surgery carried, the frozen line (its statements, its drafts, the rebuild), the touch read and the standing
arms, each row by its bank's verdict line or by the line its pattern names (section_reading); (R331)'s counter line beneath the title and the
claim arms' figure beside the suite's in the commits section; the author's word after the seal printed from its bank (tools/act_close.py
author_words_section, v5 row (74)); the carried items of (R331)(11) for b722. The standing report prints its lines in footing order (KERNEL,
#⟪END⟫
#⟪SECTION closing 2⟫
tool's scores route and written nowhere. No kernel's main written this act: the rebuild-b721 branches of the six wave 1 kernels pushed.
#⟪END⟫
#⟪SECTION closing 3⟫
    """the carried items for b722 ((R331)(11)), and (R331)(8)'s federation pin closed at its banked state -- its holds and builds from the
    worklist's lists, read against b720's pin bank's head (relay data/b720_pin.txt), nothing carried (Component 8; b720's item carried the pin)."""
    head = re.search(r'(?m)^THE PIN AT [^\n]*', rd('b720_pin.txt') or '')
    pin = ['    (g) The federation pin, CLOSED ((R331)(8)) at its banked state (relay data/b720_pin.txt%s): %d held as breaks on their %s branches, '
           'nothing repaired -- %s; %d excluded, never pushed -- %s; %d building -- %s; each kernel cited at the Mathlib its own manifest '
           'carries, the readiness test for a wave the rebuild at its own pins.' % (
               (', "%s"' % ' '.join(head.group(0).split()[:12])) if head else ', ### HEAD NOT FOUND', len(WL.PIN_HELD), WL.PIN_BRANCH,
               ', '.join(WL.PIN_HELD) or 'NONE', len(WL.PIN_EXCLUDED), ', '.join(WL.PIN_EXCLUDED) or 'NONE', len(WL.PIN_BUILDS),
               ', '.join(WL.PIN_BUILDS) or 'NONE')]
    return CARRIED_FIXED + pin
#⟪END⟫
#⟪SECTION closing 4⟫
TITLE_LINE = ('b721 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE HUNDRED AND FORTY-EIGHT, THE TABLE ACT: b720 AT ITS WEIGHT AND ITS '
              'CORRIGENDUM; THE C2 TABLE`S TEST HALTED AT ITS RULE, PROVED; THE TABLE OVER h = 3, 4, 5 AND TWO PREDICTIONS REGISTERED; THE OFFSET`S '
              'SEVENTEEN POST HOC; THE SURGERY CARRIED; THE FROZEN LINE QUOTED, DRAFTED AND REBUILT AT ITS OWN PINS; THE FEDERATION PIN CLOSED, '
              'UNDER (R331).**')
#⟪END⟫
#⟪SECTION closing 5⟫
    """the act's sections over this act's banks (Component 8, the Edit tool; b720's sections over b720's objects -- the law at -35 and -40,
    the REGISTRY cells, the challenge, the pin -- not carried). A row of two reads its bank's verdict line by vtail; a row of three reads the
    line its pattern names (a bank written by the Write tool or a route printing its result in its text carries no verdict line's form)."""
#⟪END⟫
#⟪SECTION closing 6⟫
                ('v1.2.1`s three repairs, each controlled on b720`s banks', 'b721_standing_v121.txt'),
#⟪END⟫
#⟪SECTION closing 7⟫
            ('THE C2 TABLE ((R331)(3))', [
                ('the rule committed alone, its output NONE over the class-number-2 fields, the positive control (N2)', 'b721_registrations.txt',
                 r'(?m)^THE OUTPUT: NONE\.[^\n]*')]),
            ('THE TABLE OVER h = 3, 4, 5 ((R331)(4))', [
                ('the table at Omega 1-6, each check before its step, the grade at the end', 'b721_derivation.txt'),
                ('the predictions by rule (4), committed before anything at -31 or -55', 'b721_registrations.txt', r'(?m)^  THE WALK: h = 3:[^\n]*')]),
            ('THE OFFSET, POST HOC ((R331)(5))', [
                ('the seventeen`s delta_pred from r and n*_pred alone, no n* read', 'b721_offset_pred.txt'),
                ('the observed n* beside it, every row POST HOC', 'b721_offset_read.txt'),
                ('the next tier by r(rho) <= 0.05 alone, carried', 'b721_offset_tier.txt')]),
            ('THE SURGERY ((R331)(6))', [
                ('the surgery under H-SHAPE, carried, not started', 'b721_surgery_carry.txt')]),
            ('THE FROZEN LINE ((R331)(7))', [
                ('the statements quoted at their pins, graded by E0, the sentences graded against them', 'b721_frozen_line.txt'),
                ('the drafts for the release sitting, in the relay alone', 'b721_frozen_line_drafts.txt'),
                ('the rebuild at each wave 1 kernel`s own pin, each run read by its id', 'b721_rebuild.txt')]),
            ('THE TOUCH READ (standing clauses v7)', [
#⟪END⟫
#⟪SECTION closing 8⟫
    '    kernels written: no kernel`s main touched and no tag cut ((R331)(7), N5) ; the branch rebuild-b721 pushed on the six wave 1 kernels,',
    '    SIDE-kernel, -lv-conservation, -archimedean, -spinor and -rcurve at their pins (the tagged commits, already on main), SIDE-frobenius at',
    '    two commits beyond its pin by the seat`s neutral identity (SIDE-explicit-formula`s build-module.yml copied verbatim, then the author`s',
    '    two lines: the push trigger and the fixed target), off its main, untagged ; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved,',
    '    the challenge branch challenge-b720-h2-sign-iff-rh standing as b720 left it ; the pin-b718-de5ce8a9 branches left as banked ;',
    '    port-b707 of SIDE-lv-conservation at b712`s tip cb0aea56, KEPT, its tag v0.14.0 unmoved ; SIDE-lv-conservation`s main and its',
    '    deposit v0.10.0 unmoved ; SIDE-faces-join`s main 11a472b9 with its tag v0.1.0 unmoved ; N1: no lean or lake process on this host ;',
    '    six runs (five dispatches and SIDE-frobenius`s run on push), one dispatch refused, each run read by its id, free memory read before',
    '    each push, dispatch and read ; the push-b720-* branches of relay and PLACE-papers deleted at step zero by name after --merged listed',
    '    them, one per command and each its own message ; nothing vendored ; no worktree made or removed ; b628`s local intake bank, the',
    '    navigator`s export, b671`s uncompressed points file and the earlier acts` units files untracked ; N2: data/b721_registrations.txt',
    '    committed alone with the rule (54be7b0b) before any discriminant was named, its output, rule (4) and the predictions each by a commit',
    '    of its own ; nothing at -31 or -55 computed ; no identifier of the author in any outbound request header, URL, input or payload, or',
    '    in any workflow file ; no secret added ; the seat`s plain requests to github.com (its git reads and pushes, gh with its own token)',
    '    the act`s outbound calls ; the deposit route untouched, publish never called, the draft held at v5 ; on PLACE-papers main FINDINGS',
    '    and OPEN_TRAILS appended (the weight line, the corrigendum, the entry and the trail) ; no paper cut, moved or renamed ; no ERRATA,',
    '    FOUNDATIONS, REGISTRY, README or faces page byte ; data/act_roots.txt and the corrigenda bank appended ; data/act_current.json written',
    '    at step zero ; data/arm_tags.json unedited ; tools/standing/ at v1.2.1 by (R331)(2) ; the hook in D:/.claude/settings.json unedited ;',
    '    the per-act tools of b698-b720 unedited ; the mirror zip written outside every repository over the roster read from PLACE-papers',
    '    main, the builder`s state file tools/mirror_prevbuild.json written at the build and named in (W) ; nothing of TECHNE or any patent',
    '    written',
#⟪END⟫
#⟪SECTION closing 9⟫
    '    (a) ### **THE NEXT ACT, (R331)(11)**: b722: the h = 3 and h = 4 discriminants computed under (4)`s commit (relay',
    '        data/b721_registrations.txt (5), e8c3dff4); the offset`s pairs and the surgery where (5)-(6) carried them (relay',
    '        data/b721_offset_tier.txt, data/b721_surgery_carry.txt); the release sitting`s front-door list assembled from (7)(ii) and the',
    '        edits already planned (relay data/b721_frozen_line_drafts.txt).',
#⟪END⟫
#⟪SECTION closing 10⟫
    '        W-ORD-E0-MET-CLASSK; W-ORD-README-FIGURE-SCOPE. None annotated this act; the federation pin, never an order, closed as a line of',
    '        the trail naming OPEN_TRAILS :16056, :16124, :16142 and :16232.',
    '    (c) For b722, each from its bank: (R331)(3) halted at (i), proved, (3)(ii)`s rows waiting on the author`s word (relay',
    '        data/b721_registrations.txt (2)); the census`s StrictMono DOMAIN status against e0_rule.py`s MET list, carried for the author',
    '        (relay data/b721_frozen_line.txt); SIDE-lv-conservation building at its pin with one sorry (relay data/b721_rebuild.txt); the',
    '        report tool outside the sealed list; the draft held at v5.',
#⟪END⟫
#⟪SECTION closing 11⟫
    '        units files, b714`s rectangle units file, b721`s record tool`s hashes bank (declared in their tools` heads), the zero-byte `=` and',
    '        records.json at relay`s root (2026-09-24 and 2026-09-12, neither this act`s) stay local and untracked.',
#⟪END⟫
#⟪SECTION closing 12⟫
    '        port-b707 of SIDE-lv-conservation (at the remote at cb0aea56, tagged v0.14.0); challenge-b720-h2-sign-iff-rh of',
    '        SIDE-explicit-formula; the pin-b718-de5ce8a9 branches as banked; the rebuild-b721 branches of the six wave 1 kernels.',
    '    (h) This act`s closing push-out bank gains the as-of lines after its push; the next act commits it.',
#⟪END⟫
#⟪SECTION closing 13⟫
          'written on its main, the rebuild-b721 branches of the six wave 1 kernels pushed (five at their pins, SIDE-frobenius two commits '
          'beyond its pin, off main), no main moved ; SIDE-explicit-formula main %s (unmoved), v0.37 %s, v0.17 %s, the challenge branch '
          + WL.CHALLENGE_BRANCH + ' at ' + WL.CHALLENGE_TIP[:12] + ' standing as b720 left it ; SIDE-lv-conservation main %s (unmoved), '
#⟪END⟫
#⟪SECTION closing 14⟫
    # ### b721: no carried tool repaired and no repairs bank this act (tools/standing/arms.py's RETIRED tuple the one standing change,
    # ### (R331)(10)); the carry's diffs in its place
#⟪END⟫
#⟪SECTION record 1⟫
    print('  kernels read: %d (SIDE-faces-join among them at b712`s main %s with its tag v0.1.0; no kernel`s main written this act, the rebuild-b721 branches of the six wave 1 kernels pushed on their own refs ((R331)(7)(iii)), five at their pins and SIDE-frobenius`s at its pin with the workflow copied and its two lines, off main; SIDE-lv-conservation`s main '
          'untouched, port-b707 at b712`s tip %s, its checkout at main for this read)' % (len(ks), K.JOIN_NEW_TIP[:8], K.PORT_NEW_TIP[:8]))
#⟪END⟫
#⟪SECTION record 2⟫
_trail_resolved = P3._trail_resolved
#⟪END⟫
#⟪SECTION record 3⟫
    b720's form over b720's objects in git at b720's record tool): the corrigendum's foot; the C2 halt's walk, its output and its positive
    control; the h = 3, 4 predictions; the derivation's foot; the offset's post hoc rows and its tier; the surgery's carry; the frozen line's
    grades and its drafts; the rebuild; each by its own lines through _bfig, which refuses where a bank does not carry its figure; the counter
    from the act's defects and events banks; nothing typed."""
#⟪END⟫
#⟪SECTION record 4⟫
    reg = '%s_registrations.txt' % ACT
    rg = rdn(reg)
    _bfig(reg, r'(?m)^THE OUTPUT: NONE\. Every one of the (\w+) walked fields', 'the C2 rule`s output')
    sec2 = _section(rg, '## (2) THE RULE', '## (3) ')
    walk = re.findall(r'(?m)^  (-\d+)\s+(USED|n0 \d+)', sec2)
    largest, = _bfig(reg, r'the largest \|D\| (\d+) \(Stark; Baker\)', 'the class-number-2 list`s largest |D|')
    reach, = _bfig(reg, r'the walk\s+carried to \|D\| < (\d+) finds those eighteen', 'the walk`s reach')
    pc = _bfig(reg, r'only -2 excluded takes (-\d+) \(n0 (\d+)\) and (-\d+) \(n0 (\d+)\), each b = (-?[\d/]+)', 'the positive control')
    c3, c4 = _pred34(rg, 'H-C3-31'), _pred34(rg, 'H-C4-55')
    dv = _bfig('%s_derivation.txt' % ACT, r'\*\*CHECKS \(1\) \(2\) \(4\): (ALL AS WANTED) ; PLANTS: (ALL FAIL AS WANTED) ; THE GRADE: (.+?) ; (THE TABLE FOR C3, C4, C5 AT '
               r'OMEGA 1-6 EXACT) ; (-23, -39, -47 READ BY IT AS WANTED) ;', 'the derivation`s foot')
    op = _bfig('%s_offset_pred.txt' % ACT, r'\*\*CONTROLS: ALL AS WANTED ; SCORABLE (\d+) OF (\d+) ; delta_pred WRITTEN AT (\d+), ([\d.]+) TO ([\d.]+) ; NO n\* READ ; '
               r'ALL POST HOC ;', 'the offset prediction`s foot')
    orr = _bfig('%s_offset_read.txt' % ACT, r'\*\*PLANT: REFUSES AS WANTED ; POST HOC (\d+): HELD (\d+), REFUTED (\d+), NOT SCORABLE (\d+) ; H-OFFSET (HELD|REFUTED) '
                r'\(POST HOC\) ON ITS OWN FIRST ROWS ;', 'the offset read`s foot')
    ot = _bfig('%s_offset_tier.txt' % ACT, r'\*\*THE RULE`S OUTPUT: (\d+) CHOSEN BY r\(rho\) <= 0\.05 ; delta_pred FORMED AT (\d+) \(NO n\*_pred WITHIN REACH OF ITS '
               r'LIST\) ; NO LIST EXTENDED, NO ONSET RUN ; CARRIED ;', 'the tier`s foot')
    sg = _bfig('%s_surgery_carry.txt' % ACT, r'\*\*THE SURGERY CARRIED, NOT STARTED: PRICE (\S+) h IN (\S+) CALLS \(b718\) .* ; H-SHAPE UNREAD ; NOTHING COMPUTED\.\*\*',
               'the surgery`s carry')
    fl = '%s_frozen_line.txt' % ACT
    fz = _bfig(fl, r'\*\*CONTROLS ALL AS WANTED ; (\w+) STATEMENTS QUOTED AT THEIR PINS ; (.+?) ; \d+ s\.\*\*', 'the frozen line`s foot')
    grades = re.findall(r'(?m)^    E0: (\w+)', rdn(fl))
    per = re.findall(r'(SIDE-\S+) EXCEEDS (\d+), STATED (\d+)', fz[1])
    dr = _bfig('%s_frozen_line_drafts.txt' % ACT, r"\*\*DRAFTS WRITTEN: (\d+) README PARAGRAPHS, (\d+) ONE-LINE DESCRIPTIONS, (SPIRAL_MAP :104'S SENTENCE) ; "
               r'COMMITTED TO THE RELAY ALONE ; NO KERNEL TOUCHED\.\*\*', 'the drafts` foot')
    rb = '%s_rebuild.txt' % ACT
    rh = _bfig(rb, r'(?m)^PUSHED (\d+) ; DISPATCHED (\d+) \(six at most\) ; DISPATCH REFUSED (\d+) ; READ (\d+) ; BUILDS (\d+) OF (\d+) ; HELD \(BREAKS\) (\d+) ; '
               r'NOT READ (\d+)$', 'the rebuild`s head')
    rf = _bfig(rb, r'\*\*(\d+) OF (\d+) WAVE 1 KERNELS BUILD AT THEIR OWN PINS \(ONE WITH A SORRY: (\S+)\) ; SIDE-frobenius RUN ON PUSH \(THE AUTHOR`S TWO LINES\): '
               r'(BUILDS|HELD) ; RUNS (\d+) ; NOTHING REPAIRED ; NO MAIN OR TAG TOUCHED\.\*\*', 'the rebuild`s foot')
    runs = re.findall(r'(?m)^  (SIDE-\S+)\s+.*?; run (\d+) at .*; (BUILDS|HELD \(BREAKS\))$', rdn(rb))
    v1 = _bfig('%s_standing_v121.txt' % ACT, r'\*\*v1\.2\.1: CASES (\d+), AS WANTED (\d+) ;', 'v1.2.1`s controls')
#⟪END⟫
#⟪SECTION record 5⟫
                corr_repeat=ci[5], corr_row=co.get('row'), v121_cases=v1[0], v121_wanted=v1[1],
                walk_n=len(walk), walk_used=sum(1 for _d, x in walk if x == 'USED'), walk_passed=sum(1 for _d, x in walk if x != 'USED'),
                walk_largest=largest, walk_reach=reach, pc=pc, c2_output='NONE',
                c3=c3, c4=c4, h34_same=(c3[1], c3[5]) == (c3[6], c3[7]) and (c4[1], c4[5]) == (c4[6], c4[7]),
                dv_checks=dv[0], dv_plants=dv[1], dv_grade=dv[2], dv_table=dv[3], dv_read=dv[4],
                op_scor=op[0], op_of=op[1], op_written=op[2], op_lo=op[3], op_hi=op[4],
                or_n=orr[0], or_held=orr[1], or_refuted=orr[2], or_unscor=orr[3], or_word=orr[4],
                ot_chosen=ot[0], ot_formed=ot[1], new_pairs=int(ot[1]),
                sg_hours=sg[0], sg_calls=sg[1],
                fz_n=fz[0], fz_per=per, fz_grades=grades, fz_interfaces=grades.count('INTERFACES'), fz_derives=grades.count('DERIVES'),
                dr_paras=dr[0], dr_descs=dr[1],
                rb_pushed=rh[0], rb_disp=rh[1], rb_refused=rh[2], rb_read=rh[3], rb_builds=rh[4], rb_of=rh[5], rb_held=rh[6], rb_unread=rh[7],
                rb_j=rf[0], rb_m=rf[1], rb_sorry=rf[2], rb_fro=rf[3], rb_runs=rf[4], rb_rows=runs,
#⟪END⟫
#⟪SECTION record 6⟫
def _dispatch_rows():
    """the act's dispatches as the rebuild's rows record them (data/b721_rebuild_rows.json): each dispatch row, SIDE-frobenius's run on push
    among them (via push), and each refused dispatch, as (kernel, run id or None, sha)."""
    return [(r.get('kernel'), r.get('run'), r.get('sha')) for r in _rebuild_rows() if r.get('kind') in ('dispatch', 'dispatch_refused')]
#⟪END⟫
#⟪SECTION record 7⟫
    """N1 (R331): no lean on the host -- no lean or lake process runs on this host; the runner dispatches are those of (R331)(7)(iii) alone, six
    at most, each read by its run id. From the command bank (the seat's commands, read live from the capture by the `commands` route: local lean
    none; the dispatch routes' commands counted, SIDE-frobenius's push_run among them) and the rebuild's rows (each dispatch row with its run,
    each run read, the refused dispatch spending no run)."""
#⟪END⟫
#⟪SECTION record 8⟫
    rows = _dispatch_rows()
    spent = [r for _k, r, _s in rows if r]
    runs = set(str(r) for r in spent)
    want = set(str(r) for _k, r in K.REBUILD_RUNS)
    reads = dict((str(r.get('run')), r.get('verdict')) for r in _rebuild_rows() if r.get('kind') == 'read')
    read_ok = all(r in reads for r in want)
    ok = bool(cm) and not seat_lean and disp is not None and len(disp) == len(rows) and len(spent) <= K.MAX_DISPATCHES and runs == want and read_ok
#⟪END⟫
#⟪SECTION record 9⟫
        'the seat`s commands running lean or lake on this host (relay data/b721_commands.json): %s; the dispatch routes` commands in the capture: %s; '
        'the dispatches the rebuild`s rows record (relay data/b721_rebuild_rows.json) %d, %d of them spending a run (at most %d), their runs the '
        'worklist`s: %s; each read by its run id (%s): %s' % (
            (seat_lean or 'NONE') if cm else 'unread', (len(disp) if disp else 'NONE') if cm else 'unread', len(rows), len(spent), K.MAX_DISPATCHES,
            runs == want, ', '.join('%s %s' % (r, reads.get(r, 'UNREAD')) for r in sorted(want)), read_ok))
#⟪END⟫
#⟪SECTION record 10⟫
# ### N2: the registration chain by ancestry -- the rule alone, its tool, its output (the halt), rule (4), the table it reads, its tool, the
# ### predictions -- each a commit of its own (Component 8, the Edit tool; b720's chain ran registrations -> prediction -> controls -> coefficients)
N2_ORDER = (('the rule (3)(i)', 'C2_REG'), ('the select tool', 'C2_SELECT'), ('the rule`s output NONE', 'C2_HALT'), ('rule (4)', 'C3_RULE'),
            ('the table over h = 3, 4, 5', 'C3_RELAY'), ('the predict tool', 'C3_PREDICT_TOOL'), ('the predictions at -31 and -55', 'C2_PRED'))
# ### N2: the registrations' commits whose bytes each extend the last (the registrations bank written by commits of its own)
N2_REG_COMMITS = ('C2_REG', 'C2_HALT', 'C3_RULE', 'C2_PRED')
# ### N2: the banks that would hold a figure computed at a registered discriminant -- none is written this act (the halt; (4)'s computation b722's)
N2_FIGURE_BANKS = ('data/b721_coeffs.txt', 'data/b721_coeffs.json', 'data/b721_coeffs_controls.json', 'data/b721_list.json', 'data/b721_pairs.json')
# ### N2: the act's figure banks, none of which names -31 or -55 (the registrations alone name them)
N2_ACT_BANKS = ('b721_derivation.txt', 'b721_offset_pred.txt', 'b721_offset_read.txt', 'b721_offset_tier.txt', 'b721_surgery_carry.txt',
                'b721_frozen_line.txt', 'b721_frozen_line_drafts.txt', 'b721_rebuild.txt')
# ### N2: each tool's controls before its figures, (bank, the controls' line, the first figure's line)
N2_CONTROLS = (('data/b721_registrations.txt', 'THE CONTROLS FIRST, ALL AS WANTED', 'THE WALK, every h = 2'),
               ('data/b721_derivation.txt', '## CHECK (1), BEFORE STEP (1)', '## STEP (3): THE TABLE'),
               ('data/b721_offset_pred.txt', '## THE CONTROLS, BEFORE ANY delta_pred', '## (b) delta_pred'),
               ('data/b721_offset_read.txt', '## THE PLANT, BEFORE ANY ROW', '## THE ROWS'),
               ('data/b721_frozen_line.txt', '## THE CONTROLS, BEFORE ANY STATEMENT', '## SIDE-archimedean at'))
#⟪END⟫
#⟪SECTION record 11⟫
    """N2 (R331): registrations before figures, the order printed by ancestry; nothing worked at a registered discriminant before its
    registration commits; the h = 3 and h = 4 predictions committed before anything at them is computed, and nothing at them computed this act;
    each tool's controls before its figures. From git (the rule's commit carrying data/b721_registrations.txt alone, its section (1) and no
    discriminant; the chain by merge-base; each registrations commit's bytes a prefix of the next and HEAD's equal to the last; rule (4)'s text
    naming neither -31 nor -55 before the predictions' commit), the act's banks (no figure bank at HEAD or on disk; no bank but the registrations
    naming -31 or -55), b716's to b720's registrations blob for blob at HEAD, and each tool's controls line before its first figure."""
    reg = K.REGISTRATIONS_NEW
    alone = sorted(g(ROOT, 'show', '--name-only', '--format=', K.C2_REG).split()) == [reg]
    at = dict((c, _show(ROOT, getattr(K, c), reg) or '') for c in N2_REG_COMMITS)
    rule_only = '## (1) THE RULE' in at['C2_REG'] and '## (2)' not in at['C2_REG']
    chain = [(N2_ORDER[i][0], N2_ORDER[i + 1][0], grc(ROOT, 'merge-base', '--is-ancestor', getattr(K, N2_ORDER[i][1]), getattr(K, N2_ORDER[i + 1][1])) == 0
              and getattr(K, N2_ORDER[i][1]) != getattr(K, N2_ORDER[i + 1][1])) for i in range(len(N2_ORDER) - 1)]
    seq = [at[c] for c in N2_REG_COMMITS] + [_show(ROOT, 'HEAD', reg) or '']
    prefix = all(seq[i] and seq[i + 1].startswith(seq[i]) and seq[i + 1] != seq[i] for i in range(len(seq) - 2)) and seq[-1] == seq[-2]
    unnamed = not re.search(r'(?<![\d-])-(?:31|55)\b', at['C3_RULE'])
    early = [p for p in N2_FIGURE_BANKS if _show(ROOT, 'HEAD', p) or os.path.exists(os.path.join(ROOT, *p.split('/')))]
    naming = [n for n in N2_ACT_BANKS if re.search(r'(?<![\d-])-(?:31|55)\b(?![\d.])', rdn(n))]
    regs = [(p, bool(_show(ROOT, 'HEAD', p)) and (_show(ROOT, c, p) or '') == (_show(ROOT, 'HEAD', p) or '')) for p, c in K.REG_COMMITS]
#⟪END⟫
#⟪SECTION record 12⟫
    ok = alone and rule_only and all(c for _a, _b, c in chain) and prefix and unnamed and not early and not naming and all(o for _p, o in regs) \
        and all(o for _p, o in ctl)
#⟪END⟫
#⟪SECTION record 13⟫
        'the rule committed alone at %s (git show), its section (1) and no discriminant: %s, %s; the order by ancestry (git merge-base '
        '--is-ancestor): %s; the registrations` bytes at %s each a prefix of the next, HEAD`s equal to the last: %s; rule (4) at %s naming neither '
        '-31 nor -55: %s; a figure bank at a registered discriminant (coefficients, list, pairs) at HEAD or on disk: %s; the act`s figure banks '
        'naming -31 or -55: %s; the registrations of b716 to b720 at their commits against HEAD, blob for blob: %s; each tool`s controls before '
        'its figures: %s' % (
            K.C2_REG[:8], alone, rule_only, '; '.join('%s before %s %s' % (a, b, c) for a, b, c in chain),
            ', '.join(getattr(K, c)[:8] for c in N2_REG_COMMITS), prefix, K.C3_RULE[:8], unnamed, early or 'NONE', naming or 'NONE',
            ', '.join('%s %s' % r for r in regs), ', '.join('%s %s' % (os.path.basename(p), o) for p, o in ctl)))
#⟪END⟫
#⟪SECTION record 14⟫
# ### N3: a sentence claiming more than the grade -- the table, its closed forms or a prediction said proved, a theorem or a kernel statement,
# ### the verb read with its negation (b720's repair, carried; Component 8 points it at b721's objects); a sentence naming the offset's
# ### seventeen rows without "post hoc"; a sentence counting the wave 1 builds with no word of the sorry
N3_OVERCLAIM = re.compile(r'(?i)\b(?:table|closed forms?|predictions?)\b[^.;]{0,60}?\b(?:proved|a theorem|kernel statements?)\b')
N3_NEGATED = re.compile(r'(?i)\b(?:not|nor|no|none) (?:a |the |yet |of them a )?(?:proved|theorem|kernel statements?)\b')
N3_OFFSET = re.compile(r'(?i)\b(?:offset|H-OFFSET)\b[^.;]*\b(?:seventeen|17)\b|\b(?:seventeen|17)\b[^.;]*\b(?:offset|H-OFFSET)\b')
N3_BUILDS = re.compile(r'(?i)\b(\d+|six) of (?:6|six)\b[^.;]*\bbuild')
# ### N3: the banks whose grade prints at their end, (bank, the grade's head)
N3_GRADED = (('b721_derivation.txt', '## THE GRADE'), ('b721_offset_read.txt', '## THE GRADE (POST HOC)'), ('b721_frozen_line.txt', '## THE GRADE'),
             ('b721_rebuild.txt', '## THE GRADE'))
#⟪END⟫
#⟪SECTION record 15⟫
    """N3 (R331): every grade at its end; no sentence of the entry claims more than its grade; the offset's seventeen rows POST HOC wherever
    named. From the graded banks (each grade's head after every row and step it grades, the foot after the grade), the offset banks (each
    head line carrying POST HOC, the read's foot naming its grade POST HOC) and the entry as composed (the findings bank's text, or the
    composer before it is written): no sentence claiming the table, its closed forms or a prediction proved, a theorem or a kernel statement;
    every sentence naming the offset's seventeen carrying "post hoc"; every sentence counting the wave 1 builds naming the sorry."""
#⟪END⟫
#⟪SECTION record 16⟫
    for n, head in N3_GRADED:
#⟪END⟫
#⟪SECTION record 17⟫
        i = t.rfind(head)
        before = max(t.rfind('\n## ', 0, i) if i > 0 else -1, 0)
#⟪END⟫
#⟪SECTION record 18⟫
        graded.append((n, i > 0 and t.find('\n## ', i + 1) < 0 and last[0].startswith('### ### **') and t.rfind('### ### **') > i and before >= 0))
#⟪END⟫
#⟪SECTION record 19⟫
    post = all('POST HOC' in rdn(n).split(NL)[0] for n in ('%s_offset_pred.txt' % ACT, '%s_offset_read.txt' % ACT)) \
        and 'H-OFFSET %s (POST HOC)' % f['or_word'] in rdn('%s_offset_read.txt' % ACT)
#⟪END⟫
#⟪SECTION record 20⟫
    over = [s.strip()[:120] for s in sents if N3_OVERCLAIM.search(N3_NEGATED.sub('', s))]
    bare = [s.strip()[:120] for s in sents if N3_OFFSET.search(s) and 'post hoc' not in s.lower()]
    nosorry = [s.strip()[:120] for s in sents if N3_BUILDS.search(s) and 'sorry' not in s.lower()]
    ok = all(o for _n, o in graded) and post and not over and not bare and not nosorry
#⟪END⟫
#⟪SECTION record 21⟫
        'each grade at its bank`s end, after every row it grades and before the foot: %s; the offset banks` heads POST HOC and the read`s grade '
        'H-OFFSET %s (POST HOC) (relay data/b721_offset_pred.txt, data/b721_offset_read.txt): %s; the sentences of %s claiming the table, its '
        'closed forms or a prediction proved, a theorem or a kernel statement: %s; naming the offset`s seventeen without "post hoc": %s; '
        'counting the wave 1 builds with no word of the sorry: %s' % (
            ', '.join('%s %s' % g_ for g_ in graded), f['or_word'], post, src, over or 'NONE', bare or 'NONE', nosorry or 'NONE'))
#⟪END⟫
#⟪SECTION record 22⟫
#⟪END⟫
#⟪SECTION record 23⟫
    # ### (R331)(7)(ii), N4: the drafts committed to the relay and to no kernel -- each wave 1 kernel's rebuild branch on its origin at its pin
    # ### (ls-remote), SIDE-frobenius's at the author's two lines, whose commits beyond the pin touch the workflow file alone; the drafts bank in
    # ### the relay at its commit (Component 8, the Edit tool; b720's arm read the pin's exclusions)
    tips = dict((k, (g('D:/' + k, 'ls-remote', '--heads', 'origin', K.REBUILD_BRANCH).split() or [''])[0]) for k, _t, _p in K.WAVE1)
    pins = dict((k, g('D:/' + k, 'rev-parse', '%s^{commit}' % t).strip()) for k, t, _p in K.WAVE1)
    off_pin = [k for k in tips if k != 'SIDE-frobenius' and tips[k] != pins[k]]
    fro = tips.get('SIDE-frobenius', '')
    fro_files = sorted(set(g('D:/SIDE-frobenius', 'diff', '--name-only', pins.get('SIDE-frobenius', ''), fro).split())) if fro else []
    fro_ok = fro.startswith(K.FROBENIUS_TWO_LINES) and fro_files == ['.github/workflows/build-module.yml']
    drafts_ok = 'data/%s_frozen_line_drafts.txt' % ACT in g(ROOT, 'show', '--name-only', '--format=', K.C6_DRAFTS).split()
    frozen_ok = not off_pin and fro_ok and drafts_ok
    ok = seal is not None and not late and not wrong and (not ra or not ra.get('late')) and not uncaptured and not unseen and not hand and frozen_ok
#⟪END⟫
#⟪SECTION record 24⟫
        'the drafts committed to the relay (%s, relay data/b721_frozen_line_drafts.txt): %s, and to no kernel: the branch %s on each wave 1 '
        'kernel`s origin (git ls-remote --heads) off its pin %s; SIDE-frobenius`s at %s, its files beyond the pin %s: %s; ' % (
            K.C6_DRAFTS[:8], drafts_ok, K.REBUILD_BRANCH, off_pin or 'NONE', fro[:10] or 'absent', fro_files or 'NONE', fro_ok) +
#⟪END⟫
#⟪SECTION record 25⟫
#⟪END⟫
#⟪SECTION record 26⟫
        and not differ and arms_ok and not amended and not ident and not chained and not kept and gw_ok and gl
#⟪END⟫
#⟪SECTION record 27⟫
#⟪END⟫
#⟪SECTION record 28⟫
    return ('### b721 — lane two, act one hundred and forty-eight, the table act under (R331): b720 at its weight and its corrigendum; the C2 '
            'table’s test halted at its rule, proved; the table over h = 3, 4, 5 and two predictions registered; the offset’s seventeen post hoc; '
            'the surgery carried; the frozen line quoted, drafted and rebuilt at its own pins; the federation pin closed')
#⟪END⟫
#⟪SECTION record 29⟫
#⟪END⟫
#⟪SECTION record 30⟫
    """the entry's title by its objects, the ferry's Component 8 form adjusted to what the act did ("the C2 table at two discriminants it chose:
    ... the table <HELD | REFUTED>" read as the rule choosing none, the halt proved; "the table over h = 3, 4, 5 <written and checked>, two
    predictions registered; the offset's post hoc rows and <k> new pairs <registered>; the surgery <carried>; the frozen line's statements
    quoted, its drafts for the release sitting; <j> of 6 wave 1 kernels build at their own pins; the federation pin closed"); every figure
    from the banks."""
#⟪END⟫
#⟪SECTION record 31⟫
    return ('## The C2 table at the discriminants its rule would choose: none -- every class-number-2 field’s least negative index at -2 or '
            '-1/2, the halt proved; the table over h = 3, 4, 5 written and checked, two predictions registered (n0 = %s at %s, %s at %s); the '
            'offset’s post hoc rows, H-OFFSET %s on its own first rows, and %s new pairs registered; the surgery carried; the frozen line’s '
            'statements quoted, its drafts for the release sitting; %s of %s wave 1 kernels build at their own pins, one with a sorry; the '
            'federation pin closed' % (f['c3'][1], f['c3'][0], f['c4'][1], f['c4'][0], f['or_word'].lower(), f['new_pairs'], f['rb_j'], f['rb_m']))
#⟪END⟫
#⟪SECTION record 32⟫
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) (R331)(3) halted at (i), proved: the rule’s output NONE over all %s class-number-2 fields (the largest |D| %s; the walk to |D| < '
            '%s finds no other), its positive control taking %s and %s; (3)(ii)’s rows and the coefficients wait on the author’s word, carried to '
            '%s (relay data/b721_registrations.txt (2)); (2) b720’s event (12) re-read from the transcript: its cause the branch and the push in '
            'one message, not the listing, the premise of (R331)(1) corrected in the corrigendum’s item (ii) (relay data/b721_corrigendum.txt); '
            '(3) the %d REGISTRY rows reading not yet read with b721 named, none read, (R331) ordering no read of them; (4) monotone_unique_zero '
            'graded INTERFACES by the rule, StrictMono in its MET list alone, while the keystone census v0.7.1 and v0.8.3 list StrictMono as '
            'DOMAIN: the two lists’ disagreement carried under the consistency line, the rule’s grade standing (relay data/b721_frozen_line.txt); '
            '(5) %s builds with a sorry (sorryAx in one theorem), counted among the %s of %s and not complete (relay data/b721_rebuild.txt); '
            '(6) SIDE-frobenius run on push at the author’s two lines (the push trigger and TARGET fixed) on its rebuild branch alone, its commits '
            'the seat’s neutral identity, nothing on main; the run’s conclusion failure from the axioms step, as at three other kernels, the build '
            'exit 0; (7) the report tool outside the sealed list until the root (relay data/b708_rules.txt row (1)); (8) %s and the seat’s %s '
            'defect%s as lettered' % (
                f['walk_n'], f['walk_largest'], f['walk_reach'], f['pc'][0], f['pc'][2], K.NEXT_ACT, _registry_unread(), f['rb_sorry'],
                f['rb_j'], f['rb_m'],
#⟪END⟫
#⟪SECTION record 33⟫
#⟪END⟫
#⟪SECTION record 34⟫
    the scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record (Component 8, the Edit tool; b720's composer over
    b720's objects in git at b720's record tool, not carried)."""
#⟪END⟫
#⟪SECTION record 35⟫
    """the trail record (Component 8, the Edit tool, over b721's objects; b720's composer over b720's objects in git at b720's record tool)."""
#⟪END⟫
#⟪SECTION regspec 1⟫
    ('runner dispatch commands made', 'DISPATCHES', 'DISPATCHES', 'dispatches', '### N1, (R331)(7)(iii): the rebuild`s six dispatch commands (one refused, SIDE-frobenius with no workflow on main) and SIDE-frobenius`s push_run; six runs, each read by its run id; MEASURED off the command bank (each dispatch route run at a command`s head).'),
    ('runner runs spent', 'RUNS', 'RUNS', 'runs', '### N1: six at most; MEASURED off data/b721_rebuild_rows.json`s dispatch rows carrying a run.'),
#⟪END⟫
#⟪SECTION regspec 2⟫
    ('pin branches cut on a kernel', 'PINBRANCHES', 'PINBRANCHES', 'branches', '### none: the pin-b718-de5ce8a9 branches left as banked ((R331)(8)); MEASURED off the twelve kernels` refs/heads/pin-b721*.'),
    ('rebuild branches cut on a kernel', 'RBBRANCHES', 'RBBRANCHES', 'branches', '### (R331)(7)(iii): rebuild-b721 on each wave 1 kernel; MEASURED off the six kernels` refs/heads.'),
    ('rebuild branches pushed to a kernel`s origin', 'RBPUSHED', 'RBPUSHED', 'branches', '### (R331)(7)(iii): one per message; MEASURED off each kernel`s refs/remotes/origin/rebuild-b721.'),
    ('commits on a rebuild branch beyond its pin', 'RBBEYOND', 'RBBEYOND', 'commits', '### SIDE-frobenius`s two (the workflow copied verbatim; the author`s two lines), the seat`s neutral identity; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 3⟫
    ('challenge branches cut on a kernel', 'CHBRANCH', 'CHBRANCH', 'branches', '### none this act: b720`s challenge-b720-h2-sign-iff-rh standing; MEASURED off SIDE-explicit-formula`s refs/heads/challenge-b721*.'),
#⟪END⟫
#⟪SECTION regspec 4⟫
    ('Lean files written on a rebuild branch', 'RBLEAN', 'RBLEAN', 'files', '### none: each branch at its pin or carrying the workflow alone; MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 5⟫
    ('branches deleted at step zero', 5, 5, 'branches', '### (R331)(9): relay push-b720-closing, push-b720-preroot, push-b720-record; PLACE-papers push-b720-preroot, push-b720-record; each local, by name, after --merged listed it (data/b721_stepzero.txt :52-:55).'),
#⟪END⟫
#⟪SECTION regspec 6⟫
    ('workflow files written on a kernel branch', 'RBWF', 'RBWF', 'files', '### SIDE-frobenius`s rebuild branch alone: SIDE-explicit-formula`s build-module.yml copied verbatim, then the author`s two lines (the push trigger, the fixed target); MEASURED off each branch against its pin.'),
#⟪END⟫
#⟪SECTION regspec 7⟫
    ('REGISTRY rows added', 0, 0, 'rows', '### none this act: the rows reading not yet read with b721 named left unread, (R331) ordering no read.'),
    ('REGISTRY lines removed or edited', 'REGREMOVED', 'REGREMOVED', 'lines', '### none; MEASURED off git diff --numstat b826da8c..HEAD -- REGISTRY.md.'),
#⟪END⟫
#⟪SECTION regspec 8⟫
    ('generated corrigendum entries', 1, 1, 'entries', '### (R331)(2): FINDINGS :11110.'),
    ('corrigenda bank rows appended', 1, 1, 'rows', '### (R331)(2): row (41).'),
#⟪END⟫
#⟪SECTION regspec 9⟫
    ('computations banked, each by its own tool writing its bank alone', 'COMPUTE', 'COMPUTE', 'computations', '### (R331)(4)-(7): the derivation, the offset`s prediction, read and tier, the frozen line and the rebuild; MEASURED off the banks present.'),
    ('registrations read unchanged from their commit', 4, 4, 'registrations', '### (R331)(3), N2: b716`s at dc5e808f, b718`s at 8146404b, b719`s at 965cb8e8, b720`s at 54fc03d9, blob for blob at HEAD.'),
    ('registrations commits touching the registrations alone', 'REGS', 'REGS', 'commits', '### (R331)(3)-(4), N2: the rule (54be7b0b), its output (15cb6cc4), rule (4) (5febd903), the predictions (e8c3dff4); MEASURED off each commit`s files.'),
    ('banks holding a figure at a registered discriminant', 'PREREG', 'PREREG', 'banks', '### N2: none -- no coefficient, list or pairs bank; nothing at -31 or -55 computed; MEASURED off the banks present.'),
#⟪END⟫
#⟪SECTION regspec 10⟫
    ('Lean statements of the table written or compiled', 0, 0, 'statements', '### N1: the table Python-checked against the model, graded at its end, not compiled.'),
#⟪END⟫
#⟪SECTION regspec 11⟫
    ('shared tools written by ruling', 'STANDINGWRITTEN', 'STANDINGWRITTEN', 'tools', '### (R331)(2): tools/standing/ to v1.2.1 -- VERSION and manifest.py changed, gitwrite.py, title.py and v121.py new (68440f11); MEASURED off the worklist`s lists.'),
    ('arms out of the suite`s run list by b720`s retirement', 'RETIRED', 'RETIRED', 'arms', '### b720`s RETIRED, carried unchanged (the run list of 116); MEASURED off tools/standing/arms.py.'),
    ('arms retired this act', 0, 0, 'arms', '### none: the ferry`s run list of 116 binds.'),
#⟪END⟫
#⟪SECTION regspec 12⟫
    ('shared banks written by ruling', 1, 1, 'banks', '### (R331)(9): data/act_current.json at step zero (7ecfbc05); data/arm_tags.json not written (outside (W)).'),
#⟪END⟫
#⟪SECTION regspec 13⟫
    ('computations run with free memory beneath the hold', 'BENEATH', 'BENEATH', 'computations', '### (R331)(7)(iii), (9): the 2,560 MB hold read before each push, dispatch and read; MEASURED off the defects bank.'),
#⟪END⟫
#⟪SECTION regspec 14⟫
    ('standing arms added', 0, 0, 'arms', '### N5.'),
#⟪END⟫
#⟪SECTION regspec 15⟫
    ('outbound fetches by a tool of this act carrying an identifier of the author', 0, 0, 'fetches', '### N5: no outbound fetch this act beyond the pushes, their ls-remote read-backs, the dispatches and the run reads.'),
#⟪END⟫
#⟪SECTION regspec 16⟫
        return bool(c) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.C2_REG, c], capture_output=True).returncode == 0 \
            and c != K.C2_REG
    fig_banks = [p for p in ('data/b721_coeffs.txt', 'data/b721_coeffs.json', 'data/b721_coeffs_controls.json', 'data/b721_list.json', 'data/b721_pairs.json')
#⟪END⟫
#⟪SECTION regspec 17⟫
                    REGS=len([c for c in (K.C2_REG, K.C2_HALT, K.C3_RULE, K.C2_PRED) if alone(c)]),
#⟪END⟫
#⟪SECTION regspec 18⟫
                    COMPUTE=len([n_ for n_ in ('derivation', 'offset_pred', 'offset_read', 'offset_tier', 'frozen_line', 'rebuild')
                                 if os.path.exists(os.path.join(ROOT, 'data', 'b721_%s.txt' % n_))]),
#⟪END⟫
#⟪SECTION regspec 19⟫
              'RBBRANCHES', 'RBPUSHED', 'RBBEYOND', 'RBLEAN', 'RBWF', 'RUNS', 'CHBRANCH', 'REGREMOVED',
#⟪END⟫
#⟪SECTION regspec 20⟫
    spec = {"registration": ("data/b721_registration_2026-10-28.txt -- b721, THE TABLE ACT: b720 AT ITS WEIGHT AND ITS CORRIGENDUM; THE C2 "
                             "TABLE`S TEST HALTED AT ITS RULE, PROVED; THE TABLE OVER h = 3, 4, 5 AND TWO PREDICTIONS REGISTERED; THE OFFSET`S "
                             "SEVENTEEN POST HOC; THE SURGERY CARRIED; THE FROZEN LINE QUOTED, DRAFTED AND REBUILT AT ITS OWN PINS; THE "
                             "FEDERATION PIN CLOSED, UNDER (R331)"),
#⟪END⟫
#⟪SECTION report 1⟫
Carried from b720's standing report (tools/b720_report.py) by diff and its lines rewritten at Component 8: b720's lines (the challenge,
the pin, the coefficients at -35 and -40, H-DECOMP, H-RR, the REGISTRY cells) read banks this act does not write, and are not carried; the
lines are b721's: the rebuild at each wave 1 kernel's own pin, on the runner by its run ids (KERNEL), the table over h = 3, 4, 5 exact and
the C2 rule's output NONE from decomposition types (CERTIFIED -- Python-checked, not a kernel statement, N3), the h = 3, 4 predictions and
the fourteen blind (REGISTERED), and the offset post hoc, the frozen line and its drafts, the draft and the carried (HELD).
#⟪END⟫
#⟪SECTION report 2⟫
    # ------------------------------------------------------------------ KERNEL: THE REBUILD ((R331)(7)(iii)), on the runner (N1: no lean on
    # ------------------------------------------------------------------ the host), each run read by its id
    sk = seat('%s_rebuild.txt' % ACT, 'PUSHED ')
    keys['REBUILD'] = ('KERNEL -- THE REBUILD AT EACH WAVE 1 KERNEL`S OWN PIN: %s of %s build at the Mathlib each manifest carries (%s with a '
                       'sorry, not complete); %s pushed, %s runs read by their ids, %s dispatch refused (SIDE-frobenius, no workflow on main) '
                       'and its run on push at the author`s two lines (%s); held %s, nothing repaired, no main or tag touched. SOURCE %s.' % (
                           f['rb_j'], f['rb_m'], f['rb_sorry'], f['rb_pushed'], f['rb_runs'], f['rb_refused'], K.FROBENIUS_TWO_LINES[:8],
                           f['rb_held'], sk['text']))
#⟪END⟫
#⟪SECTION report 3⟫
    # ------------------------------------------------------------------ CERTIFIED: THE TABLE OVER h = 3, 4, 5 ((R331)(4)), exact; THE HALT'S
    # ------------------------------------------------------------------ WALK ((R331)(3)), from decomposition types alone
    sd = seat('%s_derivation.txt' % ACT, '### CHECK (4): ALL AS WANTED')
    keys['TABLE'] = ('CERTIFIED -- THE TABLE OVER CYCLIC h = 3, 4, 5 AT OMEGA 1-6: %s ; %s ; %s; its checks before each step and its plants '
                     'failing as wanted; Python-checked against the group-ring model, a written table and not a kernel statement (N3). SOURCE %s.' % (
                         f['dv_grade'], f['dv_table'], f['dv_read'], sd['text']))
    seats.append(sd)
    sw = seat('%s_registrations.txt' % ACT, 'THE OUTPUT: NONE')
    keys['HALT'] = ('CERTIFIED -- THE C2 RULE`S OUTPUT NONE ((R331)(3) HALTED AT (i), PROVED): the %s class-number-2 fields walked from '
                    'decomposition types (the largest |D| %s, the walk to |D| < %s), %s used and %s passed over on -2 or -1/2; the positive '
                    'control taking %s and %s; no coefficient computed. SOURCE %s.' % (
                        f['walk_n'], f['walk_largest'], f['walk_reach'], f['walk_used'], f['walk_passed'], f['pc'][0], f['pc'][2], sw['text']))
#⟪END⟫
#⟪SECTION report 4⟫
    # ------------------------------------------------------------------ REGISTERED: THE h = 3, 4 PREDICTIONS AND THE FOURTEEN BLIND (N2)
    sp = seat('%s_registrations.txt' % ACT, '## (5) THE PREDICTIONS BY RULE (4)')
    keys['PRED'] = ('REGISTERED -- THE h = 3 AND h = 4 PREDICTIONS, committed at %s before anything at them: H-C3-31 n0 = %s, b = %s; H-C4-55 '
                    'n0 = %s, b = %s; the model naming the same n0 at both: %s; nothing at -31 or -55 computed, the computation %s`s. SOURCE %s.' % (
                        K.C2_PRED[:8], f['c3'][1], f['c3'][5], f['c4'][1], f['c4'][5], f['h34_same'], K.NEXT_ACT, sp['text']))
    seats.append(sp)
    sb = seat('%s_registrations.txt' % ACT, '## (3) THE TABLE')
    keys['BLIND'] = ('REGISTERED -- THE TABLE`S PREDICTIONS AT THE FOURTEEN UNUSED CLASS-NUMBER-2 FIELDS, blind, with their falsifier; read not '
                     'this act. SOURCE %s.' % sb['text'])
    seats.append(sb)
    # ------------------------------------------------------------------ HELD: THE OFFSET POST HOC; THE CARRIED; THE FROZEN LINE AND ITS DRAFTS
    so = seat('%s_offset_read.txt' % ACT, '## THE GRADE (POST HOC)')
    keys['OFFSET'] = ('HELD -- THE OFFSET, POST HOC: the seventeen HELD %s, REFUTED %s, NOT SCORABLE %s, H-OFFSET %s post hoc on its own first '
                      'rows, testing nothing; the tier %s chosen, %s formed, carried. SOURCE %s.' % (
                          f['or_held'], f['or_refuted'], f['or_unscor'], f['or_word'], f['ot_chosen'], f['ot_formed'], so['text']))
    seats.append(so)
    sf = seat('%s_frozen_line.txt' % ACT, '## THE GRADE')
    keys['FROZEN'] = ('HELD -- THE FROZEN LINE: %s statements at their pins, %d DERIVES and %d INTERFACES by E0; the sentences graded by the seat`s '
                      'hand, a reading; %s README paragraphs and %s descriptions drafted for the release sitting, in the relay alone. SOURCE %s.' % (
                          f['fz_n'].lower(), f['fz_derives'], f['fz_interfaces'], f['dr_paras'], f['dr_descs'], sf['text']))
    seats.append(sf)
    sh = seat('%s_ferry.txt' % ACT, '(10) THE DRAFT')
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished, nothing deposits; the surgery under H-SHAPE carried, nothing run; the federation '
                    'pin closed at its banked state. SOURCE %s.' % (K.DRAFT, sh['text']))
#⟪END⟫
#⟪SECTION report 5⟫
    order = [('KERNEL', ['REBUILD']), ('CERTIFIED', ['TABLE', 'HALT']), ('REGISTERED', ['PRED', 'BLIND']), ('HELD', ['OFFSET', 'FROZEN', 'HELD'])]
#⟪END⟫
