# -*- coding: utf-8 -*-
"""b732_doors.py -- (R342)(4): THE PHASE 2 DOORS. THE RULE, THE OBJECTS IT NAMES, THE CONTROLS, EVERY SENTENCE GRADED IN b721'S VOCABULARY.

  python -X utf8 -u tools/b732_doors.py rule             the rule, printed before any kernel is named -> data/b732_objects_rule.txt
  python -X utf8 -u tools/b732_doors.py objects          the rule applied; the navigator's list beside it, choosing nothing -> data/b732_objects.txt
  python -X utf8 -u tools/b732_doors.py price            kernels times sentences, from the objects -> data/b732_doors_price.txt
  python -X utf8 -u tools/b732_doors.py read <kernel>    one remote read: the kernel's description and its main's oid -> data/b732_door_reads.json
  python -X utf8 -u tools/b732_doors.py ids <kernel>     every README sentence with its id; grades nothing, writes nothing
  python -X utf8 -u tools/b732_doors.py decls <kernel>   every declaration at the census pin with its E0 grade; writes nothing
  python -X utf8 -u tools/b732_doors.py controls         the three controls -> printed, and carried into the bank
  python -X utf8 -u tools/b732_doors.py bank             the controls, the statements, every sentence graded -> data/b732_phase2_doors.txt

The sentence grades are the seat's reading, by hand, against the statements quoted at the census pin (data/b732_door_grades.json), in b721's vocabulary
(tools/b721_frozen_line.py VOCAB, imported, unedited); E0 grades the statements (tools/e0_rule.py, unedited). Reads the kernels' clones by `git show`; writes
nothing in them. Written by the Write tool at b732.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
PP_PIN = '69eeba3'
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'
RULE_BANK = os.path.join(D, 'b732_objects_rule.txt')
OBJ_BANK = os.path.join(D, 'b732_objects.txt')
READS = os.path.join(D, 'b732_door_reads.json')
HAND = os.path.join(D, 'b732_door_grades.json')
OUT = os.path.join(D, 'b732_phase2_doors.txt')

PHASE2_ROWS = ('R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18')
RULE = [
    'b732 -- (R342)(4), N2: THE OBJECTS RULE, PRINTED BEFORE ANY KERNEL IS NAMED',
    '',
    '### THE RULE FOR THE KERNELS: read %s at PLACE-papers %s. Its section 1 files one row for each phase and cluster; the rows whose second column opens with a Phase 2 cluster are' % (CENSUS, PP_PIN),
    '### R11 (2A), R12 (2B), R13 (2C), R14 (2D), R15 (2E), R16 (2F), R17 (2G) and R18 (Phase 2, rows filed to no lettered cluster). Section 1A prints each repository with "the rows of section 1 naming it".',
    '### A KERNEL IS AN OBJECT WHEN AND ONLY WHEN ITS ROW IN SECTION 1A NAMES ONE OF THOSE EIGHT ROWS. Its clusters are the rows named. Nothing else admits or excludes a kernel: no list, no name, no reading of its README.',
    '### THE RULE FOR THE PIN: the commit section 1A prints as the current tag (`vX = abcdef0`); where it prints "no tag", the clone/remote main section 1A prints. Each statement is quoted there, not at HEAD.',
    '### THE RULE FOR THE README AND DESCRIPTION: the README of the kernel`s main at HEAD by `git show` from its clone, its main read against the remote`s by one read; the description by that one read.',
    '### THE RULE FOR THE DEPOSITS: the records of relay data/zenodo_listing_2026-09-14_author_screen.txt, the author`s own screen (8 records), each whose subject is a Phase 2 object: a kernel the rule above names, or a Phase 2 paper. Each read anonymously',
    '### by its record id at zenodo.org/api/records, in data/b726_zenodo_read.json`s form, the author`s name masked. A record of a Phase 1 paper or of a kernel the rule does not name stands outside the rule.',
    '### THE RULE FOR THE SYNTHESES: the sentences of the four syntheses p2-36, p2-37, p2-38, p2-41 and of the two companion rows the ruling names, p2-10 and p2-8, from the file`s first line to its first section heading, at PLACE-papers %s, each read against the kernels it names.' % PP_PIN,
    '### THE GRADES: data/b721_frozen_line.txt`s vocabulary, unedited; E0 (tools/e0_rule.py, unedited) grades the statements. The price and the stop by cluster are the price table`s.',
]
NAVIGATOR = ('SIDE-cosmo', 'SIDE-omega-b', 'SIDE-constants', 'SIDE-trivium', 'SIDE-structural-error-correction', 'SIDE-yang-mills-formation', 'SIDE-quaternionic-dark-sector',
             'SIDE-local-cosmic-interface', 'SIDE-dark-interface', 'SIDE-fano-darkness', 'SIDE-silence-principle', 'SIDE-compression', 'SIDE-formation-arithmetic', 'SIDE-coupling',
             'SIDE-class-coupling', 'SIDE-bsd-formation-transfer', 'SIDE-carrier-spec', 'SIDE-cubit-axis', 'SIDE-t7-topology-cmb', 'SIDE-substrate-cluster')
SYNTHESES = (('p2-36', 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md'), ('p2-37', 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_3.md'),
             ('p2-38', 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md'), ('p2-41', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'),
             ('p2-10', 'phase2/physics/STORMER.md'), ('p2-8', 'phase2/physics/COSMOLOGICAL_SIEVE_CEILING.md'))


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    p = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, encoding='utf-8', errors='replace')
    return p.stdout


def write(p, L):
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def census():
    return git(PP, 'show', '%s:%s' % (PP_PIN, CENSUS)).split(NL)


def objects():
    """the rule applied: [{kernel, pin, tagcell, rows}] from section 1A's table, in its order."""
    out = []
    t = census()
    start = next(i for i, l in enumerate(t) if l.startswith('| repository | main, clone / remote |'))
    for l in t[start + 2:]:
        if not l.startswith('|'):
            break
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        name, main, tag, rows = c[0], c[1], c[2], c[4]
        rs = [r for r in re.findall(r'R\d\d', rows) if r in PHASE2_ROWS]
        if not rs or not name.startswith('SIDE-'):
            continue
        m = re.search(r'=\s*([0-9a-f]{7})', tag)
        pin = m.group(1) if m else main.split('/')[-1].strip()
        out.append(dict(kernel=name, pin=pin, tagcell=tag, rows=rs, main=main))
    return out


