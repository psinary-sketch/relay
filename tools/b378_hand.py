# -*- coding: utf-8 -*-
"""b378_hand.py -- THE DRAFT'S COMPONENT 3: ### **ONE `NOT DETERMINABLE` DOCUMENT, READ BY HAND.**

### `b376` scored two `TIER K`-declaring documents ### **NOT DETERMINABLE** ### on the apparatus axis
### because they name their terminals in prose or under a concordance and its instrument scanned table
### rows. ### `b377` reported them and left them, and said what would decide them: ### **A HAND READ OF
### THE NAMING SENTENCES, ONE CLAIM AT A TIME, CHECKING EACH NAMED TERMINAL AT ITS KERNEL.**
### The draft said ### **DO ONE OF THE TWO**, and this file does one.

### ### **"BY HAND" MEANS THE UNIT IS A SENTENCE, NOT A CELL.** ### The document is read paragraph by
### paragraph; every backticked identifier is taken with ### **THE SENTENCE THAT NAMES IT**, and that
### sentence is printed beside the verdict so a reader can disagree with the reading rather than with a
### number.
### ### **THE OUTCOME IS A MARK, NOT A CLASS.** ### The draft says do not move the declaration either
### way, and ### **NO DECLARATION IS MOVED, NO CLASS IS RULED AND NO BYTE IS WRITTEN INTO THE
### ### DOCUMENT.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b378_terminals as T   # noqa: E402
import run_clock             # noqa: E402

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

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def sentences_with(lines):
    """### **EVERY NON-EMPTY LINE IS A SENTENCE UNIT**, because a markdown bullet or table row is one.
    ### The line number is carried so every verdict below points at a place in the file."""
    out = []
    for i, ln in enumerate(lines, 1):
        if ln.strip():
            out.append((i, ln))
    return out


