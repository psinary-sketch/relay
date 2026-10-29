# -*- coding: utf-8 -*-
"""standing/fold.py -- THE SEVEN CLOSE TOOLS AS ONE STANDING MODULE TAKING THE ACT ((R333)(2)(i), v1.3.0, on the author's word: Option 2).
Written whole at b723 by the Write tool.

The seven tools (checks, citation, closing, record, reg_gate, regspec, report) are one template each, tools/standing/fold/<tool>.tpl, the
lines every act shares, its act names as tokens (the act ⟪ACT⟫, the act before ⟪PREV⟫, the act's ruling ⟪RUL⟫, the ruling before ⟪PRUL⟫)
and its act's own lines as slots (⟪SLOT n⟫). An act's tool is the template rendered with that act's names and its slots filled from the
act's arms module, the sections file data/act_current.json names (`sections`, else tools/acts/<act>.py). The names are read from
data/act_current.json for the act and the act before it, and from its `replay` rows for an act before those; no act's figure stands here.

  load(act, tool)    the act's tool as a module, registered as <act>_<tool>; every name the tool reads from the act's worklist (the alias
                     its `import <act>_worklist as X` binds) checked against that worklist first, a missing name refusing the load
  install()          the import finder: an import of <act>_<tool> for an act with a sections file is that act's folded tool; such an act's
                     own other tools (its worklist, its carry, its components' tools) are its files; every other act-numbered import must
                     be named in tools/standing/legacy.py (the act-numbered predecessor modules, the stated exception to
                     tools/standing/act.py's rule), or it is refused
  render(act, tool)  the act's tool as text

  python -X utf8 tools/standing/fold.py <tool> [args...] [--act bNNN]
                     runs the act's tool as `python tools/<act>_<tool>.py args...` runs it (its own __main__, tools/ first on the path),
                     the act from data/act_current.json unless --act names one
"""
import importlib.abc
import importlib.util
import json
import linecache
import os
import re
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.dirname(HERE)
ROOT = os.path.dirname(TOOLS_DIR)
TPL_DIR = os.path.join(HERE, 'fold')
TOOLS = ('checks', 'citation', 'closing', 'record', 'reg_gate', 'regspec', 'report')
ACT_NAME = re.compile(r'^b\d{3}_\w+$')
SLOT = re.compile(r'(?m)^⟪SLOT (\d+)⟫\n')
SECTION = re.compile(r'(?m)^#⟪(SECTION|OVERRIDE) (\w+) (\d+)(?: (\d+))?( NOEOL)?(?: REPAIR ([\w()]+))?⟫\n')
END = '#⟪END⟫\n'


class FoldRefused(ImportError):
    pass


