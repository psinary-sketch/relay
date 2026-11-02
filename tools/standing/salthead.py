# -*- coding: utf-8 -*-
"""standing/salthead.py -- v1.16.0, (R346)(3)(i), b735 data/b735_explicitformula.txt :211: THE VACUOUS PASS. REGISTRY.md :544's clause "no hypothesis that is the claim" was read by comparing the conclusion's text
with the binders' text. zq_count's proof is h.count, the claim inside h : ZQPremises, and the text differs, so the arm passed and tested nothing there. This reads the PROOF TERM: its head, and whether the head is a
projection of a hypothesis field. FAILS on a projection, printing it. A term that takes a field and goes on to apply compiled work to it is no projection, and the row prints which it is.

  proof_of(src, name)        the proof text of `theorem name`, from its `:=` to the next blank line or doc comment
  binders(head)              the names the statement binds
  read(head, proof)          dict(verdict PASS or FAIL, head, kind projection|elimination|compiled|tactic, why)
"""
import re

BIND = re.compile(r"[(\[{⦃]\s*([^\W\d][\w'₀-₉]*(?:\s+[^\W\d][\w'₀-₉]*)*)\s*:")
HEAD = re.compile(r"[^\W\d][\w'₀-₉]*(?:\.[^\W\d][\w'₀-₉]*)*")
ELIMS = ('elim', 'rec', 'casesOn')


def proof_of(src, name):
    L = (src or '').split('\n')
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':=' in L[k])
    out = [L[j].split(':=', 1)[1]]
    for l in L[j + 1:]:
        if not l.strip() or l.startswith('/--') or l.startswith('theorem '):
            break
        out.append(l)
    return ' '.join(' '.join(out).split())


def binders(head):
    return [n for g in BIND.findall(head or '') for n in g.split()]


def read(head, proof):
    p = (proof or '').strip()
    if p.startswith('by ') or p == 'by':
        return dict(verdict='PASS', head='by', kind='tactic', why='a tactic proof; the term arm does not apply, and the row says so')
    m = HEAD.match(p)
    h = m.group(0) if m else ''
    root, parts = h.split('.')[0], h.split('.')[1:]
    bound = binders(head)
    if root in bound and parts:
        if parts[-1] in ELIMS and re.search(r'\bfun\b|=>', p):
            return dict(verdict='PASS', head=h, kind='elimination', why='%s opens a field of %s and the body applies further work to it: %s' % (h, root, p[len(h):].strip()[:90]))
        return dict(verdict='FAIL', head=h, kind='projection', why='the proof is %s, a projection of the hypothesis %s: the claim is inside the hypothesis' % (p[:60], root))
    return dict(verdict='PASS', head=h, kind='compiled', why='the head %s is no projection of a bound hypothesis (binders %s)' % (h, bound or 'none'))
