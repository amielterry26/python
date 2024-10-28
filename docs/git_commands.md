# Essential Git Commands for Software Engineers

## 1. Setup and Configuration
- `git init`: Initialize a new Git repository in the current directory.
- `git clone <url>`: Clone a remote repository to your local machine.
- `git config --global user.name "<Your Name>"`: Set your Git username globally.
- `git config --global user.email "<Your Email>"`: Set your Git email globally.
- `git config --list`: Display current Git configuration settings.

## 2. Basic Workflow
- `git add <file>`: Stage specific files for commit.
- `git add .`: Stage all changes in the current directory.
- `git commit -m "message"`: Commit staged changes with a message.
- `git status`: Show the current status of the repository (staged, unstaged, untracked files).
- `git log`: View the commit history.
- `git diff`: Show changes between the working directory and the index (unstaged changes).
- `git diff --staged`: Show changes between the index and the last commit (staged changes).

## 3. Branching and Merging
- `git branch <branch-name>`: Create a new branch.
- `git checkout <branch-name>`: Switch to a different branch.
- `git checkout -b <branch-name>`: Create and switch to a new branch.
- `git merge <branch-name>`: Merge a branch into the current branch.
- `git branch -d <branch-name>`: Delete a local branch.
- `git branch -D <branch-name>`: Force delete a local branch (useful if there are unmerged changes).

## 4. Remote Repositories
- `git remote add origin <url>`: Add a remote repository (e.g., GitHub, GitLab).
- `git remote -v`: Show existing remotes.
- `git push origin <branch-name>`: Push changes from a local branch to a remote repository.
- `git pull origin <branch-name>`: Fetch and merge changes from a remote branch into your local branch.
- `git fetch`: Download changes from a remote repository without merging.

## 5. Stashing Changes
- `git stash`: Save (stash) uncommitted changes temporarily.
- `git stash list`: List all stashed changes.
- `git stash apply`: Apply the most recent stash without deleting it.
- `git stash pop`: Apply the most recent stash and delete it.
- `git stash drop`: Delete a specific stash.

## 6. Undoing Changes
- `git checkout -- <file>`: Discard changes in a file.
- `git reset <file>`: Unstage a file while keeping changes in the working directory.
- `git reset --soft <commit>`: Move the HEAD to a specific commit, keeping staged changes.
- `git reset --hard <commit>`: Move the HEAD to a specific commit and discard all changes.
- `git revert <commit>`: Create a new commit that undoes changes from a specific commit (safe for shared repositories).

## 7. Viewing and Comparing
- `git show <commit>`: Show details of a specific commit.
- `git log --oneline --graph --decorate`: View a summarized, graphical log.
- `git diff <branch1> <branch2>`: Show differences between two branches.

## 8. Collaboration and Tagging
- `git tag <tag-name>`: Create a tag for the current commit.
- `git push origin <tag-name>`: Push a specific tag to the remote.
- `git push --tags`: Push all tags to the remote repository.

## 9. Cleaning Up
- `git clean -fd`: Remove untracked files and directories.
- `git gc`: Clean up unnecessary files and optimize the local repository.

## 10. Additional Commands for Troubleshooting
- `git reflog`: View the history of changes to HEAD, useful for recovery.
- `git blame <file>`: View who made changes to each line in a file.
- `git cherry-pick <commit>`: Apply a commit from one branch to the current branch.

## Summary Cheatsheet

```plaintext
# Configuring Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Basic Workflow
git init
git clone <url>
git add .
git commit -m "Your message"
git push origin <branch>

# Branching and Merging
git branch <branch>
git checkout <branch>
git merge <branch>

# Undoing Changes
git checkout -- <file>
git reset --hard <commit>

# Remote Repositories
git fetch
git pull
git push

# Stashing
git stash
git stash apply