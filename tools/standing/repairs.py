# -*- coding: utf-8 -*-
"""standing/repairs.py -- EVERY CHANGE BY DIFF ((R325)(3) of the toolset act): the extraction of the core, each standing function against
the function it was copied from, as a unified diff; a standing file with no source, whole as an addition; and the act's edits to its own
carried tools and to the hook's settings, as git and file diffs. Banked as data/<act>_tool_repairs.txt.

THE PROVENANCE TABLE (prose, read by this tool; each row: the standing file and function | the source file and function, or a line
range, or * for the whole file):
  PAIR hook.py *                      | tools/b714_hook.py *
  PAIR act.py root_named              | tools/b698_record.py root_banks
  PAIR act.py sha256_file             | tools/act_root.py sha256_file
  PAIR act.py jl                      | tools/b714_components_standin.py jl
  PAIR close.py head_line             | tools/b714_closing.py head_line
  PAIR close.py combine_tally         | tools/b714_checks.py _combine_tally
  PAIR close.py neg_shown             | tools/b714_checks.py neg_shown
  PAIR close.py withheld_entries      | tools/b714_checks.py :1758-:1763
  PAIR close.py seal_record           | tools/b714_checks.py seal
  PAIR close.py read_defect_row       | tools/b703_record.py read_defect_row
  PAIR close.py letters_of            | tools/b714_record.py letters_of
  PAIR components.py composed         | tools/b714_components_standin.py lines
  PAIR components.py files_of         | tools/b714_components_standin.py files_of
  PAIR components.py banks_of         | tools/b714_components_standin.py banks_of
  PAIR arms.py prev_longest           | tools/rule_arms.py :305-:307
  PAIR scan.py split                  | tools/b703_checks.py strip_prose
  PAIR scan.py DELETE_WORDS           | tools/b703_checks.py :1334-:1339

  python -X utf8 tools/standing/repairs.py          prints the foot; writes nothing
  python -X utf8 tools/standing/repairs.py bank     writes data/<act>_tool_repairs.txt
"""
import ast
import difflib
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import act as A   # noqa: E402

S = os.path.dirname(os.path.abspath(__file__))
NL = '\n'
PAIR = re.compile(r'^\s*PAIR (\S+) (\S+)\s+\| (\S+) (\S+)\s*$', re.M)
SETTINGS = 'D:/.claude/settings.json'


def segment(text, name):
    """a function's source, or a top-level assignment's, by its name; a line range ':a-:b'; '*' the whole text."""
    if name == '*':
        return text
    m = re.match(r'^:(\d+)-:(\d+)$', name)
    if m:
        L = text.split(NL)
        return NL.join(L[int(m.group(1)) - 1:int(m.group(2))])
    tree = ast.parse(text)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return ast.get_source_segment(text, node)
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.get_source_segment(text, node)
    return None


def pairs():
    doc = ast.get_docstring(ast.parse(A.rd_path(os.path.abspath(__file__)))) or ''
    return PAIR.findall(doc)


def lines():
    cur = A.current()
    act = cur['act']
    ver = A.rd_path(os.path.join(S, 'VERSION')).strip()
    L = ['%s -- THE TOOL REPAIRS, EVERY CHANGE BY DIFF: THE STANDING TOOLSET AT %s AND THE ACT`S EDITS (%s)' % (
        act, ver, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### sections: (A) each standing function against its source, unified diff (--- the source, +++ the standing copy); (B) the standing',
         '### files with no source, whole as additions; (C) the act`s edits to its carried tools (git diff against HEAD) and to the hook`s settings.',
         '### Written by tools/standing/repairs.py from its provenance table.', '']
    L.append('## (A) THE EXTRACTION')
    covered, n_pairs, missing = set(), 0, []
    for sf, sname, src, sfunc in pairs():
        n_pairs += 1
        st = A.rd_path(os.path.join(S, sf))
        so = A.rd_path(os.path.join(A.RELAY, *src.split('/')))
        a, b = segment(so, sfunc) if so else None, segment(st, sname)
        covered.add(sf)
        if a is None or b is None:
            missing.append('%s %s | %s %s' % (sf, sname, src, sfunc))
            L += ['', '### PAIR tools/standing/%s %s <- %s %s : ### NOT FOUND (%s)' % (sf, sname, src, sfunc,
                                                                                       'the source' if a is None else 'the copy')]
            continue
        d = list(difflib.unified_diff(a.split(NL), b.split(NL), '%s %s' % (src, sfunc), 'tools/standing/%s %s' % (sf, sname), lineterm='', n=1))
        L += ['', '### PAIR tools/standing/%s %s <- %s %s : source %d lines, copy %d lines, diff %d lines%s' % (
            sf, sname, src, sfunc, a.count(NL) + 1, b.count(NL) + 1, len(d), ' (UNCHANGED)' if not d else '')] + d
    L += ['', '## (B) THE STANDING FILES WITHOUT A SOURCE PAIR, WHOLE AS ADDITIONS (their text is the file in tools/standing/)']
    for f in sorted(os.listdir(S)):
        if f.endswith('.py') or f == 'VERSION':
            t = A.rd_path(os.path.join(S, f))
            L.append('  tools/standing/%-16s +%d lines, sha256 %s%s' % (f, t.count(NL), A.sha256_file(os.path.join(S, f)),
                                                                        '' if f not in covered else ' (its paired functions in (A); the rest added)'))
    base = A.step_commit(act, 'step zero')
    L += ['', '## (C) THE ACT`S EDITS TO ITS CARRIED TOOLS SINCE THE CARRY (git diff from the act`s last step-zero commit %s to the working tree, '
          'tools/<act>_*.py and the shared tools act_current.json`s shared_edits names) AND TO THE HOOK`S SETTINGS' % (base or '-')[:8]]
    shared = A.current().get('shared_edits', [])
    out = (A.gs('relay', 'diff', base, '--', 'tools/%s_*.py' % act, *shared) or '') if base else ''
    L += (out.split(NL) if out else ['  none'])
    L += ['', '### the hook`s settings %s, read now: the hook`s command line' % SETTINGS]
    L += ['  ' + l.strip() for l in A.rd_path(SETTINGS).split(NL) if 'hook' in l and '.py' in l]
    L += ['', '### ### **PAIRS %d ; NOT FOUND %d %s ; STANDING FILES %d ; THE ACT`S CARRIED TOOLS EDITED %d.**' % (
        n_pairs, len(missing), missing or '', len([f for f in os.listdir(S) if f.endswith('.py') or f == 'VERSION']),
        len(re.findall(r'^diff --git', out, re.M)))]
    return L, act, not missing


def main(route):
    L, act, ok = lines()
    if route == 'bank':
        p = os.path.join(A.D, '%s_tool_repairs.txt' % act)
        with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(NL.join(L) + NL)
        os.replace(p + '.tmp', p)
        print('bank', p)
    print(L[-1])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'dry'))
