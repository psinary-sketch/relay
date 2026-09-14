# -*- coding: utf-8 -*-
"""b457_components.py -- (R67) THE PROFILES PRINTED AT THE TAG; (R68) THE CELLS; THE SENTENCE GATE PRICED.

### ### **EVERY RULE IS THE LOCKED FACE'S** (`data/b457_registration_2026-09-14.txt`). ### Modes, in order:
### `prepare` (the clone at the hash, verified; the packages copied and verified; the kernel read before);
### `run` (the build and the print, timed, output banked verbatim); `verdict` (per terminal from the output line; the note
### or the trigger); `close` (the scratch tree removed; the kernel read after); `cells` ((R68)); `price` (the gate);
### `report`.
"""
import datetime
import hashlib
import html
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
SCR = os.path.join('D:', os.sep, 'b457-tag-run')
CLONE = os.path.join(SCR, 'SIDE-kernel')
PROFILE_LEAN = os.path.join(SCR, 'RouteProfile.lean')
COMMIT = '0e5233f011533d09e4799107394c216a915028a1'
TAGOBJ = '922c0fc789d0b530447df12da8967fc8bccb0eb0'
RUNJ = os.path.join(D, 'b457_run.json')
RUNTXT = os.path.join(D, 'b457_profile_run.txt')
BUILDLOG = os.path.join(D, 'b457_build_log.txt')
CELLSJ = os.path.join(D, 'b457_cells.json')
PRICEJ = os.path.join(D, 'b457_gate_price.json')
NL = chr(10)
ROUTES = ('structural_exhaustiveness_proved', 'SpectralCannonFull.spectral_cannon', 'ConservationBridge.riemann_hypothesis')
MODULES = ('Bridge.TheBridgeComplete', 'Bridge.ConservationBridge', 'Kernel.SpectralCannonFull')
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def rawread(p):
    with open(p, 'rb') as fh:
        return fh.read().decode('utf-8', 'replace')


def norm(t):
    return t.replace(chr(13) + NL, NL)


def run(cmd, cwd=None, timeout=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def git(repo, *a):
    return run(['git', '-C', repo] + list(a))[1]


def dump_json(path, obj):
    data = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)


def load(path):
    try:
        return json.loads(norm(rawread(path)))
    except Exception:
        return {}


def kernel_state():
    return dict(head=git(KER, 'rev-parse', 'HEAD').strip(), refs_sha=hashlib.sha256(git(KER, 'show-ref').encode()).hexdigest(),
                tracked_status=git(KER, 'status', '--porcelain', '--untracked-files=no'), branch=git(KER, 'rev-parse', '--abbrev-ref', 'HEAD').strip())


def do_prepare():
    J = dict(kernel_before=kernel_state(), started=now().isoformat())
    if os.path.exists(SCR):
        print('  ### the scratch tree already exists -- HALT')
        return 2
    os.makedirs(SCR)
    c, o, e = run(['git', 'clone', '--no-hardlinks', '--no-checkout', KER, CLONE])
    J['clone'] = dict(code=c, err=e.strip()[-300:])
    c, o, e = run(['git', '-C', CLONE, 'checkout', '--detach', COMMIT])
    J['checkout'] = dict(code=c, err=e.strip()[-300:])
    J['clone_head'] = git(CLONE, 'rev-parse', 'HEAD').strip()
    J['clone_tag_object'] = git(CLONE, 'rev-parse', 'refs/tags/v1.5').strip()
    J['clone_remotes'] = git(CLONE, 'remote', '-v').strip()
    J['clean_before'] = git(CLONE, 'status', '--porcelain', '--ignored')
    J['hash_ok'] = J['clone_head'] == COMMIT
    J['tag_ok'] = J['clone_tag_object'] == TAGOBJ
    J['clean_ok'] = J['clean_before'].strip() == ''
    print('  clone head %s ok %s ; tag object %s ok %s ; clean %s ; remotes %r' % (J['clone_head'], J['hash_ok'], J['clone_tag_object'], J['tag_ok'], J['clean_ok'], J['clone_remotes']))
    if not (J['hash_ok'] and J['tag_ok'] and J['clean_ok']):
        dump_json(RUNJ, J)
        print('  ### HALT: the checkout fails its checks')
        return 2
    man = json.loads(rawread(os.path.join(CLONE, 'lake-manifest.json')))
    src, dst = os.path.join(KER, '.lake', 'packages'), os.path.join(CLONE, '.lake', 'packages')
    t0 = now()
    c, o, e = run(['robocopy', src, dst, '/E', '/MT:16', '/NFL', '/NDL', '/NP', '/R:1', '/W:1'])
    J['copy'] = dict(code=c, ok=c < 8, seconds=(now() - t0).total_seconds(), tail=o.strip()[-600:])
    pk = []
    for p in man['packages']:
        rv = git(os.path.join(dst, p['name']), 'rev-parse', 'HEAD').strip()
        pk.append(dict(name=p['name'], manifest=p['rev'], copied=rv, match=rv == p['rev']))
    J['packages'] = pk
    J['packages_ok'] = all(x['match'] for x in pk) and J['copy']['ok']
    J['kernel_build_copied'] = os.path.exists(os.path.join(CLONE, '.lake', 'build'))
    print('  copy code %s ok %s in %.0fs ; packages match %s ; kernel build copied %s' % (c, J['copy']['ok'], J['copy']['seconds'], J['packages_ok'], J['kernel_build_copied']))
    io.open(PROFILE_LEAN, 'w', encoding='utf-8', newline=NL).write(NL.join(['import %s' % m for m in MODULES] + [''] + ['#print axioms %s' % r for r in ROUTES]) + NL)
    J['profile_lean'] = rawread(PROFILE_LEAN)
    dump_json(RUNJ, J)
    return 0 if J['packages_ok'] and not J['kernel_build_copied'] else 2


