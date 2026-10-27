# -*- coding: utf-8 -*-
"""b717_words.py -- (R327)(5)-(6): THE AUTHOR'S WORDS OF b716 APPLIED AND THE ELEVEN NAMES, their readings and diffs banked; the edits
themselves are the Edit tool's on PLACE-papers main, and a new file the Write tool's from the draft this tool banks.

  python -X utf8 tools/b717_words.py head        (5)(i): the word on (R326)(5)(i) printed verbatim from relay data/b716_author_answers.txt :10,
                                                 section II of data/b714_heads_draft.txt (:34-:64) with its brackets removed, read against the
                                                 paragraph at Silence :15 now, and the seat's reading of which paragraph stands at :15 after the
                                                 edit -> data/b717_head.txt
  python -X utf8 tools/b717_words.py companion   the companion table day1/Silence_of_Foundations_CORRESPONDENCE.md drafted: each sentence of
                                                 :15 (cut at its eighteen openings, each opening's yield printed), its footing and source from
                                                 section I (:11-:28) -> data/b717_companion.md (the draft) and data/b717_companion.txt (its yields)
  python -X utf8 tools/b717_words.py lint        (5)(ii): b714's prose lint (tools/b714_pilot.py lint, imported unedited) over the seven day
                                                 papers as the working tree holds them, with the exception class the word orders -- REPAIR
                                                 RECORD: the banned stem quoted to name what was repaired -- granted to a hit on a blockquoted
                                                 line whose bytes the author ruled (by sha256, exact, b143's form: membership, not a pattern);
                                                 controls first -> data/b717_lint.txt
  python -X utf8 tools/b717_words.py names       (6): the eleven names of data/b716_correspondence_pins.txt :24-:34, each looked up at every
                                                 local kernel's current tag (the highest vN tag by version) by b714's lookup (imported
                                                 unedited); the statement at the tag from its line to its `:=` (a structure to its `where`),
                                                 its kind and its E0 grade (tools/e0_rule.py, from the statement alone) -> data/b717_names.txt
  python -X utf8 tools/b717_words.py edition     the census v0.8.3 begun on PLACE-papers as v0.8.2's bytes at main (b715's form for v0.8.2)
  python -X utf8 tools/b717_words.py diff        each PLACE-papers file the act writes, its working bytes against its blob at HEAD (a new
                                                 file against nothing; the census v0.8.3 against v0.8.2's blob), unified -> data/b717_words_diffs.txt

### THE MATCHER'S CLASS LIVES HERE, NOT IN tools/banned_terms.py: the (W) list of (R327)(9) does not name the shared matcher and (N5) writes no
### file beyond it, so the class the word orders is carried into this act's lint (b714's P2, the trial the six hits came from); the
### shared tool is unedited and the reading is printed in the bank for the author's strike.
Writes only its banks under relay data/ and, by `edition` alone, the census copy on PLACE-papers. No git write, no push.
"""
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
ACT = 'b717'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SILENCE = 'day1/Silence_of_Foundations.md'
COMPANION = 'day1/Silence_of_Foundations_CORRESPONDENCE.md'
CENSUS_PREV = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
CENSUS_NEW = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md'
DRAFT_AT = 'a86c9429'
SEVEN = ['day1/Silence_of_Foundations.md', 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Seven_Mechanism_Classes.md',
         'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md', 'day1/Which_Structure_Confines.md']
WRITTEN = [SILENCE, COMPANION, 'day1/Exhaustive_Enumeration.md', 'day1/ONE_PAGE_PROOF.md', 'day1/Third_Identity_Element.md',
           'day1/Seven_Mechanism_Classes.md', 'day1/Spectral_Inertness.md', 'ERRATA.md', CENSUS_NEW, 'OPEN_TRAILS.md']
OPENINGS = ['We identify an inverse relationship', 'The product formula ∏_v', 'The genetic code maps', 'We test this pattern',
            'The pattern holds in every case', 'We identify the mechanism', 'Universality implies', 'Non-discrimination implies',
            'The Silence Principle stands at three depths', '(1) Two specific instances', 'The Riemann Hypothesis is equivalent',
            "The product formula's terminal", '(2) Nine instances', '(3) The universal quantified form', 'The Lean form is the logical schema',
            'What remains empirical is scope', "The programme's registers", 'It is falsifiable']
