# -*- coding: utf-8 -*-
"""tools/b735_ef.py -- (R345)(3): THE explicitFormula BUILD'S DISPATCH ROWS, carried from tools/b733_count.py's routes. No lean process runs on this host; every build is the runner's.

  planmd5               the plan bank's md5 against its blob at de03cb85, printed before any Lean file (N2)
  commit <sha> <group>  a commit row
  push <sha>            a push row, the free read taken now
  dispatch <sha> <n> <group> <target>   gh workflow run, the row carrying the free read before it; the run id read back into the row
  read <n> <run> <artifact dir>   a read row, verdict from the artifact's files
  errors <artifact dir> error blocks from the run's build.log, at most the first 120 lines of each module
  bank <artifact dir> <tip>  data/b735_explicitformula.txt and its row-notes bank: controls first, the dispatches, the modules, the five break points, the field, the E0 re-read, the price in I-10's form, the grade at the end
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
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b735_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402

NL = '\n'
EF = 'D:/SIDE-explicit-formula'
REPO = 'psinary-sketch/SIDE-explicit-formula'
ROWS = os.path.join(D, 'b735_dispatch_rows.json')
PLAN = 'data/b734_explicitformula_plan.txt'
PLAN_MD5 = '5d3868f41eb7aa5be5fa4f7ab57e8df7'


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def cmd_planmd5():
    b = open(os.path.join(RELAY, PLAN), 'rb').read()
    h = hashlib.md5(b).hexdigest()
    blob = subprocess.run(['git', '-C', RELAY, 'show', 'de03cb85:' + PLAN], capture_output=True).stdout
    print('the plan bank %s md5 %s ; wanted %s ; equal %s ; equal its blob at de03cb85 %s' % (PLAN, h, PLAN_MD5, h == PLAN_MD5, hashlib.md5(blob).hexdigest() == h))
    if h != PLAN_MD5:
        sys.exit('### THE PLAN BANK MOVED')


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def cmd_push(sha):
    rows = _rows()
    rows.append(DR.row('push', DR.free(), kernel='SIDE-explicit-formula', branch='zq-b730', sha=sha, remote_equal=git(EF, 'rev-parse', 'origin/zq-b730').strip() == sha, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_commit(sha, item):
    rows = _rows()
    full = git(EF, 'rev-parse', sha).strip()
    rows.append(DR.row('commit', DR.free(), kernel='SIDE-explicit-formula', branch='zq-b730', item=item, sha=full, parent=git(EF, 'rev-parse', full + '^').strip(),
                       files=[x for x in git(EF, 'show', '--format=', '--name-only', full).split(NL) if x]))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_dispatch(sha, n, item, target):
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT DISPATCHED' % read[0])
    if int(n) > K.MAX_DISPATCHES:
        sys.exit('### DISPATCH %s PAST THE ACT`S SIXTEEN -- NOT DISPATCHED' % n)
    r = subprocess.run(['gh', 'workflow', 'run', 'build-module.yml', '--repo', REPO, '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + target], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel='SIDE-explicit-formula', item=item, n=int(n), sha=sha, target=target, at=read[1], error=(r.stderr or '')[:300]))
    else:
        rid = m.group(1) if m else ''
        if not rid:
            time.sleep(6)
            rid = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', REPO, '--workflow', 'build-module.yml', '--limit', '1', '--json', 'databaseId'], capture_output=True, text=True).stdout)[0]['databaseId']
        rows.append(DR.row('dispatch', read, kernel='SIDE-explicit-formula', item=item, n=int(n), workflow='build-module.yml', at_ref='main', sha=sha, target=target, run=int(rid), at=read[1]))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_read(n, run, art):
    v = json.loads(subprocess.run(['gh', 'run', 'view', str(run), '--repo', REPO, '--json', 'status,conclusion,updatedAt'], capture_output=True, text=True, encoding='utf-8').stdout)
    ex = io.open(art + '/build_exit.txt', encoding='utf-8').read().strip()
    log = io.open(art + '/build.log', encoding='utf-8', errors='replace').read()
    ref = io.open(art + '/ref.txt', encoding='utf-8').read().strip().split()[0]
    errs = [l for l in log.split(NL) if l.startswith('error: ') and 'SIDEExplicitFormula' in l]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    ax = [l for l in io.open(art + '/axioms.txt', encoding='utf-8', errors='replace').read().split(NL) if l.strip()]
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', io.open(art + '/mem.log', encoding='utf-8', errors='replace').read())]
    rows = _rows()
    rows.append(DR.row('read', DR.free(), kernel='SIDE-explicit-formula', n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'], built_ref=ref, toolchain=io.open(art + '/ref.txt', encoding='utf-8').read().strip().split()[-1],
                       build_exit=ex, verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs, sorry_warnings=len(warn_sorry), axioms_lines=[l for l in ax if 'ZQ.' in l or 'error' in l][-30:], sorryAx=any('sorryAx' in l for l in ax), runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact='scratchpad run/build-module-%s' % run))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('n', 'run', 'conclusion', 'build_exit', 'verdict', 'sorry_warnings', 'sorryAx', 'runner_low_mb', 'free_mb')}, 'errors', len(errs))


def cmd_errors(art):
    log = io.open(art + '/build.log', encoding='utf-8', errors='replace').read().split(NL)
    out, keep = [], 0
    for l in log:
        if re.search(r'^(error|warning: .*sorry)', l) or ': error' in l:
            keep = 14
        if keep:
            out.append(l)
            keep -= 1
    print(NL.join(out[:400]))
    print('### LOG LINES %d ; ERROR HEADS %d' % (len(log), len([l for l in log if l.startswith('error')])))


FIELD = 'SIDEExplicitFormula.Schema.ZQ.EF.zq_explicitFormula'
PREMISES = 'SIDEExplicitFormula.Schema.ZQ.EF.zq_premises'
STANDARD = 'propext, Classical.choice, Quot.sound'
EZ = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'
MAIN = 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean'
MODULES = tuple('SIDEExplicitFormula/Schema/ZQ/EF/%s.lean' % m for m in ('Xi', 'Landau', 'Heights', 'Contour', 'ZeroSum', 'FullLine', 'Lines', 'Main'))
PLAN_LINES = (140, 170, 340, 400, 185, 295, 400, 200)   # ### the plan's groups A-H, its table at :151-:159
ROUTE_LINES, ROUTE_DISP = (1700, 2800), (6, 16)         # ### the plan's :143
FIVE = (('continuation', 'SIDEExplicitFormula.Schema.ZQ.zq_continuation'), ('zeros', 'SIDEExplicitFormula.Schema.ZQ.zq_zeros'), ('logDeriv', 'SIDEExplicitFormula.Schema.ZQ.zq_logDeriv'),
        ('explicitFormula', FIELD), ('count', 'SIDEExplicitFormula.Schema.ZQ.zq_count_holds'))
E0_EXTENSION = {'ZQZeros': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/EpsteinZQ.lean (Z2)'),
                'ZQPremises': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/EpsteinZQ.lean (the bundle)'),
                'WideConfig': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Wide/Config.lean :28')}   # ### b703's, the shared file not edited
_DATA = (('k', 'ℝ → ℂ', 'the window, data'), ('hk hs he', 'ContDiff ℝ 2 k, HasCompactSupport k, k even', 'class restrictions on k'))
# ### the seat's reading of each premise-free form's binders by hand, BEFORE the E0 check (b703's form): landed name, form, its binders, its hand grade
THREE = (('zq_count', 'zq_count_instance', ()),
         ('zq_explicit_formula', 'zq_explicit_formula_instance', _DATA),
         ('zq_li_nonneg_imp_online', 'zq_li_nonneg_imp_online_instance', ()))
WITNESS = {'zq_count': 'the arm fires on the existential; read by hand: the witness is h.count`s, the bundle`s, no object built here',
           'zq_count_instance': 'the arm fires on the existential; read by hand: the witness is max 1 (2 * A₁), built at Schema/ZQ/Count.lean :340 from the compiled halfQ_count, under Wide.HCount, 1 ≤ A₀ and N Z t (t + 1) ≤ A₀ log(|t| + 3) at every t; a compiled bound, not a fabricated witness'}
BREAKS = ((1, 'the right edge has no room: c = 3/2 exactly, 1 - c = -1/2', ('ZQ.EF.zq_rectangle_identity', 'ZQ.EF.zq_horizontal_vanish', 'ZQ.EF.zq_full_line_identity', 'ZQ.EF.zq_prime_side_line'),
           'the rectangle, the full line and the prime line compiled at c = 3/2 itself, each carrying hc; the plan`s E7 range noted in the rows bank'),
          (2, 'the windows: ZeroConfig`s members do not apply to WideConfig', ('ZQ.EF.zq_good_heights', 'ZQ.EF.wide_zero_sum_summable', 'ZQ.EF.zq_zero_sum_limit'),
           'E6 and E9 compiled over WideConfig on the fresh route'),
          (3, 'the poles: two, with the self-dual reflection', ('ZQ.EF.lamQ_residue_zero', 'ZQ.EF.lamQ_residue_one', 'ZQ.EF.zq_rectangle_identity'),
           'both residues compiled and the rectangle compiled on them'),
          (4, 'the partial fraction`s centre at Re = 2', ('ZQ.EF.zq_logDeriv_partial_fraction',),
           'E5 compiled at group B`s first dispatch'),
          (5, 'multiplicity: Z.mult the order of Lambda_Q; the left edge at -1/2 keeps the trivial zero at -1 outside', ('ZQ.EF.analyticOrderNatAt_lamQ', 'ZQ.EF.zq_rectangle_identity'),
           'the order compiled and the rectangle`s left edge compiled at -1/2'))
ROW_NOTES = (('E2', 'lamQ is defined as zqPair.Λ, and the plan`s product stands as the theorem lamQ_eq_mul (Xi.lean :28), under s ≠ 0 and Gamma s ≠ 0: the product is 0 at s = 0, so it is no definition there. The build continued.'),
             ('E7', 'the plan`s Prop "for 1 < c <= 3/2" is false as written below 3/2: a point of the configuration can lie to the right of such a c. Stated at c = 3/2 alone (hc : c = 3/2), break point (1). The build continued.'),
             ('E8', 'stated with hc as E7.'),
             ('E11', 'stated with hc as E7.'),
             ('E12', 'stated with hc as E7. k even folds H(1 - c - it) onto H(c + it), so E14`s twin on the right line was not needed through vertical_line_shift: conductor_line_shift and Hfn_mirror carry it (with E16).'),
             ('E13', 'stated with hc1 : 3/2 <= c.'),
             ('E15', 'stated as digamma(1/2 + rI) + digamma(1/2 - rI) - 2 log lam = bracketQ r: lam is the plan`s qBase, read as a real.'),
             ('E16', 'as E12 on the fold. Beyond the rows: zq_premises and the three *_instance theorems were added to Main.lean, for (R345)(3)`s re-read; the plan`s fifteen rows do not name them.'),
             ('plan :167', 'the plan says "only then may a later act state ZQPremises and speak of the instance"; (R345)(3) orders the grade in this act and the ruling governs. The plan row stands as written.'))


def grade(last, tip, axioms, sorries):
    """The grade from the last read alone: CLOSED only on a kernel build of the tip, the field's axiom row the standard three, no sorryAx, no `sorry` in the modules."""
    why = []
    if last.get('verdict') != 'KERNEL':
        why.append('verdict %s' % last.get('verdict'))
    if last.get('built_ref') != tip:
        why.append('built ref %s is not the tip' % last.get('built_ref'))
    if last.get('sorryAx') or last.get('sorry_warnings'):
        why.append('a sorry in the build')
    if sorries:
        why.append('%d sorry in the modules' % sorries)
    if axioms.get(FIELD) != STANDARD:
        why.append('the field`s axiom row reads [%s]' % axioms.get(FIELD))
    return ('CLOSED', why) if not why else ('OPEN', why)