def do_run():
    J = load(RUNJ)
    if not (J.get('hash_ok') and J.get('tag_ok') and J.get('clean_ok') and J.get('packages_ok')):
        print('  ### HALT: prepare did not pass')
        return 2
    J['lean_version'] = run(['lean', '--version'], cwd=CLONE)[1].strip()
    J['lake_version'] = run(['lake', '--version'], cwd=CLONE)[1].strip()
    b0 = now()
    c, o, e = run(['lake', 'build'] + list(MODULES), cwd=CLONE)
    b1 = now()
    io.open(BUILDLOG, 'w', encoding='utf-8', newline=NL).write(norm(o + NL + e))
    J['build'] = dict(start=b0.isoformat(), end=b1.isoformat(), seconds=(b1 - b0).total_seconds(), code=c)
    J.setdefault('attempts', []).append(dict(attempt=len(J.get('attempts') or []) + 1, mode='foreground', outcome='build returned', build_seconds=(b1 - b0).total_seconds()))
    p0 = now()
    c2, o2, e2 = run(['lake', 'env', 'lean', PROFILE_LEAN], cwd=CLONE)
    p1 = now()
    J['print'] = dict(start=p0.isoformat(), end=p1.isoformat(), seconds=(p1 - p0).total_seconds(), code=c2, stdout=norm(o2), stderr=norm(e2))
    log = norm(o + NL + e)
    J['mathlib_compiled_lines'] = [l for l in log.split(NL) if re.search(r'(Building|Compiling|Built)\s+Mathlib\.', l)][:20]
    J['remote_lines'] = [l for l in log.split(NL) if re.search(r'(?i)cloning|fetching|downloading|git fetch|https?://', l)][:20]
    J['build_jobs_line'] = [l for l in log.split(NL) if re.search(r'Build completed|jobs', l)][-3:]
    dump_json(RUNJ, J)
    H = ['=' * 100, '### b457 -- THE ROUTE TERMINALS` PROFILES PRINTED AT THE DEPOSITED TAG, UNDER (R67).', '=' * 100,
         'SIDE-kernel tag v1.5 : tag object %s ; commit %s' % (TAGOBJ, COMMIT),
         'clone : %s at HEAD %s (tag object in the clone %s) ; clean before the run : %s' % (CLONE, J['clone_head'], J['clone_tag_object'], J['clean_ok']),
         'toolchain : %s' % J['lean_version'], 'lake : %s' % J['lake_version'],
         'packages : %s' % ', '.join('%s@%s' % (x['name'], x['copied'][:10]) for x in J['packages']),
         'build : lake build %s ; start %s ; end %s ; duration %.1f s ; exit code %s (recorded, not a verdict)' % (' '.join(MODULES), b0.isoformat(), b1.isoformat(), J['build']['seconds'], c),
         'print : lake env lean RouteProfile.lean ; start %s ; end %s ; duration %.1f s ; exit code %s (recorded, not a verdict)' % (p0.isoformat(), p1.isoformat(), J['print']['seconds'], c2),
         'attempts : %s' % '; '.join('#%d %s -- %s' % (x['attempt'], x['mode'], x['outcome']) for x in J.get('attempts') or []),
         '', '--- RouteProfile.lean ---', J['profile_lean'].rstrip(NL), '', '--- the print`s stdout, verbatim ---', J['print']['stdout'].rstrip(NL),
         '', '--- the print`s stderr, verbatim ---', J['print']['stderr'].rstrip(NL), '', '--- the build log`s last lines ---'] + log.rstrip(NL).split(NL)[-15:] + ['=' * 100]
    io.open(RUNTXT, 'w', encoding='utf-8', newline=NL).write(NL.join(H) + NL)
    print(NL.join(H))
    return 0


