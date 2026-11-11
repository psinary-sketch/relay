"""b753 -- (R363)(6) as the author's second amendment (3) keeps it: THE AGENDA OF THE TWO KEPT ITEMS, [M1] AND [D1], EVERY CURRENT READ AND
EVERY DRAFT BANKED BEFORE EITHER IS PUT (data/b753_agenda.txt). b736's form: CURRENT read from the files, DRAFTED here, passed or struck.

    python -X utf8 -u tools/b753_agenda.py control     the controls alone
    python -X utf8 -u tools/b753_agenda.py dry         composed and printed, nothing banked
    python -X utf8 -u tools/b753_agenda.py run         composed and banked; refuses unless this file is committed and clean

It reads PLACE-papers' tree at main, the roster by tools/standing/roster.py, the builder's state file, the harness's settings (three keys of
them), this session's and b752's transcripts by tools/standing/chain.py (the version and the model of their rows, no content), two cited tool
lines and the store bank's closing line. It writes its bank and nothing else: no roster, no setting, no rules bank.
"""
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
import chain
import roster

ACT = 'b753'
BANK = os.path.join(RELAY, 'data', '%s_agenda.txt' % ACT)
SETTINGS = 'C:/Users/echo chamber/.claude/settings.json'
THIS, B752 = '5a4228ab-091d-4515-b5ab-95a5e34e1e18', chain.B752
# ### (R363)(6)[M1]'s seven names, in the ruling's order
FAMILIES = ('THE_EPSTEIN_CONTROL_OBJECT', 'CERTIFIED_EVALUATION_IN_THE_STRIP', 'THE_EULER_SPECIFICATION', 'W_SIGN2_DH_CONTRAST', 'MECHANISM_EXCLUSION',
            'THE_EXCLUSION_ARCHITECTURE', 'DOMAIN_OSTROWSKI_UNIVERSALITY')
VER = re.compile(r'_v\d+(?:_\d+)*$')


def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def src(rel):
    return io.open(os.path.join(RELAY, rel), encoding='utf-8', errors='replace').read().split('\n')


def paths_of(name, tree):
    """main's paths whose file name, its version suffix apart, is `name` exactly: (outside archive/, under archive/)."""
    hit = [p for p in tree if p.endswith('.md') and VER.sub('', os.path.basename(p)[:-3]) == name]
    return [p for p in hit if not p.startswith('archive/')], [p for p in hit if p.startswith('archive/')]


def m1(tree):
    base = roster.base()
    r, joins, leaves, nj = roster.resolve(base, tree)
    state = json.load(io.open(os.path.join(T, 'mirror_prevbuild.json'), encoding='utf-8-sig'))
    flat = [os.path.basename(p) for p in r]
    rows = []
    for n in FAMILIES:
        live, arch = paths_of(n, tree)
        rows.append((n, live, arch))
    return dict(base=base, roster=r, joins=joins, leaves=leaves, nj=nj, state=state, flat=flat, rows=rows)


def d1():
    s = json.load(io.open(SETTINGS, encoding='utf-8'))
    here, prev = chain.path_of(THIS), chain.path_of(B752)
    return dict(model_word=s.get('model'), channel=s.get('autoUpdatesChannel'), env=sorted((s.get('env') or {}).keys()),
                windows=sorted((k, v.get('autoCompactWindow')) for k, v in (s.get('modelSettings') or {}).items()),
                effort=s.get('effortLevel'), retention=s.get('cleanupPeriodDays'),
                v_here=chain._version(here), v_prev=chain._version(prev), models=chain.models(here), models_prev=chain.models(prev))


