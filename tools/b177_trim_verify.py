# -*- coding: utf-8 -*-
"""b177 -- the b123 trim table's cheap re-verification. RUN, NOT CLAIMED.

### WHAT THIS IS AND IS NOT, stated before the output: an md5 match says THE ARCHIVED
### BYTES ARE THE ARCHIVED BYTES; a path check says THE SUCCESSOR IS PRESENT.
### NEITHER IS A CONTENT COMPARISON, AND b123's VERDICTS ARE b123's -- not re-issued here.
"""
import hashlib, io, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PP = r"D:\MY-DOwnloads\PLACE-papers"
ARCH = os.path.join(PP, 'archive', '2026-08-23-trim-backfill')

BACKFILL = [
    ("INTERFACETS_MANUSCRIPT (1).docx", "4326b6c5099ab28ad7b790c6cc417e6c"),
    ("TRIVIUM_The_Third_Identity_Element.md", "78720b246efe872b064d209e128a42f6"),
    ("FOUNDATIONS_CLUSTER_SYNTHESIS_2026-05-19.md", "b1b1008a611200fe46698eafc73aea71"),
    ("METHODOLOGY_CLUSTER_SYNTHESIS_2026-05-19.md", "b1061d75f066d050f8dac5852b69c604"),
    ("ARXIV_SUBMISSION_FORMS.md", "e0d58bacfdb7503ab3782b41a3e24ee0"),
    ("DARK_MATTER_SIDE_CONSULT.md", "3a36689e07ec754e371beac1dded9588"),
    ("P_IDENT_PQC_SIDE_CONSULT.md", "f15a610ea040f70b9f12618be5de951c"),
    ("P_VS_NP_SIDE_CONSULT.md", "61f6a581cdadfdbef119923a3df5ef71"),
    ("SIDE_DOOR.md", "8bc136aa6bdc02fb3fd288823affa883"),
    ("PRIME_CORE_READER.md", "6265c7c181122f060f14101f031e835b"),
    ("CONSTANCE.md", "45adae6c77ce1ade86258f68ec3e4aae"),
]

SUCCESSORS = [
    ("CONSERVATION_OF_SPECTRA", "phase1.5/spectral/CONSERVATION.md"),
    ("Silence_of_Foundations", "day1/Silence_of_Foundations.md"),
    ("BSD_FORMATION_TRANSFER", "phase2/empirical/BSD_TRANSFER.md"),
    ("ARITHMETIC_ORIGIN_STEANE_CODE_v3", "phase2/quantum/STEANE_CODE.md"),
    ("COMPRESSION_THEOREM_DRAFT", "phase2/formation/COMPRESSION.md"),
    ("IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19",
     "clusters/IDENTITY_FORMATION_BIJECTION_CLUSTER_SYNTHESIS_2026-05-19.md"),
    ("RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19",
     "clusters/RH_CASCADE_CLUSTER_SYNTHESIS_2026-05-19.md"),
    ("MATTER_COSMOLOGY_CLUSTER_SYNTHESIS_2026-05-19",
     "clusters/MATTER_COSMOLOGY_CLUSTER_SYNTHESIS_2026-05-19.md"),
    ("CUBIT_TRIVIUM_CLUSTER_SYNTHESIS_2026-05-19",
     "clusters/CUBIT_TRIVIUM_CLUSTER_SYNTHESIS_2026-05-19.md"),
    ("SILENCE_AND_EMERGENCE_SUBMISSION", "phase2/philosophy/SILENCE_EMERGENCE.md"),
    ("CARMICHAEL_SIDE_CONSULT", "clusters/CARMICHAEL_SIDE_CONSULT.md"),
    ("MAHLER_SIDE_CONSULT", "clusters/MAHLER_SIDE_CONSULT.md"),
    ("SINGMASTER_SIDE_CONSULT", "clusters/SINGMASTER_SIDE_CONSULT.md"),
    ("COLLATZ_SIDE_CONSULT", "clusters/COLLATZ_SIDE_CONSULT.md"),
    ("ENUMERA_v1_5  [tier three, no verdict]", "phase1.5/method/ENUMERA.md"),
    ("FANO_PLANE_OF_ARITHMETIC  [tier three, no verdict]", "phase2/quantum/FANO_PLANE.md"),
]


def md5(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(65536), b''):
            h.update(c)
    return h.hexdigest()


print("=" * 92)
print("b177 -- THE b123 TRIM TABLE, CHEAP RE-VERIFICATION -- RUN, NOT CLAIMED")
print("=" * 92)
print("  ### AN md5 MATCH SAYS THE ARCHIVED BYTES ARE THE ARCHIVED BYTES.")
print("  ### A PATH CHECK SAYS THE SUCCESSOR IS PRESENT. NEITHER IS A CONTENT COMPARISON,")
print("  ### AND b123's VERDICTS ARE b123's -- THEY ARE NOT RE-ISSUED HERE.")
print()

print("--- THE ELEVEN BACKFILL ROWS: archive path + md5 ---")
ok = bad = 0
for name, want in BACKFILL:
    p = os.path.join(ARCH, name)
    if not os.path.exists(p):
        print("  ### PATH MISSING : %s" % name); bad += 1; continue
    got = md5(p)
    if got == want:
        print("  md5 OK           : %-46s %s" % (name, got)); ok += 1
    else:
        print("  ### md5 MISMATCH : %-46s got %s want %s" % (name, got, want)); bad += 1
print("  ### backfill rows: %d verified, %d not" % (ok, bad))
print()

print("--- THE SIXTEEN SUCCESSOR ROWS: does the named successor path exist? ---")
sok = sbad = 0
for name, rel in SUCCESSORS:
    p = os.path.join(PP, rel.replace('/', os.sep))
    if os.path.exists(p):
        print("  present          : %-58s -> %s" % (name, rel)); sok += 1
    else:
        print("  ### NOT AT THE PATH AS WRITTEN : %-40s -> %s" % (name, rel)); sbad += 1
print("  ### successor rows: %d present, %d not at the path as written" % (sok, sbad))
print()
print("=" * 92)
print("  ### THE FOUR DO-NOT-TRIM ROWS ARE NOT RE-VERIFIED AND CANNOT BE:")
print("  ### THE EXECUTOR CANNOT FINGERPRINT WHAT HE CANNOT READ (b123's own reason).")
print("=" * 92)
