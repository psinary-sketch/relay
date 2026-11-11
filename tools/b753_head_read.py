# -*- coding: utf-8 -*-
"""b753_head_read.py -- (R363)(5)(iii): THE HEAD READ, data/b753_head_read.txt.

For each repository of (5)(i) that carries a README: the README's opening sentence and the heading and opening sentence of its latest
section, both quoted; the repository's description as GitHub returns it; and a verdict from the printed rule below. The README is read from
the clone's objects at the remote main (5)(i) banked (data/b753_kernels.json); the descriptions by one call of the GitHub CLI, the one
remote read of this generator. No door is edited and no draft applied. From a PRIVATE repository nothing is quoted (the README's size and
hash, whether a description stands and its length), PLACE-papers apart, whose README the ruling orders read by the same rule. A quoted line
that carries an identifier by form (tools/standing/outbound.py) is withheld and says so.

THE RULE, printed in the bank:
  THE HEAD            the README's opening paragraph: the first prose after its title, a heading, a badge, a rule, a table row, code and a
                      byline (a line carrying an identifier by form) passed over; quoted to the sentence end nearest beneath 300 characters.
  THE LATEST SECTION  among the level-two headings, the one naming the greatest act (b<nnn>), or, where none names an act, the latest date
                      (yyyy-mm-dd); its heading and its opening paragraph by the same reader. A README none of whose headings names an act
                      or a date has NO DATED SECTION, and its verdict rests on its head and its description.
  THE VERDICTS, every one that holds; AGREES where none does:
    AN OLDER WORDING THE REGISTRY REWORDED    the head, the latest section, the description or the README's body carries "two-leg" (REGISTRY
                                              :153, :188, :208, :492-:496: reworded on 2026-07-23 to the criterion and its verified
                                              surround); the verdict says where
    THE HEAD DENIES A LATER SECTION           the head carries a denial of the repository's content (NOTHING IN THIS REPOSITORY; VENDORED;
                                              nothing here) and a dated section's heading or opening paragraph names content of its own
                                              (theorem, instance, schema, statement, criterion, proved, compiles)
    NO DESCRIPTION                            GitHub returns none
    THE DESCRIPTION DIFFERS FROM THE HEAD     the description shares fewer than two content words (five letters or more, the repository's
                                              name and a stop list apart) with the README's title and opening paragraph, or names a version
                                              that neither the title nor the remote's latest tag carries. A rule on shared
                                              words: it reads a paraphrase as DIFFERS; each row quotes both for the author's read

  python -X utf8 -u tools/b753_head_read.py control      the controls alone, no remote read
  python -X utf8 -u tools/b753_head_read.py run          the controls, the known instance, the one remote read, the bank
  python -X utf8 -u tools/b753_head_read.py compose      the bank recomposed from the JSON, no remote read
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import outbound

ACT = 'b753'
BANK = os.path.join(RELAY, 'data', '%s_head_read.txt' % ACT)
JSN = os.path.join(RELAY, 'data', '%s_head_read.json' % ACT)
KERNELS = os.path.join(RELAY, 'data', '%s_kernels.json' % ACT)
QUOTED_PRIVATE = ('PLACE-papers',)     # ### (R363)(5)(iii): "PLACE-papers' README and description are read by the same rule"
OLD = re.compile(r'\btwo[- ]leg', re.I)
DENY = re.compile(r'NOTHING IN THIS REPOSITORY|\bVENDORED\b|\bnothing (?:here|in this repository)\b', re.I)
OWN = re.compile(r'\b(theorems?|instances?|schema|statements?|criterion|proved|compiles|compiled)\b', re.I)
ACTN = re.compile(r'\bb(\d{3})\b')
DATE = re.compile(r'\b(20\d\d-\d\d-\d\d)\b')
VER = re.compile(r'\bv\d+(?:\.\d+)+\b|\bv\d+\b')
STOP = set('''about above after again against being below between could every first from have having into itself kernel kernels lean4 mathlib more most
other over programme repository research should side some such than that their theirs them then there these they this those through under until
verification verified very what when where which while with within without would stand place statements statement theorem theorems'''.split())
EF_HEAD = "A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS THIS PROGRAMME'S MATHEMATICS."
EF_ACTS = ['b566', 'b567', 'b569', 'b570', 'b571', 'b572', 'b573', 'b743']


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.stdout, r.returncode


def path_of(name):
    return {'relay': RELAY.replace('\\', '/'), 'PLACE-papers': 'D:/MY-DOwnloads/PLACE-papers'}.get(name, 'D:/' + name)


def plain(s):
    s = re.sub(r'^\s*>\s?', '', s.strip())
    return re.sub(r'\*\*|__', '', s).strip()


def skip(l):
    s = l.strip()
    return (not s or s.startswith('#') or s.startswith('![') or s.startswith('[![') or re.fullmatch(r'[-*_]{3,}', s) is not None or s.startswith('|')
            or s.startswith('```') or l.startswith('    ') or l.startswith('\t') or bool(outbound.identifiers_in(s))
            or re.fullmatch(r'<[^>]+>', s) is not None)


def paragraph(L, start=0, end=None):
    """(line number, the opening paragraph) of L[start:end]: the first prose line and the lines after it to the next blank, heading or code."""
    end = len(L) if end is None else end
    i, fence = start, False
    while i < end:
        if L[i].strip().startswith('```'):
            fence = not fence
            i += 1
            continue
        if fence or skip(L[i]):
            i += 1
            continue
        j, out = i, []
        while j < end and L[j].strip() and not L[j].strip().startswith('#') and not L[j].strip().startswith('```') and not L[j].startswith('    '):
            if not outbound.identifiers_in(L[j]):
                out.append(plain(L[j]))
            j += 1
        return i + 1, ' '.join(out)
    return None, ''


def cut(p, n=300):
    """the paragraph to the sentence end nearest beneath n characters; whole where it is shorter."""
    if len(p) <= n:
        return p
    ends = [m.end() for m in re.finditer(r'[.!?;](?=\s)', p[:n])]
    return (p[:ends[-1]] if ends else p[:n]) + ' [...]'


def sections(L):
    """[(line number, heading, key)]: the level-two headings; key ('act', n) or ('date', d) where the heading names one, else None."""
    out, fence = [], False
    for i, l in enumerate(L):
        if l.strip().startswith('```'):
            fence = not fence
        if fence or not l.startswith('## '):
            continue
        a, d = (re.findall(r'\bact b(\d{3})\b', l) or ACTN.findall(l)), DATE.findall(l)   # ### the heading's own act ("at act b743"), before any act a name carries
        out.append((i + 1, l[3:].strip(), ('act', max(int(x) for x in a)) if a else (('date', max(d)) if d else None)))
    return out


def latest_section(L):
    """(line, heading, its opening paragraph, the dated sections) or (None, None, '', [])."""
    S = sections(L)
    dated = [s for s in S if s[2]]
    if not dated:
        return None, None, '', []
    acts = [s for s in dated if s[2][0] == 'act']
    top = max(acts, key=lambda s: s[2][1]) if acts else max(dated, key=lambda s: s[2][1])
    nxt = [s[0] for s in S if s[0] > top[0]]
    _n, para = paragraph(L, top[0], (nxt[0] - 1) if nxt else None)
    return top[0], top[1], para, dated


def words(s, name):
    own = set(x for x in re.split(r'[^a-z0-9]+', name.lower()) if x)
    toks = re.findall(r"[a-z][a-z'-]{4,}", (s or '').lower())
    toks += [x for t in toks if '-' in t for x in t.split('-') if len(x) >= 5]     # ### a hyphened word counts whole and by its parts
    return set(w for w in toks if w not in STOP and w not in own)


def verdicts(name, title, head, latest_h, latest_p, dated_text, desc, latest_tag, body=0):
    """(the verdicts, the shared content words); body: the older wording's count anywhere in the README."""
    V = []
    where = [w for w, x in (('the head', head), ('the latest section', (latest_h or '') + ' ' + (latest_p or '')), ('the description', desc)) if OLD.search(x or '')]
    inner = len(OLD.findall(head or '')) + len(OLD.findall((latest_h or '') + ' ' + (latest_p or '')))
    if body > inner:
        where.append('the README`s body, %d' % (body - inner))
    if where:
        V.append('AN OLDER WORDING THE REGISTRY REWORDED (%s)' % ' ; '.join(where))
    if DENY.search(head or '') and any(OWN.search(t) for t in dated_text):
        V.append('THE HEAD DENIES A LATER SECTION')
    shared = sorted(words(desc, name) & words((title or '') + ' ' + (head or ''), name))
    if not (desc or '').strip():
        V.append('NO DESCRIPTION')
    else:
        dv = set(VER.findall(desc))
        known = set(VER.findall(title or '')) | ({latest_tag} if latest_tag else set())
        stray = sorted(v for v in dv if v not in known)
        if len(shared) < 2 or stray:
            V.append('THE DESCRIPTION DIFFERS FROM THE HEAD' + ((' (it names %s; the title and the latest tag: %s)' % (', '.join(stray), ', '.join(sorted(known)) or 'none'))
                                                               if stray else ''))
    return V or ['AGREES'], shared