def main():
    R = json.load(io.open(os.path.join(D, 'b377_branch.json'), encoding='utf-8'))
    ND = R['not_determinable']
    # ### **WHICH OF THE TWO, CHOSEN BY A STATED RULE AND NOT BY PREFERENCE:** ### the one `b377`
    # ### measured as the more bounded read -- fewer candidates is a smaller hand read, and the draft
    # ### asked for ONE worked case rather than the harder of two.
    pick = sorted(ND, key=lambda r: r['candidates'])[0]
    rel = pick['file']
    path = os.path.join(PP, rel.replace('/', os.sep))
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    lines = txt.split(chr(10))

    rec('=' * 100)
    rec("b378 -- THE DRAFT`S COMPONENT 3: ### **ONE `NOT DETERMINABLE` DOCUMENT, READ BY HAND.**")
    rec('=' * 100)
    rec('')
    rec('  ### the two `b376` could not decide, and what each carries:')
    for r in ND:
        rec('      %-42s backticked candidates : %-4d   real Correspondence headings : %d'
            % (os.path.basename(r['file'])[:-3][:42], r['candidates'], r['corr_headings']))
    rec('')
    rec('  ### ### **CHOSEN : `%s`** ### -- by a stated rule: ### **THE MORE BOUNDED READ**, since the'
        % rel)
    rec('  ### draft asked for one worked case and not for the harder of two. ### The other is')
    rec('  ### ### **LEFT EXACTLY AS `b377` LEFT IT** ### and this act makes no new claim about it.')
    rec('')
    rec('  ### **WHAT `b376` COULD NOT DECIDE, IN ITS OWN WORDS:** ### %s.' % pick['could_not_decide'])
    rec('  ### **WHAT `b377` SAID WOULD DECIDE IT:** ### %s.' % pick['what_would_decide'])
    rec('')

    # ---------------------------------------------------------------- THE HAND READ, SENTENCE BY SENTENCE
    rec('-' * 100)
    rec('  ### THE HAND READ. ### **EVERY NAMED IDENTIFIER WITH THE SENTENCE THAT NAMES IT.**')
    rec('-' * 100)
    seen, rows = {}, []
    for lineno, ln in sentences_with(lines):
        for m in TICKED.finditer(ln):
            nm = m.group(1)
            if NOT_TERMINAL.search(nm) or not HAS_SHAPE.search(nm):
                continue
            if nm in seen:
                continue
            seen[nm] = (lineno, ln.strip())
    rec('    identifiers named in the document, each with its first naming sentence : %d' % len(seen))
    rec('')

    # ### **ONE PASS PER TREE, NOT ONE PASS PER NAME.** ### Same search, same answer, affordable.
    NAMES = sorted(seen)
    LASTS = sorted(set(T.split(n)[1] for n in NAMES))
    alt = '|'.join(re.escape(x) for x in LASTS)
    gpat = T.LEAD_POSIX + T.KEYWORD_POSIX + r'[ \t]+(' + alt + r')\b'
    pername, gerrors = {}, []
    KS = T.kernels()
    for kn, kp in KS:
        by_sha, _names = T.refs_of(kp)
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
                body_txt = None
                for nm in NAMES:
                    ns, last = T.split(nm)
                    if not T.decl_re(last).search(code):
                        continue
                    if ns is not None:
                        if body_txt is None:
                            body_txt = git(kp, 'show', sha + ':' + fp).stdout
                        if not T.declares(body_txt, nm, fp):
                            continue
                    pername.setdefault(nm, []).append(
                        dict(kernel=kn, ref=refs[0], path=fp))

    # ### **THE POSITIVE CONTROL AGAIN.** ### An absence reported by a search that cannot run is not
    # ### an absence, and this act has already been bitten by exactly that once.
    ctrl = []
    for kn, kp in KS:
        by_sha, _n = T.refs_of(kp)
        for sha, refs in by_sha.items():
            r = git(kp, 'grep', '-l', '-E',
                    T.LEAD_POSIX + T.KEYWORD_POSIX + r'[ \t]+residue_irreducible\b', sha)
            if r.returncode == 0 and r.stdout.strip():
                ctrl.append(kn)
    rec('    ### **POSITIVE CONTROL** ### -- `residue_irreducible` found on %d commit(s) : %s'
        % (len(ctrl), 'CONTROL HELD' if ctrl else '### CONTROL FAILED ###'))
    rec('    ### searches that could not run : %d' % len(gerrors))
    if not ctrl or gerrors:
        rec('    ### ### **REFUSING TO REPORT AN ABSENCE FROM A SEARCH THAT HAS NOT PROVED IT CAN')
        rec('    ### ### FIND A PRESENCE.**')
        run_clock.write(D, 'b378_hand_notes', LINES)
        return 2
    rec('')

    for nm, (lineno, sent) in sorted(seen.items()):
        hits = pername.get(nm, [])
        kernels = sorted(set(h['kernel'] for h in hits))
        if len(kernels) == 1:
            verdict = 'LOCATED, IN EXACTLY ONE KERNEL'
            where = '%s @ %s (%s)' % (hits[0]['kernel'],
                                      hits[0]['ref'].replace('refs/heads/', ''), hits[0]['path'])
        elif len(kernels) > 1:
            verdict = '### **LOCATED IN MORE THAN ONE KERNEL**'
            where = 'declared in %d kernels : %s' % (len(kernels), ', '.join(kernels))
        else:
            verdict = '### **NOT LOCATED ON ANY REF**'
            where = 'no kernel on this disk declares it'
        rows.append(dict(name=nm, line=lineno, sentence=sent[:300], verdict=verdict, where=where,
                         kernels=kernels, hits=len(hits)))
        rec('    ### `%s` ### -- line %d' % (nm, lineno))
        rec('        the sentence that names it : %s' % sent.strip()[:150])
        rec('        ### ### **%s** ### -- %s' % (verdict, where))

    loc = [r for r in rows if r['verdict'].startswith('LOCATED')]
    amb = [r for r in rows if 'MORE THAN ONE' in r['verdict']]
    nf = [r for r in rows if 'NOT LOCATED' in r['verdict']]
    rec('')
    rec('=' * 100)
    rec('  ### ### **THE HAND READ`S RESULT FOR `%s`:**' % os.path.basename(rel)[:-3])
    rec('  ###   identifiers named        : %d' % len(rows))
    rec('  ###   LOCATED in exactly one kernel : ### **%d**' % len(loc))
    rec('  ###   located in more than one      : ### **%d**' % len(amb))
    rec('  ###   NOT located on any ref        : ### **%d**' % len(nf))
    decided = 'CARRIES THE APPARATUS' if loc and not nf else (
        'CARRIES SOME APPARATUS AND SOME NAMES DO NOT RESOLVE' if loc else
        'DOES NOT CARRY LOCATABLE TERMINALS')
    rec('')
    rec('  ### ### ### **WHAT THE HAND READ DECIDES THAT THE TABLE SCAN COULD NOT:** ### the document')
    rec('  ### ### ### ### **%s.**' % decided)
    rec('  ### ### **AND WHAT IT STILL DOES NOT DECIDE:** ### whether the document`s SENTENCES about')
    rec('  ### ### those terminals are right. ### **LOCATING A NAME SAYS IT EXISTS AT THAT NAME**, and')
    rec('  ### ### this read checked existence and not truth.')
    rec('  ### ### ### **THE OUTCOME IS A MARK, NOT A CLASS.** ### No declaration was moved, no class')
    rec('  ### ### ### was ruled, and ### **NOT ONE BYTE WAS WRITTEN INTO THE DOCUMENT.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b378_hand_notes', LINES)
    io.open(os.path.join(D, 'b378_hand.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(chosen=rel, chosen_by='the more bounded read, by candidate count',
                        other=[r['file'] for r in ND if r['file'] != rel],
                        named=len(rows), located=len(loc), ambiguous=len(amb), not_located=len(nf),
                        decided=decided, rows=rows, declaration_moved=False, class_ruled=False,
                        bytes_written=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
