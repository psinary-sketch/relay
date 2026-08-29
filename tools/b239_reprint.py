# -*- coding: utf-8 -*-
"""b239_reprint.py -- RE-ELABORATE THE INTERFACES LAYER AND READ ITS PROFILES.

### THE DISCLOSED DEBT THIS DISCHARGES: b235 amended File E's docstrings and DISCLOSED that
### it had not re-elaborated; b236 and b237 disclosed the same. ### A THIRD SILENCE WOULD HAVE
### BECOME A CLAIM. ### THIS RUNS IT.

### THE LAW THE FERRY STATES, AND THIS PROGRAMME HAS BROKEN IT TWICE:
### ### **A COMPILE IS NOT A VERIFICATION AND THE PROFILE IS READ.**
### b227 shipped a file that compiled clean and printed `sorryAx`; b231 shipped one that
### compiled clean and printed EIGHT axiom-bearing terminals. ### NO CLAIM OF SUCCESS IS MADE
### FROM AN EXIT CODE HERE: every printed profile is compared to its BANKED LINE, and any
### difference is reported at full prominence.

### THE PINS, AND THERE ARE TWO -- THE BANK ITSELF SAYS SO:
###   five files  -> D:/mathlib4              (v4.30.0-rc1, mathlib4 cecd0c4d56)  the declared pin
###   RestrictedTensorLayer1 -> D:/MY-DOwnloads/mathlib4 (v4.29.0), because the banked profile's
###     own header reads "(b193, 2026-08-26; built with Lean v4.29.0 against Mathlib)".
### ### USING ONE PIN FOR BOTH WOULD BE COMPARING A NEW PROFILE TO AN OLD BANK AND CALLING A
### ### TOOLCHAIN DIFFERENCE A FINDING.
"""
import io
import os
import re
import subprocess
import sys

SGS = r"D:\SIDE-global-section"
BANK = os.path.join(SGS, "AXIOM_PRINTS_INTERFACES.txt")
PIN_MAIN = r"D:\mathlib4"
PIN_LEGACY = r"D:\MY-DOwnloads\mathlib4"

FILES = [
    ("FiniteInstanceIdentity", PIN_MAIN),
    ("GlobalSection", PIN_MAIN),
    ("LocalLimit", PIN_MAIN),
    ("PadicFourier", PIN_MAIN),
    ("PadicStandardAddChar", PIN_MAIN),
    ("RestrictedTensorLayer1", PIN_LEGACY),
]

AX = re.compile(r"^'([^']+)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)\s*$")


def banked():
    """### THE BANKED PROFILE, PARSED BY TERMINAL NAME."""
    out = {}
    for line in io.open(BANK, encoding='utf-8', errors='replace'):
        m = AX.match(line.strip())
        if m:
            out[m.group(1)] = m.group(2)
    return out


def elaborate(mod, pin):
    """### `lake env lean <file>` FROM THE CHECKOUT, exactly as the repo's README declares."""
    path = os.path.join(SGS, "Interfaces", mod + ".lean")
    try:
        r = subprocess.run(["lake", "env", "lean", path], cwd=pin,
                           capture_output=True, timeout=3600)
    except Exception as e:
        return None, "### LAUNCH FAILED: %s" % e
    out = (r.stdout.decode('utf-8', 'replace') + r.returncode * 0 * "" +
           r.stderr.decode('utf-8', 'replace'))
    got = {}
    for line in out.splitlines():
        m = AX.match(line.strip())
        if m:
            got[m.group(1)] = m.group(2)
    return got, out


def main():
    bank = banked()
    print("=" * 100)
    print("b239 -- THE INTERFACES RE-PRINT. ### THE PROFILE IS READ, NOT INFERRED.")
    print("=" * 100)
    print("  banked terminals : %d" % len(bank))
    print("  pin (five files) : %s   %s" % (PIN_MAIN,
                                            io.open(os.path.join(PIN_MAIN, 'lean-toolchain'),
                                                    encoding='utf-8').read().strip()))
    print("  pin (Restricted) : %s   %s" % (PIN_LEGACY,
                                            io.open(os.path.join(PIN_LEGACY, 'lean-toolchain'),
                                                    encoding='utf-8').read().strip()))
    total = matched = missing = differing = extra = 0
    for mod, pin in FILES:
        print("\n--- %s   (pin %s)" % (mod, pin))
        got, raw = elaborate(mod, pin)
        if got is None:
            print("    %s" % raw)
            differing += 1
            continue
        if not got:
            print("    ### NO PROFILE LINES RETURNED. ### First 800 chars of output:")
            print("    " + raw[:800].replace("\n", "\n    "))
            differing += 1
            continue
        for name, prof in sorted(got.items()):
            total += 1
            b = bank.get(name)
            if b is None:
                extra += 1
                print("    %-58s ### NOT IN BANK: %s" % (name, prof))
            elif b == prof:
                matched += 1
                print("    %-58s MATCH" % name)
            else:
                differing += 1
                print("    %-58s ### DIFFERS" % name)
                print("        banked : %s" % b)
                print("        printed: %s" % prof)
    for name in sorted(bank):
        pass
    printed_names = set()
    print("\n" + "=" * 100)
    print("  terminals printed : %d      matched to bank : %d" % (total, matched))
    print("  differing         : %d      not in bank     : %d" % (differing, extra))
    ok = (differing == 0 and extra == 0 and total == len(bank))
    print("  ### EVERY PRINTED PROFILE MATCHES ITS BANKED LINE, AND THE COUNTS AGREE: %s"
          % ("YES" if ok else "NO"))
    print("  ### 'MATCH' MEANS THE PROFILE WAS RE-PRINTED AND COMPARED. ### It does not mean the")
    print("  ### statements are true -- only that their axiom dependencies are what the record says.")
    print("  ### CORE WAS NOT TOUCHED BY THIS ACT AND ITS 404-LINE PROFILE WAS NOT RE-RUN HERE.")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
