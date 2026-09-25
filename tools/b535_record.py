# -*- coding: utf-8 -*-
"""b535_record.py -- THE UPDATE ACT`S WRITES AND RECORD, UNDER (R145).
### `python tools/b535_record.py erratum | platform | finding | ceiling | rows | components | desk | trail`

### Every corpus write here APPENDS or INSERTS a line beside a named line; no line is deleted and each write proves it
### (prior lines all present after). ERRATA entries go through `errata_append.py` (its duplicate-id refusal). The ceiling
### sentence is READ from the banked ferry, whitespace-joined, not typed. Figures are read from the banks.
"""
import html
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import errata_append  # noqa: E402
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
ERR = os.path.join(PP, 'ERRATA.md')
FIND = os.path.join(PP, 'FINDINGS.md')
README = os.path.join(PP, 'README.md')
REG = os.path.join(PP, 'REGISTRY.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
PIN_ZETA23 = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
EID1, EID2 = 'E-2026-09-25-1', 'E-2026-09-25-2'
STATUS_ADD = ('The equivalence the programme holds after b534, Weil positivity on classK ↔ RH on the kernel\'s configuration, '
              'is a finding and is recorded in FINDINGS, not here.')
TITLE = ("Weil positivity on classK and RH on the kernel's zero configuration: the equivalence compiled both ways; the seam "
         "to Mathlib's RiemannHypothesis named")
FHEAD = '## ' + TITLE
OLD_CEIL = ('RH and Weil positivity on classK are one Prop apart in the kernel, RH → h2_sign compiled, h2_sign → RH compiled to '
            "its last step; the deposit's Route 3 premise is RH restated, E-2026-09-25-1 drafted.")
README_OLD = 'Supportable: *RH reduced to a single located clause, reduction machine-verified.*'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def ceiling():
    """### (R145)(2)`s supportable sentence, READ from the banked ferry and whitespace-joined."""
    f = ' '.join(rd(os.path.join(D, 'b535_ferry.txt')).split())
    i = f.index('Supportable: "') + len('Supportable: "')
    j = f.index('" Not supportable:', i)
    return f[i:j]


def not_supportable():
    f = ' '.join(rd(os.path.join(D, 'b535_ferry.txt')).split())
    i = f.index('Not supportable: ') + len('Not supportable: ')
    j = f.index(' The sentence "RH', i)
    return f[i:j]


def insert_after(path, anchor_pred, new_lines):
    """### INSERT lines after the first line satisfying anchor_pred; prove every prior line survives, in order."""
    raw = open(path, 'rb').read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    text = raw.decode('utf-8-sig')
    lines = text.split(NL)
    k = next(i for i, l in enumerate(lines) if anchor_pred(l))
    out = lines[:k + 1] + new_lines + lines[k + 1:]
    data = NL.join(out).encode('utf-8')
    open(path, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + data)
    after = rd(path).split(NL)
    kept = after[:k + 1] + after[k + 1 + len(new_lines):] == lines
    return dict(file=os.path.relpath(path, PP), anchor_line=k + 1, inserted_at=k + 2, inserted=len(new_lines), prior_kept=kept,
                bom=bom)


def backticks_outside_code(text):
    n = 0
    for line in text.split(NL):
        rest = re.sub(r'`[^`\n]+`', '', line)
        n += rest.count('`')
    return n


# ------------------------------------------------------------------------------ COMPONENT 2
def erratum():
    d = rd(os.path.join(D, 'b532_erratum_draft.md')).rstrip(NL)
    poss = re.findall(r'[A-Za-z]`[sS]\b', d)
    t = re.sub(r'([A-Za-z])`([sS])\b', r"\1'\2", d)
    lines = t.split(NL)
    k = max(i for i, l in enumerate(lines) if l.startswith('**Status.**'))
    lines[k] = lines[k].rstrip() + ' ' + STATUS_ADD
    filing = ('*Filed 2026-09-25 by `b535` on the author\'s ruling `(R145)`(3), from relay `data/b532_erratum_draft.md` with one change '
              '— its %d backtick possessives written with apostrophes, ERRATA\'s own form — and one sentence added under Status. '
              'The words "DRAFT, NOT FILED" in the heading, "TO BE FILED ON THE AUTHOR\'S WORD AT THE PASTE AFTER" in the header '
              'and "DRAFT." under Status are the draft\'s, retained as ruled ("with one change"); from this line the entry is '
              'FILED, in the DEPOSIT-FACING list. No deposit action is taken or implied by this entry.*' % len(poss))
    block = lines + ['', filing, '']
    before = rd(ERR)
    code, out = errata_append.append(ERR, EID1, block)
    for x in out:
        print(x)
    if code != 0:
        sys.exit('### REFUSED')
    after = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(after) if l.startswith('## ' + EID1)) + 1
    last = next(i for i, l in enumerate(after) if l.startswith('*Filed 2026-09-25 by `b535`')) + 1
    entry = NL.join(after[first - 1:last])
    # ### the partition list: one bullet inserted after its last DEPOSIT-FACING bullet
    bullet = ('- `%s` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5* (appended to this list by b535 under '
              '`(R145)`(3))' % EID1)
    ins = insert_after(ERR, lambda l: l.startswith('- `E-2026-08-24-2` —'), [bullet])
    after2 = rd(ERR).split(NL)
    first2 = next(i for i, l in enumerate(after2) if l.startswith('## ' + EID1)) + 1
    last2 = next(i for i, l in enumerate(after2) if l.startswith('*Filed 2026-09-25 by `b535`')) + 1
    res = dict(possessives_found=len(poss), possessives=poss, ferry_said=10, entry_lines=[first2, last2],
               backticks_outside_code=backticks_outside_code(NL.join(after2[first2 - 1:last2])),
               backticks_total=NL.join(after2[first2 - 1:last2]).count('`'), partition=ins, append_out=out,
               deposit_facing_absent_from_list=[e for e in ('E-2026-09-14-1', 'E-2026-09-22-1')
                                                if ('- `%s`' % e) not in rd(ERR)])
    put_json('b535_erratum.json', res)
    print('  possessives found in the draft : %d (the ferry said ten) : %s' % (len(poss), poss))
    print('  the filed entry : ERRATA.md:%d-%d ; backticks outside code spans : %d ; backticks in all : %d'
          % (first2, last2, res['backticks_outside_code'], res['backticks_total']))
    print('  the partition bullet : inserted at ERRATA.md:%d (after :%d) ; prior lines kept %s' % (ins['inserted_at'], ins['anchor_line'],
                                                                                                  ins['prior_kept']))
    print('  deposit-facing entries absent from the list, reported and not added : %s' % res['deposit_facing_absent_from_list'])