# ### THE AUTHOR-RULED REPAIR RECORDS ((R327)(5)(ii) hits (1), (2), (5); the word, relay data/b716_author_answers.txt :13): the file, the line the
# ### pilot read, and the sha256 of that line's bytes (utf-8, no line end) as main holds it at the act's opening (b855623d); filled from `lint
# ### seed`, which prints them, and checked against the line every run.
RULED = {
    ('day1/Silence_of_Foundations.md', 218): '25066ead390b75873bcb87ab339335dec2ce32ea8628b8df4d8d839681b1faba',
    ('day1/Spectral_Inertness.md', 191): 'd6272cae539d43efa8b56cab8d9605f7e549a223f2b0240078fef26ae91ec27d',
}
NAMES = [('day1/Silence_of_Foundations.md', 236, 'not_register1'), ('day1/Silence_of_Foundations.md', 236, 'ch_iff_rh'),
         ('day1/Silence_of_Foundations.md', 236, 'register4_positivity_liCoeff_iff_rh'), ('day1/Silence_of_Foundations.md', 236, 'register5_output_holds'),
         ('day1/Exhaustive_Enumeration.md', 180, 'real_no_compact_open_addSubgroup'),
         ('day1/Seven_Mechanism_Classes.md', 273, 'techne_kernel_cross_exclusion.all_pairs_excluded'), ('day1/Seven_Mechanism_Classes.md', 273, 'MechanismClass'),
         ('day1/Seven_Mechanism_Classes.md', 273, 'structural_exhaustiveness_proved'), ('day1/Seven_Mechanism_Classes.md', 273, 'spectral_cannon'),
         ('day1/Spectral_Inertness.md', 199, 'general_p_no_fixed_cell'), ('day1/Third_Identity_Element.md', 261, 'Substrate')]   # ### data/b716_correspondence_pins.txt :24-:34


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def rl(rel):
    return io.open(os.path.join(D, rel), encoding='utf-8').read().replace('\r', '').split(NL)


def pp_lines(rel):
    return io.open(os.path.join(PP, *rel.split('/')), encoding='utf-8').read().replace('\r', '').split(NL)


def _membrane(p):
    import act_membrane as MEM
    import b717_record as REC
    MEM.guard_path(ACT, p, REC.R.ROOT_EXCLUDE)


def put(name, text):
    p = os.path.join(D, name)
    _membrane(p)
    data = text.encode('utf-8')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    print('  %s  data/%s' % (hashlib.sha256(data).hexdigest(), name))


# ================================================================================ (5)(i) THE HEAD
def word_head():
    l10 = rl('b716_author_answers.txt')[9]
    m = re.search(r'="(\u201cCompanion correspondence:[^\u201d]*\u201d)"', l10)
    return m.group(1) if m else None


def section_two():
    ls = rl('b714_heads_draft.txt')[33:64]           # ### :34-:64
    joined = ' '.join(l.strip() for l in ls)
    stripped = re.sub(r' \[[^\]]*\]', '', joined)
    return joined, stripped, len(re.findall(r' \[[^\]]*\]', joined))


