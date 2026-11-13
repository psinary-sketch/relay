<!-- seatfile: the lines below are written by tools/standing/seatfile.py; edited by no hand -->
# THE SEAT`S FILE

Read at every start and after every summary. Written by `tools/standing/seatfile.py write` from the hook`s own table
(tools/standing/hook.py ROWS); edited by no hand. The act is the one `data/act_current.json` names.

## The paths
- the relay: this folder; PLACE-papers and the kernels: at the places the ferry`s PATHS line gives
- the ruling and the ferry: `data/<act>_ferry.txt`; the amendments: `data/<act>_amendments.json`
- the standing clauses: `data/standing_clauses_v9.txt`; the readfirst bank: `data/<act>_readfirst.txt`
- the act`s banks: `data/<act>_stepzero.txt`, `_events.txt`, `_defects.txt`, `_hook_refusals.txt`, `_steps.json`
- the one-call tool: `tools/standing/commit.py`; the hook: `tools/standing/hook.py`; the (W) list: `data/<act>_wlist.json`

## The hook`s 21 kinds: the refused form, and the form to send in its place
- READ -- refused: a Read with no limit (a short file included), a limit above 200, or a limit with no offset. Send: an offset and a limit of at most 200 on every Read.
- PIPE -- refused: a pipe outside quotes in a shell command, `2>&1 |` and a listing included. Send: the search tool (Grep, with head_limit), the Read tool, or a scratch script that prints.
- REDIR -- refused: a redirect of any stream outside quotes (`>`, `>>`, `2>/dev/null`, `2>&1`, `*>`). Send: a scratch script that opens and writes its own file; stderr is captured as it is.
- ENV -- refused: a command opening with an assignment (`NAME=value cmd`, `env NAME=`, `$env:NAME =`). Send: none: the environment left as it is, a value passed as an argument.
- REMOTE -- refused: more than one ls-remote in one command. Send: one remote read per command; a retry is an event of the act.
- SUITE -- refused: two suite parts, or a part and a combine, in one call. Send: one suite part or combine per call, each its own message.
- ORDER -- refused: a branch delete before the citation check has run. Send: the citation check first, then each delete by the one-call tool, one per message.
- POSTSEAL -- refused: after the seal, a shell filter or redirect over the entry or the trail. Send: the Read tool, with an offset and a limit.
- GITWRITE -- refused: a second git write in one message, any repository, parallel calls included. Send: one git write per message: `commit.py <relay|pp> add <paths>` in one message, the commit in the next.
- LOCKED -- refused: a rewrite after the lock of a bank written before it. Send: the next act`s bank or the post-seal events bank; the sealed bank stands.
- INPLACE -- refused: an in-place edit by the shell (sed -i, perl -i, Set-Content, Add-Content, Clear-Content). Send: the Edit or Write tool; a rendered file by its render re-run.
- SUBJECT -- refused: a gate, lock or seal commit by the shell, or a subject the tool did not compose. Send: `commit.py <relay|pp> <gate|lock|seal>`, the subject composed from its bank.
- BACKGROUND -- refused: a suite part or combine sent in the background. Send: the foreground with the 600 s limit, each part after its predecessor`s bank.
- SED -- refused: sed in any form, a read included. Send: the Read tool, or `tools/standing/peek.py`.
- HASHED -- refused: an Edit or Write of a bank its tool wrote (named in data/<act>_bank_hashes.json). Send: the bank`s own tool run again.
- ROWID -- refused: a PLACE-papers commit adding a ledger row whose ID the file already holds. Send: the ID allocated from the file`s maximum over every table of the prefix (tools/standing/rowid.py).
- PLAINGIT -- refused: a git write by plain git (add, commit, checkout, branch, push, tag). Send: `python -X utf8 -u tools/standing/commit.py` with add, restore, delete, branch or the phase and its words.
- BYDESIGN -- refused: an Edit or Write after the lock of a file written after it by design (answers pair, author-words banks, post-lock scans, post-seal events). Send: each by its own tool: `record answers`, tools/standing/append.py, the one-call tool`s scan.
- WLIST -- refused: a Write or Edit of a tracked path outside the (W) list, or with the list absent or stale. Send: `python -X utf8 -u tools/standing/wlist.py bank <act>` after every amendment row and every change of the worklist`s W_WORDS (the entries a ruling gives in words, each with its clause); write within the list.
- COMPOSER -- refused: a question put to the author that `rootprompt.py put` did not compose and bank. Send: `python -X utf8 -u tools/standing/rootprompt.py put <act> <json>` first, then the question as banked.
- LIMIT -- refused: a route of tools/standing/limits.py`s table in the foreground with no timeout or one beneath its limit. Send: the timeout `tools/standing/limits.py` prints for that route.

## The rules beside the hook
- a commit`s words carry no semicolon; the one-call tool composes `<act> <phase>: <words>`
- one git write per message across every repository; the add in one message, the commit in the next
- a question to the author: through the composer (`rootprompt.py put`), never typed straight
- a long run: the limit `tools/standing/limits.py` prints; no suite part in the background
- the restart flag, the free memory (hold 2,560 MB) and both volumes (floor 5,000 MB) read before each route and commit
- in this file ((R364)(3)(i)): no identifier of the author and no path under the user`s profile;
  in anything the act writes (N5): no new occurrence of the author`s name, address or researcher identifier beyond a byline under
  I-23, and no program`s name and no file or folder name from the author`s own data (amendment row 4 (3): these two clauses, no other)
- a passed item`s write beyond the (W) list: `amend.py pass <item> <word_at> <word_cite> <paths> --write` before the write ((R364)(3)(xvi));
  a shared tool committed by any other route: `amend.py shared` read before its commit

## The restatement ((R364)(3)(xviii))
After a summary of the session or a change of model, and before any write: read whole, from the banks that hold them, the
ruling and the ferry, the author`s words since, and the step-zero, events, defects and refusals banks; then state in ten lines
or fewer where the act stands, the next write and the rules that bind it, and what the act does not do. The chain read`s
boundary rule (`tools/standing/chain.py`) says whether a summary stands.

## The step zero after a change ((R364)(3)(xix))
After a change of session, of the harness`s version or of a store`s place: each standing instrument that reads the session,
the transcript or the state folder runs its positive control before the act`s opening write (`chain.py control <session>`,
`hold.py control`, `hook.py control`, `harness.py control <session>`); the hook`s state stands in the state folder on the data
volume (`tools/standing/statedir.py`), read by the hook and the one-call tool alike.
<!-- seatfile: end -->