def instance_grade(field, axioms, forms):
    """The instance's grade: DERIVES only when the field is CLOSED, the five fields and the bundle stand on the standard three, and every premise-free form reads DERIVES at E0 by hand and by the rule, its salt-check PASS, its profile the standard three."""
    why = []
    if field != 'CLOSED':
        why.append('the field is %s' % field)
    for nm, full in FIVE + (('the bundle', PREMISES),):
        if axioms.get(full) != STANDARD:
            why.append('%s reads [%s]' % (nm, axioms.get(full)))
    if len(forms) != 3:
        why.append('%d forms read of three' % len(forms))
    for f in forms:
        if f['e0'] != 'DERIVES' or f['hand'] != 'DERIVES':
            why.append('%s reads %s by hand, %s at E0' % (f['name'], f['hand'], f['e0']))
        if not f['salt']:
            why.append('%s fails the salt-check' % f['name'])
        if f['prof'] != STANDARD:
            why.append('%s reads [%s]' % (f['name'], f['prof']))
    return ('DERIVES', why) if not why else ('not DERIVES', why)


def show(path, rev):
    return subprocess.run(['git', '-C', EF, 'show', '%s:%s' % (rev, path)], capture_output=True, text=True, encoding='utf-8').stdout


def sig(src, name):
    """b703's _thm_sig, the leading colon kept: a binderless statement's head is then read by e0_rule.conclusion and not as a hypothesis-free fragment."""
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':=' in L[k])
    st = NL.join(L[i:j + 1])
    return i + 1, j + 1, ' '.join(st.split('theorem %s' % name, 1)[1].split(':=', 1)[0].split()), st


