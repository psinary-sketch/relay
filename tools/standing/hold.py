# -*- coding: utf-8 -*-
"""standing/hold.py -- v1.25.0, (R355)(2)(ii), b744 events (3), THE TOOLS' [CLAIM ; NEW]: THE HOLD AT THE ROOT. b744's `record root_arm` ran with the
host's free memory at 2,360 MB, beneath the 2,560 MB hold the suite parts refuse themselves under (checks.tpl main, (R294)(2)); the record tool's
dispatch called every route with no reading. The hold now binds every record route as it binds the suite parts: the rendered record tool asks
refuses() before it calls any route, the route refusing itself and printing the figure (exit 3).

  refuses(route, hold=None, free=None) -> True when the host's free memory is beneath the hold (printed); the hold read from data/act_current.json
"""
import json
import os
import sys
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)


def hold_mb():
    with open(os.path.join(RELAY, 'data', 'act_current.json'), encoding='utf-8') as f:
        return int(json.load(f).get('hold_mb') or 2560)


def free_mb():
    if T not in sys.path:
        sys.path.insert(0, T)
    import b703_checks as C3
    return C3.free_mb()


def refuses(route, hold=None, free=None):
    h = hold_mb() if hold is None else hold
    fm = free_mb() if free is None else free
    if fm < h:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: %s NOT RUN ((R355)(2)(ii))' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fm, h, route))
        return True
    return False
