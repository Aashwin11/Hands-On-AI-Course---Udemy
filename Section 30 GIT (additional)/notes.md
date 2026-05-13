<h1 align="center">🧠 Git & GitHub — Complete Command Reference</h1>
<h3 align="center">📖 A structured, beginner-to-advanced guide to mastering Git workflows</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Version%20Control-Mastery-00D9FF?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100" />
  <img src="https://user-images.githubusercontent.com/74038190/212257460-738ff738-247f-4445-a718-cdd0ca76e2db.gif" width="100" />
  <img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7763.gif" width="100" />
</p>

---

## 📑 Table of Contents

| #   | Topic                                                  |
| --- | ------------------------------------------------------ |
| 1   | [git --version](#1-git---version)                      |
| 2   | [git init](#2-git-init)                                |
| 3   | [git status](#3-git-status)                            |
| 4   | [git commit](#4-git-commit)                            |
| 5   | [git log](#5-git-log)                                  |
| 6   | [git config](#6-git-configuration)                     |
| 7   | [.gitignore](#7-gitignore)                             |
| 8   | [Git Branches](#8-git-branches)                        |
| 9   | [git diff](#9-git-diff)                                |
| 10  | [Git Stashing](#10-git-stashing)                       |
| 11  | [git rebase](#11-git-rebase)                           |
| 12  | [Git Remote & Push](#12-pushing-code--git-remote)      |
| 13  | [git clone, fetch & pull](#13-git-cloning-fetch--pull) |

---

## 1. `git --version`

> Shows the installed version of Git.

```bash
git --version
```

---

## 2. `git init`

> Initializes Git in a directory — run **once per project**.

```bash
git init
```

- Creates a hidden `.git` folder that tracks the entire history of all files and sub-folders.
- To view hidden files: `ls -la`
- ⚠️ **Never manually modify** anything inside the `.git` folder.

---

## 3. `git status`

> Shows the current tracking status of your working directory.

```bash
git status
```

---

## 4. `git commit`

> A **checkpoint** — saves a snapshot of your staged changes.

### 🔄 The Git Workflow

```
📝 Write Code
    ↓
git add .          →  📦 STAGING AREA (changes queued, not yet saved)
    ↓
git commit -m ""   →  🏛️ LOCAL REPO (saved checkpoint)
    ↓
git push           →  ☁️ GITHUB (published online)
```

> 💡 **Every commit requires a message** and is linked to its parent commit, forming a chain.

### 📋 Example Commit History

```
7efb691 (HEAD -> main)  added the gitignore file       ← PARENT points to → null
e832c4a                 add second file to codebase    ← PARENT points to → 7efb691
4053e8c                 Add file 1
f3f07af (origin/main)   Initial commit
```

```bash
# Stage all changes
git add .

# Commit with a message
git commit -m "your message here"

# Add and commit in one step
git commit -am "your message here"
```

---

## 5. `git log`

> Displays the history of commits.

```bash
# Full log
git log

# Compact one-line log
git log --oneline
```

---

## 6. Git Configuration

> Configure Git globally (system-wide) or locally (per project). Settings saved in `.gitconfig`.

```bash
# Set your username
git config --global user.name "Your Name"

# Set your email
git config --global user.email "you@example.com"

# Set VS Code as the default editor
git config --global core.editor "code --wait"
```

> 💡 **VS Code Setup:** Press `Ctrl+Shift+P` → type `code` → select **"Install 'code' command in PATH"**

---

## 7. `.gitignore`

> A file that tells Git which files/folders to **never track**.

```bash
# Example .gitignore entries
.env
node_modules/
*.log
secrets.yaml
```

- Commonly used to hide **API keys**, credentials, and environment-specific files.
- 🔍 Use a **gitignore generator** (search online) to auto-generate one for your stack.

---

## 8. Git Branches

> Branches let you work on features independently without affecting the main codebase.

### 🌿 Branch Commands

```bash
# List all branches (* marks current branch)
git branch

# Create a new branch
git branch <branch-name>

# Switch to a branch
git checkout <branch-name>
git switch <branch-name>          # modern syntax

# Create AND switch in one step
git switch -c <branch-name>
git checkout -b <branch-name>

# Rename current branch
git branch -M <new-branch-name>

# Delete a branch
git branch -d <branch-name>
```

> ⚠️ **Always commit before switching branches.**

---

### 🔀 Merging Branches

```bash
# Run this FROM the branch you want to merge INTO
git merge <branch-to-merge-from>
```

| Merge Type              | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| ⚡ **Fast Forward**     | Feature branch worked alone; main had no new commits. Clean, linear history. |
| 🔁 **Non Fast Forward** | Both branches had new commits. Creates a merge commit.                       |

### ⚔️ Merge Conflicts

When Git can't auto-resolve differences, a conflict occurs:

```
<<<<<<< HEAD  (🟢 YOUR current branch)
  your changes here
=======
  incoming changes here
>>>>>>> feature-branch  (🔵 branch being merged in)
```

> - 🟢 **Green** = changes on your current branch
> - 🔵 **Blue** = changes coming from the branch being merged

---

## 9. `git diff`

> Shows the differences between file versions across time, commits, or branches.

```bash
# Diff working directory vs last commit
git diff

# Diff staged changes
git diff --staged

# Diff between two commits
git diff <commit_id_1> <commit_id_2>
git diff <commit_id_1>..<commit_id_2>    # same result

# Diff between two branches
git diff branchOne..branchTwo
```

### 📖 How to Read Diff Output

```diff
--- a/filename    ← Version A (older)
+++ b/filename    ← Version B (newer)

- removed line    ← line deleted
+ added line      ← line added
```

---

## 10. Git Stashing

> Temporarily shelves changes so you can switch branches **without committing**.

```bash
# Stash current changes
git stash

# List all stashes
git stash list

# Re-apply the most recent stash
git stash pop

# Apply a specific stash by ID
git stash apply stash@{0}
```

> ✅ Stashed changes **can be applied to a different branch** than where they were stashed.  
> ⚠️ **Do not rely on stash too heavily** — commit regularly instead.

---

### 🔁 Useful Restore & Navigation Commands

```bash
# Restore a file to its last committed state
git restore <filename>

# Jump HEAD to a specific commit (detached HEAD state)
git checkout <HASH>

# Navigate relative to HEAD
git checkout HEAD~<number>    # e.g., HEAD~2 = 2 commits back

# Return to main branch (easiest way back)
git checkout main

# View full history of HEAD movements
git reflog
```

---

## 11. `git rebase`

> An **alternative to merging** — replays commits onto another branch for a cleaner, linear history. Also used as a **cleanup tool** for commits.

```bash
# Rebase current branch onto another
git rebase <target-branch>
```

> ⚠️ **CAUTION:** Never rebase on the `main` / `master` branch. Only use on feature branches.

When a conflict occurs during rebase, Git will pause and show:

```
CONFLICT (content): Merge conflict in <filename>
# After resolving:
git rebase --continue
# To abort:
git rebase --abort
```

---

## 12. Pushing Code & Git Remote

> **Git** is the software. **GitHub** is the online service to host Git repositories.

```bash
# Check if a remote repo is configured
git remote -v
```

**Example output:**

```
origin  https://github.com/username/repo (fetch)
origin  https://github.com/username/repo (push)
```

```bash
# Connect a remote repository
git remote add origin https://github.com/username/repo.git

# Rename a remote
git remote rename oldName newName

# Remove a remote
git remote remove <name>

# Push and set upstream (first time)
git push -u origin main

# Push after upstream is set
git push
```

> 🔐 **Tip:** Set up **SSH keys** for a secure, password-free connection to GitHub.

---

## 13. Git Cloning, Fetch & Pull

### 📥 Clone a Repository

```bash
git clone <url>
```

> When you clone a repo, **only the main branch is locally tracked**. Other remote branches exist but are not auto-configured locally.

---

### `git fetch` vs `git pull`

| Command     | What it does                                                                  |
| ----------- | ----------------------------------------------------------------------------- |
| `git fetch` | Downloads changes from remote but **does NOT update** your working directory  |
| `git pull`  | Downloads changes from remote **AND merges** them into your working directory |

```bash
# Pull from a specific branch
git pull origin <branch-name>
```

---

<div align="center">

### 🚀 Quick Reference Cheat Sheet

| Command                    | Description                |
| -------------------------- | -------------------------- |
| `git init`                 | Initialize a repo          |
| `git status`               | Check file status          |
| `git add .`                | Stage all changes          |
| `git commit -m ""`         | Commit with message        |
| `git log --oneline`        | Compact commit history     |
| `git branch`               | List branches              |
| `git switch -c <name>`     | Create & switch branch     |
| `git merge <branch>`       | Merge a branch             |
| `git stash`                | Shelve uncommitted changes |
| `git rebase <branch>`      | Rebase onto branch         |
| `git push -u origin main`  | Push & set upstream        |
| `git pull origin <branch>` | Pull remote changes        |
| `git clone <url>`          | Clone a repository         |

</div>

---

<div align="center">

_Happy committing! Remember: commit early, commit often._ 🎯

![Git](https://img.shields.io/badge/Made%20with-Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Markdown](https://img.shields.io/badge/Formatted%20in-Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)

</div>