def self_eq(concl):
    """b703's _self_eq, carried: a top-level `=` of the conclusion whose two whole sides are one term."""
    s, depth, cut = ' '.join((concl or '').split()), 0, []
    for i, ch in enumerate(s):
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif ch == '=' and depth == 0 and s[i - 1:i] not in ('<', '>', '≠', ':', '=') and s[i + 1:i + 2] not in ('=', '>'):
            cut.append(i)
    return len(cut) == 1 and s[:cut[0]].strip() == s[cut[0] + 1:].strip()


def salt(E, name, head, read, prof, run):
    """REGISTRY.md :544 clause by clause, b703's arms; the witness clause's arm reads an existential and its row then carries the hand reading it needs."""
    concl = E.conclusion(E.statement_only(' ' + head + ' ')) or head
    wit = '∃' not in concl or name in WITNESS
    return concl, [('no True-typed conclusion, no uniformly-True predicate', not re.search(r'\bTrue\b', concl), 'the conclusion %r' % concl.strip()[:90]),
                   ('no X = X', not self_eq(concl), 'no equation of a term with itself in the conclusion (its two whole sides compared)'),
                   ('no hypothesis that is the claim', all(concl.strip() not in (t or '') for _n, t in read) if read else True, 'hypotheses %s' % ([n for n, _t in read] or 'none')),
                   ('no fabricated witness', wit, WITNESS.get(name, 'the conclusion constructs nothing') if '∃' in concl else 'the conclusion constructs nothing'),
                   ('hypotheses named', all(n for n, _t in read) if read else True, ', '.join('%s : %s' % x for x in read) or 'no binder'),
                   ('#print axioms profiled after the first three', prof == STANDARD, 'run %s: [%s]' % (run, prof))]


