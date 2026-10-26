"""b713 -- THE STANDING REPORT TOOL, (R323)(3): data/b713_report.txt (.json). A REPORT, NOT AN ARM.

Rewritten whole by the Write tool at b713 from b712's throughstone report (tools/b712_report.py), carried forward under (R323)(3): "The
throughstone report of b712 carried forward as a standing report tool, data/b713_report.txt, its four footings KERNEL, CERTIFIED, REGISTERED,
HELD, its lines recomputed from the banks with path, line and sha256, its scores line printed after the root; it is a report and not an arm."
Two routes:
  bank    (before the root) each line's figures recomputed from the act's JSON banks, beside each its SOURCE -- the bank's path, the row cited
          by line, the bank's sha256 now and, where a hashes bank exists, as that bank records it -- the lines printed in footing order
          (KERNEL, CERTIFIED, REGISTERED, HELD), a footing no line stands on printed as NONE; written through the membrane to data/b713_report.txt
          and data/b713_report.json. Nothing else is written.
  scores  (after the root) the scores line: all eight from data/b713_scores_close.json, each HELD or BROKEN, and the root line from
          data/act_roots.txt; PRINTED ONLY -- no bank is written after the root (N4), and the membrane refuses one.
The tool decides nothing: no verdict is gated on its lines (no arm reads its exit code), and a line it cannot recompute prints as such.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
import b713_worklist as K          # noqa: E402

NL = '\n'
ACT = 'b713'
FOOTINGS = ('KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD')
PP = K.PP
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace')


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.exists(p) else ''


def jl(name):
    t = rd(name)
    return json.loads(t) if t else {}


def sha(name):
    p = os.path.join(D, name)
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def line_of(name, needle):
    for i, l in enumerate(rd(name).split(NL), 1):
        if needle in l:
            return i
    return None


def seat(name, needle):
    """the line's SOURCE: the bank's path, the row cited by line (the first line carrying the needle), its sha256 now."""
    ln, now = line_of(name, needle), sha(name)
    return dict(bank='data/' + name, row=ln, sha256=now, ok=bool(now) and ln is not None,
                text='relay data/%s :%s ; sha256 %s' % (name, ln if ln is not None else '### NEEDLE NOT FOUND', (now or '### ABSENT')[:16]))


def _decl_block(text, head):
    """the declaration whose line opens (after indentation) with `head`, to the first blank line: (its line number, its lines)."""
    L = text.replace('\r', '').split(NL)
    i = next((k for k, l in enumerate(L) if l.lstrip().startswith(head)), None)
    if i is None:
        return None, []
    j = i
    while j < len(L) and L[j].strip():
        j += 1
    return i + 1, L[i:j]


def _binders(sig):
    """the binders between a theorem's name and its top-level colon, as (names, type, bracket); a type's own brackets nest."""
    pairs = {'(': ')', '{': '}', '[': ']', '⦃': '⦄'}
    out, depth, cur, opener = [], 0, '', None
    for ch in sig:
        if depth == 0:
            if ch in pairs:
                depth, opener, cur = 1, ch, ''
            elif ch == ':':
                break
            continue
        if ch == opener:
            depth += 1
        elif ch == pairs[opener]:
            depth -= 1
            if depth == 0:
                nm, _, ty = cur.partition(':')
                out.append((nm.strip(), ' '.join(ty.split()), opener))
                continue
        cur += ch
    return out


CHECK = {}


def throughstone():
    """the root's prompt, the author's word (data/b713_author_answers.txt, transcript line 8485): THE THROUGHSTONE FOR THE KERNEL FOOTING, read
    before the root and printed as the report's opening line -- (a) faces_join's statement verbatim from SIDE-faces-join at the tag, its
    hypotheses by name and type, the grade read under the E0 gate; (b) #print axioms from the join's build artifact by its run id, the
    artifact's sha256 verified, in full; (c) the tag's peeled SHA by ls-remote beside 11a472b9, the tag object's beside it; (d) lv-conservation's
    Register4_positivity at 93c27ec and at the port's tip, equal by statement, and the name faces_join uses resolved to that declaration
    through the join's import; (e) what the re-cut's distance measures, by the bank and line that define it, and the three cells held.
    Reads only: git, gh and the act's banks; nothing written (the bank route writes the report's own two files)."""
    import io as _io
    import zipfile
    import b713_record as REC
    tag, tag_obj, peeled_want = K.JOIN_TAG[0], K.JOIN_TAG[1], K.JOIN_TAG[2]
    differs, regrade = [], []
    # ---------------------------------------------------------------- (a) THE STATEMENT AT THE TAG, ITS HYPOTHESES, THE E0 GATE
    src = g(K.JOIN_DIR, 'show', '%s:FacesJoin.lean' % tag).replace('\r', '')
    ln, blk = _decl_block(src, 'theorem faces_join')
    body = NL.join(blk)
    sig = body[len('theorem faces_join'):body.find(':=')] if ':=' in body else ''
    hyps = _binders(sig)
    concl = ' '.join(sig[sig.find(':') + 1:].split()) if ':' in sig else ''
    variables = [i for i, l in enumerate(src.split(NL), 1) if re.match(r'^\s*variable\b', l)]
    sides = [s.strip() for s in concl.split('↔')]
    for nm, ty, br in hyps:
        hit = [w for w in ('h2_sign', 'Register4_positivity') if w in ty]
        if re.search(r'(?i)licoeff', ty) and '0 ≤' in ty:
            hit.append('a positivity of the Li coefficients')
        if ty == concl or any(s and s in ty for s in sides):
            hit.append('a premise equivalent to its conclusion')
        if hit:
            regrade.append('%s : %s (%s)' % (nm, ty, ', '.join(hit)))
    if variables:
        regrade.append('section variables at :%s' % ', :'.join(map(str, variables)))
    grade = 'DERIVES' if not regrade else 'INTERFACES on ' + '; '.join(regrade)
    a_line = ('(a) THE STATEMENT, SIDE-faces-join FacesJoin.lean :%s at the tag %s, verbatim (below); its hypotheses %d%s; section variables %s; '
              'the E0 gate (no hypothesis stating h2_sign, Register4_positivity, a positivity of the Li coefficients or a premise equivalent '
              'to its conclusion): %s' % (ln, tag, len(hyps), (' -- ' + '; '.join('%s : %s %s' % (n, t, b) for n, t, b in hyps)) if hyps else
                                           ' (NONE: no binder between the name and its colon)', ('at :' + ', :'.join(map(str, variables))) if variables else 'NONE',
                                           'DERIVES STANDS' if grade == 'DERIVES' else '### REGRADE ' + grade))
    # ---------------------------------------------------------------- (b) #print axioms FROM THE BUILD ARTIFACT, BY ITS RUN ID
    repo = 'psinary-sketch/SIDE-faces-join'
    art, arts = REC._artifact_named(repo, K.JOIN_RUN, 'build-module-')
    art = art or {}
    zsha = digest = None
    files, ax_lines, sorry = {}, [], []
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        zsha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        if digest and digest == zsha:
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for nm in z.namelist():
                    files[nm] = z.read(nm).decode('utf-8', 'replace').replace('\r', '')
    banked = re.search(r'sha256 ([0-9a-f]{64})', rd('%s_runner_SIDE-faces-join_join.txt' % ACT))
    banked = banked.group(1) if banked else None
    for nm in sorted(files):
        for l in files[nm].split(NL):
            if 'faces_join' in l and 'depends on axioms' in l:
                ax_lines.append((nm, l.strip()))
            if 'sorryAx' in l:
                sorry.append((nm, l.strip()))
    ax_set = set()
    for _nm, l in ax_lines:
        m = re.search(r'\[(.*)\]', l)
        ax_set |= set(x.strip() for x in (m.group(1).split(',') if m else []))
    ax_ok = bool(ax_lines) and ax_set == {'propext', 'Classical.choice', 'Quot.sound'} and not sorry
    art_ok = bool(zsha) and zsha == digest == banked
    if not (ax_ok and art_ok):
        differs.append('(b)')
    b_line = ('(b) #print axioms FROM THE BUILD ARTIFACT: run %s, artifact %s (id %s), sha256 %s, the platform`s digest %s, the runner bank`s %s -- %s; '
              'printed in full: %s; sorryAx %s; propext, Classical.choice, Quot.sound and nothing else: %s' % (
                  K.JOIN_RUN, art.get('name'), art.get('id'), zsha, digest, banked, 'EQUAL' if art_ok else '### DIFFERS',
                  ' ; '.join('%s: %s' % (n, l) for n, l in ax_lines) or '### NOT FOUND', ('IN ' + '; '.join('%s: %s' % x for x in sorry)) if sorry else 'NONE',
                  'EQUAL' if ax_ok else '### DIFFERS'))
    # ---------------------------------------------------------------- (c) THE TAG AT THE REMOTE
    lsr = dict((r.split('\t')[1], r.split('\t')[0]) for r in g(K.JOIN_DIR, 'ls-remote', 'origin', 'refs/tags/%s' % tag, 'refs/tags/%s^{}' % tag).split(NL) if '\t' in r)
    r_obj, r_peeled = lsr.get('refs/tags/%s' % tag), lsr.get('refs/tags/%s^{}' % tag)
    c_ok = r_peeled == peeled_want and r_obj == tag_obj
    if not c_ok:
        differs.append('(c)')
    c_line = ('(c) THE TAG BY ls-remote: refs/tags/%s^{} %s beside %s -- %s; the tag object refs/tags/%s %s beside %s -- %s' % (
        tag, r_peeled, peeled_want, 'EQUAL' if r_peeled == peeled_want else '### DIFFERS', tag, r_obj, tag_obj, 'EQUAL' if r_obj == tag_obj else '### DIFFERS'))
    # ---------------------------------------------------------------- (d) Register4_positivity AT THE DEPOSIT AND THE TIP; THE NAME RESOLVED BY IMPORT
    rp = jl('%s_regpos.json' % ACT)
    dep, tip = rp.get('deposit') or '', K.PORT_NEW_TIP
    reads = {}
    for c in (dep, tip):
        t = g(K.LV_DIR, 'show', '%s:SIDELvConservation/RegisterPentagon.lean' % c).replace('\r', '')
        l_, b_ = _decl_block(t, 'def Register4_positivity')
        ns = [l.strip() for l in t.split(NL)[:(l_ or 1) - 1] if l.strip().startswith(('namespace', 'end '))]
        reads[c] = (l_, b_, ns)
    norm = [' '.join(' '.join(reads[c][1]).split()) for c in (dep, tip)]
    d_eq = bool(norm[0]) and norm[0] == norm[1]
    imports = [l.strip() for l in src.split(NL) if l.startswith('import ')]
    full = 'SIDELvConservation.RegisterPentagon.Register4_positivity'
    restated = [i for i, l in enumerate(src.split(NL), 1) if re.match(r'^\s*(?:def|abbrev|theorem|lemma|structure|class|instance)\s+\S*Register4_positivity\b', l)]
    resolves = 'import SIDELvConservation.RegisterPentagon' in imports and full in body and not restated
    if not (d_eq and resolves):
        differs.append('(d)')
    d_line = ('(d) %s AT THE DEPOSIT %s (RegisterPentagon.lean :%s, inside %s) AND AT THE PORT`S TIP %s (:%s): %s -- BY STATEMENT %s; the name in '
              'faces_join`s statement %s, the join`s imports %s, no declaration of that name in FacesJoin.lean (%s) -- RESOLVED TO lv-conservation`S '
              'DECLARATION THROUGH THE IMPORT %s' % (
                  full, dep[:8], reads[dep][0], ' / '.join(reads[dep][2]) or '-', tip[:8], reads[tip][0], ' '.join(norm[0].split()) or '### NOT FOUND',
                  'EQUAL' if d_eq else '### DIFFERS', full in body, imports, ('restated at :' + ', :'.join(map(str, restated))) if restated else 'NONE',
                  'EQUAL' if resolves else '### DIFFERS'))
    # ---------------------------------------------------------------- (e) WHAT THE RE-CUT'S DISTANCE MEASURES; THE THREE CELLS HELD
    cut = rd('%s_recut_cut.txt' % ACT).split(NL)
    l_def = line_of('%s_recut_cut.txt' % ACT, 'THE DISTANCE BY THE b670 METHOD: each')
    l_ex = line_of('%s_recut_cut.txt' % ACT, 'UNDERSTATES (not in the distance)')
    held = [(i, m.group(1), m.group(2), m.group(3).strip()) for i, l in enumerate(cut, 1)
            for m in [re.match(r'^\s+:(\d+)\s+\|\s+(\w+)\s+\| HELD\s+\|.*?\|\s+errata \w+\s+\|\s+(.*)$', l)] if m]
    cu = jl('%s_recut_cut.json' % ACT)
    e_line = ('(e) THE RE-CUT`S DISTANCE %s -> %s: the count of the paper`s table rows of verdict OVERREACHES or UNLICENSED whose STATED text still '
              'stands in the document, searched whitespace-normalized at the base and now (relay data/%s_recut_cut.txt :%s-:%s), UNDERSTATES rows '
              'outside it (:%s); the one row standing after the cut a held cell. THE THREE CELLS HELD (the Correspondence table, base :208-:212): %s' % (
                  cu.get('before'), cu.get('after'), ACT, l_def, (l_def or 0) + 1, l_ex,
                  '; '.join('bank :%d -- the paper`s :%s, %s, "%s"' % h for h in held) or '### NONE FOUND'))
    CHECK.update(statement_line=ln, statement=blk, hypotheses=hyps, variables=variables, grade=grade, regrade=regrade, artifact=dict(
        name=art.get('name'), id=art.get('id'), sha256=zsha, digest=digest, banked=banked), axioms=ax_lines, sorry=sorry,
        tag=dict(object=r_obj, peeled=r_peeled), regpos=dict((c[:8], dict(line=reads[c][0], decl=reads[c][1], ns=reads[c][2])) for c in (dep, tip)),
        regpos_equal=d_eq, resolves=resolves, held=held, differs=differs)
    head = ('KERNEL -- THE THROUGHSTONE FOR THE KERNEL FOOTING (the author`s word at the root`s prompt, relay data/%s_author_answers.txt): %s. '
            'DIFFERS %s ; REGRADE %s.' % (ACT, ' ; '.join([a_line, b_line, c_line, d_line, e_line]), differs or 'NONE', regrade or 'NONE'))
    return head + NL + NL.join('        ' + l for l in blk)


def lines():
    keys, seats = {}, []
    # ------------------------------------------------------------------ KERNEL: THE THROUGHSTONE (the author's check at the root's prompt), the opening line
    keys['CHECK'] = throughstone()
    # ------------------------------------------------------------------ KERNEL: THE JOIN
    jg, jt = jl('%s_join_grade.json' % ACT), jl('%s_join_tag.json' % ACT)
    s1, s2 = seat('%s_join_grade.txt' % ACT, 'GRADE DERIVES'), seat('%s_join_tag.txt' % ACT, 'EQUAL')
    ax = (jg.get('axioms') or ['-'])[0]
    three = ax.endswith('[propext, Classical.choice, Quot.sound]')
    keys['JOIN'] = ('KERNEL -- THE JOIN BY CLOSURE: faces_join at SIDE-faces-join %s (tag object %s, peeled %s, at the remote %s/%s, read back %s), '
                    'run %s at ref %s, the lv pin %s (the port`s tip %s); its statement: %s; it names lv-conservation`s own Register4_positivity %s, '
                    'read equal at the deposit and the tip %s; #print axioms: %s -- the standard three %s; the grade %s. SOURCE %s ; %s.' % (
                        jt.get('tag'), (jt.get('object') or '')[:8], (jt.get('peeled') or '')[:8], (jt.get('remote_object') or '')[:8],
                        (jt.get('remote_peeled') or '')[:8], jt.get('ok'), jg.get('run_id'), (jg.get('ref') or '')[:8], (jg.get('pin') or '')[:8],
                        (jg.get('pin') == jg.get('tip')), ' '.join(x.strip() for x in jg.get('statement') or []), jg.get('names_lv'),
                        jg.get('regpos_equal'), ax, three, jg.get('grade'), s1['text'], s2['text']))
    seats += [s1, s2]
    # ------------------------------------------------------------------ KERNEL: THE PORT
    pj, p1 = jl('%s_port.json' % ACT), jl('%s_port_port1.json' % ACT)
    sp = seat('%s_port.txt' % ACT, '### ### **')
    built, mods = len(pj.get('built') or []), len(pj.get('modules') or [])
    art = pj.get('artifact') or {}
    fe1 = re.match(r'^error: SIDELvConservation/(\w+\.lean):(\d+):(\d+):', p1.get('first_error') or '')
    keys['PORT'] = ('KERNEL -- THE FORWARD PORT: SIDE-lv-conservation port-b707 at %s built %d of %d modules on run %s (artifact sha256 %s…, agreeing %s), '
                    'first error %s; the first dispatch, run %s at %s, held at %s; no grade claimed on the port (its print list absent at the tree, '
                    'b707`s reading). SOURCE %s.' % (
                        K.PORT_NEW_TIP[:8], built, mods, pj.get('run_id'), (art.get('sha256') or '')[:16], art.get('agree'),
                        pj.get('first_error') or 'NONE', p1.get('run_id'), K.PORT_EDIT1[:8],
                        ('%s :%s:%s' % fe1.groups()) if fe1 else '-', sp['text']))
    seats.append(sp)
    # ------------------------------------------------------------------ KERNEL: Register4_positivity READ EQUAL
    rp = jl('%s_regpos.json' % ACT)
    sr = seat('%s_regpos.txt' % ACT, 'EQUAL')
    keys['REGPOS'] = ('KERNEL -- Register4_positivity read at the deposit %s (:%s) and at the port`s tip %s (:%s), equal by statement %s, the file`s diff '
                      'lines %s: %s. SOURCE %s.' % ((rp.get('deposit') or '')[:8], rp.get('line_deposit'), (rp.get('tip') or '')[:8], rp.get('line_tip'),
                                                    rp.get('equal'), rp.get('file_diff_lines'), ' '.join(x.strip() for x in rp.get('decl_tip') or []), sr['text']))
    seats.append(sr)
    # ------------------------------------------------------------------ KERNEL: THE RE-CUT'S PINS
    cj = jl('%s_recut_compile.json' % ACT)
    sc = seat('%s_recut_compile.txt' % ACT, '### ### **')
    pins = cj.get('pins') or []
    keys['PINS'] = ('KERNEL -- THE RE-CUT`S PINS: %d of %d standing at their tags (%s), the control one line off reading %s, the old pin 0bc21c0 = v1.3 %s '
                    'with the statement standing %s. SOURCE %s.' % (
                        sum(1 for p in pins if p.get('stands')), len(pins), ', '.join(sorted(set('%s %s' % (p['repo'], p['tag']) for p in pins))),
                        cj.get('control'), (cj.get('oldpin') or {}).get('commit', '')[:7] == (cj.get('oldpin') or {}).get('v13', '-')[:7],
                        (cj.get('oldpin') or {}).get('statement'), sc['text']))
    seats.append(sc)
    # ------------------------------------------------------------------ REGISTERED: THE -15 CONTROL AND ITS PRICE
    pr = jl('%s_price.json' % ACT)
    sg, sq = seat('%s_registrations.txt' % ACT, '### ### **REGISTRATIONS'), seat('%s_price.txt' % ACT, '### ### **')
    first = g(ROOT, 'log', '--format=%H', '--reverse', '%s..HEAD' % K.PRE_RELAY).split(NL)[0].strip()
    files_first = sorted(x for x in g(ROOT, 'show', '--name-only', '--format=', first).split(NL) if x.strip())
    keys['CONTROL'] = ('REGISTERED -- THE CLASS-NUMBER-2 CONTROL AT -15: data/b713_registrations.txt committed at %s, the act`s first relay commit %s '
                       'carrying %s; priced -- the first tier %.2f h, the second %.2f h, the seat`s act budget %.1f h, the cut %s; nothing of the -15 '
                       'zeros computed. SOURCE %s ; %s.' % (
                           K.REG_COMMIT[:8], first[:8] == K.REG_COMMIT[:8], files_first, pr.get('t1') or 0, pr.get('t2') or 0, pr.get('budget') or 0,
                           pr.get('cut'), sg['text'], sq['text']))
    seats += [sg, sq]
    # ------------------------------------------------------------------ REGISTERED: THE FACES ROW
    fl = g(PP, 'show', '%s:FACES_LEDGER.md' % K.C3_PP).replace('\r', '').split(NL)
    fln = next((i for i, l in enumerate(fl, 1) if l.startswith('## UPDATE') and '(b713)' in l), None)
    keys['FACES'] = ('REGISTERED -- THE FACES ROW: FACES_LEDGER.md :%s at PLACE-papers %s, its row naming faces_join, its grade and the peeled SHA %s: %s. '
                     'SOURCE PLACE-papers FACES_LEDGER.md :%s at %s.' % (
                         fln, K.C3_PP[:8], K.JOIN_TAG[2][:8], K.JOIN_TAG[2][:7] in NL.join(fl[(fln or 1) - 1:]) and 'DERIVES' in NL.join(fl[(fln or 1) - 1:]),
                         fln, K.C3_PP[:8]))
    # ------------------------------------------------------------------ REGISTERED: THE RE-CUT
    cu = jl('%s_recut_cut.json' % ACT)
    su, sd = seat('%s_recut_cut.txt' % ACT, '### ### **'), seat('%s_recut_diff.txt' % ACT, '### ### **')
    on_remote = bool(g(PP, 'ls-remote', 'origin', 'refs/heads/' + K.RECUT_BRANCH).strip())
    keys['RECUT'] = ('REGISTERED -- THE RE-CUT OF %s: on the branch %s at %s (at the remote %s: nothing published); the distance by the b670 method %s -> %s, '
                     'the held Correspondence cells %s, the MATCHES rows lost %s. SOURCE %s ; %s.' % (
                         K.RECUT_DOC, K.RECUT_BRANCH, K.RECUT_COMMIT[:8], on_remote, cu.get('before'), cu.get('after'),
                         ', '.join(':%d' % x for x in sorted(set(cu.get('held') or []))),
                         cu.get('matches_lost') or 'NONE', su['text'], sd['text']))
    seats += [su, sd]
    # ------------------------------------------------------------------ HELD
    keys['HELD'] = ('HELD -- the draft at v5 (%s), unpublished; no lv tag (W-ORD-LV-PORT-TAG at OPEN_TRAILS :%s for the author`s word); the Correspondence '
                    'cells of the re-cut held; the -15 source pin priced for b713; the faces ledger head`s :8 sentence for the author`s word.' % (
                        K.DRAFT, K.ORDER_LV_PORT_TAG))
    order = [('KERNEL', ['CHECK', 'JOIN', 'PORT', 'REGPOS', 'PINS']), ('CERTIFIED', []), ('REGISTERED', ['CONTROL', 'FACES', 'RECUT']), ('HELD', ['HELD'])]
    out = []
    for ft, ks in order:
        if not ks:
            out.append('%s -- NONE: no certified computation this act (nothing of the -15 control computed).' % ft)
        out += [keys[k] for k in ks]
    return out, keys, seats, order


def bank():
    import act_membrane as MEM
    import b713_record as REC
    out, keys, seats, order = lines()
    bad = [s['bank'] for s in seats if not s['ok']]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['%s -- THE STANDING REPORT, (R323)(3): THE LINES IN FOOTING ORDER, EACH RECOMPUTED FROM ITS BANKS (%s)' % (ACT, at), '',
         '### rows are the report`s lines in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), each line`s figures recomputed from the act`s JSON',
         '### banks, its SOURCE the bank by path, row and sha256. A report, not an arm: no verdict reads it. The scores line is printed after the',
         '### root by `tools/b713_report.py scores`, and written nowhere.', '']
    L += ['  (%d) %s' % (i + 1, l) for i, l in enumerate(out)]
    L += ['', '### SOURCES NOT SEATED (a needle not found or a bank absent): %s' % (bad or 'NONE'),
          '### ### **THE STANDING REPORT: %d LINES IN FOOTING ORDER ; SOURCES %d, SEATED %d ; THE SCORES LINE AFTER THE ROOT.**' % (
              len(out), len(seats), len(seats) - len(bad))]
    J = dict(at=at, lines=out, keys=keys, seats=seats, unseated=bad, footing=dict(order), throughstone=CHECK)
    for name, b in (('%s_report.txt' % ACT, (NL.join(L) + NL).encode('utf-8')),
                    ('%s_report.json' % ACT, (json.dumps(J, indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(b)
        os.replace(p + '.tmp', p)
    print(NL.join(L[6:]))


def dry():
    out, _k, seats, _o = lines()
    print(NL.join('  (%d) %s' % (i + 1, l) for i, l in enumerate(out)))
    print('### SOURCES NOT SEATED: %s' % ([s['bank'] for s in seats if not s['ok']] or 'NONE'))


def scores():
    sc = jl('%s_scores_close.json' % ACT)
    keys = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    word = dict(HELD='HELD', REFUTED='BROKEN')
    roots = [l for l in rd('act_roots.txt').split(NL) if l.startswith(ACT + ' ')]
    print('### THE ROOT: %s' % (roots[-1] if roots else '### NOT APPENDED -- the scores line waits on the root'))
    print('### THE SCORES (relay data/%s_scores_close.json, sha256 %s…): %s' % (ACT, (sha('%s_scores_close.json' % ACT) or '### ABSENT')[:16],
          ' ; '.join('%s %s' % (k, word.get((sc.get(k) or ['?'])[0], (sc.get(k) or ['?'])[0])) for k in keys)))
    print('### ### **SCORES %d OF %d HELD -- PRINTED AFTER THE ROOT, WRITTEN NOWHERE.**' % (sum(1 for k in keys if (sc.get(k) or [''])[0] == 'HELD'), len(keys)))


def diff():
    """data/b713_report_diff.txt: (R323)(3)'s carry -- this tool against b712's report at the act's base (tools/b712_report.py at relay
    K.PRE_RELAY), by difflib over the two texts; written through the membrane before the root."""
    import difflib
    import act_membrane as MEM
    import b713_record as REC
    old = g(ROOT, 'show', '%s:tools/b712_report.py' % K.PRE_RELAY).replace('\r', '').split(NL)
    new = io.open(os.path.abspath(__file__), encoding='utf-8').read().replace('\r', '').split(NL)
    body = list(difflib.unified_diff(old, new, 'tools/b712_report.py@%s' % K.PRE_RELAY[:8], 'tools/b713_report.py', lineterm=''))
    add = sum(1 for l in body if l.startswith('+') and not l.startswith('+++'))
    rem = sum(1 for l in body if l.startswith('-') and not l.startswith('---'))
    L = ['%s -- (R323)(3): THE STANDING REPORT TOOL CARRIED FORWARD, ITS DIFF AGAINST b712`S REPORT (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())),
         '', '### tools/b713_report.py against tools/b712_report.py at relay %s: +%d -%d. The control of its form: `scores` writes nothing (the membrane' % (K.PRE_RELAY[:8], add, rem),
         '### refuses after the root; the route opens no file for writing), `bank` writes data/b713_report.txt and .json alone.', ''] + body + [
         '', '### ### **THE REPORT TOOL`S DIFF: +%d -%d AGAINST b712`S.**' % (add, rem)]
    p = os.path.join(D, '%s_report_diff.txt' % ACT)
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('bank', 'dry', 'scores', 'diff'):
        print('usage: b713_report.py bank | dry | scores | diff')
        sys.exit(2)
    dict(bank=bank, dry=dry, scores=scores, diff=diff)[r]()