def do_verdict():
    J = load(RUNJ)
    out = (J.get('print') or {}).get('stdout', '')
    rows = []
    for r in ROUTES:
        m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(r), out)
        n = re.search(r"'%s' does not depend on any axioms" % re.escape(r), out)
        if m:
            ax = set(x.strip() for x in m.group(1).split(','))
            rows.append(dict(terminal=r, line=m.group(0), axioms=sorted(ax), verdict='STANDARD THREE' if ax == STD3 else 'OTHER'))
        elif n:
            rows.append(dict(terminal=r, line=n.group(0), axioms=[], verdict='OTHER'))
        else:
            rows.append(dict(terminal=r, line='', axioms=None, verdict='NOT PRINTED'))
    J['verdicts'] = rows
    J['all_standard'] = all(x['verdict'] == 'STANDARD THREE' for x in rows)
    J['banked_readback'] = rawread(RUNTXT) if os.path.exists(RUNTXT) else ''
    J['banked_ok'] = all(x['line'] in J['banked_readback'] for x in rows if x['line']) and TAGOBJ in J['banked_readback'] and COMMIT in J['banked_readback']
    note = None
    if J['all_standard'] and J['banked_ok']:
        note = ('(R67) note, b457, 2026-09-14: the route terminals `structural_exhaustiveness_proved`, `SpectralCannonFull.spectral_cannon` and '
                '`ConservationBridge.riemann_hypothesis` were profiled by `#print axioms` at tag `v1.5` = `0e5233f` from a clean checkout, each printing '
                '`{propext, Classical.choice, Quot.sound}`, and the output is banked in relay `data/b457_profile_run.txt` -- the run that backs the '
                'deposited sentence *"All route terminals report {propext, Classical.choice, Quot.sound}"*.')
        raw = rawread(os.path.join(PP, 'README.md'))
        crlf = (chr(13) + NL) in raw
        ML = norm(raw).split(NL)
        anchor = ML[15].startswith('(R20) note, b456, 2026-09-14:') and ML[16].startswith('**Federation:**')
        J['note_anchor'] = anchor
        if anchor and note not in ML:
            ML = ML[:16] + [note] + ML[16:]
            t = NL.join(ML)
            open(os.path.join(PP, 'README.md') + '.tmp', 'wb').write((t.replace(NL, chr(13) + NL) if crlf else t).encode('utf-8'))
            os.replace(os.path.join(PP, 'README.md') + '.tmp', os.path.join(PP, 'README.md'))
        J['second_matter'] = 'CLOSED'
        J['wave_trigger'] = False
    else:
        J['second_matter'] = 'OPEN'
        J['wave_trigger'] = True
    J['note'] = note
    dump_json(RUNJ, J)
    for x in rows:
        print('  %-40s %-15s %s' % (x['terminal'], x['verdict'], x['line']))
    print('  all standard %s ; banked ok %s ; second matter %s ; wave trigger %s ; note %s' % (J['all_standard'], J['banked_ok'], J['second_matter'], J['wave_trigger'], bool(note)))
    return 0


