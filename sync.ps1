# sync.ps1
# Quick sync script for the sample-ai-repository fork
# Usage:
#   .\sync.ps1           -> pull latest from YOUR fork (origin/main)
#   .\sync.ps1 -upstream -> also fetch + merge from the original upstream repo

param (
    [switch]$upstream
)

$ORIGIN   = "https://github.com/TheClairvoyantBeing/sample-ai-repository.git"
$UPSTREAM = "https://github.com/YOUR_UPSTREAM_ORG/sample-ai-repository.git"  # <-- change this if needed
$BRANCH   = "main"

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  sample-ai-repository  |  Sync Script" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan

# ── 1. Pull from your fork (origin) ──────────────────────────
Write-Host "`n[1/2] Pulling latest from your fork (origin/$BRANCH)..." -ForegroundColor Yellow
git pull origin $BRANCH

if ($LASTEXITCODE -ne 0) {
    Write-Host "`n[ERROR] Pull from origin failed. Fix conflicts and try again." -ForegroundColor Red
    exit 1
}

# ── 2. (Optional) Sync from upstream ─────────────────────────
if ($upstream) {
    Write-Host "`n[2/2] Fetching from upstream..." -ForegroundColor Yellow

    # Add upstream remote if it doesn't exist yet
    $remotes = git remote
    if ($remotes -notcontains "upstream") {
        Write-Host "  Adding upstream remote: $UPSTREAM" -ForegroundColor Gray
        git remote add upstream $UPSTREAM
    }

    git fetch upstream
    Write-Host "  Merging upstream/$BRANCH into local $BRANCH..." -ForegroundColor Gray
    git merge upstream/$BRANCH --no-edit

    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n[ERROR] Merge from upstream failed. Resolve conflicts manually." -ForegroundColor Red
        exit 1
    }

    Write-Host "  Pushing merged changes back to your fork..." -ForegroundColor Gray
    git push origin $BRANCH
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "  All done! Repo is up to date." -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
