# -*- coding: utf-8 -*-
"""b462_components.py -- THE POPULATION APPLIED, AND THE CENSUS IN THREE BINS.

### ### **EVERY RULE HERE IS ON THE LOCKED FACE** -- the population and its two labelled substitutes,
### the nine proof words and the matcher bounds, the splitter, the bin rules, the resolution rule and
### the strength order. ### **NO ITEM IS GRADED AND NO TERMINAL IS NAMED FOR ANY ITEM.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
NL = chr(10)
L = []

sys.path.insert(0, T)
from b462_extract import items, PROOF, PW          # noqa: E402  ### THE SPLITTER AND MATCHER, IMPORTED

# ### THE STRENGTH ORDER, FIXED ON THE FACE BEFORE ANY ITEM WAS SEEN.
STRENGTH = ['machine-checked', 'proved', 'proven', 'proves', 'established',
            'establishes', 'verified', 'compiled', 'proof']
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|partial\s+)*'
                  r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)\s+'
                  r'([A-Za-z_][A-Za-z0-9_.\x27!?]*)')
IDENT = re.compile(r'`([^`\s]+)`')
CARRIER = re.compile(r'SIDE-[A-Za-z0-9-]+|\.lean\b|\.md\b|\bChapter\s+\d|\bSection\s+\d|\bPart\s+[IVX\d]'
                     r'|§\s*\d|\bRoute\s+\d|\bAppendix\b', re.I)
PINS = {'SIDE-kernel': 'v1.5', 'SIDE-lv-conservation': 'v0.10.0'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def build_index():
    """### **DECLARED NAMES ACROSS THE ROSTER, AT A PIN WHERE THE CORPUS NAMES ONE, ELSE AT HEAD.**
    ### The ref used is printed for every kernel, and a HEAD read is weaker and says so."""
    root = 'D:' + os.sep
    ks = sorted(n for n in os.listdir(root)
                if n.startswith('SIDE-') and os.path.isdir(os.path.join(root, n, '.git')))
    idx, per = {}, []
    for k in ks:
        repo = os.path.join(root, k)
        ref, how = PINS.get(k), 'PIN'
        if ref:
            if git(repo, 'rev-parse', '--verify', ref + '^{commit}').returncode != 0:
                ref, how = 'HEAD', 'HEAD (the pin does not resolve here)'
        else:
            ref, how = 'HEAD', 'HEAD'
        r = git(repo, 'grep', '-h', '-E',
                r'^\s*(@\[[^]]*\]\s*)?(private |protected |noncomputable |partial )*'
                r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom) ',
                ref, '--', '*.lean')
        n = 0
        for ln in r.stdout.split(NL):
            m = DECL.match(ln)
            if m:
                nm = m.group(2)
                idx.setdefault(nm.split('.')[-1], []).append((k, how, nm))
                n += 1
        dirty = len(git(repo, 'status', '--porcelain', '--untracked-files=no').stdout.strip().split(NL)) \
            if git(repo, 'status', '--porcelain', '--untracked-files=no').stdout.strip() else 0
        per.append(dict(kernel=k, ref=ref, how=how, declarations=n, tracked_dirty=dirty))
    return idx, per, ks


def surfaces():
    """### ELEVEN DEPOSIT FILES PLUS TWO LABELLED SUBSTITUTES. ### **THE LABEL TRAVELS WITH THEM.**"""
    out = []
    for f in sorted(os.listdir(DEP)):
        out.append((f, 'deposit file', read(os.path.join(DEP, f))))
    kz = git(os.path.join('D:', os.sep, 'SIDE-kernel'), 'show', 'v1.5:.zenodo.json').stdout
    out.append(('SIDE-kernel@v1.5:.zenodo.json description',
                'SUBSTITUTE -- not the Zenodo description, which is NOT BANKED',
                json.loads(kz).get('description', '') if kz.strip() else ''))
    lr = git(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'show', 'v0.10.0:README.md').stdout
    out.append(('SIDE-lv-conservation@v0.10.0:README.md',
                'SUBSTITUTE -- no .zenodo.json at the tag; the Zenodo description is NOT BANKED', lr))
    return out


