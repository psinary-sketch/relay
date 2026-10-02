# -*- coding: utf-8 -*-
"""b600_record.py -- THE ACT'S RECORD TOOL, UNDER (R210). ### ONE SUBCOMMAND PER BANK.

### ### b600: LANE THREE, ACT TWENTY-SEVEN -- REMAINDER 5, THE PRODUCT LEMMA, STATED AS A SALT-CHECKED PROP AND PROVED OR CARRIED
### TO ITS NAMED OBLIGATIONS; THE GENERATOR-RUN LINE AMENDED; THE AUTHORITY ORDER ENTERED.
### Subcommands write only `data/b600_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b596_record.py (the kernel module, its prints,
### the E0 read, the federation walk, the node lists and the pages) and b599_record.py (the record lines, the scores, the record).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
PRE_PP = 'bc1337a'
PRE_RELAY = '2b9f75cd'
PRE_KER = '5a1630b'
STEPZERO = '92b1c086'
TAG = 'v0.18'
BRANCH = 'product-b600'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/35432614-be58-48b9-8b45-54387165dcef/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/35432614-be58-48b9-8b45-54387165dcef.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
KFILES = dict(prod='SIDEExplicitFormula/Product.lean', salt='SIDEExplicitFormula/SaltCheckProduct.lean')
AXF = 'AxiomCheckProduct.lean'
OWN = ('SIDEExplicitFormula/Product.lean', 'SIDEExplicitFormula/SaltCheckProduct.lean', 'AxiomCheckProduct.lean')
NS = 'SIDEExplicitFormula.Product.'
NEW_NODES = [NS + 'sum', NS + 'sum_ef', NS + 'ProductLemma', NS + 'h2_sign_cfg_sum_iff_targets', NS + 'productLemma_holds']
THE_NODE = NS + 'productLemma_holds'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']
GRH = 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))
    return b


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE FIRST BUILD OF Product.lean WAS STOPPED BY THE HARNESS, NOT BY AN OOM AND NOT BY THE WATCHDOG: started at 2026-10-02T23:04:50Z '
    'with 4154 MB free (the hold 2560), run in the background under b596`s watchdog; the harness`s memory-pressure reaper stopped it at '
    't=600s while the session was idle (the log`s last line: free 2549 MB, lean 714 MB resident, no EXIT line, no error printed). '
    'Recorded as a stop under the amended line (OPEN_TRAILS :12352). No orphan lean, lake or python remained; the build is not restarted '
    'without the author`s word.',
    '(b) THE STEP-ZERO PROCESS LISTING`S NAME SET DID NOT INCLUDE tail: after the stop the listing found six `tail -f` processes of '
    'earlier sessions (PIDs 29544, 9680, 9720, 9032 on relay data/b505_c2_* and b506_c2_*; 38124, 6520 on data/b528_run_log.txt) and the seat`s own monitor`s tail and grep (32188, 1324); each stopped by PID with its command line read. '
    'The two tails on this session`s own task directory were left running.',
    '(c) THE SEAT`S G-NODE-LIST PREDICATE WAS DEFECTIVE AT THE FIRST PRE-PUSH RUN: it split the node list on newlines without stripping '
    'the file`s final newline, so its last element was empty and the check that the backmatter record is the list`s last line failed on '
    'a true list (the list itself verified line by line: the pin moved, every b596 line carried, the five nodes before the backmatter '
    'record). The predicate corrected through the Edit tool to strip the final newline; the suite re-run whole; the arm list unchanged.',
]


def defects():
    put_txt('b600_defects.txt', ['### b600 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('PLACE-papers OPEN_TRAILS: the work-order whole (REMAINDER 5, :12136), W-ORD-GRH-WEIL`s head and its remainders, the form, the '
     'precedence order, the research sequence, the generator-run line, b598`s and b599`s records', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11373, 11796, 11798, 11800, 11802, 11864, 12136, 12228, 12230, 12288, 12314, 12316, 12318, 12320, 12322, 12324, 12326, 12328, 12330,
      12336, 12348], 4000),
    ('PLACE-papers FINDINGS: the entry that priced the lemma (b589, :6718), its product line (:6730), its weight (:6738); b599`s entry', PP,
     PRE_PP, 'FINDINGS.md', [6718, 6730, 6738, 6928, 6944], 4000),
    ('relay the price bank the work-order cites, whole', RELAY, 'HEAD', 'data/b589_product_price.txt', list(range(1, 52))),
    ('SIDE-explicit-formula v0.17 Schema/Config.lean: the schema`s structure, the zero side, the criterion, the forward half', EFK, 'v0.17',
     'SIDEExplicitFormula/Schema/Config.lean', [13, 22, 24, 26, 28, 29, 31, 33, 34, 37, 38, 41, 44, 47]),
    ('SIDE-explicit-formula v0.17 Schema/Converse.lean: the criterion over the structure', EFK, 'v0.17', 'SIDEExplicitFormula/Schema/Converse.lean',
     [12, 237, 260, 265, 266]),
    ('SIDE-explicit-formula v0.17 Zeta23/Defs.lean: the reflection, the configuration, the window, the count', EFK, 'v0.17', 'Zeta23/Defs.lean',
     [124, 136, 138, 140, 141, 142, 143, 144, 146, 153, 162]),
    ('SIDE-explicit-formula v0.17 Zeta23/WeilEF/ZeroSummability.lean: the zero side summable on a configuration with a local count', EFK,
     'v0.17', 'Zeta23/WeilEF/ZeroSummability.lean', [29, 30, 179, 180, 181, 182, 183]),
    ('SIDE-explicit-formula v0.17 RestBound.lean: the local count', EFK, 'v0.17', 'SIDEExplicitFormula/RestBound.lean', [44, 45]),
    ('SIDE-explicit-formula v0.17 the house form of a new module: Simplicity.lean`s head', EFK, 'v0.17', 'SIDEExplicitFormula/Simplicity.lean',
     [1, 2, 3, 4, 17, 19, 21, 22, 26]),
    ('SIDE-explicit-formula v0.17 the salt-check gate`s form: SaltCheckSimplicity.lean', EFK, 'v0.17', 'SIDEExplicitFormula/SaltCheckSimplicity.lean',
     [1, 2, 3, 4, 6, 9, 11, 16, 17, 18, 98, 99, 107, 108]),
    ('SIDE-explicit-formula v0.17 the axiom audit`s form: AxiomCheckSimplicity.lean', EFK, 'v0.17', 'AxiomCheckSimplicity.lean', [1, 2, 4, 6, 14]),
    ('SIDE-explicit-formula v0.17 the off-line toy configuration the salt check reuses: Schema/Epstein.lean, Schema/SaltCheckEpstein.lean', EFK,
     'v0.17', 'SIDEExplicitFormula/Schema/Epstein.lean', [32, 34, 47, 52, 53]),
    ('SIDE-explicit-formula v0.17 Schema/SaltCheckEpstein.lean', EFK, 'v0.17', 'SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', [33, 56, 57, 58, 70, 88, 90]),
    ('PLACE-papers the ζ page at v0.17: head and the schema`s nodes', PP, PRE_PP, PAGE, [1, 3]),
    ('PLACE-papers the χ page at v0.17: head', PP, PRE_PP, DIR_PAGE, [1, 3]),
    ('PLACE-papers GRH_CASCADE v0.3.6: the per-instance premise (:45), the transport (:145)', PP, PRE_PP, GRH, [45, 145], 4000),
    ('PLACE-papers SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3: the Epstein setup (:290), the generalization (:325)', PP, PRE_PP, SIMP, [290, 325], 4000),
    ('relay b599`s closing push-out, committed at step zero', RELAY, 'HEAD', 'data/b599_closing_push_out.txt', list(range(1, 12))),
]


def reads():
    L = ['b600 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for rr in READS:
        label, repo, rev, path, sel = rr[:5]
        width = rr[5] if len(rr) > 5 else 900
        if rev == 'HEAD' and repo == RELAY and not g(repo, 'ls-files', path).strip():
            sl = io.open(os.path.join(ROOT, path), encoding='utf-8').read().split(NL)
            at = 'working tree'
        else:
            sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
            at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, at, len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    L += ['', '### SIDE-explicit-formula: v0.17 = %s ; main = %s ; tags %s ; the checkout`s branch %s' % (
        g(EFK, 'rev-parse', '--short=7', 'v0.17^{commit}').strip(), g(EFK, 'rev-parse', '--short=7', 'main').strip(),
        ' '.join(g(EFK, 'tag', '--sort=-creatordate').split()[:3]), g(EFK, 'branch', '--show-current').strip()),
          '### chain_page.py`s hold: %s' % [l for l in io.open(os.path.join(ROOT, 'tools', 'chain_page.py'), encoding='utf-8').read().split(NL)
                                             if l.startswith('HOLD_MB')]]
    put_txt('b600_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B599_ENTRY = '## CP-7, acts eighteen and nineteen: the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS from their'
GEN_LINE = '*Appended 2026-10-02 by b597 beneath the batch-refresh line (:12264), under `(R207)`(3) -- A GENERATOR RUN AT A NEW PIN, STANDING:*'
AMEND_HEAD = ('*Appended 2026-10-02 by b600 to the generator-run line (:%d), under `(R210)`(2), appended at the end and addressed to it (the '
              'ledgers append-only, the author’s answer at b599) -- THE LINE AMENDED:*')
AUTH_HEAD = '*Appended 2026-10-02 by b600, under the author’s ruling `(R210)`(3) -- THE AUTHORITY ORDER, STANDING:*'


def weight_line():
    """### PLACE-papers FINDINGS: b599's weight, one appended line addressed to b599's entry, in (R210)(1)'s facts."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B599_ENTRY)
    if entry != 6928:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    h1 = '*Appended 2026-10-02 by b600 to b599’s entry (:%d), under `(R210)`(1) -- b599 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, h1)
    t1 = ('\n%s SILENCE_STAGES_DEALIGNMENT v1.3 (ad82d5e) beside its current version, unedited: the Knill–Laflamme row naming the '
          'single-error syndrome condition knill_laflamme_t1 states, the field’s name kept, the docstring’s link noted as not compiled; the '
          'two “no terminal” rows citing d_eff_formula and silence_yields_protection at 6a4f482 as definitional T2; “We prove” read down to '
          'the §3 sketch; the five Silence Principle sentences excepted by name, the principle’s home phase1.5/structural/SILENCE_FORMAL.md '
          ':43 (silence_principle; silence_universal at :6 cited in the history line; the restatement at FOUNDATIONS :62 printed beside the '
          '(N1) score); the back matter stating no printed profile and naming W-ORD-SEC-AXIOM-ARTEFACT (OPEN_TRAILS :12330); H28a–H28c '
          'held, re-pin 71 of 71. REPARAMETERIZATION_BARRIERS v0.2 (31d4fa4): the pin named as current on its date, main 0256e9e with the '
          'blob unchanged; two “proved” phrasings read down to the compiled schema; H28a held VACUOUS (no MOVED row), H28b–H28c held, re-pin '
          '21 of 21. The alias on silence_principle at d3f32506 reaching the five sentences and no others; the erratum E-2026-10-02-1 at '
          'ERRATA :819 with its history line appended at OPEN_TRAILS :12328 addressed to :4540 (the ruling’s “beneath :4540” the '
          'navigator’s, the same placement error as (R187)(2)). FINDINGS :6924, :6926. Both pages re-emitted unchanged (neither edition '
          'names a page node), the arms and the frozen control 2 of 2. Relay 2b9f75cd, PLACE-papers bc1337a, TECHNE-Core untouched. The '
          'suite 79 of 79 before and after the push. (N2) refuted -- five fact corrections in SILENCE, the fifth :198’s “All rows pinned to '
          'v0.2.1” against the two Steane rows in SIDE-cosmo; (N4) refuted -- no Placement row gained; both the navigator’s. Defects (a)–(b) '
          'the seat’s, caught before any score or push. Nothing deposited; no kernel touched.\n' % h1)
    r = Q.append_to(Q.FIND, t1)
    put_json('b600_weight_line.json', dict(entry=entry, lines=[dict(head=h1, line=Q.line_of(Q.FIND, h1), append=r)]))
    print('  line :%s' % Q.line_of(Q.FIND, h1))