def q(s):
    """a line for the bank: withheld where it carries an identifier by form."""
    if s is None:
        return 'NONE'
    return '[WITHHELD: carries an identifier by form]' if outbound.identifiers_in(s) else '"%s"' % s


def read_readme(name, row):
    """dict for one repository on D:, from the clone's objects at the remote main where the clone holds it."""
    p = path_of(name)
    rev = row.get('main') if row.get('main') and git(p, 'cat-file', '-e', row['main'] + '^{commit}')[1] == 0 else 'HEAD'
    files = [x for x in git(p, 'ls-tree', '--name-only', rev)[0].split('\n') if re.fullmatch(r'readme(\.md|\.markdown|\.txt)?', x, re.I)]
    out = dict(rev=git(p, 'rev-parse', '--short=8', rev)[0].strip(), at_remote_main=rev != 'HEAD', readme=files[0] if files else None)
    if not files:
        return out
    t = git(p, 'show', '%s:%s' % (rev, files[0]))[0]
    L = t.split('\n')
    title = next((l.lstrip('#').strip() for l in L if l.startswith('# ')), '')
    hn, hp = paragraph(L)
    sn, sh, sp, dated = latest_section(L)
    S = sections(L)
    dt = []
    for d in dated:
        nxt = [s[0] for s in S if s[0] > d[0]]
        dt.append(d[1] + ' ' + paragraph(L, d[0], (nxt[0] - 1) if nxt else None)[1])
    out.update(lines=len(L), sha=hashlib.sha256(t.encode('utf-8')).hexdigest()[:8], bytes=len(t.encode('utf-8')), title=title, head_line=hn, head=hp,
               n_sections=len(S), dated=[(d[0], d[1], '%s %s' % d[2]) for d in dated], dated_text=dt, sec_line=sn, sec_head=sh, sec_para=sp,
               old_anywhere=len(OLD.findall(t)))
    return out


