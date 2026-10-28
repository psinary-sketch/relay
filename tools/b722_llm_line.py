# -*- coding: utf-8 -*-
"""b722_llm_line.py -- (R332)(12): THE RELEASE SITTING'S LIST, DRAFTS ALONE. Written whole at b722 by the Write tool.

  read [dry]   the LLM-contribution line quoted from day1/A_Place_to_Stand.md's end matter (after Appendix G's bibliography, before the
               colophon), its line printed; then every wave 1 paper (the eighteen documents of b720's REGISTRY cells, relay
               data/b720_registry_diff.txt) and every wave 1 kernel README (main, read from the local clone, main equal to origin/main
               printed) read against it: SAME (the sentence byte for byte, in the end matter), DIFFERS (a line of the kind -- an LLM or
               model disclosure -- in other words or another position), ABSENT (no such line). Each DIFFERS and ABSENT drafted in the
               monograph's words and position. Nothing in a paper or README is edited. -> data/b722_llm_line_drafts.txt (.json).
               THE NAME GUARD: no line naming the author is quoted -- the colophon's byline is read at run time and any line carrying it
               refuses the bank (relay data/b722_ferry.txt, (R332)(9)(i)); the byline itself is never printed.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ACT = 'b722'
PP = 'D:/MY-DOwnloads/PLACE-papers'
MONO = 'day1/A_Place_to_Stand.md'
# ### the wave 1 papers: b720's REGISTRY cells filled from each document's own text (data/b720_registry_diff.txt), the rows of documents;
# ### 1.2-A to 1.2-D are kernels (REGISTRY :715-:718) and read as READMEs below
PAPERS = [('d1-1', MONO), ('d1-2', 'day1/Exhaustive_Enumeration.md'), ('d1-3', 'day1/Which_Structure_Confines.md'),
          ('d1-4', 'day1/Spectral_Inertness.md'), ('d1-5', 'day1/Seven_Mechanism_Classes.md'), ('d1-6', 'day1/Third_Identity_Element.md'),
          ('d1-7', 'day1/Silence_of_Foundations.md'), ('d1-8', 'day1/ONE_PAGE_PROOF.md'),
          ('1.5a-1', 'phase1.5/proofs/THE_EXCLUSION_ARCHITECTURE.md'), ('1.5a-2', 'phase1.5/proofs/MECHANISM_EXCLUSION.md'),
          ('1.5a-3', 'phase1.5/proofs/IDS_TO_RH.md'), ('1.5a-4', 'phase1.5/proofs/INTEGRATED_PROOF.md'),
          ('1.5c-18', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'), ('1.5c-19', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'),
          ('1.5c-20', 'FACES_LEDGER.md'), ('1.5c-16', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'),
          ('1.5a-8', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'), ('p2-39', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md')]
KERNELS = ['SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-archimedean', 'SIDE-frobenius', 'SIDE-spinor', 'SIDE-rcurve']
KIND = re.compile(r'LLM|language model|\bClaude\b|Anthropic|assisted by')      # ### a line of the kind: a disclosure of model assistance
BIB = re.compile(r'^#+ .*(Bibliograph|References)', re.I)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def monograph():
    L = open(os.path.join(PP, MONO), encoding='utf-8').read().split(NL)
    g = next(i for i, l in enumerate(L) if l.startswith('## Appendix G'))
    rule = next(i for i in range(g + 1, len(L)) if L[i].strip() == '---')          # ### the colophon opens at the first rule after G
    hits = [i for i in range(g, rule) if KIND.search(L[i])]
    if len(hits) != 1:
        sys.exit('### THE MONOGRAPH`S END MATTER CARRIES %d LINES OF THE KIND BETWEEN APPENDIX G AND THE COLOPHON -- NOTHING WRITTEN' % len(hits))
    byline = next(L[i] for i in range(rule, rule + 8) if L[i].startswith('*') and L[i].strip('* ').strip() and 'PLACE' not in L[i]).strip('* ').strip()
    return L, g + 1, hits[0] + 1, rule + 1, L[hits[0]], byline


def end_matter_pos(L):
    """the monograph's position in a document: after the last line of its bibliography section, before what follows; with none, after the
    body's last line, before a closing rule. Returns (line after which the sentence stands, the description)."""
    b = [i for i, l in enumerate(L) if BIB.match(l)]
    if b:
        nxt = next((j for j in range(b[-1] + 1, len(L)) if L[j].startswith('#') or L[j].strip() == '---'), len(L))
        last = max(j for j in range(b[-1], nxt) if L[j].strip())
        return last + 1, 'after its bibliography (%s, :%d-:%d), before :%d' % (L[b[-1]].strip('# ').strip()[:40], b[-1] + 1, last + 1, nxt + 1)
    last = max(j for j in range(len(L)) if L[j].strip())
    return last + 1, 'no bibliography: after the document`s last line (:%d)' % (last + 1)