def rule_lines():
    """### PLACE-papers OPEN_TRAILS: (R210)(2), the generator-run line amended by a dated line appended at the end and addressed to
    ### :12288; (R210)(3), the authority order as a standing line."""
    Q = _Q()
    gl = Q.line_of(Q.OT, GEN_LINE)
    if gl != 12288:
        sys.exit('### THE ADDRESSED LINE MOVED: %s -- NOTHING WRITTEN' % gl)
    ah = AMEND_HEAD % gl
    for h in (ah, AUTH_HEAD):
        Q.guard_absent(Q.OT, h)
    t1 = ('\n%s the browser clause is struck -- the navigator seat runs in a browser and the author’s dual seats cannot run with it '
          'closed. The condition is the one the hold already states: a generator run at a new pin starts with free memory read above '
          'HOLD_MB (relay tools/chain_page.py :57, 2560 MB), one page per call in the foreground, and a run stopped by the harness is '
          'recorded as a stop, not an OOM. No line is added for the network: a failed push followed by ls-remote and a retry is a standing '
          'rule already, and a transient is not a reason for a line.\n' % ah)
    t2 = ('\n%s the programme is the A PLACE TO STAND research programme. The Zenodo deposits and the GitHub repositories under ongoing '
          'edit -- the keystones in their house format and the Lean kernels -- carry its assertions, conclusions, aims and objectives. The '
          'project workspace’s mirror is research history at every stage of edit and is not definitive where a more refined result '
          'supersedes it; the ledgers on D: are newer than any mirror. The navigator cites from the export and the seat’s prints, and not '
          'from the mirror where a newer edition exists.\n' % AUTH_HEAD)
    out = []
    for h, t in ((ah, t1), (AUTH_HEAD, t2)):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=h, line=Q.line_of(Q.OT, h), append=r))
    put_json('b600_rule_lines.json', dict(addressed=gl, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


BUILD_HEAD = ('*Appended 2026-10-02 by b600 beneath the amended generator-run line (:%d, amending :12288), under the author’s answer '
              'in b600 (relay data/b600_author_answers.txt) -- THE BUILD CLAUSE, STANDING:*')


def build_clause():
    """### PLACE-papers OPEN_TRAILS: the author's answer at b600's stop, appended at the end beneath the amendment as its build clause."""
    Q = _Q()
    rl = jl('b600_rule_lines.json')
    am = rl['lines'][0]['line']
    if Q.line_of(Q.OT, rl['lines'][0]['head']) != am:
        sys.exit('### THE AMENDMENT MOVED -- NOTHING WRITTEN')
    h = BUILD_HEAD % am
    Q.guard_absent(Q.OT, h)
    t = ('\n%s a kernel build runs as a detached process, started after free memory is read above the hold, and is watched by its PID '
         'and its log from the foreground in calls under 600 s, the seat kept awake; nothing is killed mid-write; one module per call. '
         'The harness’s reaper is a property of the harness’s background tasks, not of the machine, so the build is taken out of the '
         'harness’s hands. From b600’s first build of Product.lean, stopped by the reaper at t=600 s with no error (its defect (a)).\n' % h)
    r = Q.append_to(Q.OT, t)
    put_json('b600_build_clause.json', dict(head=h, line=Q.line_of(Q.OT, h), addressed=am, append=r))
    print('  build clause :%s' % Q.line_of(Q.OT, h))


# ================================================================================ COMPONENT 2: THE LEMMA
WORK_ORDER_LINE = 12136
# ### the work-order's statement, item by item, each beside the declaration that carries it and the check the declaration makes
ITEMS = [
    ('for two configurations of the schema', 'sum', r'def sum \(C₁ C₂ : WeilConfig\) : WeilConfig where'),
    ('the sum (carrier union', 'sum_carrier', r'theorem sum_carrier \(C₁ C₂ : WeilConfig\) : \(sum C₁ C₂\)\.carrier = C₁\.carrier ∪ C₂\.carrier := rfl'),
    ('multiplicities added', 'sum_mult', r'theorem sum_mult \(C₁ C₂ : WeilConfig\) \(ρ : ℂ\) : \(sum C₁ C₂\)\.mult ρ = onMult C₁ ρ \+ onMult C₂ ρ := rfl'),
    ('rhs added', 'sum_rhs', r'theorem sum_rhs \(C₁ C₂ : WeilConfig\) \(k : ℝ → ℂ\) : \(sum C₁ C₂\)\.rhs k = C₁\.rhs k \+ C₂\.rhs k := rfl'),
    ('targets conjoined)', 'sum_target', r'theorem sum_target \(C₁ C₂ : WeilConfig\) : \(sum C₁ C₂\)\.target ↔ C₁\.target ∧ C₂\.target := Iff\.rfl'),
    ('is a configuration', 'sum_ef', r'theorem sum_ef \(C₁ C₂ : WeilConfig\)'),
    ('and its criterion is the conjunction of the two by h2_sign_cfg_iff_target', 'ProductLemma',
     r'def ProductLemma : Prop :=\n  ∀ C₁ C₂ : WeilConfig, h2_sign_cfg \(sum C₁ C₂\) ↔ h2_sign_cfg C₁ ∧ h2_sign_cfg C₂'),
]
DECL = re.compile(r'^(theorem|def|structure|noncomputable def|abbrev) (\S+)')


def _headers(text):
    ls = text.split(NL)
    out = []
    for i, l in enumerate(ls):
        m = DECL.match(l)
        if not m:
            continue
        h = [l]
        j = i
        while not re.search(r':=|\bwhere\b', ls[j]) and j + 1 < len(ls):
            j += 1
            h.append(ls[j])
        out.append(dict(kind=m.group(1), name=m.group(2), line=i + 1, head=NL.join(h)))
    return out


def statements(key, suffix=''):
    """### the statements of one kernel file as written in the working tree of the branch, printed before its build; for `prod`, the
    ### work-order's statement beside the declarations that carry it (H34a's first half)."""
    rel = KFILES[key]
    b = open(os.path.join(EFK, rel), 'rb').read()
    t = b.decode('utf-8')
    hs = _headers(t)
    L = ['b600 -- THE STATEMENTS OF %s, PRINTED %s' % (rel, 'BEFORE THE BUILD' if not suffix else 'AGAIN AFTER THE FILE CHANGED (the first print kept beside)'), '']
    if suffix:
        first = {d['name']: d['head'] for d in jl('b600_statements_%s.json' % key)['decls']}
        now = {d['name']: d['head'] for d in hs}
        L += ['### against the first print: headers unchanged %s ; changed %s ; added %s ; gone %s' % (
            sorted(n for n in now if first.get(n) == now[n]), sorted(n for n in now if n in first and first[n] != now[n]),
            sorted(set(now) - set(first)), sorted(set(first) - set(now))), '']
    L += ['### written at (UTC) %s ; the branch %s (checked out: %s) ; the file`s sha256 %s ; its bytes %d' % (
        utc(), BRANCH, g(EFK, 'branch', '--show-current').strip(), sha(b), len(b)), '']
    items = []
    if key == 'prod':
        wo = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().split(NL)[WORK_ORDER_LINE - 1]
        L += ['### THE WORK-ORDER, OPEN_TRAILS :%d, WHOLE:' % WORK_ORDER_LINE, '    ' + wo, '',
              '### ITS STATEMENT, ITEM BY ITEM, BESIDE THE DECLARATION THAT CARRIES IT:']
        for words, name, rx in ITEMS:
            inwo = words in wo
            found = re.search(rx, t) is not None
            items.append(dict(words=words, decl=name, in_work_order=inwo, declared=found))
            L.append('    %-74s -> %-20s in the work-order %s ; declared as printed %s' % ('“%s”' % words, name, inwo, found))
        L.append('### ### **%s**' % ('EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' if all(i['in_work_order'] and i['declared'] for i in items)
                                     else '### AN ITEM NOT CARRIED'))
        L.append('')
    for h in hs:
        L.append('### :%d %s %s' % (h['line'], h['kind'], h['name']))
        L += ['    ' + x for x in h['head'].split(NL)]
    put_txt('b600_statements_%s%s.txt' % (key, suffix), L)
    put_json('b600_statements_%s%s.json' % (key, suffix), dict(file=rel, sha256=sha(b), at=utc(), decls=hs, items=items))


def build_bank(key, logpath):
    """### the watchdog's build log copied into relay data/b600_build_<key>.txt with a head line."""
    src = io.open(logpath, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    hdr = ('### b600 -- COMPONENT 2: THE BUILD OF %s ON %s, ONE MODULE PER CALL, THE WATCHDOG`S LOG (lean resident cap 3500 MB, free '
           'floor 900 MB; the seat starts no call below the 2560 MB hold), copied from the seat`s scratchpad' % (key, BRANCH))
    put_txt('b600_build_%s.txt' % key, [hdr, ''] + src.rstrip(NL).split(NL))


def prints(logpath):
    """### the Lean output of the axiom-check run (the watchdog's log, its `  | ` lines), banked as data/b600_prints.txt / .json."""
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    L = ['b600 -- THE PRINTS: `lake env lean %s` at SIDE-explicit-formula %s (checked out: %s, HEAD %s), the watchdog`s run' % (
        AXF, BRANCH, g(EFK, 'branch', '--show-current').strip(), g(EFK, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out
    put_txt('b600_prints.txt', L)
    put_json('b600_prints.json', dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a],
                                      std3=all(set(a) <= set(STD3) for a in ax.values()), exit=ex[-1] if ex else None,
                                      errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt))
    print('  prints', len(ax), 'std3', all(set(a) <= set(STD3) for a in ax.values()))


def e0(key):
    """### every declaration of one kernel file graded by the shared E0 rule (tools/e0_rule.py) at the branch tip, with its print."""
    import b569_record as R9
    import e0_rule as E0
    st = jl('b600_statements_%s_final.json' % key) if os.path.exists(os.path.join(D, 'b600_statements_%s_final.json' % key)) \
        else jl('b600_statements_%s.json' % key)
    P0 = jl('b600_prints.json')['axioms']
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    src = g(EFK, 'show', '%s:%s' % (tip, st['file']))
    rows = {}
    L = ['b600 -- THE E0 READ OF %s AT THE BRANCH TIP %s (%s)' % (st['file'], tip[:7], BRANCH)] + E0.RULE_TEXT + [
        '### the file at the tip is the one printed: %s' % (sha(src) == st['sha256']), '']
    for d in st['decls']:
        n = NS + ('SaltCheck.' if key == 'salt' else '') + d['name']
        kind = 'theorem' if d['kind'] == 'theorem' else 'def'
        head, _ln = R9.header_of(src, d['name'])
        gr, why, _b = E0.grade(head or '', kind)
        ax = P0.get(n)
        rows[n] = dict(grade=gr if kind == 'theorem' else 'DEF', why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, kind=kind)
        L.append('    %-34s %-10s %s  -- %s' % (d['name'], rows[n]['grade'], 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    gate = all(r['std3'] for r in rows.values()) and all(r['head'] is not None or r['kind'] == 'def' for r in rows.values())
    L.append('### ### **THE GATE: %s** -- declarations %d, theorems %d (DERIVES %d, INTERFACES %d)' % (
        'PASS' if gate else 'FAIL', len(rows), sum(1 for r in rows.values() if r['kind'] == 'theorem'),
        sum(1 for r in rows.values() if r['grade'] == 'DERIVES'), sum(1 for r in rows.values() if r['grade'] == 'INTERFACES')))
    put_txt('b600_e0_%s.txt' % key, L)
    put_json('b600_e0_%s.json' % key, dict(rows=rows, gate=gate, tip=tip, file=st['file'], same_file=sha(src) == st['sha256']))


# ### THE FEDERATION WALK. LOOSE: a theorem header naming the criterion over the structure, the sum or the Prop. STRICT: a conclusion
# ### that IS the Prop (ProductLemma, or the criterion of a sum iff the conjunction of the parts' criteria) or its negation.
FED_PAT = r'h2_sign_cfg|ProductLemma|WeilConfig'
STRICT_POS = re.compile(r'^\s*((SIDEExplicitFormula\.)?(Product\.)?ProductLemma|'
                        r'h2_sign_cfg\s*\((?:Product\.)?sum\s+\S+\s+\S+\)\s*↔\s*h2_sign_cfg\s+\S+\s*∧\s*h2_sign_cfg\s+\S+)\s*$')
STRICT_NEG = re.compile(r'^\s*(¬\s*\(?\s*(SIDEExplicitFormula\.)?(Product\.)?ProductLemma\s*\)?|'
                        r'¬\s*\(\s*h2_sign_cfg\s*\((?:Product\.)?sum\s+\S+\s+\S+\)\s*↔[^)]*\))\s*$')
LOOSE = re.compile(r'(ProductLemma|\bsum\s+\S+\s+\S+|h2_sign_cfg\s+\S+\s*∧\s*h2_sign_cfg)')


def _strict_controls():
    """### each strict shape on a conclusion it must read and one it must not; RETURNS the four results (all True to pass)."""
    return dict(pos_reads=bool(STRICT_POS.search(' h2_sign_cfg (sum C₁ C₂) ↔ h2_sign_cfg C₁ ∧ h2_sign_cfg C₂')),
                pos_refuses=not STRICT_POS.search(' h2_sign_cfg C ↔ C.target'),
                neg_reads=bool(STRICT_NEG.search(' ¬ ProductLemma')),
                neg_refuses=not STRICT_NEG.search(' ¬ h2_sign_cfg C'))


def _decl_heads(text):
    out = []
    for m in re.finditer(r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?(?:(?:private|protected|nonrec)[ \t]+)*(theorem|lemma)[ \t]+(\S+)(.*?):=', text, re.M | re.S):
        out.append((text[:m.start()].count(NL) + 1, m.group(2), ' '.join((m.group(2) + m.group(3)).split())))
    return out


def fed_walk():
    """### every kernel's HEAD by git grep, every theorem/lemma header naming the criterion over the structure, the configuration or the
    ### Prop, its conclusion classified. RETURNS (rows, kernels, files)."""
    kernels = sorted(d for d in os.listdir('D:/') if d.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d, '.git')))
    rows, files = [], 0
    for k in kernels:
        rep = 'D:/' + k
        out = g(rep, 'grep', '-l', '-I', '-E', FED_PAT, 'HEAD', '--', '*.lean')
        for f in [x.split(':', 1)[1] for x in out.split(NL) if x.strip()]:
            files += 1
            t = g(rep, 'show', 'HEAD:' + f)
            for ln, name, head in _decl_heads(t):
                if not re.search(FED_PAT, head):
                    continue
                depth, cut = 0, -1
                for i, ch in enumerate(head):
                    if ch in '([{⟨':
                        depth += 1
                    elif ch in ')]}⟩':
                        depth -= 1
                    elif ch == ':' and depth == 0 and head[i:i + 2] != ':=':
                        cut = i
                concl = head[cut + 1:] if cut >= 0 else head
                own = k == 'SIDE-explicit-formula' and f in OWN
                if own:
                    cls = 'OWN'
                elif STRICT_NEG.search(concl):
                    cls = 'NEGATES'
                elif STRICT_POS.search(concl):
                    cls = 'CONCLUDES'
                elif LOOSE.search(concl):
                    cls = 'READ'
                else:
                    cls = 'OTHER'
                rows.append(dict(kernel=k, file=f, line=ln, name=name, cls=cls, conclusion=concl[:300], reading=HAND.get((f, name)) if cls == 'READ' else None))
    return rows, kernels, files


HAND = {}


def grep_bank():
    """### (N3): the federation searched by git grep at every kernel's HEAD for a declaration concluding the Prop or its negation; the
    ### strict shapes exercised; the act's own files marked OWN. data/b600_grep.txt / .json."""
    rows, kernels, files = fed_walk()
    bad = [r for r in rows if r['cls'] in ('CONCLUDES', 'NEGATES') or (r['cls'] == 'READ' and not r['reading'])]
    ctl = _strict_controls()
    L = ['b600 -- COMPONENT 2: THE FEDERATION SEARCHED FOR A DECLARATION CONCLUDING THE PRODUCT LEMMA OR ITS NEGATION (UTC %s)' % utc(), '',
         '### git grep -l -E "%s" at HEAD of every kernel (%d), %d files; every theorem/lemma header naming one, its conclusion (the header '
         'after its last top-level colon) classified: CONCLUDES / NEGATES by the strict shapes, READ by the loose one, OTHER, OWN (this act`s '
         'files)' % (FED_PAT, len(kernels), files)]
    for r in rows:
        if r['cls'] != 'OTHER':
            L.append('    %-9s %s %s:%d %s -- %s' % (r['cls'], r['kernel'], r['file'], r['line'], r['name'], r['conclusion'][:180]))
            if r['cls'] == 'READ':
                L.append('              ### the seat`s hand reading: %s' % (r['reading'] or '### NONE -- COUNTED'))
    L += ['### OTHER rows (named the pattern, conclusion not the Prop) %d: %s' % (sum(r['cls'] == 'OTHER' for r in rows),
                                                                               ', '.join('%s:%s' % (r['file'].split('/')[-1], r['name']) for r in rows if r['cls'] == 'OTHER')[:3000]),
          '### headers %d ; CONCLUDES %d ; NEGATES %d ; READ %d (hand-read %d) ; OTHER %d ; OWN %d' % (
              len(rows), sum(r['cls'] == 'CONCLUDES' for r in rows), sum(r['cls'] == 'NEGATES' for r in rows), sum(r['cls'] == 'READ' for r in rows),
              sum(r['cls'] == 'READ' and bool(r['reading']) for r in rows), sum(r['cls'] == 'OTHER' for r in rows), sum(r['cls'] == 'OWN' for r in rows)),
          '### the strict shapes, each exercised: %s' % ctl,
          '', '### ### **OUTSIDE THIS ACT`S OWN FILES, DECLARATIONS CONCLUDING THE PROP OR ITS NEGATION : %d**' % len(bad)]
    put_txt('b600_grep.txt', L)
    put_json('b600_grep.json', dict(rows=rows, kernels=kernels, files=files, bad=bad, controls=ctl))
    print('  headers', len(rows), 'bad', len(bad), 'own', sum(r['cls'] == 'OWN' for r in rows), ctl)


# ================================================================================ THE NODE LIST AND THE PAGES
NODE_HEAD = ['# b600 -- THE ζ NODE LIST AT v0.18, (R210)(4): b596`s list (relay data/b596_nodes_faces.txt, every record line unchanged,',
             '# its backmatter record kept) with five declarations of SIDEExplicitFormula/Product.lean appended, the pin moved to v0.18.',
             '# Every cell is elaborated by the generator`s probe at the pin, never typed here.', '#']
NODE_ADD = [NS + 'sum | kernel | added: (R210)(4), the sum of two configurations of the schema (the work-order`s object)',
            NS + 'sum_ef | kernel | added: (R210)(4), the summed explicit formula, the work-order`s lemma of substance',
            NS + 'ProductLemma | kernel | added: (R210)(4), the product lemma as a Prop',
            NS + 'h2_sign_cfg_sum_iff_targets | kernel | added: (R210)(4), the criterion of the sum the conjunction of the targets',
            NS + 'productLemma_holds | kernel | added: (R210)(4), the product lemma proved']


def node_list():
    """### data/b600_nodes_zeta.txt: b596's ζ list (faces), the pin moved to v0.18, the five Product nodes appended before its
    ### backmatter record (the backmatter record stays the list's last line)."""
    z = rd('b596_nodes_faces.txt').rstrip(NL).split(NL)
    if z.count('# pin: v0.17') != 1 or not z[-1].startswith('# backmatter: '):
        sys.exit('### b596`s ζ list does not carry its pin once, or its backmatter record last -- NOTHING WRITTEN')
    body = [('# pin: v0.18' if l == '# pin: v0.17' else l) for l in z[:-1]]
    put_txt('b600_nodes_zeta.txt', NODE_HEAD + body + NODE_ADD + [z[-1]])


NODES = {'zeta': 'b600_nodes_zeta.txt', 'chi': 'b596_nodes_chi.txt'}
PROBE = {'zeta': 'b600_probe_out.txt', 'chi': 'b596_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}


def free_mb():
    try:
        out = subprocess.run(['powershell', '-NoProfile', '-Command', '(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory'],
                             capture_output=True, text=True).stdout
        return int(out.strip()) // 1024
    except Exception:
        return -1


def cr0(b):
    return (b or b'').replace(b'\r\n', b'\n')


def page(k):
    """### after the tag: ONE page per call in the foreground. `zeta`: a full run at v0.18 from data/b600_nodes_zeta.txt (free memory read
    ### before the call against the hold; the probe banked as data/b600_probe_out.txt and .lean.txt); `chi`: re-emitted from b596's v0.17
    ### list and banked probe. Writes the page only when it changed, and data/b600_page_<k>.json."""
    import shutil
    import difflib
    import chain_page as C
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b600_%s' % k)
    fm = free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, C.HOLD_MB))
    if k == 'zeta' and 0 <= fm < C.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    frm = None if k == 'zeta' else os.path.join(D, PROBE[k])
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), pdir, frm)
    secs = int(time.time() - t0)
    for l in log:
        print('  %s: %s' % (k, l))
    if rc:
        put_json('b600_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    if frm is None:
        shutil.copyfile(os.path.join(pdir, 'chain_page_probe_out.txt'), os.path.join(D, PROBE[k]))
        shutil.copyfile(os.path.join(pdir, 'chain_page_probe.lean'), os.path.join(D, PROBE[k].replace('_out.txt', '.lean.txt')))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    new = [dict(name=n, grade=meta['cells'][n].get('grade'), tier=meta['cells'][n].get('tier'), premises=meta['cells'][n].get('premises'),
                axioms=meta['cells'][n].get('axioms'), entry=meta['cells'][n].get('entry'), module=meta['cells'][n].get('module'))
           for n in NEW_NODES if n in (meta.get('cells') or {})]
    rows = {n: [l for l in b.decode('utf-8').split(NL) if ('`%s`' % n) in l or (' %s ' % n) in l][:2] for n in NEW_NODES}
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             free_mb_before=fm, seconds=secs, new=new, rows=rows, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), log=log)
    put_json('b600_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in new:
        print('    NEW NODE %s -- %s ; tier %s ; premises %s ; axioms %s ; entry %s' % (x['name'], x['grade'], x['tier'], x['premises'], x['axioms'], x['entry']))
    for x in dl[:80]:
        print('    ' + x[:240])


def page_arms(tag):
    """### both page arms at PLACE-papers HEAD from this act's ζ list and probe and b596's χ list and probe, and the frozen control.
    ### Writes data/b600_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    L = ['b600 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b600_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = T.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b600_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE BEARING
BEARING = [
    (GRH, 45, 'carried-open premise for each instance',
     'The sentence carries the cascade’s open node per instance, at ζ and at each primitive χ ≠ 1, each instance of '
     '`h2_sign_cfg_iff_target`. The product lemma composes the instances: for any two configurations of the schema, Weil positivity on '
     'classK of their sum is the conjunction of the two (`productLemma_holds`, SIDE-explicit-formula v0.18), and the sum’s criterion is the '
     'conjunction of the two targets (`h2_sign_cfg_sum_iff_targets`). So a finite set of the sentence’s per-instance premises is one '
     'premise of the same form, over the sum of their configurations: the joint statement (at ζ and one χ, RH and GRH_chi together) is '
     'itself an instance of the schema’s criterion, and the sentence’s “every step of the cascade inherits this single open premise rather '
     'than adding its own” holds at the sum as well -- the sum adds no open node of its own. What does not move: each premise stays open; '
     'nothing here names the sum of the ζ and χ configurations as the zeros of a product of L-functions, or identifies it with a Dedekind '
     'zeta function -- that identification is the work-order’s separate item.'),
    (SIMP, 290, 'decomposes into a sum of Dedekind zetas',
     'The sentence sets the additive sum (Epstein as a sum of Dedekind zetas) against the Euler product. The compiled sum is the other '
     'side: its carrier is the union of the parts’ zeros with their multiplicities added and its arithmetic side the two arithmetic sides '
     'added -- the zero configuration and explicit formula of a product of functions, each part bringing its own. It does not reach an '
     'additive sum of zeta functions, whose zeros are not the union of the summands’ zeros. Read beside the salt-check: the sum of a '
     'configuration on the line and b590’s two-point toy configuration off the line (the bench’s Epstein point rhoE) is not Weil-positive '
     '(`product_part_load_bearing`, v0.18), so an off-line part is never hidden by a sum. The sentence’s distinction stands, and the '
     'compiled lemma sits on its product side only.'),
]


def bearing():
    """### the keystone sentences the lemma bears on, each printed from its current version at PLACE-papers HEAD by path and line, the
    ### lemma's reading beside it; data/b600_bearing.txt / .json."""
    L = ['b600 -- COMPONENT 2: THE BEARING -- THE KEYSTONE SENTENCES THE PRODUCT LEMMA CHANGES THE READING OF, EACH PRINTED BY PATH AND LINE '
         'FROM ITS CURRENT VERSION AT PLACE-papers %s, THE LEMMA`S READING BESIDE IT (UTC %s)' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc()),
         '### the search: the keystones` current versions grepped for each instance, both instances, instances of, joint conclusion, Euler '
         'product, Dedekind, product of an L-function or zeta, sum of configurations -- the residue hand-read; two sentences bear, the rest '
         'name the Euler product as a structural component or a reference and are not moved by a lemma about the schema`s sum.', '']
    rows = []
    for path, ln, needle, reading in BEARING:
        line = g(PP, 'show', 'HEAD:' + path).split(NL)[ln - 1]
        ok = needle in line
        rows.append(dict(path=path, line=ln, needle=needle, found=ok, sentence=line, reading=reading))
        L += ['### %s :%d%s' % (path, ln, '' if ok else '   ### THE NEEDLE IS NOT ON THE CITED LINE'),
              '    THE SENTENCE: ' + line, '    THE READING: ' + reading, '']
    L.append('### ### **SENTENCES PRINTED AS BEARING : %d ; ON THEIR CITED LINES : %d**' % (len(rows), sum(r['found'] for r in rows)))
    put_txt('b600_bearing.txt', L)
    put_json('b600_bearing.json', dict(rows=rows, at=utc()))


# ================================================================================ THE PROMPTS, BANKED VERBATIM
def answers():
    """### every AskUserQuestion of this session, with question, options, recommended mark and the answer, read from the session
    ### transcript (b595's method); data/b600_author_answers.txt."""
    calls, results = [], {}
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
        try:
            o = json.loads(raw)
        except Exception:
            continue
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input']))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                results[c.get('tool_use_id')] = (i, t)
    L = ['### b600 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-02), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 35432614-be58-48b9-8b45-54387165dcef, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b600_author_answers.txt', L)


# ================================================================================ COMPONENT 3: THE RECORD
SCORE_KEYS = ('H34a', 'H34b', 'H34c', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def _first_build_ok():
    b = rd('b600_build_prod.txt')
    m = re.findall(r'^### EXIT rc=(\S+) ', b, re.M)
    return bool(m) and m[0] == '0' and not os.path.exists(os.path.join(D, 'b600_statements_prod_final.json'))


def scores():
    st = jl('b600_statements_prod.json')
    pr, ep, es = jl('b600_prints.json'), jl('b600_e0_prod.json'), jl('b600_e0_salt.json')
    gp, br = jl('b600_grep.json'), jl('b600_bearing.json')
    Z, X = jl('b600_page_zeta.json'), jl('b600_page_chi.json')
    salt_names = [NS + 'SaltCheck.' + n for n in ('product_satisfiable', 'product_part_load_bearing', 'product_sum_not_forced')]
    salt_ok = all(es['rows'].get(n, {}).get('std3') for n in salt_names)
    items_ok = bool(st.get('items')) and all(i['in_work_order'] and i['declared'] for i in st['items'])
    pl = ep['rows'].get(THE_NODE, {})
    se = ep['rows'].get(NS + 'sum_ef', {})
    proved = bool(pl.get('std3')) and bool(se.get('std3')) and not pr.get('sorry') and pr.get('std3') is True and ep.get('gate') and es.get('gate')
    zn = {x['name']: x for x in Z.get('new', [])}
    node_g = zn.get(THE_NODE, {}).get('grade')
    on_page = bool(Z.get('rows', {}).get(THE_NODE))
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle')}
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    kern_ok = kern['SIDE-explicit-formula'] == tagc and {k: v for k, v in kern.items() if k != 'SIDE-explicit-formula'} == {
        'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30',
        'SIDE-silence-principle': '667c254'}
    kfiles = sorted(x for x in g(EFK, 'diff', '--name-only', PRE_KER, TAG).split(NL) if x.strip())
    kmerges = [x for x in g(EFK, 'rev-list', '--merges', '%s..%s' % (PRE_KER, TAG)).split(NL) if x.strip()]
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + [p['page'] for p in (Z, X) if p.get('changed')])
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b600_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b599_closing_push_out.txt'))
    bear = [r for r in br.get('rows', []) if r['found']]
    S = dict(
        H34a=('HOLDS' if items_ok and salt_ok else 'REFUTED',
              'the work-order`s statement item by item carried by a declaration %s (data/b600_statements_prod.txt) ; the salt-check`s three '
              'theorems at the standard three %s (%s)' % (items_ok, salt_ok, ', '.join(n.split('.')[-1] for n in salt_names))),
        H34b=('HOLDS' if proved else 'REFUTED',
              'productLemma_holds %s, sum_ef %s ; sorryAx %s ; every print at the standard three %s ; the E0 gates %s / %s' % (
                  pl.get('axioms'), se.get('axioms'), pr.get('sorry') or 'NONE', pr.get('std3'), ep.get('gate'), es.get('gate'))),
        H34c=('HOLDS' if node_g == 'DERIVES' and on_page else 'REFUTED',
              'the node %s on the ζ page at %s graded %s, its row printed %s' % (THE_NODE.split('.')[-1], TAG, node_g, on_page)),
        N1=('HELD' if _first_build_ok() and items_ok and salt_ok else 'REFUTED',
            'the first completed build of Product.lean exit %s with the file unchanged after it %s (the attempt before it stopped by the '
            'harness at t=600 s with no error printed, data/b600_build_prod_attempt1.txt) ; the statement carried %s ; the salt check %s' % (
                (re.findall(r'^### EXIT rc=(\S+) ', rd('b600_build_prod.txt'), re.M) or ['?'])[0],
                not os.path.exists(os.path.join(D, 'b600_statements_prod_final.json')), items_ok, salt_ok)),
        N2=('HELD' if proved else 'REFUTED', 'the proof closed within the act at the standard three: %s' % proved),
        N3=('HELD' if gp.get('bad') == [] else 'REFUTED', 'outside the act`s own files, declarations concluding the Prop or its negation: %d '
                                                         '(of %d headers in %d kernels)' % (len(gp.get('bad') or []), len(gp.get('rows') or []), len(gp.get('kernels') or []))),
        N4=('HELD' if len(bear) >= 2 else 'REFUTED', 'keystone sentences printed as bearing: %d (%s)' % (len(bear), ', '.join('%s :%d' % (r['path'].split('/')[-1], r['line']) for r in bear))),
        N5=('HELD' if kern_ok and not kmerges and kfiles == sorted(OWN) and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
            'nothing deposits; SIDE-explicit-formula main at the tag %s, the other mains unmoved %s; the kernel`s files %s..%s %s, merges %d; '
            'PLACE-papers %s; relay files beyond the act`s own banks and tools and the table: %s' % (
                tagc, kern_ok, PRE_KER, TAG, kfiles, len(kmerges), pp_ch, relay_beyond)),
        S1=('HELD' if proved and es.get('gate') and ep.get('gate') else 'REFUTED',
            'every declaration of Product.lean (%d) and SaltCheckProduct.lean (%d) at the standard three, no sorryAx: %s' % (
                len(ep.get('rows', {})), len(es.get('rows', {})), ep.get('gate') and es.get('gate') and not pr.get('sorry'))),
        S2=('HELD' if salt_ok and all(es['rows'].get(n, {}).get('grade') == 'DERIVES' for n in salt_names) else 'REFUTED',
            'the salt-check`s three theorems, each DERIVES at the standard three: %s' % [(n.split('.')[-1], es['rows'].get(n, {}).get('grade')) for n in salt_names]),
        S3=('HELD' if Z.get('changed') is True and len(zn) == len(NEW_NODES) and X.get('changed') is False else 'REFUTED',
            'the ζ page re-emitted at %s changed %s with %d of the five nodes ; the χ page changed %s' % (TAG, Z.get('changed'), len(zn), X.get('changed'))),
        S4=('HELD' if gp.get('bad') == [] and all(gp.get('controls', {}).values()) and any(r['cls'] == 'OWN' for r in gp.get('rows', [])) else 'REFUTED',
            'no declaration outside the act`s files concluding the Prop or its negation ; the strict shapes exercised %s ; the act`s own '
            'declarations found by the same walk %s' % (gp.get('controls'), any(r['cls'] == 'OWN' for r in gp.get('rows', [])))),
        S5=('HELD' if [(r['path'], r['line']) for r in bear] == [(GRH, 45), (SIMP, 290)] else 'REFUTED',
            'the bearing sentences: %s' % [(r['path'].split('/')[-1], r['line']) for r in bear]),
    )
    put_json('b600_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-6s %s -- %s' % (k, S[k][0], S[k][1][:220]))


TITLE = None


def _title():
    S = jl('b600_scores.json')
    proved = S['H34b'][0] == 'HOLDS'
    return ('## REMAINDER 5: the product lemma as a salt-checked Prop at SIDE-explicit-formula %s, %s, its bearing on GRH_CASCADE :45 and '
            'SIMPLICITY_OF_RIEMANN_ZEROS :290 read' % (TAG, 'proved at the standard three' if proved else 'carried to its named obligations'))


TRAIL_HEAD = ('### b600 — lane three, act twenty-seven under (R210): REMAINDER 5 -- the product lemma stated as a salt-checked Prop and '
              'proved; the generator-run line amended; the authority order entered')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, wl, rl = jl('b600_scores.json'), jl('b600_weight_line.json'), jl('b600_rule_lines.json')
    Z, X, gp = jl('b600_page_zeta.json'), jl('b600_page_chi.json'), jl('b600_grep.json')
    title = _title()
    Q.guard_absent(Q.FIND, title[:90])
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    zcommit = _pp_commit('b600 (R210)(4): THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
    e = ['', title, '',
         '*Filed at b600 on the author’s ruling `(R210)`. Banks: relay `data/b600_statements_prod.txt`, `data/b600_build_prod.txt`, '
         '`data/b600_prints.txt`, `data/b600_e0_prod.txt`, `data/b600_e0_salt.txt`, `data/b600_grep.txt`, `data/b600_page_zeta.json`, '
         '`data/b600_page_arms_c2.txt`, `data/b600_bearing.txt`, `data/b600_reads.txt`. Nothing deposits.*', '',
         '**The lemma** (`(R210)`(4), by the work-order at OPEN_TRAILS :12136). SIDE-explicit-formula %s = `%s` (merged and tagged by '
         'push_gated.sh after read-back; the branch %s kept): `SIDEExplicitFormula/Product.lean` -- the sum of two configurations of the '
         'schema, `sum`, its carrier the union, each multiplicity read on its own carrier and the two added, the arithmetic sides added, the '
         'targets conjoined; the summed explicit formula `sum_ef`, each zero side summable by the count its part carries '
         '(`Zeta23.WeilEF.EF_zero_sum_summable_gen`) so the zero side over the union is the two added; the count of the sum the two counts '
         'added (`sumZ_N`, `sumZ_count`); the Prop `ProductLemma`, Weil positivity on classK of the sum iff that of both parts, and '
         '`productLemma_holds`, by `h2_sign_cfg_iff_target` at the sum and at each part. The salt-check `SaltCheckProduct.lean`: a sum with '
         'a point Weil-positive, and each part load-bearing -- b596’s point on the line beside b590’s off-line toy pair gives a sum that is '
         'not Weil-positive, in either order. All at the standard three, no sorryAx (relay data/b600_prints.txt). The ζ page re-emitted at '
         '%s with five Product nodes, `productLemma_holds` graded %s there (PLACE-papers %s); the χ page unchanged. The federation walk '
         'finds no declaration outside this act’s files concluding the Prop or its negation (%d headers).' % (
             TAG, tagc, BRANCH, TAG, (S['H34c'][1].split(' graded ')[1].split(',')[0] if ' graded ' in S['H34c'][1] else '?'), zcommit,
             len(gp.get('rows') or [])), '',
         '**Its bearing** (relay data/b600_bearing.txt). GRH_CASCADE v0.3.6 :45 carries the cascade’s open node per instance; the lemma '
         'makes a finite set of those premises one premise of the same form over the sum of their configurations, the sum adding no open '
         'node of its own. SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3 :290 sets the additive sum of Dedekind zetas against the Euler product; the '
         'compiled sum is the product side only -- the union of the zeros with multiplicities added -- and an off-line part is never hidden '
         'by it. Neither sentence’s open premise moves; the identification of the sum of the ζ and χ_d configurations with a Dedekind zeta '
         'function stays the work-order’s separate item.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the lemma re-reads the schema of b573 (`h2_sign_cfg_iff_target`, v0.15) and the '
         'price of b589 (FINDINGS :6718, :6730), which it meets at one lemma of substance as priced; it reuses the off-line toy pair of b590 '
         '(FINDINGS :6740) and the on-line toy of b596 (:6856) as its salt; and it is re-read by REMAINDER 2, the family form over χ mod q '
         '(OPEN_TRAILS :11798), whose sum of χ-forms is a finite iterate of this sum. It strengthens the programme’s offering of the schema '
         'and its instances: two instances now compose inside the schema, the composite’s criterion compiled.', '',
         '**The record lines.** b599’s weight at FINDINGS :%d; the generator-run line amended at OPEN_TRAILS :%d, addressed to :%d; the '
         'authority order at :%d; the build clause, by the author’s answer at the build’s stop, at :%d.' % (
             wl['lines'][0]['line'], rl['lines'][0]['line'], rl['addressed'], rl['lines'][1]['line'], jl('b600_build_clause.json')['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R210)`(5): b601, W-ORD-KEIPER-FACE (two lemmas), the research sequence’s third item. The author rules on the '
         'closing.', '',
         '*Nothing deposits; no keystone edited; README and REGISTRY unwritten; nothing here is a statement about RH, GRH or any zero beyond '
         'the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b600_findings.json', dict(entry_line=Q.line_of(Q.FIND, title[:90]), title=title, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title[:90]))


def trail():
    Q = _Q()
    S, fj, wl, rl = jl('b600_scores.json'), jl('b600_findings.json'), jl('b600_weight_line.json'), jl('b600_rule_lines.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    rows_ = ['', TRAIL_HEAD, '',
             '**(R210) ratified.** (1) b599 at its weight. (2) The generator-run line amended. (3) The authority order, standing. (4) '
             'REMAINDER 5, the product lemma, as the research act. (5) The act after: b601.', '',
             '**Entered:** FINDINGS.md:%d (b599’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the amendment, '
             'addressed to :%d), :%d (the authority order), this record; SIDE-explicit-formula %s = `%s` (Product.lean, SaltCheckProduct.lean, '
             'AxiomCheckProduct.lean); the ζ page re-emitted at %s.' % (
                 wl['lines'][0]['line'], fj['entry_line'], rl['lines'][0]['line'], rl['addressed'], rl['lines'][1]['line'], TAG, tagc, TAG), '',
             '**Answered by the author at the build’s stop** (relay data/b600_author_answers.txt): the build resumed as a detached '
             'process watched from the foreground; the build clause appended beneath the amendment at :%d. The six old `tail -f` '
             'orphans are the seat’s defects as logged (b600’s (b)).' % jl('b600_build_clause.json')['line'], '',
             '**Resolved by the seat, for the author’s strike:** the amendment “beneath :12288” appended at the ledger’s end and addressed to '
             ':12288, by the author’s answer at b599 (the ledgers append-only); the five Product nodes placed on the ζ page, as b596 placed '
             'Simplicity’s, since the ζ page’s Correspondence takes every graded non-schema kernel name and a χ-only placement would leave '
             'the ζ page’s re-emission from b596’s list unable to resolve them once graded; the bearing sentences chosen by a search of the '
             'keystones’ current versions, its residue hand-read (relay data/b600_bearing.txt).', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R210)`(5), b601, W-ORD-KEIPER-FACE (two lemmas), the research sequence’s third item; the author rules on the '
             'closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no keystone edited; FACES_LEDGER untouched; row U1 unedited; `h2` where the '
             'deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b600_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b600_trail.json')['line'])


def desk():
    S = jl('b600_scores.json')
    HK = ('H34a', 'H34b', 'H34c')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b600 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H34a-H34c, (R210)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H34 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HK), sum(S[k][0] == 'REFUTED' for k in HK),
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b600_defects.txt').rstrip(NL).split(NL)
    put_txt('b600_desk_notes.txt', L)


def components():
    S, fj, tj, wl, rl = jl('b600_scores.json'), jl('b600_findings.json'), jl('b600_trail.json'), jl('b600_weight_line.json'), jl('b600_rule_lines.json')
    Z, X = jl('b600_page_zeta.json'), jl('b600_page_chi.json')
    tagc = g(EFK, 'rev-parse', '--short=7', TAG + '^{commit}').strip()
    L = ['b600 -- THE COMPONENTS, BANKED UNDER (R210).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b599`s closing push-out relay %s ; push-b599* branches deleted by name '
         '(data/b600_branches.txt) ; the kept branches untouched ; the work-order printed whole (data/b600_reads.txt) ; the suite run at HEAD '
         'before the face (data/b600_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b599`s weight FINDINGS :%d ; the generator-run line amended OPEN_TRAILS :%d (addressed to :%d) ; the authority '
         'order :%d' % (wl['lines'][0]['line'], rl['lines'][0]['line'], rl['addressed'], rl['lines'][1]['line']),
         '### COMPONENT 2 : SIDE-explicit-formula %s = %s on %s merged ; H34a %s, H34b %s, H34c %s ; the ζ page changed %s, the χ page '
         'changed %s ; the bearing data/b600_bearing.txt' % (TAG, tagc, BRANCH, S['H34a'][0], S['H34b'][0], S['H34c'][0], Z.get('changed'), X.get('changed')),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b601, W-ORD-KEIPER-FACE ; N1 %s, N2 %s, N3 %s, '
         'N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b600_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b600_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