def owner():
    u = git(RELAY, 'remote', 'get-url', 'origin')[0].strip()
    m = re.search(r'[/:]([^/:]+)/relay(?:\.git)?$', u)
    return m.group(1) if m else None


def descriptions():
    """{name: description or None} by one call of the GitHub CLI; (None, error) where the call fails."""
    env = dict(os.environ, GH_PROMPT_DISABLED='1', NO_COLOR='1')
    r = subprocess.run(['gh', 'repo', 'list', owner(), '--limit', '400', '--json', 'name,description,visibility,isFork'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=env, timeout=120)
    if r.returncode:
        return None, 'exit %d: %s' % (r.returncode, (r.stderr or '').strip()[:240])
    return dict((x['name'], dict(description=x.get('description') or None, visibility=x.get('visibility'), fork=x.get('isFork'))) for x in json.loads(r.stdout)), None


def controls():
    L, ok = [], True

    def case(what, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    fx = ['# A title v0.2', '', '[![badge](x)](y)', '', 'A Name (ORCID: 0000-0001-2345-6789)', '', '> **The first prose line,', 'wrapped to a second.** A second sentence.', '',
          '## Status', '', 'Body.', '', '## Appended at act b571 (ruling) -- one', '', 'It states a theorem.', '', '## Appended at act b743 -- the later one', '',
          '    code line', '', 'The later section opens here.', '', '## License', '', 'MIT.']
    case('(the head) a planted README: the title, a badge and a byline passed over, the wrapped paragraph joined', paragraph(fx),
         (7, 'The first prose line, wrapped to a second. A second sentence.'))
    sn, sh, sp, dated = latest_section(fx)
    case('(the latest section) of three, two naming acts b571 and b743: (line, heading, its paragraph, dated)', (sn, sh, sp, len(dated)),
         (18, 'Appended at act b743 -- the later one', 'The later section opens here.', 2))
    case('(the latest section) by date where no heading names an act; none where none is dated',
         (latest_section(['## Note -- 2026-08-24', 'a', '## Note -- 2026-07-01', 'b'])[1], latest_section(['## License', 'x'])[0]), ('Note -- 2026-08-24', None))
    case('(the cut) a paragraph over the bound, to the sentence end beneath it', cut('One sentence here. ' + 'x' * 400, 40), 'One sentence here. [...]')
    v = lambda *a: verdicts(*a)[0]
    case('(a verdict) a planted head that denies and a dated section naming a theorem',
         v('SIDE-x', 'SIDE-x', 'A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS OURS.', 'Appended at act b743', 'States the theorem.', ['Appended at act b743 States the theorem.'],
           'A vendored kernel, nothing ours.', None), ['THE HEAD DENIES A LATER SECTION'])
    case('(a verdict) the same head with no dated section', v('SIDE-x', 'SIDE-x', 'A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS OURS.', None, '', [],
                                                              'A vendored kernel, nothing ours.', None), ['AGREES'])
    case('(a verdict) a planted head, section and description that agree',
         v('SIDE-x', 'SIDE-x', 'It compiles fraction arithmetic over literals.', None, '', [], 'Compiles fraction arithmetic over literals', None), ['AGREES'])
    case('(a verdict) no description; an empty one', (v('SIDE-x', 'SIDE-x', 'Compiles arithmetic.', None, '', [], None, None), v('SIDE-x', 'SIDE-x', 'Compiles arithmetic.', None, '', [], ' ', None)),
         (['NO DESCRIPTION'], ['NO DESCRIPTION']))
    case('(a verdict) the older wording in the head; in the README`s body alone, once',
         (v('SIDE-x', 'SIDE-x', 'The logical structure of a two-leg approach.', None, '', [], 'The logical structure of an approach', None, 1),
          v('SIDE-x', 'SIDE-x', 'The logical structure of an approach.', None, '', [], 'The logical structure of an approach', None, 1)),
         (['AN OLDER WORDING THE REGISTRY REWORDED (the head)'], ['AN OLDER WORDING THE REGISTRY REWORDED (the README`s body, 1)']))
    case('(the content words) a hyphened word shared by its parts: "fixed-point arithmetic" against "its only fixed point ... arithmetic"',
         sorted(words('the fixed-point arithmetic', 'SIDE-x') & words('its only fixed point, rational arithmetic', 'SIDE-x')), ['arithmetic', 'fixed', 'point'])
    case('(the cut) a colon is no sentence end', cut('Subject: ' + 'word ' * 80, 60).startswith('Subject: word'), True)
    case('(a verdict) a description sharing no content word; a description naming a version neither the title nor the latest tag carries',
         (v('SIDE-x', 'SIDE-x v0.2', 'It compiles fraction arithmetic.', None, '', [], 'Spectral cosmology engine', 'v0.2'),
          v('SIDE-x', 'SIDE-x v0.2', 'It compiles fraction arithmetic.', None, '', [], 'Compiles fraction arithmetic, v0.1', 'v0.2')),
         (['THE DESCRIPTION DIFFERS FROM THE HEAD'], ['THE DESCRIPTION DIFFERS FROM THE HEAD (it names v0.1; the title and the latest tag: v0.2)']))
    case('(a quoted line) one carrying a number of the identifier`s form is withheld; one carrying none is quoted', (q('By A. Name, 0000-0001-2345-6789'), q('plain')),
         ('[WITHHELD: carries an identifier by form]', '"plain"'))
    case('(the owner) read from the relay`s origin, not typed here', bool(owner()), True)
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED'))
    return ok, L


def known_instance(K):
    """(ok, lines): (R363)(5)(iii)'s control, printed before the table."""
    row = K['rows']['SIDE-explicit-formula']
    r = read_readme('SIDE-explicit-formula', row)
    acts = sorted(set('b%s' % k.split()[1] for _n, _h, k in r['dated'] if k.startswith('act ')))
    V, _s = verdicts('SIDE-explicit-formula', r['title'], r['head'], r['sec_head'], r['sec_para'], r['dated_text'], 'x', None)
    ok = (r['rev'] == '8fbab45d' and r['head'].startswith(EF_HEAD) and acts == EF_ACTS and 'THE HEAD DENIES A LATER SECTION' in V)
    L = ['  SIDE-explicit-formula`s README at main %s: the head, :%s, %s' % (r['rev'], r['head_line'], q(cut(r['head']))),
         '  the ruling`s sentence: "%s": %s' % (EF_HEAD, 'THE HEAD OPENS WITH IT' if r['head'].startswith(EF_HEAD) else '### DIFFERS'),
         '  its dated sections: %d, naming the acts %s; the ruling`s eight (b566, b567, b569 to b573, b743): %s' % (
             len(r['dated']), ', '.join(acts), 'THE SAME' if acts == EF_ACTS else '### DIFFERS')]
    L += ['      :%d ## %s' % (n, h) for n, h, _k in r['dated']]
    L += ['  the rule on it (its description apart): %s' % ' ; '.join(v for v in V if 'DESCRIPTION' not in v),
          '  ### THE KNOWN INSTANCE: %s' % ('AS WANTED' if ok else '### NOT AS WANTED')]
    return ok, L


def compose(state):
    K = json.load(io.open(KERNELS, encoding='utf-8'))
    import b303_pins as P
    vis = P.visibility()
    ok, CL = controls()
    ok2, KL = known_instance(K)
    D = state['descriptions']
    L = ['%s -- (R363)(5)(iii): THE HEAD READ -- every repository of (5)(i) that carries a README: its head, its latest section, its description, a verdict (%s)' % (
        ACT, state['at'][:10]), '',
         '### Written by tools/%s_head_read.py at relay %s (the generator committed before its run). Each README read from its clone`s objects at the remote' % (ACT, state['generator']),
         '### main (5)(i) banked; the descriptions by one call of the GitHub CLI at %s, the one remote read. No door edited, no draft applied: every row not' % state['at'],
         '### reading AGREES is carried to the sitting. From a PRIVATE repository nothing is quoted and no verdict of its wording is printed (the README`s',
         '### size and hash, whether a description stands and its length), PLACE-papers apart, which (R363)(5)(iii) orders read by the same rule. The',
         '### ruling`s expectation that every verdict quote the two sentences it compares is not met on those rows: the two orders conflict there, and the',
         '### rows say so. A quoted line carrying an identifier by form is withheld.'] + (
             ['### RECOMPOSED %s by the generator at relay %s from the banked read (data/%s_head_read.json), no second remote read: %s' % (
                 state['recomposed'][1], state['recomposed'][0], ACT, state['recomposed'][2])] if state.get('recomposed') else []) + ['', '## THE RULE'] + ['  ' + l for l in __doc__.split('THE RULE, printed in the bank:\n')[1].split('\n\n  python')[0].split('\n')]
    L += ['', '## THE CONTROLS, printed before any figure'] + CL + ['', '## THE KNOWN INSTANCE, printed before the table ((R363)(5)(iii))'] + KL + ['', '## THE TABLE']
    tally, doors, noreadme, unquoted, carried = {}, 0, [], [], []
    for n in K['order']:
        row = K['rows'][n]
        d = D.get(n) or {}
        desc = d.get('description')
        v = vis.get(n, '### NOT IN THE MAP')
        if not row['on_d']:
            noreadme.append('%s (%s): NO CLONE ON D:, its README not read ; description %s' % (n, v, ('stands, %d characters' % d['length']) if d.get('length') else 'NONE'))
            continue
        r = read_readme(n, row)
        if not r['readme']:
            noreadme.append('%s (%s): NO README at %s ; description %s' % (n, v, r['rev'], q(desc) if v == 'PUBLIC' else ('stands' if d.get('length') else 'NONE')))
            continue
        doors += 1
        if v != 'PUBLIC' and n not in QUOTED_PRIVATE:
            verdict = ['NO DESCRIPTION'] if not d.get('length') else ['READ, NOT QUOTED, NO VERDICT OF ITS WORDING PRINTED']
            unquoted.append(n)
            L.append('  %s (%s) | %s at %s: %d lines, %d bytes, sha256 %s ; level-two sections %d, dated %d | description %s | %s' % (
                n, v, r['readme'], r['rev'], r['lines'], r['bytes'], r['sha'], r['n_sections'], len(r['dated']),
                ('stands, %d characters' % d['length']) if d.get('length') else 'NONE', ' ; '.join(verdict)))
            for x in verdict:
                tally[x] = tally.get(x, 0) + 1
            continue
        V, shared = verdicts(n, r['title'], r['head'], r['sec_head'], r['sec_para'], r['dated_text'], desc, None if row.get('code') else latest_tag(row), r['old_anywhere'])
        for x in V:
            tally[x.split(' (')[0]] = tally.get(x.split(' (')[0], 0) + 1
        if V != ['AGREES']:
            carried.append(n)
        L.append('  %s (%s%s) | %s at %s%s, %d lines ; level-two sections %d, dated %d | %s' % (
            n, v, ', a fork' if d.get('fork') else '', r['readme'], r['rev'], '' if r['at_remote_main'] else ' (### the clone`s HEAD, the remote main not in it)', r['lines'],
            r['n_sections'], len(r['dated']), ' ; '.join(V)))
        L.append('      the head, :%s: %s' % (r['head_line'], q(cut(r['head']))))
        if r['sec_head']:
            L.append('      the latest section, :%s: %s -- %s' % (r['sec_line'], q('## ' + r['sec_head']), q(cut(r['sec_para']))))
        else:
            L.append('      the latest section: NO DATED SECTION (no level-two heading names an act or a date)')
        L.append('      the description: %s%s%s' % (q(desc), '' if not desc else ' ; content words shared with the title and head: %d%s' % (
            len(shared), (' (%s)' % ', '.join(shared[:6])) if shared else ''), ''))
    L += ['', '## THE REPOSITORIES OF (5)(i) THAT CARRY NO README, OR WHOSE README WAS NOT READ'] + ['  ' + x for x in noreadme]
    not_agree = sum(1 for n in carried)
    L += ['', '## CARRIED TO THE SITTING ((R363)(5)(iii), (8)): every door not reading AGREES, its draft cut there from the kernel`s printed statements',
          '  ' + (', '.join(carried) or 'none'),
          '  the PRIVATE rows not quoted (%d: %s) are the author`s to read; no verdict of their wording is printed here' % (len(unquoted), ', '.join(unquoted) or 'none'),
          '', '### ### **THE HEAD READ: %d DOORS (READMEs read) ; QUOTED %d, NOT AGREEING %d ; PRIVATE AND NOT QUOTED %d ; %s ; NO README OR NOT READ %d ; THE KNOWN INSTANCE %s ; CONTROLS %s.**' % (
              doors, doors - len(unquoted), not_agree, len(unquoted), ' ; '.join('%s %d' % (k, tally[k]) for k in sorted(tally)), len(noreadme),
              'AS WANTED' if ok2 else '### NOT AS WANTED', 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED')]
    return L


def latest_tag(row):
    v = [t for t in row.get('tags', {}) if re.fullmatch(r'v\d+(?:\.\d+)*', t)]
    return max(v, key=lambda t: tuple(int(x) for x in t[1:].split('.'))) if v else None


def bank(state):
    tmp = JSN + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(state, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
    os.replace(tmp, JSN)
    L = compose(state)
    tmp = BANK + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(L) + '\n')
    os.replace(tmp, BANK)
    return L


def committed():
    rel = 'tools/%s_head_read.py' % ACT
    tracked = git(RELAY, 'ls-files', '--error-unmatch', rel)[1] == 0
    return tracked and not git(RELAY, 'status', '--porcelain', '--', rel)[0].strip(), git(RELAY, 'rev-parse', '--short=8', 'HEAD')[0].strip()


def main(argv):
    if argv[:1] == ['control']:
        ok, L = controls()
        ok2, KL = known_instance(json.load(io.open(KERNELS, encoding='utf-8')))
        print('\n'.join(L + ['## THE KNOWN INSTANCE'] + KL))
        return 0 if ok and ok2 else 1
    if argv[:1] == ['compose'] and len(argv) == 2:
        done, head = committed()
        if not done:
            raise SystemExit('### REFUSED: tools/%s_head_read.py is not committed or differs from its commit' % ACT)
        state = json.load(io.open(JSN, encoding='utf-8'))
        state['recomposed'] = [head, stamp(), argv[1]]
        L = bank(state)
        print('\n'.join(L[:12] + L[L.index('## THE CONTROLS, printed before any figure'):L.index('## THE TABLE')] + [l for l in L[L.index('## THE TABLE'):] if not l.startswith('      ')]))
        return 0
    if argv[:1] != ['run']:
        raise SystemExit(__doc__)
    done, head = committed()
    if not done:
        raise SystemExit('### REFUSED: tools/%s_head_read.py is not committed or differs from its commit; the generator commits before its run ((R363)(5))' % ACT)
    import hold
    if hold.refuses('the head read ((R363)(5)(iii))'):
        return 3
    ok, CL = controls()
    ok2, KL = known_instance(json.load(io.open(KERNELS, encoding='utf-8')))
    print('\n'.join(['## THE CONTROLS, printed before any figure'] + CL + ['## THE KNOWN INSTANCE, printed before the table'] + KL))
    if not (ok and ok2):
        raise SystemExit('### THE CONTROLS OR THE KNOWN INSTANCE NOT AS WANTED: NOTHING READ')
    import b303_pins as P
    vis = P.visibility()
    at = stamp()
    D, err = descriptions()
    if D is None:
        raise SystemExit('### FAILED: the descriptions` one remote read at %s -- %s ((R363)(7)(ix): not an empty answer; its one retry an event)' % (at, err))
    keep = {}
    for n, d in D.items():
        public = vis.get(n) == 'PUBLIC' or n in QUOTED_PRIVATE
        keep[n] = dict(description=d['description'] if public else None, length=len(d['description'] or ''), fork=bool(d.get('fork')), github_visibility=d.get('visibility'))
    L = bank(dict(at=at, generator=head, descriptions=keep, returned=len(D)))
    print('\n'.join(L[L.index('## THE TABLE'):]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
