# Mirror build — PLACE-papers -> flat dated zip in D:\MY-DOwnloads\ (the reviewer mirror).
# Convention matched from mirror-refresh-2026-08-02.zip: flat .md roster + generated
# MANIFEST.md (bytes | md5 | version | last-commit).  Verify-by-content at the end.
param([string]$DateTag = (Get-Date -Format 'yyyy-MM-dd'))

$repo = 'D:\MY-DOwnloads\PLACE-papers'
# ### THE ROSTER MOVED OUT OF THIS FILE ON 2026-08-26 (b183).
# ### IT NOW LIVES IN tools\mirror_roster.json, WHICH IS THE SINGLE SOURCE OF TRUTH.
# ### WHY: until b183 there were TWO roster artifacts -- this array, which the builder
# ### read, and mirror_roster.json, which NOTHING read and which held STAGED ARCHIVE
# ### NAMES rather than source paths. ### AT b182 A ROW ADDED TO THE JSON CHANGED
# ### NOTHING AND THE MIRROR VERIFIED **CLEAN AT 33 FILES WITHOUT THE FILE IN IT**.
# ### THE JSON WAS AN OUTPUT WRITTEN AS THOUGH IT WERE AN INPUT.
# ### DIRECTION OF THE MERGE: ps1 -> json. The artifact carrying MORE information
# ### survives -- paths determine staged names, staged names do not determine paths.
# ### AND AN EMPIRICAL GROUND FROM b183 ITSELF: a Python reader of THIS array got it
# ### wrong on its first run, harvesting apostrophes out of these very comments.
# ### A ROSTER EVERY NON-POWERSHELL READER MUST PARSE POWERSHELL TO READ IS A ROSTER
# ### THAT WILL BE MISREAD.
$rosterPath = Join-Path $PSScriptRoot 'mirror_roster.json'
if (-not (Test-Path $rosterPath)) { throw "ROSTER MISSING: $rosterPath. Refusing to build "
  + 'an export with no roster -- an empty roster is a hard failure, never an empty build.' }
$rel = (Get-Content $rosterPath -Raw | ConvertFrom-Json).files
if (-not $rel -or $rel.Count -eq 0) {
  # ### THE ZERO CASE, AT THE BUILDER TOO AND NOT ONLY AT THE VERIFIER: b167 had to add
  # ### an empty-scope hard failure to banned_terms.py and b179's hook cleared an empty
  # ### staged set. ### IN THIS RECORD EMPTINESS READS AS SUCCESS UNLESS A LINE IS
  # ### WRITTEN AGAINST IT.
  throw 'EMPTY ROSTER. Refusing to build a zero-file export that would verify CLEAN.'
}

$head = (git -C $repo rev-parse --short HEAD).Trim()
$stage = Join-Path $env:TEMP "mirror-build-$DateTag"
if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage | Out-Null

$rows = @()
foreach ($r in $rel) {
  $src = Join-Path $repo $r
  if (-not (Test-Path $src)) { Write-Host "MISSING: $r"; continue }
  $leaf = Split-Path $r -Leaf
  # ### DEFECT FIXED b144, CAUGHT BY A MECHANICAL PROBE. The export is FLAT, so two
  # ### roster paths with the same leaf name silently collide -- the second copy
  # ### overwrites the first and the MANIFEST still verifies CLEAN, because clause 1
  # ### checks the export against ITSELF and cannot see a file that never survived
  # ### staging. b143 added archive\...\README.md to the roster and it took the flat
  # ### `README.md` slot, so the export shipped the LEDGER-SPLIT README where a
  # ### reviewer would open the REPO FRONT DOOR. ### A FLAT EXPORT MUST DISAMBIGUATE
  # ### ITS OWN NAMESPACE OR IT IS NOT A FAITHFUL EXPORT.
  $dir = Split-Path $r -Parent
  if ($dir -and (Test-Path (Join-Path $stage $leaf))) {
    $leaf = ((Split-Path $dir -Leaf) + '__' + $leaf)
  }
  if (Test-Path (Join-Path $stage $leaf)) {
    throw "ROSTER COLLISION unresolved for '$r' -> '$leaf'. Refusing to build a flat export that would silently drop a file."
  }
  Copy-Item $src (Join-Path $stage $leaf)
  $bytes = (Get-Item $src).Length
  $md5 = (Get-FileHash $src -Algorithm MD5).Hash.ToLower()
  $ver = '-'
  $head20 = Get-Content $src -TotalCount 20
  foreach ($line in $head20) {
    $m = [regex]::Match($line, '\bv\d+(\.\d+)+')
    if ($m.Success) { $ver = $m.Value; break }
  }
  $lc = (git -C $repo log -1 --format='%h %ad' --date=short -- $r).Trim()
  $rows += [pscustomobject]@{ file = $leaf; bytes = $bytes; md5 = $md5; version = $ver; commit = $lc }
}

