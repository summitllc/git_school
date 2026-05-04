# Contributing to git-school

Thank you for helping improve this training repo! This document explains how to contribute.

## Who Should Contribute

Anyone who has completed the course is encouraged to contribute. Improving documentation,
fixing typos, adding examples, and updating outdated content are all valuable contributions.

## Contribution Workflow

1. **Create a branch** off of `main` with a descriptive name:
   ```
   git checkout -b feature/improve-merge-conflict-section
   ```

2. **Make your changes** to the relevant module file(s).

3. **Commit your changes** with a clear, descriptive commit message:
   ```
   git commit -m "Clarify merge conflict resolution steps in module 4"
   ```

4. **Push your branch** to the remote repo:
   ```
   git push
   ```

5. **Open a Pull Request** into `main` on GitHub and assign a reviewer.

6. **Address any review feedback**, then merge once approved.

## What Makes a Good Contribution

- **Fix something confusing** — if a section tripped you up during training, it will trip up the next person too
- **Keep language beginner-friendly** — this repo is for people new to git
- **Update outdated content** — tools and best practices change over time
- **Add examples** — concrete examples are almost always more helpful than abstract descriptions

## What to Avoid

- Do not commit any credentials, passwords, API keys, or personal data
- Do not commit large binary files (screenshots should be kept to a minimum and sized appropriately)
- Do not make changes directly to the `main` branch — always use a Pull Request

## Repo Structure

| File/Folder | Purpose |
|---|---|
| `readme.md` | Landing page — course overview and module index |
| `01_setup.md` | Module 1: Installing git and SSH setup |
| `02_concepts.md` | Module 2: Distributed version control and branching concepts |
| `03_workflow.md` | Module 3: Core git commands and the commit workflow |
| `04_merge_conflicts.md` | Module 4: Pulling branches and resolving merge conflicts |
| `05_pull_requests.md` | Module 5: Pushing, opening PRs, and code review |
| `06_useful_commands.md` | Module 6: .gitignore, git log, git diff, git stash |
| `sandbox/` | Practice files for hands-on exercises |
| `img/` | Images used in the course modules |
