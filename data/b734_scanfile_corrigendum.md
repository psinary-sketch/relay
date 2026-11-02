
## Corrigendum to b733’s record (relay data/b733_events.txt rows (1)-(11) and data/b733_defects.txt): eleven events and eighteen defects, each CLAIM or CLOSE and NEW or REPEAT; the probe-bank class at its head, the lock gate refusing to lock over a tracked probe output; the prompt’s ceiling a dry score, GIT_WRITE on the command, one date source, subjects from the bank, the retired print removed, the empty read its own word, clauses from the ruling, defect ids from the log, at tools/standing/ v1.14.0, each controlled, under (R344)(1)-(2)

*b733’s events bank (relay data/b733_events.txt) carries eleven rows, entered after its lock and not lettered, each tagged in its own bracket (9 the seat’s, 1 the score, 1 the author’s word); its defects bank eighteen lettered rows, (a)-(r), each tagged in its own bracket (18 the seat’s); its refusal bank twelve lines at 05d53af9, nine recorded by a row, the last three by none and entered below. Each item is tagged CLAIM, where it touches a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches the close’s own record of itself; and NEW or REPEAT with the act and letter of its class. The tags are the banks’ own; this entry edits none of them.*

**The repairs of `(R344)`(2), at tools/standing/ v1.14.0, each with a control on b733’s banks, failing on the route before the repair and passing after, both instances printed; a case with no failing side printed as a guard** (relay data/b734_standing_v1140.txt, 25 cases, AS WANTED 25):

**(probes) the probe-bank class at its head (`(R344)`(2)(i), event (11); CLAIM ; REPEAT b729 trap 4)** -- standing.probes: before the lock gate permits, a plain suite part writes data/<act>_probe_<part>.txt and its mid exercise, never a name the pre-push suite writes; the comparison reads those banks; tools/b378_lockgate.py refuses while any tracked path is a probe output, printing the paths, the verdict and the exit code carrying it; the probe paths stay untracked, so the lock’s hash and N4’s read never meet them. b733’s tree at the commit before its lock, replayed with no edit: REFUSED, 24 paths, event (11)’s seventeen and seven ls-remote banks tracked beside them and moved by no later commit, so the class is wider than the row and the row’s seventeen stands for what N4 read. b732’s lock passes (:5).

**(ceiling) the root prompt’s ceiling a dry score (`(R344)`(2)(ii), event (11); CLAIM ; NEW)** -- standing.rootprompt.ceiling reads every score REFUTED at prompt time, and takes N4 where a path the suite writes stood tracked at the lock or a tracked bank differs from the lock’s; no ceiling is typed. b733’s prompt regenerated reads at most 6 of 8, N4 and N5, where the typed line read 7 (:51).

**(gitwrite) GIT_WRITE matches the command, not the path (`(R344)`(2)(iii), event (10); CLOSE ; NEW)** -- standing.gitwrite.is_write counts the gated push only where a command runs it. b733’s eighth message reads as one write, the arm’s count over its window falling from 8 to the real 7; the gated push stays a write (:63).

**(date) one date source (`(R344)`(2)(iv), event (3); CLOSE ; NEW)** -- standing.close.act_date reads the worklist’s DATE where the face and the worklist read it; close.py reads no date field of act_current. “THE FACE IS NOT LOCKED” replayed clean on b733, and close.py’s main runs as the face names it, no scratch caller; data/act_current.json keeps the field, stamped from the clock and read by nothing here (:75).

**(subjects) commit subjects composed from the bank (`(R344)`(2)(v), events (2), (5); CLAIM ; NEW)** -- standing.subjects.compose prints the head from the act and the step’s phase and any figure from its bank; check refuses a typed subject that differs. “62 files” against 63 and “b733 seal:” against the phase lock both read; b732’s lock subject reads clean (:84).

**(retired) the printed name G-READ-RULE-STANDING (`(R344)`(2)(vi); CLOSE ; NEW)** -- THE EVENT: the name printed at b732 and b733 with no arm among the 116, the arm standing on tools/standing/arms.py’s retired list. THE CHOICE PRINTED: the print removed from the suite’s template, no arm row given, a retired arm owing no row (:97).

**(emptyread) act_root’s empty remote read its own word (`(R344)`(2)(vii), defect (o); CLOSE ; NEW)** -- tools/act_root.py verify: where a repository reads empty and others answer, the empty repositories print and a row resting only on them reads UNREAD, not DISAGREE; a row with a reason of its own stays DISAGREE. b733’s three-repository read replayed over a stand-in, no remote touched (:106).

**(clauses) clause numbers read from the ruling’s text (`(R344)`(2)(viii), event (8), defect (n); CLOSE ; REPEAT b733 (n))** -- standing.cites.next_clause reads the clause naming the next act from the ruling; the entry’s touch-read line calls it and the suite’s freeze line prints no typed clause. b733’s line regenerates as (R343)(6); b734’s ruling reads (R344)(6) (:115).

**(defectids) a defect’s commit ids read from the log (`(R344)`(2)(ix), event (9); CLAIM ; NEW)** -- standing.defectids traces each message over the one-write row through its commit subject to the logs. b733’s seven read with the kernel’s 834f6ac and without relay 3471c14b (:127).

**b733’s events (1)-(11):**

