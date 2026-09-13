
<!-- b449 loom entry -->

### **A MIRROR CHECK WHOSE ARTEFACT IS GONE — noted once, 2026-09-13 (b449)**

b448’s closing record reads *“mirror           : CLEAN ON ALL THREE CLAUSES at b1656b1”* (relay `data/b448_closing.txt`). That check was made on `D:\MY-DOwnloads\mirror-refresh-2026-09-13.zip` as built at PLACE-papers `b1656b1`. Later the same day the `(R61)` execution rebuilt the mirror at `dc5e18e` (relay `data/b448_r61_mirror.txt`: *“manifest declares source HEAD    : dc5e18e”*). `tools/mirror_build.ps1` names its zip by date alone and removes an existing zip of that name before writing (lines 122–123), so the rebuild replaced the zip b448 verified. **b448’s check therefore names an artefact no longer on disk.** Its verdict is not re-read or changed, and b448’s bank is not edited. The builder already takes a `DateTag` parameter (line 4) that holds two builds from one day apart; the work-order `W-ORD-MIRROR-ZIP-NAME` is filed with b449’s trail record.
