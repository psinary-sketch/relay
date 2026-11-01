# -*- coding: utf-8 -*-
"""b732_doors.py -- (R342)(4): THE PHASE 2 DOORS. THE RULE, THE OBJECTS IT NAMES, THE CONTROLS, EVERY SENTENCE GRADED IN b721'S VOCABULARY.

  python -X utf8 -u tools/b732_doors.py rule             the rule, printed before any kernel is named -> data/b732_objects_rule.txt
  python -X utf8 -u tools/b732_doors.py objects          the rule applied; the navigator's list beside it, choosing nothing -> data/b732_objects.txt
  python -X utf8 -u tools/b732_doors.py price            kernels times sentences, from the objects -> data/b732_doors_price.txt
  python -X utf8 -u tools/b732_doors.py read <kernel>    one remote read: the kernel's description and its main's oid -> data/b732_door_reads.json
  python -X utf8 -u tools/b732_doors.py ids <kernel>     every README sentence with its id; grades nothing, writes nothing
  python -X utf8 -u tools/b732_doors.py decls <kernel>   every declaration at the census pin with its E0 grade; writes nothing
  python -X utf8 -u tools/b732_doors.py controls         the three controls, before any sentence -> data/b732_door_controls.txt; ids, decls, heads and deps refuse without it
  python -X utf8 -u tools/b732_doors.py zenodo [dry|bank]  the rule's deposits read anonymously -> data/b732_zenodo_read.json
  python -X utf8 -u tools/b732_doors.py heads | deps     the synthesis heads, the deposit descriptions, each sentence with its id; grades nothing, writes nothing
  python -X utf8 -u tools/b732_doors.py gather <dir>     the seats' proposals and the seat's rows -> data/b732_door_grades.json
  python -X utf8 -u tools/b732_doors.py exrows [<kernel>]  every EXCEEDS row, for the hand read; writes nothing
  python -X utf8 -u tools/b732_doors.py bank             every sentence graded, tallied and classed -> data/b732_phase2_doors.txt, data/b732_door_classes.json

The sentence grades are the seat's reading, by hand, against the statements quoted at the census pin (data/b732_door_grades.json), in b721's vocabulary
(tools/b721_frozen_line.py VOCAB, imported, unedited); E0 grades the statements (tools/e0_rule.py, unedited). Reads the kernels' clones by `git show`; writes
nothing in them. Written by the Write tool at b732.
"""
import collections
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
CTL_BANK = os.path.join(D, 'b732_door_controls.txt')
CLASS_HAND = os.path.join(D, 'b732_door_class_hand.json')
ZEN = os.path.join(D, 'b732_zenodo_read.json')
DEPOSITS = (('T7', '21436282'), ('SIDE-cosmo', '19938009'), ('SIDE-effects', None), ('SIDE-trivium', '19938003'), ('SIDE-interfaces', '19931797'), ('SIDE-kernel', '21520474'))

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
    if p.returncode:
        row = dict(error=(p.stderr or '')[:200], read=utc())
    else:
        r = json.loads(p.stdout)['data']['repository']
        row = dict(description=r.get('description'), private=r.get('isPrivate'), remote_main=(r.get('defaultBranchRef') or {}).get('target', {}).get('oid'), read=utc())
    row['local_main'] = git('D:/' + k, 'rev-parse', 'main').strip()
    os.makedirs(a[0], exist_ok=True)
    with open(os.path.join(a[0], k + '.json'), 'wb') as fh:      # ### one file a kernel, each read its own command; `merge` banks them
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True).encode('utf-8'))
    print(k, json.dumps(row, ensure_ascii=False))


