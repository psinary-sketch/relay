# -*- coding: utf-8 -*-
"""force_rm.py -- ### **THE SHARED REMOVAL, WITH THE READ-ONLY CURE `b314` ALREADY HAD.**

### ### **WHY THIS FILE EXISTS, IN ONE SENTENCE:** ### `b314` wrote the cure, kept it to itself, and
### `b433` reinvented it nineteen acts later -- so `(R46)` was ruled: ### **A CURE THAT LIVES IN A
### ### SINGLE TOOL IS NOT A GUARD.** ### This is that cure extracted, and nothing more.

### ### **THE HANDLER IS `b314`'S, QUOTED AT ITS OWN FILE AND LINE** -- `tools/b314_coldclone.py:47`:
###
###     def _force_rm(func, path, _exc):
###         \"\"\"### git objects arrive read-only on Windows; a plain `rmtree` refuses them.\"\"\"
###         os.chmod(path, stat.S_IWRITE)
###         func(path)
###
### ### **THREE THINGS ARE ADDED, AND EACH IS NAMED RATHER THAN SLIPPED IN.**
###
### ### **(1) IT STILL FAILS LOUDLY.** ### The handler defeats the READ-ONLY BIT and nothing else.
### A removal that fails for any other reason -- a held handle, a vanished mount, a permission the
### owner does not have -- ### **RAISES, AND THE RAISE IS THE WHOLE POINT.** ### A helper that
### swallowed everything would pass the read-only fixture and be worse than the bare call it replaced,
### and `self_test` exercises exactly that polarity.
###
### ### **(2) THE REMOVAL IS PROVED BY THE DIRECTORY'S OWN ABSENCE, NOT BY A RETURN.** ### `b434`
### minted the species ### **A TOOL ASKED NOT TO COMPLAIN REPORTS A SUCCESS IT DID NOT EARN**, whose
### cure is: ### **READ THE VERDICT FROM THE OBJECT.** ### `b433`'s incident was `ignore_errors=True`
### leaving thirty-six files behind and returning quietly. ### So this reads the object back.
###
### ### **(3) THE `onexc`/`onerror` SPLIT IS DECIDED BY READING THE SIGNATURE, NOT BY CATCHING
### ### `TypeError`.** ### `b433` detected it by calling with `onexc` and catching `TypeError` -- and
### ### **A `TypeError` RAISED INSIDE THE HANDLER IS INDISTINGUISHABLE FROM THE API MISMATCH**, so a
### genuine failure in the cure would have been read as an old interpreter and silently retried under
### the other name. ### That is the same species again, one layer down. ### The signature is read.
"""
import inspect
import io
import os
import shutil
import stat
import sys
import tempfile

MARK = '### force_rm (b435, from b314)'

# ### **READ THE SIGNATURE ONCE.** ### `onexc` is 3.12+; `onerror` is what older interpreters take.
_HAS_ONEXC = 'onexc' in inspect.signature(shutil.rmtree).parameters


class RemovalNotVerified(OSError):
    """### **RAISED WHEN A REMOVAL RETURNED AND THE TREE IS STILL THERE.**"""


def _onexc(func, path, exc):
    """### `b314`'s handler. ### git objects arrive read-only on Windows; `rmtree` refuses them."""
    if not os.path.exists(path):
        return                          # ### already gone -- nothing to force, and no error to hide
    try:
        os.chmod(path, stat.S_IWRITE)
    except OSError:
        raise exc                       # ### the ORIGINAL cause, not the cure's own failure
    func(path)                          # ### ### **IF IT FAILS AGAIN IT RAISES. THAT IS INTENDED.**


def rmtree(path, missing_ok=True):
    """### **REMOVE A TREE, DEFEAT THE READ-ONLY BIT, AND PROVE THE TREE IS GONE.**

    ### Returns `True` if it removed something, `False` if there was nothing there and `missing_ok`.
    ### ### **RAISES ON EVERY OTHER OUTCOME** -- including a removal that returned without removing.
    """
    if not os.path.exists(path):
        if missing_ok:
            return False
        raise FileNotFoundError(path)
    if _HAS_ONEXC:
        shutil.rmtree(path, onexc=_onexc)
    else:
        shutil.rmtree(path, onerror=lambda f, p, e: _onexc(f, p, e[1]))
    verify_absent(path)
    return True


def verify_absent(path):
    """### **THE OBJECT'S OWN ANSWER, WHICH IS THE ONLY ONE WORTH READING.**"""
    if os.path.exists(path):
        raise RemovalNotVerified(
            'removal returned but the tree is still present : %s' % path)
    return True


