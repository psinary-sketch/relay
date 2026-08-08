# DETACHED LAUNCH — the pattern of record (Start-Process -WindowStyle Hidden).
#
# THE RESTART COMMAND IS THIS FILE.  Re-running it after any stop resumes from the last banked
# chunk: the tail guard validates v/stage/dps/phase/idx/n, refuses a cache from another stage or
# precision, drops a torn tail, and recomputes from the last good chunk.  Nothing else is needed
# and no argument has to be remembered.
#
#     powershell -ExecutionPolicy Bypass -File D:\relay\tools\e16\launch_v3.ps1
#
# CADENCE IS SET AGAINST THE NEW MEASURED PER-ITEM COST, not inherited from the mpmath rates.
# The mpmath worker banked every 16 boundary values because each cost ~19-31 s; flint costs
# ~0.13 s at stage-3 precision, so 16 would bank ~470 times a minute and the fsync would become
# the run.  256 puts the bank interval back in the tens-of-seconds range where it belongs.
# A correctness gate does not test a rate — G3 ran at chunk 8 to make interruption likely; this
# is the production value and it is chosen separately.
$ErrorActionPreference = "Stop"
$here = "D:\relay\tools\e16"
$env:LI_TAYLOR_CHUNK = "256"
$env:LI_COEF_CHUNK   = "256"
$env:LI_LAM_CHUNK    = "128"
Remove-Item Env:\LI_TEST_ABORT      -ErrorAction SilentlyContinue
Remove-Item Env:\LI_NO_MEMO         -ErrorAction SilentlyContinue
Remove-Item Env:\LI_NO_DPS_FLOOR    -ErrorAction SilentlyContinue
Remove-Item Env:\LI_MAX_STAGE       -ErrorAction SilentlyContinue
Remove-Item Env:\LI_BANK            -ErrorAction SilentlyContinue
Remove-Item Env:\LI_CHUNKS          -ErrorAction SilentlyContinue

$p = Start-Process -FilePath "python" `
     -ArgumentList "$here\epstein_li_v3.py" `
     -WorkingDirectory $here `
     -RedirectStandardOutput "$here\li_v3_detached.log" `
     -RedirectStandardError  "$here\li_v3_detached.err" `
     -WindowStyle Hidden -PassThru
"launched PID $($p.Id) at $(Get-Date -Format o)"
$p.Id | Out-File "$here\li_v3.pid" -Encoding ascii