def head(*a):
    w = word_head()
    joined, stripped, nb = section_two()
    now = pp_lines(SILENCE)[14]
    eq = stripped == now
    first = next((i for i, (x, y) in enumerate(zip(stripped, now)) if x != y), None if len(stripped) == len(now) else min(len(stripped), len(now)))
    L = ['%s -- (R327)(5)(i): THE HEAD OF Silence_of_Foundations :15, THE WORD AND THE SEAT`S READING, PRINTED BEFORE THE EDIT (%s)' % (ACT, utc()), '',
         '### THE WORD, verbatim from relay data/b716_author_answers.txt :10 (the answer to PROMPT 1, Footings, b716`s root prompt):',
         '    %s' % w, '',
         '### SECTION II, relay data/b714_heads_draft.txt :34-:64 (its head :33: "each sentence as it stands at :15, its footing after it in brackets;',
         '### no claim, argument or sentence altered"), its lines joined, its brackets removed (%d bracketed footings, each with the space before it).' % nb,
         '### :15 NOW: PLACE-papers day1/Silence_of_Foundations.md :15 in the working tree at main %s.' % (git(PP, 'rev-parse', '--short', 'HEAD') or '').strip(),
         '  section II, brackets removed : %d characters, sha256 %s' % (len(stripped), hashlib.sha256(stripped.encode('utf-8')).hexdigest()),
         '  :15 now                      : %d characters, sha256 %s' % (len(now), hashlib.sha256(now.encode('utf-8')).hexdigest()),
         '  EQUAL, character for character: %s%s' % (eq, '' if eq else ' ; the first difference at character %s' % first), '',
         '### THE SEAT`S READING: the word names section II`s paragraph ("section II`s paragraph replaces :15 with its brackets removed"), so the',
         '### paragraph that stands at :15 after the edit is section II`s with its brackets removed; ' + (
             'that text is the paragraph now at :15, character for character -- section II was drafted from :15 with no sentence altered -- so the'
             if eq else 'that text differs from the paragraph now at :15 (above), and the edit writes section II`s text in its place; the'),
         '### ' + ('replacement leaves :15`s bytes as they stand and the word`s content is the companion table: each sentence`s footing and source'
                   if eq else 'companion table carries each sentence`s footing and source') +
         ' in day1/Silence_of_Foundations_CORRESPONDENCE.md beside the paper.',
         '', '### ### **THE WORD NAMES SECTION II ; :15 AFTER THE EDIT = SECTION II WITHOUT ITS BRACKETS ; EQUAL TO :15 NOW: %s.**' % eq]
    print(NL.join(L))
    if 'dry' not in a:
        put('%s_head.txt' % ACT, NL.join(L) + NL)


# ================================================================================ THE COMPANION
def section_one():
    rows = []
    for l in rl('b714_heads_draft.txt')[10:28]:       # ### :11-:28
        m = re.match(r'^\s+S(\d+)\s+(.*)$', l)
        parts = [x.strip() for x in re.split(r'\s*\|\s*', m.group(2))]   # ### S10 and S16 write `classification|` with no space before the bar
        rows.append((int(m.group(1)), parts[0], parts[1], ' | '.join(parts[2:])))
    return rows


def cut_sentences(par):
    pos = []
    for o in OPENINGS:
        k = [m.start() for m in re.finditer(re.escape(o), par)]
        pos.append((o, k))
    ok = all(len(k) == 1 for _o, k in pos) and [k[0] for _o, k in pos] == sorted(k[0] for _o, k in pos)
    starts = [k[0] for _o, k in pos] if ok else []
    sents = [par[s:(starts[i + 1] if i + 1 < len(starts) else len(par))].strip() for i, s in enumerate(starts)]
    return pos, ok, sents


