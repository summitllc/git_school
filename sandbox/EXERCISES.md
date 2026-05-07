# Sandbox Exercises

Work through these exercises in order. Each one builds on skills from the previous.
All commands should be run from the root of the `git_school` repo in Git Bash.

---

## Before You Begin — Create Your Personal Training Branch

**You should never commit directly to `main`.** Before starting any exercises, create a
personal training branch that you'll use as your base throughout the session:

```
git checkout main
git pull
git checkout -b training/<your-name>
```

Replace `<your-name>` with your actual name, e.g. `training/jane-smith`.

All of your work during Exercises 1–4 will live on this branch. Exercises 5 and 6
will have you create additional branches off of it.

---

## Exercise 1 — Your First Commit 🟢 Beginner

**Goal:** Edit a file, stage it, and make your first commit.

**File:** `sandbox/ex1_my_first_commit.txt`

**Steps:**
1. Make sure you're on your training branch: `git branch` (asterisk should be on `training/<your-name>`)
2. Open `sandbox/ex1_my_first_commit.txt` and fill in the blanks
3. Run `git status` — you should see the file listed as modified
4. Stage the file: `git add sandbox/ex1_my_first_commit.txt`
5. Run `git status` again — notice how the output changed
6. Commit your changes: `git commit -m "ex1: fill in my info"`
7. Run `git status` one more time — your working tree should be clean

**You'll know you're done when:** `git status` shows `nothing to commit, working tree clean`

---

## Exercise 2 — Selective Staging 🟢 Beginner

**Goal:** Learn to stage only specific files rather than everything at once.

**Files:** `sandbox/ex2_file_a.txt`, `sandbox/ex2_file_b.txt`

**Steps:**
1. Make sure you're on your training branch: `git branch`
2. Open both files and make a small edit to each (add any text you like)
3. Run `git status` — both files should appear as modified
4. Stage **only** `ex2_file_a.txt`: `git add sandbox/ex2_file_a.txt`
5. Run `git status` — observe that `file_a` is staged but `file_b` is not
6. Run `git diff` — notice it only shows the **unstaged** changes (file_b)
7. Run `git diff --staged` — notice it only shows the **staged** changes (file_a)
8. Commit only the staged file: `git commit -m "ex2: update file_a only"`
9. Stage and commit file_b separately: `git add sandbox/ex2_file_b.txt` then commit

**You'll know you're done when:** You have two separate commits, one for each file.

---

## Exercise 3 — Create a Branch 🟡 Beginner-Intermediate

**Goal:** Create a feature branch, make changes, and observe how branches isolate work.

**File:** `sandbox/ex3_feature_branch.txt`

**Steps:**
1. Make sure you're on your training branch: `git checkout training/<your-name>`
2. Create and check out a new feature branch off of it: `git checkout -b feature/my-sandbox-branch`
3. Open `sandbox/ex3_feature_branch.txt` and add your idea to the list
4. Stage and commit your change
5. Switch back to your training branch: `git checkout training/<your-name>`
6. Open `sandbox/ex3_feature_branch.txt` again — your change is gone! (It lives on your feature branch)
7. Switch back to your feature branch: `git checkout feature/my-sandbox-branch` — your change is back
8. Run `git log --oneline` on each branch to see how their histories differ

**Bonus:** Run `git diff training/<your-name> feature/my-sandbox-branch` to compare the two branches directly.

**You'll know you're done when:** You can explain why the file looks different on each branch.

---

## Exercise 4 — The .gitignore 🟡 Intermediate

**Goal:** Update the root `.gitignore` file to prevent sensitive or irrelevant files from being tracked.

**Files:** `sandbox/ex4_data/`

**Steps:**
1. Make sure you're on your training branch: `git checkout training/<your-name>`
2. Navigate to the `sandbox/ex4_data/` folder and look at its contents
3. If `secrets.env` and some CSV files are not already present, create a few dummy files to practice with, for example:
    - `touch sandbox/ex4_data/secrets.env`
    - `touch sandbox/ex4_data/data1.csv`
    - `touch sandbox/ex4_data/data2.csv`
 4. Run `git status` so you can see which files in `sandbox/ex4_data/` are currently untracked
 5. Open the `.gitignore` file at the **root of the repo** (create it if it does not exist)
 6. Add rules to ignore:
    - All `.env` files (hint: `*.env`)
    - All `.csv` files (hint: `*.csv`)
    - But leave `analysis.R` tracked
