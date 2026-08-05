# Mirror build — PLACE-papers -> flat dated zip in D:\MY-DOwnloads\ (the reviewer mirror).
# Convention matched from mirror-refresh-2026-08-02.zip: flat .md roster + generated
# MANIFEST.md (bytes | md5 | version | last-commit).  Verify-by-content at the end.
param([string]$DateTag = (Get-Date -Format 'yyyy-MM-dd'))

$repo = 'D:\MY-DOwnloads\PLACE-papers'
$rel = @(
  'FINDINGS.md','REGISTRY.md','OPEN_TRAILS.md','SPIRAL_MAP.md','VERIFICATION_LOOM.md','ERRATA.md',
  'phase1.5\proofs\THE_RESIDUE_OF_RH.md','day1\A_Place_to_Stand.md',
  'phase1.5\proofs\PATHS_TO_THE_CRITICAL_LINE.md','phase1.5\proofs\THE_UNCONDITIONAL_SURROUND.md',
  'phase1.5\simplicity\SIMPLICITY_OF_RIEMANN_ZEROS.md','phase1.5\method\EXCLUSION_ENGINE.md',
  'phase1.5\structural\FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md','phase1.5\method\INVARIANCE_BARRIERS.md',
  'phase1.5\spectral\GRH_CASCADE.md','phase1.5\spectral\BALANCE_AND_POSITIVITY.md',
  'phase2\method\ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md',
  'phase2\quantum\FORMATION_DISTANCE_AND_SILENCE_AS_PROTECTION.md',
  'phase2\quantum\SILENCE_STAGES_DEALIGNMENT.md',
  'phase1.5\proofs\INDEX_ARITY_AT_THE_CRITICAL_LINE.md',  # roster ADDITION 2026-08-04 (ferry-required)
  'phase1.5\method\INSTRUMENTS.md'                        # roster ADDITION 2026-08-05 (author-called)
)

$head = (git -C $repo rev-parse --short HEAD).Trim()
$stage = Join-Path $env:TEMP "mirror-build-$DateTag"
if (Test-Path $stage) { Remove-Item $stage -Recurse -Force }
New-Item -ItemType Directory -Path $stage | Out-Null

$rows = @()
foreach ($r in $rel) {
  $src = Join-Path $repo $r
  if (-not (Test-Path $src)) { Write-Host "MISSING: $r"; continue }
  $leaf = Split-Path $r -Leaf
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
# ---- roster line, DERIVED at build time (never authored, never carried forward) ----
# The previous build's roster is stored beside this script; the line below is computed by
# diffing it against the roster this build actually assembled.
$rosterState = Join-Path $PSScriptRoot 'mirror_roster.json'
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