def do_close():
    J = load(RUNJ)
    sys.path.insert(0, T)
    import force_rm
    t0 = now()
    force_rm.rmtree(SCR)
    J['scratch_removed'] = not os.path.exists(SCR)
    J['scratch_verify'] = str(force_rm.verify_absent(SCR))
    J['close_seconds'] = (now() - t0).total_seconds()
    J['kernel_after'] = kernel_state()
    J['kernel_unmoved'] = J['kernel_after'] == J.get('kernel_before')
    J['lane_closed_at'] = now().isoformat()
    dump_json(RUNJ, J)
    print('  scratch removed %s (%s) in %.0fs ; kernel unmoved %s' % (J['scratch_removed'], J['scratch_verify'], J['close_seconds'], J['kernel_unmoved']))
    return 0 if J['scratch_removed'] and J['kernel_unmoved'] else 2


# =====================================================================================================
# ### COMPONENT 2 -- (R68).
# =====================================================================================================
RES_REL = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
C_OLD, C_NEW = '### **HELD-BRANCH**', '### **MERGED-BRANCH**'


def do_cells():
    path = os.path.join(PP, *RES_REL.split('/'))
    raw = rawread(path)
    crlf = (chr(13) + NL) in raw
    pre = norm(raw)
    RS = pre.split(NL)
    lines = RS[126:130]
    ok = all(l.count(C_OLD) == 1 and '| same branch |' in l for l in lines) and '<!-- b457 CURRENCY ANNOTATION' not in pre
    J = dict(lines=[dict(line=127 + k, original=l, ok=l.count(C_OLD) == 1) for k, l in enumerate(lines)], ok=ok)
    if ok:
        for k in range(126, 130):
            RS[k] = RS[k].replace(C_OLD, C_NEW)
        blk = ['', '<!-- b457 CURRENCY ANNOTATION, 2026-09-14 -->', '',
               '#### **CURRENCY ANNOTATION** *(2026-09-14, b457; existing text preserved apart from the state term named here)*', '',
               '> ### **THE STATUS CELLS OF THE SAME BRANCH, UNDER RULING `(R68)`.** *The lines as they stood, preserved verbatim:*', '']
        for k, l in enumerate(lines):
            blk.append('> - line `%d` (`SIDE-lv-conservation` branch `word-pairing-interface`; fast-forward, tip `5a14205` on `main`’s first-parent line; state term `%s` → `%s`) — *%s*' % (127 + k, C_OLD, C_NEW, l))
        blk += ['', '> ### **WHY.** *`(R68)`, the author’s: these cells take the same term as line `145` (b456), merged-branch. Only the state term changed on each line; no line was removed; no grade, claim or correspondence row moved. `EXHAUSTIVENESS_LICENSE.md:9` is left, dated at its own version, as ruled.*', '']
        post = NL.join(RS).rstrip(NL) + NL + NL.join(blk).rstrip(NL) + NL
        open(path + '.tmp', 'wb').write((post.replace(NL, chr(13) + NL) if crlf else post).encode('utf-8'))
        os.replace(path + '.tmp', path)
        pl = set(post.split(NL))
        J['removed_zero'] = all(l in pl or (l in lines and l in post) for l in pre.split(NL))
        o = git(PP, 'diff', '--numstat', '--', RES_REL).strip().split()
        J['numstat'] = o[:2]
    dump_json(CELLSJ, J)
    print('  cells ok %s ; removed zero %s ; numstat %s' % (ok, J.get('removed_zero'), J.get('numstat')))
    return 0 if ok else 2


# =====================================================================================================
# ### COMPONENT 3 -- THE SENTENCE GATE, PRICED.
# =====================================================================================================
PROOFWORD = re.compile(r'(?i)prov|proof of|establish|show|certif|deriv|verif|machine-check|formali|decide|refute')


def items_of(text):
    out = []
    for block in norm(text).split(NL):
        s = block.strip()
        if not s:
            continue
        if s.startswith('|') or re.match(r'^([-*]|\d+\.) ', s):
            out.append(s)
        else:
            out += [x.strip() for x in re.split(r'(?<=[.;])\s+(?=[A-Z*`(])', s) if x.strip()]
    return out


def declared(repo, rev):
    names = set()
    o = git(repo, 'grep', '-h', '-E', r'^\s*(private |protected |noncomputable )?(theorem|lemma) [^ ]+', rev, '--', '*.lean')
    for l in o.splitlines():
        m = re.match(r'^\s*(?:private |protected |noncomputable )?(?:theorem|lemma) (\S+)', l.split(':', 1)[-1] if l.startswith(rev) else l)
        if m:
            names.add(m.group(1).split('.')[-1])
    return names