def read_form(E, src, path, name, hand, run, ax, full):
    i, j, head, st = sig(src, name)
    eg, why, read = E.grade(' ' + head + ' ', 'theorem')
    prof = ax.get(full)
    concl, rows_ = salt(E, name, head, read, prof, run)
    L = ['== %s (%s :%d-:%d):' % (name, path, i, j)] + ['    ' + l for l in st.split(NL)]
    return dict(name=name, e0=eg, why=why, read=read, prof=prof, salt=all(r[1] for r in rows_), hand=hand), L + [
        '  THE GRADE READ FROM THE STATEMENT: %s' % hand,
        '  THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (E0_EXTENSION; the shared file not edited):',
        '    E0 GRADE %s ; its reason: %s ; the hypotheses it read: %s' % (eg, why, read),
        '    THE HAND READING AND THE CHECK %s' % ('AGREE' if eg == hand else '### DIFFER (%s against %s)' % (hand, eg)),
        '  THE SALT-CHECK (REGISTRY.md :544), clause by clause:'] + ['    %-55s %s -- %s' % (c, 'PASS' if o else '### FAIL', h) for c, o, h in rows_] + [
        '  #print axioms: [%s] ; SALT-CHECK %s' % (prof, 'PASS' if all(r[1] for r in rows_) else '### FAIL'), '']


