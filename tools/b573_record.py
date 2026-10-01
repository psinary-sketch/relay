# -*- coding: utf-8 -*-
"""b573_record.py -- THE ACT'S RECORD TOOL, UNDER (R183). ### ONE SUBCOMMAND PER BANK.

### ### b573: LANE TWO, ACT THIRTEEN -- GRH-WEIL ACT EIGHT. Subcommands write only `data/b573_*` unless the docstring names a
### ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
V014 = '4dce7b97eb29733b823919bd80b08d01c82c6d8f'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']

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


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


DEFECTS = [
    '(a) A STRAY FILE IN relay/tools AGAIN: a shell command carried an empty here-document append that created '
    'relay/tools/b573_record.py.blk (empty); removed at once by its absolute path in the same command; nothing read it; within the (W) '
    'glob relay/tools/b573_*. b571`s defect (c) repeated -- the stray line was carried from a copied command.',
    '(b) THE ASSERTION LIST: its guard line names a `--diff` flag the generator does not have (the substitution-only reading is made '
    'by the record`s H25b instead); and its amendment for the count binder (hA -> hcnt, after the first Converse elaboration met a '
    'shadowing) was appended before the patch applied -- a needle failed on an escape -- so the bank carries the amendment, then a '
    'CORRECTION line printing the list as it stood when the rename applied (relay data/b573_assertions.txt).',
    '(c) THE FIELDS BANK`S :44 PICKER caught two lines (RestBound :44 and CriterionForward :44); the second is printed beside the HCount '
    'line and is not a field`s type.',
    '(d) THE χ NODE LIST GAINED TWO NODES AFTER THE PAGE WAS FIRST WRITTEN AND THE FINDINGS ENTRY APPENDED: the page`s Correspondence '
    'rows read relay HEAD`s terminal table, which at this act`s housekeeping gains rows 437-441; two schema names they grade '
    '(online_imp_h2_sign_cfg, h2_sign_cfg_zeta_statement) were outside the list and would have joined the page`s Correspondence, so '
    'the committed page would no longer regenerate. Both added as the schema`s nodes (18); the page regenerated twice (runs three and '
    'four, byte-identical; runs one and two superseded); the entry`s "16 nodes" corrected by an appended line (:6370), the entry unedited; the PLACE-papers commit dd87bdc`s message names that line :6358, wrongly.',
    '(e) THE SUITE, PRE-PUSH RUN ONE: G-PIECES-BANKED FAILED LIVE -- the carried harness`s build_ok looked for '
    '"Built SIDEExplicitFormula.Chi.<module>" and this act`s modules are Schema/; the module path corrected in the suite`s assembly, '
    'the table files restored to their committed state, the suite re-run: 76 of 76.',
]


def node_fix():
    """### PLACE-papers FINDINGS.md (one appended line): the node count of the entry corrected by append (defect (d))."""
    Q = _Q()
    fj = jl('b573_findings.json')
    h = '*Appended 2026-10-01 by b573 to its own entry (:%s) -- A CORRECTION:*' % fj['entry_line']
    Q.guard_absent(Q.FIND, h)
    a = ('\n%s the page at the Dirichlet instance has 18 nodes, not the 16 the entry says: the list gained the schema’s forward half and '
         'its ζ check, two schema names graded by this act’s correspondence rows, after the entry was written; the page was regenerated '
         'twice, byte-identical (relay `data/b573_page_runs.txt`). The entry above stands unedited.\n' % h)
    r = Q.append_to(Q.FIND, a)
    put_json('b573_node_fix.json', dict(line=Q.line_of(Q.FIND, h), append=r))
    print(jl('b573_node_fix.json'))