def _rd(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8')


def act_current():
    with open(os.path.join(ROOT, 'data', 'act_current.json'), encoding='utf-8') as f:
        return json.load(f)


def names(act):
    """the act's four names: ACT, PREV, RUL, PRUL -- from data/act_current.json for its act and the act before, else its replay rows."""
    ac = act_current()
    prev = 'b%d' % (int(act[1:]) - 1)
    if act == ac['act']:
        rul, prul = ac['ruling'], ac['prev_ruling']
    else:
        rp = ac.get('replay', {})
        if act not in rp or prev not in rp:
            raise FoldRefused('fold: %s or %s has no ruling in data/act_current.json (act or replay rows)' % (act, prev))
        rul, prul = rp[act]['ruling'], rp[prev]['ruling']
    return {'⟪ACT⟫': act, '⟪PREV⟫': prev, '⟪RUL⟫': rul, '⟪PRUL⟫': prul}


def sections_path(act):
    """the act's arms module: data/act_current.json's `sections` for its act, else tools/acts/<act>.py -- in a directory of its own, so
    no worklist's SEALED (os.listdir of tools/, every tools/<act>_*.py) takes it in."""
    ac = act_current()
    if act == ac['act'] and ac.get('sections'):
        return os.path.join(ROOT, *ac['sections'].split('/'))
    return os.path.join(TOOLS_DIR, 'acts', '%s.py' % act)


def has_sections(act):
    return os.path.isfile(sections_path(act))


def _parse(act):
    """(sections {(tool, n): text}, overrides {tool: [(first, last, text)]}) -- each the lines from its marker line to the next line
    "#⟪END⟫" (no source carries the mark, so the end cannot be mistaken; a marker ending " NOEOL" means the text's last line has no newline,
    the one written before the end line dropped). A SECTION fills the template's slot n; an OVERRIDE is the act's own lines in place of the
    template's lines first..last (1-based, inclusive; last = first - 1 inserts before first), the way an act changes a line every earlier
    act shares without changing their renders: the template stays, the act's module carries the change. Edited by the Edit tool."""
    t = _rd(sections_path(act))
    secs, ovs, i = {}, {}, 0
    while True:
        m = SECTION.search(t, i)
        if not m:
            break
        e = t.find(END, m.end())
        if e < 0 or (e > m.end() and t[e - 1] != '\n'):
            raise FoldRefused('fold: %s module: %s %s %s has no end line' % (act, m.group(1), m.group(2), m.group(3)))
        text = t[m.end():e]
        if m.group(5):
            text = text[:-1]
        if m.group(1) == 'SECTION':
            secs[(m.group(2), int(m.group(3)))] = text
        else:
            ovs.setdefault(m.group(2), []).append((int(m.group(3)), int(m.group(4)), text))
            if m.group(6):
                REPAIRS.setdefault(act, {})[(m.group(2), int(m.group(3)))] = m.group(6)
        i = e + len(END)
    return secs, ovs


REPAIRS = {}   # ### {act: {(tool, first): repair}} -- an OVERRIDE marked " REPAIR <name>": the act's named repair of a shared line


def sections(act):
    return _parse(act)[0]


def overrides(act):
    return _parse(act)[1]


def render(act, tool, secs=None, ovs=None):
    tpl = _rd(os.path.join(TPL_DIR, tool + '.tpl')).splitlines(keepends=True)
    nm = names(act)
    if secs is None or ovs is None:
        s0, o0 = _parse(act)
        secs = s0 if secs is None else secs
        ovs = o0 if ovs is None else ovs
    at = {}
    for first, last, text in ovs.get(tool, []):
        if first < 1 or last < first - 1 or last > len(tpl) or first in at:
            raise FoldRefused('fold: %s override %s %d-%d out of the template (%d lines) or overlapping' % (act, tool, first, last, len(tpl)))
        if any(SLOT.match(tpl[j]) for j in range(first - 1, last)):
            raise FoldRefused('fold: %s override %s %d-%d covers a slot line' % (act, tool, first, last))
        at[first] = (last, text)
    out, i = [], 0
    while i < len(tpl):
        if i + 1 in at:
            last, text = at.pop(i + 1)
            out.append(text)
            if last >= i + 1:
                i = last
                continue
        l = tpl[i]
        m = SLOT.match(l)
        if m:
            k = (tool, int(m.group(1)))
            if k not in secs:
                raise FoldRefused('fold: %s has no section %s %s' % (act, tool, m.group(1)))
            out.append(secs[k])
        else:
            for tok, v in nm.items():
                l = l.replace(tok, v)
            out.append(l)
        i += 1
    if at:
        raise FoldRefused('fold: %s override(s) %s not reached' % (act, sorted(at)))
    return ''.join(out)


def worklist_names(act, text):
    """(alias, the names the text reads through the alias bound to <act>_worklist)."""
    m = re.search(r'(?m)^import %s_worklist as (\w+)' % act, text)
    if not m:
        return None, set()
    return m.group(1), set(re.findall(r'(?<![\w.])%s\.([A-Za-z_]\w*)' % m.group(1), text))


DEAD = re.compile(r'(?m)^#⟪DEAD (\w+) ([\w,]*)⟫$')


def dead(act):
    """{tool: set} -- the names the act's tool reads through its worklist alias on a route the act never runs, its worklist lacking them,
    each declared in the sections file by a line "#⟪DEAD <tool> <name,...>⟫": a missing name so declared is printed, not refused."""
    p = sections_path(act)
    if not os.path.isfile(p):
        return {}
    return dict((m.group(1), set(x for x in m.group(2).split(',') if x)) for m in DEAD.finditer(_rd(p)))


PENDING = re.compile(r'(?m)^#⟪PENDING (\w+) ([\w,]*)⟫$')


def pending(act):
    """{tool: set} -- the names the act's tool reads on routes the act has still to write for itself (carried from the act before, its
    worklist not yet carrying them): each printed on stderr at every load, never silent; the act's suite holds the set empty at its seal."""
    p = sections_path(act)
    if not os.path.isfile(p):
        return {}
    return dict((m.group(1), set(x for x in m.group(2).split(',') if x)) for m in PENDING.finditer(_rd(p)))


def missing_names(act, text, worklist=None):
    alias, used = worklist_names(act, text)
    if alias is None:
        return None, set(), set()
    wl = worklist if worklist is not None else importlib.import_module('%s_worklist' % act)
    return alias, used, set(n for n in used if not hasattr(wl, n))


def check_names(act, tool, text, worklist=None):
    """the names read through the act's worklist alias, each in its worklist or declared dead; an undeclared missing name refuses."""
    alias, used, missing = missing_names(act, text, worklist)
    pend = sorted(missing & pending(act).get(tool, set()))
    bad = sorted(missing - dead(act).get(tool, set()) - set(pend))
    if bad:
        raise FoldRefused('fold: %s_%s reads %d name(s) its worklist lacks, not declared dead or pending: %s' % (act, tool, len(bad), ', '.join(bad)))
    if pend:
        sys.stderr.write('### fold: %s_%s PENDING %d (routes the act has still to write; a call on one fails): %s\n' % (act, tool, len(pend), ', '.join(pend)))
    return sorted(used)


def _code(act, tool, text):
    fn = os.path.join(TOOLS_DIR, '%s_%s.py' % (act, tool))   # ### the path the tool had as a file: its own ROOT reads resolve as before
    linecache.cache[fn] = (len(text), None, text.splitlines(keepends=True), fn)
    return fn, compile(text, fn, 'exec')


def load(act, tool, worklist=None, name=None):
    text = render(act, tool)
    check_names(act, tool, text, worklist)
    fn, code = _code(act, tool, text)
    name = name or '%s_%s' % (act, tool)
    mod = types.ModuleType(name)
    mod.__file__ = fn
    mod.__fold__ = (act, tool)
    if name != '__main__':
        sys.modules[name] = mod
    try:
        exec(code, mod.__dict__)
    except BaseException:
        if name != '__main__':
            sys.modules.pop(name, None)
        raise
    return mod


def legacy():
    import legacy as L
    return set(L.NAMES)


class Finder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path=None, target=None):
        if '.' in fullname or not ACT_NAME.match(fullname):
            return None
        act, tool = fullname[:4], fullname[5:]
        if tool in TOOLS and has_sections(act):
            return importlib.util.spec_from_loader(fullname, self)
        if has_sections(act) and tool not in TOOLS and os.path.isfile(os.path.join(TOOLS_DIR, fullname + '.py')):
            return None                     # ### a folded act's own tool beside the seven (its worklist, its carry, its components)
        if fullname in legacy():
            return None
        raise FoldRefused('fold: %s is act-numbered, neither a folded tool nor named in tools/standing/legacy.py -- refused' % fullname)

    def create_module(self, spec):
        return None

    def exec_module(self, mod):
        act, tool = mod.__name__[:4], mod.__name__[5:]
        text = render(act, tool)
        check_names(act, tool, text)
        fn, code = _code(act, tool, text)
        mod.__file__ = fn
        mod.__fold__ = (act, tool)
        exec(code, mod.__dict__)


