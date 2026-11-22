# -*- coding: utf-8 -*-
"""standing/act.py -- THE ACT, READ AT RUN TIME: the one source of the standing toolset's act figures, data/act_current.json, and the
readers every standing module shares (the chain, a bank now or at a commit, a root's named banks). No act's figure, name or object stands
here: the act, its neighbours and ranges are read from the file and from data/act_roots.txt at the call.

Extracted, not imported (the author's word (1)(a) of the toolset act): jl, rd, the git reader and the root's banks copied out of the
close's per-act tools and the shared modules they import (provenance: tools/b714_components_standin.py jl and sha; tools/act_root.py
sha256_file; tools/b698_record.py root_banks), with no import of a module whose name carries an act number.
"""
import hashlib
import json
import os
import re
import subprocess

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
NL = '\n'
# the ruling's PATHS: the repositories the close reads, by the step bank's repository keys
REPOS = dict(relay=RELAY, pp='D:/MY-DOwnloads/PLACE-papers')
NAMES = dict(relay='relay', pp='PLACE-papers')
CHAIN = os.path.join(D, 'act_roots.txt')
ACT_NAME = re.compile(r'^b\d{3}$')


def act_name(name, tool, usage=''):
    """v1.32.0, (R362)(7)(vii), b751 defect (t): A FLAG READ AS AN ACT. `wlist.py bank --quiet` took `--quiet` as its act and wrote
    data/--quiet_wlist.json. A tool that takes an act name refuses one that begins with a hyphen, before it reads or writes anything; the usage
    printed. Returns the name where it stands."""
    if isinstance(name, str) and name.startswith('-'):
        raise SystemExit('### REFUSED (v1.32.0, (R362)(7)(vii)): %s took %r in the act`s place -- a name beginning with a hyphen is a flag, not an act; '
                         'nothing read or written.%s' % (tool, name, ('\n' + usage) if usage else ''))
    return name


