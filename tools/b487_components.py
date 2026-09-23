# -*- coding: utf-8 -*-
"""b487_components.py -- COMPONENTS 1, 2 AND 3. ### Run after the seal (`479646edfdcfbf85...`).
### ### **EVERY WRITE IS AN APPEND. ### NOTHING IS FETCHED. ### NO DRAFT IS APPLIED.**
"""
import io
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import errata_append as EA  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERR = os.path.join(PP, 'ERRATA.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
B485 = os.path.join(D, 'b485_the_two_records.txt')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def append_plain(path, block, label):
    """### an APPEND with the prefix proved, for the two pointers."""
    raw = io.open(path, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    add = (eol + eol.join(block) + eol).encode('utf-8')
    io.open(path, 'ab').write(add)
    after = io.open(path, 'rb').read()
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '').split(NL)
    new = set(after.decode('utf-8-sig', 'replace').replace(chr(13), '').split(NL))
    missing = [x for x in old if x not in new]
    rec('    ### %s -- `%s`' % (label, os.path.relpath(path, ROOT if 'relay' in path else PP)))
    rec('      bytes before / appended / after : %d / %d / %d' % (len(raw), len(add), len(after)))
    rec('      PRIOR BYTES A TRUE PREFIX : %s ; BOM preserved : %s'
        % (after.startswith(raw), after.startswith(b'\xef\xbb\xbf') == bom))
    rec('      ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    return len(missing)


# ============================================================ THE DRAFTS, DECLARED AS DATA
# ### Each row: (record, sentence index, erratum or None, replacement or None, why).
TERMINAL = '`structural_exhaustiveness_proved`'
REPL_14 = (
    'Proved and machine-checked around the argument, with the catalogue read exactly as its route '
    'terminal states it: the Lean terminal ' + TERMINAL + ' proves that the kernel’s mechanism '
    'type has seven members, that none of them produces the off-line signature the kernel defines, '
    'and Ostrowski’s classification of the places of ℚ — that the seven classes '
    'exhaust the mechanisms is the manuscript’s theorem, and the kernel does not check it; '
    'and, as before, Conservation of Spectra from Tate’s thesis (Chapter 13); the Mechanism '
    'Theorem from the Independence, Determination and Symmetry principles (Chapter 10); h1 complete '
    'at the witness (`h1_complete_at_Phi`, SIDE-lv-conservation); and the finite-range Li '
    'positivity certificate whose finite-set conjunct is itself proved (`lowFinset_mem_iff`, '
    'v0.10.0).')
REPL_15 = (
    'Section 27.3, “The One Premise,” names that clause in five equivalent registers with '
    'its full literature ancestry, and locates it at one compiled goal state whose terminal in the '
    'deposit’s concordance is `conservation_s_dark` at v1.5 — which the concordance '
    'records as a SHELL, a stand-in rather than a terminal that certifies the clause; the '
    'C₅-output (Hilbert–Pólya) register is explicitly disclaimed, never claimed.')
REPL_K2 = (
    'The kernel compiles the exclusion architecture: the Lean terminal ' + TERMINAL + ' proves that '
    'the kernel’s mechanism type has seven members, that none of them produces the off-line '
    'signature the kernel defines, and Ostrowski’s classification of the places of ℚ '
    '— that the seven classes exhaust the mechanisms is the manuscript’s theorem, and the '
    'kernel does not check it.')


def main():
    SV = json.loads(read(os.path.join(D, 'b487_survey.json')))
    res = dict(writes={}, drafts=[], counts={})

    # ===================================================================== COMPONENT 1
    rec('=' * 108)
    rec('COMPONENT 1 -- (R97) EXECUTED. ### **THE RENUMBER, THE TWO POINTERS, AND THE NEW ARM.**')
    rec('=' * 108)
    rec('  ### (1a) THE APPENDER`S ARM, ON BOTH CONTROLS, BEFORE IT TOUCHES THE LEDGER.')
    tmp = tempfile.mkdtemp(prefix='b487_')
    ok, lines = EA.self_test(tmp)
    for l in lines:
        rec(l)
    if not ok:
        rec('  ### ### **HARD FAILURE: THE GUARD DOES NOT BEHAVE. NOTHING IS WRITTEN.**')
        raise SystemExit(2)
    rec('')
    rec('  ### (1b) THE RENUMBER, APPENDED BENEATH b485`S ENTRY.')
    block = [
        '',
        ('**Renumbered `E-2026-09-22-2`, `b487`, 2026-09-22, on ruling `(R97)`.** The entry '
         'immediately above — the currency note for Zenodo record `21432399`, appended by '
         '`b485` — was filed under the id `E-2026-09-22-1`, **which `b469` had already used** '
         'for *“Deposited sentences that assert a machine check, name no terminal, and have '
         'no row in the deposit’s own concordance.”* `b486`’s fold found the clash; '
         '`(R97)` disposes of it.'),
        '',
        ('**`b469`’s entry keeps `E-2026-09-22-1`, having been filed earlier. The entry above '
         'is `E-2026-09-22-2` from this line forward.** No existing line is edited and no id is '
         'rewritten in place — the ledger is append-only and its ids are cited elsewhere, so '
         'a correction to an id is itself an append.'),
        '',
        ('*Filed by `b487` (relay `data/b487_the_renumber_and_the_drafts.txt`). The appender now '
         'refuses a duplicate id before it writes, and both of its controls are exercised in that '
         'bank. No deposit action is taken or implied; nothing was written at Zenodo.*'),
        '',
    ]
    code, out = EA.append(ERR, 'E-2026-09-22-2', block)
    for l in out:
        rec(l)
    rec('    ### appender exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        raise SystemExit(2)
    res['writes']['ERRATA.md'] = 0

    rec('')
    rec('  ### (1c) THE TWO DATED CORRECTION POINTERS.')
    m1 = append_plain(OT, [
        '',
        ('*Correction pointer, `b487`, 2026-09-22, on ruling `(R97)`:* the erratum `b485`’s '
         'record above calls `E-2026-09-22-1` **is now `E-2026-09-22-2`**. `b469`’s entry, '
         'filed earlier, keeps `E-2026-09-22-1`. `b485`’s record is not edited; this pointer '
         'is appended. `b486`’s fold cites `b469`’s entry and is correct as written.'),
        '',
    ], 'the trail pointer')
    m2 = append_plain(B485, [
        '',
        ('### CORRECTION POINTER, b487, 2026-09-22, ON RULING (R97). ### The erratum this bank '
         'reports as `E-2026-09-22-1` is ### **NOW `E-2026-09-22-2`** -- b469 had already used that '
         'id, and b469`s entry keeps it. ### **NO LINE OF THIS BANK IS EDITED; THIS POINTER IS '
         'APPENDED.**'),
        '',
    ], 'the b485 bank pointer')
    res['writes']['OPEN_TRAILS.md (pointer)'] = m1
    res['writes']['b485_the_two_records.txt'] = m2
    rec('')
    rec('    ### ### **LINES REMOVED, ACROSS ALL THREE WRITES : %d.**' % (m1 + m2))
    rec('    ### ### **AND `E-2026-09-22-1` NOW APPEARS %d TIMES IN ERRATA.md** -- b469`s heading,')
    e = read(ERR)
    L[-1] = L[-1] % e.count('E-2026-09-22-1')
    rec('    ### b485`s original heading (unedited, as the law requires), and the renumber line`s')
    rec('    ### own quotation of the clash. ### **THE ID THAT GOVERNS IS THE ONE THE RENUMBER LINE')
    rec('    ### ASSIGNS, AND IT IS THE LAST WORD IN THE FILE ON THAT ENTRY.**')

    # ===================================================================== COMPONENT 2
    rec('')
    rec('=' * 108)
    rec('COMPONENT 2 -- THE THREE DESCRIPTIONS, READ. ### **NOTHING FETCHED.**')
    rec('=' * 108)
    for s in SV['sources']:
        rec('')
        rec('  ### RECORD ### **%s** ### -- %s' % (s['rec_id'], s['what']))
        rec('      source : %s' % s['source'])
        rec('      sentences : %d ; asserting a check : ### **%d**'
            % (s['n_sentences'], s['n_claims']))
    rec('')
    rec('    ### ### **TOTAL : %d.** ### The predicate`s first version caught ten; widening it to')
    L[-1] = L[-1] % len(SV['claims'])
    rec('    ### include `proves` and `certified` added monograph sentence 5 and ### **KERNEL')
    rec('    ### SENTENCE 2 -- THE VERY CLAIM `E-2026-09-14-1` WAS FILED AGAINST.**')
    rec('    ### ### **BOTH YIELDS ARE ON THE RECORD.**')
    rec('')
    for c in SV['claims']:
        rec('  ### %s sentence %d of %d' % (c['rec_id'], c['idx'], c['total']))
        for chunk in [c['text'][i:i + 126] for i in range(0, min(len(c['text']), 380), 126)]:
            rec('      %s' % chunk)
        if len(c['text']) > 380:
            rec('      ... (quoted whole in `b487_extract.txt`)')

    # ===================================================================== COMPONENT 3
    rec('')
    rec('=' * 108)
    rec('COMPONENT 3 -- THE DRAFTS. ### **BANKED AND NOT APPLIED.**')
    rec('=' * 108)
    ASSIGN = {
        ('21539167', 5): (None, 'the erratum`s own words: *"Whether the manuscript proves the '
                                'catalogue`s exhaustiveness is UNTOUCHED by this entry."* This is '
                                'the MANUSCRIPT`s claim, not a machine-check claim.'),
        ('21539167', 9): (None, 'it says the kernel *"reports its axiom base at named theorems"* '
                                '-- it names the practice and claims no check the terminals do not '
                                'carry.'),
        ('21539167', 10): (None, 'it NAMES the three route theorems and tells a skeptic how to run '
                                 'them. A sentence that names its terminals is what the errata ask '
                                 'for.'),
        ('21539167', 14): ('E-2026-09-14-1', None),
        ('21539167', 15): ('E-2026-09-22-1', None),
        ('21539167', 16): (None, 'it reports a companion census and its *"two machine-checked '
                                 'negative results"*. NEITHER erratum names that census among its '
                                 'affected deposits, so no erratum reaches it. It asserts a check '
                                 'without naming a terminal, which is a CANDIDATE for a future '
                                 'entry and NOT this act`s business.'),
        ('21520474', 2): ('E-2026-09-14-1', None),
        ('21520474', 3): (None, 'it names the modules and states what they compile with. '
                                'Verifiable as written.'),
        ('21520474', 4): (None, 'it names `silence_universal` AND discloses the load-bearing '
                                'hypothesis. It claims less, not more, than the terminal carries.'),
        ('21539068', 8): (None, 'NEITHER erratum names SIDE-lv-conservation among its affected '
                                'deposits, and the sentence states the identity it compiled.'),
        ('21539068', 12): (None, 'as above; it states a compiled count of six lemmas.'),
        ('21539068', 17): (None, 'an AXIOM AUDIT that discloses `sorryAx` on the pinned '
                                 'declaration. It is the disclosure the errata ask others to make.'),
    }
    REPL = {('21539167', 14): REPL_14, ('21539167', 15): REPL_15, ('21520474', 2): REPL_K2}
    rec('')
    rec('  %-10s %-5s %-18s %s' % ('record', 'sent', 'erratum', 'disposition'))
    rec('  ' + '-' * 100)
    n_err, n_none = 0, 0
    for c in SV['claims']:
        key = (c['rec_id'], c['idx'])
        eid, why = ASSIGN.get(key, (None, 'not assigned'))
        if eid:
            n_err += 1
        else:
            n_none += 1
        rec('  %-10s %-5d %-18s %s' % (c['rec_id'], c['idx'], eid or 'NO ERRATUM',
                                       'REPLACEMENT DRAFTED' if eid else 'LEFT AS IT STANDS'))
        res['drafts'].append(dict(rec_id=c['rec_id'], idx=c['idx'], erratum=eid,
                                  replacement=REPL.get(key), why=why))
    rec('')
    rec('  ### ### **RESTING ON AN ERRATUM : %d. ### NO ERRATUM, LEFT AS THEY STAND : %d.**'
        % (n_err, n_none))
    res['counts'] = dict(claims=len(SV['claims']), on_erratum=n_err, no_erratum=n_none)
    rec('')
    rec('  ### THE DRAFTS, IN FULL.')
    for d in res['drafts']:
        if not d['erratum']:
            continue
        rec('')
        rec('  ### ### **%s, sentence %d -- rests on `%s`**' % (d['rec_id'], d['idx'], d['erratum']))
        orig = next(c['text'] for c in SV['claims']
                    if c['rec_id'] == d['rec_id'] and c['idx'] == d['idx'])
        rec('      ORIGINAL:')
        for chunk in [orig[i:i + 118] for i in range(0, min(len(orig), 360), 118)]:
            rec('        %s' % chunk)
        if len(orig) > 360:
            rec('        ...')
        rec('      REPLACEMENT, drafted from the erratum`s own words and nothing wider:')
        for chunk in [d['replacement'][i:i + 118] for i in range(0, len(d['replacement']), 118)]:
            rec('        %s' % chunk)
    rec('')
    rec('  ### AND THE SENTENCES LEFT AS THEY STAND, EACH WITH ITS REASON:')
    for d in res['drafts']:
        if d['erratum']:
            continue
        rec('    %s sentence %-3d -- %s' % (d['rec_id'], d['idx'], d['why'][:100]))
    rec('')
    rec('  ### ### **THE DRAFTS ARE BANKED AND NOT APPLIED. ### NOTHING AT ZENODO IS WRITTEN.**')
    rec('  ### The author applies them at the platform; ### **THE ACT AFTER FETCHES EACH')
    rec('  ### DESCRIPTION BACK AND BANKS IT BEFORE ANY RECORD SAYS THE EDIT WAS MADE.**')

    io.open(os.path.join(D, 'b487_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    io.open(os.path.join(D, 'b487_the_renumber_and_the_drafts.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(res, io.open(os.path.join(D, 'b487_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