# ------------------------------------------------------------------------------ COMPONENT 3, the record
def sentence(desc, i, j):
    s0 = max(desc.rfind('. ', 0, i) + 2 if desc.rfind('. ', 0, i) >= 0 else 0, desc.rfind('<p>', 0, i) + 3)
    return ' '.join(html.unescape(desc[s0:j]).split())


def platform():
    Z = jl('b535_zenodo_results.json')
    if not (Z.get('c2') or {}).get('all_match'):
        sys.exit('### REFUSED: the fetch-backs did not all MATCH; no record is written.')
    intended = jl('b535_intended.json')
    names = {'21520474': 'SIDE-kernel v1.5', '21539167': 'A Place To Stand (monograph) Zenodo v1.1.2'}
    block = ['**`%s` — THE THREE DESCRIPTION EDITS AT ZENODO OF `(R145)`(4), WRITTEN BY THE SEAT UNDER `(R110)` AND FETCHED BACK** '
             '*(an append; no prior line is edited, the ledger\'s own law)*' % EID2, '',
             'Filed by `b535`, 2026-09-25, on rulings `(R110)` and `(R145)`(4). The two published records below had their '
             '**description** edited through the legacy deposit API\'s edit / PUT / publish sequence — **no new version, no file '
             'touched, no other field changed** — and each was then fetched back **anonymously** and compared **byte for byte** '
             'against the intended description (relay `data/b535_intended.json`, `data/b535_fetchback_<record>.json`), the bytes '
             'banked before this entry was written. The replacements are `%s`\'s, drafted at b532 (relay `data/b532_rows.txt`) and '
             'rendered in each record\'s own HTML (the drafts\' ellipses the deposited text left unchanged, their "--" the record\'s '
             'dash); the sentence of `Z21520474-01` is the ceiling\'s opening clause of `(R145)`(2), in the ferry\'s words.' % EID1, '']
    rows_out = []
    for rid in ('21520474', '21539167'):
        cell = Z['c2']['records'][rid]
        before = jl('b535_before_%s.json' % rid)['metadata']['description']
        after = json.loads(rd(os.path.join(D, 'b535_fetchback_%s.json' % rid)))['metadata']['description']
        block.append('**Record `%s` — %s** — https://zenodo.org/records/%s — fetch-back sha256 `%s` — **%s**.' % (
            rid, names[rid], rid, cell['fetchback_sha256'], 'MATCH' if cell['match'] else 'MISMATCH'))
        block.append('')
        for p in [p for p in Z['c1']['plan'] if p['record'] == rid]:
            i, j = p['span']
            old_s = sentence(before, i, j)
            k = after.find(p['new'])
            new_s = sentence(after, k, k + len(p['new']))
            m = next(r['match'] for r in cell['rows'] if r['tag'] == p['tag'])
            block.append('- [%s] **description sentence** — before: *%s* — after, as fetched: *%s* — **%s**' % (
                p['tag'], old_s, new_s, 'MATCH' if m else 'MISMATCH'))
            rows_out.append(dict(tag=p['tag'], before=old_s, after=new_s, match=m))
        block.append('')
    block.append('The seat\'s write is bounded by `(R110)` and `(R145)`(4). No mathematical claim is changed by these edits; `h2` '
                 'stands where the deposit left it. No deposit action is taken or implied.')
    code, out = errata_append.append(ERR, EID2, block)
    for x in out:
        print(x)
    if code != 0:
        sys.exit('### REFUSED')
    a = rd(ERR).split(NL)
    first = next(i for i, l in enumerate(a) if l.startswith('**`%s`' % EID2)) + 1
    put_json('b535_platform_record.json', dict(rows=rows_out, entry_first_line=first, out=out))
    print('  E-2026-09-25-2 at ERRATA.md:%d ; %s' % (first, [(r['tag'], r['match']) for r in rows_out]))


