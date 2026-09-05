# -*- coding: utf-8 -*-
"""b328_lore_append.py -- THE PHASE CONDITION INTO THE LORE, WITH ITS INCIDENT AND ITS GATE.
### APPEND ONLY, IDEMPOTENT, READ BACK BY RUNNING THE LORE'S OWN SELF-TEST.

### ### **THE RULE:** ### *a lawful test function's four-term sum at an off-line quadruple is
### `4 Re(G_e^2 - G_o^2)`: an even seed sees the zero only past forty-five degrees of phase, an odd
### component only below it.* ### **THE INCIDENT:** ### b326 -- the arc's family and a cosine-aimed
### family both came out positive at the first off-line quadruple, and the reason was named as a sign
### structure the construction lacked; b328 derived the structure: the phase. ### **THE GATE:** ###
### `b328_family.quadruple_sum` / `even_reduction` with fixtures in both polarities.
### ### **WHY LIST ONE:** ### it has a callable gate that fires.
"""
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, 'tools', 'lore_rules.py')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

MARK = "rule='A lawful test function\\'s four-term sum at an off-line quadruple is 4 Re(G_e^2 - G_o^2)"
# ### THE MARKER CARRIES THE ESCAPED APOSTROPHE THE FILE CARRIES. ### The first run's marker did not, so
# ### its read-back printed `entry once False` on an entry it had just written; the marker is corrected
# ### and the first run file is kept beside the re-run's.

ENTRY_ANCHOR = "         discharged='b326'),\n]\n"
ENTRY_NEW = (
    "         discharged='b326'),\n"
    "    dict(rule='A lawful test function\\'s four-term sum at an off-line quadruple is 4 Re(G_e^2 - G_o^2): '\n"
    "              'an even seed sees the zero only past forty-five degrees of phase, an odd component '\n"
    "              'only below it.',\n"
    "         incident='b326 -- the arc\\'s family and a cosine-aimed family both came out POSITIVE at the '\n"
    "                  'first off-line quadruple (phases -5 to 24 degrees, measured at b328), and the reason '\n"
    "                  'was named as a sign structure the construction lacked; b328 derived it from the '\n"
    "                  'source\\'s (147)-(148): f~(rho) = G(c) G(-c), the quadruple sums to 4 Re[G(c) G(-c)].',\n"
    "         tool='b328_family.quadruple_sum / even_reduction -- fixtures in both polarities (60 deg '\n"
    "              'negative, 30 deg positive; the odd part the other way round); the sine-aimed even seed '\n"
    "              'measured at 89 degrees and the cosine-aimed odd seed at 0.',\n"
    "         discharged='b328'),\n"
    "]\n")

FIX_ANCHOR = "def self_test(verbose=True):\n"
FIX_NEW = (
    "def _fixture_phase_condition():\n"
    "    \"\"\"### BOTH POLARITIES: an even seed at 60 degrees gives a NEGATIVE quadruple sum (the gate FIRES);\n"
    "    ### at 30 degrees a POSITIVE one (the gate stays QUIET); the odd part the other way round.\"\"\"\n"
    "    sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))\n"
    "    import b328_family\n"
    "    a, b, c, d = b328_family.fixtures()\n"
    "    return (a and c), (b and d)\n"
    "\n"
    "\n"
    "def self_test(verbose=True):\n")

LIST_ANCHOR = "                     ('scope-bound constant (b325/b326)', _fixture_scope_bound)]:\n"
LIST_NEW = ("                     ('scope-bound constant (b325/b326)', _fixture_scope_bound),\n"
            "                     ('phase condition (b326/b328)', _fixture_phase_condition)]:\n")

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    txt = io.open(PATH, encoding='utf-8').read()
    rec('=' * 100)
    rec('b328 -- THE LORE GAINS THE PHASE CONDITION, WITH ITS INCIDENT AND ITS GATE.')
    rec('=' * 100)
    present = MARK in txt
    rec('  rule already present : %s' % present)
    if not present:
        for anc in (ENTRY_ANCHOR, FIX_ANCHOR, LIST_ANCHOR):
            if anc not in txt:
                rec('  ### HARD FAILURE -- an anchor is not in the lore file: %r' % anc[:60])
                return 2
        new = txt.replace(ENTRY_ANCHOR, ENTRY_NEW, 1).replace(FIX_ANCHOR, FIX_NEW, 1).replace(LIST_ANCHOR, LIST_NEW, 1)
        open(PATH + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(PATH + '.tmp', PATH)
        rec('  written : the entry, its fixture, and the fixture\'s line in the self-test list')
    back = io.open(PATH, encoding='utf-8').read()
    rec('  read back : entry once %s ; fixture present %s' % (back.count(MARK) == 1, '_fixture_phase_condition' in back))
    r = subprocess.run([sys.executable, PATH], capture_output=True, text=True, encoding='utf-8', errors='replace')
    rec('  the lore\'s own self-test, run after the write : exit %d' % r.returncode)
    line = [ln for ln in (r.stdout or '').splitlines() if 'phase condition' in ln]
    for ln in line:
        rec('    %s' % ln.strip())
    both = any('fires: True' in ln and 'stays quiet: True' in ln for ln in line)
    rec('  ### BOTH POLARITIES ON THE NEW RULE : %s' % both)
    rec('=' * 100)
    return 0 if (r.returncode == 0 and both) else 1


if __name__ == '__main__':
    code = main()
    name = 'b328_lore_run.txt' if any('written :' in x for x in LINES) else 'b328_lore_rerun.txt'
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