def companion(*a):
    par = pp_lines(SILENCE)[14]
    pos, ok, sents = cut_sentences(par)
    rows = section_one()
    now_n = len(pp_lines(SILENCE))
    then = (git(PP, 'show', '%s:%s' % (DRAFT_AT, SILENCE)) or '').split(NL)
    nowl = pp_lines(SILENCE)
    changed = [i + 1 for i, (x, y) in enumerate(zip(then, nowl)) if x != y] if len(then) == len(nowl) else None
    Y = ['%s -- THE COMPANION`S DRAFT: THE EIGHTEEN OPENINGS` YIELD IN :15, SECTION I`S ROWS, THE PAPER`S LINES SINCE %s (%s)' % (ACT, DRAFT_AT, utc()), '']
    Y += ['  S%-2d %-46s yield %d at %s' % (i + 1, o, len(k), k) for i, (o, k) in enumerate(pos)]
    Y += ['  the openings each once and in order: %s ; sentences cut %d ; section I rows %d ; their numbers %s' % (ok, len(sents), len(rows), [r[0] for r in rows]),
          '  the paper at %s: %d lines ; now: %d lines ; lines changed in place since: %s' % (DRAFT_AT, len(then), now_n,
                                                                                        changed if changed is not None else 'LINE COUNT DIFFERS'), '']
    if not ok or len(rows) != 18:
        Y.append('### ### **THE CUT IS NOT CLEAN -- NO DRAFT WRITTEN.**')
        print(NL.join(Y))
        return
    esc = lambda s: s.replace('|', '\\|')   # noqa: E731
    C = ['# The Silence of Foundations — the opening paragraph’s correspondence', '',
         '*Companion to `day1/Silence_of_Foundations.md` :15, written 2026-10-27 by b717 under the author’s ruling `(R327)`(5)(i) and the author’s '
         'word on `(R326)`(5)(i): “Companion correspondence: section II’s paragraph replaces :15 with its brackets removed; each sentence’s footing '
         'and source go in a companion table beside it.” The paragraph at :15 is section II’s of the heads draft with its brackets removed, which is '
         'the paragraph as it stood, sentence for sentence. The footings and sources below are the heads draft’s section I (relay '
         '`data/b714_heads_draft.txt` :11-:28), drafted at b714 against the paper at `%s`; nothing in them is re-read here.*' % DRAFT_AT, '',
         '**The footings.** KERNEL — a compiled statement at its pin, carried by its tag and commit; HELD — stated and open, no terminal reaches it, '
         'carried by its name (the paper’s Placement :250). A source is a line of the paper; “Placement” and “Correspondence” name the paper’s own '
         'tables. %s' % ('Since `%s` the paper’s lines have changed in place at %s and none has been inserted or removed, so each source stands at '
                         'its number.' % (DRAFT_AT, ', '.join(':%d' % c for c in changed)) if changed else
                         'Since `%s` no line of the paper has moved.' % DRAFT_AT), '',
         '| S | the sentence at :15 | footing | source |', '|:--|:--|:--|:--|']
    for (n, _desc, foot, src), s in zip(rows, sents):
        C.append('| S%d | %s | %s | %s |' % (n, esc(s), esc(foot), esc(src)))
    kinds = dict(KERNEL=sum(1 for r in rows if r[2].startswith('KERNEL')), HELD=sum(1 for r in rows if r[2].startswith('HELD')))
    C += ['', '*Eighteen sentences, eighteen footed: KERNEL %d (S11, S12, S14, S17; S12 carries a HELD reading beside its terminal), HELD %d, a '
              'terminal’s reading 1 (S15), no claim 1 (S9) — the heads draft’s count (:30-:31).*' % (kinds['KERNEL'], kinds['HELD']), '']
    Y += ['### ### **SENTENCES 18 ; ROWS 18 ; KERNEL %d ; HELD %d ; THE DRAFT WRITTEN AS data/%s_companion.md.**' % (kinds['KERNEL'], kinds['HELD'], ACT)]
    print(NL.join(Y))
    if 'dry' not in a:
        put('%s_companion.md' % ACT, NL.join(C))
        put('%s_companion.txt' % ACT, NL.join(Y) + NL)


# ================================================================================ (5)(ii) THE LINT WITH THE WORD'S CLASS
def _lint_all(get_lines):
    import b714_pilot as PI
    out = []
    for p in SEVEN:
        lines = get_lines(p)
        for h in PI.lint(p, lines):
            h['file'] = p
            if h['cls'] == 'FOR THE AUTHOR':
                key = (p, h['line'])
                ln = lines[h['line'] - 1]
                if key in RULED and ln.lstrip().startswith('>') and hashlib.sha256(ln.encode('utf-8')).hexdigest() == RULED[key]:
                    h['cls'], h['why'] = 'AS DESIGNED', 'REPAIR RECORD: the banned stem quoted to name what was repaired (the author`s word, relay data/b716_author_answers.txt :13)'
            out.append(h)
    return out


