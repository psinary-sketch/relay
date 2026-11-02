# -*- coding: utf-8 -*-
"""standing/counterline.py -- v1.15.0, (R345)(2)(vii), b734 event (10): THE COUNTER IN THE HAND SECTION AND THE CLOSING. b734's hand section at OPEN_TRAILS :17273 reads CLOSE 31, REPEAT 16 of 33 and its
closing CLOSE 32, REPEAT 17 of 34, the event landing after the record's push. The rule: the hand section's figure is written after the last event, or it names the closing as the last figure.

  figure(text) -> (claim, close, repeat, total) or None     read(hand, closing) -> dict(hand, closing, equal, names_closing, ok)
"""
import re

FIG = re.compile(r'CLAIM (\d+), CLOSE (\d+)[;,] REPEAT (\d+) (?:of|OF) (\d+)')
NAMES = re.compile(r'closing (?:bank )?(?:carries|prints|reads|names) the last figure|the last figure (?:is|stands in) the closing', re.I)


def figure(text):
    m = FIG.search(text or '')
    return tuple(int(x) for x in m.groups()) if m else None


def read(hand, closing):
    h, c = figure(hand), figure(closing)
    nm = bool(NAMES.search(hand or ''))
    return dict(hand=h, closing=c, equal=h == c, names_closing=nm, ok=bool(c) and (h == c or nm))