def main():
    rec('=' * 110)
    rec('### COMPONENT 1 -- THE POPULATION AND THE PREDICATE, APPLIED.')
    rec('=' * 110)

    idx, per, ks = build_index()
    rec('  ### THE DECLARATION INDEX, BUILT BEFORE ANY ITEM IS BINNED.')
    rec('      kernels read : %d ; distinct declared short names : %d ; declarations : %d'
        % (len(ks), len(idx), sum(p['declarations'] for p in per)))
    pinned = [p for p in per if p['how'] == 'PIN']
    rec('      read AT A PIN : %d  (%s)' % (len(pinned), ', '.join('%s@%s' % (p['kernel'], p['ref'])
                                                                   for p in pinned) or 'none'))
    rec('      read AT HEAD  : %d   ### **WEAKER, AND IT SAYS SO** -- (R8): a head read dates the'
        % (len(per) - len(pinned)))
    rec('      ### check to today rather than to the pin the claim was made at.')
    dirty = [p for p in per if p['tracked_dirty']]
    rec('      kernels with tracked changes at the time of reading : %d %s'
        % (len(dirty), [p['kernel'] for p in dirty] or ''))
    ctl = 'structural_exhaustiveness_proved'
    rec('      ### ### **THE POSITIVE CONTROL: `%s` RESOLVES : %s**' % (ctl, ctl in idx))
    if ctl in idx:
        rec('          in %s' % ', '.join('%s (%s)' % (k, h) for k, h, _ in idx[ctl][:3]))
    if not idx or ctl not in idx:
        rec('  ### ### **HARD FAILURE: THE INDEX IS EMPTY OR THE CONTROL DOES NOT RESOLVE. THE CENSUS HALTS.**')
        raise SystemExit(2)
    rec('')

    surfs = surfaces()
    rec('  ### THE SURFACES, AND EVERY SUBSTITUTE CARRIES ITS LABEL.')
    allitems = []
    for name, label, text in surfs:
        it = items(text)
        for ln, kind, s, ws in it:
            allitems.append(dict(surface=name, label=label, line=ln, kind=kind, text=s, words=ws))
        rec('      %-46s %-12s %7d chars  items %4d' % (name[:46], label.split(' --')[0], len(text), len(it)))
    rec('      ### ### **TOTAL SENTENCE-ITEMS : %d.**' % len(allitems))
    bykind = {}
    for i in allitems:
        bykind[i['kind']] = bykind.get(i['kind'], 0) + 1
    rec('      by kind : ' + ' ; '.join('%s %d' % (k, bykind[k]) for k in sorted(bykind)))
    rec('      ### **HEADINGS AND TABLE ROWS ARE ITEMS BY THE RULE AND ARE NEVER HIDDEN IN A TOTAL.**')
    rec('')

    rec('=' * 110)
    rec('### COMPONENT 2 -- THE CENSUS, THREE BINS, NO GRADES.')
    rec('=' * 110)
    for i in allitems:
        cands = [c for c in IDENT.findall(i['text']) if re.search(r'[A-Za-z]', c)]
        hits = []
        for c in cands:
            short = re.sub(r'[^A-Za-z0-9_.\x27]', '', c).split('.')[-1]
            if short and short in idx:
                hits.append((c, idx[short][0][0], idx[short][0][1]))
        i['resolved'] = hits
        if hits:
            i['bin'] = 'NAMES A TERMINAL'
        elif CARRIER.search(i['text']):
            i['bin'] = 'NAMES A CARRIER'
        else:
            i['bin'] = 'NAMES NOTHING'

    BINS = ('NAMES A TERMINAL', 'NAMES A CARRIER', 'NAMES NOTHING')
    rec('  %-46s %8s %8s %8s %8s' % ('surface', 'TERMINAL', 'CARRIER', 'NOTHING', 'items'))
    rec('  ' + '-' * 88)
    for name, label, _t in surfs:
        sub = [i for i in allitems if i['surface'] == name]
        c = [sum(1 for i in sub if i['bin'] == b) for b in BINS]
        rec('  %-46s %8d %8d %8d %8d' % (name[:46], c[0], c[1], c[2], len(sub)))
    tot = [sum(1 for i in allitems if i['bin'] == b) for b in BINS]
    rec('  ' + '-' * 88)
    rec('  %-46s %8d %8d %8d %8d' % ('TOTAL', tot[0], tot[1], tot[2], len(allitems)))
    rec('  ### bins sum to items : %s' % (sum(tot) == len(allitems)))
    rec('')
    rec('  ### THE THREE BINS BY KIND:')
    for b in BINS:
        bk = {}
        for i in allitems:
            if i['bin'] == b:
                bk[i['kind']] = bk.get(i['kind'], 0) + 1
        rec('      %-18s %s' % (b, ' ; '.join('%s %d' % (k, bk[k]) for k in sorted(bk)) or 'none'))
    rec('')

    mono = [i for i in allitems if i['surface'] == 'A_Place_to_Stand.md' and i['bin'] == 'NAMES NOTHING']
    rec('  ### `NAMES NOTHING` in the monograph : %d of %d  (%.1f%%)'
        % (len(mono), tot[2], 100.0 * len(mono) / tot[2] if tot[2] else 0))
    mc = [i for i in allitems if 'machine-checked' in i['words'] and i['bin'] != 'NAMES A TERMINAL']
    mcn = [i for i in allitems if 'machine-checked' in i['words'] and i['bin'] == 'NAMES NOTHING']
    rec('  ### ### **ITEMS SAYING `machine-checked` THAT NAME NO TERMINAL : %d** (of which `NAMES NOTHING` : %d)'
        % (len(mc), len(mcn)))
    neg = [i for i in allitems if re.search(r'unprove|disprove|not proved|no proof', i['text'], re.I)]
    rec('  ### items also carrying a negated proof word (counted, not dropped) : %d' % len(neg))
    rec('')

    rec('  ### ### **THE TWENTY `NAMES NOTHING` ITEMS WITH THE STRONGEST PROOF WORDS, VERBATIM.**')
    rec('  ### the strength order was fixed on the face before any item was seen.')
    nn = sorted([i for i in allitems if i['bin'] == 'NAMES NOTHING'],
                key=lambda i: (min(STRENGTH.index(w) for w in i['words'] if w in STRENGTH),
                               i['surface'], i['line']))
    for k, i in enumerate(nn[:20], 1):
        rec('   %2d) %s:%d [%s] <%s>' % (k, i['surface'], i['line'], i['kind'], ','.join(i['words'])))
        rec('       %s' % i['text'][:230])
    rec('')
    rec('  ### **NO ITEM ABOVE IS GRADED.** ### `NAMES NOTHING` says the sentence names no terminal.')
    rec('  ### It says nothing about whether the sentence is true, whether a terminal exists that would')
    rec('  ### carry it, or whether the deposit is wrong. ### **THIS ACT NAMES NO TERMINAL FOR ANY OF THEM.**')
    rec('=' * 110)

    json.dump(dict(index_names=len(idx), index_decls=sum(p['declarations'] for p in per),
                   per_kernel=per, control_resolves=ctl in idx),
              io.open(os.path.join(D, 'b462_index.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(dict(total=len(allitems), by_bin=dict(zip(BINS, tot)), by_kind=bykind,
                   per_surface=[dict(surface=n, label=l,
                                     items=sum(1 for i in allitems if i['surface'] == n),
                                     **{b: sum(1 for i in allitems if i['surface'] == n and i['bin'] == b)
                                        for b in BINS})
                                for n, l, _ in surfs],
                   mono_nothing=len(mono), machine_checked_no_terminal=len(mc),
                   machine_checked_nothing=len(mcn), negated=len(neg),
                   top20=[dict(surface=i['surface'], line=i['line'], kind=i['kind'],
                               words=i['words'], text=i['text']) for i in nn[:20]]),
              io.open(os.path.join(D, 'b462_census.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    io.open(os.path.join(D, 'b462_census.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b462_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
