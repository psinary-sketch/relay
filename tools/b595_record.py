# -*- coding: utf-8 -*-
"""b595_record.py -- THE ACT'S RECORD TOOL, UNDER (R205). ### ONE SUBCOMMAND PER BANK.

### ### b595: LANE THREE, ACT TWENTY-TWO -- THE DELIBERATION TREE MODULE WRITTEN FROM THE PROMPTS AS A NEW DOCUMENT ON THE
### AUTHOR'S ASK (TECHNE-Core, private, not pushed); THE b547 CITATION SETTLED BY HISTORY LINES.
### Subcommands write only `data/b595_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The template is b594_record.py.
### ### **THIS FILE CARRIES NO SENTENCE OF THE DOCUMENT'S BODY.** The document's prose lives in the scratchpad (`SP`) and in
### TECHNE-Core only; the extraction's question, option and answer text is written to TECHNE-Core only. Relay banks carry
### pointers (session file, tool-use id, transcript line), sha256s, classifications and counts, as the author answered.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
TX = 'C:/Users/echo chamber/.claude/projects/D--'
PRE_PP = 'b229ff9'
PRE_RELAY = '4924e098'
PRE_TE = '12e4176'
STEPZERO = '6a123282'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/cbf1b30e-1310-463d-994c-65478058bd99/scratchpad'
DOC_REL = 'modules/2026-10/DELIBERATION_TREE.md'
EXT_REL = 'modules/2026-10/DELIBERATION_TREE_nodes.json'
DOC = TE + '/' + DOC_REL
EXT = TE + '/' + EXT_REL
SIB_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
FACES = 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md'
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SINCE = '2026-10-01T19:00'      # b577's ferry arrived at 2026-10-01T19:0x; b576's last prompt was at 18:36
UNTIL = '2026-10-02T15:50'      # b594 closed at 15:48; b595's own prompts are banked in data/b595_author_answers.txt

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_abs(path, b):
    open(path + '.tmp', 'wb').write(b)
    os.replace(path + '.tmp', path)


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE SEAT`S SECOND PROMPT MISCOUNTED THE LABEL-FORM ANSWERS: it named three (b577 head block, b578 title and stem clash) and '
    'gave the prose form as "39 of the 41 other answered prompts"; the label form answered four prompts (b578 boundary as well) and '
    'the prose form 39 of the 43 answered. Found by recount before any write; the note is banked beneath the prompt in '
    'data/b595_author_answers.txt, and the answer`s criterion is unaffected by the count.',
    '(b) THE SEAT`S THIRD PROMPT GAVE NINE BACK-MATTER CELLS FOR BALPOS v0.9.5`S RE-PIN: two of the nine (":776", ":782") cite v0.9.4`s '
    'numbering inside a sentence that names v0.9.4, and do not move; the cells citing v0.9.5 lines below the insertion are seven (:783 '
    'once, :791 six times). Found by a printed list of every citation before the write; the seven are re-pinned, the two left, both '
    'figures banked in data/b595_citation_4787.txt.',
    '(c) THE EXTRACTION`S FIRST DRY RUN MISREAD TWO ANSWERS: node 3`s kept a stray opening quote, and node 33`s, given as an unquoted '
    'note, ran on into node 34`s (the parser cut only at a quoted delimiter). Found by printing every answer`s two ends before any '
    'write; the parser now cuts at the call`s next question and strips the surrounding quotes, through the Edit tool, and the dry run '
    'was repeated with all 44 ends read clean.',
    '(d) THE SUITE`S FIRST PRE-RUN FAILED G-ANSWERS-BANKED ON ITS OWN PREDICATE: it wanted three RESULT lines, and the bank rightly '
    'holds two (the first two prompts were one call). Found by the pre-run before the seal; the predicate counts results and calls '
    'through the Edit tool, and the pre-run was re-banked; the arm list did not change.',
    '(e) THE HISTORY-LINE STEP`S FIRST DRY RUN EXITED 1: `cite_faces` returned the new bytes and the dispatcher passed them to '
    '`sys.exit`, printing the file to the terminal and stopping the `&&` chain before BALPOS`s dry run; nothing was written (the '
    'dry flag held, and PLACE-papers` status showed no change). The returns were removed through the Edit tool and both dry runs '
    'repeated before either write.',
]


def defects():
    put_txt('b595_defects.txt', ['### b595 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the b592 answers bank, whole (seven prompts, question and answer verbatim, no options)', RELAY, 'HEAD', 'data/b592_author_answers.txt', list(range(1, 24))),
    ('relay the b593 answers bank, whole (five prompts, question and answer verbatim, no options)', RELAY, 'HEAD', 'data/b593_author_answers.txt', list(range(1, 17))),
    ('PLACE-papers OPEN_TRAILS, the form, its clauses, each act`s answered line and record, b577-b594', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 11872, 11892, 11902, 11904, 11906, 11908, 11920, 11924, 11930, 11932, 11934, 11936, 11944, 11954, 11956, 11964, 11984, 11996,
      12004, 12034, 12044, 12052, 12070, 12072, 12082, 12104, 12118, 12144, 12160, 12178, 12188, 12190, 12192, 12194, 12202, 12220,
      12228, 12230, 12232, 12238]),
    ('PLACE-papers FINDINGS, the census heading, the TECHNE credit re-read, b594`s entry', PP, PRE_PP, 'FINDINGS.md', [4786, 4787, 4788, 6716, 6818]),
    ('PLACE-papers FACES v0.2, b547`s census block and the line after it', PP, PRE_PP, FACES, list(range(213, 234))),
    ('PLACE-papers BALANCE_AND_POSITIVITY v0.9.5, b545`s sentence-read block, its head and its end', PP, PRE_PP, BALPOS, [709, 711, 713, 722, 723, 728, 734, 735, 737, 755, 766, 767, 768, 769]),
    ('relay banned_terms.py, the stems and the pattern', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(62, 68))),
    ('relay b594`s closing push-out, its head', RELAY, 'HEAD', 'data/b594_closing_push_out.txt', list(range(1, 6))),
    ('relay b591`s no-disclosure arm, its needles and its predicate', RELAY, 'HEAD', 'tools/b591_checks.py', [489, 490, 493, 494, 495, 496, 497, 498, 499, 500, 501]),
]


def reads():
    L = ['b595 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    # ### the sibling is private: its head and Placement are cited by line and heading marker only, never by text
    sib = g(TE, 'show', 'HEAD:' + SIB_REL).split(NL)
    marks = [(i, re.match(r'^(#+ \(?[ivx]*\)?|#+ )', l).group(0).strip()) for i, l in enumerate(sib, 1) if l.startswith('#')]
    L += ['', '### TECHNE-Core THE_LOCATED_CLAUSE_METHOD.md (the sibling, private) @ %s -- %d lines; read for its form: title line :1, version '
          'line :3, the provenance line :5, section heads %s ; the Placement table :66-:78 (two columns, object | location). No line of its '
          'text is printed here.' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), len(sib), [(i, m) for i, m in marks])]
    put_txt('b595_reads.txt', L)


# ================================================================================ THE PROMPTS: EXTRACTION (COMPONENT 2)
# ### The trail lines the record holds for each act's answers ("Answered before the seal"), read at b229ff9.
RECORD_LINE = {'b577': 11872, 'b578': 11892, 'b579': 11920, 'b580': 11944, 'b581': 11964, 'b582': 11984, 'b585': 12052, 'b586': 12070,
               'b587': 12104, 'b588': 12118, 'b589': 12144, 'b590': 12160, 'b591': 12178, 'b592': 12202, 'b593': 12220}
# ### The clauses of the form each answer produced, by trail line, read at b229ff9. 'answer': the line is entered under the author's
# ### answer itself; 'ruling': the line is entered under a ruling that made the answer standing (its record names the answer).
CLAUSE = {5: (11904, 'ruling', '(R189)(3) made the stem substitution standing; the answer recorded at :11892'),
          6: (11906, 'answer', 'the ceiling clause'),
          7: (11930, 'ruling', '(R190)(2) added the version line to H28b; the occasion at :11924, the version line the author ruled'),
          9: (11908, 'answer', 'the history clause'),
          11: (11934, 'answer', 'the name-and-title exception'),
          13: (11956, 'answer', 'the placement clause'),
          18: (12044, 'answer', 'inside a dated entry the history clause governs'),
          34: (12190, 'answer', 'the page clause'),
          35: (12192, 'answer', 'the restatement clause'),
          36: (12194, 'answer', 'an era annotation is a dated entry')}
# ### Other standing lines or readings an answer produced, not clauses of the form.
OTHER = {1: (11872, 'the ferry`s Component 4 withdrawn; the edition at the act after'),
         2: (11872, 'the head placement struck; FINDINGS written by appending'),
         19: (12072, 'a reading on the ceiling clause: census proved / exhaustiveness open'),
         31: (12160, 'claim-family text travels in a separate local-only paste')}
# ### Outcomes the record holds after the act. Default: 'stood'.
OUTCOME = {5: 'stood; its clause scoped by :12044 (b585, node 18) and ordered by the precedence order :12228 (b594)',
           8: 'unanswered; put again as node 9 three minutes later',
           9: 'stood; its clause extended by :12044 (b585) and :12194 (b592)',
           11: 'stood; its clause extended by :12082 (b587, (R197)(2))',
           25: 'amended at b589: the answer`s word "outside" recorded as the navigator`s (FINDINGS :6716), the file agreeing with the verdict',
           27: 'HELD at the act (Component 3); the .docx found after the seal, not opened, for the author (:12146)'}
AMENDED = (5, 9, 11, 25)
REVERSED = ()


def _jsonl(path):
    out = []
    with io.open(path, encoding='utf-8') as f:
        for i, ln in enumerate(f, 1):
            try:
                out.append((i, json.loads(ln)))
            except Exception:
                pass
    return out


def _texts(c):
    if isinstance(c, str):
        return [c]
    return [b.get('text', '') for b in (c or []) if isinstance(b, dict) and b.get('type') == 'text']


def _parse_answer(result, q, others):
    """### the answer text for question q inside a tool result: from after `"q"=` to the start of the call's next question
    ### (`, "q2"=`) or the result's closing sentence, its surrounding quotes removed."""
    if result is None:
        return None
    i = result.find('"%s"=' % q)
    if i < 0:
        return None
    start = i + len(q) + 3
    seg = result[start:]
    ends = [seg.find(x) for x in ('. You can now continue', '. Read the answers carefully') if seg.find(x) >= 0]
    for q2 in others:
        j = seg.find(', "%s"=' % q2)
        if j >= 0:
            ends.append(j)
    seg = seg[:min(ends)] if ends else seg
    seg = seg.strip()
    if seg.startswith('"') and seg.endswith('"') and len(seg) >= 2:
        seg = seg[1:-1]
    return seg.strip()