# ------------------------------------------------------------------------------ COMPONENT 1
def append_to(path, text):
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def ker_show(spec):
    return subprocess.run(['git', '-C', KER, 'show', spec], capture_output=True, text=True, encoding='utf-8').stdout


def finding():
    if FHEAD in rd(FIND):
        sys.exit('### ALREADY PRESENT')
    h2s = NL.join(ker_show('baed4df:SIDEExplicitFormula/H2Sign.lean').split(NL)[28:31])
    pw = ker_show('baed4df:SIDEExplicitFormula/PowerWindow.lean').split(NL)
    rhs = pw[482]
    seam = pw[494]
    pl = ker_show('baed4df:SIDEExplicitFormula/PowerLimit.lean').split(NL)
    iff = pl[1232]
    of_seam = NL.join(pl[1235:1237])
    assert rhs.startswith('def rh_strip :') and seam.startswith('def rh_strip_imp_rh') and iff.startswith('theorem h2_sign_iff_rh_strip')
    prof = jl('b534_profile.json')
    ax = next(l for l in prof['lines'] if l.startswith("'%sh2_sign_iff_rh_strip'" % NS))
    ax2 = next(l for l in prof['lines'] if l.startswith("'%sh2_sign_imp_rh_of_seam'" % NS))
    tag = rd(os.path.join(D, 'b535_tag.txt'))
    peeled = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.1\^\{\}', tag, re.M).group(1)
    L = ['', FHEAD, '',
         '*Filed at b535, 2026-09-25, on ruling `(R145)`(1): b534 entered as it closed. SIDE-explicit-formula tag `v0.1` = `%s` '
         '(the peeled SHA read back from the remote, relay `data/b535_tag.txt`). Every line below is quoted from the files at that '
         'commit. No grade is conferred in this section; the two correspondence rows carry the grades.*' % peeled, '',
         '**The two statements, verbatim.** `SIDEExplicitFormula/H2Sign.lean:29-31`:', '', '```lean', h2s, '```', '',
         '`SIDEExplicitFormula/PowerWindow.lean:483` (`:481` at `f42102f`, before b534\'s two-line comment note):', '',
         '```lean', rhs, '```', '',
         '**The equivalence, compiled.** `SIDEExplicitFormula/PowerLimit.lean:1233`, with its `#print axioms` line from b534\'s '
         'profile run (relay `data/b534_profile.json`):', '', '```lean', iff, '```', '', '```', ax, '```', '',
         '**The route, in one paragraph.** For an off-line zero ρ₁ the kernel\'s plateau at a small enough width has a nonzero '
         'transform there (`base_nonzero_at`), and by the decay bound (`paperFT_decay` at p = 4) and the kernel\'s local count the '
         'zeros whose score |ĝ(γ_ρ)| lies above any level are finitely many, so an off-line zero of maximal score M exists '
         '(`dominant_exists`, `plateau_dominant`). The window is a real polynomial operator applied to the j-th self-convolution '
         'power of the plateau, P(w) = S(w²)·K(w²)·(1 + c·w): K kills the on-line zeros of score at least M, the odd factor '
         '1 + c·w turns a real tie node negative, and S, interpolated on the nodes v = (ρ − 1/2)² (`real_even_interpolant`, '
         '`nodes_distinct`), makes every tie term −|X|. Its `weilTest` is in classK (`kWindow_classK`); divided by M^(2^(j+1)), '
         'the rest of the zero sum tends to 0 by dominated convergence (Tannery\'s theorem, the dominant summable by the local '
         'count: `dominant_summable`, `rest_tendsto_zero`), so for some j the zero side has negative real part '
         '(`zeroSide_eventually_neg`), and b321\'s identity (`b321_identity`) makes P − PR + A negative for a k in classK, against '
         '`h2_sign`. The converse is b513\'s proof on the strip form (`rh_strip_imp_h2_sign`).', '',
         '**What it consumes.** `EF_lit_zetaZeroConfig` (`Zeta23/WeilEF/Main.lean:286`), through `b321_identity`; the zero side\'s '
         'summability is `EF_lit`\'s own conjunct (`Zeta23/ExplicitFormula.lean:97-100`), proved hypothesis-free for '
         '`zetaZeroConfig`; the vendored zeta23 at v1.0 = `%s`. The navigator read the module at `baed4df` and found no `sorry`, '
         '`axiom`, `native_decide` or `unsafe` in `PowerWindow.lean` or `PowerLimit.lean`; the assembly (`PowerLimit.lean:1167-1193`) '
         'consumes `plateau_dominant`, `kWindow_classK`, `b321_identity` and `Complex.nonneg_iff` and nothing else (`(R145)`(1)).'
         % PIN_ZETA23, '',
         '**The seam, named.** `SIDEExplicitFormula/PowerWindow.lean:495` (`:493` at `f42102f`), a `Prop`, not proved:', '',
         '```lean', seam, '```', '',
         '`h2_sign → RiemannHypothesis` is compiled FROM it, `PowerLimit.lean:1236`:', '', '```lean', of_seam, '```', '', '```', ax2,
         '```', '',
         'Mathlib at the kernel\'s pin holds `riemannZeta_ne_zero_of_one_le_re` (`NumberTheory/LSeries/Nonvanishing.lean:411`) for '
         'Re ≥ 1 and, by name, nothing for Re ≤ 0 — b533\'s probe (relay `data/b533_probe2.txt`). The seam is the one classical '
         'fact that every zero of zeta with Re ≤ 0 is a trivial zero.', '',
         '**This is Weil\'s criterion (1952) in the kernel\'s own objects, a formalization of a classical theorem, not a statement '
         'about where the zeros are.** `h2` stands where the deposit left it; no premise is discharged.', '',
         '*Correspondence rows 384 (`h2_sign_iff_rh_strip`, DERIVES against "h2_sign ↔ rh_strip") and 385 (`h2_sign_imp_rh_of_seam`, '
         'INTERFACES on `rh_strip_imp_rh` against "h2_sign → RH"), by statement-read. Filed by b535 (relay `data/b535_finding.json`).*',
         '']
    w = append_to(FIND, NL.join(L))
    t = rd(FIND).split(NL)
    first = t.index(FHEAD) + 1
    put_json('b535_finding.json', dict(write=w, heading_line=first, peeled=peeled, axioms_line=ax, seam_axioms_line=ax2,
                                       quoted=dict(h2_sign=h2s, rh_strip=rhs, iff=iff, seam=seam, of_seam=of_seam)))
    print('  FINDINGS.md : %(before)d + %(added)d bytes ; prefix %(prefix)s' % w, '; heading at line', first)