**(1)** the seat recorded the lock commit 09fe2151 as phase ’seal’ from a stale note of its own, where the commit takes ’lock’ … (relay data/b733_events.txt, row (1); the seat’s; CLAIM; NEW; the row corrected before any commit; the phase the arm reads).
**(2)** the lock commit’s subject opens "b733 seal:" where its phase is ’lock’ and b732’s opened "b732 lock:", of the same … (relay data/b733_events.txt, row (2); the seat’s; CLOSE; NEW; repair (subjects)).
**(3)** tools/standing/close.py dry refused, "THE FACE IS NOT LOCKED": data/act\_current.json :8 reads date 2026-11-01, carried … (relay data/b733_events.txt, row (3); the seat’s; CLOSE; NEW; repair (date)).
**(4)** a ’git grep’ chain carrying a pipe refused by the hook, PIPE; nothing ran (data/b733\_hook\_refusals.txt :9). (relay data/b733_events.txt, row (4); the seat’s; CLOSE; REPEAT of b733 (i); nothing ran).
**(5)** the seal commit e5ae2b8d’s subject says "62 files", copied from b732’s line; data/b733\_seal\_hashes.json reads 63. … (relay data/b733_events.txt, row (5); the seat’s; CLAIM; NEW; repair (subjects)).
**(6)** N5 REFUTED on one clause alone, the scorer’s one git write per message, the seven ’add && commit’ messages of defect … (relay data/b733_events.txt, row (6); the score; CLOSE; REPEAT of b733 (q); ’(R344)’(1): the navigator’s omission, the clause named in this act’s N5; the add and the commit separate messages since).
**(7)** the root’s prompt, 2 questions in 1 call, both answered by the recommended option, "Print as read" and "Land and push" … (relay data/b733_events.txt, row (7); the author’s word; CLOSE; NEW; ’(R344)’(1): read as answers to the readings, not to the figure).
**(8)** the entry’s touch-read paragraph prints "the next act of (R343)(9)", the carried composer’s clause number under the act … (relay data/b733_events.txt, row (8); the seat’s; CLOSE; REPEAT of b733 (n); repair (clauses)).
**(9)** defect (q) names relay 3471c14b (02:03:48Z) among its seven, where that commit is not among the arm’s messages; the … (relay data/b733_events.txt, row (9); the seat’s; CLAIM; NEW; repair (defectids)).
**(10)** the commit ca9c2162 chained to a read, ’git grep ... tools/push\_gated.sh’: G-RULE-ONE-GIT-WRITE moves from 7 to 8 at … (relay data/b733_events.txt, row (10); the seat’s; CLOSE; NEW; repair (gitwrite)).
**(11)** N4 goes REFUTED at the pre-push suite. The gate commit eb9b34da carried the suite’s probe banks, so seventeen of them … (relay data/b733_events.txt, row (11); the seat’s; CLAIM; REPEAT of b729 trap 4; repairs (probes) and (ceiling); the class wider than the row, seven ls-remote banks beside the seventeen).

**b733’s defects:**

**(a)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b732 (a)).
**(b)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of class (19)).
**(c)** (relay data/b733_defects.txt; the seat’s; CLOSE; NEW).
**(d)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b732 (d)).
**(e)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b732 (g)).
**(f)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b732 (c)).
**(g)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b733 (d)).
**(h)** (relay data/b733_defects.txt; the seat’s; CLOSE; NEW).
**(i)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of class (19)).
**(j)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b733 (e)).
**(k)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of class (14)).
**(l)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of class (19)).
**(m)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of class (19)).
**(n)** (relay data/b733_defects.txt; the seat’s; CLOSE; NEW; repair (clauses)).
**(o)** (relay data/b733_defects.txt; the seat’s; CLOSE; NEW; repair (emptyread)).
**(p)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b731 (8)).
**(q)** (relay data/b733_defects.txt; the seat’s; CLOSE; NEW; the name 3471c14b corrected by event (9), repair (defectids)).
**(r)** (relay data/b733_defects.txt; the seat’s; CLOSE; REPEAT of b733 (i)).

**b733’s refusals** (relay data/b733_hook_refusals.txt at 05d53af9, one a line): :1 READ 00:48:06Z, recorded at defect (b); :2 READ 00:48:06Z, recorded at defect (b); :3 READ 00:48:06Z, recorded at defect (b); :4 PIPE 01:19:12Z, recorded at defect (i); :5 REDIR 02:11:00Z, recorded at defect (k); :6 READ 02:19:15Z, recorded at defect (l); :7 READ 02:22:38Z, recorded at defect (m); :8 PIPE 03:15:28Z, recorded at defect (r); :9 PIPE 04:23:23Z, recorded at event (4); :10 READ 05:33:01Z, no row, entered here; :11 READ 05:33:01Z, no row, entered here; :12 READ 05:33:02Z, no row, entered here.

**The counter:** CLAIM 4, CLOSE 25 over the 29 items (eleven events, eighteen defects), as b733’s closing prints it (relay data/b733_closing.txt :5); REPEAT 17 of 29; the CLAIM items (1), (5), (9), (11).

*Filed at b734 on the author’s ruling `(R344)`(1)-(2): generated by the record tool’s c1 route (`tools/standing/fold.py record c1 corrigendum`, the act’s override in relay tools/acts/b734.py) from b733’s events and defects banks read unedited, its refusal bank, and the v1.14.0 controls bank; banked as relay `data/b734_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (54). It answers b733’s record; no sealed tool, face, trail or root-named bank of b733 is edited.*
