# -*- coding: utf-8 -*-
"""b531_read.py -- COMPONENTS 1 AND 2: THE DEPOSITED PREMISE PRINTED, AT THE PIN AND AT HEAD. ### `python tools/b531_read.py`

### READING (1) of the sealed face. Every quotation is `git show <ref>:<file>` of SIDE-kernel, cut from the declaration
### line to the `:=` (and, for the terminal and the lemmas it uses, whole), at the deposit pin v1.5 = 0e5233f and at HEAD;
### the two refs compared byte for byte per file. ### The unfolding chain: ConservationHypothesis -> is_xi_zero (XiDef)
### and prime_as_real (Voice1); the terminal -> rh_from_structural_exhaustiveness, structural_exhaustiveness_proved,
### conservation_activates_balance, balance_theorem, rh_implies_mathlib_rh, Mathlib's RiemannHypothesis (quoted from
### XiDef's own docstring and from the pin's Mathlib source). ### Profiles: READ from banked output only -- nothing compiled.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
PIN, NL = '0e5233f', chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

FILES = ['Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean', 'Kernel/Integration.lean',
         'Kernel/PoissonExhaustion.lean', 'AxiomCheck_v1_3.lean', 'DEPOSIT_v1_2_NOTES.md']
DECLS = [('Bridge/ConservationBridge.lean', 'def', 'ConservationHypothesis'),
         ('Bridge/ConservationBridge.lean', 'theorem', 'riemann_hypothesis'),
         ('Bridge/ConservationBridge.lean', 'theorem', 'structural_exhaustiveness_proved'),
         ('Bridge/ConservationBridge.lean', 'theorem', 'conservation_activates_balance'),
         ('Kernel/XiDef.lean', 'def', 'is_xi_zero'),
         ('Kernel/XiDef.lean', 'theorem', 'rh_implies_mathlib_rh'),
         ('Kernel/Voice1.lean', 'def', 'prime_as_real'),
         ('Kernel/Voice1.lean', 'theorem', 'balance_theorem'),
         ('Kernel/Integration.lean', 'def', 'StructuralExhaustiveness'),
         ('Kernel/Integration.lean', 'theorem', 'rh_from_structural_exhaustiveness'),
         ('Kernel/Integration.lean', 'theorem', 'structural_exhaustiveness_from_rh'),
         ('Kernel/Integration.lean', 'theorem', 'structural_exhaustiveness_iff_rh')]


def show(ref, f):
    r = subprocess.run(['git', '-C', SK, 'show', '%s:%s' % (ref, f)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def decl(text, kw, name):
    m = re.search(r'^%s %s\b' % (kw, re.escape(name)), text, re.M)
    if not m:
        return None, None
    i = m.start()
    j = text.index(':=', i)
    k = text.find(NL + NL, i)
    return text[i:j + 2], text[i:k if k >= 0 else len(text)].rstrip()


def main():
    head = subprocess.run(['git', '-C', SK, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    pin = subprocess.run(['git', '-C', SK, 'rev-parse', PIN], capture_output=True, text=True).stdout.strip()
    tag = subprocess.run(['git', '-C', SK, 'tag', '--points-at', PIN], capture_output=True, text=True).stdout.split()
    same = {f: (show(PIN, f) == show('HEAD', f), show(PIN, f) is not None) for f in FILES}
    out = dict(pin=pin, pin_tags=tag, head=head, files_identical={f: v[0] for f, v in same.items()},
               files_present_at_pin={f: v[1] for f, v in same.items()}, decls=[])
    L = ['=' * 120, 'b531 -- THE DEPOSITED PREMISE, PRINTED (SIDE-kernel, pin %s %s, HEAD %s).' % (pin[:12], tag, head[:12]), '=' * 120, '']
    L.append('### THE FILES, PIN AGAINST HEAD, BYTE FOR BYTE:')
    for f, (s, p) in same.items():
        L.append('  %-36s present at pin %-5s identical %s' % (f, p, s))
    for f, kw, name in DECLS:
        t = show(PIN, f)
        h, whole = decl(t, kw, name)
        th = show('HEAD', f)
        h2, whole2 = decl(th, kw, name)
        body_lines = len(whole.split(NL)) if whole else 0
        out['decls'].append(dict(file=f, name=name, kw=kw, head=h, whole=whole, lines=body_lines, same_at_head=(whole == whole2)))
        L += ['', '### %s %s  (%s ; %d lines ; identical at HEAD %s)' % (kw, name, f, body_lines, whole == whole2), whole or '### NOT FOUND']
    nt = show(PIN, 'DEPOSIT_v1_2_NOTES.md') or ''
    prof = [l for l in nt.split(NL) if "'ConservationBridge.riemann_hypothesis' depends on axioms" in l
            or "'techne_kernel_integration.structural_exhaustiveness_iff_rh' depends on axioms" in l
            or "'techne_kernel_integration.rh_from_structural_exhaustiveness' depends on axioms" in l]
    out['banked_profiles'] = prof
    out['banked_profiles_source'] = 'DEPOSIT_v1_2_NOTES.md at %s (recorded at v1.2 = b1407b2, before W-7 changed the premise at v1.3)' % PIN
    std3 = "depends on axioms: [propext, Classical.choice, Quot.sound]"
    out['riemann_hypothesis_std3_banked'] = any(l.strip() == "'ConservationBridge.riemann_hypothesis' %s" % std3 for l in prof)
    L += ['', '### THE PROFILES, READ FROM THE BANKED OUTPUT (nothing compiled):'] + ['  ' + l for l in prof]
    L += ['  ### source : %s' % out['banked_profiles_source'],
          '  ### ConservationHypothesis is a def: it has no theorem profile of its own; its dependencies are those of its',
          '  ### unfolding (riemannZeta, Nat.Prime, Real.rpow), printed above.']
    io.open(os.path.join(D, 'b531_read.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b531_premise.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