# ------------------------------------------------------------------------------ COMPONENT 4
def ceiling_write():
    c = ceiling()
    ns = not_supportable()
    res = dict(ceiling=c, not_supportable=ns)
    # README: a paragraph inserted after its "What is claimed" paragraph; the old sentence kept
    rl = rd(README).split(NL)
    old_ln = rl.index(README_OLD) + 1
    k = old_ln - 1
    while rl[k].strip():
        k += 1
    para_end = rl[k - 1]
    new_para = ['', '*(Reworded under the author\'s ruling `(R145)`(2), 2026-09-25, b535, beside the sentence above, which stays: that '
                'sentence is supportable only with the clause named as `h2_sign` and the two lines below beside it.)* Supportable: '
                '*%s* Not supportable: %s' % (c, ns)]
    ins = insert_after(README, lambda l: l == para_end, new_para)
    rl2 = rd(README).split(NL)
    res['README'] = dict(old_line_before=old_ln, old_line_after=rl2.index(README_OLD) + 1,
                         new_line=next(i for i, l in enumerate(rl2) if 'Reworded under the author' in l) + 1, insert=ins)
    # REGISTRY: a ceiling line inserted at the end of the SIDE-explicit-formula section, citing the tag
    gl = rd(REG).split(NL)
    s = next(i for i, l in enumerate(gl) if l.startswith('## Kernel-table addition — 2026-09-23 — `SIDE-explicit-formula`'))
    e = next((i for i in range(s + 1, len(gl)) if gl[i].startswith('## ')), len(gl))
    last = max(i for i in range(s, e) if gl[i].strip())
    tag = rd(os.path.join(D, 'b535_tag.txt'))
    peeled = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.1\^\{\}', tag, re.M).group(1)
    line = ('**THE CEILING LINE, `(R145)`(2), filed b535, 2026-09-25 — pinned at `SIDE-explicit-formula` tag `v0.1` = `%s` (the '
            'peeled SHA read back from the remote; a tag is not a deposit):** *%s* (The ceiling in force before this line, b532\'s '
            'interim sentence, stands in `OPEN_TRAILS.md`:10790; README\'s older sentence at its line %d; neither is deleted.)'
            % (peeled, c, old_ln))
    raw = open(REG, 'rb').read()
    lines = raw.decode('utf-8-sig').split(NL)
    out = lines[:last + 1] + ['', line] + lines[last + 1:]
    open(REG, 'wb').write(NL.join(out).encode('utf-8'))
    g2 = rd(REG).split(NL)
    kept = g2[:last + 1] + g2[last + 3:] == lines
    res['REGISTRY'] = dict(section_line=s + 1, new_line=last + 3, prior_kept=kept, old='NONE -- REGISTRY carried no ceiling line')
    # OPEN_TRAILS: the old line located; the new sentence goes into this act's record (trail)
    ot = rd(OT).split(NL)
    res['OPEN_TRAILS'] = dict(old_lines=[i + 1 for i, l in enumerate(ot) if OLD_CEIL in ' '.join(l.split()) or
                                        OLD_CEIL.replace("'", '`') in l])
    put_json('b535_ceiling.json', res)
    print('  the ceiling, read from the ferry :', c)
    print('  README : old at %(old_line_before)d before, %(old_line_after)d after ; new at %(new_line)d' % res['README'],
          '; prior kept', ins['prior_kept'])
    print('  REGISTRY : section at %(section_line)d ; new line at %(new_line)d ; prior kept %(prior_kept)s ; old %(old)s' % res['REGISTRY'])
    print('  OPEN_TRAILS : b532`s interim sentence at lines %s (they stay); the new one goes into this act`s record' % res['OPEN_TRAILS']['old_lines'])


