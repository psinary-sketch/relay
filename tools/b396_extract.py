# -*- coding: utf-8 -*-
"""b396_extract.py -- THE EXTRACT AND THE SURVEYS FOR THE BACKTICK SWEEP.

### ### **THE ORDER'S FIRST INSTRUCTION IS THAT THE SWEEP'S OWN PREMISE BE TESTED**, and the
### fixture in `b396_narrow.py` is run HERE, before a single instrument is read, with its result
### printed. ### **A SWEEP FOR NARROW MATCHERS THAT IS ITSELF NARROW WOULD BE THE SPECIES INSIDE
### ### THE ACT THAT MEASURES IT, FOR THE THIRD TIME IN FOUR ACTS.**
###
### ### **NARROW IS NOT A DEFECT. ### NARROW UNDER A NEGATIVE FINDING IS A RISK.** ### The
### product is a list of ### **FINDINGS AT RISK**, not a count of regexes, and the two signals
### that make a finding negative are ### **REPORTED APART AND NEVER SUMMED.**
###
### ### **NOTHING IS EDITED BY THIS FILE. ### NOTHING IS WRITTEN AT ZENODO.**
"""
import ast
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402
import b396_narrow as NAR       # noqa: E402
import b396_figures as FG      # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FERRY = os.path.join(D, 'b396_ferry_2026-09-10.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


SKIP = ('.git', 'archive', 'outputs')


# ==================================================================================================
#  SURVEY 0 -- THE ORDER'S FIRST INSTRUCTION. ### **THE SWEEP'S OWN PREMISE.**
# ==================================================================================================
def survey0():
    bar('-')
    rec('  ### SURVEY 0 -- **THE SWEEP\'S OWN PREMISE, TESTED BEFORE ANY INSTRUMENT IS READ.**')
    bar('-')
    # ### **THE NEEDLE IS ONE LINE OF THE FERRY AS THE FERRY WRAPS IT.** ### A hint beginning
    # ### `this ` spans the break and matches nothing -- the record's oldest instrument defect,
    # ### banked across six acts, and it is cheaper to read the line than to retype it.
    ai, aln = AF.find(FERRY, "sweep's own predicate must be shown capable of finding a")
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    (f1, f2, f3), wide_clean, byline = NAR.fixture()
    rec('  ### **ONE NARROW MATCHER, WRITTEN THREE WAYS:**')
    rec('    form 1  a raw-string regex, backtick-delimited            FOUND : %s' % f1)
    rec('    form 2  a double-quoted escaped regex                     FOUND : %s' % f2)
    rec('    form 3  ### **NO REGEX AT ALL** -- startswith + `in` + islower()  FOUND : %s' % f3)
    rec('  ### ### **ALL THREE FOUND : %s.**' % (f1 and f2 and f3))
    rec('  ### ### **AND THE WIDE FIXTURE IS CLEAN : %s** ### -- without a negative control the'
        % wide_clean)
    rec('  ### ### fixture would prove the detector FIRES, not that it DISCRIMINATES.')
    for ln in sorted(byline):
        for ctx, s, why in byline[ln]:
            rec('      line %-3d %-11s %-44s %s' % (ln, ctx, repr(s)[:44], ','.join(why)))
    rec()
    rec('  ### **AND A RAW `grep` IS NOT THE INSTRUMENT:**')
    allt = sorted(x for x in os.listdir(T) if x.startswith('b') and x.endswith('.py'))
    raw = [x for x in allt if '`' in text_of(os.path.join(T, x))]
    rec('  ###   `tools/b*.py`                          : ### **`%d`**' % len(allt))
    rec('  ###   carrying a backtick ANYWHERE           : ### **`%d`**' % len(raw))
    rec('  ### ### **ALMOST EVERY ONE OF THOSE IS PROSE.** ### **A BACKTICK IN A SENTENCE IS NOT')
    rec('  ### ### A BACKTICK IN A MATCHER**, and the difference is the whole survey.')
    rec()
    rec('  ### **WHAT THIS SWEEP IS DEAF TO, STATED BEFORE ITS RESULT:**')
    for d in NAR.DEAF:
        rec('    -- %s' % flat(d, 150))
    return dict(forms=[f1, f2, f3], all_three=(f1 and f2 and f3), wide_clean=wide_clean,
                tools=len(allt), raw_backtick=len(raw), deaf=len(NAR.DEAF))


