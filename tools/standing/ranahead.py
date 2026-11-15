# -*- coding: utf-8 -*-
"""standing/ranahead.py -- v1.35.2, (R366)(6), the carried fault (10) of relay data/b755_carried_faults.txt (8 acts by data/b756_faults.txt:
b698, b706, b711, b712, b714, b716, b727, b754): G-NOTHING-RAN-AHEAD FAILED NAMING NOTHING. The arm (checks.tpl nothing_ahead_ok, :1306-:1325)
is a bool over every commit at or before the lock, and its failing reading printed no commit: b754's closing message carried it "open" with
no commit named, and no bank of b754 says which commit was undeclared. Here the same clauses, in the same order, return what failed: None
where the arm fails before any commit is read (the face carries no section (0), no lock time, or no `gate` row), else the commits at or
before the lock that are neither the gate's, nor stepped after the face's first commit, nor declared on the face by their hash. The arm
itself is unchanged; the suite prints this beside it.

  undeclared(face, lock_epoch, logs, steps, face_first=None) -> None | [(hash8, subject)]
"""


def undeclared(face, lock_epoch, logs, steps, face_first=None):
    AC = __import__('act_close')
    FF = __import__('standing.faceform', fromlist=['declared'])
    gates = AC.step_commits(steps, phase='gate')
    if 'WHAT RAN AHEAD OF THIS SEAL' not in (face or '') or lock_epoch is None or not gates:
        return None
    stepped = AC.step_commits(steps)
    fe = [t for h, s, t in logs if face_first and (h.startswith(face_first[:7]) or face_first.startswith(h[:7]))]
    fe = min(fe) if fe else None
    return [(h[:8], s) for h, s, t in logs if t <= lock_epoch and not any(gc.startswith(h[:7]) for gc in gates)
            and not (fe is not None and t >= fe and any(c.startswith(h[:7]) for c in stepped)) and not FF.declared(h, face)]


def line(S, face_first):
    """the suite's detail line beside the arm."""
    try:
        u = undeclared(S.get('face'), S.get('lock_epoch'), (S.get('rlog') or []) + (S.get('plog') or []), S.get('steps') or [], face_first)
    except Exception as e:  # noqa: BLE001
        return '  ### G-NOTHING-RAN-AHEAD`s reading (v1.35.2, (R366)(6), carried (10)): RAISED %s: %s' % (type(e).__name__, e)
    if u is None:
        return ('  ### G-NOTHING-RAN-AHEAD`s reading (v1.35.2, (R366)(6), carried (10)): no commit read -- the face`s section (0) %s ; the lock '
                'time %s ; the step bank`s `gate` rows %d' % ('present' if 'WHAT RAN AHEAD OF THIS SEAL' in (S.get('face') or '') else 'ABSENT',
                                                           S.get('lock_epoch'), len(__import__('act_close').step_commits(S.get('steps') or [], phase='gate'))))
    return '  ### G-NOTHING-RAN-AHEAD`s reading (v1.35.2, (R366)(6), carried (10)): commits at or before the lock undeclared on the face %d%s' % (
        len(u), (': ' + '; '.join('%s %s' % (h, s[:60]) for h, s in u)) if u else ' (NONE)')
