# Welcome to `git-school`!

## Goal

The goal of `git-school` is to get you up and running with the following:

- a SSH key that you can use to authenticate into our GitLab server (rather than
  typing your username and password constantly)
- an account on our GitLab server
- a basic `git` workflow for coding collaboratively with other Summiteers

## Install `git`

To do any of this cool stuff, you need to install `git`:

- [ ] Download `git` here: https://git-scm.com/downloads
- [ ] You can follow all of the defaults during installation

Check that you successfully installed `git` by:

- [ ] Opening the `Git Bash` application
- [ ] In the `Git Bash` terminal that opens, issue this command: `git --version`
- [ ] If you do not have `Git Bash` installed or you get an error from
      `git --version`, you have a problem.

## Set up Secure Shell (SSH) Authentication

Each time you request resources from the GitLab server, you have to authenticate
yourself, proving that you have the permissions required to access that
resource. Most people do this via SSH rather than typing a username and
password in repeatedly:

### Generate SSH Key

- [ ] Generate an SSH keypair by executing the following command in `Git Bash`:
  - `ssh-keygen -t rsa -b 4096 -C "<your_email@example.com>"`
- [ ] Accept all of the defaults (press enter until you see a "randomart image"
      representing your new SSH keypair)
- [ ] Check for your new keypair in the following directory:
  - `/c/Users/<first.last>/.ssh/`
- [ ] You should see two new files:
  - `id_rsa` is your new private key - DO NOT share this with anyone
  - `id_rsa.pub` is your new public key - you will place this on the GitLab
    server, under your account settings, to authenticate against (with your
    private key, hence "keypair") - note: Windows attempts to associate the
    `.pub` extension with Microsoft Publisher. Ignore this.

### Associate Public Key with GitLab Account

- [ ] Go to the desired GitLab server (typically http://f3-git.summit.local/)
- [ ] If you don't already have one, create an account
- [ ] Click on your avatar &rarr; `Settings` &rarr; `SSH Keys`
- [ ] Back in Windows Explorer, open your public key in a text editor
  - [ ] Right-click on `id_rsa.pub` &rarr; 'Open With' &rarr; 'Notepad',
        for example
- [ ] Copy the entire contents of your public key into the 'Key' section of
      the SSH Key
- [ ] Click 'Add key'

### Clone a Project (this one!) to Test Everything So Far

- [ ] Go to the GitLab page for this project:
      http://f3-git.summit.local/data-science-team/git-school.
- [ ] Copy the SSH URL for the project, which is located just underneath the
      title, `git-school` - ensure it says `SSH`, not `HTTP`, just to the left
      of the URL
- [ ] In `Git Bash`, navigate to the directory where you want to create your
      local copy of this project (I recommend your Documents folder,
      `C:/Users/<first.last>/Documents`)
  - [ ] `cd ~/Documents`
- [ ] Clone the project with
      `git clone git@f3-git.summit.local:data-science-team/git-school.git`

You should have a copy of the project files in
`C:/Users/<first.last>/Documents/git-school`.

## Git Workflow

Now you are ready to contribute to the project, but you need to understand the
`git` workflow. As always, you should read the [docs](https://git-scm.com/docs),
but I will explain the main commands you need to be familiar with below. This
list is not exhaustive, nor will some of the commands make sense until you have
used them a few times:

- `git branch` - list the branches in your local repository, with an asterisk
  on the branch that you have checked out
- `git branch <new_branch>` - create a new branch, named `<new_branch>`
- `git checkout <branch_to_checkout>` - checks out the branch named
  `<branch_to_checkout>`
- `git status` - shows the working tree status, i.e. the changes you've made
  since your last commit
- `git add <file1> <file2>` - add changed files `file1` and `file2` to the
  "staging area" so you can commit them
  - You can use `git add -A` to add all changed files rather than typing them
    out individually
- `git commit -m "<commit message>"` -
