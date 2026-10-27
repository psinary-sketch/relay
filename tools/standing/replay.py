# -*- coding: utf-8 -*-
"""standing/replay.py -- THE REPLAY CONTROL ((R325)(3)(iv); the author's word (1)(c) of the toolset act: the replay is the
specification). For the previous act and the act before it, each read from the chain (data/act_roots.txt) at the call, the core rebuilds
from the act's committed banks what its per-act tools wrote, and prints each EQUAL or DIFFERS:
  (1) the head line, against data/<act>_closing.txt :1
  (2) the suite's tally, against the combined post-push bank's three figure lines (its figures, and its text)
  (3) the withheld field, against the seal record's `withheld`
  (4) neg_shown's three lists, against the seal record's `neg_shown` count, its `withheld`, and no arm unshown (the seal was written)
  (5) the seal's record, field by field (the tools' sha256, the letters, the defects' sha256, the runs on the previous act's banks)
  (6) the components bank, its component lines (and its head line apart)
Each act's withheld field and components are read as data from data/act_current.json `replay`. A DIFFERS is printed with both sides;
naming it -- the core's fault, or the old tool's, a finding -- is the seat's, in the bank's notes.

  python -X utf8 tools/standing/replay.py          prints; writes nothing
  python -X utf8 tools/standing/replay.py bank     writes data/<act>_replay.txt, the one bank it writes, refused once the act's root is
                                                   appended to the chain
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A          # noqa: E402
import close as C        # noqa: E402
import components as CO  # noqa: E402

NL = '\n'


def verdict(a, b):
    return 'EQUAL' if a == b else 'DIFFERS'


def replay_act(act, cur):
    spec = (cur.get('replay') or {}).get(act) or {}
    parts = cur['parts']
    out, figs = [], []

    def row(key, ok, *detail):
        figs.append((key, ok))
        out.append('  (%s) %-58s %s' % (key, detail[0], 'EQUAL' if ok else 'DIFFERS'))
        for d in detail[1:]:
            out.append('        ' + d)

    seal_rev = A.step_commit(act, 'seal')
    closing_rev = A.step_commit(act, 'closing')
    out.append('### %s -- the seal`s commit %s ; the closing`s %s ; the ruling %s ; parts %s' % (
        act, (seal_rev or '-')[:8], (closing_rev or '-')[:8], spec.get('ruling'), ' '.join(parts)))
    # (1) the head line
    ev = []
    got = C.head_line(act, mains=C.mains_from_steps(act), events=ev, rev=closing_rev)
    want = A.rd('%s_closing.txt' % act, closing_rev).split(NL)[0]
    row('1', got == want, 'the head line, rebuilt from the banks', 'rebuilt: ' + got, 'banked : ' + want,
        'events : %s' % (ev or 'none'))
    # (2) the suite's tally, the post-push parts with the seal record's withheld field
    rec = A.jl('%s_seal_hashes.json' % act, closing_rev)
    W = [w.get('arm') for w in (rec.get('withheld') or [])]
    pb = C.part_banks(act, 'checks_postpush', parts, closing_rev)
    nofoot = [p for p, m, _t in pb if m is None]
    comb = A.rd('%s_checks_postpush.txt' % act, closing_rev)
    if nofoot:
        row('2', False, 'the suite`s tally', 'parts with no footer: %s' % nofoot)
    else:
        t = C.tally_lines(pb, W, C.carried_of(comb))
        b = C.read_tally(comb)
        gf = dict(arms=t['arms'], passing=t['passing'], failing=t['failing'], fails=t['fails'], withheld=t['withheld'], neg=t['neg'],
                  pos=t['pos'], defs=t['defs'])
        bf = dict((k, b[k]) for k in gf)
        verd = t['lines'][2].split('VERDICT : ')[1].split(' ;')[0].rstrip('*')
        row('2', gf == bf and verd == b['verdict'], 'the suite`s tally: %d/%d/%d (passing/failing/withheld)' % (
            t['passing'], t['failing'], len(t['withheld'])),
            'rebuilt: %s ; verdict %s' % (json.dumps(gf), verd), 'banked : %s ; verdict %s' % (json.dumps(bf), b['verdict']))
        blines = [l for l in comb.split(NL) if l.startswith('  ### ### **')][:3]
        same = [verdict(x, y) for x, y in zip(t['lines'], blines)]
        out.append('        the three figure lines` text: %s%s' % (' '.join(same), '' if all(s == 'EQUAL' for s in same) else ''.join(
            NL + '          rebuilt: ' + x + NL + '          banked : ' + y for x, y, s in zip(t['lines'], blines, same) if s != 'EQUAL')))
    # (3) the withheld field, condition-bound, at the seal's commit
    wh = C.withheld_entries(spec.get('withheld'), rev=seal_rev)
    rw = [(w.get('arm'), w.get('reason')) for w in (A.jl('%s_seal_hashes.json' % act, seal_rev).get('withheld') or [])]
    row('3', wh == rw, 'the withheld field, its condition read at the seal`s commit', 'rebuilt: %s' % (wh or 'none'),
        'banked : %s' % (rw or 'none (the record carries no field)'))
    # (4) and (5) neg_shown and the seal's record
    if not seal_rev:
        row('4', False, 'neg_shown`s three lists', 'no seal row in the step bank')
        return out, figs
    got, srec = C.seal_record(act, parts, seal_rev, seal_rev, spec.get('withheld'))
    ns_ok = got['neg_shown'] == srec.get('neg_shown') and got['withheld'] == (srec.get('withheld') or []) and not got['bad']
    row('4', ns_ok, 'neg_shown`s three lists: shown %d, unshown %d, withheld %d' % (got['neg_shown'], len(got['bad']), len(got['withheld'])),
        'banked : neg_shown %s ; withheld %d ; unshown none (the seal was written)' % (srec.get('neg_shown'), len(srec.get('withheld') or [])),
        'unshown rebuilt: %s' % (got['bad'] or 'none'))
    tdiff = sorted(t for t, h in got['tools'].items() if h != (srec.get('tools') or {}).get(t))
    hdiff = sorted(t for t, h in got['tools_at_head'].items() if h != (srec.get('tools') or {}).get(t))
    fields = [('tools', not tdiff, '%d tools, at the seal`s commit %s ; differing %s' % (len(got['tools']), seal_rev[:8], tdiff or 'none')),
              ('letters', got['letters'] == srec.get('letters'), '%d letters ; the record %d' % (len(got['letters']), len(srec.get('letters') or [])))]
    if 'defects_sha256' in srec:
        fields.append(('defects_sha256', got['defects_sha256'] == srec['defects_sha256'], 'rebuilt %s ; the record %s' % (
            got['defects_sha256'][:16], srec['defects_sha256'][:16])))
    else:
        fields.append(('defects_sha256', True, 'the record carries no such field (rebuilt %s, not compared)' % got['defects_sha256'][:16]))
    fields.append(('prev_run', got['prev_run'] == srec.get('prev_run'), 'rebuilt %s' % json.dumps(got['prev_run'], sort_keys=True)))
    row('5', all(f[1] for f in fields), 'the seal`s record, field by field', *['%-15s %s %s' % (f[0], 'EQUAL' if f[1] else 'DIFFERS', f[2])
                                                                             for f in fields])
    out.append('        the record`s relay head %s carries the sealed bytes of %d of %d tools ; not: %s' % (
        (srec.get('relay_head') or '-')[:8], len(got['tools']) - len(hdiff), len(got['tools']), hdiff or 'none'))
    for t in hdiff:   # where the record's sha256 for a tool its relay head does not carry is found: the act's relay step commits, in order
        want = (srec.get('tools') or {}).get(t)
        hits = []
        for r in A.steps(act):
            if r.get('repo') == 'relay':
                b = A.blob(r['commit'], 'tools/' + t)
                if b is not None and A.sha256_bytes(b) == want:
                    hits.append('%s (%s)' % (r['commit'][:8], r['phase']))
        first = A.gs('relay', 'log', '--format=%h %cI', '-1', srec.get('relay_head') or 'HEAD', '--', 'tools/' + t)
        out.append('        %s: the record %s ; at the relay head %s ; the step commits carrying the record`s bytes: %s ; its last commit at or '
                   'before the relay head: %s' % (t, (want or '-')[:16], (got['tools_at_head'].get(t) or '-')[:16], hits or 'NONE', first))
    if got['letters'] != srec.get('letters'):
        out.append('        letters rebuilt: %s' % [s[:40] for s in got['letters']])
        out.append('        letters banked : %s' % [s[:40] for s in srec.get('letters') or []])
    if 'prev_run' in srec and got['prev_run'] != srec.get('prev_run'):
        out.append('        prev_run banked : %s' % json.dumps(srec.get('prev_run'), sort_keys=True))
    # (6) the components bank
    # v1.1.0: composed from the banks as they stood at the commit that first carries the components bank (rows appended to the step bank
    # after it, the toolset act's rows 19 and 20, are not the composer's input)
    added = (A.gs('relay', 'log', '--diff-filter=A', '--format=%H', closing_rev or 'HEAD', '--', 'data/%s_components.txt' % act) or '').split(NL)
    crev = added[-1].strip() if added and added[-1].strip() else None
    comp = CO.composed(act, spec.get('components') or [], spec.get('ruling'), rev=crev)
    bank = A.rd('%s_components.txt' % act, closing_rev).rstrip(NL).split(NL)
    out.append('        the components bank first carried at %s ; composed from the banks as they stood there' % (crev or '-')[:8])
    gl, bl = [l for l in comp if l.startswith('### ')], [l for l in bank if l.startswith('### ')]
    same = [verdict(x, y) for x, y in zip(gl, bl)]
    ok6 = len(gl) == len(bl) and all(s == 'EQUAL' for s in same)
    row('6', ok6, 'the components bank: %d component lines, %d banked' % (len(gl), len(bl)),
        'per line: %s' % (' '.join(same) or 'none'), 'the head line apart: %s' % verdict(comp[0], bank[0] if bank else ''))
    for x, y, s in zip(gl, bl, same):
        if s != 'EQUAL':
            out.append('          rebuilt: ' + x[:400])
            out.append('          banked : ' + y[:400])
    return out, figs


def lines():
    cur = A.current()
    act = cur['act']
    # ### v1.1.0: the acts replayed are those the ruling's replay field specifies (data/act_current.json `replay`), the chain's acts among
    # ### them, newest first; v1.0.0 read the previous act and the one before it alone
    chain = [r[0] for r in A.chain()]
    acts = sorted((a for a in (cur.get('replay') or {}) if a in chain), key=chain.index, reverse=True)
    L = ['%s -- THE REPLAY CONTROL OF THE STANDING TOOLSET AT %s, OVER %s (%s)' % (
        act, A.rd_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION')).strip(), ', '.join(acts),
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
        '### rows are the objects of the author`s word (1)(c), per act: (1) the head line, (2) the suite`s tally, (3) the withheld field,',
        '### (4) neg_shown`s three lists, (5) the seal`s record, (6) the components bank, each EQUAL or DIFFERS with both sides printed.',
        '### Written by tools/standing/replay.py; it writes nothing else.', '']
    tot = []
    for a in acts:
        o, f = replay_act(a, cur)
        L += o + ['']
        tot += [(a, k, ok) for k, ok in f]
    dif = [(a, k) for a, k, ok in tot if not ok]
    rp = cur.get('replay') or {}
    fnd, forms = rp.get('findings') or [], rp.get('forms') or []
    L += ['### THE DIFFERENCES NAMED (the seat`s, read from data/act_current.json `replay`): each DIFFERS by the finding that names it']
    unnamed = []
    for a, k in dif:
        f = [x for x in fnd if a in x.get('acts', []) and x.get('object') == k]
        if not f:
            unnamed.append('%s (%s)' % (a, k))
        L.append('  %s (%s): %s' % (a, k, ('%s, %s' % (f[0]['id'], f[0]['whose'])) if f else '### UNNAMED'))
    L += ['', '### THE FINDINGS, the old tools` (not copied forward):'] + ['  %s [%s ; object (%s)] %s' % (
        x['id'], ', '.join(x['acts']), x['object'], x['text']) for x in fnd]
    L += ['', '### THE FORMS, read and not counted (an old tool`s text where the figures are EQUAL):'] + ['  [%s ; object (%s)] %s' % (
        ', '.join(x['acts']), x['object'], x['text']) for x in forms]
    L += ['', '### ### **OBJECTS %d ; EQUAL %d ; DIFFERS %d %s ; NAMED %d ; UNNAMED %d ; FINDINGS %d.**' % (
        len(tot), len(tot) - len(dif), len(dif), ['%s (%s)' % d for d in dif] or '', len(dif) - len(unnamed), len(unnamed), len(fnd))]
    return L, act


def main(route):
    L, act = lines()
    if route == 'bank':
        if act in [r[0] for r in A.chain()]:
            print('### %s`s ROOT IS APPENDED TO THE CHAIN -- NOTHING WRITTEN' % act)
            return 4
        p = os.path.join(A.D, '%s_replay.txt' % act)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
