"""
Week 2 — Git Branch & Commit History Viewer
Shows: your repository's branch structure and recent commit log in a visual format.
Run:  python weekly-reports/week-2/git_branch_viewer.py
"""

import subprocess
import sys
import os


def run_git(args):
    """Execute a git command and return the output."""
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True, text=True, encoding="utf-8",
            cwd=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        )
        return result.stdout.strip()
    except FileNotFoundError:
        print("  ❌ Git is not installed or not in PATH.")
        sys.exit(1)


def main():
    print("=" * 62)
    print("  🌿  WEEK 2 — GIT REPOSITORY OVERVIEW")
    print("=" * 62)

    # ── Current branch ──
    current = run_git(["branch", "--show-current"])
    print(f"\n  📍 Current branch: {current}")

    # ── All branches ──
    branches = run_git(["branch", "-a"])
    print("\n  ┌────────────────────────────────────────────────┐")
    print("  │              BRANCH STRUCTURE                  │")
    print("  └────────────────────────────────────────────────┘")
    for line in branches.splitlines():
        marker = "  →" if "*" in line else "   "
        branch_name = line.strip().replace("* ", "")
        if "*" in line:
            print(f"  {marker} 🟢 {branch_name}  (active)")
        elif "remote" in branch_name:
            print(f"  {marker} 🔵 {branch_name}")
        else:
            print(f"  {marker} ⚪ {branch_name}")

    # ── Recent commit history (graph) ──
    print("\n  ┌────────────────────────────────────────────────┐")
    print("  │              COMMIT HISTORY (last 15)          │")
    print("  └────────────────────────────────────────────────┘\n")

    log = run_git([
        "log", "--oneline", "--graph", "--decorate",
        "--all", "-n", "15",
        "--format=%C(auto)%h %C(blue)%an %C(reset)%s %C(yellow)(%cr)"
    ])

    if log:
        for line in log.splitlines():
            print(f"    {line}")
    else:
        print("    (no commits found)")

    # ── Repo stats ──
    print("\n  ┌────────────────────────────────────────────────┐")
    print("  │              REPOSITORY STATS                  │")
    print("  └────────────────────────────────────────────────┘")

    total_commits = run_git(["rev-list", "--count", "HEAD"])
    contributors = run_git(["log", "--format=%an", "--all"])
    unique_authors = set(contributors.splitlines()) if contributors else set()
    remote_url = run_git(["remote", "get-url", "origin"])

    print(f"\n    📊 Total Commits:   {total_commits}")
    print(f"    👥 Contributors:    {len(unique_authors)}")
    for author in sorted(unique_authors):
        print(f"       • {author}")
    print(f"    🔗 Remote:          {remote_url}")

    print("\n" + "=" * 62)
    print("  ✅ Git overview complete!")
    print("=" * 62)


if __name__ == "__main__":
    main()
