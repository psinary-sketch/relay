# -*- coding: utf-8 -*-
"""b327_bridge_pairs.py -- THE LIVE ROW'S PAIRS, READ FROM `data/b327_bridge.json`. ### DATA, NOT A WRITER.

### ### **THE VERDICT WORDS IN THESE PAIRS ARE THE ONES `b327_bridge.py` DECIDED BY THE REGISTERED BARS**,
### read from its JSON record; nothing here is typed from memory of the run.
"""
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = os.path.join(ROOT, 'data', 'b327_bridge.json')

_rec = json.load(io.open(J, encoding='utf-8'))
PAIRS = {}
for k, (kind, text, quotes) in _rec['pairs'].items():
    a, b = k.split('|')
    PAIRS[(a, b)] = (kind, text, [(q[0], q[1], bool(q[2])) for q in quotes])