def controls(M, D):
    L, ok = ['## THE CONTROLS, printed before any current word or draft'], [True]

    def case(what, got, want):
        good = got == want
        ok[0] = ok[0] and good
        L.append('  %s: %r %s' % (what, got, 'AS WANTED' if good else '### NOT AS WANTED, wanted %r' % (want,)))
    case('([M1]) each of the seven names resolves to one path on main outside archive/', [len(live) for _n, live, _a in M['rows']], [1] * 7)
    case('([M1]) none of the seven paths is in the roster as the builder reads it; none`s flat name is one the roster already carries',
         (sum(1 for _n, live, _a in M['rows'] for p in live if p in M['roster']), sum(1 for _n, live, _a in M['rows'] for p in live if os.path.basename(p) in M['flat'])), (0, 0))
    case('([M1]) the name rule on planted paths: an exact name with a version suffix found, a longer name holding it not', (
        paths_of('MECHANISM_EXCLUSION', ['a/MECHANISM_EXCLUSION_v0_2.md', 'a/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'archive/x/MECHANISM_EXCLUSION.md'])),
        (['a/MECHANISM_EXCLUSION_v0_2.md'], ['archive/x/MECHANISM_EXCLUSION.md']))
    case('([M1]) the roster, the builder`s state file and b752`s build agree at 75 (data/b752_mirror.txt :3 reads "files 75")',
         (len(M['roster']), len(M['state']['files']), any('files 75' in l for l in src('data/b752_mirror.txt')[:5])), (75, 75, True))
    case('([D1]) the settings read: a model word, an update channel, a window per model entry', (bool(D['model_word']), bool(D['channel']), all(w for _k, w in D['windows'])), (True, True, True))
    case('([D1]) this session`s rows name a harness version and at least one model; b752`s session a version', (D['v_here'] != '-', len(D['models']) >= 1, D['v_prev'] != '-'), (True, True, True))
    a, b = src('tools/standing/v1170.py')[23], src('tools/b752_worklist.py')[32]
    case('([D1]) the two cited lines carry the two forms of the scratch folder`s parent: tools/standing/v1170.py :24 "D--", tools/b752_worklist.py :33 sixteen hexadecimal characters',
         ('/Temp/claude/D--/' in a, bool(re.search(r'/Temp/claude/[0-9a-f]{16}/', b))), (True, True))
    case('([D1]) the store read`s bank stands with its closing line', any(l.startswith('### ### **THE STORE READ: SESSIONS ') for l in src('data/b753_store.txt')), True)
    L.append('  ### THE CONTROLS: %d ; %s' % (len(L) - 1, 'ALL AS WANTED' if ok[0] else '### NOT ALL AS WANTED'))
    return ok[0], L


def compose(gen):
    pp = subprocess.run(['git', '-C', roster.A.PP if hasattr(roster.A, 'PP') else 'D:/MY-DOwnloads/PLACE-papers', 'rev-parse', '--short=8', 'main'], capture_output=True, text=True).stdout.strip()
    tree = roster.main_tree()
    M, D = m1(tree), d1()
    ok, C = controls(M, D)
    r, base, st = M['roster'], M['base'], M['state']
    add = [live[0] for _n, live, _a in M['rows'] if len(live) == 1]
    L = ['%s -- THE AGENDA OF THE TWO KEPT ITEMS, [M1] AND [D1]: EVERY CURRENT READ AND EVERY DRAFT, BANKED BEFORE EITHER IS PUT (%s; generator tools/%s_agenda.py at relay %s)' % (ACT, stamp(), ACT, gen), '',
         '### (R363)(6) as the author`s second amendment (3) keeps it (relay data/b753_author_words_preseal.txt :23): "Kept, put after the reads: [M1] and [D1]"; [C1], [H1], [M2],',
         '### [L1] and onward are the sitting`s opening items and are not drafted here. b736`s form: CURRENT read from the files (PLACE-papers main %s), DRAFTED here, each' % pp,
         '### passed or struck by number, through the composer. Nothing below is done by this bank: no roster, no rules bank and no setting is written until an item passes.', ''] + C + ['']

    # ---------------- [M1]
    dupes = sorted(set(x for x in M['flat'] if M['flat'].count(x) > 1))
    L += ['## [M1] THE ARCHIVE`S ROSTER GAINS FAMILIES, by a ruling as data/b715_rules.txt (1) asks ("a new family enters only by a ruling", :7)', '',
          '[M1] FILE tools/standing/roster.py (the rule`s reader) and a new list beside tools/mirror_roster.json (the b707 roster, kept unedited) ; a row of data/b753_rules.txt',
          '  CURRENT: the roster as the builder reads it from PLACE-papers main %s: the base roster %d entries in %d families ; the roster %d entries ; joins %d, leaves %d, editions not joined %d' % (
              pp, len(base), len(set(roster.family(p) for p in base)), len(r), len(M['joins']), len(M['leaves']), len(M['nj']))]
    L += ['    JOINS %s  (%s)' % (p, why) for p, _f, why in M['joins']]
    L += ['  THE COUNT IN ONE LINE: the archive of b752 holds 76 files = the roster`s %d and MANIFEST.md ; the builder`s state file (tools/mirror_prevbuild.json, lastChanged %s) holds %d names, equal to the build`s 75 --' % (
        len(r), st.get('lastChanged'), len(st['files'])),
        '    ### the ruling`s "state file`s 74" DIFFERS from the file, which reads %d; 74 is reproduced as the roster`s distinct file names (%d): %s is carried twice by its name, once from the root and once from a' % (
            len(st['files']), len(set(M['flat'])), ', '.join(dupes) or '-'),
        '    folder of archive/, which the builder flattens to a name of its own (%s). The state file is the previous build`s staged names (tools/mirror_build.ps1 :85-:89), not the roster.' % (
            ', '.join(sorted(set(st['files']) - set(M['flat']))) or '-'),
        '  THE SEVEN, each at the path read on main %s (the name exactly, a version suffix apart; a copy under archive/ printed and not taken):' % pp]
    for n, live, arch in M['rows']:
        L.append('    %-36s %s%s' % (n, ' ; '.join(live) or '### NO PATH', (' ; under archive/, not taken: ' + ' ; '.join(arch)) if arch else ''))
    L += ['  DRAFT, THE ROSTER`S DIFF: %d entries -> %d ; added %d, appended at the roster`s end in the ruling`s order so no slot changes ; removed 0 ; families %d -> %d' % (
        len(r), len(r) + len(add), len(add), len(set(roster.family(p) for p in r)), len(set(roster.family(p) for p in r + add)))]
    L += ['    + %s' % p for p in add]
    L += ['  DRAFT, THE RULE`S ROW (data/b753_rules.txt (1), written at the pass with the author`s word quoted): "THE ROSTER GAINS SEVEN FAMILIES, by the ruling data/b715_rules.txt (1) asks: [the seven paths].',
          '    Each enters as a family; its later editions join by the rule of b715 (1) as any family`s do; the base roster tools/mirror_roster.json stays unedited."',
          '  DRAFT, THE MEANS: the seven paths in a list of their own beside the base roster (tools/mirror_roster_added.json: the paths, the act and the ruling), read by tools/standing/roster.py after the base',
          '    roster`s families; a control that the base roster`s %d entries keep their slots and the seven follow them; the builder untouched. The mirror of this act then prints the diff in its MANIFEST.' % len(r),
          '  PASSED: the row, the list and the reader`s change are written and committed, one git write per message; the mirror carries %d files and MANIFEST.md. STRUCK: the roster stays at %d.' % (len(r) + len(add), len(r)),
          '  "Any other file of the seat`s list joins on the author`s word at the item, by name" ((R363)(6)[M1]): none is drafted here.', '']

    # ---------------- [D1]
    S = [l for l in src('data/b753_store.txt') if l.startswith('### ### **THE STORE READ: SESSIONS ')][0]
    ms = ' ; '.join('%s (%d rows from :%d, %s)' % x for x in D['models'])
    L += ['## [D1] THE HARNESS UNDER THE RECORD ((R363)(6)[D1]; the author`s fourth word, the model beside the version; the fifth word (6), the alias, the window, the channel and form (c))', '',
          '[D1] FILE the harness`s settings (outside every repository) ; a row of data/b753_rules.txt',
          '  CURRENT, read by this agenda:',
          '    the harness`s version: this session`s rows read %s ; b752`s session`s rows read %s' % (D['v_here'], D['v_prev']),
          '    the model, from this session`s transcript rows: %s' % ms,
          '    the settings` model word: "%s" -- an alias, which names no one model (the rows read as above; the settings` per-model entries name %s)' % (D['model_word'], ', '.join(k for k, _w in D['windows'])),
          '    the window as the settings hold it: %s ; no effort level in the settings (%r)' % (' ; '.join('%s %s' % kw for kw in D['windows']), D['effort']),
          '    the update channel as the settings hold it: "%s" ; the settings` env keys: %s ; the transcripts` retention: %s days' % (D['channel'], ', '.join(D['env']) or 'none', D['retention']),
          '    the scratch folder`s parent under the temp directory: "D--" in tools/standing/v1170.py :24 and sixteen hexadecimal characters in tools/b752_worklist.py :33 (both lines read, control above)',
          '  CURRENT, as the hold read it and the ruling states it, not read again here: the harness updates itself in the background on its latest channel; b752`s session ran 2.1.321 while 2.1.322 was',
          '    installed beneath it forty seconds after its launch (2026-11-10 16:44:56Z); the form of the scratch folder`s parent changed between b736 and b752 with the working directory the same.',
          '  CURRENT, the navigator`s reads of the harness`s documentation, not read by the seat: the transcript`s row format is internal and changes between versions (the answers, author-words and chain',
          '    reads parse those rows); an update downloaded in the background takes effect at the next start of the harness and not within a session; the stable channel is a version about a week old that',
          '    skips releases with major regressions.',
          '  BESIDE IT, THE STORE READ ((R363)(5)(vii), relay data/b753_store.txt, its closing line): %s' % S.strip('# *'),
          '    of it for this item: 39 record tools of b605 to b645 (tools/b644_record.py :94 among them, beside its repaired copy under tools/standing/routes/) test for the transcript and go on where it is absent',
          '    (the form (R363)(7)(viii) names); none is a route this act runs and none was repaired. The operating system`s cleaner reads switched on over temporary files: a candidate, no finding.',
          '  DRAFTED in three forms:',
          '    (a) background updating switched off for the seat by the settings` env key (its name read from the harness`s documentation at the pass, before the write); the program updated on the author`s',
          '        word between acts and at no other time; the version and the model entered at step zero; a change of version an event, with the forms re-read (a transcript row of each kind the routes',
          '        parse; the scratch path).',
          '    (b) updating left as it is (channel "%s"); the version and the model read and printed at step zero as (7)(viii) orders; a change of version an event in the same way.' % D['channel'],
          '    (c) the update channel set to stable (the settings` autoUpdatesChannel, now "%s"); the version and the model read and printed at step zero; a change of version an event in the same way.' % D['channel'],
          '  PASSED AS (a) OR (c): the one settings key is written by the seat on the author`s word at the pass, the file read back and printed, and the form entered as a row of data/b753_rules.txt; it takes',
          '    effect at the harness`s next start. PASSED AS (b): the row alone. STRUCK: nothing written; step zero reads the version as (7)(viii) already orders.', '',
          '### ### **THE AGENDA: 2 ITEMS, [M1] AND [D1] ; [M1] DRAFTS %d FAMILIES, THE ROSTER %d -> %d ; [D1] DRAFTS 3 FORMS ; NOTHING WRITTEN BEYOND THIS BANK ; CONTROLS %s.**' % (
              len(add), len(r), len(r) + len(add), 'ALL AS WANTED' if ok else '### NOT ALL AS WANTED')]
    return ok, L


def committed():
    rel = 'tools/%s_agenda.py' % ACT
    g = lambda *a: subprocess.run(['git', '-C', RELAY] + list(a), capture_output=True, text=True)
    return g('ls-files', '--error-unmatch', rel).returncode == 0 and not g('status', '--porcelain', '--', rel).stdout.strip(), g('rev-parse', '--short=8', 'HEAD').stdout.strip()


def main(argv):
    if argv[:1] == ['control']:
        ok, L = controls(m1(roster.main_tree()), d1())
        print('\n'.join(L))
        return 0 if ok else 1
    if argv[:1] not in (['run'], ['dry']):
        raise SystemExit(__doc__)
    done, gen = committed()
    if argv[0] == 'run' and not done:
        raise SystemExit('### REFUSED: tools/%s_agenda.py is not committed or differs from its commit' % ACT)
    import hold
    if hold.refuses('the agenda of the kept items ((R363)(6))'):
        return 3
    ok, L = compose(gen)
    if argv[0] == 'run':
        if not ok:
            raise SystemExit('### THE CONTROLS NOT ALL AS WANTED: NOTHING BANKED')
        tmp = BANK + '.tmp'
        with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(L) + '\n')
        os.replace(tmp, BANK)
    print('\n'.join(l[:330] for l in L))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
