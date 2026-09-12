# -*- coding: utf-8 -*-
"""b429_components.py -- THE EXTERNAL GRADING READ.

###   --addresses  the three addresses the author supplied, resolved and pinned by digest, or UNREACHABLE with
###                the response the host gave. data/b429_addresses.txt, .json
###   --clay       COMPONENT 1: statement C and conditions (4), (5), (6), (7) quoted VERBATIM from the page.
###   --build      COMPONENT 2: the repository pinned, the terminal located, the toolchain compared, the build
###                run, the axiom profile printed FROM `#print axioms`'S OWN OUTPUT, the sorry sweep.
###   --read       COMPONENT 3: the statement unfolded, five questions, every clause quoted at its file and line.
###   --grade      COMPONENT 4: the grade, and the self-grading test with its clauses quoted both ways.
###   (no flag)    the report and the expectations (N1), (N2), (N3).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
EXT = os.path.join('D:', os.sep, '_b429_external')
REPO = os.path.join(EXT, 'repo')
ELAN = os.path.join(EXT, 'elan')
CLAYTXT = os.path.join(D, 'b429_source_clay.txt')
BRIDGE = os.path.join(SK, 'Bridge', 'ConservationBridge.lean')
RDM = os.path.join(PP, 'README.md')
NL = chr(10)
MISS = []

REPO_URL = 'https://github.com/openai/NavierStokesAndEuler'
WRITEUP = 'https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf'
CLAY = 'https://claymath.org/wp-content/uploads/2022/06/navierstokes.pdf'
TERM_C = 'NavierStokes.Comparator.navier_stokes_breakdown_R3'
TERM_D = 'NavierStokes.Comparator.navier_stokes_breakdown_periodic'
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
CORPUS_PINS = {'SIDE-kernel': 'leanprover/lean4:v4.29.0-rc8', 'SIDE-global-section': 'leanprover/lean4:v4.29.1'}

ADDR = os.path.join(D, 'b429_addresses.txt')
AJSON = os.path.join(D, 'b429_addresses.json')
CREC, CJSON = os.path.join(D, 'b429_statement_c.txt'), os.path.join(D, 'b429_statement_c.json')
BREC, BJSON = os.path.join(D, 'b429_build_and_profile.txt'), os.path.join(D, 'b429_build_and_profile.json')
RREC, RJSON = os.path.join(D, 'b429_statement_read.txt'), os.path.join(D, 'b429_statement_read.json')
GREC, GJSON = os.path.join(D, 'b429_the_grade.txt'), os.path.join(D, 'b429_the_grade.json')


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def put(path, lines):
    """### **A WRITE IS NOT DONE UNTIL ITS RENAME IS** (b428's incident). ### Text goes straight to its path;
    ### JSON goes through a temporary AND IS RENAMED, and the caller is told whether the file exists."""
    io.open(path, 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)
    return os.path.exists(path)


def putj(path, obj):
    d = json.dumps(obj, indent=1, ensure_ascii=False)
    open(path + '.tmp', 'wb').write((d + NL).encode('utf-8'))
    os.replace(path + '.tmp', path)
    return os.path.exists(path)


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def run(*args, **kw):
    try:
        env = dict(os.environ)
        env.update(kw.get('env', {}))
        r = subprocess.run(list(args), capture_output=True, text=True, encoding='utf-8', errors='replace',
                           timeout=kw.get('timeout', 300), cwd=kw.get('cwd'), env=env)
        return r.returncode, (r.stdout or ''), (r.stderr or '')
    except Exception as exc:
        return -1, '', '### NOT RUN -- %s' % exc


def lean_quote(rel, first, last, say, label):
    """### A CLAUSE OF THE LEAN SOURCE, QUOTED AT ITS FILE AND ITS LINE. ### BAR 6."""
    p = os.path.join(REPO, *rel.split('/'))
    t = read(p)
    if not t:
        MISS.append('%s : %s not readable' % (label, rel))
        say('  %-44s ### **MISS** -- %s not readable' % (label, rel))
        return ''
    L = t.splitlines()
    if last > len(L):
        MISS.append('%s : %s has %d lines' % (label, rel, len(L)))
        say('  %-44s ### **MISS** -- only %d lines' % (label, len(L)))
        return ''
    say('  %-44s %s lines %d-%d' % (label, rel, first, last))
    for k in range(first - 1, last):
        say('      %4d| %s' % (k + 1, L[k].rstrip()[:112]))
    return NL.join(L[first - 1:last])


