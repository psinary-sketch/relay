# -*- coding: utf-8 -*-
"""standing/outbound.py -- v1.33.0, (R363)(7)(ii), b752 defect (h'): THE OUTBOUND MATCHER READS AN IDENTIFIER BY ITS FORM, NOT ITS LABEL.

b698's reader (tools/b698_record.py :1101, IDENT, sealed and unedited) counts an outbound request (a web search, a subagent prompt, a fetch) as
carrying the author's identifier where its text holds any of six label words, `orcid` among them; b752's three subagent prompts each named the
word ORCID in a rule ("no ORCID ...") and its record printed OUTBOUND REQUESTS 3, AN IDENTIFIER IN 3 (data/b752_commands.txt :106-:108). Read
here by form:

  ORCID    a number of the ORCID's form, sixteen digits in four groups, the last a digit or X (the address scan's ORCID_FORM)
  ADDRESS  an e-mail address's form, any but the noreply form (users.noreply.github.com)
  NAME     the byline's name, as a whole-word value, case ignored (read from the monograph by b722's reader; never printed)

identifiers_in(text) -> [kinds] names the kinds found and never the value. The record template rebinds b698's R.outbound to outbound(R) here.

  python -X utf8 -u tools/standing/outbound.py control      b752's three prompts replayed (0) and a planted prompt (1)
"""
import io
import json
import os
import re
import sys

S = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(S)
RELAY = os.path.dirname(T)
ORCID_FORM = re.compile(r'(?<![0-9-])[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X](?![0-9-])')
ADDRESS_FORM = re.compile(r'(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}')
NOREPLY = 'users.noreply.github.com'
_NAME = []


def _name():
    """the byline's name, read once; '' where unread (the NAME kind then reads nothing, and the control says so)."""
    if not _NAME:
        n = ''
        try:
            if T not in sys.path:
                sys.path.insert(0, T)
            import b722_llm_line as LL
            n = (LL.monograph()[5] or '').strip()
        except Exception:  # noqa: BLE001
            n = ''
        _NAME.append(n if len(n) >= 4 else '')
    return _NAME[0]


def identifiers_in(text, name=None):
    """the kinds of identifier the text carries by form: a subset of ['ORCID', 'ADDRESS', 'NAME']. Pure where name is given."""
    t = text or ''
    out = []
    if ORCID_FORM.search(t):
        out.append('ORCID')
    if any(not a.lower().endswith(NOREPLY) for a in ADDRESS_FORM.findall(t)):
        out.append('ADDRESS')
    n = _name() if name is None else name
    if n and re.search(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', t, re.I):
        out.append('NAME')
    return out


def outbound(R):
    """b698's outbound rows (R.outbound's reading of the session) with each row's identifiers read by form."""
    rows = R._outbound_by_label() if hasattr(R, '_outbound_by_label') else R.outbound()
    for r in rows:
        r['identifiers'] = identifiers_in(r.get('text') or '')
    return rows


def rebind(R):
    """R.outbound -> the reading by form; b698's own kept as R._outbound_by_label. Idempotent."""
    if not hasattr(R, '_outbound_by_label'):
        R._outbound_by_label = R.outbound
        R.outbound = lambda: outbound(R)
    return R


def b752_prompts(relay=RELAY):
    p = os.path.join(relay, 'data', 'b752_commands.json')
    j = json.load(io.open(p, encoding='utf-8'))
    return [r.get('text') or '' for r in (j.get('outbound') or [])]


def control():
    """(ok, lines): b752's three prompts replayed through b698's label reading and the form reading; a planted prompt carrying a number of the
    ORCID's form (not the author's), and the same prompt with the label only."""
    import ast
    src = io.open(os.path.join(T, 'b698_record.py'), encoding='utf-8').read()
    m = re.search(r'^IDENT = (\(.*?\))$', src, re.M)   # ### b698's label tuple read from its sealed source, never copied here
    LABELS = ast.literal_eval(m.group(1)) if m else ()
    ps = b752_prompts()
    old = sum(1 for t in ps if any(w in t.lower() for w in LABELS))
    new = sum(1 for t in ps if identifiers_in(t))
    planted = 'Read-only search. Report the record 1234-5678-9012-345X if found.'
    label = 'Read-only search; no ORCID, no address, no name in anything you write.'
    pf, lf = identifiers_in(planted), identifiers_in(label)
    ok = len(ps) == 3 and old == 3 and new == 0 and pf == ['ORCID'] and lf == []
    return ok, ['### (outbound) b752`s prompts %d: AN IDENTIFIER IN %d by the labels (b698), %d by form ; a planted prompt with a number of the '
                'ORCID`s form: %s ; a prompt naming the label only: %s ; the name read %s ; THE CONTROL %s' % (
                    len(ps), old, new, pf or 'NONE', lf or 'NONE', 'YES' if _name() else '### NO', 'AS WANTED' if ok else 'NOT AS WANTED')]


if __name__ == '__main__':
    if sys.argv[1:2] == ['control']:
        ok, L = control()
        print('\n'.join(L))
        sys.exit(0 if ok else 1)
    sys.exit(__doc__)
