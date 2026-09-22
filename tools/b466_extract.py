# -*- coding: utf-8 -*-
"""b466_extract.py -- THE SURVEY. ### THE PRECONDITION CENSUS, AND WHAT THE PRESENT ARTEFACTS ALLOW.

### ### **THE PRECONDITION IS A MEASUREMENT HERE, NOT A GLANCE.** ### Five artefacts are named by
### the order; each is searched for by NAME across three trees and by CONTENT across the record,
### and each search is printed whether it hits or misses. ### **AN `ABSENT` THAT IS NOT SEARCHED
### FOR IS A GUESS**, and b404's rule -- every ABSENT carries a control -- applies to five of them
### at once. ### The control here is b358's own pinned source file, which IS on disk: the same
### searcher run over it must FIND it, or the searcher is what is broken and not the artefacts.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
NL = chr(10)
L, MISSES = [], []

# ### THE DEPOSITED PIN THE KERNEL LANE OPENS AT, AND NOTHING WIDER.
LV_PIN = 'v0.10.0'

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


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def sha256(p):
    try:
        return hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except Exception:
        return None


def by_name(pats, trees):
    """### **THE NAME SEARCH.** ### Every hit printed; the pattern printed even when it misses."""
    hits = []
    for tree in trees:
        for dp, dns, fns in os.walk(tree):
            if os.sep + '.git' in dp:
                continue
            for fn in fns:
                low = fn.lower()
                if any(re.search(p, low) for p in pats):
                    hits.append(os.path.join(dp, fn))
    return sorted(set(hits))


def by_content(needle, trees, cap=6):
    """### **THE CONTENT SEARCH.** ### A file that does not carry the NAME may carry the THING."""
    hits = []
    for tree in trees:
        for dp, dns, fns in os.walk(tree):
            if os.sep + '.git' in dp:
                continue
            for fn in fns:
                if not fn.lower().endswith(('.md', '.txt', '.json', '.lean', '.toml')):
                    continue
                p = os.path.join(dp, fn)
                try:
                    if os.path.getsize(p) > 4000000:
                        continue
                except Exception:
                    continue
                if needle.lower() in read(p).lower():
                    hits.append(p)
                    if len(hits) >= cap:
                        return sorted(set(hits))
    return sorted(set(hits))


def line_of(path, needle, show=240):
    for i, l in enumerate(read(path).split(NL)):
        if needle in l:
            return i + 1, l.strip()[:show]
    MISSES.append((os.path.basename(path), needle))
    return None, None


# --------------------------------------------------------------------------------------------
# ### (P1) THE PRECONDITION, ARTEFACT BY ARTEFACT.
# --------------------------------------------------------------------------------------------
TREES = [D, os.path.join(ROOT, 'reports'), PP]

ARTEFACTS = [
    ('the paper', [r'riemann.*zeta.*(paper|proportion)', r'anthropic.*\.pdf$', r'zeta.?23.*\.pdf$',
                   r'proportion.*\.(pdf|txt|md)$'], 'critical-line proportion'),
    ('the informal note', [r'informal.?note', r'anthropic.*note'], 'informal note'),
    ('the methodology note', [r'methodolog'], 'methodology note'),
    ('the transcripts', [r'transcript'], 'transcript'),
    ('a clone of anthropics/zeta-23-lean', [r'zeta.?23'], 'zeta-23-lean'),
]

# ### ### **THE NAME SEARCH KEPT THE CORPUS'S OWN FILES.** ### `methodolog` matched the programme's
# ### four `A_METHODOLOGY` documents and `transcript` matched its own `VERIFICATION_TRANSCRIPT`, and
# ### an artefact census that counts the searcher's own corpus as the thing it is looking for is
# ### b396's species -- a filter that keeps nine tenths. ### **BOTH YIELDS ARE PRINTED.** ### The
# ### narrowed one requires the file to be ABOUT THE EXTERNAL RESULT, which is what the order asked
# ### for: a hit must carry one of these owners' marks in its own bytes.
OWNER = re.compile(r'anthropic|zeta.?23|67\.2\s*%|41\.6\s*%', re.I)


def owned(path):
    """### **DOES THIS FILE BELONG TO THE EXTERNAL RESULT, OR TO THIS PROGRAMME?**"""
    if OWNER.search(os.path.basename(path)):
        return True
    try:
        if os.path.getsize(path) > 4000000:
            return False
    except Exception:
        return False
    return bool(OWNER.search(read(path)[:400000]))