def do_price():
    NAMES = declared(KER, 'v1.5') | declared(LV, 'v0.10.0')
    fr = json.loads(norm(rawread(os.path.join(D, 'b359_fetch_F2.json'))))
    S = []
    dep = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
    for f in fr['files']:
        k = f['key']
        p = os.path.join(dep, k)
        ok = ('md5:' + hashlib.md5(open(p, 'rb').read()).hexdigest()) == f['checksum']
        if k.endswith('.svg'):
            S.append(dict(surface='record v1.1.2 / %s' % k, verified=ok, excluded='a graphic', text=''))
            continue
        t = rawread(p)
        if k.endswith('.html'):
            t = html.unescape(re.sub(r'<[^>]+>', NL, t))
        S.append(dict(surface='record v1.1.2 / %s' % k, verified=ok, text=t))
    S.append(dict(surface='record v1.1.2 / description', verified=True, text=NL.join(html.unescape(re.sub(r'<[^>]+>', '', p)) for p in re.findall(r'<p>(.*?)</p>', fr['metadata']['description'], re.S))))
    S.append(dict(surface='SIDE-kernel v1.5 / README.md', verified=True, text=git(KER, 'show', 'v1.5:README.md')))
    S.append(dict(surface='SIDE-kernel v1.5 / .zenodo.json description', verified=True, text=json.loads(git(KER, 'show', 'v1.5:.zenodo.json'))['description']))
    S.append(dict(surface='SIDE-lv-conservation v0.10.0 / README.md', verified=True, text=git(LV, 'show', 'v0.10.0:README.md')))
    per, allpairs, terms, out_of_reach, naming_only = [], [], set(), 0, 0
    sample = []
    for s in S:
        n_items = n_named = n_counted = n_oor = 0
        for it in items_of(s['text']):
            n_items += 1
            toks = set(re.findall(r'`([^`]+)`', it)) | set(t for t in re.findall(r'[A-Za-z][A-Za-z0-9_.′]*', it) if ('_' in t or '.' in t))
            hit = sorted(set(t.strip().split('.')[-1] for t in toks if t.strip().split('.')[-1] in NAMES and len(t.strip().split('.')[-1]) > 2))
            pw = bool(PROOFWORD.search(it))
            if hit:
                n_named += 1
            if hit and pw:
                n_counted += 1
                terms |= set(hit)
                allpairs += [(s['surface'], h) for h in hit]
                if len(sample) < 12:
                    sample.append(dict(surface=s['surface'], item=it[:220], terminals=hit))
            elif pw:
                n_oor += 1
        per.append(dict(surface=s['surface'], verified=s['verified'], excluded=s.get('excluded'), items=n_items, naming_a_terminal=n_named, counted=n_counted, proof_word_no_terminal=n_oor))
        out_of_reach += n_oor
        naming_only += n_named
    Scount, U, P = sum(x['counted'] for x in per), len(terms), len(allpairs)
    acts = max(math.ceil(Scount / 20.0), math.ceil(U / 2.0), math.ceil(P / 12.0)) if Scount else 0
    J = dict(declared_names=len(NAMES), surfaces=per, S=Scount, U=U, P=P, naming_yield=naming_only, out_of_reach=out_of_reach,
             terminals=sorted(terms), sample=sample, formula='max(ceil(S/20), ceil(U/2), ceil(P/12))',
             terms_of_formula=dict(by_items=math.ceil(Scount / 20.0), by_unfoldings=math.ceil(U / 2.0), by_relations=math.ceil(P / 12.0)), acts=acts)
    dump_json(PRICEJ, J)
    for x in per:
        print('  %-50s verified %-5s items %5d naming %4d counted %4d proof-word-no-terminal %4d %s' % (x['surface'], x['verified'], x['items'], x['naming_a_terminal'], x['counted'], x['proof_word_no_terminal'], x['excluded'] or ''))
    print('  declared names %d ; S %d ; U %d ; P %d ; naming yield %d ; out of reach %d ; acts %d %s' % (len(NAMES), Scount, U, P, naming_only, out_of_reach, acts, J['terms_of_formula']))
    return 0