# ------------------------------------------------------------------------------ the rows
def rows():
    prof = jl('b534_profile.json')
    std = prof['std3']
    out = []
    specs = [
        ('384', '**WEIL POSITIVITY ON classK AND RH ON THE KERNEL\'S ZERO CONFIGURATION: THE EQUIVALENCE COMPILED BOTH WAYS** (b535, '
         'under (R145), the finding entered). h2_sign_iff_rh_strip : h2_sign ↔ rh_strip, SIDE-explicit-formula v0.1 = baed4df, '
         'PowerLimit.lean:1233; h2_sign as H2Sign.lean:29-31, rh_strip as PowerWindow.lean:483 (:481 at f42102f); no hypothesis. '
         'Weil\'s criterion (1952) in the kernel\'s own objects; not a statement about where the zeros are.',
         '`SIDE-explicit-formula/SIDEExplicitFormula/PowerLimit.lean` : `%sh2_sign_iff_rh_strip` (tag v0.1)' % NS,
         'h2_sign_iff_rh_strip',
         '`h2_sign_iff_rh_strip` DERIVES -- by statement-read, against "h2_sign ↔ rh_strip"'),
        ('385', '**h2_sign → MATHLIB\'S RiemannHypothesis, COMPILED FROM THE SEAM** (b535, under (R145)). h2_sign_imp_rh_of_seam : '
         'rh_strip_imp_rh → h2_sign_imp_rh, PowerLimit.lean:1236 at v0.1; the seam rh_strip_imp_rh (PowerWindow.lean:495, :493 at '
         'f42102f) a Prop, not proved: every zero of zeta with Re ≤ 0 is a trivial zero, ABSENT from Mathlib by name (b533).',
         '`SIDE-explicit-formula/SIDEExplicitFormula/PowerLimit.lean` : `%sh2_sign_imp_rh_of_seam` (tag v0.1)' % NS,
         'h2_sign_imp_rh_of_seam',
         '`h2_sign_imp_rh_of_seam` INTERFACES on rh_strip_imp_rh -- by statement-read, against "h2_sign → RH"'),
    ]
    for num, title, term, name, grade in specs:
        line = next(l for l in prof['lines'] if l.startswith("'%s%s'" % (NS, name)))
        cells = [num, title, term, 'each [propext, Classical.choice, Quot.sound] (%s, b534`s profile, std3 %s)' % (name, std.get(NS + name)),
                 grade, 'No other grade moved; h2 where the deposit left it; nothing deposits.']
        r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
        print(r.stdout[-400:])
        out.append(dict(cells=cells, exit=r.returncode, axioms_line=line))
    put_json('b535_rows.json', dict(rows=out))