def precondition():
    rec('=' * 104)
    rec('(P1) THE PRECONDITION, SEARCHED FOR RATHER THAN ASSUMED.')
    rec('=' * 104)
    rec('  ### trees searched : %s' % ' ; '.join(os.path.basename(t) or t for t in TREES))
    out = []
    for label, pats, needle in ARTEFACTS:
        wide = by_name(pats, TREES)
        nh = [h for h in wide if owned(h)]
        ch = [h for h in by_content(needle, TREES) if h not in nh]
        state = 'PRESENT' if nh else 'ABSENT'
        rec('')
        rec('  %-38s ### **%s**' % (label, state))
        rec('    by name, WIDE     : %d hit(s)' % len(wide))
        for h in wide[:4]:
            rec('      %s  %s' % (os.path.relpath(h, 'D:' + os.sep),
                                  'OWNED' if h in nh else '### REJECTED -- this corpus own file'))
        rec('    by name, NARROWED : %d hit(s)%s' % (len(nh), '' if nh else '   ### the artefact itself'))
        for h in nh[:4]:
            rec('      %s  sha256 %s' % (os.path.relpath(h, 'D:' + os.sep), (sha256(h) or '')[:16]))
        rec('    by content : %d hit(s)%s' % (len(ch), '   ### a RECORD OF it, not it' if ch else ''))
        for h in ch[:4]:
            rec('      %s' % os.path.relpath(h, 'D:' + os.sep))
        out.append(dict(artefact=label, state=state, name_hits=len(nh), wide_hits=len(wide), content_hits=len(ch),
                        content_examples=[os.path.relpath(h, 'D:' + os.sep) for h in ch[:4]]))
    # ### THE CONTROL. ### b404's rule: every ABSENT carries a control.
    ctl = by_name([r'^b358_source_lagarias'], TREES)
    rec('')
    rec('  ### ### **THE CONTROL ON FIVE ABSENTS** -- the same searcher, on a file known to be here:')
    rec('    b358_source_lagarias0404394.txt : %s   ### **CONTROL %s**'
        % ('FOUND' if ctl else 'NOT FOUND', 'FIRES' if ctl else 'FAILS -- THE SEARCHER IS BROKEN'))
    absent = [o['artefact'] for o in out if o['state'] == 'ABSENT']
    rec('')
    rec('  ### ### **PRESENT : %d. ### ABSENT : %d.**' % (5 - len(absent), len(absent)))
    rec('  ### ### **THE ORDER\x27s BRANCH IS TAKEN: `run only what the present artefacts allow`.**')
    return out, bool(ctl)


# --------------------------------------------------------------------------------------------
# ### (P2) WHAT THE RECORD DOES CARRY ABOUT THE ABSENT ARTEFACTS -- A PRIOR READ, LABELLED.
# --------------------------------------------------------------------------------------------
INTAKE = os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')
ACTIVATION = os.path.join(ROOT, 'reports', '2026-08-20-activation-act.md')


def prior_read():
    rec('')
    rec('=' * 104)
    rec('(P2) THE PRIOR READ, 2026-08-20. ### **A BANK ABOUT THE ARTEFACTS IS NOT THE ARTEFACTS.**')
    rec('=' * 104)
    got = {}
    for label, path, needle in (
            ('the intake headline', INTAKE, 'critical-line proportion 41.6%'),
            ('the Rule-3 primary log', INTAKE, 'FETCHED AND READ AT'),
            ('the method shape', INTAKE, 'rank inequality'),
            ('the paper-read flags', INTAKE, 'no-Euler-clause'),
            ('the clone SHA', ACTIVATION, 'shallow clone at'),
            ('the Mathlib pin', ACTIVATION, 'Mathlib `51e6992`'),
            ('the ExplicitFormula row', ACTIVATION, 'WEIL EXPLICIT FORMULA'),
            ('the conversion verdict', ACTIVATION, 'THE CONVERSION QUESTION'),
    ):
        n, txt = line_of(path, needle)
        if n:
            rec('  %-26s %s:%d' % (label, os.path.basename(path), n))
            rec('      %s' % txt)
            got[label] = dict(file=os.path.basename(path), line=n, text=txt)
        else:
            rec('  %-26s ### MISS -- %r' % (label, needle))
    return got