# ==================================================================================================
#  SURVEY 1 -- THE SWEEP. ### **FINDINGS AT RISK, NOT A COUNT OF REGEXES.**
# ==================================================================================================
NEGWORDS = re.compile(r'(?i)\b(none|no |not |absent|missing|unreachable|nothing|never|'
                      r'zero|empty|carries none|found : 0)\b')


def emptiness_sites(tree, targets):
    """### **THE PRECISE SIGNAL:** ### is the matcher's own yield tested for emptiness?"""
    hits = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.Not):
            for x in ast.walk(n.operand):
                if isinstance(x, ast.Name) and x.id in targets:
                    hits.add(x.id)
        if isinstance(n, ast.Compare):
            parts = [n.left] + list(n.comparators)
            names = [p.id for p in parts if isinstance(p, ast.Name) and p.id in targets]
            lens = [p for p in parts if isinstance(p, ast.Call)
                    and getattr(p.func, 'id', None) == 'len'
                    and p.args and isinstance(p.args[0], ast.Name) and p.args[0].id in targets]
            zeros = [p for p in parts if isinstance(p, ast.Constant) and p.value in (0, [], '')]
            empt = [p for p in parts if isinstance(p, (ast.List, ast.Tuple)) and not p.elts]
            if (zeros or empt) and (names or lens):
                for p in parts:
                    if isinstance(p, ast.Name) and p.id in targets:
                        hits.add(p.id)
                for p in lens:
                    hits.add(p.args[0].id)
    return hits


def matcher_targets(tree):
    """### The names a narrow-capable matcher call is assigned to."""
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            calls = [c for c in ast.walk(n.value) if isinstance(c, ast.Call)]
            f = [getattr(c.func, 'attr', None) or getattr(c.func, 'id', None) for c in calls]
            if any(x in NAR.RE_FUNCS or x in NAR.STR_TESTS for x in f):
                for tg in n.targets:
                    if isinstance(tg, ast.Name):
                        out[tg.id] = getattr(n, 'lineno', 0)
    return out


def printed_negatives(tree):
    """### **THE CO-SIGNAL, REPORTED APART:** ### does the module PRINT an absence?"""
    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and (getattr(n.func, 'id', None) in ('print', 'rec')):
            for a in ast.walk(n):
                if isinstance(a, ast.Constant) and isinstance(a.value, str):
                    if NEGWORDS.search(a.value):
                        out.append(flat(a.value, 70))
    return out


