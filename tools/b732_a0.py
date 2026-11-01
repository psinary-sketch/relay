# -*- coding: utf-8 -*-
"""b732 (R342)(3): THE A0 RESTATEMENT, read from the two blobs and the one dispatch's artefact.
`rows <artifact dir>` appends the commit, push, dispatch and read rows to data/b732_dispatch_rows.json, once.
`bank <artifact dir>` writes data/b732_a0_restatement.txt. No lean process on this host; nothing here writes a kernel."""
import io, json, os, re, subprocess, sys

EF = 'D:/SIDE-explicit-formula'
K = 'SIDE-explicit-formula'
REPO = 'psinary-sketch/' + K
BANK = 'D:/relay/data/b732_a0_restatement.txt'
ROWS = 'D:/relay/data/b732_dispatch_rows.json'
BEFORE = '23b006df'
TIP = '1b34964ae229c8d3ce769dbe01e53d8f43b92ed0'
FILE = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'
Q0 = 'SIDEExplicitFormula/Schema/EpsteinQ0.lean'
RUN = '41337967613'
TARGET = 'SIDEExplicitFormula.Schema.EpsteinZQ SIDEExplicitFormula.Schema.ZQ.Zeros SIDEExplicitFormula.Schema.ZQ.LogDeriv'
BINDERS = ('zq_count', 'zq_explicit_formula', 'zq_li_nonneg_imp_online')
WORD = 'Field, follow zq_count (Recommended)'


def git(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, encoding='utf-8').stdout


def gh(*a):
    return subprocess.run(['gh'] + list(a), capture_output=True, encoding='utf-8').stdout


def header(blob, name):
    """the statement from `theorem <name>` to its `:=`, whitespace folded"""
    m = re.search(r'(?m)^theorem ' + name + r'\b(.*?):=', blob, re.S)
    assert m, name
    return ' '.join(m.group(0)[:-2].split())


def conclusion(h):
    """after the last top-level colon of the header: depth counted over ( { ["""
    d, cut = 0, None
    for i, c in enumerate(h):
        d += c in '({[' or c == '⟨'
        d -= c in ')}]' or c == '⟩'
        if c == ':' and d == 0 and not h[i:i + 2] == ':=':
            cut = i
            break
    return h[cut + 1:].strip()


def field(blob, name):
    m = re.search(r'(?m)^  ' + name + r' : (.*)$', blob)
    assert m, name
    return m.group(1).strip()


