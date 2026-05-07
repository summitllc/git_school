# Facilitator Guide

This document is for whoever is running the git-school training session.
It covers repo prep, timing guidance, and answers to common trainee questions.

---

## Before the Session

### 1. Ensure the repo is up to date
```
git checkout main
git pull
```

### 2. Create the merge conflict branch for Exercise 5

Exercise 5 requires a branch called `feature/conflict-notes` that modifies the same
section of `sandbox/ex5_team_notes.txt` as trainees will, triggering a conflict.

```
git checkout main
git checkout -b feature/conflict-notes
```

Open `sandbox/ex5_team_notes.txt` and add a note in the **In Progress** section, e.g.:

```
## In Progress

- Refactoring the ingestion pipeline (added by facilitator to create a conflict)
```

Then commit and push:

```
git add sandbox/ex5_team_notes.txt
git commit -m "facilitator: seed conflict branch for exercise 5"
git push origin feature/conflict-notes
git checkout main
```

This branch must exist on the **remote** (GitHub) before trainees reach Exercise 5.

### 3. Verify SSH access
Make sure all trainees have completed Module 1 (SSH key setup + clone) before the
session starts, or budget 20–30 minutes at the beginning for setup.

---

## Suggested Timing (2-hour session)

| Time | Activity |
|---|---|
| 0:00–0:20 | Module 1 — Setup (or verify pre-done homework) |
| 0:20–0:35 | Module 2 — Git Concepts (lecture/discussion) |
| 0:35–1:00 | Module 3 — Git Workflow + Exercises 1 & 2 |
| 1:00–1:15 | Module 4 — Merge Conflicts + Exercise 5 |
| 1:15–1:30 | Module 5 — Pull Requests + capstone PR |
| 1:30–1:45 | Module 6 — Useful Commands + Exercises 3, 4, 6, 7 (if time permits) |
| 1:45–2:00 | Q&A, wrap-up |

_Note:_ Exercises 3, 4, 6, and 7 work well as take-home practice if time runs short.

---

## Common Questions & Answers

**"Why do I get `Please tell me who you are` when I try to commit?"**
They skipped `git config`. Have them run:
```
git config --global user.name "First Last"
git config --global user.email "first.last@summitllc.us"
```

**"My push was rejected with `error: failed to push some refs`"**
Their remote branch has commits they don't have locally. They need to pull first:
```
git pull origin <their-branch>
```
Then resolve any conflicts and push again.

**"I accidentally committed to `main`"**
This can happen. To undo the last commit and move the changes back to the working tree:
```
git reset HEAD~1
```
Then have them create a proper branch and commit there. Do **not** force push `main`.

**"I can't find my branch after switching"**
Run `git branch` to list local branches. If it's not there, it may only exist on the
remote — run `git fetch` then `git branch -r` to see remote branches, and
`git checkout <branch-name>` to check it out locally.

**"git says my branch is ahead/behind origin"**
- *Ahead* means they have local commits not yet pushed — run `git push`
- *Behind* means the remote has commits they don't have — run `git pull`
- *Ahead and behind* means both — they'll need to pull, resolve any conflicts, then push

**"What's the difference between `git fetch` and `git pull`?"**
`git fetch` downloads changes from GitHub but doesn't touch your working files.
`git pull` = `git fetch` + automatically merges into your current branch.
Fetching first is safer if you want to review what changed before merging.

---

## Post-Session

- Remind trainees to delete their `training/<name>` branch once their capstone PR is merged
- Encourage them to reference [Module 6](./06_useful_commands.md) and the [resources in the readme](./readme.md) as they start using git on real projects