def sentences(text):
    import b721_frozen_line as F
    return F.sentences(text)


def no_claim(s):
    import b721_frozen_line as F
    return F.no_claim(s)


def readme(k):
    r = 'D:/' + k
    return git(r, 'show', 'main:README.md')


DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|unsafe\s+|partial\s+)*(theorem|lemma|def|abbrev|structure|class|inductive|instance|axiom|opaque)\s+([^\s:({\[]+)?")


def lean_files(k, pin):
    r = 'D:/' + k
    fs = git(r, 'ls-tree', '-r', '--name-only', pin).split(NL)
    return [f for f in fs if f.endswith('.lean') and not f.startswith('.lake') and os.path.basename(f) not in ('lakefile.lean',)]


def decls(k, pin):
    """every top-level declaration at the pin: (file, line, kind, name, header to `:=` or ` where`)."""
    r = 'D:/' + k
    out = []
    for f in lean_files(k, pin):
        src = git(r, 'show', '%s:%s' % (pin, f)).replace(chr(13), '')
        lines = src.split(NL)
        depth = 0
        for i, l in enumerate(lines):
            # ### block comments skipped by depth; a declaration is read at the head of a line or indented in a namespace
            o, c = l.count('/-'), l.count('-/')
            before = depth
            depth = max(0, depth + o - c)
            if before > 0:
                continue
            m = DECL.match(l.strip())
            if not m:
                continue
            buf = []
            for x in lines[i:i + 14]:
                buf.append(x.strip())
                j = ' '.join(buf)
                if ':=' in j or re.search(r'\swhere\b', j) or (m.group(1) == 'inductive' and len(buf) > 1):
                    break
            j = ' '.join(buf)
            j = j[:j.index(':=')].strip() if ':=' in j else j[:220]
            out.append((f, i + 1, m.group(1), m.group(2) or '(anonymous)', j))
    return out


def e0_row(kind, name, head):
    import e0_rule as E0
    if kind not in ('theorem', 'lemma'):
        return kind.upper()
    try:
        return E0.grade(head[head.index(name) + len(name):], 'theorem')[0]
    except Exception as e:
        return 'E0 RAISED %s' % type(e).__name__


def cmd_rule(*a):
    L = RULE + ['', '### ### **THE RULE PRINTED %s ; NO KERNEL NAMED ABOVE ITS OWN RULE.**' % utc()]
    write(RULE_BANK, L)
    print(NL.join(L))


def cmd_objects(*a):
    if not os.path.exists(RULE_BANK):
        sys.exit('### THE RULE IS NOT BANKED -- NO KERNEL NAMED')
    O = objects()
    names = [o['kernel'] for o in O]
    L = ['b732 -- (R342)(4), N2: THE OBJECTS THE RULE NAMES (data/b732_objects_rule.txt), AND THE NAVIGATOR`S LIST BESIDE IT, CHOOSING NOTHING (%s)' % utc(), '',
         '## THE KERNELS THE RULE NAMES, IN SECTION 1A`S ORDER (the kernel | the pin | the census`s tag cell | the Phase 2 rows naming it | a clone at D:/)']
    for o in O:
        L.append('  %-34s %s | %-24s | %-22s | %s' % (o['kernel'], o['pin'], o['tagcell'][:24], ' '.join(o['rows']), 'CLONE' if os.path.isdir('D:/%s/.git' % o['kernel']) else '### ABSENT'))
    L += ['', '## THE NAVIGATOR`S LIST, BESIDE IT, CHOOSING NOTHING ((R342)(4)): in the rule`s list or not']
    for n in NAVIGATOR:
        L.append('  %-34s %s' % (n, 'NAMED BY THE RULE' if n in names else 'NOT NAMED BY THE RULE: section 1A prints no Phase 2 row for it (present at D:/: %s)' % os.path.isdir('D:/%s/.git' % n)))
    extra = [n for n in names if n not in NAVIGATOR]
    L += ['', '## NAMED BY THE RULE AND NOT THE NAVIGATOR`S: %s' % (', '.join(extra) or 'NONE'), '',
          '### ### **THE RULE NAMES %d KERNELS ; THE NAVIGATOR`S %d ; IN BOTH %d.**' % (len(names), len(NAVIGATOR), len([n for n in NAVIGATOR if n in names]))]
    write(OBJ_BANK, L)
    print(NL.join(L))


def cmd_price(*a):
    O = objects()
    L = ['b732 -- (R342)(4): THE DOORS PRICED, KERNELS TIMES SENTENCES, READ FROM THE OBJECTS (%s)' % utc(), '',
         '## kernel | clusters | README sentences graded by hand (less NO CLAIM by form) | README lines | declarations at the pin | theorems at the pin']
    tot = 0
    bycl = {}
    for o in O:
        k = o['kernel']
        rd = readme(k)
        S = [s for _i, s in sentences(rd)]
        hand = [s for s in S if not no_claim(s)]
        ds = decls(k, o['pin'])
        th = [d for d in ds if d[2] in ('theorem', 'lemma')]
        L.append('  %-34s %-20s %5d %6d %6d %6d' % (k, ' '.join(o['rows']), len(hand), len(rd.split(NL)), len(ds), len(th)))
        tot += len(hand)
        for r in o['rows']:
            bycl[r] = bycl.get(r, 0) + len(hand)
    L += ['', '## BY CLUSTER (a kernel counted under each row naming it): ' + ' ; '.join('%s %d' % (r, bycl[r]) for r in sorted(bycl)),
          '', '### ### **KERNELS %d ; README SENTENCES TO GRADE BY HAND %d.**' % (len(O), tot)]
    write(os.path.join(D, 'b732_doors_price.txt'), L)
    print(NL.join(L))


def cmd_read(k, *a):
    """one remote read: the description and main's oid in one GraphQL request, by gh's own authentication, no identifier of the author in it."""
    q = 'query{repository(owner:"psinary-sketch",name:"%s"){description isPrivate defaultBranchRef{target{oid}}}}' % k
    p = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=' + q], capture_output=True, encoding='utf-8', errors='replace')
    R = json.load(io.open(READS, encoding='utf-8')) if os.path.exists(READS) else {}
    if p.returncode:
        R[k] = dict(error=(p.stderr or '')[:200], read=utc())
    else:
        r = json.loads(p.stdout)['data']['repository']
        R[k] = dict(description=r.get('description'), private=r.get('isPrivate'), remote_main=(r.get('defaultBranchRef') or {}).get('target', {}).get('oid'), read=utc())
    R[k]['local_main'] = git('D:/' + k, 'rev-parse', 'main').strip()
    with open(READS + '.tmp', 'wb') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')
    os.replace(READS + '.tmp', READS)
    print(k, json.dumps(R[k], ensure_ascii=False))


def cmd_ids(k, *a):
    for sid, s in sentences(readme(k)):
        print('  %s %s| %s' % (sid, 'NC ' if no_claim(s) else '', '(the author line)' if 'orcid.org' in s else s))


def cmd_decls(k, *a):
    pin = next(o['pin'] for o in objects() if o['kernel'] == k)
    print('=====', k, 'at', pin)
    for f, n, kd, nm, h in decls(k, pin):
        if kd in ('instance',):
            continue
        print('  %s :%d %s | %s' % (f, n, e0_row(kd, nm, h), h[:230]))


if __name__ == '__main__':
    fn = {'rule': cmd_rule, 'objects': cmd_objects, 'price': cmd_price, 'read': cmd_read, 'ids': cmd_ids, 'decls': cmd_decls}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit(__doc__)
    fn(*sys.argv[2:])