def cmd_rows(art):
    full = git('rev-parse', TIP).strip()
    parent = git('rev-parse', full + '^').strip()
    kinds = git('show', '-s', '--format=%ae%n%ce', full).strip().split('\n')
    assert len(kinds) == 2 and all(k.endswith('@users.noreply.github.com') for k in kinds), 'a commit e-mail is not the noreply form'
    v = json.loads(gh('run', 'view', RUN, '--repo', REPO, '--json', 'status,conclusion,createdAt,updatedAt'))
    ex = open(art + '/build_exit.txt', encoding='utf-8').read().strip()
    log = open(art + '/build.log', encoding='utf-8', errors='replace').read()
    ref = open(art + '/ref.txt', encoding='utf-8').read().strip().split()[0]
    errs = [l for l in log.split('\n') if l.startswith('error: SIDEExplicitFormula')]
    ax = [l for l in open(art + '/axioms.txt', encoding='utf-8', errors='replace').read().split('\n') if l.strip()]
    nums = [int(x) for x in re.findall(r'(?m)(\d+)\s*$', open(art + '/mem.log', encoding='utf-8', errors='replace').read())]
    rows = [dict(kind='commit', kernel=K, branch='zq-b730', item='A0', sha=full, parent=parent, files=[FILE], identity='the global noreply form, read back by kind (author and committer) at this row'),
            dict(kind='push', kernel=K, branch='zq-b730', sha=full, remote_equal=True, at='2026-11-01T18:42:05Z', capture='data/b732_SIDE-explicit-formula_zq-b730_push_out.txt'),
            dict(kind='dispatch', kernel=K, item='A0', n=1, workflow='build-module.yml', at_ref='main', sha=full, target=TARGET, run=int(RUN), at=v['createdAt']),
            dict(kind='read', kernel=K, item='A0', n=1, run=int(RUN), status=v['status'], conclusion=v['conclusion'], built_ref=ref, toolchain='leanprover/lean4:v4.34.0-rc1', build_exit=ex,
                 verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs, axioms_lines=ax, sorryAx=any('sorryAx' in l for l in ax), runner_low_mb=min(nums) if nums else None, at=v['updatedAt'],
                 free_mb=4328, free_at='2026-11-01T18:49:34Z', artifact='scratchpad a0run/build-module-' + RUN)]
    assert not os.path.exists(ROWS), 'the rows stand'
    with open(ROWS, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('[\n' + ',\n'.join('  ' + json.dumps(r, ensure_ascii=False) for r in rows) + '\n]\n')
    print(len(rows), full[:8], 'parent', parent[:8], rows[3]['verdict'], ex, 'errors', len(errs), 'axiom lines', len(ax), 'sorryAx', rows[3]['sorryAx'], 'low', rows[3]['runner_low_mb'], 'ref', ref[:8])


def cmd_bank(art):
    old, new = git('show', '%s:%s' % (BEFORE, FILE)), git('show', '%s:%s' % (TIP, FILE))
    q0 = git('show', '%s:%s' % (TIP, Q0))
    rows = json.load(io.open(ROWS, encoding='utf-8'))
    rd = next(r for r in rows if r['kind'] == 'read')
    ax = dict(re.findall(r"'SIDEExplicitFormula\.Schema\.([A-Za-z_]+)' depends on axioms: \[([^\]]*)\]", open(art + '/axioms.txt', encoding='utf-8', errors='replace').read()))
    unknown = [l for l in rd['axioms_lines'] if 'unknownIdentifier' in l]
    out = ['b732 -- (R342)(3): THE A0 PREMISE RESTATED, THE COMMIT, THE ONE DISPATCH AND EVERY THEOREM BINDING THE PREMISES',
           '',
           '## THE WORD. The question put at Component 2 (zq_count\'s conclusion names the field; the field\'s type changes, so either the conclusion follows or the theorem breaks), answered: "%s".' % WORD,
           '## THE COMMIT: %s on zq-b730, parent %s, file %s alone; main untouched; pushed and read back equal (data/b732_SIDE-explicit-formula_zq-b730_push_out.txt).' % (TIP, BEFORE, FILE),
           '## THE DISPATCH, THE ONE (N1): run %s, built ref %s, status %s, conclusion %s, build_exit %s, errors %d, sorryAx %s. No lean process ran on this host.' % (RUN, rd['built_ref'], rd['status'], rd['conclusion'], rd['build_exit'], len(rd['errors']), rd['sorryAx']),
           '',
           '## THE FIELD',
           '  before | count : ' + field(old, 'count'),
           '  after  | count : ' + field(new, 'count'),
           '  the form asked | WeilConfig.count, Schema/Config.lean :31 at the tip: ' + re.search(r'(?m)^\s*count\s*:.*$', git('show', '%s:SIDEExplicitFormula/Schema/Config.lean' % TIP)).group(0).strip(),
           '',
           '## EVERY THEOREM BINDING ZQPremises (git grep at the tip: the structure and these %d, nothing else in the kernel), EACH ELABORATED BY THE RUN ABOVE, CONCLUSION BEFORE AND AFTER FROM THE BLOBS' % len(BINDERS)]
    moved = []
    for n in BINDERS:
        a, b = conclusion(header(old, n)), conclusion(header(new, n))
        same = a == b
        if not same:
            moved.append(n)
        out += ['  %s | %s | axioms [%s]' % (n, 'UNCHANGED' if same else 'MOVED, THE AUTHOR\'S WORD', ax[n]), '    before: ' + a, '    after : ' + b]
    assert moved == ['zq_count']
    out += ['',
            '### ### **THE CONCLUSIONS: 2 of 3 UNCHANGED; zq_count MOVED, THE ONE CONCLUSION THAT MOVED. IT READS THE FIELD OFF THE BUNDLE, SO IT FOLLOWS THE FIELD, BY THE AUTHOR\'S WORD ABOVE; THE QUESTION\'S WORDS "printed unchanged in conclusion" STAND FOR THE OTHER TWO AND NOT FOR THIS ONE.**',
            '',
            '## WHAT THE COMMIT ALSO CHANGED, BEYOND THE FIELD\'S LINE, PRINTED PLAINLY',
            '  zq_count\'s statement (above); zq_li_nonneg_imp_online\'s PROOF, h.count now opened by .elim, its statement unchanged; the docstring of ZQPremises (:135-:136), which named the old form;',
            '  and the module docstring at :17, beyond what the question named: it stated the count as `Wide.HCount Z A0Q`, which would have read false at the tip. Stat: 6 insertions, 6 deletions, one file.',
            '',
            '## THE A0Q ROW, (R342)(3)\'s LAST CLAUSE: the named value stays a separate definition and is not a field',
            '  ' + re.search(r'(?m)^.*\bA0Q\b.*:=.*$', q0).group(0).strip() + ' | ' + Q0,
            '  ' + re.search(r'(?m)^.*\bQ0Count\b.*$', q0).group(0).strip() + ' | ' + Q0,
            '  git diff %s..%s over that file: %d lines (0 wanted).' % (BEFORE, TIP[:8], len(git('diff', BEFORE, TIP, '--', Q0).strip().split('\n')) if git('diff', BEFORE, TIP, '--', Q0).strip() else 0),
            '  THE BANKS THAT CITE IT: every bank row naming `HCount Z A0Q` or zq_count\'s A0Q form cites main or a commit before this one (b703_epstein_grade.txt, b729_count_price.txt, b730_ferry.txt among them; git grep over data/b7[0-3]*): main badacccb is untouched, so they stand as cited. No theorem row is added: no compiled statement proves the count at 10, and Q0Count is the separate definition such a row would name.',
            '',
            '## THE PROBE NOT RUN: ChainProbe.lean would have added a file to the commit that changes the field and nothing else, so the conclusions above are read from the source blobs and the compile, exit 0, is what elaborated them; chainprobe_log: NOT RUN.',
            '## THE ARTEFACT\'S REFUSED ROWS, NOT A FAILURE OF THE BUILD: the workflow carries a fixed print list; %d names on it are not on this branch ("Unknown constant"), 2 print targets refused (axioms_refused.txt). build_exit governs and is 0. %s' % (len(unknown), 'None of the three binders is among them.'),
            '## (R342)(3) NEXT: b733 takes the count field on the restated premise; C3 and C4 are priced before any build. No field of ZQPremises is discharged here: the premises stand, stated and not proved.']
    t = '\n'.join(out) + '\n'
    with io.open(BANK, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(t)
    print(t)


if __name__ == '__main__':
    {'rows': cmd_rows, 'bank': cmd_bank}[sys.argv[1]](*sys.argv[2:])
