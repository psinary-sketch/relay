# -*- coding: utf-8 -*-
"""b257_checks.py -- the b257 gates (resumed act). ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION; NO `or` APPEARS IN ANY CHECK.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the exception weakened a guard. ### **GATES 2-3 ARE THE ONES THIS ACT MOST NEEDS:
###       ### the guard files must be BYTE-UNCHANGED, and the hook must be shown STILL REFUSING --
###       ### with a positive control proving the refusal DISCRIMINATES rather than blankets.**
###   (2) that the exception exceeded its ruled diff. ### Gate 1 checks the commit's shape.
###   (3) that TECHNE-Core was pushed. ### Gate 6.
###   (4) that the author's text was edited. ### Gate 5, verbatim comparison.
###   (5) that a filing overwrote instead of appending. ### Gate 8.
"""
import io
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
TC = 'D:/MY-DOwnloads/TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-08')
PATH = 'phase1.5/method/patent-package'

REG = os.path.join(D, 'b257_registration_2026-08-29.txt')
BANK = os.path.join(D, 'b257_methodology_sweep.txt')
HOOKSRC = os.path.join(ROOT, 'tools', 'hooks', 'place_papers_pre_commit.py')
GUARD = os.path.join(ROOT, 'tools', 'place_add.py')
LOOM = os.path.join(PP, 'VERIFICATION_LOOM.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'CONTRIBUTION_MAP_2026-08.md')
LORE = os.path.join(MOD, 'HARNESS_LORE.md')
SIGN = os.path.join(MOD, 'SIGNEDNESS.md')
IDX = os.path.join(MOD, 'INDEX.md')

TC_HEAD = '22739c921dbc7019b97a50dc31a2239e6f0161fc'


def g(args, cwd=PP):
    return subprocess.run(['git', '-C', cwd] + args, capture_output=True, text=True).stdout


def hook_verdict(repo, staged_foreign):
    """### RUN THE REAL HOOK ON A SYNTHETIC REPO. ### Returns its exit code."""
    import tempfile
    import shutil
    d = tempfile.mkdtemp()
    try:
        os.makedirs(os.path.join(d, *PATH.split('/')))
        io.open(os.path.join(d, 'own.md'), 'w').write('x')
        if staged_foreign:
            io.open(os.path.join(d, *(PATH.split('/') + ['F.md'])), 'w').write('y')
        for a in (['init', '-q', '.'], ['config', 'user.email', 't@t'],
                  ['config', 'user.name', 't'], ['add', '-A']):
            subprocess.run(['git', '-C', d] + a, capture_output=True)
        env = dict(os.environ, PLACE_REPO=d)
        return subprocess.run([sys.executable, HOOKSRC], env=env,
                              capture_output=True).returncode
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main():
    h = Harness(ROOT, 'b257')

    # 1 -- ### THE CLOSE CONDITION, AND THE RULED DIFF'S SHAPE.
    h.run('zero-patent-paths-tracked-and-files-still-on-disk',
          check=lambda: bool(len([x for x in g(['ls-files']).split('\n')
                                  if x.startswith(PATH + '/')]) == 0
                             and os.path.isdir(os.path.join(PP, *PATH.split('/')))
                             and len([1 for dp, dn, fn in
                                      os.walk(os.path.join(PP, *PATH.split('/')))
                                      for f in fn if '.git' not in dp]) > 200
                             and contains(BANK, '**0** PATENT-PACKAGE PATHS TRACKED')),
          # ### FIXTURE: demand the files be GONE from disk too. ### The ruling forbade that, and
          # ### 221 remain, so this fails on the real tree rather than on a negation.
          fixture=lambda: bool(not os.path.isdir(os.path.join(PP, *PATH.split('/')))),
          witness=lambda: bool(os.path.isdir(PP)))

    # 2 -- ### THE GUARDS ARE BYTE-UNCHANGED. ### NO AMENDMENT WAS MADE.
    h.run('neither-guard-file-was-edited',
          check=lambda: bool(g(['status', '--porcelain', '--',
                                'tools/hooks/place_papers_pre_commit.py', 'tools/place_add.py'],
                               cwd=ROOT).strip() == ''
                             and contains(HOOKSRC, 'git commit --no-verify` bypasses it')
                             and contains(HOOKSRC, 'A hook constrains a habit; it does')
                             and contains(BANK, 'THE GUARD\'S OWN DOCUMENTED OVERRIDE')
                             and contains(BANK, 'NEVER EDITED')),
          # ### FIXTURE: demand the whole relay tree be clean. ### It is not -- this act wrote
          # ### banks and tools -- so this fails on the real state.
          fixture=lambda: bool(g(['status', '--porcelain'], cwd=ROOT).strip() == ''),
          witness=lambda: bool(os.path.exists(GUARD)))

    # 3 -- ### THE HOOK STILL REFUSES, AND ITS REFUSAL DISCRIMINATES.
    #      ### **THE POSITIVE CONTROL IS THE HALF THAT MATTERS: a guard that refused everything
    #      ### would also "still refuse", and would be worthless.**
    h.run('hook-refuses-foreign-and-passes-own-positive-control',
          check=lambda: bool(hook_verdict(PP, True) == 1 and hook_verdict(PP, False) == 0
                             and contains(BANK, 'SO THE REFUSAL DISCRIMINATES')),
          # ### FIXTURE: claim the hook refuses a NON-foreign staging too. ### It does not (exit 0),
          # ### so this fails -- and that failure is what proves the guard is not a blanket no.
          fixture=lambda: bool(hook_verdict(PP, False) == 1),
          witness=lambda: bool(hook_verdict(PP, True) == 1))

    # 4 -- ### NINE MODULE FILES, IN THE CANONICAL CLONE.
    h.run('nine-modules-written-in-the-canonical-clone',
          check=lambda: bool(sorted(os.listdir(MOD)) == sorted([
              'SIGNEDNESS.md', 'BANKED_MEANINGS_ENGINE.md', 'IMPORT_LEDGER.md',
              'HARNESS_LORE.md', 'DISCRIMINATOR_PROTOCOL.md', 'FACE_OFF_PROTOCOL.md',
              'DECISION_CARD_FORMAT.md', 'RENDER_AS_E0.md', 'INDEX.md'])
              and g(['rev-parse', 'HEAD'], cwd=TC).strip() == TC_HEAD),
          fixture=lambda: bool(len(os.listdir(MOD)) == 8),
          witness=lambda: bool(os.path.isdir(MOD)))

    # 5 -- ### THE AUTHOR'S BLOCK IS VERBATIM. ### NOT EDITED, NOT PARAPHRASED.
    h.run('signedness-block-verbatim-and-unedited',
          check=lambda: bool(all(s in io.open(SIGN, encoding='utf-8').read() for s in [
              'S \u2014 SYMMETRY', 'I \u2014 INDEPENDENCE', 'D \u2014 DETERMINATION',
              'E \u2014 EXHAUSTIVENESS', '+S \u2014 CLOSURE',
              "reference implementation: b254's", 'Signedness\nCertificate',
              "Loci's Ratchet \u2014 subsumed as the module's monotone special"])
              and contains(SIGN, 'The author\'s text stands as written')
              and contains(SIGN, 'UNCONFIRMED AT THE ONE DOCUMENT READ')),
          # ### FIXTURE: claim a phrase the block does NOT contain.
          fixture=lambda: bool('S \u2014 SIGNATURE' in io.open(SIGN, encoding='utf-8').read()),
          witness=lambda: bool(os.path.getsize(SIGN) > 3000))

    # 6 -- ### TECHNE-Core WAS NOT PUSHED. ### LOCAL-ONLY, AS SCOPED.
    h.run('techne-core-not-pushed-modules-untracked',
          check=lambda: bool(g(['rev-parse', 'HEAD'], cwd=TC).strip() == TC_HEAD
                             and any(l.startswith('?? modules/')
                                     for l in g(['status', '--porcelain'], cwd=TC).split('\n'))
                             and contains(BANK, 'TECHNE-Core WAS *NOT* PUSHED')
                             and contains(IDX, 'was NOT pushed by the act that wrote these files')),
          # ### FIXTURE: demand modules/ be TRACKED. ### It is untracked by design.
          fixture=lambda: bool(g(['ls-files', 'modules/'], cwd=TC).strip() != ''),
          witness=lambda: bool(len(TC_HEAD) == 40))

    # 7 -- ### THE TWO ORDERED LORE LINES, AND NO CLAIM LANGUAGE IN THE INDEX.
    h.run('two-lore-lines-added-and-index-is-aim-only',
          check=lambda: bool(contains(LORE, 'A guard minted after an incident audits the past it '
                                            'was minted against')
                             and contains(LORE, 'Closed-by-default disclosure')
                             # ### THIS GATE'S FIRST FORM CARRIED TWO NEGATED CONJUNCTS DEMANDING
                             # ### THE **ABSENCE** OF `enumerations private, counts public` -- a
                             # ### phrase that is the lore line's own subtitle and is of course
                             # ### present. ### **THAT IS b255's DEFECT EXACTLY, AND I COMMITTED IT
                             # ### IN THE GATE THAT CHECKS THE LORE LINE ABOUT IT.**
                             # ### ### **THE RULE IS WRITTEN DOWN AND STILL WENT UNAPPLIED ONE
                             # ### ### FUNCTION AWAY FROM ITS OWN TEXT -- WHICH IS THE SHARPEST
                             # ### ### EVIDENCE THIS SESSION HAS PRODUCED THAT LORE IS NOT A GUARD.**
                             # ### Corrected to assert PRESENCE, which is what was meant.
                             and contains(LORE, 'enumerations private, counts public')
                             and contains(LORE, 'b258')
                             # ### every relevance row in the INDEX is graded AIM
                             and io.open(IDX, encoding='utf-8').read().count('**AIM**') >= 8
                             and contains(IDX, 'No claim language is drafted here')),
          fixture=lambda: bool(io.open(IDX, encoding='utf-8').read().count('**AIM**') == 0),
          witness=lambda: contains(LORE, 'b258'))

    # 8 -- ### THE FILINGS APPENDED; NOTHING OVERWRITTEN; THE OWED MARKER SURVIVES.
    h.run('loom-and-map-appended-owed-marker-intact',
          check=lambda: bool(contains(LOOM, 'b257 \u2014 THE GUARD EXCEPTION')
                             and contains(MAP, 'QUOTATION OWED')
                             and contains(MAP, 'DISCHARGED 2026-08-29 (b257)')
                             and contains(MAP, 'the `OWED` marker above is left visible')
                             # ### the commit that wrote them had 0 deletions
                             and re.search(r'62 insertions\(\+\)',
                                           g(['show', '--stat', '--format=', '240cf04']))
                             is not None
                             and 'deletion' not in g(['show', '--stat', '--format=', '240cf04'])),
          # ### FIXTURE: claim the OWED marker was removed. ### It was deliberately kept.
          fixture=lambda: bool(not contains(MAP, 'QUOTATION OWED')),
          witness=lambda: contains(MAP, 'b257'))

    # 9 -- ### THE TAUTOLOGY CONTROL. ### THE OVERRIDE CLAIM MUST HAVE CONTENT.
    #      ### "the guard is unchanged" is FORCED if nothing was ever going to change it; what is
    #      ### NOT forced is that the hook still DISCRIMINATES. ### Gate 3 supplies that half.
    h.run('override-claim-is-not-vacuous',
          check=lambda: bool(
              # ### forced half: an unedited file is unedited
              g(['status', '--porcelain', '--',
                 'tools/hooks/place_papers_pre_commit.py'], cwd=ROOT).strip() == ''
              # ### NOT forced: that the unedited guard still separates the two cases
              and hook_verdict(PP, True) != hook_verdict(PP, False)
              and contains(BANK, 'IT IS A DEMONSTRATION OF\n### ### CONTINUITY, NOT OF REPAIR')),
          # ### FIXTURE: the vacuous form -- the two hook verdicts asserted EQUAL, which would mean
          # ### the guard cannot tell the cases apart and the demonstration proves nothing.
          fixture=lambda: bool(hook_verdict(PP, True) == hook_verdict(PP, False)),
          witness=lambda: bool(hook_verdict(PP, True) == 1))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
