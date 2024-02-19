Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Commands
### git init

This command turns a directory into an empty Git repository. This is the first step in creating a repository. After running git init, adding and committing files/directories is possible.
### git add

Adds files in the to the staging area for Git. Before a file is available to commit to a repository, the file needs to be added to the Git index (staging area). There are a few different ways to use git add, by adding entire directories, specific files, or all unstaged files.
### git commit

Record the changes made to the files to a local repository. For easy reference, each commit has a unique ID.

It’s best practice to include a message with each commit explaining the changes made in a commit. Adding a commit message helps to find a particular change or understanding the changes.
### git status

This command returns the current state of the repository.

_git status_ will return the current working branch. If a file is in the staging area, but not committed, it shows with _git status_. Or, if there are no changes it’ll return _nothing to commit, working directory clean._
### git config

With Git, there are many configurations and settings possible. _git config_ is how to assign these settings. Two important settings are user user.name and user.email. These values set what email address and name commits will be from on a local computer. With _git config_, a _--global_ flag is used to write the settings to all repositories on a computer. Without a _--global_ flag settings will only apply to the current repository that you are currently in.

### git branch

To determine what branch the local repository is on, add a new branch, or delete a branch.
### git checkout

To start working in a different branch, use _git checkout_ to switch branches.
### git merge

Integrate branches together. _git merge_ combines the changes from one branch to another branch. For example, merge the changes made in a staging branch into the stable branch.
### git remote

To connect a local repository with a remote repository. A remote repository can have a name set to avoid having to remember the URL of the repository.
### git clone

To create a local working copy of an existing remote repository, use _git clone_ to copy and download the repository to a computer. Cloning is the equivalent of _git init_ when working with a remote repository. Git will create a directory locally with all files and repository history.
### git pull

To get the latest version of a repository run _git pull_. This pulls the changes from the remote repository to the local computer.
### git push

Sends local commits to the remote repository. _git push_ requires two parameters: the remote repository and the branch that the push is for.
### git stash

To save changes made when they’re not in a state to commit them to a repository. This will store the work and give a clean working directory. For instance, when working on a new feature that’s not complete, but an urgent bug needs attention.
### git log

To show the chronological commit history for a repository. This helps give context and history for a repository. _git log_ is available immediately on a recently cloned repository to see history.
example:
```bash
# Show entire git log 
$ git log
# Show git log with date pameters 
$ git log --<after/before/since/until>=<date>
# Show git log based on commit author 
$ git log --<author>="Author Name"
```

### git rm

Remove files or directories from the working index (staging area). With _git rm_, there are two options to keep in mind: force and cached. Running the command with force deletes the file. The cached command removes the file from the working index. When removing an entire directory, a recursive command is necessary.
### git fetch
git-fetch - Download objects and refs from another repository
Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated (see the description of <refspec> below for ways to control this behavior).

By default, any tag that points into the histories being fetched is also fetched; the effect is to fetch tags that point at branches that you are interested in. This default behavior can be changed by using the --tags or --no-tags options or by configuring remote.<name>.tagOpt. By using a refspec that fetches tags explicitly, you can fetch tags that do not point into branches you are interested in as well.