def defects():
    put_txt('b573_defects.txt', ['### b573 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def _Q():
    import b566_record as R6
    return R6.Q


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
SGS = 'D:/SIDE-global-section'
READS = [
    ('vendored Zeta23 Defs (ZeroConfig)', EF, V014, 'Zeta23/Defs.lean', [136]),
    ('vendored Zeta23 ExplicitFormula (EF_lit)', EF, V014, 'Zeta23/ExplicitFormula.lean', [97]),
    ('kernel B321Identity (zeroSide; b321_identity -- the EF field`s consuming type)', EF, V014, 'SIDEExplicitFormula/B321Identity.lean', [24, 46, 47, 48]),
    ('kernel RestBound (HCount -- the COUNT field`s type)', EF, V014, 'SIDEExplicitFormula/RestBound.lean', [44, 45]),
    ('kernel PowerLimit (dominant_summable and its count; the assembly)', EF, V014, 'SIDEExplicitFormula/PowerLimit.lean', [949, 952, 955, 1167, 1188]),
    ('kernel PowerWindow (rh_strip -- the TARGET field`s strip form)', EF, V014, 'SIDEExplicitFormula/PowerWindow.lean', [483]),
    ('kernel Seam (h2_sign_iff_rh)', EF, V014, 'SIDEExplicitFormula/Seam.lean', [101]),
    ('kernel Chi/CriterionForward (zeroSide_chi_eq; rh_strip_chi_iff_grh_chi)', EF, V014, 'SIDEExplicitFormula/Chi/CriterionForward.lean', [None]),
    ('kernel Chi/CriterionConverse (h2_sign_chi_iff_grh_chi)', EF, V014, 'SIDEExplicitFormula/Chi/CriterionConverse.lean', [None]),
    ('relay the b572 generator', RELAY, 'HEAD', 'data/b572_gen_converse.py.txt', [12, 13, 14]),
    ('relay the b572 lemma list (the converse`s count line)', RELAY, 'HEAD', 'data/b572_lemmas.txt', [None]),
    ('PLACE-papers README (the (R182)(2) line)', PP, 'HEAD', 'README.md', [123]),
    ('PLACE-papers REGISTRY (the (R182)(2) line)', PP, 'HEAD', 'REGISTRY.md', [958]),
    ('PLACE-papers FINDINGS (the ceiling`s χ-sentence record)', PP, 'HEAD', 'FINDINGS.md', [6328]),
    ('PLACE-papers OPEN_TRAILS (the schema`s price)', PP, 'HEAD', 'OPEN_TRAILS.md', [11764]),
    ('relay chain_page.py (the page name; the open line; the ceiling line; the probe imports)', RELAY, 'HEAD', 'tools/chain_page.py', [58, 59, 387, 204]),
    ('relay b569`s node list (its pin line)', RELAY, 'HEAD', 'data/b569_nodes.txt', [4]),
]
FIND_DECL = {'SIDEExplicitFormula/Chi/CriterionForward.lean': ('theorem zeroSide_chi_eq', 'theorem rh_strip_chi_iff_grh_chi'),
             'SIDEExplicitFormula/Chi/CriterionConverse.lean': ('theorem h2_sign_chi_iff_grh_chi',),
             'data/b572_lemmas.txt': ('### THE CONVERSE (h2_sign_imp_rh_holds)', '### ### **THE CONVERSE`S ζ-NAMING LEMMAS')}


def reads():
    L = ['b573 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        sl = src.split(NL)
        if lines == [None]:
            lines = [i for i, l in enumerate(sl, 1) for p in FIND_DECL[path] if l.startswith(p)]
        L.append('### %s -- %s @ %s' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip()))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b573_reads.txt', L)


# ================================================================================ COMPONENT 1
SUCCESSOR = ('The criterion for primitive χ is composed: Weil positivity on classK for χ ⟺ GRH_chi, both directions compiled '
             '(h2_sign_chi_iff_grh_chi, v0.14), the converse by the ζ route over the χ-configuration with its own local count. The '
             'one clause now has two compiled instances, ζ and primitive χ ≠ 1, each equivalent to the location of its own zeros; '
             'neither is proved.')
NOT_SUP = ('Not supportable: *GRH reduced* without *for primitive Dirichlet characters, to the positivity clause*, *GRH proved*, '
           'anything about a zero.')
SUCC_LINE = ('*(Appended under the author\'s ruling `(R183)`(3), 2026-10-01, b573, replacing by append the last clause of b572\'s '
             '`(R182)`(2) sentence directly above, which stays, as do the `(R146)`(2), `(R174)`(1), `(R176)`(2) and `(R177)`(2) '
             'sentences: b572 entered at its weight, SIDE-explicit-formula v0.14 = `4dce7b9`.)* Supportable, the author\'s sentence: *'
             + SUCCESSOR + '* ' + NOT_SUP)


def weight():
    """### PLACE-papers FINDINGS.md (two appended lines): (R183)(1)-(2) -- b572 at its weight; the H24c re-read by kind."""
    Q = _Q()
    sj = jl('b572_schema.json')
    k = {a: len(b) for a, b in sj['kinds'].items()}
    e = Q.line_of(Q.FIND, '## GRH-Weil, act seven: the criterion at the χ-instance')
    h1 = '*Appended 2026-10-01 by b573 to b572’s entry (:%s), under `(R183)`(1) -- b572 AT ITS WEIGHT:*' % e
    h2 = '*Appended 2026-10-01 by b573 to b572’s entry (:%s), under `(R183)`(2) -- H24c RE-READ BY KIND:*' % e
    Q.guard_absent(Q.FIND, h1)
    a1 = ('\n%s SIDE-explicit-formula v0.14 = `4dce7b9`, tagged by the push script and read back: Weil positivity on classK for χ is '
          'equivalent to GRH for χ, every primitive χ ≠ 1, at the standard three with domain conditions only, no sorryAx on main; an '
          'equivalence between open statements, proving neither. The reality read found the ζ converse consuming the configuration’s '
          'reflection and no conjugation fact, its sign read on the real part, so b562’s statement is the statement of record, '
          'unedited. The forward half compiled at its elaboration; the converse carries PowerLimit’s L7e to the χ-configuration with '
          'its own local count, every generic lemma consumed as it stands; no seam is consumed for χ. H24a, H24b, H24d held; the '
          'suite 69 of 69.\n' % h1)
    a2 = ('\n%s the walk found %d ζ-naming declarations in the converse (relay `data/b572_lemmas.txt`): in letter the navigator’s '
          'bound of three is refuted at %d; in kind the ζ-content is three -- the explicit formula (%d), the local count (%d), the seam '
          '(%d) -- and the other %d name the ζ configuration in their statement alone, instantiations. That reading is the schema’s '
          'price; (S1) and (S2) stand refuted as b572 scored them.\n' % (h2, sum(k.values()), sum(k.values()), k.get('EF', 0),
                                                                        k.get('COUNT', 0), k.get('SEAM', 0), k.get('NONE', 0)))
    r = [Q.append_to(Q.FIND, a1), Q.append_to(Q.FIND, a2)]
    lines = [Q.line_of(Q.FIND, h1), Q.line_of(Q.FIND, h2)]
    put_json('b573_weight.json', dict(entry=e, lines=lines, appends=r, kinds=k))
    print(jl('b573_weight.json'))


def _place_after(path, line_no, text, expect_prefix):
    raw = open(path, 'rb').read()
    crlf = b'\r\n' in raw
    s = raw.decode('utf-8').replace('\r\n', '\n')
    ls = s.split('\n')
    if not ls[line_no - 1].startswith(expect_prefix):
        sys.exit('### %s :%d does not start with the expected ceiling line: %r' % (path, line_no, ls[line_no - 1][:80]))
    if text in s:
        sys.exit('### %s already carries the line' % path)
    new = ls[:line_no] + ['', text] + ls[line_no:]
    out = '\n'.join(new)
    if crlf:
        out = out.replace('\n', '\r\n')
    b = out.encode('utf-8')
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)
    return line_no + 2


def ceiling():
    """### PLACE-papers README.md and REGISTRY.md (one placed line each, after b572`s (R182)(2) line) and FINDINGS.md (one
    ### appended line addressed to :6328): (R183)(3), the author`s successor sentence."""
    Q = _Q()
    pre = '*(Appended under the author\'s ruling `(R182)`(2), 2026-10-01, b572'
    rl = _place_after(os.path.join(PP, 'README.md'), 123, SUCC_LINE, pre)
    gl = _place_after(os.path.join(PP, 'REGISTRY.md'), 958, SUCC_LINE, pre)
    h = ('*Appended 2026-10-01 by b573 to the ceiling’s χ-sentence record (:6328), under `(R183)`(3) -- THE CEILING’S SUCCESSOR, '
         'replacing by append the last clause of `(R182)`(2):*')
    Q.guard_absent(Q.FIND, h)
    a = '\n%s the author’s sentence, placed at README.md :%d and REGISTRY.md :%d: *%s* %s\n' % (h, rl, gl, SUCCESSOR, NOT_SUP)
    r = Q.append_to(Q.FIND, a)
    put_json('b573_ceiling.json', dict(readme=rl, registry=gl, findings=Q.line_of(Q.FIND, h), append=r, line=SUCC_LINE, sentence=SUCCESSOR))
    L = ['b573 -- COMPONENT 1: THE CEILING`S SUCCESSOR SENTENCE, (R183)(3), AT ITS THREE PLACES', '']
    for f, n in (('README.md', rl), ('REGISTRY.md', gl), ('FINDINGS.md', Q.line_of(Q.FIND, h))):
        sl = io.open(os.path.join(PP, f), encoding='utf-8').read().replace(chr(13), '').split(NL)
        L.append('### PLACE-papers %s :%d' % (f, n))
        L.append('    ' + sl[n - 1])
    put_txt('b573_ceiling.txt', L)
    print(jl('b573_ceiling.json'))


# ================================================================================ COMPONENT 2: THE FIELDS
STMT = r'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5226893c-b61b-44e1-b55a-66d9d0e7c6b1/scratchpad/fields_stmt.txt'


def fields():
    """### Component 2: each field's type read off its consuming lemma, the structure printed, H25a provisional; banks
    ### data/b573_fields.txt (and .json). Written before any kernel file."""
    rd_ = rd('b573_reads.txt').split(NL)
    pick = lambda key: [l for l in rd_ if key in l]
    stmt = io.open(STMT, encoding='utf-8').read().rstrip(NL)
    sj = jl('b572_schema.json')
    L = ['b573 -- COMPONENT 2: THE FIELDS, (R183)(4)(a) -- EACH TYPE READ OFF ITS CONSUMING LEMMA; THE STRUCTURE PRINTED BEFORE THE BUILD',
         '', '### written at (UTC) %s' % utc(), '',
         '### FIELD 1, EF -- consumed by h2_sign_imp_rh_strip_of (PowerLimit.lean :1167, at :1184-:1188 `b321_identity _ hc hs he`) and by',
         '###   zeroSide_eventually_neg through the zero side; its type is b321_identity`s (B321Identity.lean :46-:48):'] + \
        ['###     ' + l.strip() for l in pick(':46 ') + pick(':47 ') + pick(':48 ')] + [
         '###   χ`s identity (zeroSide_chi_eq, Chi/CriterionForward.lean :34) carries no evenness: the field takes the even form, which both meet.',
         '### FIELD 2, COUNT -- consumed by dominant_summable (PowerLimit.lean :949), the one lemma of the kind COUNT; its type is HCount:'] + \
        ['###     ' + l.strip() for l in pick(':952 ') + pick(':955 ') + pick(':44 ') + pick(':45 ')] + [
         '### FIELD 3, TARGET -- the strip form rh_strip (PowerWindow.lean :483) is what h2_sign_iff_rh_strip concludes; the seam (the 4 SEAM',
         '###   lemmas) carries it to the instance`s own statement, so the field is a Prop with its equivalence to the strip form:'] + \
        ['###     ' + l.strip() for l in pick(':483 ')] + [
         '', '### THE b572 PRICE BY KIND (relay data/b572_schema.json): %s' % {k: len(v) for k, v in sj['kinds'].items()},
         '###   EF -> field 1 ; COUNT -> field 2 ; SEAM -> field 3`s equivalence (left to the instance) ; NONE -> re-targeted by substitution.',
         '', '### THE STRUCTURE AND ITS STATEMENTS, AS THEY WILL BE WRITTEN (SIDEExplicitFormula/Schema/Config.lean, namespace '
         'SIDEExplicitFormula.Schema):', ''] + ['    ' + l for l in stmt.split(NL)] + [
         '', '### ### **H25a, PROVISIONAL: HELD ON THE LIST -- every ζ-naming lemma of the converse maps to one of the three fields or to a '
         'statement-level re-target; no fourth kind is named. Final score on the build.**']
    put_txt('b573_fields.txt', L)
    put_json('b573_fields.json', dict(fields=['EF', 'COUNT', 'TARGET'], kinds={k: len(v) for k, v in sj['kinds'].items()},
                                      provisional='HELD', statement=stmt))

# ================================================================================ COMPONENT 4: E0, rowgen
TERMS = [('438', 'online_imp_h2_sign_cfg', 'SIDEExplicitFormula/Schema/Config.lean'),
         ('439', 'h2_sign_cfg_iff_target', 'SIDEExplicitFormula/Schema/Converse.lean'),
         ('440', 'h2_sign_cfg_zeta_statement', 'SIDEExplicitFormula/Schema/Instances.lean'),
         ('441', 'h2_sign_cfg_chi_statement', 'SIDEExplicitFormula/Schema/Instances.lean')]
ROW_ACT = '437'
NS = 'SIDEExplicitFormula.Schema.'


def e0(rev='grh-weil-b573'):
    """### every declaration of the act graded by the shared E0 rule at `rev` (the branch, before the merge), its print, and
    ### rowgen's record of the terminals of record (b566_record.Q.rowgen_record, IMPORTED)."""
    import b569_record as R9
    Q = _Q()
    pr = rd('b573_schema_prints.txt')
    P0 = R9.prints_axioms(pr)
    dj = jl('b573_decls_chi.json')
    tip = g(EF, 'rev-parse', rev).strip()
    rows, srcs = {}, {}
    L = ['b573 -- COMPONENTS 2-3: THE E0 READ -- EVERY DECLARATION GRADED, THE ROWGEN RECORD', '',
         '### the prints of record: relay data/b573_schema_prints.txt ; the statements at %s (%s).' % (tip[:7], rev)] + E0.RULE_TEXT + ['']
    for d in dj['decls']:
        n = d['name']
        if d['file'] not in srcs:
            srcs[d['file']] = g(EF, 'show', '%s:%s' % (tip, d['file']))
        head, _ln = R9.header_of(srcs[d['file']], n.split('.')[-1])
        gr, why, _b = E0.grade(head or '', d['kind'])
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, file=d['file'],
                       header_read=head is not None, kind=d['kind'])
        L.append('    %-46s %-10s %s  -- %s' % (n.split('.')[-1], gr, 'std3' if rows[n]['std3'] else ax, (why or '')[:120]))
    cons = {n: P0.get(n) for n in dj['consumed']}
    L += ['', '### THE CONSUMED TERMINALS, their prints:'] + ['    %-62s %s' % (n, 'std3' if a is not None and set(a) <= set(STD3) else a)
                                                            for n, a in cons.items()]
    recs, ctl = [], (True,)
    for rn, n, rel in TERMS:
        r, ctl = Q.rowgen_record([NS + n], rel, tip, pr)
        recs += r
    L += ['', '### THE ROWGEN RECORD (at %s):' % tip[:7]]
    L += ['    %-40s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])) for r in recs]
    th = [r for r in rows.values() if r['kind'] == 'theorem']
    cnt = {k: sum(1 for r in th if r['grade'] == k) for k in ('DERIVES', 'INTERFACES')}
    gate = (all(r['std3'] for r in rows.values()) and all(a is not None and set(a) <= set(STD3) for a in cons.values())
            and all(r['header_read'] for r in rows.values()) and ctl[0] and not any(r['defenc'] for r in recs) and all(r['check'] for r in recs))
    L.append('### ### **THE GATE: %s** -- declarations %d (theorems %d: DERIVES %d, INTERFACES %d), consumed %d'
             % ('PASS' if gate else 'FAIL', len(rows), len(th), cnt['DERIVES'], cnt['INTERFACES'], len(cons)))
    put_txt('b573_e0.txt', L)
    put_json('b573_e0.json', dict(rows=rows, consumed=cons, gate=gate, rowgen=recs, rowgen_control=ctl[0], tip=tip, rev=rev, counts=cnt))


def rowgen_diff():
    """### the act's terminal rows (438-441) read by rowgen.diff (IMPORTED, Lean's identifier set since relay 618143a8)."""
    Q = _Q()
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))
    import rowgen as RG
    recs = jl('b573_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b573 -- THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 438-441', '']
    res = {}
    for rn, n, rel in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [list(x) for x in out if isinstance(x, tuple) and x[0] == NS + n]
        res[rn] = dict(found=len(rowtxt) == 1, mine=mine)
        L.append('### row %s found: %s' % (rn, len(rowtxt) == 1))
        L += ['    ' + str(x) for x in out]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for v in res.values())
    L += ['', '### ### **THE ROWGEN DIFF : %s on all %d rows.**' % ('CLEAN' if ok else 'NOT CLEAN', len(TERMS))]
    put_txt('b573_rowgen.txt', L)
    put_json('b573_rowgen.json', dict(rows=res, clean=ok))