def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- THE SWEEP. ### **THE PRODUCT IS FINDINGS AT RISK.**')
    bar('-')
    allt = sorted(x for x in os.listdir(T) if re.match(r'^b\d+_.*\.py$', x))
    narrow, broke, figs = [], [], []
    for f in allt:
        src = text_of(os.path.join(T, f))
        try:
            hits, case_hits = NAR.scan_source(src)
        except SyntaxError as ex:
            broke.append((f, str(ex)[:60]))
            continue
        if hits or case_hits:
            narrow.append(f)
        try:
            g = FG.figures(src)
        except SyntaxError:
            g = []
        for o in g:
            figs.append(dict(o, file=f, act=re.match(r'^(b\d+)_', f).group(1)))
    rec('  ### **THE FUNNEL, AND EVERY STAGE PRINTED:**')
    rec('  ###   `tools/b*.py` parsed                          ### **`%d`** (unparseable `%d`)'
        % (len(allt), len(broke)))
    rec('  ###   carrying at least one NARROW TEST             ### **`%d`**' % len(narrow))
    rec('  ###   ### **CARRYING AT LEAST ONE AT-RISK FIGURE**  ### **`%d`**'
        % len(set(x['file'] for x in figs)))
    rec('  ###   ### **AT-RISK FIGURES**                       ### **`%d`**' % len(figs))
    rec()
    rec('  ### ### **AND TWO FILTERS THIS ACT TRIED AND THREW OUT BEFORE THE LOCK, BECAUSE A')
    rec('  ### ### FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER:**')
    rec('  ###   ### **(i) `the module prints an absence somewhere`** ### kept `374` of `407`.')
    rec('  ###   ### **(ii) `the act`s name appears in a ledger`** ### kept `350` of `380`.')
    rec('  ###   ### **(iii) `the instrument reads corpus text rather than its own artifacts`**')
    rec('  ###        ### kept `79` of `82`. ### The distinction is REAL -- a narrow matcher')
    rec('  ###        against text the act WROTE fails its own gate loudly, while one against the')
    rec('  ###        CORPUS shrinks a finding in silence, which is `b394`s species -- but ###')
    rec('  ###        **IT IS NOT SEPARABLE AT MODULE GRANULARITY**, because nearly every')
    rec('  ###        instrument names a corpus path somewhere. ### **A TRUE DISTINCTION THAT A')
    rec('  ###        ### TOOL CANNOT DRAW IS NOT A FILTER**, and it is filed as a limit rather')
    rec('  ###        than applied as one.')
    rec('  ### ### **ANY OF THE THREE WOULD HAVE PRODUCED A COUNT OF REGEXES DRESSED AS A LIST')
    rec('  ### ### OF FINDINGS**, which is the one thing the order said the product must not be.')
    rec('  ### ### They are reported here as discarded, with their yields, because ### **A')
    rec('  ### ### TIGHTENING MADE IN SILENCE IS ONE NOBODY CAN AUDIT** (`b381`).')
    rec('  ### ### ### **AND THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT:** ### the')
    rec('  ### ### ### narrow shape is ### **PERVASIVE**, so the order`s question -- how many')
    rec('  ### ### ### findings rest on a backtick -- ### **HAS NO ANSWER AT INSTRUMENT')
    rec('  ### ### ### GRANULARITY.** ### It has one at FIGURE granularity, and that is the')
    rec('  ### ### ### list below.')
    rec()
    rec('  ### **WHAT MAKES A FIGURE AT RISK, STATED BEFORE THE LIST:** ### a narrow literal whose')
    rec('  ### yield is bound to a name, and a report naming that same name whose OWN LITERAL')
    rec('  ### carries an absence -- a zero, a `none`, or a phrase saying the thing was not found.')
    rec('  ### ### **THE ABSENCE AND THE MEASUREMENT MUST SIT IN THE SAME LITERAL**, or it is')
    rec('  ### ### prose that happens to contain the word `no`.')
    a, b, c = FG.fixture()
    rec('  ### **AND THIS FILTER IS TESTED TOO, ON BOTH AXES:** ### narrow+absence FIRES `%s` ;'
        % a)
    rec('  ### narrow+ordinary QUIET `%s` ; wide+absence QUIET `%s`.' % (b, c))
    for f, ex in broke[:5]:
        rec('      ### **NOT PARSED AND SAID SO** : %s -- %s' % (f, ex))
    return dict(parsed=len(allt), broke=broke, narrow=len(narrow),
                atrisk_files=len(set(x['file'] for x in figs)), figures=len(figs),
                rows=figs, filter_fixture=[a, b, c])


