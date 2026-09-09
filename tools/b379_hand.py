# -*- coding: utf-8 -*-
"""b379_hand.py -- THE DRAFT'S COMPONENT 3: ### **THE OTHER `NOT DETERMINABLE` DOCUMENT, BY HAND.**

### `b378` read `THE_LOAD_BEARING_MAP` by hand and left `A_Place_to_Stand` exactly as `b377` left it.
### The draft asked for the other one, and noted why it is the more interesting of the two:
### ### **IT IS THE DAY-1 DOCUMENT, AND IT IS THE ONE THE CORPUS'S OWN `CONCORDANCE-CARRIED` CLASS WAS
### ### INVENTED FOR** -- so the read is also a test of whether that class does any work.

### ### **THE UNIT IS A SENTENCE, NOT A CELL.** ### Every backticked identifier is taken with the
### sentence that names it, and the sentence is printed beside the verdict so a reader can disagree
### with the reading rather than with a number.
### ### **AND EVERY ABSENCE CARRIES A POSITIVE CONTROL** ### -- the standing clause, and `b378` paid
### for it. ### **AN ERROR EXIT IS RECORDED AS AN ERROR AND NEVER AS AN ANSWER.**

### ### **THE OUTCOME IS A MARK, NOT A CLASS.** ### No declaration is moved, no class is ruled, and
### ### **NOT ONE BYTE IS WRITTEN INTO THE DOCUMENT.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b378_terminals as T    # noqa: E402  ### THE BOTH-DIALECT MATCHER, IMPORTED UNMODIFIED
import row_categories as RC   # noqa: E402
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TICKED = re.compile(r'`([A-Za-z_][A-Za-z0-9_₀-₉\'!?]*(?:\.[A-Za-z_][A-Za-z0-9_₀-₉\'!?]*)*)`')
NOT_TERMINAL = re.compile(
    r'^(SIDE-|PLACE-|TECHNE)|^(np|numpy|scipy|os|sys|io|re|json|math)\.'
    r'|\.(md|py|lean|txt|json|toml|yml|yaml)$'
    r'|^(true|false|none|nil|Prop|Type|Sort|main|HEAD|README|AGENTS|FINDINGS|REGISTRY)$', re.I)
HAS_SHAPE = re.compile(r'_|\.')
CONCORDANCE = re.compile(r'\bKernel Concordance\b|\bconcordance\b', re.I)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def main():
    R = json.load(io.open(os.path.join(D, 'b377_branch.json'), encoding='utf-8'))
    H8 = json.load(io.open(os.path.join(D, 'b378_hand.json'), encoding='utf-8'))
    ND = R['not_determinable']
    done = H8['chosen']
    pick = [r for r in ND if r['file'] != done]
    if len(pick) != 1:
        rec('  ### ### **THE POPULATION IS NOT WHAT THIS TOOL EXPECTS. ### REFUSING.**')
        run_clock.write(D, 'b379_hand_notes', LINES)
        return 2
    pick = pick[0]
    rel = pick['file']
    path = os.path.join(PP, rel.replace('/', os.sep))
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    lines = txt.split(chr(10))

    rec('=' * 100)
    rec("b379 -- THE OTHER `NOT DETERMINABLE` DOCUMENT, READ BY HAND.")
    rec('=' * 100)
    rec('')
    rec('  ### **`b378` READ `%s` AND LEFT THIS ONE.**' % os.path.basename(done)[:-3])
    rec('  ### ### **CHOSEN : `%s`** ### -- by exclusion, not by preference: it is the one of the two'
        % rel)
    rec('  ### that has not been read.')
    rec('  ### **WHAT `b376` COULD NOT DECIDE:** ### %s.' % pick['could_not_decide'])
    rec('  ### **WHAT `b377` SAID WOULD DECIDE IT:** ### %s.' % pick['what_would_decide'])
    rec('  ### ### **AND THE DRAFT`S REASON FOR PICKING IT:** ### it is the day-1 document, and the')
    rec('  ### one the corpus`s own `CONCORDANCE-CARRIED` class was invented for. ### **SO THE READ IS')
    rec('  ### ### ALSO A TEST OF WHETHER THAT CLASS DOES ANY WORK.**')
    rec('')

    seen = {}
    for i, ln in enumerate(lines, 1):
        if not ln.strip():
            continue
        for m in TICKED.finditer(ln):
            nm = m.group(1)
            if NOT_TERMINAL.search(nm) or not HAS_SHAPE.search(nm):
                continue
            if nm not in seen:
                seen[nm] = (i, ln.strip())
    rec('-' * 100)
    rec('  ### THE HAND READ. ### **EVERY NAMED IDENTIFIER WITH THE SENTENCE THAT NAMES IT.**')
    rec('-' * 100)
    rec('    identifiers named : ### **%d**' % len(seen))
    conc = CONCORDANCE.search(txt)
    rec('    concordance language present in the document : ### **%s**' % bool(conc))
    rec('')

    NAMES = sorted(seen)
    if not NAMES:
        rec('    ### ### **THE DOCUMENT NAMES NO BACKTICKED IDENTIFIER OF TERMINAL SHAPE.**')
    LASTS = sorted(set(T.split(n)[1] for n in NAMES))
    alt = '|'.join(re.escape(x) for x in LASTS) if LASTS else 'zzz_no_names_zzz'
    gpat = T.LEAD_POSIX + T.KEYWORD_POSIX + r'[ \t]+(' + alt + r')\b'
    pername, gerrors = {}, []
    KS = T.kernels()
    for kn, kp in KS:
        by_sha, _n = T.refs_of(kp)
        for sha, refs in by_sha.items():
            r = git(kp, 'grep', '-n', '-E', gpat, sha)
            if r.returncode > 1:
                gerrors.append(dict(kernel=kn, sha=sha[:12], err=(r.stderr or '').strip()[:120]))
                continue
            if r.returncode != 0 or not r.stdout.strip():
                continue
            for ln in r.stdout.split(chr(10)):
                if not ln.strip() or ':' not in ln:
                    continue
                parts = ln.split(':', 3)
                if len(parts) < 4:
                    continue
                fp, code = parts[1], parts[3]
                body = None
                for nm in NAMES:
                    ns, last = T.split(nm)
                    if not T.decl_re(last).search(code):
                        continue
                    if ns is not None:
                        if body is None:
                            body = git(kp, 'show', sha + ':' + fp).stdout
                        if not T.declares(body, nm, fp):
                            continue
                    pername.setdefault(nm, []).append(dict(kernel=kn, path=fp, refs=refs))

    # ### **THE POSITIVE CONTROL. ### AN ABSENCE FROM A SEARCH THAT CANNOT RUN IS NOT AN ABSENCE.**
    ctrl = []
    for kn, kp in KS:
        by_sha, _n = T.refs_of(kp)
        for sha, _refs in by_sha.items():
            r = git(kp, 'grep', '-l', '-E',
                    T.LEAD_POSIX + T.KEYWORD_POSIX + r'[ \t]+residue_irreducible\b', sha)
            if r.returncode == 0 and r.stdout.strip():
                ctrl.append(kn)
    rec('    ### **POSITIVE CONTROL** ### -- `residue_irreducible` found on %d commit(s) : %s'
        % (len(ctrl), 'CONTROL HELD' if ctrl else '### CONTROL FAILED ###'))
    rec('    ### searches that could not run : %d ### **-- AN ERROR EXIT IS NOT AN ANSWER**'
        % len(gerrors))
    if not ctrl or gerrors:
        rec('    ### ### **REFUSING TO REPORT AN ABSENCE FROM A SEARCH THAT HAS NOT PROVED IT CAN')
        rec('    ### ### FIND A PRESENCE.**')
        run_clock.write(D, 'b379_hand_notes', LINES)
        return 2
    rec('')

    DOCS = RC.corpus_document_basenames(PP)
    rows = []
    for nm in NAMES:
        lineno, sent = seen[nm]
        hits = [dict(path=h['path'], refs=h['refs']) for h in pername.get(nm, [])]
        refs = sorted(set(r for h in pername.get(nm, []) for r in h['refs']))
        cat, why = RC.categorise(nm, hits, refs, sent, DOCS)
        kernels = sorted(set(h['kernel'] for h in pername.get(nm, [])))
        rows.append(dict(name=nm, line=lineno, sentence=sent[:300], category=cat, why=why,
                         kernels=kernels, n_kernels=len(kernels)))
        rec('    ### `%s` ### -- line %d' % (nm, lineno))
        rec('        the sentence that names it : %s' % sent[:132])
        rec('        ### ### **%s** ### -- %s' % (cat, why[:96]))

    tally = {}
    for r in rows:
        tally[r['category']] = tally.get(r['category'], 0) + 1
    located = sum(1 for r in rows if r['category'] in ('CORPUS_TERMINAL', 'ON_A_TAG_NOT_A_BRANCH'))
    notloc = tally.get('NOT_LOCATED', 0)
    rec('')
    rec('=' * 100)
    rec('  ### ### **THE HAND READ`S RESULT FOR `%s`:**' % os.path.basename(rel)[:-3])
    rec('  ###   identifiers named : %d' % len(rows))
    rec('  ###   ### **THE CATEGORIES : %s**' % tally)
    rec('  ###   ### **LOCATED IN A CORPUS KERNEL : %d ### / ### NOT LOCATED : %d**'
        % (located, notloc))
    decided = ('CARRIES APPARATUS' if located else
               'DOES NOT CARRY A LOCATABLE CORPUS TERMINAL AT THIS HEAD')
    rec('')
    rec('  ### ### ### **WHAT THE HAND READ DECIDES THAT THE TABLE SCAN COULD NOT:** ### the document')
    rec('  ### ### ### ### **%s.**' % decided)
    rec('  ### ### **AND WHAT IT SAYS ABOUT THE `CONCORDANCE-CARRIED` CLASS**, which the draft named as')
    rec('  ### ### the point of reading this one:')
    if conc:
        rec('  ###   the document does carry concordance language, so `b376`s `B?` was the right mark')
        rec('  ###   for a TABLE scan. ### **THE CLASS DESCRIBES SOMETHING REAL ON THIS PAGE.**')
    else:
        rec('  ###   ### **THE DOCUMENT CARRIES NO CONCORDANCE LANGUAGE AT THIS HEAD**, so the class')
        rec('  ###   the corpus invented for it is not doing work on this document now.')
    if located and notloc:
        rec('  ### ### **AND IT IS NOT A CLEAN ANSWER EITHER WAY:** ### some names locate and some do')
        rec('  ### ### not, which is the same shape `b378` found in the other document.')
    rec('  ### ### **WHAT IT STILL DOES NOT DECIDE:** ### whether the document`s SENTENCES about those')
    rec('  ### names are right. ### **LOCATING A NAME SAYS IT EXISTS AT THAT NAME.**')
    rec('  ### ### ### **THE OUTCOME IS A MARK, NOT A CLASS. ### NO DECLARATION WAS MOVED, NO CLASS')
    rec('  ### ### ### WAS RULED, AND NOT ONE BYTE WAS WRITTEN INTO THE DOCUMENT.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b379_hand_notes', LINES)
    io.open(os.path.join(D, 'b379_hand.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(chosen=rel, chosen_by='by exclusion -- the one of the two b378 did not read',
                        already_done=done, named=len(rows), categories=tally,
                        located=located, not_located=notloc, decided=decided,
                        concordance_language=bool(conc), control_held=bool(ctrl),
                        grep_errors=gerrors, rows=rows,
                        declaration_moved=False, class_ruled=False, bytes_written=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