def lint(*a):
    import b714_pilot as PI
    if a and a[0] == 'seed':
        for p, ln in (('day1/Silence_of_Foundations.md', 218), ('day1/Spectral_Inertness.md', 191)):
            l = (git(PP, 'show', 'b855623d:%s' % p) or '').split(NL)[ln - 1]
            print("    ('%s', %d): '%s'," % (p, ln, hashlib.sha256(l.encode('utf-8')).hexdigest()))
        return
    L = ['%s -- (R327)(5)(ii): THE SIX HITS SETTLED -- b714`S PROSE LINT OVER THE SEVEN AS THE WORKING TREE HOLDS THEM, WITH THE WORD`S CLASS (%s)' % (ACT, utc()), '',
         '### the matcher: tools/b714_pilot.py lint (b714`s P2, imported unedited; tools/banned_terms.py`s PAT and classify inside it, unedited),',
         '### and the class the word orders, REPAIR RECORD, granted to a FOR THE AUTHOR hit on a blockquoted line whose bytes the author ruled:',
         '### ' + ' ; '.join('%s :%d sha256 %s' % (p, ln, h[:16]) for (p, ln), h in sorted(RULED.items())),
         '### THE SEAT`S READING: the shared matcher tools/banned_terms.py is not in the (W) list of (R327)(9) and (N5) writes nothing beyond it, so',
         '### the class lives in this act`s lint; banned_terms.py is unedited (sha256 %s).' % hashlib.sha256(open(os.path.join(T, 'banned_terms.py'), 'rb').read()).hexdigest()[:16],
         '', '## THE CONTROLS, BEFORE THE FIGURES']
    planted = ['a line saying the RH proof stands here.', 'Not supportable: RH proved; h2_sign proved.', 'a line with no pattern.', 'a ' + 'bli' + 'nd spot in the text.']
    got = [[(h['what'], h['cls']) for h in PI.lint('planted.md', [p])] for p in planted]
    want = [[('RH proof', 'FOR THE AUTHOR')], [('RH proved', 'AS DESIGNED')], [], [('bli' + 'nd', 'FOR THE AUTHOR')]]
    ok = [got == want]
    L.append('  (L1) b714`s planted lines (its C5): %s -- %s' % (got, 'AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    base = lambda p: (git(PP, 'show', 'b855623d:%s' % p) or '').split(NL)   # noqa: E731
    pre = _lint_all(base)
    ruled = [h for h in pre if (h['file'], h['line']) in RULED]
    ok.append(len(ruled) == 3 and all(h['cls'] == 'AS DESIGNED' and h['why'].startswith('REPAIR RECORD') for h in ruled))
    L.append('  (L2) POS the three ruled hits at b855623d (Silence :218 twice, Spectral :191): %s -- %s' % (
        [(os.path.basename(h['file']), h['line'], h['what'], h['cls']) for h in ruled], 'REPAIR RECORD AS WANTED' if ok[-1] else 'NOT AS WANTED'))

    def plant(p):
        ls = base(p)
        if p == 'day1/Silence_of_Foundations.md':
            ls[217] = ls[217] + ' '
        return ls
    neg = [h for h in _lint_all(plant) if h['file'] == 'day1/Silence_of_Foundations.md' and h['line'] == 218]
    ok.append(len(neg) == 2 and all(h['cls'] == 'FOR THE AUTHOR' for h in neg))
    L.append('  (L3) NEG Silence :218 with one space appended (its bytes no longer the ruled ones): %s -- %s' % (
        [(h['what'], h['cls']) for h in neg], 'FOR THE AUTHOR AS WANTED' if ok[-1] else 'NOT AS WANTED'))
    fa_pre = [h for h in pre if h['cls'] == 'FOR THE AUTHOR']
    L.append('  (L4) the seven at b855623d with the class: FOR THE AUTHOR %d %s' % (len(fa_pre), [(os.path.basename(h['file']), h['line'], h['what']) for h in fa_pre]))
    L += ['', '## THE SEVEN AS THE WORKING TREE HOLDS THEM (after the edits of (5)(ii))']
    now = _lint_all(pp_lines)
    for h in now:
        L.append('  %s :%-4d %-9s | %-26s | %-14s | %s' % (os.path.basename(h['file']), h['line'], h['kind'], h['what'], h['cls'], h['why']))
    fa = [h for h in now if h['cls'] == 'FOR THE AUTHOR']
    L += ['', '### ### **CONTROLS %d OF %d ; HITS %d ; AS DESIGNED %d (REPAIR RECORD %d) ; FOR THE AUTHOR %d.**' % (
        sum(ok), len(ok), len(now), sum(1 for h in now if h['cls'] == 'AS DESIGNED'), sum(1 for h in now if h['why'].startswith('REPAIR RECORD')), len(fa))]
    print(NL.join(L))
    if 'dry' not in a:
        put('%s_lint.txt' % ACT, NL.join(L) + NL)


# ================================================================================ (6) THE ELEVEN NAMES
def kernels():
    out = []
    for d in sorted(os.listdir('D:/')):
        p = 'D:/' + d
        if d.startswith('SIDE-') and os.path.isdir(os.path.join(p, '.git')):
            tags = [t for t in (git(p, 'tag', '--sort=-v:refname') or '').split(NL) if re.match(r'^v\d+(\.\d+)*$', t)]
            if tags:
                out.append((d, p, tags[0], (git(p, 'rev-parse', '--short', tags[0] + '^{commit}') or '').strip()))
    return out


def statement(repo, rev, path, line):
    ls = (git(repo, 'show', '%s:%s' % (rev, path)) or '').split(NL)
    out = []
    for l in ls[line - 1:line + 40]:
        k = l.find(':=')
        if k >= 0:
            out.append(l[:k].rstrip())
            break
        if re.search(r'\bwhere\s*$', l) and out == []:
            out.append(l.rstrip())
            break
        out.append(l.rstrip())
        if re.search(r'\bwhere\s*$', l):
            break
    return out


def names(*a):
    import b714_pilot as PI
    import e0_rule as E0
    import inspect
    global GP
    GP = [p for p in inspect.signature(E0.grade).parameters if p != 'kind']
    K = kernels()
    L = ['%s -- (R327)(6): THE ELEVEN NAMES, EACH LOOKED UP AT EVERY LOCAL KERNEL`S CURRENT TAG, ITS STATEMENT AND ITS E0 GRADE (%s)' % (ACT, utc()), '',
         '### the names: relay data/b716_correspondence_pins.txt :24-:34. The kernels: every D:/SIDE-* clone with a vN tag, its current tag the',
         '### highest by version: ' + ' ; '.join('%s %s = %s' % (d, t, c) for d, _p, t, c in K),
         '### the lookup: tools/b714_pilot.py lookup (git grep for the declaration of the name`s last component at the tag; a field second).',
         '### the statement: git show <tag>:<path> from its line to its `:=` (a structure, class or inductive to its `where`). The grade: tools/e0_rule.py',
         '### grade from the statement alone, for a theorem or lemma; a def, structure, class, inductive or field is not graded and is named as such.',
         '### No axioms are read: no lean runs on this host (N1). e0_rule.grade%s, called with the statement and the kind.' % inspect.signature(E0.grade), '']
    found = 0
    rows = []
    for f, ln, name in NAMES:
        hits = []
        for d, p, t, c in K:
            h = PI.lookup(p, t, name)
            if h:
                hits.append((d, p, t, c, h))
        L.append('--- %s :%d  %s  -- found at %d kernel(s)' % (f, ln, name, len(hits)))
        if not hits:
            L.append('    MISSING at every current tag')
            rows.append(dict(file=f, line=ln, name=name, found=[]))
            L.append('')
            continue
        found += 1
        r = dict(file=f, line=ln, name=name, found=[])
        for d, p, t, c, h in hits:
            st = statement(p, t, h[0], h[1])
            first = st[0] if st else ''
            kind = h[2] if h[2] == 'field' else ((re.search(r'\b(theorem|lemma|def|abbrev|structure|class|instance|inductive|axiom|opaque)\b', first) or [None, '?'])[1]
                                                 if True else '?')
            if kind in ('theorem', 'lemma'):
                try:
                    hd = re.sub(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable)\s+)*(?:theorem|lemma)\s+\S+\s*', '',
                                ' '.join(x.strip() for x in st))   # ### the header after the name, as e0_rule reads it (its binder groups first)
                    g = E0.grade(**{GP[0]: hd, 'kind': kind})
                except Exception as e:   # noqa: BLE001
                    g = 'GRADE RAISED %s: %s' % (type(e).__name__, e)
            else:
                st = st[:1]           # ### a type former's head line alone (its constructors are no statement)
                g = 'not graded: %s %s' % ('an' if kind[0] in 'aeiou' else 'a', kind)
            L.append('    at   : %s %s = %s : %s :%d (%s ; the grep`s hits %d)' % (d, t, c, h[0], h[1], h[2], h[3]))
            L += ['    stmt : %s' % x for x in st]
            L.append('    kind %s ; GRADE %s' % (kind, g))
            r['found'].append(dict(kernel=d, tag=t, commit=c, path=h[0], line=h[1], kind=kind, grade=str(g), stmt=st))
        rows.append(r)
        L.append('')
    L.append('### ### **NAMES %d ; FOUND AT A CURRENT TAG %d ; MISSING %d.**' % (len(NAMES), found, len(NAMES) - found))
    print(NL.join(L))
    if 'dry' not in a:
        put('%s_names.txt' % ACT, NL.join(L) + NL)
        put('%s_names.json' % ACT, json.dumps(dict(at=utc(), kernels=K, rows=rows), indent=1, ensure_ascii=False) + NL)