def current():
    """data/act_current.json, read now."""
    with open(os.path.join(D, 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)


def chain():
    """the chain's rows in order, each (act, root, previous root), read from data/act_roots.txt."""
    out = []
    for l in rd_path(CHAIN).split(NL):
        p = l.split()
        if len(p) == 3 and ACT_NAME.match(p[0]):
            out.append(tuple(p))
    return out


def prev_of(act):
    """the act before `act` on the chain, or, for the act not yet appended, the chain's last row's act."""
    acts = [r[0] for r in chain()]
    if act in acts:
        i = acts.index(act)
        return acts[i - 1] if i > 0 else None
    return acts[-1] if acts else None


def git(repo, *args):
    """a git read in a repository by its key, its stdout as bytes (None on a failure)."""
    r = subprocess.run(['git', '-C', REPOS.get(repo, repo)] + list(args), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def gs(repo, *args):
    b = git(repo, *args)
    return None if b is None else b.decode('utf-8', 'replace').replace('\r', '').strip()


def landed_entry(act, fj, rev='HEAD'):
    """v1.12.0, (R342)(2)(iv): the act's FINDINGS entry as it landed, keyed to the line data/<act>_findings.json banks, read from PLACE-papers at `rev`, as many bytes as the bank's `append` records (a later act's
    dated note under the entry is not the entry: b730's stands so), to the next heading at column 0 where it records none. The bank carries no `text` key, so N3's reader, reading that key, fell to the composer at
    b730 and b731 (b731 event (10)). The line must read the bank's head or this raises; it never falls to the composer."""
    b = git('pp', 'show', '%s:FINDINGS.md' % rev)
    if b is None:
        raise ValueError('landed_entry: %s: no FINDINGS.md at %s' % (act, rev))
    lines = b.decode('utf-8').split(NL)
    i = int(fj['line']) - 1
    if not 0 <= i < len(lines) or lines[i].rstrip() != conv(fj.get('head') or fj.get('title') or '').rstrip():   # ### v1.35.6, (R368)(1): conv below
        raise ValueError('landed_entry: %s: FINDINGS.md :%d does not read the bank`s head' % (act, i + 1))
    ap = fj.get('append') or {}
    if ap.get('added'):
        at = len(NL.join(lines[:i]).encode('utf-8')) + 1
        return b[at:at + int(ap['added']) - (1 if ap.get('prefix') else 0)].decode('utf-8').strip() + NL
    e = next((k for k in range(i + 1, len(lines)) if lines[k].startswith('## ')), len(lines))
    return NL.join(lines[i:e]).strip() + NL


# ### v1.35.6, (R368)(1), b757's halt at [22] (21:55:35Z, the entry's title composed with two backticks): the landing wrote the title's
# ### backticks as ’ and :82 compared the landed line with the bank's head raw, so b757's own entry did not read. :82 now passes the head
# ### through THE LANDING'S ONE CONVERSION, copied here from tools/b652_record.py :31 and :34-:37 (CONV and conv) and not imported: this
# ### module imports no module whose name carries an act number (:6-:8). tools/standing/v1356.py reads the copy against b652's on every line
# ### of FINDINGS.md.
CONV = re.compile(r'(?<=[A-Za-z0-9)])`(?=[a-z])')


def conv(t):
    """the landing's one conversion ((R262)(2)), copied from tools/b652_record.py: a backtick standing as an apostrophe -- after a letter, a
    digit or `)`, before a lower-case letter -- written ’."""
    return CONV.sub('’', t)


def entry_ends_with(text, line, conv):
    """v1.34.0, (R364)(3)(ix), b753's N3 at the close: whether the entry's last line not blank is the act module's line, BOTH SIDES THROUGH THE
    RECORD TOOL'S OWN CONVERTER (`conv`, b652's one conversion, the landing's, passed by the record module), one function for the composer's text
    and the landed entry. b753's module compared its constant raw: the composer's text before the lock read it equal (scores HELD) and the landed
    line, where the landing had turned the constant's backtick, read it not (scores close REFUTED)."""
    ls = [l for l in (text or '').split(NL) if l.strip()]
    return bool(ls) and conv(ls[-1].strip()) == conv((line or '').strip())


def blob(rev, rel, repo='relay'):
    """a file's bytes at a commit (None where the commit does not carry it)."""
    return git(repo, 'show', '%s:%s' % (rev, rel))


def rd_path(p):
    return open(p, encoding='utf-8', errors='replace').read().replace('\r', '') if os.path.isfile(p) else ''


def rd(name, rev=None):
    """a bank's text under relay data/, now or at a commit, CR removed ('' where absent)."""
    if rev is None:
        return rd_path(os.path.join(D, name))
    b = blob(rev, 'data/' + name)
    return '' if b is None else b.decode('utf-8', 'replace').replace('\r', '')


def jl(name, rev=None):
    t = rd(name, rev)
    try:
        return json.loads(t) if t.strip() else {}
    except ValueError:
        return {}


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    with open(p, 'rb') as f:
        return sha256_bytes(f.read())


def root_named(act):
    """the banks an act's root names, {relay path: sha256}: its root bank's `banks` map, or its `items` rows "data/<name> <sha256>"."""
    rj = jl('%s_act_root.json' % act)
    banks = dict(rj.get('banks') or {})
    for it in rj.get('items') or []:
        p = it.split(' ')
        if len(p) == 2 and p[0].startswith('data/'):
            banks.setdefault(p[0], p[1])
    return banks


def steps(act, rev=None):
    """the act's step bank rows (data/<act>_steps.json `rows`)."""
    return jl('%s_steps.json' % act, rev).get('rows') or []


def step_commit(act, phase, repo='relay'):
    """the last step row's commit of a phase in a repository (None where there is none)."""
    cs = [r['commit'] for r in steps(act) if r.get('phase') == phase and r.get('repo') == repo]
    return cs[-1] if cs else None


def answer_banks(act):
    """(R337)(2), b725 event (4): the answers pair and the answer check's output, written after the lock by design."""
    return ('data/%s_author_answers.txt' % act, 'data/%s_author_answers.json' % act, 'data/%s_answer_check.txt' % act)


def by_design(act):
    """v1.30.0, (R360)(3)(ii), b749 events (4)-(6): THE FILES WRITTEN AFTER THE LOCK BY DESIGN, each appended by its tool and none edited by
    hand -- the answers pair and the answer check's output (`record answers`), the author-words banks (tools/standing/append.py) and the post-lock
    scan banks (the one-call tool's scan). The hook's row (65) refuses an Edit or Write of them after the lock; N4's clause reads the same list
    through post_lock_appended. v1.34.0, (R364)(3)(v): the post-seal events bank data/<act>_events_postseal.txt, which the close writes by
    design (b751's refusal entered by data/b752_corrigendum.txt :68; b752's refusals :26, :27; b753's events (14)); the events bank itself is
    not on the list, so N4 reads a hand edit of it after the lock as an edit."""
    return answer_banks(act) + ('data/%s_author_words.txt' % act, 'data/%s_author_words_preseal.txt' % act,
                                'data/%s_address_scan_postlock.txt' % act, 'data/%s' % scan_commits_name(act), 'data/%s_events_postseal.txt' % act)


def post_lock_appended(act):
    """the banks written after the lock by design, outside the lock's hash set and N4's read; the lock gate prints them by name. v1.30.0: the
    design list (by_design) whole, the author-words banks with it."""
    base = ('data/%s_steps.json' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act, 'data/%s_address_scan_postlock.txt' % act,
            'tools/mirror_prevbuild.json', 'data/%s' % scan_commits_name(act)) + answer_banks(act)
    return base + tuple(p for p in by_design(act) if p not in base)


# ### v1.38.0, (R374)(5) [K10], b763's finding 10 (relay data/b764_events.txt (22)): STEP [21] AGAINST N4. v5 row (79)'s step [21] reads "the
# ### events bank (an event found after it appended by the Edit tool before the closing) (data/<act>_events.txt)", a bank tracked at the lock;
# ### N4's clause (the act's post-lock reader, less post_lock_appended) reads a commit touching it after the lock as an edit, and b763's [21]
# ### commit d784c1da refuted N4, against the rule the closing message cites ((R365)(2)(ii), (R366)(1)(ii)). The standing clauses' bank is not
# ### rewritten ((R374)(12)): the close order the seat reads (`fold.py record closeorder`) takes its step [21] from STEP_21, which names the bank
# ### written after the lock by design (by_design's last, appended by tools/standing/append.py's `events` kind) and the closing message. The
# ### row's own evidence for [21] (data/<act>_events.txt, present at every act) still stands under close_refuses, so no lower-step reading moves.
STEP_21 = (21, 'what is found after the lock, entered in the bank written after the lock by design by `tools/standing/append.py <act> events '
               '<source>` and by no hand, no bank tracked at the lock written (N4), and printed with its times in the closing message; where '
               'nothing is found, no bank written', 'data/<act>_events_postseal.txt')


# ### v1.38.10, (R374)(5) [K11], finding 3 of b763's closing message (relay data/b764_events.txt (15)), b763 events (21) and (96), b762 events
# ### (18): THE POST-LOCK ADDRESS SCAN'S PLACE AGAINST THE SEAL, BY ONE WRITTEN RULE. No row ordered the scan against close.py's seal route:
# ### b758, b759 and b760 ran it before the route, b761, b762 and b763 after it and before the seal commit, each seal commit from b759 carrying
# ### its bank. THE RULE: the post-lock address scan runs after close.py's seal route has written data/<act>_seal_hashes.json and before the
# ### seal commit, which carries its bank, so the scan reads the seal record among the act's writes. The close order the seat reads takes it as
# ### step [8a]; the one-call tool's seal commit refuses where the post-lock bank holds no run stamped at or after the seal record's time, or
# ### where that bank is not staged with the seal (postlock_place, read by tools/standing/commit.py's postlock_refusal). The standing clauses'
# ### bank is not rewritten ((R374)(12)); the row's own steps and their evidence stand as they are, so no lower-step reading moves.
STEP_8A = ('8a', 'the post-lock address scan, after close.py`s seal route has written the hashes and before the seal commit, which carries '
                 'its bank: `tools/<act>_address_scan.py scan --bank`, a run stamped at or after the seal record`s time, refused at the seal '
                 'commit otherwise ((R374)(5) [K11])', 'data/<act>_address_scan_postlock.txt')
POSTLOCK_RUN = re.compile(r'^## THE RUN AFTER THE LOCK, (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', re.M)


def postlock_place(act, seal_at, bank_text, staged):
    """v1.38.10, (R374)(5) [K11]: the post-lock scan in its place at the seal commit, pure in its arguments -- the seal record's `at`, the
    post-lock bank's text ('' where absent) and the names staged for the seal commit. Returns (ok, why)."""
    runs = POSTLOCK_RUN.findall((bank_text or '').replace('\r', ''))
    bank = 'data/%s_address_scan_postlock.txt' % act
    if not seal_at:
        return False, 'the seal record carries no time'
    after = [r for r in runs if r >= seal_at]
    if not after:
        return False, 'the post-lock bank holds no run stamped at or after the seal record`s time %s (its runs: %s)' % (seal_at, ', '.join(runs) or 'NONE')
    if bank not in set(staged or ()):
        return False, '%s is not staged with the seal (its run of %s)' % (bank, after[-1])
    return True, 'the run of %s, at or after the seal record`s %s, its bank staged with the seal' % (after[-1], seal_at)


# ### v1.38.24, (R376)(7) [K24], data/b765_misses.txt (9), b765 post-seal rows (87)-(88), data/b765_put_3.json: THE PROJECT SET'S BUILD IN
# ### THE CLOSE'S ORDER. (R375)(7) set the build at the record commit; b765 built after PLACE-papers' pre-root push, from an export of its
# ### own made by tools/project_set.py's mirror route, and its three banks, written after the relay's pre-root push, stood outside a commit
# ### when root part 1 read them (150 of 153, READY False). The build takes step [23a]: after the mirror [23], from that step's export, the
# ### one carrying the root line (tools/project_set.py close_export, read from data/<act>_mirror.json), so that the Project's repository
# ### equals that export file for file by md5; its banks are committed with the mirror's by the closing commit [25], and the one-call tool
# ### refuses any relay commit while one of them stands written and untracked (tools/standing/commit.py close_left_out). The standing
# ### clauses' bank is not rewritten ((R376)(10)); [25] keeps its evidence and its number, so no lower-step reading moves.
STEP_23A = ('23a', 'the Project set from [23]`s export, root line in it, banks committed at [25] ([K24]): `tools/project_set.py branch`, '
                   '`write` and `commit`, the gated push of push-<act>-set, then `readback`; the repository equal to that export file for '
                   'file by md5 ((R376)(7))', 'data/<act>_project_set_build.txt')
STEP_25_WORDS = 'the closing and its push, captured, the commit carrying [23]`s and [23a]`s banks ([K24])'
CLOSE_COMMITS = (19, 25)   # ### v1.38.24, [K24]: the relay's commits of the close after the root, the record commit and the closing commit


def project_set_banks(act):
    """v1.38.24, (R376)(7) [K24]: the banks tools/project_set.py and the gated push of push-<act>-set write (the build's json and its
    rendering, the push's capture; the control's, the verifier's and the repository's banks where their routes run)."""
    return tuple('data/%s_%s' % (act, n) for n in ('project_set_build.json', 'project_set_build.txt', 'project_set_verify.txt',
                                                   'project_set_control.txt', 'project_set_repo.json',
                                                   'PLACE-project-set_push-%s-set_push_out.txt' % act))


def close_carried(act):
    """v1.38.24, (R376)(7) [K24]: the banks the closing commit [25] carries -- the mirror's of [23] (the record tool's mbuild, mroot, mverify
    and mbank, as b765's closing commit c90a62d7 carried them) and the Project set's of [23a]."""
    return tuple('data/%s_%s' % (act, n) for n in ('mirror.txt', 'mirror.json', 'mirror_build.json', 'mirror_root.json',
                                                   'mirror_verify.txt')) + project_set_banks(act)


def close_order(text=None):
    """v1.38.0, (R374)(5) [K10]: the close order as the seat reads it -- tools/act_close.py close_steps_printed (v5 row (79), with [5a] and
    [7a]), its step [21] taken from STEP_21. v1.38.10 ([K11]): step [8a], the post-lock address scan's place (STEP_8A), after [8]. v1.38.24
    ([K24]): step [23a], the Project set's build (STEP_23A), after [23], and [25]'s words naming the banks its commit carries. [(n, words,
    evidence)]; pure in the row's text."""
    import sys as _sys
    if T not in _sys.path:
        _sys.path.append(T)
    import act_close as _AC
    out = []
    for s in _AC.close_steps_printed(text):
        if s[0] == 21:
            out.append(STEP_21)
        elif s[0] == 25:
            out.append((25, STEP_25_WORDS, s[2]))
        else:
            out.append(s)
        if s[0] == 8:
            out.append(STEP_8A)
        if s[0] == 23:
            out.append(STEP_23A)
    return out


def close_dry(act, order=None):
    """v1.38.24, (R376)(7) [K24]: a dry run of the close's order over the builder's banks; nothing run, nothing written. Each step taken in
    its order: the step whose evidence is the build's bank (STEP_23A's) writes the three banks the build writes at every close (its json,
    its rendering and the push's capture); the root [14] reads each bank written before it as outside a commit (root part 1 wants every
    named bank clean and equal at HEAD, tools/standing/rootparts.py :104, :150); a relay commit step of CLOSE_COMMITS carries each bank
    written before it. Returns dict(slot, carried_at, at_root, outside): the build's step, the commit step that first carries its banks, the
    banks the root reads outside a commit and the banks no commit carries. Pure in `order` (the close order as printed where None)."""
    order = close_order() if order is None else order
    three = ('data/<act>_project_set_build.json', 'data/<act>_project_set_build.txt', 'data/<act>_PLACE-project-set_push-<act>-set_push_out.txt')
    written, carried, at_root, slot, carried_at = [], set(), [], None, None
    for k, _w, e in order:
        if e == STEP_23A[2]:
            slot = k
            written += [b.replace('<act>', act) for b in three]
        if k == 14:
            at_root = [b for b in written if b not in carried]
        if k in CLOSE_COMMITS and written and not carried >= set(written):
            carried |= set(written)
            carried_at = k if carried_at is None else carried_at
    return dict(slot=slot, carried_at=carried_at, at_root=at_root, outside=[b for b in written if b not in carried])


APPEND_HEAD = '## APPENDED BY %s AT %s: %d LINE(S); NO LINE ALREADY IN THE BANK REWRITTEN'


# ### v1.32.0, (R362)(7)(iv), b751 events (4): THE APPEND KEYED ON PLACE AND WORDS. A row of the answers bank opens on a heading that names its place
# ### (a word's or a message's transcript line; a call's tool-use id, line and time); a block whose heading is not in the bank is a new row and is
# ### appended whole, its text lines included even where an earlier row carries the same words (b751's go of 16:47:23Z, word for word line 20339's).
# ### A block whose heading stands keeps the line-keyed append of v1.30.0: its lines not already in the bank appended, none rewritten.
KEYED_HEADS = ('### THE AUTHOR`S WORD (transcript line ', '### THE AUTHOR`S MESSAGE (transcript line ', '### CALL tool-use id ')


def answers_append(prior, lines, stamp, tool='`record answers`'):
    """v1.30.0, (R360)(3)(i), b749 events (4): the answers route appends. `prior` the bank's text as it stands ('' where none), `lines` the route's
    composed lines. Where no bank stands the composed lines are the bank. Otherwise every line of the bank is kept where it stands, and the
    composed lines not already in it are appended beneath one head; a line already in the bank is never rewritten, moved or dropped (the [Z1]
    sitting block committed at relay 1858213d stays at its rows). Returns (text, appended): the text ends with one newline, appended the
    count of lines added (0: the bank stands unchanged, nothing to write)."""
    lines = [l.replace('\r', '') for l in lines]
    if not (prior or '').strip():
        return NL.join(lines).rstrip(NL) + NL, len([l for l in lines if l.strip()])
    P = prior.replace('\r', '').rstrip(NL).split(NL)
    have = set(l for l in P if l.strip())
    new, blank = [], False
    whole = False   # ### v1.32.0, (R362)(7)(iv), b751 events (4): inside a block whose keyed heading is new, every line is appended
    for l in lines:
        if l.strip() and l.startswith(KEYED_HEADS):
            whole = l not in have
        if l.strip() and l in have and not whole:
            continue
        if not l.strip():
            whole = False
            if new and not blank:
                new.append('')
            blank = True
            continue
        new.append(l)
        blank = False
    while new and not new[-1].strip():
        new.pop()
    if not new:
        return NL.join(P) + NL, 0
    n = len([l for l in new if l.strip()])
    return NL.join(P + ['', APPEND_HEAD % (tool, stamp, n)] + new) + NL, n


def words_append(prior, text, stamp, src):
    """v1.30.0, (R360)(3)(ii), (iv): an author-words bank appended by its tool (tools/standing/append.py): the bank as it stands, then one head
    naming the source and its sha256, then the words verbatim. Nothing in the bank is rewritten. Returns the new text."""
    body = (text or '').replace('\r', '').rstrip(NL)
    head = '## APPENDED BY tools/standing/append.py AT %s FROM %s (sha256 %s), VERBATIM:' % (
        stamp, src, hashlib.sha256(body.encode('utf-8')).hexdigest()[:16])
    pre = (prior or '').replace('\r', '').rstrip(NL)
    return (pre + NL + NL if pre else '') + head + NL + body + NL


def author_words_section(act, dd=None):
    """v1.30.0, (R360)(3)(iv), b749 events (9): the section the closing, record and trail tools print for the author's words after the seal,
    composed from its bank. The bank is appended after the root by design (by_design, tools/standing/append.py) and read apart: before the
    root, with no bank, the sentence says it is composed at the close and not yet composed -- never NONE RECEIVED, which b749's record and
    trail printed before the root while the words were being received; after the root, the shared reader (tools/act_close.py) as before."""
    import sys
    if T not in sys.path:
        sys.path.insert(0, T)
    import act_close as AC_
    dd = dd or D
    if AC_.author_words(act, dd) is None and not os.path.exists(os.path.join(dd, '%s_act_root.json' % act)):
        return [AC_.AUTHOR_WORDS_HEAD + ' (data/%s_author_words.txt): COMPOSED AT THE CLOSE FROM ITS BANK, which is appended after the root by '
                                        'design and read apart; not yet composed' % act]
    return AC_.author_words_section(act, dd)


SITTING_ROW = re.compile(r'^\[(?:[A-Z]\d*|\(\d+\))\] (?:PASS|STRIKE|PASSED|STRUCK)\b', re.M)


def question_count(text):
    """v1.30.0, (R360)(3)(vii), b749 defect (u), events (6): the questions put, counted from the composed prompts' rows (`### PROMPT n` under a
    `### CALL` of the answers bank), the sitting rows (`[Z1] PASS ...`, b736's form) read apart and not added. Returns dict(prompts, calls,
    sitting). b749's file at its close: prompts 2, sitting 1 (the count of b749's module read 3)."""
    t = (text or '').replace('\r', '')
    return dict(prompts=len(re.findall(r'(?m)^### PROMPT \d+ ', t)), calls=len(re.findall(r'(?m)^### CALL ', t)), sitting=len(SITTING_ROW.findall(t)))


ZENODO_WRITE = re.compile(r'(?im)^(?:[^\n]*?\b)?(POST|PUT|PATCH|DELETE)\b[^\n]*?(?:zenodo|deposit|/records?/|/actions/)[^\n]*$')
ZENODO_RELEASE = re.compile(r'(?i)/actions/(?:publish|newversion|edit)\b|\bgh\s+release\s+create\b|\bgh\s+repo\s+edit\b')


def zenodo_banks(act, dd=None):
    """v1.30.0, (R360)(3)(vi): the act's Zenodo banks, data/<act>_zenodo*.txt, by name (none where the act wrote none)."""
    dd = dd or D
    try:
        return sorted(f for f in os.listdir(dd) if f.startswith('%s_zenodo' % act) and f.endswith('.txt'))
    except OSError:
        return []


def zenodo_requests(act, dd=None, texts=None):
    """v1.30.0, (R360)(3)(vi), b749 defects (l), (q), (t): N5's matcher reads a release, a new version, a publish or a repository edit from the
    act's Zenodo banks alone -- the request lines they bank -- and from no other text: "the draft held at v5" is the monograph's manuscript
    draft and names no Zenodo object; a search's own pattern in a captured command is no request. `texts` {name: text} given, those are read
    in place of the files. Returns dict(banks, writes [(bank, line, method, text)], releases [(bank, line, text)])."""
    dd = dd or D
    if texts is None:
        texts = dict((f, rd_path(os.path.join(dd, f))) for f in zenodo_banks(act, dd))
    writes, releases = [], []
    for f in sorted(texts):
        for i, l in enumerate((texts[f] or '').replace('\r', '').split(NL), 1):
            m = ZENODO_WRITE.match(l)
            if m:
                writes.append((f, i, m.group(1).upper(), l.strip()[:160]))
            if ZENODO_RELEASE.search(l):
                releases.append((f, i, l.strip()[:160]))
    return dict(banks=sorted(texts), writes=writes, releases=releases)


def shared_edits(act, base, head='HEAD', root=None):
    """v1.30.0, (R360)(3)(x), b749 defect (k): data/act_current.json's shared_edits written from this act's own list -- the tools this act's
    commits changed between `base` (the act's entering relay head) and `head`, under tools/ and outside the act's own (tools/<act>_*), the
    act modules (tools/acts/) and the standing tools (tools/standing/); never carried from the previous act's file."""
    root = root or RELAY
    r = subprocess.run(['git', '-C', root, 'diff', '--name-only', '%s..%s' % (base, head), '--', 'tools/'], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return sorted(p for p in r.stdout.split(NL) if p.strip() and not p.startswith(('tools/%s_' % act, 'tools/acts/', 'tools/standing/')))


def scan_commits_name(act):
    """v1.29.0, (R359)(3)(ii), b748 defect (r): the per-commit scan's own appended bank. The one-call tool's scan before each commit is written
    here, every run beneath the earlier, so the act's scan bank (written once at its step) and the post-lock bank (after the lock) are not
    rewritten by a commit and the root's dry run reads them as committed."""
    return '%s_address_scan_commits.txt' % act


def scan_commits_append(prior, stamp, what, text):
    """the commits bank's text: each scan beneath the earlier, headed by its time and the commit it stood before."""
    return (prior or '') + ('' if not prior else '\n') + '## THE SCAN BEFORE THE COMMIT, %s, %s\n' % (stamp, what) + text.rstrip('\n') + '\n'


def scan_bank_name(act, locked):
    """v1.9.0, (R339)(2)(v): the scan's bank before the lock and its bank after it: the lock freezes the first, so a run after the lock lands in the second, in the same form."""
    return '%s_address_scan%s.txt' % (act, '_postlock' if locked else '')


def scan_append(prior, stamp, text):
    """the post-lock bank's text: each run beneath the earlier, its bank form whole, none rewritten."""
    return (prior or '') + ('' if not prior else '\n') + '## THE RUN AFTER THE LOCK, %s\n' % stamp + text + '\n'


def stamped_name(d, name, exists=os.path.exists):
    """v1.11.0: a stamped route's bank name: <name> where it does not stand, else <stem>_rerun<n><ext>, the first free n: the stamp stands and the re-run is kept beside it, the first bank unedited."""
    if not exists(os.path.join(d, name)):
        return name
    stem, ext = os.path.splitext(name)
    n = 1
    while exists(os.path.join(d, '%s_rerun%d%s' % (stem, n, ext))):
        n += 1
    return '%s_rerun%d%s' % (stem, n, ext)


def first_stamp(prev, now):
    """(R337)(2), b726 event (3): the time of a bank's first banking, kept through a re-bank; prev the bank's json as it stands, {} where absent."""
    return (prev or {}).get('first_at') or (prev or {}).get('at') or now


def shared_tools_changed(repo, base, act):
    """(R337)(2), b726 event (2): the tools outside the act's own files and the standing toolset that git shows changed from base to HEAD, as
    tools/<name>, sorted: what data/act_current.json's shared_edits must name."""
    out = subprocess.run(['git', '-C', repo, 'diff', '--name-only', base, 'HEAD', '--', 'tools/'], capture_output=True, text=True,
                         encoding='utf-8', errors='replace').stdout.split()
    return sorted(p for p in out if not p.startswith(('tools/%s_' % act, 'tools/acts/', 'tools/standing/')))


def chain_in_time(head, chain, tail, ct):
    """v1.38.20, (R375)(8) [K21], b764's post-seal row (73) (data/b764_events_postseal.txt :30): THE ACT'S RELAY CHAIN READ IN TIME ORDER, THE
    LOCK GATE'S CARRY AMONG IT. `head` (key, commit) first -- the standing clauses' commit -- then the worklist's CHAIN in its own order, with
    each (key, commit) of `tail` (the passed bank, the handoff page, the lock gate's carry) that is set and not already in CHAIN placed by its
    commit time among them: after every commit of no later time, before the first of a later time at the chain's end. ct(commit) -> its
    commit time (seconds), None where it does not resolve; a tail commit with no time goes at the end. CHAIN's own order is not changed, so
    the arm's ancestry pairs still read it. Before v1.38.20 an act module appended the tail after CHAIN in a fixed order (passed, handoff,
    lock gate), and b764's lock gate carry ec439ca3 (00:27:48Z), absent from its CHAIN, was read after its handoff 6d4d47f5 (03:03:26Z): the
    times out of order and the pair handoff -> lock gate no ancestor, G-COEFFS-LAW failing beyond the face."""
    out = list(chain)
    have = set((h_ or '')[:8] for _k, h_ in out)
    for k_, h_ in tail:
        if not h_ or h_[:8] in have:
            continue
        t_ = ct(h_)
        i_ = len(out)
        if t_ is not None:
            while i_ > 0:
                p_ = ct(out[i_ - 1][1])
                if p_ is None or p_ <= t_:
                    break
                i_ -= 1
        out.insert(i_, (k_, h_))
        have.add(h_[:8])
    return [head] + out


def keys_in_time(order, extra, t):
    """v1.38.20, (R375)(8) [K21]: the arm's keys in time order: the worklist's TIME_ORDER as written, then each key of `extra` (the tail keys
    chain_in_time() placed, in the chain's order) not already in it, placed by its time in `t` {key: time} after every key of no later time;
    a key with no time goes at the end. TIME_ORDER's own order is not changed, so the arm still reads it against the times. Before v1.38.20
    the tail keys followed TIME_ORDER in the chain's fixed order."""
    out = list(order)
    for k_ in extra:
        if k_ in out:
            continue
        t_ = t.get(k_)
        i_ = len(out)
        if t_ is not None:
            while i_ > 0:
                p_ = t.get(out[i_ - 1])
                if p_ is None or p_ <= t_:
                    break
                i_ -= 1
        out.insert(i_, k_)
    return out