def cmd_bank(art, tip):
    import e0_rule as E
    import pricebank as PB
    E.LEXICON.update(E0_EXTENSION)
    rows = _rows()
    reads = [r for r in rows if r['kind'] == 'read']
    last = reads[-1]
    disp = [r for r in rows if r['kind'] == 'dispatch']
    ax_text = io.open(art + '/axioms.txt', encoding='utf-8', errors='replace').read()
    ax = {k_: ' '.join(v.split()) for k_, v in re.findall(r"'(\S+?)' depends on axioms: \[([^\]]*)\]", ax_text)}
    good = dict(verdict='KERNEL', built_ref=tip, sorryAx=False, sorry_warnings=0)
    ok = {FIELD: STANDARD}
    out = ['b735 -- (R345)(3): THE explicitFormula FIELD, BUILT AND GRADED ON zq-b730 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
           '### every figure read from the dispatch rows, the run`s artifacts and the tree at the tip; no lean process on this host (N1).', '',
           '## THE GRADE`S CONTROLS FIRST']
    for name, want, got in (('a kernel build of the tip, the standard three', 'CLOSED', grade(good, tip, ok, 0)[0]),
                            ('a planted broken build', 'OPEN', grade(dict(good, verdict='BREAKS'), tip, ok, 0)[0]),
                            ('a planted build of another ref', 'OPEN', grade(dict(good, built_ref='0' * 40), tip, ok, 0)[0]),
                            ('a planted sorryAx', 'OPEN', grade(dict(good, sorryAx=True), tip, ok, 0)[0]),
                            ('a planted `sorry` in a module', 'OPEN', grade(good, tip, ok, 1)[0]),
                            ('a planted axiom beyond the three', 'OPEN', grade(good, tip, {FIELD: STANDARD + ', sorryAx'}, 0)[0]),
                            ('no axiom row for the field', 'OPEN', grade(good, tip, {}, 0)[0])):
        if want != got:
            sys.exit('### CONTROL FAILED: %s -- NOTHING WRITTEN' % name)
        out.append('  %-50s %s AS WANTED' % (name, want))
    fa = dict((f, STANDARD) for _n, f in FIVE + (('b', PREMISES),))
    fm = [dict(name=n, e0='DERIVES', hand='DERIVES', salt=True, prof=STANDARD) for n in 'abc']
    for name, want, got in (('all five, three forms DERIVES', 'DERIVES', instance_grade('CLOSED', fa, fm)[0]),
                            ('a planted OPEN field', 'not DERIVES', instance_grade('OPEN', fa, fm)[0]),
                            ('a planted field off the three', 'not DERIVES', instance_grade('CLOSED', dict(fa, **{FIVE[0][1]: STANDARD + ', sorryAx'}), fm)[0]),
                            ('no bundle row', 'not DERIVES', instance_grade('CLOSED', dict((f, STANDARD) for _n, f in FIVE), fm)[0]),
                            ('a planted form at INTERFACES', 'not DERIVES', instance_grade('CLOSED', fa, [dict(fm[0], e0='INTERFACES')] + fm[1:])[0]),
                            ('a planted salt failure', 'not DERIVES', instance_grade('CLOSED', fa, [dict(fm[0], salt=False)] + fm[1:])[0]),
                            ('two forms of three', 'not DERIVES', instance_grade('CLOSED', fa, fm[:2])[0]),
                            ('e0_rule`s own self_test, both polarities', 'True', str(E.self_test()))):
        if want != got:
            sys.exit('### CONTROL FAILED: %s -- NOTHING WRITTEN' % name)
        out.append('  %-50s %s AS WANTED' % (name, want))
    plan_at = git(RELAY, 'log', '-1', '--format=%cI', K.REG_COMMIT).strip()
    first = next(r for r in rows if r['kind'] == 'commit')
    first_at = git(EF, 'log', '-1', '--format=%cI', first['sha']).strip()
    out += ['', '## (N2) THE PLAN BEFORE ANY LEAN, BY ANCESTRY AND TIME',
            '  the plan bank %s at relay %s, committed %s' % (PLAN, K.REG_COMMIT, plan_at),
            '  the first Lean commit of this act %s, parent %s = zq-b730 entering (%s), committed %s' % (first['sha'][:8], first['parent'][:8], first['parent'] == K.ZQ_ENTERING, first_at),
            '  plan before Lean: %s' % (plan_at < first_at), '',
            '## THE DISPATCHES: %d OF AT MOST %d, EACH READ BY ITS RUN ID, EACH ROW CARRYING free_mb' % (len(disp), K.MAX_DISPATCHES)]
    for r in disp:
        rd = next(x for x in reads if x['n'] == r['n'])
        out.append('  %d | group %-9s | %s | sha %s | run %s | free %d MB | %s, exit %s, %d errors, sorry warnings %d, sorryAx %s, read at free %d MB' % (r['n'], r['item'], r['target'].split('.')[-1], r['sha'][:8], r['run'], r['free_mb'], rd['verdict'], rd['build_exit'], len(rd['errors']), rd['sorry_warnings'], rd['sorryAx'], rd['free_mb']))
        for e in rd['errors']:
            out.append('      ' + e)
    repairs = len([r for r in disp if 'repair' in r['item']])
    sor, lines, axdecl = 0, [], 0
    out += ['', '## THE MODULES AT THE TIP %s, zq-b730 ALONE, origin/zq-b730 EQUAL %s' % (tip, git(EF, 'rev-parse', 'origin/zq-b730').strip() == tip)]
    for p, est in zip(MODULES, PLAN_LINES):
        t = show(p, tip)
        body = re.sub(r'/-.*?-/', '', t, flags=re.S)
        n = len(re.findall(r'\bsorry\b', body))
        axdecl += len(re.findall(r'(?m)^axiom\b', body))
        sor += n
        lines.append(len(t.rstrip(NL).split(NL)))
        out.append('  %s : %d lines (the plan`s group row %d), %d `sorry` outside comments, git blob %s' % (p, lines[-1], est, n, git(EF, 'rev-parse', '%s:%s' % (tip, p)).strip()))
    tot = sum(lines)
    on_main = [x for x in git(EF, 'ls-tree', '-r', '--name-only', 'origin/main', 'SIDEExplicitFormula/Schema/ZQ/EF/').split(NL) if x]
    out += ['  `axiom` declarations in the modules: %d ; files of EF/ on main: %d (0 wanted, this act touches no main)' % (axdecl, len(on_main)), '',
            '## THE FIVE BREAK POINTS, EACH WITH ITS RESULT; EACH GROUP`S READ DECIDED ITS NEXT DISPATCH AND THE ROWS ARE BANKED HERE AT THE END']
    stops = 0
    for n, name, decls, why_ in BREAKS:
        held = [ax.get('SIDEExplicitFormula.Schema.' + d) == STANDARD for d in decls]
        stops += 0 if all(held) else 1
        out.append('  (%d) %s' % (n, name))
        out.append('      %s: %s' % ('CONTINUE' if all(held) else 'STOP', why_))
        out.append('      %s' % ' ; '.join('%s [%s]' % (d.split('.')[-1], ax.get('SIDEExplicitFormula.Schema.' + d)) for d in decls))
    src_main, src_ez = show(MAIN, tip), show(EZ, tip)
    n, ln = next((i + 1, l) for i, l in enumerate(src_main.split(NL)) if l.startswith('theorem zq_explicitFormula'))
    g, why = grade(last, tip, ax, sor)
    ez = src_ez.split(NL)

    def block(nm):
        i = next(k for k, l in enumerate(ez) if l.startswith('structure %s ' % nm))
        return ez[i:next(k for k in range(i, len(ez)) if not ez[k].strip())]

    out +=['', '## THE FIELD`S THEOREM, FROM THE BLOB, BESIDE THE FIELD IT MATCHES',
            '  %s :%d  %s' % (MAIN, n, ln), '  its axioms, run %s: [%s]' % (last['run'], ax.get(FIELD))] + ['    ' + l for l in block('ZQExplicitFormula')] + ['    ' + l for l in block('ZQPremises')]
    out += ['', '## THE FIVE FIELDS, EACH ITS AXIOM ROW IN THE ONE RUN %s, AND THE BUNDLE' % last['run']]
    out += ['  %-16s %-46s [%s]' % (f, nm.split('.')[-1], ax.get(nm)) for f, nm in FIVE]
    i, j, _h, st = sig(src_main, 'zq_premises')
    out += ['  %s :%d-:%d  %s' % (MAIN, i, j, ' '.join(st.split())), '    %s' % src_main.split(NL)[j].strip(), '    its axioms: [%s]' % ax.get(PREMISES)]
    out += ['', '## THE RE-READ AT E0: THE THREE THEOREMS AT THEIR LANDED LINES, THE MATCHED POSITIVE CONTROL OF THE SAME READER']
    for nm, _f, _h2 in THREE:
        f, L = read_form(E, src_ez, EZ, nm, 'INTERFACES', last['run'], ax, 'SIDEExplicitFormula.Schema.' + nm)
        if f['e0'] != 'INTERFACES':
            sys.exit('### %s AT ITS LANDED LINE READS %s: THE READER DOES NOT SEE THE BINDER -- NOTHING WRITTEN' % (nm, f['e0']))
        out += L
    out += ['## THE SAME THREE AT THE INSTANCE, THE PREMISE h FILLED BY THE COMPILED zq_premises: EACH A NEW DECLARATION OF Main.lean WHOSE PROOF IS THE LANDED THEOREM APPLIED TO zq_premises']
    forms = []
    for _nm, form, hand in THREE:
        if hand:
            out += ['  the binders of %s, read by hand before the check:' % form] + ['    %-12s : %-44s %s' % b for b in hand]
        f, L = read_form(E, src_main, MAIN, form, 'DERIVES', last['run'], ax, 'SIDEExplicitFormula.Schema.ZQ.EF.' + form)
        forms.append(f)
        out += L
    ig, iwhy = instance_grade(g, ax, forms)
    row = PB.measured('explicitFormula', 'the fresh route, eight modules at zq-b730', tot, [r['run'] for r in disp])
    r_ = PB.ratio(row, ROUTE_LINES, ROUTE_DISP)
    unk = len(re.findall(r'unknownIdentifier', ax_text))
    unk2 = len(re.findall(r'Unknown constant', ax_text))
    out += ['## THE PRICE AND THE MEASURED FIGURE, %s' % PB.FORM,
            '  the seat`s estimate carried: 2130 lines on the fresh route, its range %d-%d, %d-%d dispatches (%s :143).' % (ROUTE_LINES + ROUTE_DISP + (PLAN,)),
            '  the measured: %d lines in eight modules, %d dispatches, %d of them repairs ; %.3f of the 2130 ; against the range %.3f-%.3f in lines, %.3f-%.3f in dispatches.' % (tot, row['dispatches'], repairs, tot / 2130.0, r_[0], r_[1], r_[2], r_[3]),
            '  by group, measured against the plan: %s.' % ', '.join('%s %d/%d' % (c, a, b) for c, a, b in zip('ABCDEFGH', lines, PLAN_LINES)),
            '  one route`s figure; no bound on another and no estimate of the next field.', '',
            '## WHAT THE ARTEFACT REFUSES, NOT A FAILURE OF THE BUILD: the workflow carries a fixed print list; `unknownIdentifier` rows %d, `Unknown constant` rows %d, names lying outside the target`s imports. build_exit governs and is %s.' % (unk, unk2, last['build_exit']), '',
            '## WHAT THE GRADE SAYS AND WHAT IT DOES NOT',
            '  THE LANDED LINES ARE UNCHANGED AND STILL READ INTERFACES. zq_count :153, zq_explicit_formula :157 and zq_li_nonneg_imp_online :164 are general over zq, Z, c and bind h : ZQPremises zq Z c; EpsteinZQ.lean is imported by the modules that',
            '  discharge the bundle, so no restatement at those lines can name the instance. W-ORD-ZQ-DERIVES`s words (data/b730_ferry.txt :13) read "the instance`s theorems (... :153 ... :157 ... :164) binding no named premise": the seat reads "the instance`s theorems" as those',
            '  three applied to the compiled zq_premises, the three forms above, three declarations beyond the plan`s rows. That reading is the seat`s, put to the author; the grade below stands on it and on nothing stronger.',
            '  THE LANDED ROWS` "no hypothesis that is the claim" PASS IS VACUOUS: the arm compares text, while the proofs at those lines are projections of the bundle (h.count, h.explicitFormula.ef), the claim inside h. It tests nothing there; the substance is zq_premises, whose fields are the five compiled theorems.',
            '  zq_li_nonneg_imp_online_instance is an implication. Its antecedent, the Li nonnegativity of the configuration, is not proved here, and nothing here locates any zero or says anything of RH or GRH. data/b703_epstein_grade.txt :183-:184 names Davenport-Heilbronn for Z_Q, the reason that antecedent is not to be expected.',
            '  DERIVES is a reading of a statement`s binders; it confers no deposit, no tag and no line on any main.', '',
            '## THE GRADE, AT ITS END',
            '  THE FIELD: %s%s' % (g, ' : ' + ' ; '.join(why) if why else ''),
            '  THE FIVE BREAK POINTS: %d STOP' % stops,
            '  THE INSTANCE: %s%s' % (ig, ' : ' + ' ; '.join(iwhy) if iwhy else ', read on the three forms; the landed lines INTERFACES as above'), '']
    if g == 'CLOSED':
        out.append('### ### **THE explicitFormula FIELD CLOSED: zq_explicitFormula, RUN %s, TIP %s, BUILD EXIT %s, NO sorryAx, AXIOMS %s ; %d OF %d DISPATCHES, %d REPAIRS ; %d LINES AGAINST 2,130 ; FIVE OF FIVE FIELDS ; THE INSTANCE %s ON THE THREE PREMISE-FREE FORMS, THE LANDED LINES INTERFACES.**' % (last['run'], tip[:8], last['build_exit'], STANDARD, len(disp), K.MAX_DISPATCHES, repairs, tot, ig))
    t = NL.join(out) + NL
    io.open(os.path.join(D, 'b735_explicitformula.txt'), 'w', encoding='utf-8', newline='\n').write(t)
    rn = ['b735 -- (R345)(3): THE ROWS THE BUILD FOUND WRONG OR READ OTHERWISE, EACH BESIDE ITS ROW; NO ROW OF %s REWRITTEN' % PLAN, '']
    rn += ['  %-10s %s' % x for x in ROW_NOTES]
    rn += ['', '### ### **%d NOTES ; THE PLAN BANK UNMOVED, md5 %s ; NO NOTE STOPPED THE BUILD.**' % (len(ROW_NOTES), hashlib.md5(open(os.path.join(RELAY, PLAN), 'rb').read()).hexdigest())]
    io.open(os.path.join(D, 'b735_explicitformula_rows.txt'), 'w', encoding='utf-8', newline='\n').write(NL.join(rn) + NL)
    print(t)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == 'planmd5':
        cmd_planmd5()
    elif a[0] == 'bank':
        cmd_bank(a[1], a[2])
    elif a[0] == 'commit':
        cmd_commit(a[1], a[2])
    elif a[0] == 'push':
        cmd_push(a[1])
    elif a[0] == 'dispatch':
        cmd_dispatch(a[1], a[2], a[3], a[4])
    elif a[0] == 'read':
        cmd_read(a[1], a[2], a[3])
    elif a[0] == 'errors':
        cmd_errors(a[1])
    else:
        sys.exit(__doc__)
