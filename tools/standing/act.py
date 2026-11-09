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
    if not 0 <= i < len(lines) or lines[i].rstrip() != (fj.get('head') or fj.get('title') or '').rstrip():
        raise ValueError('landed_entry: %s: FINDINGS.md :%d does not read the bank`s head' % (act, i + 1))
    ap = fj.get('append') or {}
    if ap.get('added'):
        at = len(NL.join(lines[:i]).encode('utf-8')) + 1
        return b[at:at + int(ap['added']) - (1 if ap.get('prefix') else 0)].decode('utf-8').strip() + NL
    e = next((k for k in range(i + 1, len(lines)) if lines[k].startswith('## ')), len(lines))
    return NL.join(lines[i:e]).strip() + NL


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
    through post_lock_appended."""
    return answer_banks(act) + ('data/%s_author_words.txt' % act, 'data/%s_author_words_preseal.txt' % act,
                                'data/%s_address_scan_postlock.txt' % act, 'data/%s' % scan_commits_name(act))


def post_lock_appended(act):
    """the banks written after the lock by design, outside the lock's hash set and N4's read; the lock gate prints them by name. v1.30.0: the
    design list (by_design) whole, the author-words banks with it."""
    base = ('data/%s_steps.json' % act, 'data/%s_bank_hashes.json' % act, 'data/%s_hook_refusals.txt' % act, 'data/%s_address_scan_postlock.txt' % act,
            'tools/mirror_prevbuild.json', 'data/%s' % scan_commits_name(act)) + answer_banks(act)
    return base + tuple(p for p in by_design(act) if p not in base)


APPEND_HEAD = '## APPENDED BY %s AT %s: %d LINE(S); NO LINE ALREADY IN THE BANK REWRITTEN'


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
    for l in lines:
        if l.strip() and l in have:
            continue
        if not l.strip():
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
