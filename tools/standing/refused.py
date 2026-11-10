# -*- coding: utf-8 -*-
"""standing/refused.py -- v1.32.0, (R362)(7)(ii), b751 events (1): THE ARM THAT READ A REFUSED CALL. G-RULE-REMOTE-REREAD (tools/rule_arms.py)
read every shell call of the act's transcript, a call the PreToolUse hook refused before it ran included: b751's PowerShell call of
2026-11-10T17:54:13.904Z carried three ls-remote reads, the hook refused it (REFUSED REMOTE) and nothing ran, and the arm read it as a call naming
more than one repository and failed. The arm reads the calls that ran; a refused call is counted apart and printed. tools/rule_arms.py stands
outside the act's (W) list, so the repair stands here and the suite's checks render (tools/standing/fold/checks.tpl) reads the arm through it.

A refused call is known by its result alone: the hook's error text, "PreToolUse:<Tool> hook error: REFUSED <CLASS>: ..." (with "Error: " before
it in the result's mirror), the form tools/standing/hook.py prints for every refusal.

  is_refused(call) -> bool        reading(RA, R) -> (ok, rows read, rows failing, note) for ARM over the calls that ran, the refused printed
"""
import re

ARM = 'G-RULE-REMOTE-REREAD'
HOOK_REFUSED = re.compile(r'^(?:Error: )?PreToolUse:\w+ hook error: REFUSED\b')


def is_refused(c):
    return bool(HOOK_REFUSED.match((c or {}).get('out') or ''))


def refused_remote(calls):
    """the times of the ls-remote calls the hook refused before they ran."""
    return [c.get('ts') for c in calls or [] if 'ls-remote' in (c.get('cmd') or '') and is_refused(c)]


def reading(RA, R):
    """the arm's own reading (tools/rule_arms.py reading) over the calls that ran, the refused ls-remote calls printed apart."""
    calls = list(R.get('calls') or [])
    ref = refused_remote(calls)
    ok, n, bad, note = RA.reading(ARM, dict(R, calls=[c for c in calls if not is_refused(c)]))
    return ok, n, bad, note + ' ; refused by the hook before they ran, counted apart %d %s' % (len(ref), ref or 'NONE')