# ==================================================================================================
#  SURVEY 2 -- EXPOSURE. ### **WHAT RESTS ON THE FINDING, NOT WHAT IT COST.**
# ==================================================================================================
def survey2(s1):
    bar('-')
    rec('  ### SURVEY 2 -- EXPOSURE. ### **WHAT RESTS ON THE FIGURE, NOT WHAT IT COST.**')
    bar('-')
    ai, aln = AF.find(FERRY, 'before the three cheapest are re-run, rank the at-risk findings')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    REGISTRY = text_of(os.path.join(PP, 'REGISTRY.md'))
    TAX = text_of(os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md'))
    FINDINGS = text_of(os.path.join(PP, 'FINDINGS.md'))
    CORR = text_of(os.path.join(SIDE, 'CORRESPONDENCE.md'))
    MAPT = text_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    LEDGERS = {'REGISTRY.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'ERRATA.md',
               'HANDOFF.md', 'AGENTS.md', 'README.md'}
    keystone_text = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in fn:
            if f.endswith('.md') and f not in LEDGERS:
                keystone_text.append((rel + '/' + f if rel != '.' else f,
                                      text_of(os.path.join(dp, f))))
    rec('  ### ### **EXPOSURE IS COUNTED OUTSIDE THE ACT`S OWN ARTIFACTS**, which is the order`s')
    rec('  ### ### own distinction -- ### *more exposed than one that sits in its own bank.* ### An')
    rec('  ### ### earlier form of this survey counted the act`s name ANYWHERE and kept `350` of')
    rec('  ### ### `380`: ### **EVERY ACT NAMES ITSELF IN ITS OWN ROW, SO THAT MEASURED NOTHING.**')
    rec('  ### ### A correspondence row whose own marker names the act is that act`s own bank and')
    rec('  ### ### is excluded here.')
    rec()
    rec('  ### **THE FOUR CLASSES, COUNTED SEPARATELY AND NEVER ADDED:**')
    rec('  ###   RULING   -- `REGISTRY.md` or the class taxonomy')
    rec('  ###   KEYSTONE -- a corpus document that is not a ledger  (`%d` scanned)'
        % len(keystone_text))
    rec('  ###   FOLD     -- `FINDINGS.md`')
    rec('  ###   ROW      -- a `CORRESPONDENCE.md` row that is NOT the act`s own, or `SPIRAL_MAP.md`')
    rec()
    corr_lines = CORR.split(chr(10))
    byact = {}
    for x in s1['rows']:
        byact.setdefault(x['act'], []).append(x)
    out = []
    for a in sorted(byact):
        pat = re.compile(r'\b%s\b' % a)
        ruling = len(pat.findall(REGISTRY)) + len(pat.findall(TAX))
        fold = len(pat.findall(FINDINGS))
        rows_other = sum(1 for ln in corr_lines
                         if pat.search(ln) and ('(%s,' % a) not in ln[:500]
                         and ('(%s ' % a) not in ln[:500])
        row = rows_other + len(pat.findall(MAPT))
        ks = [p for p, tx in keystone_text if pat.search(tx)]
        out.append(dict(act=a, figures=len(byact[a]),
                        files=sorted(set(z['file'] for z in byact[a])),
                        ruling=ruling, fold=fold, row=row, keystone=len(ks),
                        keystone_docs=ks[:3],
                        sample=byact[a][0]['report'][:110],
                        why=sorted(set(w for z in byact[a] for w in z['why']))))
    rec('  ### ### **THE ORDERING RULE, STATED BEFORE THE RANKING:** ### a ruling outranks a')
    rec('  ### ### keystone, a keystone outranks a fold, a fold outranks a row, and ties break on')
    rec('  ### ### the figure count. ### **THE FOUR COUNTS ARE PRINTED APART SO A READER CAN RANK')
    rec('  ### ### THEM DIFFERENTLY.**')
    out.sort(key=lambda z: (-z['ruling'], -z['keystone'], -z['fold'], -z['row'], -z['figures']))
    rec()
    rec('    %-7s %-5s %-7s %-9s %-6s %-5s %s'
        % ('act', 'figs', 'RULING', 'KEYSTONE', 'FOLD', 'ROW', 'narrowness'))
    for z in out:
        rec('    %-7s %-5d %-7d %-9d %-6d %-5d %s'
            % (z['act'], z['figures'], z['ruling'], z['keystone'], z['fold'], z['row'],
               ','.join(z['why'])[:44]))
    exposed = [z for z in out if (z['ruling'] or z['keystone'] or z['fold'])]
    rec('  ### ### **ACTS CARRYING AN AT-RISK FIGURE : `%d`.**' % len(out))
    rec('  ### ### **OF THOSE, EXPOSED BEYOND THEIR OWN BANK : `%d`.**' % len(exposed))
    rec('  ### ### **AND `%d` SIT IN THEIR OWN BANK AND NOWHERE ELSE** -- ### **STILL AT RISK,'
        % (len(out) - len(exposed)))
    rec('  ### ### AND CHEAPER TO BE WRONG.**')
    return out


# ==================================================================================================
#  SURVEY 3 -- COST. ### **WHAT A RE-DERIVATION WOULD TAKE.**
# ==================================================================================================
def survey3(ranked):
    bar('-')
    rec('  ### SURVEY 3 -- COST. ### **CHEAP MEANS RE-DERIVABLE BY A TEXT SCAN THIS DRIVE CAN RUN.**')
    bar('-')
    rec('  ### **THE COST MEASURE, STATED BEFORE IT IS APPLIED:** ### the number of narrow')
    rec('  ### literals that must be widened, plus `1` for each input the drive cannot read')
    rec('  ### without a build or a network call. ### **A FINDING WHOSE INPUTS ARE LOCAL `.md`')
    rec('  ### ### FILES AND WHOSE MATCHER IS ONE LITERAL IS THE CHEAPEST THING IN THE RECORD.**')
    out = []
    for z in ranked:
        src = text_of(os.path.join(T, z['files'][0]))
        needs_net = any(k in src for k in ('urllib', 'requests', 'ls-remote', 'curl'))
        needs_build = any(k in src for k in ('lake ', 'LEAN_PATH', '.olean'))
        cost = z['figures'] + (3 if needs_net else 0) + (5 if needs_build else 0)
        out.append(dict(z, cost=cost, needs_net=needs_net, needs_build=needs_build))
    cheap = sorted(out, key=lambda z: (z['cost'], z['act']))
    rec()
    rec('    %-8s %-6s %-7s %-7s %s' % ('act', 'cost', 'net?', 'build?', 'instrument'))
    for z in cheap[:12]:
        rec('    %-8s %-6d %-7s %-7s %s'
            % (z['act'], z['cost'], z['needs_net'], z['needs_build'], z['files'][0][:34]))
    return out, cheap


# ==================================================================================================
#  SURVEY 4 -- THE PRESERVATION HAZARD. ### **ARE PRESERVED BLOCKS STRUCTURALLY IDENTIFIABLE?**
# ==================================================================================================
PRESERVE_MARKS = [
    ('a blockquote line', re.compile(r'^\s*>')),
    ('a PRESERVED/SUPERSEDED banner', re.compile(r'(?i)preserved here verbatim|superseded .{0,40}'
                                                 r'preserved|preserved,? not removed|'
                                                 r'quoted, not removed')),
    ('an HTML comment naming a preservation', re.compile(r'(?i)<!--[^>]*(preserv|superseded|'
                                                         r'annotation)[^>]*-->')),
]


def survey4():
    bar('-')
    rec('  ### SURVEY 4 -- THE PRESERVATION HAZARD. ### **`b395`\'S NEAR MISS, MEASURED.**')
    bar('-')
    ai, aln = AF.find(FERRY, 'needle matched a preserved quotation and resolved to it')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    files, blocks, quoted_lines, total = 0, 0, 0, 0
    banners = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in sorted(fn):
            if not f.endswith('.md'):
                continue
            p = (rel + '/' + f if rel != '.' else f)
            lines = text_of(os.path.join(dp, f)).split(chr(10))
            total += len(lines)
            q = [i for i, ln in enumerate(lines, 1) if PRESERVE_MARKS[0][1].match(ln)]
            if q:
                files += 1
                quoted_lines += len(q)
                runs = 1 + sum(1 for a, b in zip(q, q[1:]) if b != a + 1)
                blocks += runs
            for nm, pat in PRESERVE_MARKS[1:]:
                for i, ln in enumerate(lines, 1):
                    if pat.search(ln):
                        banners.append((p, i, nm, flat(ln, 90)))
    rec('  ### **BLOCKQUOTED (`>`-PREFIXED) TEXT IN THE PAPER TREE:**')
    rec('  ###   documents carrying at least one            ### **`%d`**' % files)
    rec('  ###   contiguous blocks                          ### **`%d`**' % blocks)
    rec('  ###   lines                                      ### **`%d`** of `%d` total'
        % (quoted_lines, total))
    rec('  ### **BANNERS NAMING A PRESERVATION EXPLICITLY : `%d`.**' % len(banners))
    for p, i, nm, ln in banners[:6]:
        rec('      %s:%d  (%s)' % (p, i, nm))
        rec('      > %s' % ln)
    # ### **THE VERDICT THE ORDER ASKS FOR: MECHANIZABLE OR JUDGEMENT.**
    mech = quoted_lines > 0 and blocks > 0
    rec()
    rec('  ### ### **ARE PRESERVED BLOCKS STRUCTURALLY IDENTIFIABLE : %s.**' % mech)
    rec('  ### ### **A `>`-PREFIXED LINE IS A STRUCTURAL FACT A TOOL CAN READ WITHOUT JUDGEMENT**,')
    rec('  ### ### and it is the form `b388` used to preserve the superseded cluster table -- the')
    rec('  ### ### exact block `b395`\'s needle resolved into.')
    rec('  ### ### **BUT IT IS A SUFFICIENT CONDITION AND NOT A NECESSARY ONE:** ### not every')
    rec('  ### ### preserved passage is blockquoted, and ### **A RULE MECHANIZED ON `>` ALONE')
    rec('  ### ### WOULD MISS A PRESERVATION WRITTEN ANY OTHER WAY** -- which is this act\'s own')
    rec('  ### ### subject turned on its own remedy. ### **SO THE MECHANIZED HALF AND THE')
    rec('  ### ### JUDGEMENT HALF ARE LISTED APART AND THE SECOND IS NOT CLAIMED AS THE FIRST.**')
    return dict(files=files, blocks=blocks, lines=quoted_lines, total=total,
                banners=len(banners), banner_sample=banners[:6], mechanizable=mech)


# ==================================================================================================
#  SURVEY 5 -- THE PRICE INPUTS. ### **b394'S OWN MEASURED RATE, READ AND NOT RECALLED.**
# ==================================================================================================
def survey5():
    bar('-')
    rec('  ### SURVEY 5 -- THE PRICE INPUTS, READ FROM THE ACTS THAT MEASURED THEM.')
    bar('-')
    c394 = json.load(io.open(os.path.join(D, 'b394_components.json'), encoding='utf-8'))
    c395 = json.load(io.open(os.path.join(D, 'b395_components.json'), encoding='utf-8'))
    C3 = c394['c3']
    rec('  ### **`b394`\'S OWN FIGURES, FROM ITS OWN COMPONENT JSON:**')
    rec('  ###   minutes for three keystones      ### **`%s`**' % C3['minutes'])
    rec('  ###   per keystone                     ### **`%s`**' % C3['per_keystone'])
    rec('  ###   `b390`\'s figure for one          ### **`%s`**' % C3['b390_minutes'])
    rec('  ###   reconciled after `b394`          ### **`%s` of `%s`**'
        % (C3['reconciled'], C3['of']))
    rec('  ### **`b395`\'S FIGURE FOR WHAT IS NOW REACHABLE:** ### **`%d` OF THE ELEVEN.**'
        % c395['c1']['readable'])
    rec('  ### ### **BOTH OF `b394`\'S FIGURES WERE DECLARED FLOORS BY THE ACT THAT TOOK THEM**,')
    rec('  ### ### and a price built on a floor is a floor. ### **THIS ACT DOES NOT PROMOTE ONE')
    rec('  ### ### INTO AN ESTIMATE.**')
    return dict(minutes=C3['minutes'], per_keystone=C3['per_keystone'],
                b390=C3['b390_minutes'], reconciled=C3['reconciled'], of=C3['of'],
                readable=c395['c1']['readable'])


def do_reads(ranked, cheap):
    bar('-')
    rec('  ### THE READS. ### **EVERY QUOTED LINE CARRIES AN ANCHOR FOUND BY THE TOOL.**')
    bar('-')
    reads, without, amb = [], 0, 0
    todo = [(FERRY, 'ADDITION ONE'), (FERRY, 'ADDITION TWO'), (FERRY, 'ADDITION THREE'),
            (FERRY, 'COMPONENT 1 — THE SWEEP'), (FERRY, 'COMPONENT 2 — RE-RUN'),
            (FERRY, 'COMPONENT 3 — THE WORK NOW AVAILABLE')]
    # ### **THE NEEDLE IS THE AT-RISK REPORT ITSELF**, not `def `. ### A needle of `def ` matched
    # ### every function in the file and came back AMBIGUOUS six times out of six -- an anchor
    # ### that matches everything anchors nothing, which is the tool's own stated limit.
    seen = []
    for z in (ranked[:3] + cheap[:3]):
        if z['act'] in seen:
            continue
        seen.append(z['act'])
        todo.append((os.path.join(T, z['files'][0]), z['sample'][:60]))
    for p, want in todo:
        try:
            i, ln = AF.find(p, want)
            v = 'ANCHORED'
        except Exception as e:
            i, ln = 0, ''
            v = 'AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT'
            if v == 'AMBIGUOUS':
                amb += 1
            else:
                without += 1
        reads.append(dict(path=os.path.basename(p), needle=flat(want, 46), line=i, verdict=v))
        rec('    %-30s %-46s %-10s line %s'
            % (os.path.basename(p)[:30], flat(want, 46), v, i or '--'))
    rec('  ### **reads %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d**'
        % (len(reads), len(reads) - amb - without, amb, without))
    return reads, without, amb


def refs():
    out = {}
    for name, repo in b303_pins.REPOS:
        b = subprocess.run(['git', '-C', repo, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        h = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        out[name] = dict(branch=(b.stdout or '').strip(), head=(h.stdout or '').strip()[:12])
    return out


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b396 -- THE EXTRACT, AND THE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s0 = survey0()
    rec()
    s1 = survey1()
    rec()
    ranked = survey2(s1)
    rec()
    costed, cheap = survey3(ranked)
    rec()
    s4 = survey4()
    rec()
    s5 = survey5()
    rec()
    reads, without, amb = do_reads(ranked, cheap)
    rec()
    bar('=')
    rec('  0 : forms %s ; wide clean %s ; tools %d ; raw-backtick %d ; deaf %d'
        % (s0['forms'], s0['wide_clean'], s0['tools'], s0['raw_backtick'], s0['deaf']))
    rec('  1 : parsed %d ; narrow %d ; at-risk instruments %d ; AT-RISK FIGURES %d'
        % (s1['parsed'], s1['narrow'], s1['atrisk_files'], s1['figures']))
    rec('  2 : acts %d ; top exposure %s'
        % (len(ranked), [z['act'] for z in ranked[:3]]))
    rec('  3 : cheapest %s' % [z['act'] for z in cheap[:3]])
    rec('  4 : quoted blocks %d in %d docs ; banners %d ; mechanizable %s'
        % (s4['blocks'], s4['files'], s4['banners'], s4['mechanizable']))
    rec('  5 : per-keystone %s ; readable %d' % (s5['per_keystone'], s5['readable']))
    rec('  reads %d without_anchor %d ambiguous %d' % (len(reads), without, amb))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b396_extract_notes', L)
    json.dump(dict(s0=s0, s1=s1,
                   ranked=ranked, cheap=[z['act'] for z in cheap[:6]], costed=costed,
                   s4=s4, s5=s5, reads=len(reads), without_anchor=without, ambiguous=amb,
                   refs=R, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b396_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