7. Run `git status` again — the `.env` and `.csv` files in `sandbox/ex4_data/` should no longer appear
8. Stage and commit your `.gitignore`: `git add .gitignore` then commit


**Bonus:** Try running `git add sandbox/ex4_data/secrets.env` after adding it to `.gitignore`. What happens?

**You'll know you're done when:** Only `analysis.R` shows as untracked in `sandbox/ex4_data/`.

---

## Exercise 5 — Resolve a Merge Conflict 🟠 Intermediate

**Goal:** Experience and resolve a merge conflict — the most important skill for collaborative work.

**File:** `sandbox/ex5_team_notes.txt`

**Steps:**
1. Make sure you're on your training branch and create a new branch off of it: `git checkout training/<your-name>` then `git checkout -b feature/my-notes`
2. Open `sandbox/ex5_team_notes.txt` and replace the placeholder line **under the "In Progress" section** with your own note _(do not add a new line elsewhere in the section)
3. Stage and commit your change
4. Now pull the pre-built conflicting branch into your branch:
   `git pull origin feature/conflict-notes`
   _(Ask your facilitator to confirm this branch exists, or they may substitute a different branch name)_
5. Git will report a conflict in `ex5_team_notes.txt` — open the file
6. Look for the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
7. Decide what the file should look like and delete the markers
8. Stage the resolved file: `git add sandbox/ex5_team_notes.txt`
9. Complete the merge: `git commit -m "ex5: resolve merge conflict"`

**You'll know you're done when:** There are no conflict markers left in the file and `git status` is clean.

---

## Exercise 6 — Git Stash 🔴 Moderate

**Goal:** Use `git stash` to safely set aside work-in-progress so you can switch context.

**File:** `sandbox/ex6_analysis.py`

**The Scenario:** You're in the middle of adding a new function to `ex6_analysis.py` when your
teammate asks you to urgently fix a typo in `sandbox/ex1_my_first_commit.txt` on a separate branch.
You're not ready to commit your half-finished work, so you'll stash it.

**Steps:**
1. Make sure you're on your training branch, then create a working branch off of it: `git checkout training/<your-name>` then `git checkout -b feature/analysis-update`
2. Open `sandbox/ex6_analysis.py` and add a new function stub at the bottom (don't finish it)
3. Run `git status` — you have unstaged changes
4. Stash your work: `git stash`
5. Run `git status` — your working tree is clean again
6. Switch to a hotfix branch: `git checkout -b hotfix/typo-fix`
7. Make a small edit to `sandbox/ex1_my_first_commit.txt`, commit it
8. Switch back to your feature branch: `git checkout feature/analysis-update`
9. Restore your stashed work: `git stash pop`
10. Run `git status` — your unfinished changes are back

**Bonus:** Run `git stash list` at step 9 (before `git stash pop`) to see your stash.

**You'll know you're done when:** Your work-in-progress is restored on your feature branch.

---

## Exercise 7 — Explore History with git log and git diff 🔴 Moderate

**Goal:** Use `git log` and `git diff` to investigate the repo's history like a detective.

**No new file needed — you'll explore the repo itself.**

**Steps:**
1. Run `git log --oneline` — how many commits are in this repo?
2. Run `git log --oneline --graph` — can you see where branches were created or merged?
3. Pick a commit hash from the log. Run `git show <hash>` to see exactly what changed in that commit
4. Run `git diff HEAD~1 HEAD` — compare the most recent commit to the one before it
   - `HEAD` means "my current commit", `HEAD~1` means "one commit before that"
5. Run `git log --oneline --author="<someone's name>"` to filter commits by author
6. Run `git log --oneline sandbox/` to see only commits that touched the sandbox folder

**Bonus:** Run `git log --oneline --since="1 week ago"` — useful for catching up after time off.

**You'll know you're done when:** You can answer: _"What changed in the most recent commit, and who made it?"_