def cmd_merge(d, *a):
    """the reads of `read <kernel> <dir>` into data/b732_door_reads.json, every kernel the rule names or none."""
    R = {}
    for o in objects():
        R[o['kernel']] = json.load(io.open(os.path.join(d, o['kernel'] + '.json'), encoding='utf-8'))
    with open(READS + '.tmp', 'wb') as fh:
        fh.write(json.dumps(R, indent=1, ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')
    os.replace(READS + '.tmp', READS)
    print('kernels', len(R), 'main equal to the remote', sum(1 for v in R.values() if v.get('remote_main') == v.get('local_main')), 'private', [k for k, v in R.items() if v.get('private')], 'errors', [k for k, v in R.items() if v.get('error')])


def controls():
    """the three controls of (R342)(4), b721's (C1)-(C3) at this act's objects: [lines], all as wanted."""
    import e0_rule as E0
    st = E0.self_test()
    c1 = st[0] if isinstance(st, tuple) else st
    plant = E0.grade('(h : RiemannHypothesis) (s : ℂ) : s.re = 1 / 2', 'theorem')[0]
    k, pin, name = 'SIDE-cosmo', next(o['pin'] for o in objects() if o['kernel'] == 'SIDE-cosmo'), 'archimedean_forces_half'
    yes = next(d for d in decls(k, pin) if d[2] in ('theorem', 'lemma'))[3]
    grep = lambda n: len([l for l in git('D:/' + k, 'grep', '-n', '-E', r'^\s*(theorem|lemma)\s+%s\b' % re.escape(n), pin, '--', '*.lean').split(NL) if l])   # noqa: E731
    L = ['  (C1) E0`s own self-test (e0_rule.self_test, both polarities): %s -- %s' % ('PASSES' if c1 else 'FAILS', 'AS WANTED' if c1 else 'NOT AS WANTED'),
         '  (C2) PLANT: a header with a premise binder (h : RiemannHypothesis) grades %s -- %s' % (plant, 'AS WANTED' if plant == 'INTERFACES' else 'NOT AS WANTED'),
         '  (C3) NEG: %s sought in %s at %s: yield %d -- %s ; beside it, the same search for %s, declared there: yield %d -- %s' % (
             name, k, pin, grep(name), 'ABSENT, AS WANTED' if grep(name) == 0 else 'NOT AS WANTED', yes, grep(yes), 'FOUND, AS WANTED' if grep(yes) >= 1 else 'NOT AS WANTED')]
    return L, not any('NOT AS WANTED' in l for l in L)


def cmd_controls(*a):
    L, ok = controls()
    write(CTL_BANK, ['b732 -- (R342)(4): THE CONTROLS, BEFORE ANY SENTENCE IS READ FOR A GRADE (%s)' % utc(), ''] + L + ['', '### ### **CONTROLS %s.**' % ('ALL AS WANTED' if ok else 'NOT ALL AS WANTED')])
    print(NL.join(L))
    if not ok:
        sys.exit('### A CONTROL MISSED -- NO SENTENCE GRADED')


def need_controls():
    if not os.path.exists(CTL_BANK) or 'ALL AS WANTED.**' not in io.open(CTL_BANK, encoding='utf-8').read():
        sys.exit('### THE CONTROLS ARE NOT BANKED -- NO SENTENCE PRINTED ((R342)(4), N2)')


def cmd_ids(k, *a):
    need_controls()
    for sid, s in sentences(readme(k)):
        print('  %s %s| %s' % (sid, 'NC ' if no_claim(s) else '', '(the author line)' if 'orcid.org' in s else s))


ORCID = re.compile(r'\d{4}-\d{4}-\d{4}-\d{3}[\dX]')   # ### the author's identifier is not banked; found in the first read, masked before any commit


def strip_html(s):
    return re.sub(r'[ \t]+', ' ', re.sub(r'&[a-z]+;', ' ', re.sub(r'<[^>]+>', NL, s or '')))


def cmd_zenodo(mode='dry', *a):
    """every Phase 2 record the rule names, anonymously: no token, no identity in any header, one GET a record, one search by the kernel's name where no id is banked; the author's name masked, the bank refusing an identifier."""
    import urllib.parse
    import urllib.request
    import b732_address_scan as SC
    def fetch(u):
        with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'relay-read', 'Accept': 'application/json'}), timeout=60) as f:
            return json.loads(f.read().decode('utf-8'))
    name, user, addr = SC.author_name(), SC.previous_username(), SC.previous_address()
    out = []
    for subj, rid in DEPOSITS:
        time.sleep(2)
        if rid is None:
            h = fetch('https://zenodo.org/api/records?' + urllib.parse.urlencode({'q': 'title:"Verification of nine framework consequences"', 'size': 25})).get('hits', {}).get('hits', [])
            h = [x for x in h if (x.get('metadata', {}).get('title') or '').startswith(subj)]   # ### the case kept: a stranger's "side-effects" record met the first cut, a case-blind match
            if not h:
                out.append(dict(subject=subj, id=None, how='search by the kernel`s name, no hit whose title names it'))
                print('##', subj, 'NO RECORD FOUND BY THE SEARCH')
                continue
            o, how = h[0], 'search by the kernel`s name'
        else:
            o, how = fetch('https://zenodo.org/api/records/' + rid), 'the record id'
        m = o.get('metadata', {})
        row = dict(subject=subj, id=str(o.get('id')), how=how, doi=o.get('doi'), masked=0)
        for k in ('title', 'version', 'publication_date', 'description', 'notes'):
            s = m.get(k)
            if isinstance(s, str):
                row['masked'] += s.count(name) + len(ORCID.findall(s))
                row[k] = ORCID.sub('[the identifier]', s.replace(name, '[the author]'))
        out.append(row)
        print('## %s %s v%s %s | %s (masked %d)' % (subj, row['id'], row.get('version'), row.get('publication_date'), row.get('title'), row['masked']))
    t = json.dumps(dict(read_utc=utc(), rows=out), indent=1, ensure_ascii=False) + NL
    if SC.count(t, name) or SC.count(t, user) or SC.count(t, addr):
        sys.exit('### AN IDENTIFIER SURVIVES THE MASK -- NOTHING WRITTEN')
    if mode == 'bank':
        with open(ZEN + '.tmp', 'wb') as f:
            f.write(t.encode('utf-8'))
        os.replace(ZEN + '.tmp', ZEN)
        print('written data/b732_zenodo_read.json')


