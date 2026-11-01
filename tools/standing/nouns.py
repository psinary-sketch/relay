# -*- coding: utf-8 -*-
"""standing/nouns.py -- v1.9.0, (R339)(2)(vii): COUNTS AND OBJECT NOUNS READ FROM THE BANKS; A TYPED ONE THAT DIFFERS HALTS THE CITATION CHECK.

b728's title said "the C2 theorem at 18 of 18 fields" where data/b728_c2.txt says the certificate compiled and the theorem did not; (R338)(3) said seven onsets
where the banks hold six. A row here names a text, what the text types, a bank and what the bank reads; the two read through one normal form (a number word to its
figure, a noun singular and lower case). The composers call `of_bank` for the word they print; the citation check calls `halts` over the act's rows and exits 3 on any.

  of_bank(bank_text, pattern) -> the normal form      halts(rows, read) -> [(label, typed, banked)]
  a row: (label, the text's name, the typed pattern, the bank's name, the bank's pattern); each pattern's group 1 the word
"""
import re

WORDS = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9, ten=10, eleven=11, twelve=12, eighteen=18)


def normal(w):
    w = (w or '').strip().lower()
    if w in WORDS:
        return str(WORDS[w])
    return w[:-1] if w.endswith('s') and not w.isdigit() else w


def of_bank(text, pattern):
    m = re.search(pattern, text or '')
    return normal(m.group(1)) if m else None


def answer_checks(bank):
    """v1.10.0, (R340)(2)(v): the answer checks the act ran, read from data/<act>_answer_check.txt, the bank the check writes, and not from the step-zero citation bank (b729's entry: 0 against three)."""
    return len(re.findall(r'(?m)^### \(R278\)\(4\) THE MID-ACT CHECK ', bank or ''))


def halts(rows, read):
    """each row whose text types a word that differs from its bank's; a text that does not type it is no difference, a bank that does not read it is one."""
    out = []
    for label, name, typed, bank, banked in rows:
        m = re.search(typed, read(name) or '')
        if not m:
            continue
        b = of_bank(read(bank), banked)
        if b != normal(m.group(1)):
            out.append((label, normal(m.group(1)), b))
    return out