def _classify(ans, opts):
    if ans is None:
        return None, None
    a = ans.strip().strip('"')
    for k, o in enumerate(opts, 1):
        if a == o['label']:
            return 'label', k
    m = re.search(r'\boption (\d)\b', a)
    return ('prose', int(m.group(1))) if m else (None, None)


def prompts(*a):
    """### Extract every AskUserQuestion of b577-b594 from the session transcripts, one node per question, with its sources by line.
    ### Stages the extraction (text verbatim) in the scratchpad for TECHNE-Core (`ext_place` writes it there) and writes relay
    ### data/b595_nodes.json / data/b595_nodes.txt (pointers, sha256s, classifications, counts; no text). `dry`: the scratchpad only."""
    files = sorted((os.path.join(TX, f) for f in os.listdir(TX) if f.endswith('.jsonl')), key=os.path.getmtime)
    nodes = []
    for f in files:
        if os.path.getmtime(f) < 1759190400:
            continue
        rows = _jsonl(f)
        act = None
        pend = {}
        calls = []
        for i, o in rows:
            m = o.get('message') or {}
            c = m.get('content')
            if o.get('type') == 'user':
                for t in _texts(c):
                    mm = re.search(r'ACT (b\d{3})', t)
                    if mm and 'FERRY BEGIN' in t:
                        act = mm.group(1)
                if isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get('type') == 'tool_result' and b.get('tool_use_id') in pend:
                            r = b.get('content')
                            if isinstance(r, list):
                                r = ' '.join(x.get('text', '') for x in r if isinstance(x, dict))
                            call = pend.pop(b['tool_use_id'])
                            call.update(result=r, result_line=i)
                            calls.append(call)
            if o.get('type') == 'assistant' and isinstance(c, list):
                for b in c:
                    if isinstance(b, dict) and b.get('type') == 'tool_use' and b.get('name') == 'AskUserQuestion':
                        pend[b['id']] = dict(act=act, ts=o.get('timestamp', ''), id=b['id'], input=b['input'], call_line=i)
        for call in calls:
            if not (SINCE <= call['ts'] < UNTIL):
                continue
            rejected = 'The user wants to clarify these questions' in (call['result'] or '')
            chat = None
            if rejected:
                for i, o in rows:
                    if i <= call['result_line'] or o.get('type') != 'user':
                        continue
                    t = ' '.join(_texts((o.get('message') or {}).get('content')))
                    if t.strip():
                        chat = (i, t)
                        break
            for q in call['input']['questions']:
                opts = q['options']
                ans, src = None, None
                if rejected:
                    blk = call['result'].split('- "%s"' % q['question'], 1)
                    if len(blk) == 2:
                        mm = re.match(r'\s*Answer: (.*?)(?:\n- "|\Z)', blk[1], re.S)
                        if mm:
                            ans, src = mm.group(1).strip(), ('rejection-notes', call['result_line'])
                    if ans is None and chat and len(call['input']['questions']) >= 1:
                        hm = re.match(r'\s*Answer to the ([^:]+?) prompt', chat[1])
                        key = (hm.group(1).lower() if hm else '')
                        hdr = q['header'].lower()
                        if key and (key.replace('-', ' ') in hdr.replace('-', ' ') or hdr.replace('-', ' ') in key.replace('-', ' ')):
                            ans, src = chat[1].strip(), ('chat', chat[0])
                else:
                    ans = _parse_answer(call['result'], q['question'], [x['question'] for x in call['input']['questions'] if x is not q])
                    if ans and ans.startswith('(no option selected) notes: '):
                        ans = ans[len('(no option selected) notes: '):]
                    src = ('tool-result', call['result_line']) if ans else None
                form, k = _classify(ans, opts)
                rec = [n for n, o in enumerate(opts, 1) if '(Recommended)' in o['label']]
                nodes.append(dict(act=call['act'], ts=call['ts'], session=os.path.basename(f), tool_use_id=call['id'],
                                  call_line=call['call_line'], answer_source=src, header=q['header'], question=q['question'],
                                  options=[dict(label=o['label'], description=o['description']) for o in opts],
                                  recommended=rec[0] if rec else None, answer=ans, form=form, answered=k))
    nodes.sort(key=lambda x: x['ts'])
    for n, x in enumerate(nodes, 1):
        x['n'] = n
        x['relayed'] = (x['form'] == 'prose')
        c = CLAUSE.get(n)
        x['clause'] = dict(line=c[0], basis=c[1], what=c[2]) if c else None
        o = OTHER.get(n)
        x['other'] = dict(line=o[0], what=o[1]) if o else None
        x['record_line'] = RECORD_LINE.get(x['act'])
        x['outcome'] = OUTCOME.get(n, 'stood')
    ext = (json.dumps(dict(source='the session transcripts, AskUserQuestion inputs and results, %s to %s (the author`s answer before b595`s seal)'
                           % (SINCE, UNTIL), nodes=nodes), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    os.makedirs(os.path.dirname(EXT), exist_ok=True)
    put_abs(SP + '/DELIBERATION_TREE_nodes.json', ext)
    pub = []
    for x in nodes:
        pub.append(dict(n=x['n'], act=x['act'], ts=x['ts'], session=x['session'], tool_use_id=x['tool_use_id'], call_line=x['call_line'],
                        answer_source=x['answer_source'], n_options=len(x['options']), recommended=x['recommended'], answered=x['answered'],
                        form=x['form'], relayed=x['relayed'], clause=x['clause'] and dict(line=x['clause']['line'], basis=x['clause']['basis']),
                        other=x['other'] and x['other']['line'], record_line=x['record_line'],
                        outcome=('amended' if x['n'] in AMENDED else 'reversed' if x['n'] in REVERSED else
                                 'superseded' if x['n'] == 8 else 'HELD at the act' if x['n'] == 27 else 'stood'),
                        sha256_question=sha(x['question']), sha256_options=sha(json.dumps(x['options'], ensure_ascii=False, sort_keys=True)),
                        sha256_answer=sha(x['answer']) if x['answer'] else None))
    C = counts(nodes)
    if 'dry' in a:
        for x in pub:
            print('  %2d %s %s:%d ans=%s rec=%s got=%s form=%s clause=%s rec_line=%s %s' % (
                x['n'], x['act'], x['session'][:8], x['call_line'], x['answer_source'], x['recommended'], x['answered'], x['form'],
                x['clause'] and x['clause']['line'], x['record_line'], x['outcome']))
        for k, v in C.items():
            print('    %-58s %s' % (k, v))
        return
    put_json('b595_nodes.json', dict(extraction=dict(path='TECHNE-Core ' + EXT_REL, sha256=sha(ext), bytes=len(ext), staged=SP + '/DELIBERATION_TREE_nodes.json'),
                                     nodes=pub, counts=C))
    L = ['b595 -- THE NODES, AS EXTRACTED. ### pointers, classifications and digests only; the text is in TECHNE-Core %s (sha256 %s).' % (EXT_REL, sha(ext)),
         '### source: the session transcripts (%s, *.jsonl), every AskUserQuestion with %s <= timestamp < %s; one node per question.' % (TX, SINCE, UNTIL),
         '### columns: node | act | session:call line | answer source:line | options | recommended | answered | form | clause (trail line, basis) | '
         'record line | outcome', '']
    for x in pub:
        L.append('  %2d | %s | %s:%d | %s | %d | %s | %s | %s | %s | %s | %s' % (
            x['n'], x['act'], x['session'][:8], x['call_line'], ('%s:%d' % tuple(x['answer_source'])) if x['answer_source'] else 'none',
            x['n_options'], x['recommended'] or '-', x['answered'] or '-', x['form'] or '-',
            (':%d %s' % (x['clause']['line'], x['clause']['basis'])) if x['clause'] else '-', (':%d' % x['record_line']) if x['record_line'] else '-',
            x['outcome']))
    L += ['', '### THE COUNTS:'] + ['    %-58s %s' % (k, v) for k, v in C.items()]
    put_txt('b595_nodes.txt', L)
    for l in L:
        print(l[:220])


def counts(nodes):
    ans = [x for x in nodes if x['answered']]
    withrec = [x for x in ans if x['recommended']]
    match = [x for x in withrec if x['answered'] == x['recommended']]
    div = [x['n'] for x in withrec if x['answered'] != x['recommended']]
    rel = [x for x in ans if x['form'] == 'prose']
    own = [x for x in ans if x['form'] == 'label']
    rel_rec = [x for x in rel if x['recommended']]
    rel_div = [x['n'] for x in rel_rec if x['answered'] != x['recommended']]
    own_rec = [x for x in own if x['recommended']]
    own_div = [x['n'] for x in own_rec if x['answered'] != x['recommended']]
    cl = [x['n'] for x in nodes if CLAUSE.get(x['n'])]
    cl_ans = [n for n in cl if CLAUSE[n][1] == 'answer']
    return {
        'prompts (nodes)': len(nodes),
        'acts with a prompt': len(sorted(set(x['act'] for x in nodes))),
        'options offered': sum(len(x['options']) for x in nodes),
        'nodes answered': len(ans),
        'nodes unanswered (put again)': [x['n'] for x in nodes if not x['answered']],
        'nodes with a recommended option': len([x for x in nodes if x['recommended']]),
        'answered nodes with a recommended option': len(withrec),
        'answer = recommended option': len(match),
        'agreement rate': '%d of %d = %.1f%%' % (len(match), len(withrec), 100.0 * len(match) / max(1, len(withrec))),
        'answer differs from the recommended option (nodes)': div,
        'answers in the prose form (relayed)': len(rel),
        'answers in the label form (the author`s own)': len(own),
        'relayed answers differing from the recommendation': '%d of %d %s' % (len(rel_div), len(rel_rec), rel_div),
        'own answers differing from the recommendation': '%d of %d %s' % (len(own_div), len(own_rec), own_div),
        'answers later reversed': list(REVERSED),
        'answers or their clauses later amended': list(AMENDED),
        'nodes producing a clause of the form': '%d %s' % (len(cl), cl),
        '... entered under the answer itself': '%d %s' % (len(cl_ans), cl_ans),
        '... entered under a ruling that made the answer standing': '%d %s' % (len(cl) - len(cl_ans), [n for n in cl if n not in cl_ans]),
        'answers producing a clause and later reversed': [n for n in cl if n in REVERSED],
    }


# ================================================================================ COMPONENT 1: THE RECORD LINES
B594_ENTRY = '## CP-7, act sixteen: the edition of FACES_OF_H2_AT_FINITE_INSTANCE from its tier block and work-list'
PRECEDENCE = '*Appended 2026-10-02 by b594, under the author’s ruling `(R204)`(2), to the form of an edition (:11864) -- THE PRECEDENCE ORDER:*'


def weight_line():
    """### PLACE-papers FINDINGS: b594's weight, one appended line addressed to b594's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B594_ENTRY)
    if entry != 6818:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b595 to b594’s entry (:%d), under `(R205)`(1) -- b594 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s FACES_OF_H2_AT_FINITE_INSTANCE v0.2 beside the draft unedited, the draft read as v0.1 (it carries no version '
            'number; the seat’s reading, accepted): the one row pinning h1_complete_at_Phi at v0.6.0 = c80bdc2; §2’s R4 row naming the '
            'three faces at their pins; two history lines beneath the dated §4 -- the pole-term difference between P + A − PR and A − PR '
            '(relay data/b550_reading37.txt :18; the ruling’s “b549” the navigator’s) and the finite-support ladder '
            '(h2_sign_iff_forall_upto, forall_upto_iff_rh, v0.3) with a cell or window as a rung; five collisions resolved by the '
            'precedence order and listed (:95, :116, :102, :133, :180); no circularity witness in the draft (the expectation the '
            'navigator’s); no ceiling, stem or fact correction; body 205 against 202 (+3), back matter 76, re-pin 44 of 44; H28a-H28c '
            'held, the scanner clean; both pages re-emitted, 2 of 2; the entry’s mutual-light line (the census :4788, the credit :5563, '
            'the ladder :6012, the faces :6212) and two offerings named. The precedence order at OPEN_TRAILS :12228, the three '
            'instructions at :12230 with the research sequence. The suite read 66 of 66.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b595_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def rule_lines():
    """### PLACE-papers OPEN_TRAILS: the standing line of the author's answer before b595's seal, addressed to the precedence order
    ### (:12228), whose prompt clause it serves. One appended line."""
    Q = _Q()
    p = Q.line_of(Q.OT, PRECEDENCE)
    if p != 12228:
        sys.exit('### THE ADDRESSED LINE MOVED: precedence %s -- NOTHING WRITTEN' % p)
    head = ('*Appended 2026-10-02 by b595 to the precedence order (:%d), under the author’s answer before b595’s seal -- EVERY PROMPT '
            'BANKED VERBATIM:*' % p)
    Q.guard_absent(Q.OT, head)
    text = ('\n%s from b595, every prompt the seat puts to the author is banked in relay at the act’s close with its question, its '
            'options and the recommended mark verbatim, beside the answer as given (relay data/bNNN_author_answers.txt). The occasion is '
            'b595: the relay’s banks held 12 of the 44 prompts of b577-b594 with the question verbatim and none with its options, and the '
            'tree of those prompts was built from the session transcripts by the same answer. Applied first to b595’s own three prompts '
            '(relay data/b595_author_answers.txt).\n' % head)
    r = Q.append_to(Q.OT, text)
    put_json('b595_rule_lines.json', dict(precedence=p, lines=[dict(head=head, line=Q.line_of(Q.OT, head), append=r)]))
    print('  rule line :%s' % Q.line_of(Q.OT, head))


# ================================================================================ COMPONENT 1: THE b547 CITATION
CITE_RE = re.compile(r'FINDINGS\.md`?:4787\b')
FACES_AFTER = 229
BALPOS_AFTER = 767
FACES_LINE = ('*History line, 2026-10-02 (v0.2, b595, under `(R205)`(2)): the dated block above cites the register census as “FINDINGS.md:4787” '
              '(:219, :225); FINDINGS :4787 is a blank line and the census heading, “The five registers of §27.3 and lv-conservation’s h2, '
              'graded by their Lean statements against RH”, is FINDINGS :4788. The block carries unchanged as a dated record.*')
BALPOS_LINE = ('*History line, 2026-10-02 (v0.9.5, b595, under `(R205)`(2)): the dated block above cites the register census as “FINDINGS.md:4787” '
               '(:722, :723, :728, :734, :735, :737, :755); FINDINGS :4787 is a blank line and the census heading, “The five registers of '
               '§27.3 and lv-conservation’s h2, graded by their Lean statements against RH”, is FINDINGS :4788. The block carries unchanged '
               'as a dated record.*')
# ### BALPOS v0.9.5's back-matter cells citing v0.9.5 lines below :767, re-pinned +2 (the author's answer); the two v0.9.4-numbered
# ### citations (":776" in "b546’s line at v0.9.4 :776", ":782" in "beneath v0.9.4 :782") do not move.
REPIN_OLD = {783: 785, 791: 793}


def _disk_lines(rel):
    b = open(os.path.join(PP, *rel.split('/')), 'rb').read()
    eol = b'\r\n' if b'\r\n' in b else b'\n'
    return b, eol, b.split(eol)


def citation_search():
    """### The :4787 search over PLACE-papers at HEAD (the roster and beyond), each occurrence with its document's edition state."""
    out = g(PP, 'grep', '-n', '-I', '-E', r'FINDINGS\.md`?:4787\b', 'HEAD', '--')
    rows = []
    for l in out.split(NL):
        if not l.strip():
            continue
        _h, path, n, text = l.split(':', 3)
        rows.append((path, int(n)))
    files = sorted(set(p for p, _ in rows))
    roster = [x.replace('\\', '/') for x in json.load(io.open(os.path.join(ROOT, 'tools', 'mirror_roster.json'), encoding='utf-8'))['files']]
    tracked = g(PP, 'ls-files').split(NL)
    state = {}
    for f in files:
        stem = re.sub(r'\.md$', '', f)
        eds = sorted(t for t in tracked if t.startswith(stem + '_v') and t.endswith('.md'))
        base = re.sub(r'_v\d+(?:_\d+)*$', '', stem) + '.md'
        if f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md'):
            state[f] = 'a ledger (append-only; its dated entries carry): left'
        elif re.search(r'_v\d+(?:_\d+)*\.md$', f):
            state[f] = 'the CP-7 edition of %s: corrected here by a history line (R205)(2)' % base
        elif eds:
            state[f] = 'the current version, unedited beside its edition %s: left (the edition carries the line)' % eds
        else:
            state[f] = 'no edition: left for its edition'
    L = ['b595 -- THE :4787 SEARCH, (R205)(2). ### PLACE-papers @ %s, git grep of "FINDINGS.md:4787" and "FINDINGS.md`:4787" over every tracked file.'
         % g(PP, 'rev-parse', '--short=7', 'HEAD').strip(),
         '### FINDINGS :4787 is "%s" (blank); :4788 is "%s".' % (g(PP, 'show', 'HEAD:FINDINGS.md').split(NL)[4786][:60],
                                                                 g(PP, 'show', 'HEAD:FINDINGS.md').split(NL)[4787][:120]),
         '### occurrences : %d in %d files' % (len(rows), len(files)), '']
    for f in files:
        L.append('### %s -- %s -- roster: %s' % (f, state[f], 'yes' if f in roster else 'no'))
        L.append('    lines %s' % [n for p, n in rows if p == f])
    put_json('b595_citation_search.json', dict(rows=rows, state=state))
    put_txt('b595_citation_search.txt', L)
    for l in L:
        print('  ' + l[:220])


def cite_faces(*a):
    """### FACES v0.2: one history line (a blank and the line) beneath b547's census block, after :229. Nothing it cites moves."""
    b, eol, ls = _disk_lines(FACES)
    if not ls[FACES_AFTER - 1].startswith(b'*Filed by b547. No byte above this block changes; nothing here is a statement about RH.*') \
            or ls[FACES_AFTER] != b'' or b'<!-- b547 (R157) CENSUS TABLE' not in ls[214]:
        sys.exit('### FACES v0.2 :%d IS NOT THE END OF b547`S CENSUS BLOCK -- NOTHING WRITTEN' % FACES_AFTER)
    if FACES_LINE.encode('utf-8') in b:
        sys.exit('### ALREADY PRESENT -- NOTHING WRITTEN')
    new = ls[:FACES_AFTER] + [b'', FACES_LINE.encode('utf-8')] + ls[FACES_AFTER:]
    nb = eol.join(new)
    if 'dry' not in a:
        put_abs(os.path.join(PP, *FACES.split('/')), nb)
    print('  FACES v0.2: +2 lines after :%d (%s); %d -> %d bytes' % (FACES_AFTER, 'dry' if 'dry' in a else 'written', len(b), len(nb)))


def _repin_balpos_line(l):
    """### re-pin one back-matter line: v0.9.5 citations :783 and :791 to +2; a citation preceded by "v0.9.4 " is not touched."""
    def sub(m):
        if l[max(0, m.start() - 7):m.start()] == 'v0.9.4 ':
            return m.group(0)
        n = int(m.group(1))
        return ':%d' % REPIN_OLD[n] if n in REPIN_OLD else m.group(0)
    return re.sub(r':(\d{3})\b', sub, l)


def cite_balpos(*a):
    """### BALPOS v0.9.5: one history line beneath b545's sentence-read block (after :767), and the back-matter cells citing v0.9.5
    ### lines below it re-pinned +2 (the author's answer before the seal). Both values banked."""
    b, eol, ls = _disk_lines(BALPOS)
    if not ls[BALPOS_AFTER - 1].startswith(b'*Filed by b545. No byte above this block changes; nothing deposits;') \
            or ls[BALPOS_AFTER] != b'' or not ls[708].startswith(b'<!-- b545 (R155) SENTENCE READ'):
        sys.exit('### BALPOS v0.9.5 :%d IS NOT THE END OF b545`S SENTENCE-READ BLOCK -- NOTHING WRITTEN' % BALPOS_AFTER)
    if BALPOS_LINE.encode('utf-8') in b:
        sys.exit('### ALREADY PRESENT -- NOTHING WRITTEN')
    tag = [i for i, l in enumerate(ls) if l.startswith(b'<!-- b593 (R203) THE v0.9.5 EDITION')]
    if len(tag) != 1:
        sys.exit('### THE BACK-MATTER TAG IS NOT UNIQUE -- NOTHING WRITTEN')
    rp = []
    out = list(ls)
    for i in range(tag[0], len(out)):
        s = out[i].decode('utf-8')
        t = _repin_balpos_line(s)
        if t != s:
            rp.append(dict(old_line=i + 1, new_line=i + 3, old=[m.group(0) for m in re.finditer(r'(?<!v0\.9\.4 ):(?:783|791)\b', s)],
                           kept=[m.group(0) for m in re.finditer(r'v0\.9\.4 :\d{3}', s)]))
            out[i] = t.encode('utf-8')
    n_cells = sum(len(x['old']) for x in rp)
    new = out[:BALPOS_AFTER] + [b'', BALPOS_LINE.encode('utf-8')] + out[BALPOS_AFTER:]
    nb = eol.join(new)
    if n_cells != 7:
        sys.exit('### RE-PIN FOUND %d CELLS, NOT 7 -- NOTHING WRITTEN %s' % (n_cells, rp))
    if 'dry' not in a:
        put_abs(os.path.join(PP, *BALPOS.split('/')), nb)
        put_json('b595_balpos_repin.json', dict(after=BALPOS_AFTER, cells=n_cells, rows=rp, map=REPIN_OLD, prompt_said=9,
                                                kept_v094=[':776', ':782']))
    print('  BALPOS v0.9.5: +2 lines after :%d ; re-pinned cells %d on %d lines (%s)' % (BALPOS_AFTER, n_cells, len(rp), 'dry' if 'dry' in a else 'written'))
    for x in rp:
        print('    back matter :%d -> :%d  cells %s  kept (v0.9.4) %s' % (x['old_line'], x['new_line'], x['old'], x['kept']))


def citation_bank():
    """### The bank of (R205)(2): the search, the two history lines and the re-pin, both values."""
    S = jl('b595_citation_search.json')
    R = jl('b595_balpos_repin.json') if os.path.exists(os.path.join(D, 'b595_balpos_repin.json')) else {}
    L = rd('b595_citation_search.txt').rstrip(NL).split(NL)
    fl = io.open(os.path.join(PP, *FACES.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    bl = io.open(os.path.join(PP, *BALPOS.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    L += ['', '### THE HISTORY LINES, each beneath the dated block that holds the citations (the author`s answer: beneath the block`s end, '
          'nothing re-pinned in FACES; BALPOS`s back matter re-pinned +2):',
          '    FACES v0.2 :%d -- %s' % (FACES_AFTER + 2, 'present' if fl[FACES_AFTER + 1] == FACES_LINE else '### ABSENT'),
          '    BALPOS v0.9.5 :%d -- %s' % (BALPOS_AFTER + 2, 'present' if bl[BALPOS_AFTER + 1] == BALPOS_LINE else '### ABSENT'),
          '', '### BALPOS v0.9.5`s back-matter re-pin: the seat`s prompt said 9 cells; the citations of v0.9.5 lines below :%d are %s; '
          'the two v0.9.4-numbered citations (:776, :782) do not move.' % (BALPOS_AFTER, R.get('cells'))]
    for x in R.get('rows', []):
        L.append('    back matter line :%d (now :%d) -- old %s -> new %s ; kept v0.9.4 %s' % (
            x['old_line'], x['new_line'], x['old'], [':%d' % REPIN_OLD[int(c[1:])] for c in x['old']], x['kept']))
    put_txt('b595_citation_4787.txt', L)


# ================================================================================ COMPONENT 2: THE DOCUMENT
SECTION_RE = re.compile(r'^## \((i|ii|iii|iv|v|vi|vii|viii)\) ', re.M)
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|GRH (?:is )?established|RH IS SIMPLE|[Tt]he theorem is at rest|'
                     r'The proof is pointing|closes the catalogue\b|Establishes exhaustiveness|closes exhaustiveness|catalogue is exhaustive\.|'
                     r'(?:proves|proved|settles|resolves) (?:the )?(?:conjecture|hypothesis|Riemann)|zeros? (?:all )?(?:lie|lies) on the|'
                     r'[Tt]he Riemann Hypothesis — established|problem closed \(RH|\bRH \(kernel-verified\)|With GRH (?:established|proved)')
TABLE_HEAD = '| node | act | the question, verbatim | the options, verbatim (the recommended marked ▶) | the answer, verbatim, and its form | clause produced (trail line) | outcome |'


def _cell(s):
    return ' '.join((s or '').replace('|', '\\|').split())


def _sections(text):
    ms = list(SECTION_RE.finditer(text))
    out = []
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        out.append((m.group(1), text[m.start():end]))
    return out


def _prose_sentences(text):
    """### prose sentences of the body (i)-(vii), tables and headings dropped, markdown stripped, at least 40 characters -- the
    ### no-disclosure needles (b591's form, carried)."""
    body = ''.join(s for k, s in _sections(text) if k != 'viii')
    out = []
    for para in re.split(r'\n\s*\n', body):
        if para.lstrip().startswith(('|', '#', '```')):
            continue
        flat = ' '.join(re.sub(r'[*_`]', '', para).split())
        for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(])', flat):
            if len(s) >= 40:
                out.append(s)
    return out


def _words_outside_tables(text, sec_filter=None):
    n = 0
    for k, s in _sections(text):
        if sec_filter and k not in sec_filter:
            continue
        for l in s.split(NL):
            if l.lstrip().startswith('|'):
                continue
            n += len(l.split())
    return n


def _table(nodes):
    L = [TABLE_HEAD, '|:--|:--|:--|:--|:--|:--|:--|']
    for x in nodes:
        opts = []
        for k, o in enumerate(x['options'], 1):
            mark = '▶ ' if x['recommended'] == k else ''
            opts.append('%s%d. %s :: %s' % (mark, k, _cell(o['label']), _cell(o['description'])))
        if x['answered']:
            form = ('relayed: the prose form' if x['form'] == 'prose' else 'the author’s own: the label selected')
            ans = 'option %d (%s). %s' % (x['answered'], form, _cell(x['answer']))
        else:
            ans = 'no answer; put again as node %d' % (x['n'] + 1)
        if x['clause']:
            cl = 'OPEN_TRAILS :%d, %s (%s)' % (x['clause']['line'], _cell(x['clause']['what']),
                                                'under the answer' if x['clause']['basis'] == 'answer' else 'under the ruling that made it standing')
        elif x['other']:
            cl = 'none of the form; OPEN_TRAILS :%d, %s' % (x['other']['line'], _cell(x['other']['what']))
        else:
            cl = 'none'
        rec = (' Recorded at OPEN_TRAILS :%d.' % x['record_line']) if x['record_line'] else ''
        L.append('| %d | %s | %s | %s | %s | %s | %s%s |' % (x['n'], x['act'], _cell(x['question']), ' ◦ '.join(opts), ans, cl, _cell(x['outcome']), rec))
    return L


def _counts_table(C):
    L = ['| count | value |', '|:--|:--|']
    for k, v in C.items():
        L.append('| %s | %s |' % (_cell(k.replace('`', '’')), _cell(str(v))))
    return L


def _corr_table(nodes):
    L = ['| trail line | what it holds | nodes citing it |', '|:--|:--|:--|']
    cites = {}
    for x in nodes:
        if x['record_line']:
            cites.setdefault(x['record_line'], ('the act’s answers before the seal, recorded', []))[1].append(x['n'])
        if x['clause']:
            cites.setdefault(x['clause']['line'], (_cell(x['clause']['what']), []))[1].append(x['n'])
        if x['other']:
            cites.setdefault(x['other']['line'], (_cell(x['other']['what']), []))[1].append(x['n'])
    for ln in sorted(cites):
        what, ns = cites[ln]
        L.append('| OPEN_TRAILS :%d | %s | %s |' % (ln, what, ', '.join(str(n) for n in sorted(set(ns)))))
    L.append('| OPEN_TRAILS :12228 | the precedence order, which orders every clause above (b594) | 5, 6, 9, 11, 18, 35, 36 |')
    L.append('| FINDINGS :6716 | the TECHNE credit re-read (b589) | 25 |')
    return L


def doc_build():
    """### Assemble the document in the scratchpad from the seat's prose (SP/tree_prose.md, private) and the extraction:
    ### <<TABLE>>, <<COUNTS>>, <<CORRESPONDENCE>> replaced. Writes SP/DELIBERATION_TREE.md only."""
    ext = json.load(io.open(SP + '/DELIBERATION_TREE_nodes.json', encoding='utf-8'))
    nodes = ext['nodes']
    prose = io.open(SP + '/tree_prose.md', encoding='utf-8').read().replace(chr(13), '')
    C = counts(nodes)
    for k, v in (('<<TABLE>>', NL.join(_table(nodes))), ('<<COUNTS>>', NL.join(_counts_table(C))), ('<<CORRESPONDENCE>>', NL.join(_corr_table(nodes)))):
        if prose.count(k) != 1:
            sys.exit('### PLACEHOLDER %s FOUND %d TIMES -- NOTHING WRITTEN' % (k, prose.count(k)))
        prose = prose.replace(k, v)
    put_abs(SP + '/DELIBERATION_TREE.md', prose.encode('utf-8'))
    print('  assembled: %s/DELIBERATION_TREE.md (%d bytes, sha256 %s)' % (SP, len(prose.encode('utf-8')), sha(prose)))


def doc_scan(which='draft'):
    """### The ceiling read and the stem scan over the assembled draft or the placed file; words per section outside tables; the
    ### table's rows against the extraction. Banked by position and phrase; never a sentence."""
    import banned_terms as BT
    path = DOC if which == 'placed' else SP + '/DELIBERATION_TREE.md'
    text = io.open(path, encoding='utf-8').read().replace(chr(13), '')
    ls = text.split(NL)
    secs = _sections(text)
    starts = {}
    for k, s in secs:
        starts[k] = text[:text.find(s)].count(NL) + 1
    def sec_of(i):
        cur = 'head'
        for k, st in sorted(starts.items(), key=lambda kv: kv[1]):
            if i >= st:
                cur = k
        return cur
    ceil, stems = [], []
    for i, l in enumerate(ls, 1):
        intable = l.lstrip().startswith('|')
        for m in CEILING.finditer(l):
            ceil.append(dict(line=i, section=sec_of(i), table=intable, phrase=m.group(0)))
        for m in BT.PAT.finditer(l):
            if not any(rx.search(l) for rx, _ in BT.EXCEPT):
                stems.append(dict(line=i, section=sec_of(i), table=intable, phrase=m.group(0)))
    words = {k: _words_outside_tables(text, [k]) for k, _s in secs}
    body = sum(v for k, v in words.items() if k != 'viii')
    ext = json.load(io.open(SP + '/DELIBERATION_TREE_nodes.json', encoding='utf-8'))
    rows = [l for l in ls if re.match(r'^\| \d+ \| b\d{3} \| ', l)]
    want = _table(ext['nodes'])[2:]
    res = dict(which=which, sha256=sha(text), words=words, body_outside_tables=body, table_rows=len(rows), rows_equal=rows == want,
               ceiling_body=[c for c in ceil if not c['table'] and c['section'] != 'viii'], ceiling_table=len([c for c in ceil if c['table']]),
               ceiling_bm=[c for c in ceil if not c['table'] and c['section'] == 'viii'],
               stems_body=[s for s in stems if not s['table'] and s['section'] != 'viii'], stems_table=len([s for s in stems if s['table']]),
               stems_bm=[s for s in stems if not s['table'] and s['section'] == 'viii'],
               sentences=len(_prose_sentences(text)))
    put_json('b595_doc_scan_%s.json' % which, res)
    L = ['b595 -- THE DOCUMENT`S READ, %s. ### positions and phrases only; no sentence of the document is printed.' % which,
         '### sha256 %s' % res['sha256'],
         '### words outside tables per section %s ; body (i)-(vii) %d (cap 2500)' % (words, body),
         '### the table: %d rows ; equal to the extraction row for row: %s' % (len(rows), res['rows_equal']),
         '### the ceiling read: body %d %s ; back matter %d ; inside the table`s verbatim quotations %d' % (
             len(res['ceiling_body']), res['ceiling_body'], len(res['ceiling_bm']), res['ceiling_table']),
         '### the stem scan (banned_terms.PAT less its EXCEPT): body %d %s ; back matter %d ; inside the table`s verbatim quotations %d' % (
             len(res['stems_body']), res['stems_body'], len(res['stems_bm']), res['stems_table']),
         '### prose sentences (the no-disclosure needles) : %d' % res['sentences']]
    put_txt('b595_doc_scan_%s.txt' % which, L)
    for x in L[1:]:
        print('  ' + x[:300])


def ext_place():
    """### TECHNE-Core: the extraction written beside the document (the file created; the seat commits it alone)."""
    if os.path.exists(EXT):
        sys.exit('### THE FILE EXISTS AT %s -- NOTHING WRITTEN' % EXT)
    b = open(SP + '/DELIBERATION_TREE_nodes.json', 'rb').read()
    if sha(b) != jl('b595_nodes.json')['extraction']['sha256']:
        sys.exit('### THE STAGED EXTRACTION DOES NOT MATCH THE RELAY BANK`S DIGEST -- NOTHING WRITTEN')
    os.makedirs(os.path.dirname(EXT), exist_ok=True)
    put_abs(EXT, b)
    print('  written: %s (%d bytes, sha256 %s)' % (EXT, len(b), sha(b)))


def doc_place():
    """### TECHNE-Core: the assembled document written beside the method document (the file created; the seat commits it alone)."""
    if os.path.exists(DOC):
        sys.exit('### THE FILE EXISTS AT %s -- NOTHING WRITTEN' % DOC)
    b = io.open(SP + '/DELIBERATION_TREE.md', encoding='utf-8').read().replace(chr(13), '').encode('utf-8')
    put_abs(DOC, b)
    print('  written: %s (%d bytes, sha256 %s)' % (DOC, len(b), sha(b)))


# ================================================================================ THE HYPOTHESES
def h33():
    """### H33a-H33d, each by its letter, the other figure printed beside it."""
    nb = jl('b595_nodes.json')
    nodes = nb['nodes']
    C = nb['counts']
    sc = jl('b595_doc_scan_placed.json')
    # H33a: the relay banks -- questions verbatim, option sets verbatim (the two shapes of the reads, re-run here)
    ext = json.load(io.open(EXT, encoding='utf-8'))
    def norm(s):
        return ' '.join(s.split())
    def an(s):
        return re.sub(r'[^0-9A-Za-z]+', '', s)
    banks = {}
    for dp, _dn, fs in os.walk(D):
        for f in fs:
            if f.endswith(('.txt', '.json', '.md')) and not f.startswith('b595_'):
                p = os.path.join(dp, f)
                if os.path.getsize(p) < 30_000_000:
                    t = io.open(p, encoding='utf-8', errors='replace').read()
                    banks[p] = (norm(t), an(t))
    qv, ov = [], []
    for x in ext['nodes']:
        if any(norm(x['question']) in t for t, _a in banks.values()):
            qv.append(x['n'])
        if all(any(norm(o['description']) in t for t, _a in banks.values()) for o in x['options']):
            ov.append(x['n'])
    both = sorted(set(qv) & set(ov))
    h33a = 'HOLDS' if len(both) >= 25 else 'REFUTED'
    rate = C['answer = recommended option'] / float(C['answered nodes with a recommended option'])
    h33b = 'HOLDS' if rate <= 0.8 else 'REFUTED'
    cl_rev = C['answers producing a clause and later reversed']
    h33c = 'HOLDS' if not cl_rev else 'REFUTED'
    n_ceil = len(sc['ceiling_body']) + len(sc['ceiling_bm']) + sc['ceiling_table']
    n_stem = len(sc['stems_body']) + len(sc['stems_bm']) + sc['stems_table']
    h33d = 'HOLDS' if n_ceil == 0 and n_stem == 0 else 'REFUTED'
    H = dict(H33a=h33a, H33b=h33b, H33c=h33c, H33d=h33d, nodes=len(nodes), q_verbatim=qv, opts_verbatim=ov, both=both, rate=rate,
             divergent=C['answer differs from the recommended option (nodes)'], clause_reversed=cl_rev, ceiling_whole=n_ceil, stems_whole=n_stem,
             ceiling_body=len(sc['ceiling_body']), stems_body=len(sc['stems_body']), ceiling_table=sc['ceiling_table'], stems_table=sc['stems_table'],
             body_words=sc['body_outside_tables'], sha256=sc['sha256'], table_rows=sc['table_rows'], rows_equal=sc['rows_equal'])
    put_json('b595_h33.json', H)
    L = ['b595 -- H33a-H33d, EACH BY ITS LETTER.',
         '  H33a %s -- nodes recoverable from the relay banks with question and options verbatim: %d (question verbatim %d %s ; option set verbatim '
         '%d %s) ; from the session transcripts: %d' % (h33a, len(both), len(qv), qv, len(ov), ov, len(nodes)),
         '  H33b %s -- the answer matched the recommended option in %s (cap: four of every five, 80.0%%) ; divergent nodes %s' % (
             h33b, C['agreement rate'], H['divergent']),
         '  H33c %s -- answers that produced a clause of the form and were later reversed: %s ; answers or clauses amended %s' % (
             h33c, cl_rev or 'none', C['answers or their clauses later amended']),
         '  H33d %s -- the document, whole: ceiling hits %d, banned stems %d ; the body and back matter (outside the table): ceiling %d, stems '
         '%d ; inside the table`s verbatim quotations of the record: ceiling %d, stems %d' % (
             h33d, n_ceil, n_stem, len(sc['ceiling_body']) + len(sc['ceiling_bm']), len(sc['stems_body']) + len(sc['stems_bm']),
             sc['ceiling_table'], sc['stems_table']),
         '  the body outside the tables: %d words (cap 2500) ; table rows %d, equal to the extraction: %s' % (sc['body_outside_tables'],
                                                                                                         sc['table_rows'], sc['rows_equal'])]
    put_txt('b595_h33.txt', L)
    for l in L:
        print(l[:300])


# ================================================================================ THE SCORES AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERNELS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
           'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
           'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
NAV_DIVERGENT = {'the head block': 2, 'the §7 scope': 35, 'the :33 ceiling': 12, 'the TECHNE placement': 32, 'the ENUMERA cap': 19}


def scores():
    H, nb = jl('b595_h33.json'), jl('b595_nodes.json')
    C = nb['counts']
    byn = {x['n']: x for x in nb['nodes']}
    heads = {k: g('D:/' + k, 'rev-parse', 'main').strip() for k in KERNELS}
    kern_ok = all(heads[k].startswith(v) for k, v in KERNELS.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pub = rd('b595_no_body_public.txt')
    nav = {k: ('divergent' if byn[n]['recommended'] and byn[n]['answered'] != byn[n]['recommended'] else
               'no recommended option marked' if not byn[n]['recommended'] else 'matched') for k, n in NAV_DIVERGENT.items()}
    cl = [x for x in nb['nodes'] if x['clause']]
    a2 = rd('b595_page_arms.txt')
    R = jl('b595_balpos_repin.json')
    S = dict(
        N1=('HELD' if H['H33a'] == 'HOLDS' else 'REFUTED', 'H33a %s: %d nodes from the relay banks with question and options verbatim ; %d from '
            'the session transcripts, the source the author answered' % (H['H33a'], len(H['both']), H['nodes'])),
        N2=('HELD' if H['H33b'] == 'HOLDS' and all(v == 'divergent' for v in nav.values()) else 'REFUTED',
            'H33b %s (%s) ; the five named: %s' % (H['H33b'], C['agreement rate'], nav)),
        N3=('HELD' if H['H33c'] == 'HOLDS' else 'REFUTED', 'H33c %s ; reversed none ; amended %s' % (H['H33c'], C['answers or their clauses later amended'])),
        N4=('HELD' if len(cl) >= 10 and all(x['clause']['line'] for x in cl) else 'REFUTED',
            'nodes producing a clause of the form, each cited: %d %s ; under the answer itself %s' % (
                len(cl), [(x['n'], x['clause']['line']) for x in cl], C['... entered under the answer itself'])),
        N5=('HELD' if kern_ok and pp_ch == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', FACES]) and 'NO BODY SENTENCE' in pub else 'REFUTED',
            'nothing deposits; kernel heads %s; PLACE-papers %s (BALPOS v0.9.5 by the author`s answer, %s cells re-pinned) ; %s' % (
                'unmoved' if kern_ok else heads, pp_ch, R.get('cells'), (pub.split(NL)[-1] if pub else '?'))),
        S1=('HELD' if H['nodes'] == 44 else 'REFUTED', 'nodes extracted %d' % H['nodes']),
        S2=('HELD' if C['answer = recommended option'] == 35 and C['answered nodes with a recommended option'] == 41 else 'REFUTED',
            'agreement %s' % C['agreement rate']),
        S3=('HELD' if C['nodes producing a clause of the form'].startswith('10 ') and C['... entered under the answer itself'].startswith('8 ') else 'REFUTED',
            'clauses %s ; under the answer %s' % (C['nodes producing a clause of the form'], C['... entered under the answer itself'])),
        S4=('HELD' if R.get('cells') == 7 and 'PAGE ARMS PASSING : 2 of 2' in a2 else 'REFUTED',
            'BALPOS re-pin cells %s ; page arms after the history lines: %s' % (R.get('cells'),
                                                                               re.search(r'PASSING : (\d of 2)', a2).group(1) if re.search(r'PASSING : (\d of 2)', a2) else '?')),
        S5=('HELD' if H['H33d'] == 'REFUTED' and H['ceiling_body'] == 0 and H['stems_body'] == 0 and (H['stems_table'] + H['ceiling_table']) > 0 else 'REFUTED',
            'H33d %s in its letter by the table`s verbatim quotations (ceiling %d, stems %d) ; body ceiling %d, stems %d' % (
                H['H33d'], H['ceiling_table'], H['stems_table'], H['ceiling_body'], H['stems_body'])),
    )
    S.update(H33a=(H['H33a'], S['N1'][1]), H33b=(H['H33b'], '%s ; divergent nodes %s' % (C['agreement rate'], H['divergent'])),
             H33c=(H['H33c'], 'reversed none'), H33d=(H['H33d'], S['S5'][1]))
    put_json('b595_scores.json', S)
    for k in SCORE_KEYS + ('H33a', 'H33b', 'H33c', 'H33d'):
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:200]))


def no_body_public():
    """### The no-disclosure arm extended (b591's form): needles built at run time from the placed file's prose sentences, against
    ### every relay file this act writes, every appended PLACE-papers byte, the two history lines, and SIDE-global-section."""
    text = io.open(DOC, encoding='utf-8').read().replace(chr(13), '')
    nd = [' '.join(x.split()) for x in _prose_sentences(text)]
    pub = {}
    for f in sorted(os.listdir(D)):
        if f.startswith(('b595_', 'audit_b595_')) and f != 'b595_no_body_public.txt':
            pub['relay/data/' + f] = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
    for f in sorted(os.listdir(os.path.join(ROOT, 'tools'))):
        if f.startswith('b595_'):
            pub['relay/tools/' + f] = io.open(os.path.join(ROOT, 'tools', f), encoding='utf-8', errors='replace').read()
    for rel in ('FINDINGS.md', 'OPEN_TRAILS.md', FACES, BALPOS):
        pre = g(PP, 'show', '%s:%s' % (PRE_PP, rel))
        now = io.open(os.path.join(PP, *rel.split('/')), encoding='utf-8').read().replace(chr(13), '')
        pub['PLACE-papers ' + rel + ' (changed bytes)'] = now[len(pre):] if now.startswith(pre) else NL.join(set(now.split(NL)) - set(pre.split(NL)))
    pub['SIDE-global-section diff'] = g('D:/SIDE-global-section', 'diff', 'HEAD')
    hits = [(k, i) for k, t in pub.items() for i, n in enumerate(nd) if n in ' '.join(t.split())]
    L = ['b595 -- THE NO-DISCLOSURE ARM, EXTENDED TO THE DELIBERATION TREE. ### needles: the placed file`s prose sentences (i)-(vii), %d, '
         'built at run time and not printed; haystacks %d.' % (len(nd), len(pub))]
    L += ['    %s' % k for k in pub]
    L.append('### hits: %d %s' % (len(hits), [h[0] for h in hits]))
    L.append('### %s' % ('NO BODY SENTENCE REACHES relay, PLACE-papers OR SIDE-global-section' if not hits and len(nd) >= 30 else 'NOT CLEAN'))
    put_txt('b595_no_body_public.txt', L)
    print(L[0][:200])
    print(L[-2][:200])
    print(L[-1])


def page_arms():
    """### both page arms run at HEAD after the history-line commits (the page clause's question: did a Placement move?)."""
    import g_chain_page as GCP
    L = ['b595 -- THE PAGE ARMS AFTER THE TWO HISTORY-LINE COMMITS (PLACE-papers %s)' % g(PP, 'rev-parse', '--short=7', 'HEAD').strip()]
    n = 0
    for arm, nodes, probe in (('G-CHAIN-PAGE', 'b592_nodes.txt', 'b592_probe_out.txt'), ('G-CHAIN-PAGE-CHI', 'b592_nodes_chi.txt', 'b592_chi_probe_out.txt')):
        r = GCP.arm(os.path.join(D, nodes), os.path.join(SP, '_b595_gcp'), os.path.join(D, probe))
        ok = r.get('ok') is True
        n += ok
        L.append('  %s : %s' % (arm, 'PASS' if ok else 'FAIL %s' % {k: v for k, v in r.items() if k != 'ok'}))
    L.append('### PAGE ARMS PASSING : %d of 2' % n)
    put_txt('b595_page_arms.txt', L)
    for l in L:
        print(l[:200])


TITLE = ('## The deliberation tree: the relay’s prompts since b577 as nodes with options, answers, clauses produced and outcomes; the counts; '
         'the scoring rule stated')
TRAIL_HEAD = ('### b595 — lane three, act twenty-two under (R205): the deliberation tree written from the prompts as a new document in '
              'TECHNE-Core, private and not pushed; the b547 citation settled by history lines')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _te_commit(path):
    return g(TE, 'log', '-1', '--format=%h', '--', path).strip() or '?'


def findings():
    Q = _Q()
    S, H, wl, rl, nb = jl('b595_scores.json'), jl('b595_h33.json'), jl('b595_weight_line.json'), jl('b595_rule_lines.json'), jl('b595_nodes.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    e = ['', TITLE, '',
         '*Filed at b595 on the author’s ruling `(R205)`. Banks: relay `data/b595_nodes.json` (pointers, digests and classifications, no '
         'text), `data/b595_author_answers.txt`, `data/b595_h33.txt`, `data/b595_citation_4787.txt`, `data/b595_no_body_public.txt`. '
         'Nothing deposits.*', '',
         '**The document** (`(R205)`(3), the author’s explicit ask): `DELIBERATION_TREE.md`, at TECHNE-Core `%s` (private, committed alone '
         'at %s, not pushed); %d nodes; sha256 `%s`. Its extraction beside it, `%s` (committed alone at %s, not pushed), sha256 `%s`. '
         'The nodes come from the session transcripts, as the author answered before the seal; the relay banks held 12 of them with the '
         'question verbatim and none with its options.' % (DOC_REL, _te_commit(DOC_REL), H['nodes'], H['sha256'], EXT_REL, _te_commit(EXT_REL),
                                                           nb['extraction']['sha256']), '',
         '**The b547 citation** (`(R205)`(2)): one history line beneath b547’s census block in `%s` (PLACE-papers %s) and one beneath '
         'b545’s sentence-read block in `%s` (PLACE-papers %s, its back matter re-pinned at seven cells), each stating that the census '
         'heading is FINDINGS :4788; the other occurrences listed in relay `data/b595_citation_4787.txt` and left.' % (
             FACES, _pp_commit('b595 housekeeping -- FACES'), BALPOS, _pp_commit('b595 housekeeping -- BALANCE')), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the tree re-reads the form’s clauses at OPEN_TRAILS :11904-:12194 as answers '
         'given before seals, and FINDINGS :6716 (b589’s TECHNE credit re-read) as the one answer amended later; the census heading '
         'FINDINGS :4788 is re-cited by two history lines; its own reading is changed by the precedence order (OPEN_TRAILS :12228), '
         'which orders the clauses ten of its nodes produced. It strengthens one of the programme’s offerings: the relay’s record of '
         'whose reasoning failed.', '',
         '**The record lines.** b594’s weight at FINDINGS :%d; the standing line on prompts banked verbatim at OPEN_TRAILS :%d.' % (
             wl['line'], rl['lines'][0]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in ('H33a', 'H33b', 'H33c', 'H33d') + SCORE_KEYS) + '.', '',
         '**Next.** Per `(R205)`(5): b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY’s edition, H29a-H29c as '
         '`(R194)`(3) fixed them; the author rules on the closing.', '',
         '*Nothing deposits; no kernel written; no sentence of the new document’s body is written here; README, REGISTRY and ERRATA '
         'unwritten; nothing here is a statement about RH or any zero.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b595_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, rl, H = jl('b595_scores.json'), jl('b595_findings.json'), jl('b595_weight_line.json'), jl('b595_rule_lines.json'), jl('b595_h33.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R205) ratified.** (1) b594 at its weight. (2) The b547 citation. (3) The deliberation tree. (4) H33a-H33d. (5) The act '
             'after: b596.', '',
             '**Entered:** FINDINGS.md:%d (b594’s weight), :%d (the entry: name, location, node count, sha256); OPEN_TRAILS.md:%d (every '
             'prompt banked verbatim), this record; PLACE-papers `%s` and `%s` (one history line each, housekeeping, each alone); '
             'TECHNE-Core `%s` and `%s` (each alone, not pushed).' % (wl['line'], fj['entry_line'], rl['lines'][0]['line'], FACES, BALPOS, EXT_REL, DOC_REL), '',
             '**Answered before the seal, by the author** (relay data/b595_author_answers.txt): the nodes from the session transcripts, '
             'the extraction private beside the document, H33a scored in its letter on the relay banks, and the standing line that every '
             'prompt is banked verbatim; the prose form marks a relayed answer, which the author’s passing it on ratifies with the same '
             'authority; the history lines beneath each citing block’s end, BALPOS v0.9.5’s back matter re-pinned. **Recorded as the '
             'navigator’s:** `(R205)`(2)’s “the earliest”, and `(R205)`(3)’s “from the relay’s prompt banks”, the banks holding no option set.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in ('H33a', 'H33b', 'H33c', 'H33d') + SCORE_KEYS) + '.**', '',
             '**Next:** per `(R205)`(5), b596, W-ORD-SIMPLICITY-FACE as the research act ahead of SIMPLICITY’s edition, H29a-H29c as fixed; '
             'the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; ERRATA untouched; FACES_LEDGER untouched; row U1 '
             'unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b595_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b595_trail.json')['line'])