def deposit_sentences(row):
    out = []
    paras = []
    for p in [x.strip() for x in strip_html(row.get('description')).split(NL) if x.strip()]:
        # ### three May records hard-break their sentences at <br>: a line opening lower-case, or following one that ends mid-phrase, continues it
        if paras and (p[0].islower() or re.search(r'(?: in| of| the| and| from| /)$', paras[-1])):
            paras[-1] += ' ' + p
        else:
            paras.append(p)
    for n, para in enumerate(paras, 1):
        for j, s in enumerate([x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z`*(])', para) if x.strip()], 1):
            out.append(('%d.%d' % (n, j), s))
    return out


AUTHOR_MARK = '(the author line)'


def head_sentences(path):
    """the file's sentences from its first line to its first section heading: the title line kept, a subtitle heading with nothing between it and the title kept,
    the next heading the stop. the author line never leaves this function: it is replaced at the line, before the sentence split, which cuts at an initial."""
    t = git(PP, 'show', '%s:%s' % (PP_PIN, path)).replace(chr(13), '').split(NL)
    keep, seen, body = [], 0, False
    for l in t:
        if l.startswith('#'):
            if seen and (body or seen == 2):
                break
            seen += 1
        elif seen and l.strip() and l.strip() != '---':
            body = True
        keep.append(AUTHOR_MARK if l.startswith('**J.') or 'orcid' in l.lower() else l)
    return sentences(NL.join(keep))


def cmd_heads(*a):
    need_controls()
    for k, p in SYNTHESES:
        print('=====', k, p, 'PRESENT' if git(PP, 'ls-tree', PP_PIN, '--', p).strip() else '### ABSENT AT THE PIN')
        for sid, s in head_sentences(p):
            print('  %s %s| %s' % (sid, 'NC ' if no_claim(s) or s == AUTHOR_MARK else '', s))


def cmd_deps(*a):
    need_controls()
    for r in json.load(io.open(ZEN, encoding='utf-8'))['rows']:
        print('=====', r['subject'], r.get('id'), r.get('version'), '|', r.get('title'))
        for sid, s in deposit_sentences(r):
            print('  %s | %s' % (sid, s))


def units():
    """every graded row of the act, in the bank's order: (group, row, key, id, text, cluster rows). group is README | DESCRIPTION | DEPOSIT | HEAD."""
    out = []
    R = json.load(io.open(READS, encoding='utf-8'))
    for o in objects():
        k = o['kernel']
        for sid, s in sentences(readme(k)):
            if not no_claim(s):
                out.append(('README', k, k, sid, s, o['rows']))
        if R[k].get('description'):
            out.append(('DESCRIPTION', k, k, 'description', R[k]['description'], o['rows']))
    for r in json.load(io.open(ZEN, encoding='utf-8'))['rows']:
        for sid, s in deposit_sentences(r):
            out.append(('DEPOSIT', r['subject'], 'dep:%s' % r['id'], sid, s, CLUSTER_OF_DEP.get(r['subject'], ())))
    for k, p in SYNTHESES:
        for sid, s in head_sentences(p):
            if not (no_claim(s) or s == AUTHOR_MARK or s.strip() == '---'):
                out.append(('HEAD', k, k, sid, s, CLUSTER_OF_HEAD[k]))
    return out


CLUSTER_OF_HEAD = dict([('p2-36', ('R12',)), ('p2-37', ('R14',)), ('p2-38', ('R16',)), ('p2-41', ('R13',)), ('p2-10', ('R14',)), ('p2-8', ('R14',))])
CLUSTER_OF_DEP = dict([('T7', ('R15',)), ('SIDE-cosmo', ('R14', 'R15')), ('SIDE-effects', ('R13', 'R14')), ('SIDE-trivium', ('R15',)), ('SIDE-interfaces', ('R12', 'R13')), ('SIDE-kernel', ('R13',))])
DF_MAX = 8
GRADES = ('STATED', 'EXCEEDS', 'OUTSIDE', 'SCOPE', 'NO CLAIM')
FINDINGS_READ = [
    'SIDE-kernel README 3.1 at main still reads a formalization of the SIDE proof of the Riemann Hypothesis, and 55.1 that `lake build` verifies the theorem; the pin carries no unconditional term of RiemannHypothesis (SEAT: the deposit`s note, ERRATA E-2026-09-25-1). The default target `lean_lib Kernel` does not reach Bridge/ (README 30.1, graded NO CLAIM as a build line).',
    'SIDE-effects at the pin: three sorry (SEAT, Milestones.lean :39 :61 :80), the nine skeletons standing; the README says retired.',
    'SIDE-cosmo and SIDE-trivium at the pin close by native_decide; main dropped it. README `0 axioms` and p2-10`s {propext, Quot.sound} hold at main and not at the pin (SEAT, FormationPhaseSpace.lean :59-:70).',
    'SIDE-yang-mills-formation README 72.1 says 0.13 sigma where the record encodes exclusion_sigma_x10 := 13, 1.3 sigma on the field`s stated scale, its comment saying 0.13 (SEAT, Basic.lean :226, :238): the source disagrees with itself; [[8,1,5]] fails the quantum Singleton bound as a quantum code (SEAT, 7 >= 8 false).',
    'The Planck error bar: 0.00059 (SIDE-cosmo, b726 [20]), 0.00066 (SIDE-omega-b, p2-10), 0.0031 (the SIDE-cosmo record): three figures for one citation (SEAT).',
    'SIDE-silence-principle: B, C and E of the six consequences were removed at the pin as vacuous (section 7 note), and the README still lists them. SIDE-bsd and SIDE-yang-mills: the SCAFFOLDING banner withdraws what sentences below it assert.',
    'SIDE-trivium: all_discriminants_squarefree reduces to True; SIDE-coupling, SIDE-meta, SIDE-bijection, SIDE-compression and SIDE-dark-interface each have a headline theorem that restates its hypothesis, a field or a reflexivity.',
    'SIDE-dark-interface 34.3 contradicts its own table (kappa_x100 .validity .formal_subset_of_NL = 50). SIDE-class-coupling`s Framework.lean is not the re-implementation it says, the same names on different structures. SIDE-cubit-axis imports no sibling, so nothing it says of siblings can fire.',
    'Mechanism-class numbering differs between SIDE-trivium (C2 Euler, C6 Cauchy-Riemann) and SIDE-bsd-formation-transfer (C2 reality, C3 cauchy_riemann, C4 balance).',
]
PRIVATE = ('SIDE-constants',)