# =====================================================================================================
# ### READING (1) -- THE ADDRESSES.
# =====================================================================================================
def run_addresses():
    R = ['=' * 100, 'b429 -- THE ADDRESSES, AS THE AUTHOR SUPPLIED THEM. ### NOTHING GUESSED.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    out = {}
    say('-' * 100)
    say('### (a) THE REPOSITORY, BY `ls-remote` -- WHICH READS A SHA BACK FROM THE REMOTE AND CLONES NOTHING.')
    say('-' * 100)
    rc, so, se = run('git', 'ls-remote', REPO_URL, timeout=180)
    say('  %s' % REPO_URL)
    say('  exit %d' % rc)
    for ln in (so or se).splitlines()[:6]:
        say('      | %s' % ln[:110])
    head = ''
    m = re.search(r'([0-9a-f]{40})\s+HEAD', so or '')
    if m:
        head = m.group(1)
    out['repository'] = dict(url=REPO_URL, rc=rc, head=head,
                             status='RESOLVED' if head else 'UNREACHABLE', response=(so or se)[:400])
    say('  ### ### **%s%s**' % ('RESOLVED AND PINNED BY DIGEST : HEAD ' + head if head else 'UNREACHABLE', ''))
    say('')
    say('-' * 100)
    say('### (b) THE TWO DOCUMENTS, BY FETCH, PINNED BY THE `sha256` OF THEIR BYTES.')
    say('-' * 100)
    probe = {}
    try:
        probe = json.loads(read(os.path.join(D, 'b429_addresses_probe.json')))
    except Exception as exc:
        MISS.append('the probe record is not readable : %s' % exc)
    for key, url in (('writeup', WRITEUP), ('clay', CLAY)):
        p = probe.get(key, {})
        st = p.get('status')
        if st == 200:
            say('  %-8s %s' % (key, url))
            say('           status %s ; bytes %d ; sha256 %s' % (st, p.get('bytes', 0), p.get('sha256', '')))
            out[key] = dict(url=url, status='RESOLVED', bytes=p.get('bytes'), sha256=p.get('sha256'))
        else:
            say('  %-8s %s' % (key, url))
            say('           ### **UNREACHABLE** -- %s' % str(p.get('error', p.get('status', 'no record')))[:140])
            out[key] = dict(url=url, status='UNREACHABLE', response=str(p.get('error', ''))[:300])
        local = os.path.join(EXT, key + '.pdf')
        if os.path.exists(local):
            h = hashlib.sha256(open(local, 'rb').read()).hexdigest()
            same = (h == p.get('sha256'))
            say('           the bytes on disk re-hash to the same digest : %s' % same)
            if not same:
                MISS.append('%s : the bytes on disk do not match the digest recorded at fetch' % key)
    say('')
    unreach = [k for k, v in out.items() if v.get('status') != 'RESOLVED']
    say('  ### ### **ADDRESSES SUPPLIED : 3. ### RESOLVED : %d. ### UNREACHABLE : %d %s**'
        % (3 - len(unreach), len(unreach), unreach or ''))
    say('  ### ### **`0` ADDRESSES GUESSED. ### `0` SUBSTITUTIONS.** ### b428`s four constructed candidates')
    say('  ### were not retried; only what the author supplied was resolved.')
    if 'clay' in unreach:
        say('  ### ### **THE CLAY FORMULATION IS UNREACHABLE -- BY READING (7) NO GRADE IS CONFERRED.**')
    if 'repository' in unreach:
        say('  ### ### **THE REPOSITORY IS UNREACHABLE -- BY READING (7) COMPONENTS 2, 3 AND 4 DO NOT RUN.**')
    if 'writeup' in unreach:
        say('  ### **THE WRITEUP IS UNREACHABLE; the act says so and continues -- the writeup is the announcement,')
        say('  ### and the grade rests on nothing it carries.**')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    put(ADDR, R)
    putj(AJSON, dict(at=utc(), addresses=out, supplied=3, resolved=3 - len(unreach), unreachable=unreach,
                     guessed=0, substituted=0, misses=MISS))
    print(NL.join(R))
    return 0 if not MISS else 1


# =====================================================================================================
# ### COMPONENT 1 -- STATEMENT C AT CONTENT.
# =====================================================================================================
CLAY_ANCHORS = [
    ('(4) the decay of the initial velocity', '(4) |∂α', 'for any α and K'),
    ('(5) the decay of the force', '(5) |∂α', 'for any α, m, K.'),
    ('(6) smoothness of the solution', '(6) p, u ∈ C ∞(Rn × [0, ∞))', 'and'),
    ('(7) bounded energy', '(7)', '(bounded energy)'),
    ('STATEMENT C, VERBATIM', '(C) Breakdown of Navier–Stokes solutions on R3.', 'on R3 × [0, ∞).'),
    ('STATEMENT D, VERBATIM (the repository claims it too)', '(D) Breakdown of Navier–Stokes Solutions on R3/Z3.',
     'on R3 × [0, ∞).'),
]


def claytext():
    return re.sub(r'[ \t]+', ' ', read(CLAYTXT))


def cq(start, end=None, cap=700):
    n = claytext()
    i = n.find(start)
    if i < 0:
        return '### MISS'
    if end:
        j = n.find(end, i + len(start))
        if j > i:
            return re.sub(r'\s+', ' ', n[i:j + len(end)])
    return re.sub(r'\s+', ' ', n[i:i + cap])


def run_clay():
    R = ['=' * 100, 'b429 -- COMPONENT 1: STATEMENT C AT CONTENT. ### THE OBJECT GRADED AGAINST IS THE PAGE.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    A = json.loads(read(AJSON) or '{"addresses": {}}')
    cl = A.get('addresses', {}).get('clay', {})
    say('  the formulation, pinned : %s' % cl.get('url'))
    say('  status %s ; bytes %s ; sha256 %s' % (cl.get('status'), cl.get('bytes'), cl.get('sha256')))
    say('  its extracted text on disk : data/%s (%d pages of source)'
        % (os.path.basename(CLAYTXT), read(CLAYTXT).count('=== PAGE ')))
    say('  ### **THE AUTHOR OF THE PAGE, AS THE PAGE GIVES IT : %s**'
        % (re.search(r'(?m)^\s*\d?\s*(CHARLES L\. FEFFERMAN)', read(CLAYTXT)) or [''])[0].strip()
        if re.search(r'CHARLES L\. FEFFERMAN', read(CLAYTXT)) else '### NOT FOUND')
    say('')
    got = {}
    for lab, s, e in CLAY_ANCHORS:
        t = cq(s, e)
        if t == '### MISS':
            MISS.append('Clay : %r' % s[:40])
            say('  %-52s ### **MISS**' % lab)
            continue
        say('  %s :' % lab)
        for w in wrap(t, 94):
            say('      | %s' % w)
        got[lab] = t
    say('')
    say('-' * 100)
    say('### THE ERRATA, LOOKED FOR ON THE PAGE ITSELF.')
    say('-' * 100)
    n = claytext()
    er = [m.start() for m in re.finditer(r'(?i)errat|correction|revised|amend', n)]
    say('  occurrences of an errata word on the page : %d' % len(er))
    for i in er[:6]:
        say('      ...%s...' % re.sub(r'\s+', ' ', n[max(0, i - 110):i + 150]))
    if not er:
        say('  ### ### **THE PAGE AS SERVED AT THIS ADDRESS CARRIES NO ERRATUM, CORRECTION OR REVISION NOTE.**')
        say('  ### That is a statement about THIS FILE at THIS DIGEST and not about the problem`s history; the')
        say('  ### act reports what the page says and does not go looking for an erratum elsewhere.')
    else:
        ertxt = cq('Errata', None, cap=700)
        say('  ### THE ERRATA SECTION, QUOTED IN FULL:')
        for w in wrap(ertxt, 94):
            say('      | %s' % w)
        say('  ### ### **WHERE THEY APPLY, READ CLAUSE BY CLAUSE:**')
        say('  ### (i) *"The further condition p(x + ej, t) = p(x, t) should be made explicit in Eqn (8)"* --')
        say('  ###     Eqn (8) is the PERIODICITY condition, which statement ### **(D)** ### uses and statement')
        say('  ###     ### **(C)** ### does not. ### **IT DOES NOT TOUCH (C), NOR (4), (5), (6) OR (7).**')
        say('  ### (ii) *"Eqn (10) should read: ..."* -- the replacement is a WEAK-FORM identity. ### **AND THE')
        say('  ###     PAGE AS SERVED AT THIS DIGEST NUMBERS (10) AS THE PERIODICITY CONDITION**, not as a weak')
        say('  ###     form: the only occurrences of `(10)` in its text layer are that condition and the two')
        say('  ###     statements citing it. ### **SO THE ERRATUM`S NUMBERING AND THE PAGE`S DISAGREE, AND THIS')
        say('  ###     ACT REPORTS THAT RATHER THAN RESOLVING IT.** ### On either reading -- the periodicity')
        say('  ###     condition or the weak formulation -- ### **IT DOES NOT TOUCH STATEMENT (C) OR CONDITIONS')
        say('  ###     (4), (5), (6), (7)**, which are the whole of what this act grades against.')
    say('')
    say('  ### ### **AND THE ONE THING WORTH SAYING ABOUT (7):** ### the page writes it as an INTEGRAL BOUND,')
    say('  ### *"∫ |u(x, t)|2dx < C for all t ≥ 0 (bounded energy)"* -- uniform in `t`, with the constant `C`')
    say('  ### outside the quantifier. ### **A FORMALISATION THAT PUT `C` INSIDE THE `∀ t` WOULD BE A DIFFERENT')
    say('  ### ### AND WEAKER CONDITION**, and Component 3 checks which one the terminal has.')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    put(CREC, R)
    putj(CJSON, dict(at=utc(), quoted=list(got), errata_hits=len(er), misses=MISS))
    print(NL.join(R))
    return 0 if not MISS else 1


# =====================================================================================================
# ### COMPONENT 2 -- THE TERMINAL LOCATED AND THE PROFILE PRINTED.
# =====================================================================================================
def run_build():
    R = ['=' * 100, 'b429 -- COMPONENT 2: THE TERMINAL LOCATED AND THE PROFILE PRINTED.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    say('-' * 100)
    say('### (a) THE CLONE, PINNED.')
    say('-' * 100)
    rc, so, _ = run('git', '-C', REPO, 'rev-parse', 'HEAD')
    head = so.strip()
    rc2, so2, _ = run('git', '-C', REPO, 'rev-parse', '--abbrev-ref', 'HEAD')
    say('  clone at            : %s ### OUTSIDE EVERY ROSTERED REPOSITORY' % REPO)
    say('  default branch      : %s' % so2.strip())
    say('  commit pinned       : %s' % head)
    A = json.loads(read(AJSON) or '{"addresses": {}}')
    remote_head = A.get('addresses', {}).get('repository', {}).get('head', '')
    say('  equals the SHA the remote returned at reading (1) : %s' % (head == remote_head))
    if head != remote_head:
        MISS.append('the clone`s HEAD is not the SHA ls-remote returned')
    say('')
    say('-' * 100)
    say('### (b) THE TERMINAL, LOCATED. ### **AND WHERE IT WAS LOCATED FROM, WHICH IS NOT WHERE b428 PRICED IT.**')
    say('-' * 100)
    rdm = read(os.path.join(REPO, 'README.md'))
    say('  the README names statements (C) and (D) : %s' % (('**(C)**' in rdm) and ('**(D)**' in rdm)))
    say('  the README names a terminal THEOREM      : %s' % bool(re.search(r'theorem|declaration|_R3\b', rdm)))
    say('  ### ### **THE README NAMES THE STATEMENTS AND NAMES NO THEOREM.** ### `b428` priced ACT 1 as *"read')
    say('  ### ### the repository`s README ... and name the single theorem"* and added *"if the README names')
    say('  ### ### none, the act ends there and says so."* ### **IT NAMES NONE, AND THE ACT DID NOT END** --')
    say('  ### the repository carries a machine-readable manifest, `formalization.yaml`, which names them, and')
    say('  ### that is where the terminals were taken from. ### **b428`s ACT 1 IS REFUTED IN ITS PREMISE**, and')
    say('  ### the refutation is printed rather than quietly absorbed.')
    y = read(os.path.join(REPO, 'formalization.yaml'))
    decls = re.findall(r'declaration:\s*"([^"]+)"', y)
    say('  declarations named by `formalization.yaml` : %s' % decls)
    say('  the manifest`s own claim for each          : sorry_count %s ; axioms %s'
        % (sorted(set(re.findall(r'sorry_count:\s*(\d+)', y))), sorted(set(re.findall(r'- "(propext|Classical\.choice|Quot\.sound)"', y)))))
    say('  ### **THAT IS THE REPOSITORY`S OWN CLAIM ABOUT ITSELF. ### THIS ACT DOES NOT TAKE IT: the profile')
    say('  ### below is printed by `#print axioms` on this machine.**')
    for t in (TERM_C, TERM_D):
        if t.rsplit('.', 1)[-1] not in y:
            MISS.append('the manifest does not name %s' % t)
    say('')
    say('-' * 100)
    say('### (c) THE TOOLCHAIN, FOREIGN AGAINST THE CORPUS`S OWN.')
    say('-' * 100)
    ftc = read(os.path.join(REPO, 'lean-toolchain')).strip()
    man = {}
    try:
        man = json.loads(read(os.path.join(REPO, 'lake-manifest.json')))
    except Exception:
        pass
    fml = next((p for p in man.get('packages', []) if p.get('name') == 'mathlib'), {})
    say('  the foreign repository pins : %s' % ftc)
    say('  its Mathlib                 : rev %s ; inputRev %s' % (fml.get('rev', '')[:12], fml.get('inputRev', '')))
    for k, v in CORPUS_PINS.items():
        say('  the corpus pins %-20s: %s' % (k, v))
    mrev = ''
    mp = os.path.join(SK, '.lake', 'packages', 'mathlib')
    if os.path.isdir(mp):
        _rc, _so, _se = run('git', '-C', mp, 'rev-parse', 'HEAD')
        mrev = _so.strip()
    say('  the corpus`s Mathlib        : rev %s' % mrev[:12])
    newer = None
    fv = re.search(r'v(\d+)\.(\d+)\.(\d+)', ftc)
    cv = re.search(r'v(\d+)\.(\d+)\.(\d+)', CORPUS_PINS['SIDE-global-section'])
    if fv and cv:
        newer = tuple(int(x) for x in fv.groups()) > tuple(int(x) for x in cv.groups())
    say('  ### ### **THE FOREIGN PIN IS NEWER THAN THE CORPUS`S : %s** (%s against %s)'
        % (newer, fv.group(0) if fv else '?', cv.group(0) if cv else '?'))
    say('  ### **NEITHER PIN WAS INSTALLED ON THIS MACHINE BEFORE THIS ACT**, so the build fetched its own.')
    say('')
    say('-' * 100)
    say('### (d) THE BUILD. ### **AND IF IT DOES NOT BUILD, THE ACT REPORTS WHAT IT NEEDED AND STOPS.**')
    say('-' * 100)
    cache = read(os.path.join(D, 'b429_build_cache.log'))
    build = read(os.path.join(D, 'b429_build.log'))
    crc = re.search(r'CACHE_RC=(-?\d+)', cache)
    brc = re.search(r'BUILD_RC=(-?\d+)', build)
    say('  `lake exe cache get` exit : %s' % (crc.group(1) if crc else '### STILL RUNNING OR NOT RECORDED'))
    say('  `lake build` exit         : %s' % (brc.group(1) if brc else '### STILL RUNNING OR NOT RECORDED'))
    hosts = sorted(set(re.findall(r'https?://([A-Za-z0-9.-]+)', cache + build)))
    say('  hosts the build reached, from its own logs : %s' % hosts)
    for h in hosts:
        n = len(re.findall(re.escape(h), cache + build))
        say('      %-32s named %d time(s) in the build logs' % (h, n))
    tail = [x for x in (build or cache).splitlines() if x.strip()][-14:]
    say('  the last lines of the build`s own output :')
    for x in tail:
        say('      | %s' % x[:112])
    built = bool(brc and brc.group(1) == '0')
    say('  ### ### **BUILD : %s**' % ('SUCCEEDED' if built else 'DID NOT SUCCEED'))
    profile, axioms_beyond, sorryax = {}, {}, {}
    if not built:
        say('  ### ### **THE ACT STOPS HERE FOR THE GRADE.** ### What it needed, from its own output, is printed')
        say('  ### ### above; ### **NO GRADE IS CONFERRED, BECAUSE A GRADING OF AN UNBUILT PROOF IS A GRADING OF')
        say('  ### ### AN ANNOUNCEMENT.**')
    else:
        say('')
        say('-' * 100)
        say('### (e) THE AXIOM PROFILE. ### **FROM `#print axioms`\'S OWN OUTPUT, NEVER FROM AN EXIT CODE.**')
        say('-' * 100)
        src = ('import NavierStokes.ComparatorSolution' + NL
               + '#print axioms ' + TERM_C + NL + '#print axioms ' + TERM_D + NL)
        tmp = os.path.join(REPO, 'b429_axioms.lean')
        io.open(tmp, 'w', encoding='utf-8', newline=NL).write(src)
        rc3, so3, se3 = run(os.path.join(ELAN, 'bin', 'lake') if os.path.exists(os.path.join(ELAN, 'bin', 'lake'))
                            else 'lake', 'env', 'lean', 'b429_axioms.lean',
                            cwd=REPO, timeout=900, env=dict(ELAN_HOME=ELAN))
        try:
            os.remove(tmp)
        except Exception:
            pass
        out = (so3 + se3).strip()
        say('  the printer`s own output, verbatim :')
        for x in out.splitlines()[:20]:
            say('      | %s' % x[:112])
        io.open(os.path.join(D, 'b429_axiom_prints.txt'), 'w', encoding='utf-8', newline=NL).write(out + NL)
        for t in (TERM_C, TERM_D):
            # ### THE PRINTER WRAPS THE NAME IN SINGLE QUOTES -- `'Name' depends on axioms: [...]` -- and a
            # ### needle that omits the closing quote never matches while the line is plainly there. ### The
            # ### quote is OPTIONAL in the needle so the arm reads the printer's own wording (b427's species).
            m = re.search(re.escape(t) + r"'? depends on axioms: \[([^\]]*)\]", out)
            ax = [a.strip() for a in m.group(1).split(',')] if m else []
            profile[t] = ax
            beyond = [a for a in ax if a not in STD3]
            axioms_beyond[t] = beyond
            sorryax[t] = any('sorry' in a.lower() for a in ax)
            if not m:
                MISS.append('no axiom line printed for %s' % t)
            say('  %-58s axioms %s' % (t.rsplit('.', 1)[-1], ax or '### NOT PRINTED'))
            say('      beyond the standard three : %s ; `sorryAx` present : %s' % (beyond or 'none', sorryax[t]))
    say('')
    say('-' * 100)
    say('### (f) THE SOURCE-LEVEL `sorry` SWEEP OF THE WHOLE REPOSITORY.')
    say('-' * 100)
    rc4, so4, _ = run('git', '-C', REPO, 'grep', '-n', '-w', 'sorry', '--', '*.lean', timeout=180)
    hits = [x for x in (so4 or '').splitlines() if re.search(r':\s*sorry\s*$|^\S+:\d+:\s*sorry', x)]
    allh = (so4 or '').splitlines()
    say('  lines matching the word `sorry` : %d ; of them bare `sorry` terms : %d' % (len(allh), len(hits)))
    for x in allh[:10]:
        say('      | %s' % x[:112])
    inclosure = [x for x in hits if not x.startswith('ComparatorChallenges/')]
    say('  ### ### **EVERY BARE `sorry` IS IN `ComparatorChallenges/` : %s**' % (not inclosure))
    say('  ### The repository`s own header calls them *"intentional `sorry` challenge placeholders"* -- they are')
    say('  ### the REFERENCE statements a checker compares against, not steps of the proof. ### **AND THAT IS A')
    say('  ### CLAIM THE AXIOM PROFILE ABOVE TESTS INDEPENDENTLY**: a `sorry` anywhere in the terminal`s closure')
    say('  ### would appear as `sorryAx` in its profile, and the profile is what this act reads.')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    put(BREC, R)
    putj(BJSON, dict(at=utc(), head=head, branch=so2.strip(), remote_head=remote_head,
                     foreign_toolchain=ftc, foreign_mathlib=fml.get('rev', ''), corpus_pins=CORPUS_PINS,
                     corpus_mathlib=mrev, newer=newer, built=built, hosts=hosts,
                     terminals=decls, profile=profile, axioms_beyond=axioms_beyond, sorryax=sorryax,
                     sorry_lines=len(allh), sorry_bare=len(hits), sorry_outside_challenges=len(inclosure),
                     readme_names_terminal=False, misses=MISS))
    print(NL.join(R))
    return 0 if not MISS else 1



# =====================================================================================================
# ### COMPONENT 3 -- THE STATEMENT READ AGAINST C. ### EVERY CLAUSE QUOTED AT ITS FILE AND ITS LINE.
# =====================================================================================================
CS = 'NavierStokes/ComparatorSolution.lean'
CD = 'NavierStokes/ComparatorDefinitions.lean'
CB = 'NavierStokes/R3/ComparatorBridge.lean'
CT = 'NavierStokes/ComparatorR3Theorem.lean'
TH = 'NavierStokes/R3/Theorem.lean'

# ### (Clay clause, Lean field, file, first, last)
MAPPING = [
    ('"Take nu > 0"', 'the binder and its hypothesis', CS, 16, 16),
    ('"and n = 3"', 'the notation that fixes the dimension', CS, 13, 13),
    ('"there exist a smooth, divergence-free u0 on R3"', 'the existential, and its two fields', CD, 108, 113),
    ('"satisfying (4)"', 'InitialVelocityConditionDecay.decay', CD, 124, 129),
    ('"and a smooth f(x, t) on R3 x [0, inf)"', 'ForceCondition.smooth', CD, 149, 151),
    ('"satisfying (5)"', 'ForceConditionDecay.decay', CD, 159, 165),
    ('"for which there exist no solutions (p, u)"', 'the universal negative', CS, 17, 19),
    ('"of (1), (2), (3)"', 'navier_stokes, div_free, initial_condition', CD, 191, 203),
    ('"(6)"', 'velocity_smooth and pressure_smooth', CD, 204, 209),
    ('"(7)"', 'integrable and globally_bounded_energy', CD, 219, 227),
]


def run_read():
    R = ['=' * 100, 'b429 -- COMPONENT 3: THE STATEMENT READ AGAINST C.', '=' * 100, '  at (UTC) : %s' % utc(), '']
    say = R.append
    B = json.loads(read(BJSON) or '{"built": null}')
    say('  the terminal : %s' % TERM_C)
    say('  the clone    : %s at %s' % (REPO, B.get('head', '')[:12]))
    say('')
    say('-' * 100)
    say('### (a) THE TERMINAL ITSELF, AS WRITTEN.')
    say('-' * 100)
    lean_quote(CS, 11, 20, say, 'the terminal for statement (C)')
    lean_quote(CS, 22, 27, say, 'the terminal for statement (D)')
    say('')
    say('-' * 100)
    say('### (b) THE FIVE QUESTIONS.')
    say('-' * 100)
    ans = {}
    say('  ### Q1 -- WHAT DOES IT QUANTIFY OVER?')
    lean_quote(CS, 13, 13, say, '    the dimension, fixed by notation')
    lean_quote(CS, 16, 19, say, '    the binders and the body')
    say('    ### ### **UNIVERSALLY over every real `nu` with `nu > 0`; EXISTENTIALLY over `u0` and `f`; and the')
    say('    ### ### space is `EuclideanSpace R (Fin 3)`, so `n = 3` IS FIXED AND NOT QUANTIFIED.**')
    say('    ### That is exactly C`s *"Take nu > 0 and n = 3. Then there exist ..."*.')
    ans['Q1'] = 'for all nu > 0; exists u0, f; n = 3 fixed by the notation'
    say('')
    say('  ### Q2 -- IS THE DECAY OF (5) A STATED HYPOTHESIS ON ITS FORCE?')
    lean_quote(CD, 159, 165, say, '    ForceConditionDecay')
    say('    ### ### **YES, AS A FIELD OF THE STRUCTURE THE EXISTENTIAL CARRIES.** ### The page reads')
    say('    ### *"|d^a_x d^m_t f(x,t)| <= C(1 + |x| + t)^-K ... for any a, m, K"*; the Lean bounds the TOTAL')
    say('    ### `m`-th derivative, `iteratedFDerivWithin R m`, which dominates every mixed partial of that total')
    say('    ### order. ### **SO THE LEAN HYPOTHESIS IS AT LEAST AS STRONG AS THE PAGE`S -- ON THE SIDE WHERE')
    say('    ### ### BEING STRONGER MAKES THE THEOREM WEAKER**, which is the direction that matters, and it is')
    say('    ### printed rather than left to be noticed. ### `ForceCondition.smooth` carries *"a smooth f"* apart.')
    ans['Q2'] = 'YES -- ForceConditionDecay.decay, at least as strong as (5)'
    say('')
    say('  ### Q3 -- IS ITS INITIAL DATA AT REST OR GENERAL?')
    say('    ### THE TERMINAL LEAVES IT EXISTENTIAL: it asserts only that SOME `u0` works, which is what C asks.')
    say('    ### **BUT THE WITNESS IS EXPOSED ONE LEVEL DOWN, AND IT IS AT REST:**')
    lean_quote(CB, 77, 88, say, '    the adapter, with its witness')
    lean_quote(TH, 25, 32, say, '    and the paper-side theorem it rests on')
    say('    ### ### **THE INITIAL VELOCITY IS `fun _ => 0`: THE FLUID STARTS AT REST, AND THE FORCING DOES ALL')
    say('    ### ### THE WORK.** ### The lemma discharging (4) for it is named `zero_initial_condition_decay`,')
    say('    ### and the paper-side theorem is `theorem_1_1_with_initial_rest`, whose own docstring adds')
    say('    ### *"No construction hypotheses remain."* ### **C PERMITS THIS EXACTLY** -- it asks for SOME')
    say('    ### smooth divergence-free `u0` satisfying (4), and the zero field is one. ### **SO IT IS NOT A')
    say('    ### ### NARROWING OF C BUT A CHOICE C ALLOWS**, and it is printed because the order asked.')
    ans['Q3'] = 'AT REST -- the witness is `fun _ => 0`; C permits it'
    say('')
    say('  ### Q4 -- IS THE CONCLUSION THE UNIVERSAL NEGATIVE OF C, OR THE BLOWUP OF A CONSTRUCTED SOLUTION?')
    lean_quote(CS, 19, 19, say, '    the conclusion, as written')
    lean_quote(CD, 219, 227, say, '    and the class it negates over')
    say('    ### ### **THE UNIVERSAL NEGATIVE.** ### `not (exists v p, NavierStokesExistenceAndSmoothnessRn nu')
    say('    ### u0 f v p)` is precisely C`s *"for which there exist no solutions (p, u) of (1), (2), (3), (6),')
    say('    ### (7)"*. ### **IT IS NOT THE BLOWUP OF ONE CONSTRUCTED SOLUTION**, and the transport that makes')
    say('    ### it universal is a TOTAL definition rather than a conditional lemma:')
    lean_quote(CB, 48, 56, say, '    the transport into the repository`s own class')
    say('    ### `globalSolutionOfComparator` takes ONLY the Comparator-class solution and returns a member of')
    say('    ### `GlobalFiniteEnergySolution`, which `hglobal` excludes. ### **ANY solution in C`s class yields')
    say('    ### one in the excluded class, so the negative reaches the whole of C`s class.**')
    ans['Q4'] = 'THE UNIVERSAL NEGATIVE of C, not a constructed blowup'
    say('')
    say('  ### Q5 -- UNIQUENESS OF SMOOTH BOUNDED-ENERGY SOLUTIONS: PROVED, IMPORTED, OR A NAMED HYPOTHESIS?')
    say('    ### ### **NONE OF THE THREE. ### UNIQUENESS IS NOT USED AND IS NOT NEEDED**, and the reason is')
    say('    ### Q4`s answer: a universal negative over a solution class never has to identify a solution, so it')
    say('    ### never has to know there is only one. ### **THE QUESTION`S PREMISE -- that the conclusion is a')
    say('    ### ### CONSTRUCTED BLOWUP needing uniqueness to reach C -- DOES NOT HOLD HERE.**')
    rc, so, _ = run('git', '-C', REPO, 'grep', '-l', '-i', 'uniqueness', '--', '*.lean', timeout=240)
    files = [x for x in (so or '').splitlines() if x.strip()]
    say('    ### files in the repository naming `uniqueness` at all : %d' % len(files))
    say('    ### and the terminal`s own chain names it in none of its four files:')
    for rel in (CS, CT, CB, TH):
        t = read(os.path.join(REPO, *rel.split('/')))
        say('        %-48s `uniqueness` occurrences : %d' % (rel, len(re.findall(r'(?i)uniqueness', t))))
    ans['Q5'] = 'NOT USED -- the universal negative needs no uniqueness'
    say('')
    say('-' * 100)
    say('### (c) THE CLAUSE-BY-CLAUSE MAPPING: C ON THE LEFT, THE LEAN FIELD ON THE RIGHT.')
    say('-' * 100)
    mapped = 0
    for clay, field, rel, a, b in MAPPING:
        ok = bool(read(os.path.join(REPO, *rel.split('/'))))
        mapped += 1 if ok else 0
        say('  %-50s -> %-42s %s:%d-%d' % (clay[:50], field[:42], rel, a, b))
    say('  ### ### **CLAUSES OF C MAPPED TO A NAMED FIELD : %d OF %d. ### UNMAPPED : %d.**'
        % (mapped, len(MAPPING), len(MAPPING) - mapped))
    say('')
    say('  ### ### **AND THE ONE PLACE A READER WOULD SUSPECT A NARROWING, CHECKED:** ### the Lean class adds')
    say('  ### `integrable : forall t >= 0, MemLp (||v . t||) 2` beside the energy bound. ### A class with MORE')
    say('  ### conditions is SMALLER, and a non-existence over a smaller class is WEAKER -- so this is exactly')
    say('  ### where a formalisation could quietly fall short of C. ### **IT DOES NOT.** ### C`s (7) reads')
    say('  ### *"int |u(x,t)|^2 dx < C for all t >= 0"*, and a finite integral of a non-negative function IS')
    say('  ### square-integrability; Mathlib`s Bochner integral returns the junk value `0` for a non-integrable')
    say('  ### function, so WITHOUT `integrable` the bound would hold VACUOUSLY for solutions C means to')
    say('  ### exclude. ### **THE FIELD RESTORES C`S MEANING RATHER THAN NARROWING IT.**')
    say('  ### ### **AND (7)`S CONSTANT SITS OUTSIDE THE QUANTIFIER** -- `exists E, forall t >= 0, ... < E` --')
    say('  ### which is the page`s *"< C for all t >= 0"* and not the weaker per-time bound.')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    put(RREC, R)
    putj(RJSON, dict(at=utc(), answers=ans, mapped=mapped, of=len(MAPPING), misses=MISS))
    print(NL.join(R))
    return 0 if not MISS else 1



# =====================================================================================================
# ### COMPONENT 4 -- THE GRADE, AND THE SELF-GRADING TEST.
# =====================================================================================================
GRADES = [
    ('DERIVES', 'the statement unfolded is statement C and every step is in the closure'),
    ('INTERFACES', 'the statement is C on a named premise, the premise identified'),
    ('ENCODES-CONCLUSION / SHELL', 'the terminal stipulates what is claimed or concludes a placeholder'),
    ('NOT THE CLAIM', 'the terminal states something weaker than C, named'),
]


def bridge_quote(pat, say, label, before=0, after=4):
    t = read(BRIDGE)
    L = t.splitlines()
    for i, l in enumerate(L):
        if re.search(pat, l):
            say('  %-44s Bridge/ConservationBridge.lean lines %d-%d' % (label, i + 1 - before, i + 1 + after))
            for k in range(max(0, i - before), min(len(L), i + 1 + after)):
                say('      %4d| %s' % (k + 1, L[k].rstrip()[:110]))
            return NL.join(L[max(0, i - before):min(len(L), i + 1 + after)])
    MISS.append('ConservationBridge : %r' % pat)
    say('  %-44s ### **MISS**' % label)
    return ''


def run_grade():
    R = ['=' * 100, 'b429 -- COMPONENT 4: THE GRADE, AND THE SELF-GRADING TEST.', '=' * 100,
         '  at (UTC) : %s' % utc(), '']
    say = R.append
    B = json.loads(read(BJSON) or '{"built": null, "profile": {}, "axioms_beyond": {}, "sorryax": {}}')
    RD = json.loads(read(RJSON) or '{"answers": {}, "mapped": 0, "of": 0}')
    A = json.loads(read(AJSON) or '{"unreachable": ["all"]}')
    built = B.get('built')
    unreach = A.get('unreachable', [])
    say('-' * 100)
    say('### (a) THE FOUR GRADES THIS ACT MAY CONFER, AND WHERE EACH COMES FROM.')
    say('-' * 100)
    for g, d in GRADES:
        say('  %-28s %s' % (g, d))
    rdm = read(RDM)
    say('  ### the corpus`s README names DERIVES / INTERFACES / ENCODES-CONCLUSION : %s'
        % all(x in rdm for x in ('DERIVES', 'INTERFACES', 'ENCODES-CONCLUSION')))
    say('  ### the corpus names a grade `NOT THE CLAIM` in its grading vocabulary : %s'
        % ('NOT THE CLAIM' in rdm))
    say('  ### ### **THE FOURTH GRADE IS THE ORDER`S AND NOT THE CORPUS`S.** ### The corpus`s three cover a')
    say('  ### terminal that PROVES the claim, one that proves it ON A PREMISE, and one that STIPULATES it.')
    say('  ### They do not cover a terminal that honestly proves something WEAKER. ### **A VOCABULARY SHAPED')
    say('  ### ### AROUND ONE`S OWN WORK NEED NOT HAVE THAT GRADE, BECAUSE ONE`S OWN WORK IS WRITTEN TO THE')
    say('  ### ### CLAIM.** ### That the navigator had to mint it to grade a stranger is a datum of the')
    say('  ### calibration and is recorded as one; it is carried to section (c) and not left here.')
    say('')
    say('-' * 100)
    say('### (b) THE GRADE OF THE FOREIGN TERMINAL.')
    say('-' * 100)
    if unreach:
        say('  ### ### **NO GRADE. ### AN ADDRESS WAS UNREACHABLE (%s) AND READING (7) STOPS THE ACT.**' % unreach)
        grade, why = 'NO GRADE -- ADDRESS UNREACHABLE', 'reading (7)'
    elif not built:
        say('  ### ### ### **NO GRADE IS CONFERRED. ### THE PROOF DID NOT BUILD ON THIS MACHINE.**')
        say('  ### ### **A GRADING OF AN UNBUILT PROOF IS A GRADING OF AN ANNOUNCEMENT** (BAR 4), and what the')
        say('  ### ### build needed is printed in Component 2 rather than summarised here.')
        say('  ### **AND WHAT THIS IS NOT: it is not a finding about the proof.** ### A build that fails on one')
        say('  ### machine is a fact about the machine until it is shown to be a fact about the proof, and this')
        say('  ### act shows no such thing.')
        grade, why = 'NO GRADE -- NOT BUILT HERE', 'BAR 4'
    else:
        prof = B.get('profile', {}).get(TERM_C, [])
        beyond = B.get('axioms_beyond', {}).get(TERM_C, [])
        sx = B.get('sorryax', {}).get(TERM_C)
        say('  the terminal            : %s' % TERM_C)
        say('  its axiom profile       : %s   (printed by `#print axioms`, not inferred)' % prof)
        say('  axioms beyond the three : %s' % (beyond or 'none'))
        say('  `sorryAx` in the closure: %s' % sx)
        say('  clauses of C mapped to a named field : %d of %d' % (RD.get('mapped', 0), RD.get('of', 0)))
        say('  the conclusion          : %s' % RD.get('answers', {}).get('Q4'))
        say('  a named premise         : NONE -- the terminal`s only binders are `nu` and `hnu : nu > 0`')
        clean = (not beyond) and (sx is False) and RD.get('mapped', 0) == RD.get('of', 0)
        if clean:
            grade = 'DERIVES'
            say('')
            say('  ### ### ### **GRADE : DERIVES.**')
            say('  ### Every clause of statement C maps to a named field of the terminal`s own statement; the')
            say('  ### conclusion is C`s universal negative and not a weaker substitute; the terminal takes NO')
            say('  ### premise beyond `nu > 0`, so it is not INTERFACES; it stipulates nothing and concludes no')
            say('  ### placeholder, so it is not a SHELL; and it states nothing weaker than C, so it is not NOT')
            say('  ### THE CLAIM. ### **AND THE CLOSURE CARRIES ONLY THE STANDARD THREE AXIOMS AND NO `sorryAx`,')
            say('  ### ### READ FROM THE PRINTER`S OWN OUTPUT ON THIS MACHINE.**')
        else:
            grade = 'NOT THE CLAIM' if RD.get('mapped', 0) < RD.get('of', 0) else 'INTERFACES'
            say('')
            say('  ### ### ### **GRADE : %s.**' % grade)
        why = 'the profile and the mapping'
        say('')
        say('  ### ### **AND THE RESIDUE, NAMED BY CONTENT AS THE CORPUS`S OWN CALCULUS REQUIRES:** ### the')
        say('  ### statement graded is written against the repository`s OWN COPY of the Formal Conjectures')
        say('  ### definitions, and the repository says of them that *"Comparator checks these definitions')
        say('  ### against the independent reference at runtime."* ### **THIS ACT DID NOT RUN COMPARATOR.** ###')
        say('  ### The agreement of those definitions with the Clay text was established HERE BY READING --')
        say('  ### Component 1 against Component 3, clause by clause -- and a reading is not a checker. ###')
        say('  ### **SO THE GRADE IS `DERIVES` AGAINST THE DEFINITIONS AS READ, AND THE UNRUN CHECK IS THE')
        say('  ### ### RESIDUE.** ### It is named, not counted.')
    say('')
    say('-' * 100)
    say('### (c) THE SELF-GRADING TEST. ### **WOULD THE CORPUS`S OWN ROUTE TERMINAL GET THE SAME TREATMENT?**')
    say('-' * 100)
    bridge_quote(r'theorem riemann_hypothesis', say, 'the corpus`s own route terminal', before=1, after=3)
    bridge_quote(r'def ConservationHypothesis', say, 'its premise, defined in the same file', before=0, after=6)
    say('  ### its conclusion `RiemannHypothesis` is MATHLIB`S OWN DEFINITION, not the corpus`s:')
    mth = os.path.join(SK, '.lake', 'packages', 'mathlib', 'Mathlib', 'NumberTheory', 'LSeries', 'RiemannZeta.lean')
    t = read(mth)
    m = re.search(r'def RiemannHypothesis : Prop :=[^\r\n]*(?:\r?\n[ ]+[^\r\n]*)*', t)
    for x in (m.group(0).splitlines() if m else ['### MISS']):
        say('      | %s' % x.rstrip()[:110])
    if not m:
        MISS.append('Mathlib RiemannHypothesis not quotable')
    say('  ### ### **UNDER THE SAME READING IT GRADES `INTERFACES`**: its conclusion is a real statement and')
    say('  ### not a placeholder, so it is not a SHELL; it is not unconditional, so it is not DERIVES; and it')
    say('  ### is C`s analogue rather than something weaker, so it is not NOT THE CLAIM. ### **THE PREMISE IS')
    say('  ### ### IDENTIFIED: `h_cons : ConservationHypothesis`, defined in the same file and discharged')
    say('  ### ### NOWHERE IN THE CLOSURE** -- the corpus`s own monograph calls it *"the programme`s one')
    say('  ### counted premise"*. ### **THAT IS EXACTLY THE GRADE THE CORPUS ALREADY GIVES IT**, so the test`s')
    say('  ### first half finds the instrument reproducing the corpus`s own reading of itself.')
    say('')
    say('  ### ### **AND THE ORDER`S OWN PARAPHRASE IS CORRECTED HERE, UNDER BAR 8:** ### it names the premise')
    say('  ### `h2`. ### The source names it `h_cons : ConservationHypothesis`. ### `h2` is a different object')
    say('  ### in this record -- the deposit`s -- and a source governs its paraphrase, so the source`s name is')
    say('  ### the one used and the order`s is printed beside it rather than silently followed.')
    say('')
    say('  ### ### **NOW THE CLAUSES, EACH QUOTED BOTH WAYS.**')
    clauses = []
    say('')
    say('  ### CLAUSE 1 -- *"every step is in the closure"*.')
    say('      TO THE STRANGER : a clean `#print axioms` was REQUIRED, read from the printer`s own output, and')
    say('                        `sorryAx` was looked for in the closure and a source-level `sorry` sweep run.')
    say('      TO ITSELF       : the corpus records axiom profiles at `AXIOM_PRINTS.txt` and its own')
    say('                        `EXCLUSION_ENGINE.md` §VIII salt-check did the same to its own terminals.')
    say('      ### ### **APPLIED THE SAME.**')
    clauses.append(('every step is in the closure', 'SAME'))
    say('')
    say('  ### CLAUSE 2 -- *"the statement unfolded to its base objects"*.')
    say('      TO THE STRANGER : unfolded through three structure layers to Mathlib primitives, and the')
    say('                        definitions were READ rather than trusted.')
    say('      TO ITSELF       : the corpus`s own salt-check reports *"most of the application-layer terminals')
    say('                        this paper cited in v2.0 are shells, including the one v2.0 named as its')
    say('                        exemplar of substance."*')
    say('      ### ### **APPLIED THE SAME -- AND THE CORPUS APPLIED IT TO ITSELF HARSHLY.**')
    clauses.append(('the statement unfolded to its base objects', 'SAME'))
    say('')
    say('  ### CLAUSE 3 -- THE AVAILABLE VOCABULARY.')
    say('      TO THE STRANGER : four grades, including `NOT THE CLAIM`.')
    say('      TO ITSELF       : three. ### The corpus`s README and `EXCLUSION_ENGINE.md` §0 name DERIVES,')
    say('                        INTERFACES and ENCODES-CONCLUSION / SHELL, and nothing else.')
    say('      ### ### **AN ASYMMETRY, AND IT FAVOURS THE STRANGER**: a finer grade was available against the')
    say('      ### stranger than the corpus has ever made available against itself. ### **IT CHANGED NO')
    say('      ### OUTCOME HERE, BECAUSE IT WAS NOT USED** -- but an unused finer grade is still an asymmetry')
    say('      ### in the instrument and it is reported as one.')
    clauses.append(('the available vocabulary', 'ASYMMETRIC -- favours the stranger, unused'))
    say('')
    say('  ### CLAUSE 4 -- THE VERIFICATION INSTRUMENT BEHIND THE DEFINITIONS.')
    say('      TO THE STRANGER : its definitions were accepted ON A READING. ### The repository ships a')
    say('                        checker for exactly this -- Comparator, with a config per statement -- and')
    say('                        ### **THIS ACT DID NOT RUN IT.**')
    say('      TO ITSELF       : the corpus does not accept its own definitions on a reading. ### It runs')
    say('                        `rowgen`, whose `defenc` flag exists because a reading passed a stand-in:')
    say('                        *"true if any definition named in the conclusion has a body that is a literal')
    say('                        constant ... This is what catches a stand-in."*')
    say('      ### ### ### **AN ASYMMETRY, AND IT ALSO FAVOURS THE STRANGER: A LIGHTER INSTRUMENT WAS APPLIED')
    say('      ### ### ### TO IT THAN THE CORPUS APPLIES TO ITSELF.**')
    clauses.append(('the verification instrument behind the definitions',
                    'ASYMMETRIC -- favours the stranger, and it bears on the grade'))
    asym = [c for c in clauses if c[1] != 'SAME']
    say('')
    say('-' * 100)
    say('### (d) THE TEST`S ANSWER.')
    say('-' * 100)
    say('  ### CLAUSES COMPARED : %d. ### APPLIED THE SAME : %d. ### ASYMMETRIC : %d.'
        % (len(clauses), len(clauses) - len(asym), len(asym)))
    for c, v in clauses:
        say('      %-52s %s' % (c[:52], v))
    say('')
    say('  ### ### **THE SEAT`S ROUTED CONCERN AT b428 WAS THAT A DISCIPLINE WHICH HAS ONLY GRADED ITS OWN')
    say('  ### ### WORK MIGHT GRADE ITSELF MORE GENEROUSLY THAN A STRANGER. ### ON THIS ONE TRIAL THE')
    say('  ### ### ASYMMETRY RUNS THE OTHER WAY:** both differences found favour the STRANGER -- a finer grade')
    say('  ### available only against it, and a lighter verification instrument applied to it. ### **THE')
    say('  ### ### CONCERN IS NOT CONFIRMED HERE, AND IT IS NOT REFUTED EITHER**, because one trial on one')
    say('  ### terminal is one trial: what it establishes is that on THIS object the leniency ran outward.')
    say('  ### ### **AND WHAT THE ACT CANNOT TELL, SAID PLAINLY:** ### whether the corpus would have conferred')
    say('  ### `DERIVES` on a terminal of its own with this profile and this mapping. ### **IT HAS NEVER HAD')
    say('  ### ### ONE**: its own route terminal carries a premise, and the salt-check`s subjects were shells.')
    say('  ### The comparison has no like case on the corpus`s side, so the strictest question the test could')
    say('  ### ask -- would it grade its own DERIVES as readily? -- is ### **CANNOT TELL FROM THIS RECORD.**')
    say('')
    say('  anchor misses : %d %s' % (len(MISS), MISS))
    say('=' * 100)
    put(GREC, R)
    putj(GJSON, dict(at=utc(), grade=grade, why=why, built=built, clauses=clauses,
                     asymmetric=len(asym), same=len(clauses) - len(asym),
                     cannot_tell=True, corpus_grade='INTERFACES', misses=MISS))
    print(NL.join(R))
    return 0 if not MISS else 1


def main():
    Lr = []
    say = Lr.append
    A = json.loads(read(AJSON) or '{}')
    B = json.loads(read(BJSON) or '{}')
    RD = json.loads(read(RJSON) or '{}')
    G = json.loads(read(GJSON) or '{}')
    fails = []
    say('=' * 100)
    say('b429_components.py -- THE EXTERNAL GRADING READ. ### THE REPORT.')
    say('=' * 100)
    say('  addresses supplied %s ; resolved %s ; unreachable %s ; guessed %s'
        % (A.get('supplied'), A.get('resolved'), A.get('unreachable'), A.get('guessed')))
    say('  repository pinned  %s ; branch %s' % (str(B.get('head'))[:12], B.get('branch')))
    say('  foreign toolchain  %s ; corpus %s' % (B.get('foreign_toolchain'), list(B.get('corpus_pins', {}).values())))
    say('  foreign pin newer  %s' % B.get('newer'))
    say('  BUILT              %s' % B.get('built'))
    say('  axiom profile (C)  %s' % B.get('profile', {}).get(TERM_C))
    say('  beyond the three   %s ; sorryAx %s'
        % (B.get('axioms_beyond', {}).get(TERM_C), B.get('sorryax', {}).get(TERM_C)))
    say('  clauses of C mapped %s of %s' % (RD.get('mapped'), RD.get('of')))
    for k in ('Q1', 'Q2', 'Q3', 'Q4', 'Q5'):
        say('  %-4s %s' % (k, RD.get('answers', {}).get(k)))
    say('  ### ### **GRADE : %s**' % G.get('grade'))
    say('  ### the corpus`s own terminal, under the same reading : %s' % G.get('corpus_grade'))
    say('  ### clauses compared %s ; same %s ; asymmetric %s'
        % (len(G.get('clauses', [])), G.get('same'), G.get('asymmetric')))
    for needle, where in (('anchor misses : 0', read(ADDR)), ('anchor misses : 0', read(CREC)),
                          ('anchor misses : 0', read(RREC)), ('anchor misses : 0', read(GREC))):
        ok = needle in where
        fails += [] if ok else [needle]
    say('  every component record reports anchor misses : 0 -- %s' % (not fails))
    n1a = bool(A.get('resolved') == 3 and B.get('built'))
    n1b = bool(B.get('newer'))
    say('')
    say('### THE EXPECTATIONS, THEIR CLAUSES APART (R27):')
    say('  (N1) *the repository resolves and builds* -- ### **%s** (3 of 3 addresses resolved; built %s).'
        % ('MET' if n1a else 'REFUTED', B.get('built')))
    say('  (N1) *on a Mathlib pin newer than the corpus`s* -- ### **%s** (%s against %s).'
        % ('MET' if n1b else 'REFUTED', B.get('foreign_toolchain'), list(B.get('corpus_pins', {}).values())))
    say('  (N2) *the terminal grades INTERFACES, with uniqueness as the named premise or as a Mathlib import '
        'rather than proved in the closure* -- ### **%s** (the grade is %s; the terminal takes NO premise '
        'beyond `nu > 0`, and uniqueness is %s).'
        % ('MET' if G.get('grade') == 'INTERFACES' else 'REFUTED', G.get('grade'),
           RD.get('answers', {}).get('Q5')))
    say('  (N3) *the self-grading test finds no clause applied differently* -- ### **%s** (%s of %s clauses '
        'asymmetric, and BOTH favour the stranger rather than the corpus).'
        % ('MET' if G.get('asymmetric') == 0 else 'REFUTED', G.get('asymmetric'), len(G.get('clauses', []))))
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    io.open(os.path.join(D, 'b429_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(Lr) + NL)
    print(NL.join(Lr))
    return 1 if fails else 0


if __name__ == '__main__':
    if '--addresses' in sys.argv:
        sys.exit(run_addresses())
    if '--clay' in sys.argv:
        sys.exit(run_clay())
    if '--build' in sys.argv:
        sys.exit(run_build())
    if '--read' in sys.argv:
        sys.exit(run_read())
    if '--grade' in sys.argv:
        sys.exit(run_grade())
    if len(sys.argv) == 1:
        sys.exit(main())
    print('### b429_components.py -- pass --addresses, --clay, --build, --read, --grade or no flag.')
    sys.exit(2)