def desk():
    S = jl('b595_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    HK = ('H33a', 'H33b', 'H33c', 'H33d')
    L = ['=' * 104, 'b595 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H33a-H33d.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **' + ' ; '.join('%s %s' % (k, S[k][0]) for k in HK) + '.**', '']
    L += rd('b595_defects.txt').rstrip(NL).split(NL)
    put_txt('b595_desk_notes.txt', L)


def components():
    S, fj, tj, wl, rl, H = (jl('b595_scores.json'), jl('b595_findings.json'), jl('b595_trail.json'), jl('b595_weight_line.json'),
                            jl('b595_rule_lines.json'), jl('b595_h33.json'))
    L = ['b595 -- THE COMPONENTS, BANKED UNDER (R205).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b594`s closing push-out relay %s ; push-b594* branches deleted by name '
         '(data/b595_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b595_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b594`s weight FINDINGS :%d ; the standing line OPEN_TRAILS :%d ; the :4787 search and the two history lines '
         '(data/b595_citation_4787.txt)' % (wl['line'], rl['lines'][0]['line']),
         '### COMPONENT 2 : TECHNE-Core %s (sha256 %s, %d nodes, body %d words outside the tables) and %s, each alone, not pushed ; H33a %s, '
         'H33b %s, H33c %s, H33d %s' % (DOC_REL, H['sha256'][:16], H['nodes'], H['body_words'], EXT_REL, S['H33a'][0], S['H33b'][0], S['H33c'][0], S['H33d'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b596 W-ORD-SIMPLICITY-FACE ; N1 %s, N2 %s, N3 %s, '
         'N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b595_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b595_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