def digest(s):
    import hashlib
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


def grade_of(H, key, sid):
    if key in H and sid == 'description':
        return H[key].get('description')
    if key in H and 'readme' in H[key]:
        return H[key]['readme'].get(sid)
    return H.get(key, {}).get(sid)


def cmd_gather(d, *a):
    """the proposals of the grading seats, one file a kernel, and the seat's own rows and corrections (a JSON beside them, seat.json), into data/b732_door_grades.json."""
    H = {}
    for o in objects():
        H[o['kernel']] = json.load(io.open(os.path.join(d, o['kernel'] + '.json'), encoding='utf-8'))
    seat = json.load(io.open(os.path.join(d, 'seat.json'), encoding='utf-8'))
    for key, rows in seat.get('rows', {}).items():
        H.setdefault(key, {}).update(rows)
    n = 0
    for key, rows in seat.get('corrections', {}).items():
        for sid, row in rows.items():
            if sid == 'description':
                H[key]['description'] = row
            else:
                H[key]['readme'][sid] = row
            n += 1
    for k in PRIVATE:      # ### the relay is public: the private kernel's notes leave the scratchpad by digest alone
        for sid, r in H[k]['readme'].items():
            r[1] = 'private; sha256 ' + digest(r[1])
    with open(HAND + '.tmp', 'wb') as fh:
        fh.write(json.dumps(H, indent=0, ensure_ascii=False, sort_keys=True).encode('utf-8') + b'\n')
    os.replace(HAND + '.tmp', HAND)
    U = units()
    miss = [(u[2], u[3]) for u in U if not grade_of(H, u[2], u[3])]
    bad = [(u[2], u[3]) for u in U if grade_of(H, u[2], u[3]) and grade_of(H, u[2], u[3])[0] not in GRADES]
    print('units', len(U), 'missing', len(miss), miss[:30], 'bad grade', bad[:10], 'corrections', n)


def cmd_exrows(k=None, *a):
    """every EXCEEDS row with its sentence and its note, for the seat's hand read; prints to the screen, writes nothing."""
    H = json.load(io.open(HAND, encoding='utf-8'))
    n = 0
    for g, row, key, sid, s, cl in units():
        r = grade_of(H, key, sid)
        if r and r[0] == 'EXCEEDS' and (k is None or row == k):
            n += 1
            print('[%s %s] %s' % (row, sid, s[:600]))
            print('     -> %s' % r[1][:500])
    print('rows', n)


