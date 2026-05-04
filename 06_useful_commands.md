# Module 6: Useful Commands

This module covers four tools that will save you time and frustration once you start using `git` regularly.

## `.gitignore`

A `.gitignore` file tells git which files and directories to **never track**. This is one of the most
important habits to build — it's how you prevent accidentally committing secrets, credentials,
large data files, or machine-specific config that has no business being in source control.

A `.gitignore` file lives at the root of your repo. Each line is a pattern for files to ignore:

```
# Ignore a specific file
secrets.env

# Ignore all .csv files
*.csv

# Ignore an entire folder
data/

# Ignore all files with a specific extension in any subfolder
**/*.log
```

Every repo should have a `.gitignore`. GitHub provides useful templates for common languages
and environments at https://github.com/github/gitignore.

_Note:_ Adding a file to `.gitignore` only prevents it from being tracked going forward. If you
have already committed a file, adding it to `.gitignore` will **not** remove it from history.
Removing sensitive data from git history is painful — prevention is far easier.

---

## `git log`

`git log` shows the commit history of your current branch:

```
$ git log
commit a3f9c12 (HEAD -> feature/my-feature, origin/feature/my-feature)
Author: Jane Smith <jane.smith@summitllc.us>
Date:   Mon Apr 28 10:22:01 2026 -0400

    Add data validation to input parser

commit 7b1d4e8 (origin/main, main)
Author: Tom Gardner <tom.gardner@summitllc.us>
Date:   Fri Apr 25 14:05:33 2026 -0400

    Initial project setup
```

Each entry shows the commit hash, author, date, and message. A few useful variations:

- `git log --oneline` — condensed view, one line per commit
- `git log --oneline --graph` — adds a visual branch/merge graph
- `git log --oneline -10` — show only the last 10 commits
- `git log --author="Jane"` — filter commits by author

`git log` is read-only and safe to run at any time.

---

## `git diff`

`git diff` shows the line-by-line changes between two states. It's what the "Files Changed" tab
in a GitHub Pull Request is doing under the hood.

Common usages:

```bash
# Show unstaged changes in your working tree (what you've changed but not yet git add-ed)
git diff

# Show staged changes (what you've git add-ed but not yet committed)
git diff --staged

# Compare two branches
git diff main feature/my-feature

# Compare a specific file between two branches
git diff main feature/my-feature -- path/to/file.R
```

Lines starting with `-` were removed. Lines starting with `+` were added.

`git diff` is read-only and safe to run at any time.

---

## `git stash`

`git stash` temporarily shelves changes you've made to your working tree so you can switch
context — then brings them back when you're ready.

**The problem it solves:** You're halfway through some work when you need to urgently fix a bug
on a different branch. You don't want to commit half-finished code, but you also don't want to
lose your changes. `git stash` saves them for later.

```bash
# Stash your current uncommitted changes
git stash

# List all stashes
git stash list

# Restore the most recent stash (and remove it from the stash list)
git stash pop

# Restore the most recent stash (but keep it in the stash list)
git stash apply
```

Example workflow:

```
$ git stash
Saved working directory and index state WIP on feature/my-feature: a3f9c12 Add data validation

$ git checkout -b hotfix/urgent-fix
# ... fix the bug, commit, push ...

$ git checkout feature/my-feature
$ git stash pop
# Your work-in-progress is restored exactly as you left it
```

_Note:_ By default, `git stash` does not stash untracked files (new files you haven't `git add`-ed yet).
Use `git stash -u` to include those as well.

---

## What's Next?

You've now completed all six modules. You know how to set up git, understand how it works,
follow the full commit and PR workflow, resolve merge conflicts, and use the most valuable
day-to-day commands.

**Capstone Exercise:** Put it all together by adding yourself to `yearbook.md`:
1. Create a branch off of `main`: `git checkout -b training/<your-name>/yearbook`
2. Add your name and preferred language/tool to the file
3. Commit and push your branch
4. Open a Pull Request into `main` on GitHub

Once your PR is merged, you're officially a git-school graduate.

---

**Previous:** [Module 5 - Pull Requests](./05_pull_requests.md) | [Back to Course Overview](./readme.md)
