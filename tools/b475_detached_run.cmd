@echo off
rem b475_detached_run.cmd -- the zeta23 axiom run under (R80), SERIALIZED, started DETACHED.
rem ### ONE `lake build <module>` PER CALL, in the order b475_order.txt holds, with LEAN_NUM_THREADS=1,
rem ### so no two Lean processes run at once. ### A timestamp and an exit code per module.
rem ### Nothing is written into the clone but its own ignored .lake.
setlocal enabledelayedexpansion
set "LEAN_NUM_THREADS=1"
set "LOG=D:\relay\data\b475_zeta23_build.log"
set "ORDER=D:\relay\data\b475_order.txt"
set "NAMED=C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--\49943484-5ff3-4a99-9f75-0f3a8ae0d39a\scratchpad\B471NamedAxioms.lean"
cd /d D:\relay\data\anthropic-zeta23\formal-math\zeta23
echo === [%date% %time%] b475 detached SERIALIZED run START in %cd% >> "%LOG%"
echo === LEAN_NUM_THREADS=%LEAN_NUM_THREADS% ; order file %ORDER% >> "%LOG%"
set /a N=0
for /f "usebackq delims=" %%M in ("%ORDER%") do (
  set /a N+=1
  echo === [%date% %time%] MODULE !N! : %%M >> "%LOG%"
  call lake build %%M >> "%LOG%" 2>&1
  echo === EXIT !errorlevel! : %%M >> "%LOG%"
)
echo === [%date% %time%] MODULES DONE : !N! >> "%LOG%"
echo === STEP : lake build Solution (the library target, after its modules) >> "%LOG%"
call lake build Solution >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : lake build Solution >> "%LOG%"
echo === [%date% %time%] STEP : lake env lean scripts\PrintAxioms.lean (as shipped) >> "%LOG%"
call lake env lean scripts\PrintAxioms.lean >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : scripts\PrintAxioms.lean >> "%LOG%"
echo === [%date% %time%] STEP : lake env lean B471NamedAxioms.lean (EF_lit_zetaZeroConfig, EF_lit, EF_lit_zeta) >> "%LOG%"
call lake env lean "%NAMED%" >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : B471NamedAxioms.lean >> "%LOG%"
echo === [%date% %time%] RUN COMPLETE >> "%LOG%"
endlocal