def classing(U, H):
    """W-ORD-SILENT-SENTENCES over the EXCEEDS rows, b726's sweep imported unedited: the corpus adds this act's six records; a row's own document is out of its own sweep."""
    import b726_frontdoors as F
    rows = F.corpus()
    for z in json.load(io.open(ZEN, encoding='utf-8'))['rows']:
        rows.append(('DEPOSIT', 'zenodo %s' % z['id'], F.norm(F.strip_html(z.get('description') or ''))))
    paths = dict(SYNTHESES)
    res = []
    df = {}
    for g, row, key, sid, s, cl in U:
        r = grade_of(H, key, sid)
        if not r or r[0] != 'EXCEEDS':
            continue
        own = row if row.startswith('SIDE-') and g != 'DEPOSIT' else ('PLACE-papers' if g == 'HEAD' else row)
        need = None
        drop = None
        if g == 'DEPOSIT':
            drop = 'zenodo ' + key.split(':')[1]
            need = F.names(s, row)
        elif g == 'HEAD':
            drop = paths[row]
            need = [F.norm(x) for x in re.findall(r'SIDE-[a-z-]+', s)] + [x for x in re.findall(r'`([A-Za-z_][\w.]*)`', s) if '_' in x]
        use = [x for x in rows if x[1] != drop]
        y, hits = F.sweep(s, use, own, need) if (need is None or need) else ({'M1': {}, 'M2': {}, 'M3': {}, 'M4': {}}, [])
        # ### M5: b726's M4 kept, on the row's distinctive words alone. M4 classed 123 of 472: a wrapped line's lone word ("the", "bijection") matches whole, and its first shingle is often a
        # ### phrase every paper carries ("the seven mechanism classes"). A row under four words takes no shingle; a four-word shingle in more than DF_MAX documents is common property, not a citation.
        words = F.norm(s).split()
        sh = []
        for x in (F.shingles(s, 4) if len(words) >= 4 else []):
            if x not in df:
                df[x] = sum(1 for r in rows if x in r[2])
            if df[x] <= DF_MAX:
                sh.append(x)
        nd = need if need is not None else F.names(s, own)
        m5 = []
        for repo, path, txt in (use if sh and nd else []):
            k = F.kind(repo, path, own)
            if k in ('paper', 'page', 'deposit'):
                got = F.near(txt, nd, sh)
                if got:
                    m5.append((repo, path, got[1], got[2]))
        y['M5'] = dict(collections.Counter(F.kind(h[0], h[1], own) for h in m5))
        res.append(dict(group=g, row=row, id=sid, yields=y, m4=[h[:3] for h in hits], hits=m5, cls='LOAD-BEARING' if m5 else 'SILENT'))
    return res


def sweep_controls():
    import b726_frontdoors as F
    rows = [('PLACE-papers', 'phase2/x.md', F.norm('as SIDE-cosmo states the formation distance is the dark sector of the model')), ('SIDE-cosmo', 'README.md', F.norm('the formation distance is the dark sector of the model'))]
    a = F.sweep('The formation distance is the dark sector of the model.', rows, 'SIDE-cosmo')[1]
    b = F.sweep('A planted sentence which nothing in any document cites at all.', rows, 'SIDE-cosmo')[1]
    return [('a citing paper classes LOAD-BEARING', bool(a), True), ('a planted sentence classes SILENT', bool(b), False)]


def tally(U, H, pick):
    T = {}
    for u in U:
        r = grade_of(H, u[2], u[3])
        for name in pick(u):
            d = T.setdefault(name, dict.fromkeys(GRADES, 0))
            d[r[0]] += 1
    return T


