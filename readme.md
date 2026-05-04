# Welcome to `git-school`!

![XKCD Git Comic](./img/git_xkcd.png)

_Credit: XKCD, https://xkcd.com/1597/_

## What is This?

`git-school` is Summit's hands-on introduction to `git` and GitHub. By the end of this course you will have:

- A working SSH key for authenticating with Summit's GitHub Organization
- A conceptual understanding of how `git` works
- Hands-on experience with the core git workflow used on Summit projects
- Completed a real Pull Request in this repo as a capstone exercise

## Why Git?

Software can be a very tricky thing to get exactly right. One line of bad code can cause an entire website or product to
crash unexpectedly. Using a **version control** system helps mitigate those issues by creating parallel branches and
save points that can always be returned to if a critical failure occurs. It also creates a history of the code that
tells the story of how and why changes were made. Most critically, it encourages collaboration through code review as
changes are merged together into a main branch that results in a deliverable product.

Git is one of the most widely used version control systems in the world and is the default on GitHub and GitLab.
Since Summit uses GitHub to host its repositories, this course teaches you the fundamentals so you can follow best
practices for software development from day one.

## Course Modules

Work through these in order:

| Module | Topic |
|---|---|
| [Module 1](./01_setup.md) | Setup — install git, configure SSH, clone this repo |
| [Module 2](./02_concepts.md) | Git Concepts — distributed version control and branching |
| [Module 3](./03_workflow.md) | Git Workflow — branches, commits, and the staging area |
| [Module 4](./04_merge_conflicts.md) | Merge Conflicts — pulling branches and resolving conflicts |
| [Module 5](./05_pull_requests.md) | Pull Requests — pushing, opening PRs, and code review |
| [Module 6](./06_useful_commands.md) | Useful Commands — `.gitignore`, `git log`, `git diff`, `git stash` |

## Capstone Exercise

Once you've completed the modules, sign the yearbook by going through the full
workflow: create a branch, edit [yearbook.md](./yearbook.md), commit, push, and open a Pull Request into `main`.

_Don't see a yearbook.md? Ask your facilitator — it may be set up as a separate exercise branch._

## Other Resources

### This Repo
- [CONTRIBUTING.md](./CONTRIBUTING.md) — how to contribute improvements to this repo

### Interactive Practice
- [Learn Git Branching](https://learngitbranching.js.org) — the best visual, interactive git sandbox available; great for understanding branching and rebasing
- [GitHub Skills](https://skills.github.com) — guided, hands-on courses that run directly inside GitHub (official)
- [Oh My Git!](https://ohmygit.org) — a card-based game for learning git; good for absolute beginners

### Reference & Reading
- [Official git docs](https://git-scm.com/docs) — comprehensive reference for every git command
- [Pro Git (free book)](https://git-scm.com/book/en/v2) — the definitive git book, free online; chapters 1–3 are especially relevant for this course
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) — well-written tutorials on everything from basics to advanced workflows
- [Conventional Commits](https://www.conventionalcommits.org) — a widely used standard for writing consistent, readable commit messages

### Cheat Sheets
- [GitHub Git Cheat Sheet (PDF)](https://education.github.com/git-cheat-sheet-education.pdf) — one-page reference for the most common commands
- [Atlassian Git Cheat Sheet (PDF)](https://www.atlassian.com/dam/jcr:e7e22f25-bba2-4ef1-a197-53f46b6df4a5/SWTM-2088_Atlassian-Git-Cheatsheet.pdf) — alternative one-pager with workflow diagrams

---