# ------------------------------------------------------------------------------ record banks
def scores():
    er = jl('b535_erratum.json')
    Z = jl('b535_zenodo_results.json')
    ce = jl('b535_ceiling.json')
    tag = rd(os.path.join(D, 'b535_tag.txt'))
    peeled = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.1\^\{\}', tag, re.M)
    full = re.search(r'^baed4df full : ([0-9a-f]{40})', tag, re.M)
    span_after = jl('b535_span_after.json')
    tok = jl('b535_tokenscan.json')
    ot = rd(OT)
    rec_i = ot.find(HEADING)
    trail = ot[rec_i:] if rec_i >= 0 else ''
    c = ceiling()
    rows_z = [r for rid in ('21520474', '21539167') for r in ((Z.get('c2') or {}).get('records', {}).get(rid, {}).get('rows') or [])]
    return dict(
        n1=er.get('backticks_outside_code') == 0,
        n2=len(rows_z) == 3 and all(r['match'] for r in rows_z),
        n3=bool(trail) and c in ' '.join(trail.split()) and OLD_CEIL in ' '.join(trail.split())
        and bool((ce.get('README') or {}).get('new_line')) and bool((ce.get('REGISTRY') or {}).get('new_line')),
        n4=span_after.get('current_span') == 1, span_after=span_after.get('current_span'),
        n5=bool(peeled and full and peeled.group(1) == full.group(1)),
        n6=(tok.get('hits_total') == 0 and tok.get('files_scanned', 0) > 0 and not tok.get('warnings')
            and subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2'],
                               capture_output=True, text=True).stdout.strip() == ''),
        s1=span_after.get('current_span') == 0,
        s2=er.get('possessives_found') == 9,
        s3=all(((Z.get('c2') or {}).get('records', {}).get(rid, {}).get('tries') or [{}])[0].get('identical') is True
               for rid in ('21520474', '21539167')),
        possessives=er.get('possessives_found'), trail_present=bool(trail))


def w(v):
    return 'HELD' if v else 'REFUTED'


