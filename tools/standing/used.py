# -*- coding: utf-8 -*-
"""standing/used.py -- v1.2.2 ((R332)(2)(ii)): THE READER THAT MARKS A DISCRIMINANT USED, BY THE DISCRIMINANT AND BY ITS PRINCIPAL FORM, IN
EVERY WORDING THE COEFFICIENT BANKS b711-b721 CARRY.

b721's reader (tools/b721_select.py used_set) read `D = ` and `n0(` alone, and missed -15, -23 and -39 in the older banks' wording (b721's
defect (h)): b711 names its field by its form's name alone ("Q0`s log-derivative coefficients"), b713 by "AT -15" and "Q1 = x^2 + xy +
4y^2", b717 by "AT -39" and "Q1 = x^2 + xy + 10y^2". The wordings, each read as written in the banks:
  HEAD       the head line's "AT -<n>" ("THE COEFFICIENT OBSERVATION AT -15", "THE COEFFICIENTS AT -39")
  D          "D = -<n>"
  N0         "n0(-<n>)"
  FORM       a principal form written out, "x^2 + xy + <c>y^2" (D = 1 - 4c) or "x^2 + <c>y^2" (D = -4c), not preceded by a coefficient
  TRIPLE     a principal form as a triple, "(1, 1, <c>)" or "(1, 0, <c>)"
  NAMED      the programme's named form Q0 (the principal form (1, 1, 6) of -23, b694's), where a bank names it as its object
A discriminant is USED where a coefficient bank carries it in any of these. Nothing written.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

BANKS = ('b711_coeffs.txt', 'b713_coeffs.txt', 'b717_coeffs.txt', 'b719_coeffs.txt', 'b720_coeffs.txt')   # ### b721 wrote none
NAMED = {'Q0': -23}

WORDINGS = (
    ('HEAD', re.compile(r'\A[^\n]*?\bAT (-\d+)\b'), lambda m: int(m.group(1))),
    ('D', re.compile(r'\bD = (-\d+)\b'), lambda m: int(m.group(1))),
    ('N0', re.compile(r'\bn0\((-\d+)\)'), lambda m: int(m.group(1))),
    ('FORM', re.compile(r'(?<![\w^])x\^2 \+ xy \+ (\d+)y\^2'), lambda m: 1 - 4 * int(m.group(1))),
    ('FORM', re.compile(r'(?<![\w^])x\^2 \+ (\d+)y\^2'), lambda m: -4 * int(m.group(1))),
    ('TRIPLE', re.compile(r'\(1, 1, (\d+)\)'), lambda m: 1 - 4 * int(m.group(1))),
    ('TRIPLE', re.compile(r'\(1, 0, (\d+)\)'), lambda m: -4 * int(m.group(1))),
    ('NAMED', re.compile(r'\b(Q0)(?:`s| \(1, 1, 6\)| =)'), lambda m: NAMED[m.group(1)]),
)


def read_text(text):
    """{D: set of wording kinds} in one bank's text."""
    out = {}
    for kind, rx, f in WORDINGS:
        for m in rx.finditer(text):
            out.setdefault(f(m), set()).add(kind)
    return out


def used(banks=BANKS, texts=None):
    """{D: {bank: sorted kinds}} over the coefficient banks (texts may pass {bank: text} in place of the files, for a plant)."""
    out = {}
    for b in banks:
        t = texts[b] if texts is not None and b in texts else A.rd(b)
        for d, kinds in read_text(t).items():
            out.setdefault(d, {})[b] = sorted(kinds)
    return out


def old_reading(banks=BANKS):
    """b721's reading (tools/b721_select.py used_set, its needle copied): `D = ` and `n0(` alone."""
    out = {}
    for b in banks:
        for m in re.finditer(r'(?:\bD = |n0\()(-\d+)', A.rd(b)):
            out.setdefault(int(m.group(1)), set()).add(b)
    return out
