# -*- coding: utf-8 -*-
"""b722_instruments.py -- THE RESEARCH INSTRUMENTS ENUMERATED BY RULE, (R332)(6). Written whole at b722 by the Write tool.

  rule [dry]   prints THE RULE before any tool is named; then the population, each screen's yield, the hand-read residue, the rule's output
               with each tool's importers and runners, and beside it the navigator's expectation (choosing nothing).
               -> data/b722_instruments.txt (the bank of the enumeration; the entries themselves are written to INSTRUMENTS.md by
               tools/b722_instruments.py entries, from this bank's output).
  entries [dry] composes the entries I-41 onward, one per tool of the rule's output, in b618's form with (R332)(6)'s fields, from
               ENTRY (below, written by the Write tool from each tool's own docstring and banks, each cited by line); appends them to
               PLACE-papers phase1.5/method/INSTRUMENTS.md after its last line; nothing above is edited.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b722'
BANK = '%s_instruments.txt' % ACT
PP = 'D:/MY-DOwnloads/PLACE-papers'
INSTR = 'phase1.5/method/INSTRUMENTS.md'

RULE = [
    'THE RULE ((R332)(6)), printed before any tool is named: an act-numbered tool under relay tools/ (tools/bNNN_<name>.py, tracked at HEAD) is a',
    'RESEARCH INSTRUMENT when (I) it computes a figure about a mathematical object -- a zero, a coefficient, an eigenvalue, an onset, a table, a',
    'build, a statement`s grade -- and (II) a later act imported it unedited or ran it again.',
    'AS READ BY THIS TOOL:',
    '  (II) IMPORTED: a tool of a later act (tools/bMMM_*.py, MMM > NNN) carries an import line naming the module (`import bNNN_<name>`,',
    '       `from bNNN_<name> import`); an import by name edits nothing. Whether a later act edited the module`s own file is NOT read by this',
    '       tool (a limit, printed). RAN AGAIN: a later act`s bank or tool carries a command line running it (`python` ... `tools/bNNN_<name>.py`).',
    '       A mention that is neither is not a reuse.',
    '  (I)  COMPUTES A FIGURE ABOUT A MATHEMATICAL OBJECT, read in two screens and a hand read: (S1) the close`s own families, by the name`s',
    '       stem, are not instruments -- record, worklist, checks, carry, citation, closing, regspec, reg_gate, report, standing, corrigendum,',
    '       c1, tests, hooks, extract, lockgate, prune, select of a close, mirror, push, stepzero, rowgen, census, survey of the record --',
    '       FAMILIES below; (S2) of the rest, a tool whose source imports a mathematical library (flint, mpmath, sympy, numpy, scipy,',
    '       fractions) or an act tool already passing (S2), or invokes lean or lake, passes; (H) every tool (S2) passes and every tool it',
    '       sets aside is read by hand from its docstring, each reading printed with its reason; the hand read may strike a tool (S2) passed',
    '       (a figure about the record, not a mathematical object) and may not add one (S2) set aside without printing why.',
    '  TOOLS ALREADY ENTERED in INSTRUMENTS.md (I-1 to I-40) are printed and not entered again.',
]
FAMILIES = ('record', 'worklist', 'checks', 'carry', 'citation', 'closing', 'regspec', 'reg_gate', 'report', 'standing', 'corrigendum', 'c1',
            'tests', 'hooks', 'extract', 'lockgate', 'prune', 'mirror', 'push', 'stepzero', 'rowgen', 'census', 'record_tool', 'scan',
            'ferry', 'gate', 'touch', 'readfirst', 'answers', 'title', 'face', 'events', 'defects', 'seal', 'root', 'trail', 'entry', 'ledger',
            'propagation', 'instruments', 'cites', 'registry', 'snapshot', 'order', 'orders', 'moves', 'select')
MATHLIB = re.compile(r'^\s*(?:import|from)\s+(flint|mpmath|sympy|numpy|scipy|fractions)\b', re.M)
LEAN = re.compile(r"['\"](?:lean|lake)['\"]|\blake build\b|\blake env\b")
NAV = ('b707_onset', 'b709_pairs', 'b711_list', 'b713_list', 'b717_list', 'b711_coeffs', 'b711_surgery', 'b713_predict', 'b718_classgroup',
       'b718_abstract', 'b718_decomp', 'b720_predict', 'b721_derivation', 'b721_rebuild', 'b721_frozen_line')
ACTN = re.compile(r'^b(\d{3})_([a-z0-9_]+)$')


def git(*a, repo=ROOT):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def population():
    out = {}
    for p in git('ls-files', '--', 'tools/').split(NL):
        m = re.match(r'^tools/(b\d{3}_[a-z0-9_]+)\.py$', p)
        if m:
            out[m.group(1)] = p
    return out


def reuse(pop):
    """imports and runs by later acts: {module: {'imp': set(act tools), 'ran': set(paths)}}."""
    imp = dict((k, set()) for k in pop)
    ran = dict((k, set()) for k in pop)
    for l in git('grep', '-n', '-E', r'^\s*(import|from)\s+b[0-9]{3}_[a-z0-9_]+', '--', 'tools/').split(NL):
        m = re.match(r'^tools/(b(\d{3})_[a-z0-9_]+)\.py:\d+:\s*(?:import|from)\s+(.*)$', l)
        if not m:
            continue
        who, wact = m.group(1), int(m.group(2))
        for mod in re.findall(r'\b(b\d{3}_[a-z0-9_]+)\b', m.group(3).split('#')[0]):
            mm = ACTN.match(mod)
            if mod in imp and mm and wact > int(mm.group(1)):
                imp[mod].add(who)
    for l in git('grep', '-n', '-E', r'python[^`]*tools/b[0-9]{3}_[a-z0-9_]+\.py', '--', 'data/', 'tools/').split(NL):
        m = re.match(r'^((?:data|tools)/(?:b(\d{3})_)?[^:]*):\d+:(.*)$', l)
        if not m or not m.group(2):
            continue
        wact = int(m.group(2))
        for mod in re.findall(r'python[^`]*?tools/(b\d{3}_[a-z0-9_]+)\.py', m.group(3)):
            mm = ACTN.match(mod)
            if mod in ran and mm and wact > int(mm.group(1)):
                ran[mod].add(m.group(1))
    return imp, ran


def stem(mod):
    return ACTN.match(mod).group(2)


def in_family(mod):
    s = stem(mod)
    return any(s == f or s.startswith(f + '_') or s.endswith('_' + f) for f in FAMILIES)


def doc_of(path):
    t = io.open(os.path.join(ROOT, path), encoding='utf-8', errors='replace').read()
    m = re.search(r'"""(.*?)"""', t, re.S)
    return t, (m.group(1).strip().split(NL)[0] if m else '')


def entered():
    t = io.open(os.path.join(PP, INSTR), encoding='utf-8').read()
    return t, sorted(set(re.findall(r'\b(b\d{3}_[a-z0-9_]+)\b', t)))


# ### (H) THE HAND READ: each tool (S2) passes or sets aside, read from its docstring by the seat (the Read tool, :1-:30 of each), its reading
# ### and reason. A tool absent here that (S2) passes is printed UNREAD and refuses the bank.
I_, N_ = 'INSTRUMENT', 'NOT'
HAND = {
    'b302_correspondence': (N_, 'writes a CORRESPONDENCE row from a build`s profile: a row of the record'),
    'b302_kernel': (I_, 'the kernel build, its profile and byte comparisons: a build'),
    'b303_correspondence': (N_, 'a CORRESPONDENCE row: the record'),
    'b303_family': (I_, 'the family`s finite half verified at content: computed'),
    'b303_pins': (N_, 'pins by ls-remote: the record`s repositories'),
    'b303_source': (N_, 'a source text read: a document, not a mathematical object'),
    'b304_smearing': (I_, 'the finite analogue of the source`s move computed'),
    'b305_source': (N_, 'a source pinned by hash and its quotations located'),
    'b306_stem_scope': (N_, 'a stem sweep over the record'),
    'b308_local_field': (I_, 'the local-field instrument, built with its controls'),
    'b309_scaling_trace': (I_, 'the scaling trace Tr(theta(p^k) Pi) computed'),
    'b316_instrument': (I_, 'a computable truncation of the archimedean space'),
    'b317_smear': (I_, 'the smeared trace on the truncated space'),
    'b318_square': (I_, 'the square form computed'),
    'b319_stable': (I_, 'the stable rank of the subspace'),
    'b320_corroborate': (I_, 'the Weil side by a second route'),
    'b320_weil': (I_, 'the archimedean Weil distribution evaluated'),
    'b321_window': (I_, 'the remainder integral and places sum on a lawful test function'),
    'b322_ladder': (I_, 'the unit`s residual along the domain ladder and its rate'),
    'b325_epstein': (I_, 'the Epstein channels'),
    'b326_closure': (I_, 'the explicit formula closed at every cell'),
    'b326_windows': (I_, 'the two windows at every cell'),
    'b326_zeros': (I_, 'the Epstein zeros on the line'),
    'b327_bridge': (I_, 'the archimedean channel identity measured'),
    'b327_faces_row': (N_, 'the faces ledger`s row-writer'),
    'b328_family': (I_, 'the discriminating family, its condition and seeds'),
    'b332_statement': (N_, 'generates a clause`s text; computes no figure and grades nothing'),
    'b333_diagnose': (I_, 'evaluates the source`s (150) and attributes each banked number'),
    'b334_aimmap': (I_, 'the aim-map`s four quantities per aim'),
    'b340_li_control': (I_, 'the archimedean distribution on the Li family'),
    'b352_fit': (I_, 'fits sealed models to banked residuals: fitted constants'),
    'b363_span': (N_, 'counts the record`s span'),
    'b366_sweep': (N_, 'counts gate suites` arms'),
    'b371_inventory': (N_, 'a row inventory of the record'),
    'b374_hedge': (N_, 'a hedge audit of sentences'),
    'b376_axes': (N_, 'a rubric`s axes applied to documents'),
    'b378_terminals': (N_, 'identifier search across kernel refs: names, not a figure'),
    'b437_components': (I_, 'the window opened by rungs: values computed'),
    'b456_components': (N_, 'an errata entry and routed items: the record'),
    'b462_components': (N_, 'a census of items in bins: the record'),
    'b501_bound': (I_, 'the places-side quadrature bound'),
    'b503_zero': (I_, 'the zero side alias-free'),
    'b504_chain': (I_, 'the chain on one transform over 119 cells'),
    'b511_families': (I_, 'two test-function families in the compiled class'),
    'b512_table': (I_, 'set aside by (S2), kept by hand: the register forms` statements graded STATABLE / COMPILED at a kernel pin, a statement`s grade'),
    'b514_window': (I_, 'the matched window'),
    'b519_window': (I_, 'three variants of the two-property window'),
    'b521_tail': (I_, 'Q0`s tail tightened and the width pass'),
    'b522_reach': (I_, 'the reach read per width'),
    'b523_caveats': (I_, 'the witness`s caveats priced: sigma_max, counts'),
    'b527_values': (I_, 'the plateau`s values two ways'),
    'b544_probe_part': (I_, 'axiom probes by lake env lean: a statement`s grade'),
    'b604_rows': (N_, 'data only, the sieve table`s rows'),
    'b616_claims': (N_, 'papers` claims graded: sentences of the record'),
    'b634_elab': (I_, 'the elaborated reader of kernel declarations: a statement`s grade'),
    'b661_map': (I_, 'the detection-index map at Z1'),
    'b662_map': (I_, 'the detection-index map at Z1'),
    'b663_epstein_map': (I_, 'the rate index and zero side at Q0'),
    'b667_epstein_certify': (I_, 'Q0`s zeros below 150 isolated in balls'),
    'b667_epstein_map_balls': (I_, 'the rate index on the balls'),
    'b671_narrow': (I_, 'Q0`s points narrowed'),
    'b675_li_bench': (I_, 'the Li index at Q0'),
    'b677_epstein_map_angle': (I_, 'the detection map in the angle form'),
    'b680_readings': (N_, 'readings of the record under the pair rule'),
    'b685_count': (I_, 'the count law for Z_Q at -23 in balls'),
    'b687_readings': (I_, 'refutation tests of b685`s derivation at named steps'),
    'b690_readings': (N_, 'readings of the record'),
    'b694_witness': (I_, 'the off-line zeros as balls, the witness`s zeros route'),
    'b694_witness_terms': (I_, 'the Weil-face witness computed'),
    'b696_witness_balls': (I_, 'the witness with certified tail balls'),
    'b704_read_arm': (N_, 'a standing arm over read banks'),
    'b705_detection': (I_, 'the detection law over seventeen pairs'),
    'b707_onset': (I_, 'the sign-onset radius: least eigenvalues'),
    'b709_grid': (I_, 'the onset`s fine grid'),
    'b709_pairs': (I_, 'the detection law over the twelve higher pairs'),
    'b710_fit': (I_, 'set aside by (S2), kept by hand: the detection law`s two constants fitted from banked figures, and its predictions'),
    'b711_coeffs': (I_, 'Q0`s log-derivative coefficients exactly'),
    'b711_list': (I_, 'the certified zero list toward 443'),
    'b712_genus_control': (I_, 'set aside by (S2), kept by hand: the genus identity checked on representation counts'),
    'b712_locate': (N_, 'a line locator'),
    'b713_list': (I_, 'the certified zero list at -15'),
    'b713_predict': (I_, 'n* predictions from the registered law at -15'),
    'b714_hook': (N_, 'the PreToolUse hook'),
    'b714_pilot': (N_, 'a pilot reading the record'),
    'b716_genus_control': (I_, 'set aside by (S2), kept by hand: the representation-count control at -39'),
    'b717_coeffs': (I_, 'the coefficients at -39'),
    'b717_list': (I_, 'the certified zero list at -39'),
    'b717_predict': (I_, 'n* predictions at -39'),
    'b718_abstract': (I_, 'the group-ring model of log(Z_Q1/2)'),
    'b718_classgroup': (I_, 'class groups and log(Z_Q1/2) coefficients'),
    'b718_pin': (I_, 'the federation pin`s builds dispatched and read by run id: a build'),
    'b719_arms': (N_, 'the close arms` history'),
    'b720_predict': (I_, 'the shape rule`s n0 and b(n0) at -35 and -40'),
}


def rule(*a):
    t0 = time.time()
    pop = population()
    imp, ran = reuse(pop)
    _instr_text, already = entered()
    reused = sorted(k for k in pop if imp[k] or ran[k])
    s1 = [k for k in reused if not in_family(k)]
    src = dict((k, doc_of(pop[k])) for k in s1)
    s2 = []
    for k in s1:   # ### two passes: an act tool importing one already passing (S2) passes
        if MATHLIB.search(src[k][0]) or LEAN.search(src[k][0]):
            s2.append(k)
    grew = True
    while grew:
        grew = False
        for k in s1:
            if k not in s2 and any(re.search(r'^\s*(?:import|from)\s+%s\b' % x, src[k][0], re.M) for x in s2):
                s2.append(k)
                grew = True
    aside = [k for k in s1 if k not in s2]
    L = ['%s -- (R332)(6): THE RESEARCH INSTRUMENTS ENUMERATED BY RULE (%s)' % (ACT, utc()), ''] + RULE + [''] + [
        '### FAMILIES (S1), by the name`s stem: ' + ', '.join(FAMILIES), '',
        '## THE YIELDS',
        '  THE POPULATION: act-numbered tools tracked at HEAD: %d' % len(pop),
        '  (II) REUSED by a later act (imported %d, ran again %d, either): %d' % (sum(1 for k in pop if imp[k]), sum(1 for k in pop if ran[k]), len(reused)),
        '  (S1) not of the close`s families: %d' % len(s1),
        '  (S2) a mathematical library, an act tool passing (S2), or lean/lake: %d ; set aside %d' % (len(s2), len(aside)), '']
    unread = [k for k in s1 if k not in HAND]
    L += ['## THE HAND READ (H): each tool (S1) keeps, its first docstring line, (S2)`s word, the seat`s reading and its reason']
    out = []
    for k in sorted(s1, key=lambda x: (int(x[1:4]), x)):
        h = HAND.get(k)
        word = h[0] if h else 'UNREAD'
        if h and h[0] == 'INSTRUMENT':
            out.append(k)
        L.append('  %-28s (S2) %-8s HAND %-14s %s | %s' % (k, 'PASS' if k in s2 else 'ASIDE', word, (h[1] if h else ''), src[k][1][:150]))
    L += ['', '## THE RULE`S OUTPUT, each with its importers and runners (later acts), ALREADY ENTERED marked']
    for k in sorted(out, key=lambda x: (int(x[1:4]), x)):
        L.append('  %-28s imported by %s ; ran again by %s%s' % (
            k, ', '.join(sorted(imp[k])) or 'NONE', ', '.join(sorted(ran[k])[:6]) + (' (+%d)' % (len(ran[k]) - 6) if len(ran[k]) > 6 else '') if ran[k] else 'NONE',
            ' ; ALREADY ENTERED' if k in already else ''))
    nav_in = [n for n in NAV if n in out]
    L += ['', '## BESIDE IT, THE NAVIGATOR`S EXPECTATION ((R332)(6)), CHOOSING NOTHING',
          '  in the expectation and the output: %s' % (', '.join(nav_in) or 'NONE'),
          '  in the expectation, not the output: %s' % (', '.join('%s (%s)' % (n, 'not reused' if n in pop and not (imp[n] or ran[n]) else
                                                                   ('a close family' if n in pop and in_family(n) else ('hand: ' + HAND[n][1] if n in HAND else 'not at HEAD' if n not in pop else 'set aside')))
                                                            for n in NAV if n not in out) or 'NONE'),
          '  in the output, not the expectation: %s' % (', '.join(k for k in out if k not in NAV) or 'NONE'), '']
    new = [k for k in out if k not in already]
    L += ['### ### **THE RULE`S OUTPUT: %d INSTRUMENTS (%d NEW, TO BE ENTERED AS I-41 TO I-%d) ; POPULATION %d, REUSED %d, (S1) %d, (S2) %d ; '
          'THE NAVIGATOR`S %d: %d IN THE OUTPUT ; UNREAD BY HAND %d ; %d s.**' % (
              len(out), len(new), 40 + len(new), len(pop), len(reused), len(s1), len(s2), len(NAV), len(nav_in), len(unread),
              int(time.time() - t0))]
    print(NL.join(L))
    if unread:
        print('### UNREAD BY HAND: %s -- NOTHING BANKED' % ', '.join(unread))
        return
    if 'dry' in a:
        return
    p = os.path.join(D, BANK)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    with open(os.path.join(D, '%s_instruments.json' % ACT) + '.tmp', 'wb') as fh:
        fh.write((json.dumps(dict(at=utc(), output=out, new=new, importers=dict((k, sorted(imp[k])) for k in out),
                                  runners=dict((k, sorted(ran[k])) for k in out)), indent=1) + NL).encode('utf-8'))
    os.replace(os.path.join(D, '%s_instruments.json' % ACT) + '.tmp', os.path.join(D, '%s_instruments.json' % ACT))
    print('written data/%s, .json' % BANK)


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = dict(rule=rule).get(route)
    if fn is None:
        sys.exit('usage: b722_instruments.py rule [dry]')
    fn(*sys.argv[2:])