def in_position(L, n):
    """the monograph's position, as its own end matter defines it: after the bibliography heading and before the first rule after it."""
    b = [i for i, l in enumerate(L) if BIB.match(l)]
    if not b or n is None:
        return None
    rule = next((j for j in range(b[-1] + 1, len(L)) if L[j].strip() == '---'), len(L))
    return b[-1] < n - 1 < rule, b[-1] + 1, rule + 1


def sentence_of(line):
    """a long line quoted from the sentence of the kind: from the end of the sentence before the match."""
    m = KIND.search(line)
    if len(line) <= 300 or not m:
        return line
    s = line.rfind('. ', 0, m.start())
    return '…' + line[s + 2 if s >= 0 else 0:][:300]


def grade(L, sentence, readme=False):
    hits = [(i + 1, l) for i, l in enumerate(L) if KIND.search(l)]
    if not hits:
        return 'ABSENT', None, None
    for n, l in hits:
        if l.strip() == sentence.strip():
            return 'SAME', n, l
    return 'DIFFERS', hits[-1][0], hits[-1][1]


def read(*a):
    t0 = time.time()
    M, g, mline, rule, sentence, byline = monograph()
    S = sentence.strip()
    guard = lambda s: byline and byline in s
    rows = []
    # ### THE CONTROLS, before any document: the monograph against itself SAME; a planted variant DIFFERS; a planted empty document ABSENT
    c1 = grade(M, S)[0]
    c2 = grade(['x', S.replace('strategies of argument', 'proof strategies'), 'y'], S)[0]
    c3 = grade(['# A document', 'no disclosure here'], S)[0]
    controls = [('C1', 'the monograph against its own line', c1, 'SAME'), ('C2', 'a planted variant ("proof strategies")', c2, 'DIFFERS'),
                ('C3', 'a planted document with no line', c3, 'ABSENT')]
    if any(got != want for _k, _w, got, want in controls):
        sys.exit('### A CONTROL NOT AS WANTED: %r -- NOTHING READ' % controls)
    for rid, p in PAPERS:
        L = open(os.path.join(PP, p), encoding='utf-8').read().split(NL)
        gr, n, line = grade(L, S)
        after, where = end_matter_pos(L)
        hits = [(i + 1, l) for i, l in enumerate(L) if KIND.search(l)]
        ip = in_position(L, n)
        rows.append(dict(kind='paper', row=rid, path=p, grade=gr, line=n, text=sentence_of((line or '').strip()), hits=[h[0] for h in hits],
                         position=where, after=after, in_position=ip[0] if ip else None,
                         span=('after the bibliography heading :%d, before the rule :%d' % ip[1:]) if ip else None))
    for k in KERNELS:
        main, om = git('D:/' + k, 'rev-parse', 'main').strip(), git('D:/' + k, 'rev-parse', 'refs/remotes/origin/main').strip()
        L = git('D:/' + k, 'show', 'main:README.md').split(NL)
        gr, n, line = grade(L, S)
        head = next((i + 1 for i, l in enumerate(L) if l.strip().lower() == '## ai disclosure'), None)
        last = max(j for j in range(len(L)) if L[j].strip()) + 1
        rows.append(dict(kind='README', row=k, path='%s README.md at main %s (origin/main equal: %s)' % (k, main[:7], main == om), grade=gr,
                         line=n, text=(line or '').strip(), hits=[i + 1 for i, l in enumerate(L) if KIND.search(l)],
                         position=('under its "## AI disclosure" heading (:%d)' % head) if head else
                         'at the README`s end (after :%d), under a heading "## AI disclosure" as the other wave 1 READMEs carry it' % last,
                         after=n or last))
    bad = [r for r in rows if guard(r['text'])]
    if guard(S) or bad:
        sys.exit('### THE NAME GUARD: %d quoted lines carry the colophon`s byline -- NOTHING WRITTEN' % (len(bad) + guard(S)))
    L = ['%s -- (R332)(12): THE RELEASE SITTING`S LIST, DRAFTS ALONE: THE LLM-CONTRIBUTION LINE AND EVERY WAVE 1 PAPER AND KERNEL README '
         'READ AGAINST IT (%s)' % (ACT, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### THE LINE AS THE MONOGRAPH CARRIES IT: PLACE-papers %s :%d, in the end matter after Appendix G`s bibliography (:%d) and before '
         'the colophon (the rule at :%d), quoted:' % (MONO, mline, g, rule), '    ' + S, '',
         '### THE GRADES, printed before any document: SAME -- the sentence byte for byte; DIFFERS -- a line of the kind (a disclosure of model '
         'assistance: LLM, language model, Claude, Anthropic, "assisted by") in other words; ABSENT -- no line of the kind. Position is read '
         'beside the grade. THE DRAFT for each DIFFERS and ABSENT: the monograph`s sentence verbatim, at the monograph`s position (after the '
         'bibliography, before the colophon; a README under its "## AI disclosure" heading). Nothing in a paper or README is edited.',
         '### THE NAME GUARD: every quoted line read against the colophon`s byline (read at run time, not printed): 0 carry it.', '',
         '## THE CONTROLS, BEFORE ANY DOCUMENT'] + ['  (%s) %s: %s -- AS WANTED' % (k, w, got) for k, w, got, _ in controls] + ['']
    for r in rows:
        L.append('## %s %s -- %s%s' % (r['kind'], r['row'], r['grade'], (' at :%d' % r['line']) if r['line'] else ''))
        L.append('  ' + r['path'] + ('' if r['kind'] == 'README' else ' ; lines of the kind at %s' % (', '.join(':%d' % h for h in r['hits']) or 'none')))
        if r['text']:
            L.append('  READ:  ' + r['text'][:400] + ('…' if len(r['text']) > 400 else ''))
        if r['grade'] != 'SAME':
            if r['kind'] == 'paper' and r['grade'] == 'DIFFERS' and r['in_position']:
                pos = 'in place of :%d, which stands at the monograph`s position (%s): the words differ, the position agrees' % (r['line'], r['span'])
            elif r['kind'] == 'paper' and r['grade'] == 'DIFFERS':
                pos = ('the line at :%d stands outside the monograph`s position%s; the draft stands %s, the line at :%d left for the release '
                       'sitting`s word' % (r['line'], (' (' + r['span'] + ')') if r['span'] else '', r['position'], r['line']))
            elif r['kind'] == 'paper':
                pos = r['position']
            else:
                pos = ('in place of :%d, ' % r['line'] if r['line'] else '') + r['position']
            L += ['  DRAFT: ' + S, '  WHERE: ' + pos]
        L.append('')
    tally = dict((g_, sum(1 for r in rows if r['grade'] == g_)) for g_ in ('SAME', 'DIFFERS', 'ABSENT'))
    L.append('### ### **THE LLM-CONTRIBUTION LINE (PLACE-papers %s :%d) AGAINST %d WAVE 1 PAPERS AND %d KERNEL READMES: SAME %d ; DIFFERS %d ; '
             'ABSENT %d ; DRAFTS %d ; NOTHING EDITED ; %d s.**' % (MONO, mline, len(PAPERS), len(KERNELS), tally['SAME'], tally['DIFFERS'],
                                                                 tally['ABSENT'], tally['DIFFERS'] + tally['ABSENT'], int(time.time() - t0)))
    print(NL.join(L))
    if 'dry' in a:
        return
    for name, data in (('%s_llm_line_drafts.txt' % ACT, NL.join(L) + NL),
                       ('%s_llm_line_drafts.json' % ACT, json.dumps(dict(line=mline, sentence=S, controls=controls, rows=rows), indent=1,
                                                                    ensure_ascii=False) + NL)):
        p = os.path.join(D, name)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print('written data/%s_llm_line_drafts.txt, .json' % ACT)


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'read':
        sys.exit('usage: b722_llm_line.py read [dry]')
    read(*sys.argv[2:])