# --------------------------------------------------------------------------------------------
# ### (P3) THE DEPOSIT'S OWN LINE FOR THE PENDING INPUT -- THE SIDE OF THE COMPARISON THAT IS HERE.
# --------------------------------------------------------------------------------------------
def deposit_side():
    rec('')
    rec('=' * 104)
    rec('(P3) THE DEPOSIT\x27s OWN LINE: WHAT IT NAMES AS PENDING MATHLIB FORMALIZATION.')
    rec('=' * 104)
    out = {}
    for needle in ('the decomposition conjunct (Guinand–Weil) and the tail premise remain named',
                   'decomposition conjunct (Guinand–Weil) and `TailBoundPremise` remain named'):
        n, txt = line_of(os.path.join(DEP, 'A_Place_to_Stand.md'), needle, show=300)
        if n:
            rec('  A_Place_to_Stand.md:%d' % n)
            rec('      ...%s...' % txt[:280])
            out['deposit_line'] = dict(line=n, needle=needle)
            break
    n, txt = line_of(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md'),
                     'ExplicitFormulaDecomp', show=300)
    if n:
        rec('  PATHS_TO_THE_CRITICAL_LINE.md:%d   ### the same input, named as the DOOR-1 ingredient' % n)
        rec('      %s' % txt[:280])
        out['paths_line'] = dict(line=n)
    return out


# --------------------------------------------------------------------------------------------
# ### (P4) THE KERNEL LANE, OPEN FOR COMPONENT 2 ONLY: THE PREMISE AS DECLARED AT THE PIN.
# --------------------------------------------------------------------------------------------
GW = ('ExplicitFormulaDecomp', 'TailBoundPremise', 'partialPositivity_finiteRange',
      'lowFinset', 'explicitFormula')


def lv_side():
    rec('')
    rec('=' * 104)
    rec('(P4) THE KERNEL LANE, OPEN FOR THIS COMPONENT ONLY. ### SIDE-lv-conservation @ %s.' % LV_PIN)
    rec('=' * 104)
    r = git(LV, 'rev-parse', LV_PIN + '^{commit}')
    pin = r.stdout.strip()[:7]
    rec('  pin resolves to : %s   ### the deposit names v0.10.0 = 93c27ec' % pin)
    found = {}
    for name in GW:
        g = git(LV, 'grep', '-n', '-E',
                r'(theorem|lemma|def|abbrev|structure|inductive)\s+%s\b' % re.escape(name),
                LV_PIN, '--', '*.lean')
        lines = [l for l in g.stdout.strip().split(NL) if l.strip()]
        if not lines:
            rec('  %-32s ### NOT DECLARED AT THE PIN' % name)
            continue
        parts = lines[0].split(':', 3)
        path, lno = parts[1], int(parts[2])
        blob = git(LV, 'show', '%s:%s' % (LV_PIN, path)).stdout.replace(chr(13), '').split(NL)
        # ### ### **THE FIRST FORM STOPPED AT THE `:=` AND PRINTED A SIGNATURE, NOT A STATEMENT.**
        # ### For a `def ... : Prop :=` the Prop IS the body after the `:=`, and this act's whole
        # ### comparison is about that body -- so a reader that cuts there prints the one thing the
        # ### act is not allowed to leave out. ### Now: take the signature to its `:=`, then keep
        # ### every following line until the first BLANK line or the next top-level declaration.
        body, depth, past = [], 0, False
        for l in blob[lno - 1:lno + 24]:
            if past:
                if not l.strip():
                    break
                if re.match(r'^\s*(/--|@\[|theorem |lemma |def |noncomputable |abbrev )', l)                         and l[:1] not in (' ', chr(9)):
                    break
                body.append(l)
                continue
            body.append(l)
            depth += l.count('(') - l.count(')')
            if (':=' in l or ' where' in l) and depth <= 0 and len(body) >= 1:
                if l.rstrip().endswith(':=') or ' where' in l:
                    past = True
                    continue
                break
        stmt = NL.join(body)
        rec('')
        rec('  %-32s %s:%d   ### **READ AT THE PIN, STATEMENT NOT DOCSTRING**' % (name, path, lno))
        for l in stmt.split(NL)[:14]:
            rec('      %s' % l[:150])
        found[name] = dict(path=path, line=lno, statement=stmt, decls=len(lines))
    return pin, found


def main():
    pre, ctl = precondition()
    got = prior_read()
    dep = deposit_side()
    pin, lv = lv_side()
    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b466_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(precondition=pre, control_fires=ctl, prior_read=sorted(got),
                   deposit=dep, lv_pin=pin, lv_declared=sorted(lv),
                   lv_statements={k: v['statement'] for k, v in lv.items()},
                   misses=MISSES),
              io.open(os.path.join(D, 'b466_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
