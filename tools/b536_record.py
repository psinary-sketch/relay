# -*- coding: utf-8 -*-
"""b536_record.py -- THE ACT`S CORPUS WRITES AND RECORD, UNDER (R146).
### `python tools/b536_record.py housekeeping | priorart | understandings | ceiling | rows | components | desk | trail`

### Every corpus write INSERTS a line beside a named line or APPENDS; no line is deleted and each write proves every prior line
### stands, in order. The navigator`s text and both ceiling sentences are READ from the banked ferries, not typed. Figures are
### read from the banks.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
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
PRIOR_PP = '6813679'
THMS = ['zeta_zero_re_nonpos', 'rh_strip_imp_rh_holds', 'h2_sign_imp_rh_holds', 'h2_sign_iff_rh', 'h2_sign_imp_ch_holds', 'ch_iff_h2_sign']
RH_PRINT = '∀ (s : ℂ), riemannZeta s = 0 → (¬∃ n, s = -2 * (↑n + 1)) → s ≠ 1 → s.re = 1 / 2'
UTITLE = ("## Understandings arising from the Weil converse arc, b526–b535, in the navigator's words, entered on the author's word "
          "(R146)(5)")
PTITLE = "## The prior-art search for Weil's criterion in Lean, b536, 2026-09-25 — dated and refutable"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def wsj(s):
    return ' '.join((s or '').split())


def insert_after(path, anchor_pred, new_lines):
    raw = open(path, 'rb').read()
    bom = raw[:3] == b'\xef\xbb\xbf'
    lines = raw.decode('utf-8-sig').split(NL)
    k = next(i for i, l in enumerate(lines) if anchor_pred(l))
    out = lines[:k + 1] + new_lines + lines[k + 1:]
    open(path, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + NL.join(out).encode('utf-8'))
    after = rd(path).split(NL)
    head_same = open(path, 'rb').read().startswith((b'\xef\xbb\xbf' if bom else b'') + NL.join(lines[:k + 1]).encode('utf-8'))
    kept = after[:k + 1] + after[k + 1 + len(new_lines):] == lines
    return dict(file=os.path.relpath(path, PP), anchor_line=k + 1, inserted_from=k + 2, inserted=len(new_lines), prior_kept=kept,
                earlier_bytes_same=head_same)


def append_to(path, text):
    before = open(path, 'rb').read()
    add = text.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(path, 'ab').write(add)
    after = open(path, 'rb').read()
    return dict(file=os.path.relpath(path, PP), before=len(before), added=len(after) - len(before), prefix=after.startswith(before))


def seam_line(name):
    t = rd(os.path.join(KER, 'SIDEExplicitFormula', 'Seam.lean')).split(NL)
    return next(i for i, l in enumerate(t) if l.startswith('theorem %s ' % name)) + 1


def peeled():
    m = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.2\^\{\}', rd(os.path.join(D, 'b536_tag.txt')), re.M)
    return m.group(1) if m else ''


def compiled():
    pr = jl('b536_profile.json')
    return all((pr.get('std3') or {}).get(NS + n) is True for n in THMS)


# ------------------------------------------------------------------------------ COMPONENT 2
def housekeeping():
    res = {}
    e = rd(ERR).split(NL)
    head_ln = next(i for i, l in enumerate(e) if l.startswith('## E-2026-09-25-1 ')) + 1
    line_a = ('*Appended under the heading by b536 on the author\'s ruling `(R146)`(3): this entry was FILED at b535, 2026-09-25, on '
              '`(R145)`(3); the heading\'s words "DRAFT, NOT FILED" are the draft\'s, retained as written.*')
    res['a'] = dict(heading_line_before=head_ln, **insert_after(ERR, lambda l: l.startswith('## E-2026-09-25-1 '), ['', line_a]))
    e2 = rd(ERR).split(NL)
    res['a']['heading_line_after'] = next(i for i, l in enumerate(e2) if l.startswith('## E-2026-09-25-1 ')) + 1
    res['a']['line_at'] = e2.index(line_a) + 1
    b_ln = next(i for i, l in enumerate(e2) if l.startswith('- `E-2026-09-25-1` —')) + 1
    bullets = ['- `E-2026-09-14-1` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5* (appended to this list by b536 '
               'under `(R146)`(3); b535 reported the omission)',
               '- `E-2026-09-22-1` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2* (appended to this list by b536 under `(R146)`(3); b535 '
               'reported the omission)']
    res['b'] = dict(last_bullet_line_before=b_ln, **insert_after(ERR, lambda l: l.startswith('- `E-2026-09-25-1` —'), bullets))
    ot = rd(OT).split(NL)
    res['c'] = dict(b535_fold_line=next(i for i, l in enumerate(ot) if l.startswith('**The fold.** `FINDINGS.md` gains **THE WEIL CONVERSE ARC')) + 1,
                    where='this act`s trail record, one line')
    put_json('b536_housekeeping.json', res)
    print(json.dumps(res, indent=1, ensure_ascii=False))


# ------------------------------------------------------------------------------ COMPONENT 3
def priorart():
    g = rd(os.path.join(D, 'b536_priorart_grep.txt'))
    weil_files = re.search(r"### files matching 'weil':\n(.*?)\n### count : (\d+)", g, re.S)
    weil_lines = g[g.index('### hit lines:') + len('### hit lines:'):g.index("### files matching 'explicit formula'")].strip().split(NL)
    ef = re.search(r"### files matching 'explicit formula':\n(.*?)\n### count : (\d+)", g, re.S)
    other = [l for l in weil_lines if l.strip() and not re.search(r'Weilacher|Kurzweil|Mordell-Weil', l)]
    readme = rd(os.path.join(D, 'b536_priorart_readme_main.md'))
    q1 = wsj(readme[readme.index('The Riemann hypothesis is **not proved** here.'):readme.index('RhOutputAxiomLedger.lean (')])
    q2 = 'The negative sign is formal. The positive sign is the open C3 theorem.'
    q3 = 'exists_healthyDetectorData_of_sourceNontrivialZero_right'
    assert q2 in readme and q3 in readme
    notice = NL.join(rd(os.path.join(KER, 'NOTICE')).split(NL)[:3])
    sentence = ("The explicit formula is Zeta23's. A public repository, github.com/peter941221/Connes-Weil-RH-Proof (README fetched by "
                "b536, 2026-09-25), states in Lean, on its own test class, an off-line-zero detector (`" + q3 + "`, \"The negative sign is "
                "formal\") inside the same contradiction architecture, with the Riemann hypothesis not proved there and five project "
                "axioms in its output skeleton; which of its declarations those axioms reach was not read. The two directions of the "
                "criterion on classK — h2_sign ↔ RiemannHypothesis at the standard three (`h2_sign_iff_rh`, SIDE-explicit-formula v0.2) — "
                "are, after this search, the programme's own as Lean theorems on this class; that they are the first formalization of "
                "Weil's criterion in Lean is NOT claimed. The search is dated and refutable.")
    L = ['', PTITLE, '',
         '*Filed at b536 on the author\'s ruling `(R146)`(4), before any sentence claims novelty. Sources: relay `data/b536_priorart_grep.txt` '
         '(the greps), `data/b536_priorart_readme_main.md` (the README, fetched by the seat).*', '',
         '**(1) The explicit formula is Zeta23\'s.** `SIDE-explicit-formula/NOTICE` lines 1-3:', '', '```', notice, '```', '',
         'vendored byte-identical at v1.0 = `3635e748`; its files deriving from PrimeNumberTheoremAnd carry their upstream notices '
         '(NOTICE lines 6-10).', '',
         '**(2) Zeta23 carries no positivity criterion, read from the files.** `grep -i criterion` over `Zeta23/`: **0 files**. '
         '`grep -i positiv`: %s, every hit the `positivity` tactic, the word "positive", or positive-definiteness of a Hermitian form in '
         '`Zeta23/LinAlg/` (Inertia, PosIndex, Sylvester, Weyl) — none a positivity statement about zeros. Zeta23 defines Weil\'s form '
         '`W(f,g)` (`Zeta23/Defs.lean:179-186`) and states the explicit formula (`Zeta23/ExplicitFormula.lean:29`, `:66-68`), and relates '
         'RH only by its sanity anchors (`Zeta23/Statement.lean:152-160`).' % re.search(r"'positiv'.*\n(?:.*\n)*?### count : (.*)", g).group(1), '',
         '**(3) The Mathlib checkout** (`.lake/packages/mathlib`, case-insensitive): **"weil" — %s files**, every hit line an author name '
         '(Felix Weilacher), the substring of "Henstock-Kurzweil", or the Mordell-Weil theorem (`Mathlib/GroupTheory/Descent.lean:46-47`); '
         'lines outside those three: %d. **"explicit formula" — %s files**, every one a closed form (derivatives, Catalan numbers, ζ(2k), '
         'traces and norms, Beta values), none the explicit formula for the zeros of ζ. The file lists are in the bank.'
         % (weil_files.group(2), len(other), ef.group(2)), '',
         '**(4) Related prior art, found.** github.com/peter941221/Connes-Weil-RH-Proof, its README fetched by the seat: *"%s"*; *"%s"*; '
         'its item 2, `%s`, states that a hypothetical zero to the right of the critical line supplies a test g with its detector data. '
         'Its Lean files were not read here.' % (q1, q2, q3), '',
         '**The sentence, in its corrected form (the search found related prior art):** %s' % sentence, '']
    w = append_to(FIND, NL.join(L))
    put_json('b536_priorart.json', dict(write=w, weil_count=int(weil_files.group(2)), weil_other_lines=other, ef_count=int(ef.group(2)),
                                        readme_quotes=[q1, q2, q3], sentence=sentence, heading_line=rd(FIND).split(NL).index(PTITLE) + 1))
    print('  prior-art entry at FINDINGS.md:%d ; weil files %s, other lines %d ; explicit formula files %s'
          % (rd(FIND).split(NL).index(PTITLE) + 1, weil_files.group(2), len(other), ef.group(2)))


# ------------------------------------------------------------------------------ COMPONENT 4
def understandings():
    f = rd(os.path.join(D, 'b536_ferry.txt'))
    text = f[f.index('TEXT BEGIN\n') + len('TEXT BEGIN\n'):f.index('\nTEXT END')]
    paras = [p.replace(' [procedural]', '') for p in text.split(NL) if p.strip()]
    assert len(paras) == 8 and all(p.startswith('%d. ' % (i + 1)) for i, p in enumerate(paras[:7]))
    q = lambda path, n: rd(os.path.join(ROOT, path)).split(NL)[n - 1].strip()
    ladder = [('relay/tools/b511_families.py', 4), ('relay/tools/b511_families.py', 65), ('relay/tools/b511_families.py', 66),
              ('relay/tools/b519_window.py', 9), ('relay/tools/b519_window.py', 86), ('relay/tools/b521_tail.py', 53),
              ('relay/tools/b522_reach.py', 18)]
    qlines = ['`%s:%d`: `%s`' % (p, n, q(p.replace('relay/', ''), n).replace('`', "'")) for p, n in ladder]
    ok = compiled()
    labels = [
        '**[COMPILED — `ch_iff_rh` (`H2Bridge.lean:71`), `h2_sign_iff_rh_strip` (`PowerLimit.lean:1233`); the closure claims ("closes over '
        '…") READING until a closure walk is compiled.]**',
        '**[READING; its expectation — "I expect the two lv-conservation registers to collapse" — EXPECTATION, not a finding.]**',
        '**[CORRECTED — by the window definitions read in their own files. The ladder\'s family is the cardinal B-spline N_m defined by '
        'the Cox–de Boor recursion — the m-fold self-convolution of an indicator only by the classical identity, not so written; and the '
        'b522 witness at width 34, order 7 used NOT that family but variant (B), the indicator of [−W, W] convolved with the order-p '
        'B-spline — a plateau with B-spline ramps, two widths, not a power of one base. So the witness is not a finite instance of '
        '`zeroSide_eventually_neg` as written. The lines:]** ' + ' · '.join(qlines),
        '**[COMPILED — `not_f4_needs` (`RestBound.lean:360`), `h2_sign_iff_rh_strip` (`PowerLimit.lean:1233`).]**',
        '**[COMPILED as the kernel\'s version — `Efac_ne` (`PowerLimit.lean:403`), `tie_term_neg` (`PowerLimit.lean:749`); READING as to '
        'prior knowledge.]**',
        ('**[READING — UPDATED by b536: the seam compiled from Mathlib\'s functional equation, `zeta_zero_re_nonpos` (`Seam.lean:%d`) and '
         '`rh_strip_imp_rh_holds` (`Seam.lean:%d`); `h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis` (`Seam.lean:%d`) lands the criterion on '
         'Mathlib\'s own statement, SIDE-explicit-formula v0.2.]**' % (seam_line('zeta_zero_re_nonpos'), seam_line('rh_strip_imp_rh_holds'),
                                                                      seam_line('h2_sign_iff_rh')))
        if ok else '**[READING — b536\'s seam attempt halted; see the trail.]**',
        '**[READING — the acts: the Epstein control (relay `tools/b325_epstein.py`, its bank completed b505–b506), the numerical witness '
        '(b522–b523), the compiled generalization (b533–b534), the deposit read against the kernel (b531–b532), the erratum and the '
        'platform edit with fetch-back (b535).]**',
        '**[READING — UPDATED by b536\'s search: related prior art was found (the prior-art entry above); "the first of Weil\'s criterion '
        'in Lean" is not supported as written.]**']
    L = ['', UTITLE, '',
         '*Filed at b536 on the author\'s ruling `(R146)`(5). The navigator\'s eight paragraphs are COPIED from the banked ferry (relay '
         '`data/b536_ferry.txt`, between TEXT BEGIN and TEXT END), three procedural tags dropped; each is headed by its status label. The '
         'labels are the record\'s; the words below them are the navigator\'s, unedited.*', '']
    for lab, p in zip(labels, paras):
        L += [lab, '', p, '']
    w = append_to(FIND, NL.join(L))
    put_json('b536_understandings.json', dict(write=w, paragraphs=paras, labels=labels, ladder_lines=qlines,
                                              heading_line=rd(FIND).split(NL).index(UTITLE) + 1))
    print('  understandings at FINDINGS.md:%d ; paragraphs %d' % (rd(FIND).split(NL).index(UTITLE) + 1, len(paras)))


# ------------------------------------------------------------------------------ COMPONENT 5
def new_ceiling():
    f = wsj(rd(os.path.join(D, 'b536_ferry.txt')))
    i = f.index('reads, supportable: "') + len('reads, supportable: "')
    return f[i:f.index('" Not supportable: unchanged', i)]


def old_ceiling():
    return jl('b535_ceiling.json')['ceiling']


def ceiling():
    if not compiled():
        put_json('b536_ceiling.json', dict(stands='(R145)(2) stands'))
        print('(R145)(2) stands')
        return
    c = new_ceiling()
    pk = peeled()
    res = dict(ceiling=c, old=old_ceiling())
    para = ['', '*(Reworded under the author\'s ruling `(R146)`(2), 2026-09-25, b536, beside the `(R145)`(2) sentence above, which stays: the '
            'seam compiled.)* Supportable: *%s* Not supportable: *RH proved*; *h2_sign proved*.' % c]
    res['README'] = insert_after(README, lambda l: l.startswith("*(Reworded under the author's ruling `(R145)`(2)"), para)
    r = rd(README).split(NL)
    res['README'].update(old_line=next(i for i, l in enumerate(r) if l.startswith("*(Reworded under the author's ruling `(R145)`(2)")) + 1,
                         new_line=next(i for i, l in enumerate(r) if l.startswith("*(Reworded under the author's ruling `(R146)`(2)")) + 1)
    line = ('**THE CEILING LINE, `(R146)`(2), filed b536, 2026-09-25 — pinned at `SIDE-explicit-formula` tag `v0.2` = `%s` (the peeled '
            'SHA read back from the remote; a tag is not a deposit):** *%s* (The `(R145)`(2) line above stands.)' % (pk, c))
    res['REGISTRY'] = insert_after(REG, lambda l: l.startswith('**THE CEILING LINE, `(R145)`(2)'), ['', line])
    g = rd(REG).split(NL)
    res['REGISTRY'].update(old_line=next(i for i, l in enumerate(g) if l.startswith('**THE CEILING LINE, `(R145)`(2)')) + 1,
                           new_line=next(i for i, l in enumerate(g) if l.startswith('**THE CEILING LINE, `(R146)`(2)')) + 1)
    put_json('b536_ceiling.json', res)
    print('  the ceiling, read from the ferry :', c)
    print('  README old %s new %s ; REGISTRY old %s new %s' % (res['README']['old_line'], res['README']['new_line'],
                                                               res['REGISTRY']['old_line'], res['REGISTRY']['new_line']))


# ------------------------------------------------------------------------------ the row
CLAIMS = {'zeta_zero_re_nonpos': 'a zero of zeta with Re ≤ 0 is a trivial zero', 'rh_strip_imp_rh_holds': 'rh_strip → RiemannHypothesis',
          'h2_sign_imp_rh_holds': 'h2_sign → RH', 'h2_sign_iff_rh': 'h2_sign ↔ RH',
          'h2_sign_imp_ch_holds': 'h2_sign → conservationHypothesis', 'ch_iff_h2_sign': 'conservationHypothesis ↔ h2_sign'}


def rows():
    pr = jl('b536_profile.json')
    std = pr.get('std3') or {}
    graded = [n for n in THMS if std.get(NS + n) is True]
    cells = ['386',
             '**THE SEAM FROM THE FUNCTIONAL EQUATION; WEIL POSITIVITY ON classK IS MATHLIB\'S RiemannHypothesis** (b536, under (R146)). '
             'SIDE-explicit-formula v0.2, Seam.lean: zeta_zero_re_nonpos (a zero of zeta with Re ≤ 0 is a trivial zero, from '
             'riemannZeta_one_sub); rh_strip_imp_rh_holds; h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis; ch_iff_h2_sign : '
             'conservationHypothesis ↔ h2_sign. Equivalences between open statements; neither side proved.',
             '`SIDE-explicit-formula/SIDEExplicitFormula/Seam.lean` : ' + ', '.join('`%s%s`' % (NS, n) for n in THMS) + ' (tag v0.2)',
             '%d of %d theorems of the module: each [propext, Classical.choice, Quot.sound]' % (len(graded), len(THMS)),
             ' ; '.join('`%s` DERIVES' % n for n in graded) + ' -- each by statement-read against its claim: '
             + '; '.join('%s "%s"' % (n, CLAIMS[n]) for n in graded),
             'No other grade moved; h2 where the deposit left it; nothing deposits; nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-400:])
    put_json('b536_rows.json', dict(cells=cells, exit=r.returncode))


# ------------------------------------------------------------------------------ scores, record
def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    n = 0
    for d0 in (D, T):
        for f in os.listdir(d0):
            if f.startswith('b536_'):
                n += open(os.path.join(d0, f), 'rb').read().count(t)
    return n


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def scores():
    at = jl('b536_attempts.json') or []
    pr = jl('b536_profile.json')
    std = pr.get('std3') or {}
    chk = pr.get('checks') or {}
    p1 = rd(os.path.join(D, 'b536_probe1.txt'))
    pa = jl('b536_priorart.json')
    fails = {}
    for a in at:
        for d0 in a.get('failed_decls', []):
            fails.setdefault(d0, []).append(a['attempt'])
    files = ['ERRATA.md', 'FINDINGS.md', 'README.md', 'REGISTRY.md', 'OPEN_TRAILS.md']
    kept = {f: subseq(subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRIOR_PP, f)], capture_output=True).stdout.decode('utf-8', 'replace')
                      .replace(chr(13), '').lstrip('﻿'), rd(os.path.join(PP, f))) for f in files}
    needle = 'https://' + 'zenodo' + '.org'   # ### built, so the needle is not in this source itself (b536 defect (e))
    zen = [f for f in os.listdir(T) if f.startswith('b536_') and needle in rd(os.path.join(T, f))]
    tok = token_count()
    ot = rd(OT)
    tr = ot[ot.find(HEADING):] if HEADING in ot else ''
    return dict(
        n1=RH_PRINT in p1,
        n2=std.get(NS + 'zeta_zero_re_nonpos') is True and not any(a >= 2 for a in fails.get('zeta_zero_re_nonpos', [])),
        n3=compiled() and (chk.get('h2_sign_iff_rh') or '') == '%sh2_sign_iff_rh : %sh2_sign ↔ RiemannHypothesis' % (NS, NS),
        n4=pa.get('weil_count', 0) >= 0 and pa.get('weil_other_lines') == [],
        n5=all(kept.values()), kept=kept,
        n6=(subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip() == ''
            and not zen and tok == 0), token=tok, zenodo_tools=zen,
        s1='zeta_zero_re_nonpos' not in fails,
        s2=pa.get('weil_count', 0) >= 1 and all(re.search(r'Mordell-Weil|Weil pairing|Weil conjecture', l)
                                                for l in re.findall(r'^\.lake/\S+:\d+:.*$', rd(os.path.join(D, 'b536_priorart_grep.txt')), re.M)
                                                if re.search(r'(?i)weil', l)),
        s3=os.path.exists(os.path.join(D, 'b536_priorart_readme_main.md')) and bool(pa.get('readme_quotes')),
        failures=fails, trail_present=bool(tr))


def w(v):
    return 'HELD' if v else 'REFUTED'


HEADING = '### b536 — the seam from the functional equation; h2_sign ↔ RiemannHypothesis compiled; the housekeeping, the prior art, the understandings; (R146) entered'


def components():
    at, pr = jl('b536_attempts.json') or [], jl('b536_profile.json')
    L = ['=' * 132, 'b536 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '', '### COMPONENT 1 -- THE SEAM: `SIDEExplicitFormula/Seam.lean` (NEW).']
    for a in at:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s ; failing %s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                              a.get('failed_decls') or 'NONE'))
    L += ['  profile :'] + ['    ' + l for l in pr.get('lines', [])]
    L += ['  #check %s : %s' % (k, ' '.join((v or 'NONE').split())) for k, v in (pr.get('checks') or {}).items()]
    L += ['  the tag :'] + ['    ' + l for l in rd(os.path.join(D, 'b536_tag.txt')).rstrip(NL).split(NL)]
    L += ['', '### COMPONENT 2 -- THE HOUSEKEEPING:', '  ' + json.dumps(jl('b536_housekeeping.json'), ensure_ascii=False)]
    L += ['', '### COMPONENT 3 -- THE PRIOR ART:', '  ' + json.dumps({k: v for k, v in jl('b536_priorart.json').items() if k != 'write'}, ensure_ascii=False)]
    L += ['', '### COMPONENT 4 -- THE UNDERSTANDINGS: FINDINGS.md:%s ; item 3 CORRECTED by :' % jl('b536_understandings.json').get('heading_line')]
    L += ['  ' + x for x in jl('b536_understandings.json').get('ladder_lines', [])]
    L += ['', '### COMPONENT 5 -- THE CEILING: ' + json.dumps(jl('b536_ceiling.json'), ensure_ascii=False), '=' * 132]
    io.open(os.path.join(D, 'b536_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc = scores()
    L = ['=' * 104, 'b536 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- probe 1 prints `%s`.' % (w(sc['n1']), RH_PRINT),
         '  **(N2)** ### **%s.** -- zeta_zero_re_nonpos std3, failures %s.' % (w(sc['n2']), sc['failures'].get('zeta_zero_re_nonpos', 'NONE')),
         '  **(N3)** ### **%s.** -- `%s` ; six std3 %s.' % (w(sc['n3']), (jl('b536_profile.json').get('checks') or {}).get('h2_sign_iff_rh'), compiled()),
         '  **(N4)** ### **%s.** -- "weil" files %s, hit lines outside Weilacher / Kurzweil / Mordell-Weil : %s.'
         % (w(sc['n4']), jl('b536_priorart.json').get('weil_count'), jl('b536_priorart.json').get('weil_other_lines')),
         '  **(N5)** ### **%s.** -- every prior line kept, in order : %s.' % (w(sc['n5']), sc['kept']),
         '  **(N6)** ### **%s.** -- deposit tree clean ; b536 tools naming the platform`s address %s ; token hits in b536 files %s.'
         % (w(sc['n6']), sc['zenodo_tools'] or 'NONE', sc['token']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- zeta_zero_re_nonpos failing at : %s.' % (w(sc['s1']), sc['failures'].get('zeta_zero_re_nonpos', 'NONE')),
         '  **(S2)** ### **%s.** -- the hits are Felix Weilacher, "Henstock-Kurzweil" and one Mordell-Weil: most are not another Weil but '
         'another name.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- the README fetched HTTP 200 by the seat.' % w(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(True), [sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in rd(os.path.join(D, 'b536_defects.txt')).rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b536_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b536_scores.json', sc)
    print(NL.join(L))


def trail():
    sc = scores()
    hk, ce, pa = jl('b536_housekeeping.json'), jl('b536_ceiling.json'), jl('b536_priorart.json')
    chk = jl('b536_profile.json').get('checks') or {}
    body = [
        '', HEADING, '',
        '**(R146) ratified.** (1) The seam attempted from Mathlib\'s functional equation. (2) If it compiled, the five theorems, the '
        'ceiling reworded, the kernel tagged v0.2. (3) The housekeeping appends. (4) The prior-art search before any novelty sentence. '
        '(5) The navigator\'s understandings entered in FINDINGS with their status labels.',
        '',
        '**The seam, compiled.** `SIDEExplicitFormula/Seam.lean` (new), clean at attempt 2 (attempt 1 failed in `rh_strip_imp_rh_holds`: '
        '`le_or_lt` unknown at this pin, `le_or_gt` in its place); six of six at the standard three on the whole string. '
        '`zeta_zero_re_nonpos` — a zero of zeta with Re ≤ 0 is a trivial zero — from `riemannZeta_one_sub`, `Complex.Gamma_ne_zero`, '
        '`Complex.cpow_ne_zero_iff` (the checkout\'s form; `Complex.cpow_ne_zero` is unknown), `riemannZeta_ne_zero_of_one_le_re`, '
        '`Complex.cos_eq_zero_iff` and `riemannZeta_zero`. Then `rh_strip_imp_rh_holds`, `h2_sign_imp_rh_holds`, `h2_sign_imp_ch_holds` '
        'and, with no hypothesis:',
        '',
        '```', ' '.join((chk.get('h2_sign_iff_rh') or '').split()), ' '.join((chk.get('ch_iff_h2_sign') or '').split()), '```',
        '',
        'SIDE-explicit-formula tagged `v0.2`; the remote\'s peeled line reads `%s`. **Both sides of each equivalence are open**: '
        'nothing here proves RH or h2_sign.' % peeled(),
        '',
        '**The ceiling, reworded under (R146)(2)**, beside (R145)(2)\'s, which stays:',
        '',
        '> old (R145)(2): "%s"' % ce.get('old', ''),
        '> new (R146)(2): "%s"' % ce.get('ceiling', ''),
        '',
        'README carries it at line %s (the (R145) sentence at %s, kept); REGISTRY at line %s (the (R145) line at %s, kept). The Zenodo '
        'descriptions are not re-edited ((R146)(2), (R66)).' % ((ce.get('README') or {}).get('new_line'), (ce.get('README') or {}).get('old_line'),
                                                              (ce.get('REGISTRY') or {}).get('new_line'), (ce.get('REGISTRY') or {}).get('old_line')),
        '',
        '**The housekeeping.** Under E-2026-09-25-1\'s heading, a line at `ERRATA.md`:%s stating the filing act and that the heading is '
        'retained as written; E-2026-09-14-1 and E-2026-09-22-1 appended to the DEPOSIT-FACING list from line %s, each noting that b535 '
        'reported the omission; every prior line kept, every earlier byte unchanged. **The span tool\'s convention, recorded once under '
        '(R146)(3):** `b363_span.py` counts from the act after the fold\'s filing act — b535\'s fold (its trail line, `OPEN_TRAILS.md`:%s) '
        'read 0 at b535 and reads 1 at this act; the tool is not edited (R96).'
        % ((hk.get('a') or {}).get('line_at'), (hk.get('b') or {}).get('inserted_from'), (hk.get('c') or {}).get('b535_fold_line')),
        '',
        '**The prior art** (`FINDINGS.md`:%s): Zeta23 carries the explicit formula and no positivity criterion (0 files for "criterion"); '
        'Mathlib\'s "weil" hits are %s files, none a criterion; **a public repository, github.com/peter941221/Connes-Weil-RH-Proof, states '
        'in Lean an off-line-zero detector on its own test class, the negative sign "formal", RH not proved there and five project axioms '
        'in its output skeleton** — so the (R146)(4) sentence is entered in corrected form: the two directions on classK are the '
        'programme\'s own as Lean theorems on this class; "the first formalization of Weil\'s criterion in Lean" is not claimed.'
        % (pa.get('heading_line'), pa.get('weil_count')),
        '',
        '**The understandings** (`FINDINGS.md`:%s), the navigator\'s eight paragraphs copied, each labelled; **item 3 entered CORRECTED**: '
        'the b522 witness used variant (B), the indicator of [−W, W] convolved with the order-p B-spline (`relay/tools/b521_tail.py:53`), '
        'not the power window with an indicator base.' % jl('b536_understandings.json').get('heading_line'),
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s.'
        % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
        '**The kernel lane shuts at this act\'s close.** Nothing deposits; nothing at Zenodo written; no grade moved on any other row; row U1 '
        'unedited; `h2` where the deposit left it — an equivalence between two open statements discharges neither; the four lists stay '
        'OPEN; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b536_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'housekeeping': housekeeping, 'priorart': priorart, 'understandings': understandings, 'ceiling': ceiling, 'rows': rows,
              'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