# ----------------------------------------------------------------------------------------------
# ### **THE FIXTURES. ### BOTH POLARITIES, AND A CONTROL ON THE FIRST.**
# ----------------------------------------------------------------------------------------------
def _readonly_tree(root):
    """### Build a tree whose files carry the bit git leaves on its objects."""
    sub = os.path.join(root, 'objects', 'ab')
    os.makedirs(sub)
    for name in ('blob1', 'blob2'):
        p = os.path.join(sub, name)
        io.open(p, 'w', encoding='utf-8').write('x')
        os.chmod(p, stat.S_IREAD)
    return sub


def self_test(verbose=True):
    lines = []
    ok = True

    def say(label, good):
        nonlocal ok
        ok = ok and good
        lines.append('    %-58s %s' % (label, 'ok' if good else '### FAILED'))

    # ### (a) THE CONTROL FIRST. ### **A FIXTURE THAT PASSES WITHOUT THE CURE TESTS NOTHING**, so the
    # ### act first proves the bare call REFUSES this tree. ### On a filesystem that ignores the
    # ### read-only bit the control will not refuse -- and then it is REPORTED AS NOT APPLICABLE,
    # ### never counted as a pass.
    base = tempfile.mkdtemp(prefix='force_rm_fix_')
    try:
        t = os.path.join(base, 'control')
        os.makedirs(t)
        _readonly_tree(t)
        bare_refused = False
        try:
            shutil.rmtree(t)
        except OSError:
            bare_refused = True
        if bare_refused:
            say('### **CONTROL: the bare `rmtree` REFUSES a read-only tree**', True)
        else:
            lines.append('    %-58s %s' % (
                '### CONTROL: this filesystem ignores the read-only bit',
                '### NOT APPLICABLE -- NOT COUNTED AS A PASS'))
        shutil.rmtree(t, ignore_errors=True)

        # ### (b) POLARITY ONE: THE READ-ONLY TREE IS REMOVED.
        t = os.path.join(base, 'positive')
        os.makedirs(t)
        _readonly_tree(t)
        removed = rmtree(t)
        say('a read-only tree is removed, and the tree is gone',
            removed and not os.path.exists(t))

        # ### (c) POLARITY TWO: ### **A GENUINE FAILURE STILL FAILS LOUDLY.**
        # ### A file held open cannot be unlinked on Windows and `chmod` does not help -- which is
        # ### exactly the case that must NOT be swallowed.
        t = os.path.join(base, 'negative')
        os.makedirs(t)
        p = os.path.join(t, 'held')
        fh = io.open(p, 'w', encoding='utf-8')
        fh.write('x')
        fh.flush()
        raised = None
        try:
            rmtree(t)
        except Exception as e:                                   # noqa: BLE001
            raised = e
        fh.close()
        if raised is not None:
            say('### **a genuine failure still RAISES (%s)**' % type(raised).__name__, True)
        elif sys.platform.startswith('win'):
            say('### **a genuine failure still RAISES**', False)
        else:
            lines.append('    %-58s %s' % (
                '### a held handle is removable on this platform',
                '### NOT APPLICABLE -- NOT COUNTED AS A PASS'))
        shutil.rmtree(t, ignore_errors=True)

        # ### (d) THE VERIFICATION ARM ITSELF: a path that is still there is REFUSED.
        t = os.path.join(base, 'still_here')
        os.makedirs(t)
        refused = False
        try:
            verify_absent(t)
        except RemovalNotVerified:
            refused = True
        say('### **a removal that left the tree standing is REFUSED**', refused)

        # ### (e) A MISSING PATH IS NOT AN ERROR, AND SAYS SO BY ITS RETURN.
        gone = os.path.join(base, 'never_existed')
        say('a missing path returns False and does not raise', rmtree(gone) is False)
        strict = False
        try:
            rmtree(gone, missing_ok=False)
        except FileNotFoundError:
            strict = True
        say('and refuses when the caller asked for strict', strict)
    finally:
        shutil.rmtree(base, ignore_errors=True)

    if verbose:
        print('%s -- FIXTURES, BOTH POLARITIES' % MARK)
        for ln in lines:
            print(ln)
        print('    ### ### **VERDICT : %s**' % ('HELD' if ok else 'NOT HELD'))
    return ok, lines


if __name__ == '__main__':
    good, _ = self_test(True)
    sys.exit(0 if good else 1)