# ================================================================================ THE CENSUS EDITION AND THE DIFFS
def edition(*a):
    p = os.path.join(PP, *CENSUS_NEW.split('/'))
    if os.path.exists(p):
        sys.exit('### %s EXISTS -- NOTHING WRITTEN' % CENSUS_NEW)
    r = subprocess.run(['git', '-C', PP, 'show', 'main:%s' % CENSUS_PREV], capture_output=True)
    if r.returncode or not r.stdout:
        sys.exit('### main:%s NOT READ -- NOTHING WRITTEN' % CENSUS_PREV)
    with open(p, 'wb') as fh:
        fh.write(r.stdout)
    print('  %s begun as main:%s`s bytes (%d bytes, sha256 %s)' % (CENSUS_NEW, CENSUS_PREV, len(r.stdout), hashlib.sha256(r.stdout).hexdigest()))


def diff(*a):
    h = (git(PP, 'rev-parse', 'HEAD') or '').strip()
    L = ['%s -- (R327)(5)-(6): THE EDITS ON PLACE-papers MAIN, EACH FILE`S WORKING BYTES AGAINST ITS BLOB AT HEAD %s (%s)' % (ACT, h[:8], utc()), '',
         '### --- the file at HEAD (a new file: nothing; the census v0.8.3: v0.8.2`s blob at HEAD), +++ the file as the Edit or Write tool left it;',
         '### written by tools/b717_words.py diff before the commit.', '']
    n = 0
    for f in WRITTEN:
        src = CENSUS_PREV if f == CENSUS_NEW else f
        a_ = git(PP, 'show', '%s:%s' % (h, src))
        a_ = a_.split(NL) if a_ is not None else []
        fp = os.path.join(PP, *f.split('/'))
        b_ = io.open(fp, encoding='utf-8').read().replace('\r', '').split(NL) if os.path.exists(fp) else []
        d = list(difflib.unified_diff(a_, b_, '%s at %s' % (src, h[:8]) if a_ else '/dev/null', '%s edited' % f, lineterm='', n=0))
        n += 1 if d else 0
        L += ['## %s : %s' % (f, ('%d diff lines' % len(d)) if d else 'UNCHANGED')] + d + ['']
    L.append('### ### **FILES %d ; WRITTEN %d.**' % (len(WRITTEN), n))
    print(L[-1])
    if 'dry' not in a:
        put('%s_words_diffs.txt' % ACT, NL.join(L) + NL)


def locate(rel, *needles):
    """`locate <PLACE-papers path> <needle> ...`: the line numbers carrying each needle (literal), each line's length and whether it opens
    `*Appended` -- numbers only, no text -> data/b717_locate.txt (appended per call); the lines then read by the Read tool."""
    ls = pp_lines(rel)
    L = ['%s -- locate in PLACE-papers %s (%d lines) at %s' % (ACT, rel, len(ls), utc())]
    for nd in needles:
        hits = [(i, len(l), l.startswith('*Appended')) for i, l in enumerate(ls, 1) if nd in l]
        L.append('  %r : yield %d : %s' % (nd, len(hits), hits[:40]))
    print(NL.join(L))
    p = os.path.join(D, '%s_locate.txt' % ACT)
    _membrane(p)
    with io.open(p, 'a', encoding='utf-8', newline='\n') as fh:
        fh.write(NL.join(L) + NL)


ROUTES = dict(head=head, companion=companion, lint=lint, names=names, edition=edition, diff=diff, locate=locate)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print(__doc__)
        sys.exit(2)
    fn(*sys.argv[2:])