$man = @()
$man += "# MANIFEST - mirror-refresh-$DateTag"
$man += ""
$man += "Source: PLACE-papers @ ``$head`` (main). Export $DateTag. $($rows.Count) files flat."
# ---- roster-CHANGE line, DERIVED at build time (never authored, never carried forward) ----
# The PREVIOUS BUILD'S STAGED-NAME LIST is stored beside this script in
# mirror_prevbuild.json; the line below diffs it against the staged names THIS build
# assembled. ### IT IS BUILD STATE, NOT THE ROSTER, AND IT IS OVERWRITTEN EVERY RUN.
# ### THE STATE FILE IS **NOT** THE ROSTER. b183 split them.
# ### Until b183 this line pointed at mirror_roster.json and the block below
# ### OVERWROTE IT with STAGED NAMES at the end of every build. ### THE FILE WAS
# ### PLAYING TWO ROLES: it looked like the builder's INPUT and it was the
# ### builder's OUTPUT. ### THAT IS WHY THE ROW ADDED AT b182 VANISHED.
# ### An input a process overwrites is not an input; it is a scratch pad with a
# ### misleading name.
$rosterState = Join-Path $PSScriptRoot 'mirror_prevbuild.json'
$now = $rows | ForEach-Object { $_.file } | Sort-Object
$prev = @()
$prevDate = $null
if (Test-Path $rosterState) {
  $st = Get-Content $rosterState -Raw | ConvertFrom-Json
  $prev = @($st.files)
  $prevDate = $st.lastChanged
}
$added = @($now | Where-Object { $prev -notcontains $_ })
$removed = @($prev | Where-Object { $now -notcontains $_ })
if (-not (Test-Path $rosterState)) {
  $man += "ROSTER: $($now.Count) files. No previous roster was recorded, so no diff is"
  $man += "available for this build; the change line begins from the next one."
  $changedOn = $DateTag
} elseif ($added.Count -or $removed.Count) {
  $man += "ROSTER CHANGE, THIS BUILD ($DateTag): $($now.Count) files."
  if ($added.Count)   { $man += "  ADDED:   $($added -join ', ')" }
  if ($removed.Count) { $man += "  REMOVED: $($removed -join ', ')" }
  $changedOn = $DateTag
} else {
  $since = if ($prevDate) { $prevDate } else { 'the first recorded build' }
  $man += "ROSTER: $($now.Count) files, unchanged since $since."
  $changedOn = $prevDate
}
$man += "This line is computed at build time by diffing the assembled roster against the"
$man += "previous build's, not carried forward as authored text."
@{ files = $now; lastChanged = $changedOn } | ConvertTo-Json -Depth 3 |
  Out-File $rosterState -Encoding utf8
$man += ""
$man += "| flat file | bytes | md5 | version | last-commit |"
$man += "|:--|--:|:--|:--|:--|"
foreach ($row in $rows) {
  $man += "| $($row.file) | $($row.bytes) | ``$($row.md5)`` | $($row.version) | $($row.commit) |"
}
$man -join "`n" | Out-File (Join-Path $stage 'MANIFEST.md') -Encoding utf8

$zip = "D:\MY-DOwnloads\mirror-refresh-$DateTag.zip"
if (Test-Path $zip) { Remove-Item $zip -Force }
Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $zip -CompressionLevel Optimal
Write-Host "built: $zip"
Write-Host "source HEAD: $head"