def cmd_bank(*a):
    need_controls()
    t0 = time.time()
    H = json.load(io.open(HAND, encoding='utf-8'))
    U = units()
    miss = [(u[2], u[3]) for u in U if not grade_of(H, u[2], u[3])]
    if miss:
        sys.exit('### %d ROWS UNGRADED -- NOTHING WRITTEN: %r' % (len(miss), miss[:12]))
    ctl = sweep_controls()
    if not all(x[1] == x[2] for x in ctl):
        sys.exit('### A SWEEP CONTROL NOT AS WANTED: %r' % ctl)
    import b732_address_scan as SC
    tokens = [x for x in SC.author_name().split() if len(x) > 2]
    mark, was = {}, False
    for u in U:      # ### a README's author row is split at the initial; the name's words mask the row, a row ending on an initial and an initial after a masked row go with it
        s = u[4]
        m = any(x in s for x in tokens) or bool(re.search(r'[|>] (?:\w+, )?[A-Z]\.$', s.strip())) or (was and bool(re.match(r'^[A-Z]\. ', s.strip())))
        mark[(u[2], u[3])] = m
        was = m
    C = classing(U, H)
    OV = json.load(io.open(CLASS_HAND, encoding='utf-8')) if os.path.exists(CLASS_HAND) else {}
    for c in C:
        v = OV.get('%s|%s|%s' % (c['row'], c['group'], c['id']))
        if v:
            c['hand'] = v
            c['cls'] = v[0]
            if v[0] == 'SILENT':
                c['struck'], c['hits'] = c['hits'], []
    if len(a) > 0:      # ### the hand read's screen, into the scratchpad: words around each hit, never banked
        with io.open(a[0], 'w', encoding='utf-8') as fh:
            for c in C:
                if c['hits'] or c.get('struck'):
                    fh.write('%s|%s|%s\n' % (c['row'], c['group'], c['id']))
                    for h in c['hits'] or c['struck']:
                        fh.write('   [%s] %s %s :: %s\n' % (h[2], h[0], h[1].split('/')[-1], h[3][:230]))
    for c in C:
        c['hits'] = [h[:3] for h in c['hits']]
        c.pop('struck', None)
        if c['row'] in PRIVATE:
            c['hits'] = [[h[0], h[1], 'private'] for h in c['hits']]
            c['m4'] = [[h[0], h[1], 'private'] for h in c['m4']]
    cls = dict(((c['row'], c['group'], c['id']), c) for c in C)
    import b721_frozen_line as F
    L = ['b732 -- (R342)(4): THE PHASE 2 DOORS GRADED IN b721`S VOCABULARY (%s)' % utc(), '',
         '### THE OBJECTS: data/b732_objects_rule.txt, printed before any kernel was named; data/b732_objects.txt, the navigator`s list beside it, choosing nothing. THE CONTROLS: data/b732_door_controls.txt, run before any sentence.',
         '### THE READING: six grading seats proposed a grade for every README sentence and description against the statements at the census pin (read by `git show`); the act`s seat graded the deposits and heads and read every EXCEEDS row by hand (corrections printed at their row). The price`s stop was not reached: all six clusters are graded.',
         '### THE PINS ARE THE CENSUS`S; THE READMES ARE MAIN AT HEAD; A README AHEAD OF ITS PIN IS GRADED AGAINST THE PIN, AS THE RULING ORDERS. PLACE-papers %s for the heads. SIDE-constants is private and the relay public: its rows carry id, grade and digest, no words, in SPIRAL_MAP`s form.' % PP_PIN,
         '', '## THE VOCABULARY, UNEDITED (tools/b721_frozen_line.py VOCAB)']
    L += ['  %s' % str(v) for v in (F.VOCAB.items() if hasattr(F.VOCAB, 'items') else F.VOCAB)]
    L += ['', '## THE CONTROLS OF THE CITATION SWEEP, BEFORE ANY CLASS'] + ['  %-40s %s' % (n, 'AS WANTED' if x == w else 'NOT') for n, x, w in ctl]
    O = dict((o['kernel'], o) for o in objects())
    last = None
    for g, row, key, sid, s, cl in U:
        if (g, row) != last:
            last = (g, row)
            L += ['']
            if g in ('README', 'DESCRIPTION') and row in O and g == 'README':
                ds = decls(row, O[row]['pin'])
                e = {}
                for d in ds:
                    x = e0_row(d[2], d[3], d[4])
                    e[x] = e.get(x, 0) + 1
                L += ['## %s at %s (%s), README at main ; E0 over the declarations at the pin: %s' % (row, O[row]['pin'], ' '.join(O[row]['rows']), ' ; '.join('%s %d' % kv for kv in sorted(e.items())))]
                if row not in PRIVATE:
                    th = [d for d in ds if d[2] in ('theorem', 'lemma')]
                    L += ['  THE STATEMENTS: every theorem at the pin with its E0 grade, by the bank`s reader at `decls`: tools/b732_doors.py decls %s (%d theorems); the rows below name each statement they rest on, file :line.' % (row, len(th))]
            elif g == 'DEPOSIT':
                L += ['## THE DEPOSIT %s, %s' % (row, key)]
            elif g == 'HEAD':
                L += ['## THE HEAD OF %s (%s)' % (row, dict(SYNTHESES)[row])]
        r = grade_of(H, key, sid)
        c = cls.get((row, g, sid))
        tag = ' | ' + c['cls'] if c else ''
        lab = 'THE GITHUB DESCRIPTION' if sid == 'description' else sid
        if row in PRIVATE and g != 'DEPOSIT':
            L.append('  %-8s %-9s | [private; sha256 %s]%s' % (lab, r[0], digest(s), tag))
            if r[0] == 'EXCEEDS':
                L.append('           EXCEEDS: [%s]' % r[1])
            continue
        if mark.get((key, sid)):
            L.append('  %-8s %-9s | (the author line)' % (lab, r[0]))
            continue
        L.append('  %-8s %-9s | %s%s' % (lab, r[0], s, tag))
        if r[0] == 'EXCEEDS':
            L.append('           EXCEEDS: %s' % r[1])
            if c and c['hits']:
                L.append('           CITED AT: ' + ' ; '.join(sorted(set('%s %s' % (h[0], h[1]) for h in c['hits']))))
    L += ['', '## THE PINS AGAINST MAIN: THE RULING GRADES AT THE CENSUS PIN AND READS THE README AT MAIN, SO A KERNEL WHOSE MAIN MOVED IN LEAN IS READ ACROSS A GAP (commits ahead ; Lean files changed ; its EXCEEDS rows)']
    gap = 0
    for k in sorted(O):
        n = git('D:/' + k, 'rev-list', '--count', O[k]['pin'] + '..main').strip()
        st = git('D:/' + k, 'diff', '--stat', O[k]['pin'], 'main', '--', '*.lean').strip().split(NL)[-1].strip()
        ex = sum(1 for u in U if u[1] == k and u[0] in ('README', 'DESCRIPTION') and grade_of(H, u[2], u[3])[0] == 'EXCEEDS')
        if st:
            gap += ex
            L.append('  %-34s %3s ; %s ; EXCEEDS %d' % (k, n, st, ex))
    abs_rows = sum(1 for u in U if u[1] == 'SIDE-effects' and grade_of(H, u[2], u[3])[0] == 'EXCEEDS' and re.search(r'absent at pin|not in the pin|0 hits|not retired|no retirement|no status ledger|no such type|names? (?:a ladder|Grade|EDifficultyTop)', grade_of(H, u[2], u[3])[1]))
    L += ['  THE EXCEEDS ROWS AT THOSE KERNELS: %d. EXCEEDS AT A PIN BEHIND MAIN MEANS NOT COMPILED AT THE PIN; IT DOES NOT SAY WHAT MAIN COMPILES, WHICH WAS NOT GRADED.' % gap,
          '  SIDE-effects IS THE WIDE CASE: the census pin is v0.1 = afb196e and main is 24 commits on; %d of its EXCEEDS rows name an object absent at the pin (ExhaustivenessLicense.lean, Phase15/SIDEFramework.lean, Phase15/Module1.lean, the retirement ledger), present at main by file listing and not read.' % abs_rows]
    L += ['', '## WHAT THE READ FOUND AT THE PINS, BEYOND THE GRADES (each confirmed by the seat`s own read where marked SEAT; the others are the grading seat`s, cited at their row)']
    L += ['  ' + x for x in FINDINGS_READ]
    L += ['', '## THE HAND READ: EVERY EXCEEDS ROW PROPOSED WAS READ BY THE SEAT; THE CORRECTIONS (the note of each carries HAND READ)']
    n_c = 0
    for key, v in sorted(H.items()):
        for sid, r in sorted(list((v.get('readme') or {}).items()) + ([('description', v['description'])] if isinstance(v.get('description'), list) else [])):
            if r[1].startswith('HAND READ') or ' HAND READ:' in r[1]:
                n_c += 1
                L.append('  %s %s -> %s | %s' % (key, sid, r[0], r[1][:200]))
    L += ['  CORRECTED %d OF THE PROPOSED EXCEEDS ROWS. RULED NOT CORRECTED: the bare topic-label descriptions (a label names its object, and the vocabulary`s `an object the statements do not name` reads it); the boundary rows the grading seats flagged (a name read as content).' % n_c,
          '  NOT HAND-READ: the STATED, OUTSIDE, SCOPE and NO CLAIM rows the six seats proposed; (R342)(4) and this act`s reading rule hold the hand read to EXCEEDS, so a row graded too low is not caught here.',
          '  E0 READS THE STATEMENT AND NOT THE PROOF: the three sorry theorems at SIDE-effects Milestones.lean grade DERIVES; E0 RAISED BinderUnclassed rows stand as the reader printed them. A SENTENCE ID IS THE TOOL`S (tools/b721_frozen_line.py sentences): a hard-wrapped README gives one sentence several ids, so the counts below are ids (SIDE-meta`s 29 EXCEEDS ids are 9 sentences).']
    def row_tally(title, T, keys):
        out = ['', '## ' + title, '  %-36s %7s %7s %7s %7s %8s %7s' % (('', ) + GRADES + ('ROWS',))]
        for k in keys:
            d = T[k]
            out.append('  %-36s %7d %7d %7d %7d %8d %7d' % ((k,) + tuple(d[g] for g in GRADES) + (sum(d.values()),)))
        return out
    TK = tally(U, H, lambda u: [u[1]])
    keys = sorted(TK, key=lambda k: (not k.startswith('SIDE-'), k))
    TC = tally(U, H, lambda u: list(u[5]))
    TG = tally(U, H, lambda u: [u[0]])
    L += row_tally('THE TALLY PER KERNEL, DOCUMENT OR DEPOSIT (a kernel`s row carries its README, its description and, under its own name, its deposit)', TK, keys)
    L += row_tally('THE TALLY PER CLUSTER (a row counted under each cluster naming it)', TC, sorted(TC))
    L += row_tally('THE TALLY BY KIND', TG, sorted(TG))
    lb = [c for c in C if c['cls'] == 'LOAD-BEARING']
    L += ['', '## W-ORD-SILENT-SENTENCES OVER THE EXCEEDS ROWS: THE MATCHERS` YIELDS (b726`s sweep, imported unedited; a row`s own document out of its sweep)']
    L.append('  M1-M4 ARE b726`S; M4 CLASSED %d ROWS. M5 IS M4 ON THE ROW`S DISTINCTIVE WORDS (a row of four words or more; a shingle in at most %d documents of the corpus): THE MATCHER THAT CLASSES, ITS HITS READ BY HAND: %d STRUCK, data/b732_door_class_hand.json, EACH WITH ITS REASON. A ROW M4 CLASSED ON COMMON WORDS AND M5 DID NOT STANDS SILENT; ITS PARAGRAPH FALLS WITH THE README PARAGRAPH OF THE DRAFTS.' % (sum(1 for c in C if c.get('m4')), DF_MAX, sum(1 for v in OV.values() if v[0] == 'SILENT')))
    for k in ('M1', 'M2', 'M3', 'M4', 'M5'):
        tot = {}
        for c in C:
            for kk, v in c['yields'][k].items():
                tot[kk] = tot.get(kk, 0) + v
        L.append('  %s %r' % (k, sorted(tot.items())))
    L += ['', '## THE LOAD-BEARING ROWS, AT THE HEAD (%d)' % len(lb)]
    for c in sorted(lb, key=lambda c: (c['row'], c['group'], c['id'])):
        L.append('  %s %s %s | %s' % (c['row'], c['group'], c['id'], ' ; '.join(sorted(set('%s %s' % (h[0], h[1]) for h in c['hits'])))))
    e = sum(1 for u in U if grade_of(H, u[2], u[3])[0] == 'EXCEEDS')
    k_n = len([u for u in O]); dn = len(set(u[2] for u in U if u[0] == 'DEPOSIT')); sn = len(set(u[2] for u in U if u[0] == 'HEAD'))
    L += ['', '### ### **KERNELS %d ; DEPOSITS %d ; SYNTHESIS HEADS %d ; SENTENCES %d ; EXCEEDS %d ; LOAD-BEARING %d ; SILENT %d ; SWEEP CONTROLS %d OF %d AS WANTED ; %d s.**' % (k_n, dn, sn, len(U), e, len(lb), e - len(lb), len(ctl), len(ctl), time.time() - t0)]
    write(OUT, L)
    with open(os.path.join(D, 'b732_door_classes.json') + '.tmp', 'wb') as fh:
        fh.write(json.dumps(C, ensure_ascii=False, indent=0).encode('utf-8'))
    os.replace(os.path.join(D, 'b732_door_classes.json') + '.tmp', os.path.join(D, 'b732_door_classes.json'))
    print(NL.join(L[-14:]))


def cmd_decls(k, *a):
    need_controls()
    pin = next(o['pin'] for o in objects() if o['kernel'] == k)
    print('=====', k, 'at', pin)
    for f, n, kd, nm, h in decls(k, pin):
        if kd in ('instance',):
            continue
        print('  %s :%d %s | %s' % (f, n, e0_row(kd, nm, h), h[:230]))


if __name__ == '__main__':
    fn = {'rule': cmd_rule, 'objects': cmd_objects, 'price': cmd_price, 'read': cmd_read, 'ids': cmd_ids, 'decls': cmd_decls, 'controls': cmd_controls, 'zenodo': cmd_zenodo,
          'merge': cmd_merge, 'heads': cmd_heads, 'deps': cmd_deps, 'gather': cmd_gather, 'exrows': cmd_exrows, 'bank': cmd_bank}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        sys.exit(__doc__)
    fn(*sys.argv[2:])