def do_report():
    J, C, P = load(RUNJ), load(CELLSJ), load(PRICEJ)
    face = norm(rawread(os.path.join(D, 'b457_registration_2026-09-14.txt')))
    sh = re.search(r'([0-9a-f]{64})', face.split('THE REGISTRATION LOCK')[-1])
    O = []
    r = O.append
    bar = lambda c='-': r(c * 100)
    bar('=')
    r('b457 -- THE COMPONENTS. ### THE PROFILES PRINTED AT THE TAG, AND THE SENTENCE GATE PRICED.')
    r('### the face, locked before the run and any write : sha256 %s' % (sh.group(1) if sh else '?'))
    r('### RULINGS (R66), (R67), (R68), the author`s, ratified by the paste, entered.')
    bar('=')
    r('')
    bar()
    r('### COMPONENT 1 -- (R67): THE ROUTE TERMINALS PROFILED AT THE DEPOSITED TAG.')
    bar()
    r('  clone : head %s (must be %s) %s ; tag object %s %s ; clean before %s ; remotes %r' % (J.get('clone_head'), COMMIT, J.get('hash_ok'), J.get('clone_tag_object'), J.get('tag_ok'), J.get('clean_ok'), J.get('clone_remotes')))
    r('  packages copied from the local cache (%.0f s, robocopy code %s) ; each at its manifest revision : %s ; the kernel`s own build copied : %s'
      % ((J.get('copy') or {}).get('seconds', 0), (J.get('copy') or {}).get('code'), J.get('packages_ok'), J.get('kernel_build_copied')))
    r('  toolchain : %s ; lake : %s' % (J.get('lean_version'), J.get('lake_version')))
    b, p = J.get('build') or {}, J.get('print') or {}
    r('  build : %.1f s (%s to %s), exit %s ; print : %.1f s (%s to %s), exit %s -- exit codes recorded, never a verdict'
      % (b.get('seconds', 0), b.get('start'), b.get('end'), b.get('code'), p.get('seconds', 0), p.get('start'), p.get('end'), p.get('code')))
    r('  ### THE RUN TOOK TWO ATTEMPTS IN THE SAME VERIFIED CLONE: %s' % ' ; '.join('#%d %s -- %s' % (x['attempt'], x['mode'], x['outcome']) for x in J.get('attempts') or []))
    r('  build log: Mathlib modules compiled %d %s ; remote-contact lines %d %s ; last job lines %s'
      % (len(J.get('mathlib_compiled_lines') or []), (J.get('mathlib_compiled_lines') or [])[:3], len(J.get('remote_lines') or []), (J.get('remote_lines') or [])[:3], J.get('build_jobs_line')))
    r('  the print`s stdout, verbatim:')
    for l in (p.get('stdout') or '').rstrip(NL).split(NL):
        r('    | %s' % l)
    r('')
    r('  | route terminal | output line | verdict |')
    r('  |:--|:--|:--|')
    for x in J.get('verdicts') or []:
        r('  | `%s` | `%s` | **%s** |' % (x['terminal'], x['line'] or '(no line)', x['verdict']))
    r('  banked file data/b457_profile_run.txt carries the tag digest, the commit, the toolchain, the durations and the output : %s' % J.get('banked_ok'))
    if J.get('all_standard') and J.get('banked_ok'):
        r('  ### ### **ALL THREE STANDARD. THE DEPOSITED SENTENCE "All route terminals report {propext, Classical.choice, Quot.sound}" NOW HAS A BANKED RUN BEHIND IT. THE SECOND MATTER CLOSES.**')
        r('  the live note inserted in README.md after the (R20) note (anchor held %s):' % J.get('note_anchor'))
        r('    %s' % J.get('note'))
    else:
        r('  ' + '#' * 96)
        r('  ### ### **WAVE TRIGGER (R66)/(R67): A ROUTE TERMINAL DOES NOT PRINT THE STANDARD THREE AT THE DEPOSITED TAG. THE DEPOSITED SENTENCE IS NOT BACKED. NOTHING ELSE IS DONE.**')
        r('  ' + '#' * 96)
    r('  ### THE LANE: the scratch tree %s removed %s (%s) ; D:\\SIDE-kernel HEAD, refs and tracked status unmoved %s ; closed at %s'
      % (SCR, J.get('scratch_removed'), J.get('scratch_verify'), J.get('kernel_unmoved'), J.get('lane_closed_at')))
    r('')
    bar()
    r('### COMPONENT 2 -- (R68): THE CELLS.')
    bar()
    for x in C.get('lines') or []:
        r('  THE_RESIDUE_OF_RH.md:%d  `%s` -> `%s` ; exactly once %s' % (x['line'], C_OLD, C_NEW, x['ok']))
    r('  the four lines as they stood preserved verbatim in one appended currency annotation ; numstat %s ; LINES REMOVED 0 : %s ; EXHAUSTIVENESS_LICENSE.md:9 not written'
      % (C.get('numstat'), C.get('removed_zero')))
    r('')
    bar()
    r('### COMPONENT 3 -- THE SENTENCE GATE, PRICED AND NOT BUILT.')
    bar()
    r('  terminal names read: %d theorem/lemma names declared in SIDE-kernel@v1.5 and SIDE-lv-conservation@v0.10.0' % P.get('declared_names', 0))
    r('  | surface | checksum verified | items | naming a terminal | naming + a proof word (S) | a proof word, no terminal |')
    r('  |:--|:--|--:|--:|--:|--:|')
    for x in P.get('surfaces') or []:
        r('  | %s%s | %s | %d | %d | %d | %d |' % (x['surface'], (' (excluded: %s)' % x['excluded']) if x.get('excluded') else '', x['verified'], x['items'], x['naming_a_terminal'], x['counted'], x['proof_word_no_terminal']))
    r('  ### S = %d items ; U = %d distinct terminals ; P = %d item-terminal pairs ; naming yield %d ; out of reach %d' % (P.get('S', 0), P.get('U', 0), P.get('P', 0), P.get('naming_yield', 0), P.get('out_of_reach', 0)))
    r('  the terminals named: %s' % ', '.join(P.get('terminals') or []))
    r('  a sample of the counted items (word test, not graded):')
    for s_ in P.get('sample') or []:
        r('    %s -- %s -- *"%s"*' % (s_['surface'], s_['terminals'], s_['item']))
    t = P.get('terms_of_formula') or {}
    r('  ### ### **THE PRICE: ACTS = %s = max(%s, %s, %s) = %d**, on b455`s measured act (20 items read, a pair of terminals unfolded, 12 relations graded).'
      % (P.get('formula'), t.get('by_items'), t.get('by_unfoldings'), t.get('by_relations'), P.get('acts', 0)))
    r('  the bound term is the unfoldings: each distinct terminal must be unfolded before any sentence naming it can be graded.')
    r('  ### WHAT IT WOULD NOT CATCH: every sentence that states what is proved without naming a terminal -- %d items carry a proof word and name none,' % P.get('out_of_reach', 0))
    r('  ### b455`s C2 among their kind ("Proved and machine-checked ... the exhaustiveness of the seven-class catalogue"); and any surface outside the deposited line.')
    r('  ### NOTHING WAS GRADED; THE GATE IS NOT BUILT.')
    r('')
    bar()
    r('### THE EXPECTATIONS.')
    bar()
    n1 = J.get('all_standard') and J.get('second_matter') == 'CLOSED'
    r('  (N1) every route terminal reports the standard three at the tag and the second matter closes : %s' % ('HELD' if n1 else 'REFUTED'))
    s_ok, a_ok = P.get('S', 99) < 40, P.get('acts', 99) < 3
    r('  (N2) fewer than forty terminal-naming items, and one pass under three acts : %s -- S = %d (%s), acts = %d (%s)'
      % ('HELD' if (s_ok and a_ok) else 'REFUTED', P.get('S', 0), 'under forty' if s_ok else 'not under forty', P.get('acts', 0), 'under three' if a_ok else 'not under three'))
    r('  ### the seat`s own from the face: (N1) HELD -- %s; (N2) no reading offered.' % ('HELD' if n1 else 'REFUTED'))
    bar('=')
    io.open(os.path.join(D, 'b457_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(O) + NL)
    print(NL.join(O))
    return 0


def main(argv):
    mode = argv[0] if argv else ''
    fn = dict(prepare=do_prepare, run=do_run, verdict=do_verdict, close=do_close).get(mode) or globals().get('do_' + mode)
    if not fn:
        print('modes: prepare | run | verdict | close | cells | price | report')
        return 2
    return fn()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