def components():
    er, pr, fi, ce, rw = jl('b535_erratum.json'), jl('b535_platform_record.json'), jl('b535_finding.json'), jl('b535_ceiling.json'), jl('b535_rows.json')
    L = ['=' * 132, 'b535 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### COMPONENT 6 -- THE TAG:'] + ['  ' + l for l in rd(os.path.join(D, 'b535_tag.txt')).rstrip(NL).split(NL)] + [
         '', '### COMPONENT 3 -- THE PLATFORM EDITS:'] + ['  ' + l for l in rd(os.path.join(D, 'b535_zenodo_c2.txt')).rstrip(NL).split(NL)] + [
         '  E-2026-09-25-2 at ERRATA.md:%s' % pr.get('entry_first_line')] + [
         '  [%(tag)s] before : %(before)s' % r + NL + '  [%(tag)s] after  : %(after)s' % r + NL + '  [%(tag)s] %(m)s' % dict(r, m='MATCH' if r['match'] else 'MISMATCH')
         for r in pr.get('rows', [])] + [
         '', '### COMPONENT 2 -- THE ERRATUM:',
         '  possessives found in the draft : %s (the ferry said ten) : %s' % (er.get('possessives_found'), er.get('possessives')),
         '  the filed entry : ERRATA.md:%s ; backticks outside code spans : %s ; in all : %s' % (er.get('entry_lines'),
                                                                                             er.get('backticks_outside_code'), er.get('backticks_total')),
         '  the partition bullet : ERRATA.md:%s ; prior lines kept %s' % ((er.get('partition') or {}).get('inserted_at'),
                                                                        (er.get('partition') or {}).get('prior_kept')),
         '  deposit-facing entries absent from the list, reported, not added : %s' % er.get('deposit_facing_absent_from_list'),
         '', '### COMPONENT 1 -- THE FINDING: FINDINGS.md:%s ; %s' % (fi.get('heading_line'), fi.get('write')),
         '  axioms : %s' % fi.get('axioms_line'),
         '  rows : %s' % [(r['cells'][0], r['cells'][4], r['exit']) for r in rw.get('rows', [])],
         '', '### COMPONENT 4 -- THE CEILING, (R145)(2), READ FROM THE FERRY:', '  "%s"' % ce.get('ceiling'),
         '  README.md : the old line %s before and %s after ; the new at %s' % ((ce.get('README') or {}).get('old_line_before'),
                                                                               (ce.get('README') or {}).get('old_line_after'),
                                                                               (ce.get('README') or {}).get('new_line')),
         '  REGISTRY.md : %s ; the new line at %s' % ((ce.get('REGISTRY') or {}).get('old'), (ce.get('REGISTRY') or {}).get('new_line')),
         '  OPEN_TRAILS.md : b532`s interim sentence at %s ; the new one in this act`s record' % (ce.get('OPEN_TRAILS') or {}).get('old_lines'),
         '', '### COMPONENT 5 -- THE FOLD: %s' % json.dumps({k: v for k, v in jl('b535_fold.json').items() if k in ('heading', 'writes', 'columns')},
                                                          ensure_ascii=False),
         '  the span tool after the fold : %s' % jl('b535_span_after.json').get('current_span'),
         '', '### THE TOKEN SCAN: %s' % json.dumps({k: v for k, v in jl('b535_tokenscan.json').items() if k != 'files'}), '=' * 132]
    io.open(os.path.join(D, 'b535_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


def desk():
    sc = scores()
    L = ['=' * 104, 'b535 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- backticks outside code spans in the filed entry : %s.' % (w(sc['n1']), jl('b535_erratum.json').get('backticks_outside_code')),
         '  **(N2)** ### **%s.** -- the three replacements : %s.' % (w(sc['n2']), [(r['tag'], r['match']) for r in jl('b535_platform_record.json').get('rows', [])]),
         '  **(N3)** ### **%s.** -- the ceiling equal to the ferry`s (whitespace-joined) and printed beside the old in the trail ; README and REGISTRY lines printed.' % w(sc['n3']),
         '  **(N4)** ### **%s.** -- the span tool reads %s after the fold (it counts from the act after the filing act).' % (w(sc['n4']), sc['span_after']),
         '  **(N5)** ### **%s.** -- peeled SHA against baed4df`s full SHA.' % w(sc['n5']),
         '  **(N6)** ### **%s.** -- the token scan : %s ; the deposit tree clean.' % (w(sc['n6']), {k: v for k, v in jl('b535_tokenscan.json').items() if k in ('hits_total', 'files_scanned', 'commits_scanned', 'warnings')}),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- span after the fold : %s.' % (w(sc['s1']), sc['span_after']),
         '  **(S2)** ### **%s.** -- possessives found : %s.' % (w(sc['s2']), sc['possessives']),
         '  **(S3)** ### **%s.** -- first-try identical at both records.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in rd(os.path.join(D, 'b535_defects.txt')).rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b535_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b535_scores.json', sc)
    print(NL.join(L))


HEADING = '### b535 — the update act: the finding entered, the erratum filed, the descriptions edited, the ceiling reworded, the fold, the tag; (R145) entered'


def trail():
    sc = scores()
    er, pr, ce, fo = jl('b535_erratum.json'), jl('b535_platform_record.json'), jl('b535_ceiling.json'), jl('b535_fold.json')
    tag = rd(os.path.join(D, 'b535_tag.txt'))
    peeled = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.1\^\{\}', tag, re.M).group(1)
    c = ceiling()
    body = [
        '', HEADING, '',
        '**(R145) ratified.** (1) b534 is entered as it closed: `h2_sign ↔ rh_strip` compiled at the standard three, no hypothesis '
        'added, the seam a Prop, `h2_sign → RiemannHypothesis` compiled from it; the navigator\'s read of the module at `baed4df` '
        'recorded. (2) The claim ceiling reworded. (3) E-2026-09-25-1 filed, deposit-facing. (4) The three (R110) edits applied '
        'and recorded as E-2026-09-25-2. (5) The fold of b526–b534. (6) SIDE-explicit-formula tagged `v0.1`. (7) Not this act: '
        'the seam, K1, the register-depth read, the mirror refresh and the memory refresh.',
        '',
        '**The tag.** `v0.1` at `baed4df`; the remote\'s peeled line reads `%s`, equal to `baed4df`\'s full SHA.' % peeled,
        '',
        '**The finding**, appended to `FINDINGS.md` (line %s): *%s* — the two statements verbatim, the equivalence with its '
        '`#print axioms` line, the route, what it consumes, the seam; Weil\'s criterion (1952) in the kernel\'s own objects, not a '
        'statement about where the zeros are. Rows 384 (DERIVES) and 385 (INTERFACES on `rh_strip_imp_rh`).'
        % (jl('b535_finding.json').get('heading_line'), TITLE),
        '',
        '**The erratum.** E-2026-09-25-1 filed at `ERRATA.md`:%s, the draft\'s text with its %s backtick possessives written '
        'as apostrophes (the ferry said ten; the draft carries %s) and the one Status sentence added; its draft-state words are '
        'the draft\'s, a filing line appended beside them. The DEPOSIT-FACING list gains its bullet at line %s; E-2026-09-14-1 '
        'and E-2026-09-22-1, deposit-facing by their own headings and absent from the list, are reported and not added.'
        % (er.get('entry_lines'), er.get('possessives_found'), er.get('possessives_found'), (er.get('partition') or {}).get('inserted_at')),
        '',
        '**The descriptions.** Records 21520474 and 21539167 edited by the (R110) route (edit, PUT, publish; no new version, no '
        'file), fetched back anonymously: %s. Recorded as E-2026-09-25-2 at `ERRATA.md`:%s.'
        % (', '.join('%s %s' % (r['tag'], 'MATCH' if r['match'] else 'MISMATCH') for r in pr.get('rows', [])), pr.get('entry_first_line')),
        '',
        '**The ceiling, reworded under (R145)(2)**, beside b532\'s interim sentence (`OPEN_TRAILS.md`:%s), which stays:'
        % ', :'.join(str(x) for x in (ce.get('OPEN_TRAILS') or {}).get('old_lines', [])),
        '',
        '> old (b532): "%s"' % OLD_CEIL,
        '> new (R145)(2): "%s"' % c,
        '',
        'README carries the new sentence at line %s beside its older one at line %s (kept); REGISTRY carries it at line %s, '
        'pinned to the tag — REGISTRY had no ceiling line before.'
        % ((ce.get('README') or {}).get('new_line'), (ce.get('README') or {}).get('old_line_after'), (ce.get('REGISTRY') or {}).get('new_line')),
        '',
        '**The fold.** `FINDINGS.md` gains **%s** and the digest one block, both appended, prefixes proved; the span tool read '
        '%s before it and reads **%s** after it at this act (it counts from the act after the filing act).'
        % (fo.get('heading', '').lstrip('# '), jl('b535_span.json').get('current_span'), jl('b535_span_after.json').get('current_span')),
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s.'
        % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
        'No lane opened; no kernel file written; nothing deposits — a description edited under (R110) is not a deposit and a tag '
        'is not one; no mirror built ((R145)(7)); no grade moved on any other row; row U1 unedited; `h2` where the deposit left it; '
        'the four lists stay OPEN; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b535_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'erratum': erratum, 'platform': platform, 'finding': finding, 'ceiling': ceiling_write, 'rows': rows,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
