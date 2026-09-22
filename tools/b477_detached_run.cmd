@echo off
rem b477_detached_run.cmd -- the Gram run under (R80) per (R86), started DETACHED by Start-Process.
rem ### The runner is PYTHON, so every log line carries its own real timestamp -- b475's launcher
rem ### stamped one instant on every line because cmd expands %time% once per FOR block, and that
rem ### defect is not repeated here. ### The runner halts itself if the diagonal control fails.
setlocal
set "LOG=D:\relay\data\b477_gram.log"
cd /d D:\relay
echo === [%date% %time%] b477 GRAM RUN launched >> "%LOG%"
python tools\b477_gram.py >> "%LOG%" 2>&1
echo === EXIT %errorlevel% : b477_gram.py >> "%LOG%"
echo === [%date% %time%] RUN COMPLETE >> "%LOG%"
endlocal
