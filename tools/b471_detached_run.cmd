@echo off
rem b471_detached_run.cmd -- the zeta23 axiom run under (R80), started DETACHED by Start-Process.
rem Every step's exit code goes into the log; the last line is "RUN COMPLETE" when it ends.
rem LEAN_NUM_THREADS is UNSET, as the order says. Nothing is written into the clone but its own .lake.
setlocal
set "LEAN_NUM_THREADS="
set "LOG=D:\relay\data\b471_zeta23_build.log"
set "NAMED=C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\49943484-5ff3-4a99-9f75-0f3a8ae0d39a\scratchpad\B471NamedAxioms.lean"
cd /d D:\relay\data\anthropic-zeta23\formal-math\zeta23
echo === [%date% %time%] b471 detached run START in %cd% >> "%LOG%"
echo === STEP 1 : lake build Solution >> "%LOG%"
call lake build Solution >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : lake build Solution >> "%LOG%"
echo === STEP 2 : lake env lean scripts\PrintAxioms.lean (as shipped) >> "%LOG%"
call lake env lean scripts\PrintAxioms.lean >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : scripts\PrintAxioms.lean >> "%LOG%"
echo === STEP 3 : lake env lean B471NamedAxioms.lean (EF_lit_zetaZeroConfig, EF_lit, EF_lit_zeta) >> "%LOG%"
call lake env lean "%NAMED%" >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : B471NamedAxioms.lean >> "%LOG%"
echo === [%date% %time%] RUN COMPLETE >> "%LOG%"
endlocal
