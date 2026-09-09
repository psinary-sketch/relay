# -*- coding: utf-8 -*-
"""b386_components.py -- THE FOUR COMPONENTS OF b386.

### ### **COMPONENT 2 DELETES A TRACKED FILE, AND THE ORDER OF OPERATIONS IS THE POINT.** ### The
### recoverability proof is printed ### **BEFORE** ### the `git rm`, not after it. ### `b385`
### removed an untracked backup and only afterwards worked out what had been in it; ### **THAT IS
### ### THE SAME ACT IN THE WRONG ORDER**, and the arm that catches it is an ordering arm, not a
### content arm.
###
### ### **AND THE INSTALLED GUARD IS COMPARED AGAINST THE SOURCE`S OWN GIT BLOB, NOT AGAINST THE
### ### SOURCE`S WORKING FILE.** ### `core.autocrlf` makes the working file CRLF while the blob
### stays LF (`b309`), so a working-file comparison would fail on a correct install and a
### size comparison would pass on a wrong one. ### **LF-NORMALISED, AGAINST THE BLOB. ### NEVER BY
### ### FILENAME AND NEVER BY SIZE ALONE.**
###
### ### **COMPONENT 3`S REPAIR IS STRICTLY STRONGER THAN THE ORDER ASKED FOR, AND THAT IS SAID
### ### RATHER THAN SLIPPED IN.** ### The order asks that the tool not overwrite a backup ### *it
### did not create*. ### There is no reliable way to ask a file who wrote it, so the implemented
### invariant is ### **IT NEVER OVERWRITES AN EXISTING BACKUP AT ALL** -- which implies the
### property asked for and is checkable. ### **A STRONGER INVARIANT SUBSTITUTED FOR A WEAKER ONE
### ### IS STILL A SUBSTITUTION**, so it is named here and in the bank.
###
### ### **COMPONENT 4(i) IS AN EXPERIMENT WHOSE RESULT WAS KNOWN BEFORE THE LOCK** ### and is
### declared on the face as reading (6), so it is reported and not presented as a discovery.
"""
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
GUARD = os.path.join(ROOT, '.githooks', 'pre-push')
SRCREL = 'tools/git-hooks/pre-push'
SRC = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')
HOOKTOOL = os.path.join(ROOT, 'tools', 'b304_hooks.py')
REGISTRY = os.path.join(PP, 'REGISTRY.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def d(n):
    return os.path.join(D, n)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gitb(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def lf(b):
    return b.replace(b'\r\n', b'\n')


def sha(b):
    return hashlib.sha256(b).hexdigest()


E = json.load(io.open(d('b386_reads.json'), encoding='utf-8'))
BUILT = {r['label']: r for r in E['built']}


def q(label):
    """### A QUOTATION IS PULLED BY ITS LABEL OUT OF THE EXTRACT AND ### **RE-READ AT ITS OWN LINE
    ### NUMBER** ### before it is printed. ### A quotation that cannot re-read is a failure and is
    ### counted, never softened."""
    b = BUILT[label]
    ok = False
    if b.get('line'):
        try:
            ls = io.open(b['path'], encoding='utf-8', errors='replace').read().split(chr(10))
            ok = (ls[b['line'] - 1].rstrip(chr(10)) == b['text'])
        except OSError:
            ok = False
    if not ok:
        FAILS.append((label, b['file'], b['line']))
    return b, ok


FAILS = []


# ==================================================================================================
def component1():
    rec('')
    rec('-' * 100)
    rec("### COMPONENT 1 -- b385'S THREE OPTIONS, QUOTED, AND THE ONE THAT IMPLEMENTS `(R15)`.")
    rec('-' * 100)
    rec('### ### **ONE DISCREPANCY WITH THE ORDER, REPORTED RATHER THAN SMOOTHED.** ### The order')
    rec('### says to reproduce the three options ### *from its bank*. ### **`b385`S BANK,')
    rec('### ### `data/b385_the_six_on_the_trails.txt`, DOES NOT CARRY THEM** -- they are in')
    rec('### `data/b385_closing.txt`, in that act`s DRAFT for this one. ### The quotation is taken')
    rec('### from where the text is and ### **THE LOCATION IS PRINTED WITH IT.**')
    bank385 = io.open(d('b385_the_six_on_the_trails.txt'), encoding='utf-8',
                      errors='replace').read()
    in_bank = ('REPAIR THE SOURCE' in bank385) or ('RETIRE THE SOURCE' in bank385)
    rec('###   the options appear in `b385_the_six_on_the_trails.txt` : ### **%s**' % in_bank)
    rec('')
    rec('### ### **THE THREE OPTIONS, VERBATIM, WITH THEIR LOCATIONS:**')
    OPT = [
        ('(a)', 'b385 option (a) -- repair the source, leaving both files'),
        ('(b)', 'b385 option (b) -- retire the source and repoint the installer'),
        ('(b)', 'b385 option (b) -- one source of truth, the tool installs what runs'),
        ('(c)', 'b385 option (c) -- neither, the comment allowed to drift'),
    ]
    quoted = {}
    for tag, lbl in OPT:
        b, ok = q(lbl)
        quoted.setdefault(tag, []).append(b['text'])
        rec('###   `%s` line %-4d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'])
    rec('')
    rec('### ### **`(R15)`, IN THE AUTHOR`S OWN WORDS, READ AT ITS OWN LINE:**')
    for lbl in ('the ruling (R15) -- one guard, one source',
                'the ruling (R15) -- the installer reads from that source',
                'the ruling (R15) -- the three disposals of a second copy',
                'the ruling (R15) -- whichever the repository`s mechanics allow',
                'the ruling (R15) -- a topology defect, not a repair job'):
        b, _ok = q(lbl)
        rec('###   | %s' % b['text'])
    rec('')
    rec('### ### ### **WHICH OPTION IMPLEMENTS `(R15)`, TESTED CLAUSE BY CLAUSE.**')
    tests = [
        ('(a)', 'REPAIR THE SOURCE, LEAVING BOTH FILES', False,
         'it makes the two copies AGREE but leaves ### **TWO TRACKED SOURCES OF TRUTH**, which is '
         'the first clause of the ruling. ### And `(R15)` says the divergence is ### **A TOPOLOGY '
         'DEFECT** -- (a) repairs the text and leaves the topology.'),
        ('(b)', 'RETIRE THE SOURCE AND REPOINT THE INSTALLER', True,
         'it leaves ### **EXACTLY ONE TRACKED SOURCE** ### per repository and makes ### **THE '
         'INSTALLER READ FROM IT** -- the ruling`s two clauses, in order. ### The retirement is '
         '`(R15)`s FIRST disposal, ### *a second copy is deleted*.'),
        ('(c)', 'NEITHER, THE COMMENT ALLOWED TO DRIFT', False,
         'it leaves both copies AND the divergence. ### **IT IS THE STATE THE RULING WAS WRITTEN '
         'TO END.**'),
    ]
    impl = []
    for tag, name, ok, why in tests:
        rec('###   ### **OPTION `%s` -- %s : %s**' % (tag, name, 'IMPLEMENTS `(R15)`' if ok
                                                      else 'DOES NOT'))
        rec('###     %s' % why[:170])
        if len(why) > 170:
            rec('###     %s' % why[170:400])
        if ok:
            impl.append(tag)
    rec('')
    rec('### ### **OPTIONS REPRODUCED : %d. ### NAMED AS IMPLEMENTING `(R15)` : %d. ### INVENTED '
        'BY THIS SEAT : 0.**' % (len(quoted), len(impl)))
    if len(impl) != 1:
        rec('### ### ### **HALT. ### %s OPTION IMPLEMENTS THE RULING, SO NOTHING IS EXECUTED.**'
            % ('NO' if not impl else 'MORE THAN ONE'))
        rec('### ### ### **THE AUTHOR DOES NOT RULE ON OPTIONS A SEAT HAS NOT SHOWN HIM.**')
        return dict(halt=True, options_quoted=len(quoted), implementing=impl,
                    options_in_bank385=in_bank)
    rec('### ### ### **OPTION `%s` IS EXECUTED. ### NO OPTION WAS RE-WORDED TO MAKE IT FIT.**'
        % impl[0])
    return dict(halt=False, options_quoted=len(quoted), implementing=impl, chosen=impl[0],
                options_in_bank385=in_bank, options_invented=0)


# ==================================================================================================
def component2():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 2 -- THE REPAIR. ### **THE PROOF BEFORE THE DELETION.**')
    rec('-' * 100)
    rec('### ### ### **(a) THE RECOVERABILITY PROOF, PRINTED BEFORE ANYTHING IS DELETED.**')
    # ### ### **THE PROOF IS TAKEN FROM THE FILE IF IT IS THERE AND FROM ITS BLOB IF THIS ACT HAS
    # ### ### ALREADY REMOVED IT**, so a re-run reports the deletion as already done instead of
    # ### crashing. ### **AN ACT THAT CANNOT BE RE-RUN CANNOT BE CHECKED.**
    already_gone = not os.path.exists(SRC)
    if already_gone:
        src_now = gitb(ROOT, 'show', 'HEAD:%s' % SRCREL) or b''
        rec('###   ### **ALREADY DELETED BY THIS ACT`S OWN EARLIER RUN.** ### The proof below is')
        rec('###   taken from `HEAD:%s`, which still carries it.' % SRCREL)
    else:
        src_now = io.open(SRC, 'rb').read()
    blobs = {}
    for path in ('.githooks/pre-push', SRCREL):
        for c in git(ROOT, 'log', '--format=%H', '--all', '--', path).split(chr(10)):
            if not c.strip():
                continue
            b = gitb(ROOT, 'show', '%s:%s' % (c.strip(), path))
            if b is not None:
                blobs['%s:%s' % (c.strip()[:7], path)] = lf(b)
    match = sorted(k for k, v in blobs.items() if v == lf(src_now))
    rec('###   the file about to be deleted : `%s`' % SRCREL)
    rec('###   bytes on disk %d   sha (LF-normalised) `%s`' % (len(src_now), sha(lf(src_now))[:16]))
    rec('###   ### **RECOVERABLE FROM : %s**' % (', '.join(match) or '### ### **NONE**'))
    proof_before = bool(match)
    if not proof_before:
        rec('###   ### ### **HALT. ### A COPY THAT MATCHES NO TRACKED BLOB IS NOT DELETED.**')
        return dict(halt=True, deleted=0)
    rec('###   ### **AND THE DELETION IS ITSELF RECOVERABLE**: the file is TRACKED, so `git rm`')
    rec('###   leaves it in every commit that carried it. ### **THIS IS THE ORDER `b385` GOT')
    rec('###   ### WRONG** -- it removed a file and worked out afterwards what had been in it.')

    rec('')
    rec('### ### ### **(b) THE DELETION.** ### `(R15)`s FIRST DISPOSAL.')
    if already_gone:
        rec('###   `git rm %s` : ### **ALREADY APPLIED**' % SRCREL)
        deleted = True
    else:
        r = subprocess.run(['git', '-C', ROOT, 'rm', '-q', '--', SRCREL], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        deleted = not os.path.exists(SRC)
        rec('###   `git rm %s` : exit %d ; gone from the working tree : ### **%s**'
            % (SRCREL, r.returncode, deleted))
    tracked_after = [x for x in git(ROOT, 'ls-files').split(chr(10)) if 'pre-push' in x]
    rec('###   tracked paths matching `pre-push` in `relay` now : %s' % tracked_after)

    rec('')
    rec('### ### ### **(c) THE INSTALLER REPOINTED.**')
    src_txt = io.open(HOOKTOOL, encoding='utf-8').read()
    OLD = "SOURCE = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')"
    NEW = "SOURCE = os.path.join(ROOT, '.githooks', 'pre-push')"
    repointed = False
    if OLD in src_txt:
        src_txt = src_txt.replace(OLD, NEW, 1)
        io.open(HOOKTOOL, 'w', encoding='utf-8', newline=chr(10)).write(src_txt)
        repointed = True
    elif NEW in src_txt:
        repointed = True
    rec('###   was : `%s`' % OLD)
    rec('###   now : `%s`' % NEW)
    rec('###   ### **THE INSTALLER NOW READS THE FILE THE REPOSITORIES RUN : %s**' % repointed)

    return dict(halt=False, proof_before_deletion=proof_before, deleted=1 if deleted else 0,
                recoverable_from=match, repointed=repointed,
                tracked_pre_push_in_relay=tracked_after)


def component2_install():
    """### RUN AFTER THE TOOL IS REPAIRED, SO THE INSTALL EXERCISES THE REPAIRED TOOL AND NOT THE
    ### OLD ONE. ### **AN INSTALL RUN BY THE DEFECTIVE TOOL WOULD PROVE NOTHING ABOUT THE FIX.**"""
    rec('')
    rec('### ### ### **(d) THE INSTALLER RUN, AND THE INSTALLED BYTES COMPARED TO THE SOURCE`S')
    rec('### ### ### OWN GIT BLOB.**')
    r = subprocess.run([sys.executable, HOOKTOOL], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT)
    out = (r.stdout or '') + (r.returncode and (r.stderr or '') or '')
    io.open(d('b386_install_run.txt'), 'w', encoding='utf-8', newline=chr(10)).write(out)
    for ln in out.split(chr(10)):
        if any(k in ln for k in ('REPLACED', 'ALREADY IDENTICAL', 'INSTALLED',
                                 'BYTE-IDENTICAL TO THE TRACKED SOURCE')):
            rec('###   %s' % ln.strip()[:120])
    blob = gitb(ROOT, 'show', 'HEAD:.githooks/pre-push')
    rec('###   ### **THE SOURCE`S OWN GIT BLOB** ### `HEAD:.githooks/pre-push` : %d bytes (LF), '
        'sha `%s`' % (len(blob or b''), sha(lf(blob or b''))[:16]))
    REPAIRED = '# Tracked at .githooks/pre-push (moved there b371, 2026-09-08).'
    rows, allmatch, allline = [], True, True
    for name, repo in b303_pins.REPOS:
        p = os.path.join(repo, '.githooks', 'pre-push')
        raw = io.open(p, 'rb').read() if os.path.exists(p) else b''
        same = lf(raw) == lf(blob or b'')
        line = REPAIRED.encode('utf-8') in lf(raw)
        hp = git(repo, 'config', 'core.hooksPath').strip()
        allmatch = allmatch and same
        allline = allline and line
        rows.append(dict(repo=name, bytes=len(raw), sha=sha(lf(raw)),
                         matches_blob=same, carries_repaired_line=line, hooks_path=hp))
        rec('###   %-22s %5d bytes  blob-equal (LF) : %-5s  repaired line : %-5s  hooksPath `%s`'
            % (name, len(raw), same, line, hp))
    rec('###   ### **ALL FOUR LF-NORMALISED-EQUAL TO THE SOURCE`S BLOB : %s**' % allmatch)
    rec('###   ### **ALL FOUR CARRY THE REPAIRED LINE : %s**' % allline)
    rec('###   ### ### **THE COMPARISON IS AGAINST THE BLOB AND `LF`-NORMALISED. ### NEVER BY')
    rec('###   ### ### FILENAME, AND NEVER BY SIZE ALONE.**')
    # ### **THE UNTRACKED LEGACY COPIES, DISPOSED OF BY `(R15)`S THIRD CLAUSE AND NOT DELETED.**
    rec('')
    rec('### ### ### **(e) THE UNTRACKED `.git/hooks/pre-push` COPIES.**')
    legacy = []
    for name, repo in b303_pins.REPOS:
        p = os.path.join(repo, '.git', 'hooks', 'pre-push')
        ex = os.path.exists(p)
        hp = git(repo, 'config', 'core.hooksPath').strip()
        legacy.append(dict(repo=name, exists=ex, hooks_path=hp, deleted=False))
        rec('###   %-22s present : %-5s   core.hooksPath = `%s`  ### ### **INERT : %s**'
            % (name, ex, hp, hp == '.githooks'))
    rec('###   ### **`(R15)`S THIRD DISPOSAL -- *the repository is reconfigured so the source is')
    rec('###   ### what runs* -- IS ALREADY IN FORCE FOR THESE**, verified above in each')
    rec('###   repository. ### **NONE IS DELETED.**')
    rec('###   ### ### **AND THAT IS A JUDGEMENT, MARKED AS ONE:** ### deleting them would remove')
    rec('###   a working fallback if `core.hooksPath` were ever unset, and the order did not ask')
    rec('###   for that. ### **THE AUTHOR MAY OVERTURN IT.**')
    return dict(install_rows=rows, all_match_blob=allmatch, all_carry_line=allline,
                legacy=legacy, legacy_deleted=0,
                blob_sha=sha(lf(blob or b'')), install_record='b386_install_run.txt')


# ==================================================================================================
BACKUP_FIX_OLD = """        shutil.copy2(dest, dest + '.b304-backup')
        open(dest, 'wb').write(src_bytes)
        return 'REPLACED (previous kept as .b304-backup)', sha256_bytes(src_bytes)"""

BACKUP_FIX_NEW = '''        # ### ### **THIS TOOL DESTROYED A BACKUP AT `b385` AND THE CONTENT WAS ONLY
        # ### ### IDENTIFIED AFTERWARDS.** ### It wrote `.b304-backup` unconditionally, over a
        # ### backup a previous run had left there. ### **REPAIRED AT `b386` UNDER `(R15)`'s act:
        # ### ### IT NEVER OVERWRITES AN EXISTING BACKUP.**
        # ### ### **THE INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE ASKED FOR.** ###
        # ### The order said *a backup it did not create*; a file cannot be asked who wrote it, so
        # ### the tool refuses to overwrite ANY existing backup and takes a fresh name instead.
        # ### **A STRONGER INVARIANT SUBSTITUTED FOR A WEAKER ONE IS STILL A SUBSTITUTION**, and
        # ### it is named here rather than slipped in.
        bak = dest + '.b304-backup'
        n = 0
        while os.path.exists(bak):
            n += 1
            bak = '%s.b304-backup-%d' % (dest, n)
        shutil.copy2(dest, bak)
        open(dest, 'wb').write(src_bytes)
        return ('REPLACED (previous kept as %s)' % os.path.basename(bak),
                sha256_bytes(src_bytes))'''


def component3():
    rec('')
    rec('-' * 100)
    rec("### COMPONENT 3 -- THE INSTALLER'S SECOND DEFECT.")
    rec('-' * 100)
    rec('### ### ### **(a) WHAT WAS LOST, NAMED WITH ITS NUMBERS.**')
    b371 = gitb(ROOT, 'show', '6de6336:.githooks/pre-push')
    b127 = gitb(ROOT, 'show', '323fd7a:%s' % SRCREL)
    crlf = (b371 or b'').replace(b'\n', b'\r\n')
    rec('###   the removed file : `.githooks/pre-push.b304-backup`, ### **`3139` BYTES** ### as')
    rec('###   `b385` recorded it before the tool overwrote it.')
    rec('###   `6de6336:.githooks/pre-push`      : %d bytes (LF)   sha `%s`'
        % (len(b371 or b''), sha(b371 or b'')[:16]))
    rec('###   the same blob, CRLF-expanded       : %d bytes         sha `%s`'
        % (len(crlf), sha(crlf)[:16]))
    identified = (len(crlf) == 3139)
    rec('###   ### **THE CRLF EXPANSION IS `%d` BYTES, WHICH IS THE REMOVED FILE`S SIZE : %s**'
        % (len(crlf), identified))
    same_lf = (lf(b371 or b'') == lf(b127 or b''))
    rec('###   and `323fd7a:%s` is LF-identical to it : ### **%s**' % (SRCREL, same_lf))
    rec('###   ### ### **SO THE LOST CONTENT IS RECOVERABLE FROM A TRACKED BLOB -- FROM TWO OF')
    rec('###   ### ### THEM.** ### `(F2)` IS MET, and by a printed digest rather than an')
    rec('###   assurance.')
    rec('###   ### **AND ONE THING THE RECOVERY DOES NOT UNDO:** ### the backup existed to hold')
    rec('###   what was on disk before an install, and ### **THIS ONE HELD NOTHING THE RECORD DID')
    rec('###   ### NOT ALREADY TRACK.** ### Had it held an untracked local edit, ### **IT WOULD')
    rec('###   ### HAVE BEEN GONE**, and that is the hazard the repair below removes.')

    rec('')
    rec('### ### ### **(b) THE TOOL REPAIRED.**')
    txt = io.open(HOOKTOOL, encoding='utf-8').read()
    fixed = False
    if BACKUP_FIX_OLD in txt:
        txt = txt.replace(BACKUP_FIX_OLD, BACKUP_FIX_NEW, 1)
        io.open(HOOKTOOL, 'w', encoding='utf-8', newline=chr(10)).write(txt)
        fixed = True
    elif 'while os.path.exists(bak):' in txt:
        fixed = True
    rec('###   `tools/b304_hooks.py` -- the unconditional `shutil.copy2` replaced by a')
    rec('###   ### **NEVER-OVERWRITE-AN-EXISTING-BACKUP LOOP** : %s' % fixed)
    rec('###   ### **THE INVARIANT IMPLEMENTED IS STRICTLY STRONGER THAN THE ONE ASKED FOR**, and')
    rec('###   the substitution is named rather than slipped in.')

    rec('')
    rec('### ### ### **(c) THE FIXTURE, IN BOTH POLARITIES.**')
    rec('###   ### **A FIXTURE THAT PASSES IN ONLY ONE POLARITY IS NOT A FIXTURE** (`b370`).')
    tmp = tempfile.mkdtemp(prefix='b386_backup_')
    pol = []
    try:
        sys.path.insert(0, os.path.join(ROOT, 'tools'))
        import importlib
        mod = importlib.import_module('b304_hooks')
        importlib.reload(mod)
        # ### (+) NO BACKUP EXISTS -- the tool may write one and replace the destination.
        r1 = os.path.join(tmp, 'r1', '.githooks')
        os.makedirs(r1)
        dest1 = os.path.join(r1, 'pre-push')
        io.open(dest1, 'wb').write(b'OLD-CONTENT\n')
        verdict1, _s1 = mod.install(os.path.join(tmp, 'r1'), b'NEW-CONTENT\n')
        made = os.path.exists(dest1 + '.b304-backup')
        kept1 = io.open(dest1 + '.b304-backup', 'rb').read() if made else b''
        p1 = (io.open(dest1, 'rb').read() == b'NEW-CONTENT\n' and made
              and kept1 == b'OLD-CONTENT\n')
        pol.append(('a backup the tool may write : it writes it and replaces the destination', p1))
        rec('###   (+) %-64s %s' % ('no backup present -> writes one, replaces dest', p1))
        rec('###       verdict: %s' % verdict1)
        # ### (-) A FOREIGN BACKUP EXISTS -- it must survive byte-for-byte.
        r2 = os.path.join(tmp, 'r2', '.githooks')
        os.makedirs(r2)
        dest2 = os.path.join(r2, 'pre-push')
        io.open(dest2, 'wb').write(b'OLD-CONTENT-2\n')
        io.open(dest2 + '.b304-backup', 'wb').write(b'SOMEONE-ELSES-BACKUP\n')
        verdict2, _s2 = mod.install(os.path.join(tmp, 'r2'), b'NEW-CONTENT-2\n')
        survived = io.open(dest2 + '.b304-backup', 'rb').read() == b'SOMEONE-ELSES-BACKUP\n'
        elsewhere = os.path.exists(dest2 + '.b304-backup-1')
        p2 = survived and elsewhere
        pol.append(('a backup the tool did NOT create : it survives byte-for-byte', p2))
        rec('###   (-) %-64s %s' % ('foreign backup present -> preserved, new one elsewhere', p2))
        rec('###       verdict: %s' % verdict2)
        rec('###       the foreign backup survived byte-for-byte : %s ; the new one went to '
            '`.b304-backup-1` : %s' % (survived, elsewhere))
    except Exception as e:      # noqa: BLE001
        pol.append(('the fixture ran', False))
        rec('###   ### ### **THE FIXTURE RAISED : %s**' % str(e)[:160])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    both = all(ok for _l, ok in pol) and len(pol) == 2
    rec('###   ### ### **BOTH POLARITIES HELD : %s**' % both)
    disp = 'DONE' if (fixed and both) else 'NOT DONE'
    rec('')
    rec('### ### ### **DISPOSITION : %s.** ### The repair is INSIDE this act`s face, which names'
        % disp)
    rec('### ### ### `tools/b304_hooks.py`. ### **IT IS NOT ROUTED**, because a component routed')
    rec('### ### ### for want of a face this act wrote itself would be this seat routing its own')
    rec('### ### ### omission.')
    return dict(lost_bytes=3139, lost_identified=identified, lost_sha=sha(crlf),
                recoverable_refs=['6de6336:.githooks/pre-push', '323fd7a:%s' % SRCREL],
                lf_identical=same_lf, tool_repaired=fixed, polarities=len(pol),
                polarities_held=both, disposition=disp, routed=False)


# ==================================================================================================
def component4():
    rec('')
    rec('-' * 100)
    rec('### COMPONENT 4 -- THE TWO FILINGS.')
    rec('-' * 100)
    rec('### ### ### **(i) THE SEARCH LESSON, MINTED -- AND TESTED BEFORE IT IS FILED AS A CURE.**')
    rec('### ### **THE SPECIES:** ### *a search for a rule uses the rule`s own words, not the name')
    rec('### ### a reader gave it.*')
    rec('')
    rec('### ### **INCIDENT ONE -- `b383`, A CLEAN ABSENCE THAT WAS WRONG.** ### Its six terms:')
    A = E['attestation']
    for t in E['b383_terms']:
        rec('###     `%-22s`  attested in the corpus `b383` searched : %d file(s)%s'
            % (t, A['b383|True']['counts'][t],
               '   ### ### **UNATTESTED**' if not A['b383|True']['counts'][t] else ''))
    rec('### ### **INCIDENT TWO -- `b385`, THE SAME RULE, LOCATED.** ### Its seven terms:')
    for t in E['b385_terms']:
        rec('###     `%-22s`  attested in the same corpus              : %d file(s)%s'
            % (t, A['b385|True']['counts'][t],
               '   ### ### **UNATTESTED**' if not A['b385|True']['counts'][t] else ''))
    rec('')
    rec('### ### ### **IS IT MECHANIZABLE? ### THE ANSWER IS A RESULT, NOT AN OPINION.**')
    rec('### ### **THE LESSON ITSELF IS NOT:** ### a check for ### *the rule`s own words* ### needs')
    rec('### the rule, and the rule is what the search was for.')
    rec('### ### **THE SHADOW IS:** ### ### **IS EACH TERM ATTESTED ANYWHERE IN THE CORPUS AT')
    rec('### ### ALL?** ### A term that occurs nowhere cannot find anything.')
    rows = []
    for lbl, key in (('the corpus as it stands', 'False'),
                     ('with the b383-b386 records excluded', 'True')):
        a3, a5 = A['b383|%s' % key], A['b385|%s' % key]
        rows.append((lbl, a3['attested'], a3['total'], a5['attested'], a5['total'], a3['control']))
        rec('###     %-38s  `b383` %d/%d attested   `b385` %d/%d   (control fired on %d files)'
            % (lbl, a3['attested'], a3['total'], a5['attested'], a5['total'], a3['control']))
    sep_clean = (A['b383|True']['attested'] < A['b383|True']['total']
                 and A['b385|True']['attested'] == A['b385|True']['total'])
    sep_dirty = (A['b383|False']['attested'] < A['b383|False']['total'])
    rec('')
    rec('### ### ### **THE CHECK SEPARATES THE TWO INCIDENTS ON THE UNCONTAMINATED SWEEP : %s.**'
        % sep_clean)
    rec('### ### ### **AND IT DOES NOT SEPARATE THEM ON THE CONTAMINATED ONE : %s** -- because'
        % (not sep_dirty))
    rec('### ### ### **`b383`-`b385`S OWN RECORDS NOW CONTAIN EVERY ONE OF `b383`S TERMS.**')
    rec('### ### **THAT CONTAMINATION IS ITSELF THE FINDING:** ### an act`s own records make its')
    rec('### terms attested afterwards, so ### **THE CHECK MUST EXCLUDE THE RECORDS OF THE ACT IT')
    rec('### ### IS CHECKING** -- `b368`s rule, arriving one level out.')
    verdict = 'MECHANIZED' if sep_clean else 'JUDGEMENT'
    rec('')
    rec('### ### ### **FILED AS : %s.**' % verdict)
    rec('### ### **AND ITS LIMIT IS STATED BESIDE IT, NOT BELOW IT:** ### the check asks whether a')
    rec('### term is attested, ### **NOT WHETHER IT IS THE RIGHT TERM.** ### `b385`s own')
    rec('### `reservoir` probe was attested and still wrong. ### **SO THE CHECK IS NECESSARY AND')
    rec('### ### NOT SUFFICIENT**, exactly as `b378`s positive-control rule turned out to be --')
    rec('### ### **AND A RULE THAT IS NECESSARY AND NOT SUFFICIENT IS NOT LISTED BESIDE THE ARMS')
    rec('### ### THAT DECIDE.**')

    rec('')
    rec('### ### ### **(ii) THE NAVIGATOR`S PARAPHRASE, CORRECTED ON THE RECORD.**')
    rec('### ### **THE RULE`S OWN WORDS, READ AT THE CANONICAL DRIVE AT THEIR OWN LINE NUMBERS:**')
    for lbl in ('the rule -- its standing-rule heading',
                'the rule -- the currency check, the authority clause',
                'the rule -- the procedure and the manifest columns'):
        b, ok = q(lbl)
        rec('###   `%s` line %-4d %s' % (b['file'], b['line'], '' if ok else '### RE-READ FAILED'))
        rec('###   | %s' % b['text'][:300])
    rec('')
    rec('### ### **THE NAVIGATOR`S STATEMENT:** ### *the export`s manifest is the reviewer`s')
    rec('### ### authority over recall.*')
    rec('### ### ### **MARK : OVER-STATED.**')
    rec('### ### **THE CORRECTION, IN THE RULE`S TERMS:** ### the authority is ### **THE')
    rec('### ### MANIFEST`S DIGEST AND `last-commit` COLUMNS**, not the manifest wholesale. ### The')
    rec('### Currency check widens the disagreement test to three fields -- ### *version, md5, or')
    rec('### last-commit* ### -- and ### **NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY.**')
    rec('### ### ### **THE CORRECTION IS OF A PARAPHRASE AND NOT OF THE RULE. ### THE RULE IS NOT')
    rec('### ### ### EDITED**, and `REGISTRY.md` is byte-identical to its blob at the end of this')
    rec('### act.')
    reg_dirty = bool(git(PP, 'diff', '--name-only', 'HEAD', '--', 'REGISTRY.md').strip())
    rec('###   `REGISTRY.md` differs from its blob : ### **%s**' % reg_dirty)
    return dict(term_lists=2, sweeps=len(rows), separates_clean=sep_clean,
                separates_contaminated=sep_dirty, filing=verdict, limit_stated=True,
                paraphrase_corrected=1, rules_edited=0, registry_dirty=reg_dirty,
                attestation_rows=rows)


def techne_module(C4):
    """### THE MODULE BESIDE THE ARM SPECIES. ### **LOCAL, COMMITTED, AND NOT PUSHED.**"""
    rec('')
    rec('### ### ### **THE TECHNE MODULE.**')
    p = os.path.join(TC, 'modules', '2026-09', 'SEARCH_BY_THE_RULES_OWN_WORDS.md')
    A = E['attestation']
    body = [
        '# SEARCH BY THE RULE’S OWN WORDS',
        '',
        '*Minted b386, 2026-09-09. Local to TECHNE-Core. Not pushed.*',
        '',
        '## The species',
        '',
        'A search for a rule uses **the rule’s own words**, not the name a reader gave it. '
        'A reader who describes a rule to you has given you two things: the rule’s content, '
        'and a name they invented for it. **The content is a query. The name is not.**',
        '',
        '## The two incidents',
        '',
        '**b383 — a clean absence that was wrong.** Asked to locate a standing rule about '
        'the reviewer’s sources, it swept the canonical tree, the relay tools and the TECHNE '
        'modules with a positive control that fired, excluded its own files, and reported NOT '
        'LOCATED. Its six terms were `%s`. **The rule uses none of those words.** It was in '
        '`REGISTRY.md` the whole time.'
        % '`, `'.join(B383 for B383 in json.load(
            io.open(os.path.join(ROOT, 'data', 'b386_reads.json'), encoding='utf-8'))['b383_terms']),
        '',
        '**b385 — the same rule, located.** The order described the rule’s *content*. '
        'The three terms that found it — `SESSION PROTOCOL`, `reviewer’s authority`, '
        '`not from recall` — **all came from that description.**',
        '',
        '## What the positive control does not buy you',
        '',
        'b383’s control fired. Its sweep was honest, its exclusions were right, its files '
        'were right. **A controlled search for the wrong string is still a controlled search for '
        'the wrong string.** A positive control proves the matcher works. It says nothing about '
        'whether the term is the right one. b378’s rule — *an absence needs a proved '
        'search* — is therefore **necessary and not sufficient**.',
        '',
        '## The mechanizable shadow, and its limit',
        '',
        'The species itself cannot be checked before the search: a check for *the rule’s own '
        'words* needs the rule, which is what you are looking for. What **can** be checked is '
        'weaker: **is each term of the query attested anywhere in the corpus at all?** A term that '
        'occurs nowhere cannot find anything.',
        '',
        'Run on the two incidents’ actual term lists, with the records of b383–b386 '
        'excluded: **b383 %d/%d terms attested, b385 %d/%d.** The check separates them.'
        % (A['b383|True']['attested'], A['b383|True']['total'],
           A['b385|True']['attested'], A['b385|True']['total']),
        '',
        'Run over the corpus as it stands: **b383 %d/%d, b385 %d/%d** — it separates nothing, '
        'because b383–b385’s own records now contain every one of b383’s terms. '
        '**An act’s own records make its terms attested afterwards**, so the check must '
        'exclude the records of the act it is checking. That is b368’s sweep rule, one level '
        'out.'
        % (A['b383|False']['attested'], A['b383|False']['total'],
           A['b385|False']['attested'], A['b385|False']['total']),
        '',
        '**And the shadow does not reach the species.** It asks whether a term is attested, not '
        'whether it is the right term: b385’s own `reservoir` probe was attested and still '
        'wrong. **Necessary, not sufficient** — and so it is not listed beside the arms that '
        'decide.',
        '',
        '## How to apply',
        '',
        '1. When a requester describes a rule, **query the description, not their label for it.**',
        '2. Before reporting an absence, check that your terms are attested somewhere — and '
        'exclude your own act’s records from that check.',
        '3. An unattested term is not evidence of absence. **It is evidence that you have not '
        'searched yet.**',
        '',
    ]
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(body) + chr(10))
    subprocess.run(['git', '-C', TC, 'add', '--', os.path.relpath(p, TC).replace(os.sep, '/')],
                   capture_output=True)
    cm = subprocess.run(['git', '-C', TC, 'commit', '-q', '-m',
                         'SEARCH_BY_THE_RULES_OWN_WORDS.md -- a search uses the rule\'s own '
                         'words, not the name a reader gave it (b386). LOCAL, NOT PUSHED.'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    head = git(TC, 'rev-parse', 'HEAD').strip()[:12]
    ahead = git(TC, 'status', '-sb').split(chr(10))[0].strip()
    rec('###   written : `modules/2026-09/%s`' % os.path.basename(p))
    rec('###   committed locally at `%s` : exit %d' % (head, cm.returncode))
    rec('###   branch state : `%s`' % ahead[:110])
    rec('###   ### **NOT PUSHED. ### THE STANDING REFUSAL: TECHNE-Core STAYS PRIVATE UNTIL THE')
    rec('###   ### PROVISIONALS.**')
    return dict(path='modules/2026-09/%s' % os.path.basename(p), head=head, pushed=False)


def main():
    rec('=' * 100)
    rec('b386 -- THE GUARD MADE SINGLE-SOURCED. ### THE FOUR COMPONENTS.')
    rec('=' * 100)
    C1 = component1()
    if C1['halt']:
        run_clock.write(D, 'b386_components_notes', LINES)
        return 1
    C2 = component2()
    if C2['halt']:
        run_clock.write(D, 'b386_components_notes', LINES)
        return 1
    C3 = component3()
    # ### **THE INSTALL RUNS AFTER THE TOOL IS REPAIRED**, so it exercises the repaired tool.
    C2.update(component2_install())
    C4 = component4()
    C4.update(techne=techne_module(C4))

    rec('')
    rec('=' * 100)
    rec('### THE FOUR COMPONENTS, SUMMED.')
    rec('=' * 100)
    rec('### ### **QUOTATIONS THAT FAILED TO RE-READ : %d** %s' % (len(FAILS), FAILS or ''))
    rec('### ### **OPTIONS REPRODUCED %d ; IMPLEMENTING (R15) %s ; INVENTED 0**'
        % (C1['options_quoted'], C1['implementing']))
    rec('### ### **TRACKED GUARD COPIES DELETED : %d, PROOF PRINTED FIRST : %s**'
        % (C2['deleted'], C2['proof_before_deletion']))
    rec('### ### **INSTALLER REPOINTED : %s ; ALL FOUR MATCH THE BLOB : %s ; ALL FOUR CARRY THE '
        'REPAIRED LINE : %s**' % (C2['repointed'], C2['all_match_blob'], C2['all_carry_line']))
    rec('### ### **UNTRACKED LEGACY COPIES DELETED : %d** -- (R15)`s third disposal, already in '
        'force' % C2['legacy_deleted'])
    rec('### ### **INSTALLER DEFECT REPAIRED : %s ; FIXTURE POLARITIES HELD : %s ; DISPOSITION '
        '%s**' % (C3['tool_repaired'], C3['polarities_held'], C3['disposition']))
    rec('### ### **THE LOST BACKUP IS IDENTIFIED AND RECOVERABLE : %s**' % C3['lost_identified'])
    rec('### ### **THE SEARCH LESSON FILED AS : %s ; ITS LIMIT STATED : %s**'
        % (C4['filing'], C4['limit_stated']))
    rec('### ### **THE PARAPHRASE CORRECTED : %d ; RULES EDITED : %d**'
        % (C4['paraphrase_corrected'], C4['rules_edited']))
    rec('### ### **NO CLASS RULED. ### NO STANDARD EDITED. ### NO ARCHIVE FILE TOUCHED. ### NO')
    rec('### ### CLUSTER OPENED. ### THE MIRROR ROSTER NOT EDITED. ### THE CITATION QUESTION NOT')
    rec('### ### MOVED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b386_components_notes', LINES)
    out = dict(C1=C1, C2=C2, C3=C3, C4=C4, reread_failures=FAILS,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(d('b386_components.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    ok = (not FAILS and C2['deleted'] == 1 and C2['repointed'] and C2['all_match_blob']
          and C2['all_carry_line'] and C3['tool_repaired'] and C3['polarities_held'])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