FINDER = Finder()


def install():
    if HERE not in sys.path:
        sys.path.append(HERE)               # ### legacy.py, read by name
    if TOOLS_DIR not in sys.path:
        sys.path.insert(0, TOOLS_DIR)
    if FINDER not in sys.meta_path:
        sys.meta_path.insert(0, FINDER)


def main(argv):
    act = None
    if '--act' in argv:
        i = argv.index('--act')
        act = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    if not argv or argv[0] not in TOOLS:
        sys.exit('usage: fold.py <%s> [args...] [--act bNNN]' % '|'.join(TOOLS))
    act = act or act_current()['act']
    tool = argv[0]
    sys.path[0] = TOOLS_DIR                 # ### as `python tools/<act>_<tool>.py` sets it
    install()
    sys.argv = [os.path.join(TOOLS_DIR, '%s_%s.py' % (act, tool))] + argv[1:]
    main_mod = sys.modules['__main__']
    text = render(act, tool)
    check_names(act, tool, text)
    fn, code = _code(act, tool, text)
    g = {'__name__': '__main__', '__file__': fn, '__builtins__': __builtins__, '__doc__': None, '__package__': None,
         '__spec__': None, '__loader__': None, '__fold__': (act, tool)}
    main_mod.__dict__.clear()
    main_mod.__dict__.update(g)
    exec(code, main_mod.__dict__)


if __name__ == '__main__':
    import fold as _F                       # ### the loader as its own module: the tool's run takes over __main__'s namespace
    _F.main(sys.argv[1:])