# ================================================================================ COMPONENT 6: THE RECORD
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
INSTR = dict(page='e293b1c7')
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SCORE_KEYS = ('H25a', 'H25b', 'H25c', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
CARRIED = ['fR', 'fR_norm_le', 'fR_bound', 'rest_tendsto_zero', 'sT', 'mem_sT', 'zeroSide_eventually_neg']


def _attempt_ok(name):
    t = rd(name)
    return re.search(r'^=== END \S+ rc=0$', t, re.M) is not None and 'error' not in t


def scores():
    e, sj = jl('b573_e0.json'), jl('b572_schema.json')
    kp = rd('b573_kernel_push_out.txt')
    ns = [x for x in g(EF, 'diff', '--name-status', V014, 'main').split(NL) if x.strip()]
    rows = e['rows']
    conv = g(EF, 'show', V015 + ':SIDEExplicitFormula/Schema/Converse.lean')
    cfg = g(EF, 'show', V015 + ':SIDEExplicitFormula/Schema/Config.lean')
    fields = re.findall(r'^  (rhs|ef|count|target|target_iff) :', cfg, re.M)
    carried_ok = all(('theorem %s_cfg' % n) in conv or ('def %s_cfg' % n) in conv for n in CARRIED)
    assembly_changed = 'b321Norm' not in conv and 'zeroSide_cfg_eq C hc hs he' in conv
    wrappers_dropped = 'zeroSideNeg' not in conv
    st = {n: rows.get(NS + n, {}) for n in ('h2_sign_cfg_zeta_statement', 'h2_sign_cfg_chi_statement', 'h2_sign_cfg_iff_target')}
    v015 = ('tag v0.15 peeled local %s remote %s' % (V015, V015)) in kp
    pr = rd('b573_page_runs.txt')
    nodes = re.search(r'nodes (\d+)', pr.split(NL)[-2] if pr else '')
    nnodes = int(nodes.group(1)) if nodes else -1
    ts = rd('b573_page_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', ts, re.M) is not None
    page_b569 = subprocess.run(['git', '-C', PP, 'show', 'bd2a616:THE_CLAUSE_AND_ITS_COMPILED_FACES.md'], capture_output=True).stdout
    page_head = subprocess.run(['git', '-C', PP, 'show', 'HEAD:THE_CLAUSE_AND_ITS_COMPILED_FACES.md'], capture_output=True).stdout
    S = dict(
        H25a=('HELD' if sorted(fields) == sorted(['rhs', 'ef', 'count', 'target', 'target_iff']) and e.get('gate') else 'REFUTED',
              'the structure carries the three fields EF (rhs, ef), COUNT (count), TARGET (target, target_iff) and no other '
              '(Schema/Config.lean, fields read %s); the restatement compiled over them with no fourth fact: every generic lemma '
              'consumed as it stands, and the instances supply each field from a compiled ζ or χ fact (Schema/Instances.lean)' % fields),
        H25b=('HELD' if carried_ok and not assembly_changed else 'REFUTED',
              'refuted by one proof: of the 11 statement-naming lemmas, the 7 L7e lemmas (%s) re-target by substitution alone (relay '
              'data/b573_assertions.txt) and rh_strip becomes the def `online`; the Prop wrappers zeroSideNeg and zeroSideNeg_holds are '
              'not restated (the assembly calls zeroSide_eventually_neg_cfg directly); h2_sign_imp_rh_strip_of`s proof NEEDED A CHANGE '
              'at its EF use -- its four lines through b321_identity, b321Norm and one_mul become one rewrite by the ef field '
              '(zeroSide_cfg_eq) in h2_sign_cfg_imp_online' % ', '.join(CARRIED)),
        H25c=('HELD' if all(v.get('std3') for v in st.values()) and v015 else 'REFUTED',
              'both instances reproduce the existing equivalences: h2_sign_cfg_zeta_statement : (h2_sign_cfg zetaWeilConfig ↔ '
              'zetaWeilConfig.target) = (h2_sign ↔ RiemannHypothesis) and h2_sign_cfg_chi_statement : (… chiWeilConfig …) = '
              '(h2_sign_chi χ ↔ GRH_chi χ), each by rfl, prints %s (relay data/b573_schema_prints.txt); no sorryAx'
              % [v.get('axioms') for v in st.values()][0]),
        N1=('HELD', 'H25a HELD'),
        N2=('REFUTED', 'H25b refuted: one proof (the assembly`s EF use) changed; 7 of the 11 by substitution alone'),
        N3=('HELD' if all(v.get('std3') for v in st.values()) and v015 else 'REFUTED',
            'both checks print the standard three; v0.15 = %s made by push_gated.sh and read back with the schema' % V015[:7]),
        N4=('HELD' if 12 <= nnodes <= 20 and clean else 'REFUTED',
            'the page has %d nodes, and relay tools/banned_terms.py reads it %s (data/b573_page_termscan.txt)' % (nnodes, 'CLEAN' if clean else 'NOT CLEAN')),
        N5=('HELD' if ns and all(x.startswith('A\t') or x == 'M\tREADME.md' for x in ns) else 'REFUTED',
            'v0.14 against main: %s; nothing at Zenodo; nothing deposits; the kept branches unmoved (the suite`s G-KEPT-BRANCHES)' % ns),
        S1=('HELD', 'the EF field takes the even form; ζ`s identity carries evenness, χ`s does not; the converse consumes it at the classK '
                    'window only (h2_sign_cfg_imp_online, `obtain ⟨he, hc, hs, -⟩ := hk`)'),
        S2=('HELD' if all(v.get('std3') for v in st.values()) else 'REFUTED', 'both equality checks close by rfl (Schema/Instances.lean)'),
        S3=('HELD' if page_head == page_b569 and page_head else 'REFUTED', 'the ζ page at PLACE-papers HEAD is b569`s blob, unchanged; no node changed'),
        counts=dict(decls=len(rows), theorems=sum(1 for r in rows.values() if r['kind'] == 'theorem'), derives=e['counts']['DERIVES'],
                    interfaces=e['counts']['INTERFACES'], consumed=len(e['consumed']), nodes=nnodes, carried=len(CARRIED),
                    kinds={k: len(v) for k, v in sj['kinds'].items()}),
    )
    put_json('b573_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


def findings():
    Q = _Q()
    S = jl('b573_scores.json')
    c = S['counts']
    title = ('## GRH-Weil, act eight: the criterion over a configuration with an explicit formula and a local count, ζ and primitive χ as '
             'instances, landed; the page at the Dirichlet instance')
    Q.guard_absent(Q.FIND, title)
    e = ['', title, '',
         '*Filed at b573 on the author’s ruling `(R183)`. Banks: relay `data/b573_fields.txt`, `data/b573_assertions.txt`, '
         '`data/b573_schema_prints.txt`, `data/b573_e0.txt`, `data/b573_gen_schema.py.txt`, `data/b573_page_runs.txt`, '
         '`data/b573_test_chain_page.txt`. Nothing about the zeros of ζ or of any L(s, χ) is claimed beyond the compiled statements’ own '
         'words.*', '',
         '**The schema** (`(R183)`(4)), SIDE-explicit-formula v0.15 = `%s`, %d declarations at the standard three. A configuration of zeros '
         'with three fields read off the lemmas that consume them -- an explicit formula (the zero side equal to an arithmetic side on '
         'even test functions), a local count, and a target equivalent to the strip form -- and over it Weil positivity on classK is '
         'equivalent to the target, both directions compiled: the forward half by the argument of the ζ case, the converse by the ζ '
         'converse carried over by named, asserted replacements. ζ and every primitive χ ≠ 1 are its instances, and each instance’s '
         'equivalence is the existing one, checked by the definition. Equivalences between open statements; they prove neither.'
         % (V015[:7], c['decls']), '',
         '**The page at the Dirichlet instance** (`(R183)`(5)): `%s`, generated by the page generator’s Dirichlet variant (relay `%s`) '
         'from %d nodes at v0.15, twice, byte-identical; its open line as ruled, its last line the successor sentence of the ceiling.'
         % (DIR_PAGE, INSTR['page'], c['nodes']), '',
         '**The scores.** H25a %s; H25b %s; H25c %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R183)`(6), the schema landed, so the next act is CP-5: the deposit reconciliation carrying Anomaly 1, '
         'E-2026-09-25-1 through -6, E-2026-09-27-1 and the `(R110)` description edit.', '',
         '*Nothing deposits; nothing at Zenodo written; no existing statement of any kernel changed; no sentence here claims priority; '
         'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b573_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def workorder():
    Q = _Q()
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h = '*Appended 2026-10-01 by b573, under the author’s ruling `(R183)`(6), to the W-ORD-GRH-WEIL entry'
    Q.guard_absent(Q.OT, h + ' (:%s) -- THE SCHEMA' % wg)
    a = ('\n%s (:%s) -- THE SCHEMA LANDED:* SIDE-explicit-formula v0.15 = `%s` compiles the criterion over any configuration with an '
         'explicit formula, a local count and a target (Schema/), ζ and every primitive χ ≠ 1 as instances; the priced item of b572 '
         '(:11764) is closed by it. The χ-leg’s page is `%s`. The next act is CP-5.\n' % (h, wg, V015[:7], DIR_PAGE))
    r = Q.append_to(Q.OT, a)
    put_json('b573_workorder.json', dict(line=Q.line_of(Q.OT, h + ' (:%s) -- THE SCHEMA' % wg), wg=wg, append=r))
    print(jl('b573_workorder.json'))


def trail():
    Q = _Q()
    S = jl('b573_scores.json')
    fj, wj, cj, wt = jl('b573_findings.json'), jl('b573_workorder.json'), jl('b573_ceiling.json'), jl('b573_weight.json')
    head = ('### b573 — lane two, act thirteen under (R183): GRH-Weil act eight -- the generic schema from the lemma list, ζ and χ as '
            'instances, landed; the ceiling’s successor sentence; the page at the Dirichlet instance')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R183) ratified.** (1) b572 entered at its weight. (2) H24c re-read by kind. (3) The ceiling’s successor sentence. (4) '
            'GRH-Weil act eight, the schema. (5) The χ-leg’s page. (6) The gates; v0.15; CP-5 next.', '',
            '**Entered:** FINDINGS.md:%s and :%s (b572’s weight; the re-read), :%s (the successor’s record), :%s (the entry); README.md:%s '
            'and REGISTRY.md:%s (the successor line); OPEN_TRAILS.md:%s (the work-order line), this record; the page `%s`; '
            'SIDE-global-section CORRESPONDENCE.md rows 437-441; SIDE-explicit-formula main = **v0.15** = `%s`, grh-weil-b573 pushed by '
            'name. Relay instrument commit: the page`s Dirichlet variant `%s`.' % (wt['lines'][0], wt['lines'][1], cj['findings'],
                                                                               fj['entry_line'], cj['readme'], cj['registry'],
                                                                               wj['line'], DIR_PAGE, V015[:7], INSTR['page']), '',
            '**H25a %s · H25b %s · H25c %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**Next:** per `(R183)`(6), the schema landed: CP-5, the deposit reconciliation (Anomaly 1, E-2026-09-25-1 through -6, '
            'E-2026-09-27-1, the `(R110)` description edit).', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no existing statement changed; no Zeta23 or vendored '
            'file edited or added; ERRATA untouched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists '
            'stay OPEN; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b573_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r))
    print(jl('b573_trail.json')['line'])


def rows():
    import b569_record as R9
    Q = _Q()
    e = jl('b573_e0.json')
    for rn, n, rel in TERMS:
        if e['rows'][NS + n]['grade'] != 'DERIVES' or not e['rows'][NS + n]['std3']:
            sys.exit('### %s not graded at the standard three: no row' % n)
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    pr = R9.prints_axioms(rd('b573_schema_prints.txt'))
    out = []
    act = [ROW_ACT,
           '**GRH-WEIL ACT EIGHT** (b573, under (R183)(4)). SIDE-explicit-formula v0.15 = %s: the generic schema -- a configuration with '
           'an explicit formula, a local count and a target; Weil positivity on classK over it equivalent to its target; ζ and primitive '
           'χ ≠ 1 as instances, each checked equal to its existing equivalence. Nothing here proves RH or GRH.' % V015[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/Schema/{Config,Converse,Instances}.lean (v0.15 = %s)' % V015[:7],
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b573_schema_prints.txt)' % len(e['rows']),
           ' ; '.join('`%s` DERIVES' % t[1] for t in TERMS),
           'LANDED at v0.15 = %s; nothing deposits; nothing at Zenodo written.' % V015[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    for rn, n, rel in TERMS:
        head = ' '.join(e['rows'][NS + n]['head'].split()).replace('|', '‖')
        cells = [rn, '**%s** (b573, under (R183)(4)), SIDE-explicit-formula v0.15 = %s: `%s%s %s`.' % (n, V015[:7], NS, n, head),
                 '`SIDE-explicit-formula/%s` (v0.15 = %s) : `%s%s`' % (rel, V015[:7], NS, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b573_schema_prints.txt)' % (NS, n, ', '.join(pr.get(NS + n) or [])),
                 '`%s` DERIVES' % n,
                 'LANDED at v0.15 = %s; the E0 read at the branch tip (relay data/b573_e0.txt).' % V015[:7]]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b573_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def desk():
    S = jl('b573_scores.json')
    L = ['=' * 104, 'b573 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H25a-H25c ((R183)(4)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H25a', 'H25b', 'H25c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in
                                                         ('N1', 'N2', 'N3', 'N4', 'N5')]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in ('N1', 'N2', 'N3', 'N4', 'N5') if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (nh, 5 - nh, sh, 3 - sh), '']
    L += rd('b573_defects.txt').rstrip(NL).split(NL)
    put_txt('b573_desk_notes.txt', L)


def components():
    S = jl('b573_scores.json')
    fj, tj, rj, wj, cj, wt = (jl('b573_findings.json'), jl('b573_trail.json'), jl('b573_rows.json'), jl('b573_workorder.json'),
                              jl('b573_ceiling.json'), jl('b573_weight.json'))
    L = ['b573 -- THE COMPONENTS, BANKED UNDER (R183).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b572`s push-out banks relay 296eb292 ; push-b572 branches deleted by name '
         '(data/b573_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b572`s weight FINDINGS :%s, the H24c re-read :%s ; the successor sentence README :%s, REGISTRY :%s, FINDINGS :%s '
         '(data/b573_ceiling.txt) -- before any build' % (wt['lines'][0], wt['lines'][1], cj['readme'], cj['registry'], cj['findings']),
         '### COMPONENT 2 : the fields (data/b573_fields.txt) : EF, COUNT, TARGET ; H25a %s' % S['H25a'][0],
         '### COMPONENT 3 : the assertion list (data/b573_assertions.txt) ; Schema/Config, Schema/Converse built ; H25b %s' % S['H25b'][0],
         '### COMPONENT 4 : Schema/Instances, both statement checks by rfl ; H25c %s ; v0.15 = %s by push_gated.sh ; grh-weil-b573 pushed, '
         'no held branch' % (S['H25c'][0], V015[:7]),
         '### COMPONENT 5 : the node list (data/b573_nodes_chi.txt) ; the Dirichlet variant relay %s (26 of 26) ; %s, %d nodes, twice '
         'byte-identical (data/b573_page_runs.txt) ; banned-stem scan CLEAN' % (INSTR['page'], DIR_PAGE, S['counts']['nodes']),
         '### COMPONENT 6 : FINDINGS :%s ; OPEN_TRAILS :%s (the work-order), :%s (the record) ; CORRESPONDENCE rows %s ; the ζ page '
         'unchanged ; next: CP-5' % (fj['entry_line'], wj['line'], tj['line'], ', '.join('%s (exit %d)' % (o['row'], o['exit']) for o in rj['rows']))]
    put_txt('b573_components.txt', L)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b573_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
