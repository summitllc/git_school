# Module 1: Setup

Before you can use `git`, you need to install it, configure SSH authentication, and clone this repo.

## Install `git`

- [ ] Download `git` here: https://git-scm.com/downloads
- [ ] You can follow all of the defaults during installation

Check that you successfully installed `git` by:

- [ ] Opening the `Git Bash` application
- [ ] In the `Git Bash` terminal that opens, issue this command: `git --version`
- [ ] If you do not have `Git Bash` installed, or if you get an error from
      `git --version`, you have a problem.

_Minor Note:_ Any of the git commands below will work in any command line shell where git is available. This includes command prompt (cmd), PowerShell, or Bash on a linux machine. For this tutorial, we will assume you are using Git Bash.

## Configure Your Identity

Before you can make your first commit, git needs to know who you are. This information
gets attached to every commit you make — it's how the project history shows who changed what.

Run these two commands in Git Bash, substituting your real name and Summit email:

```
git config --global user.name "First Last"
git config --global user.email "first.last@summitllc.us"
```

You only need to do this once per machine. To verify it was set correctly:

```
git config --global user.name
git config --global user.email
```

## Set up Secure Shell (SSH) Authentication

Each time you request resources from Summit's GitHub Organization, you have to authenticate
yourself, proving that you have the permissions required to access that
resource. Most people do this via SSH rather than typing a username and
password in repeatedly:

### Generate SSH Key

- [ ] Generate an SSH keypair by executing the following command in `Git Bash`:
  - `ssh-keygen -t ed25519 -C "<your_email@example.com>"`
- [ ] Accept all of the defaults (press enter until you see a "randomart image"
      representing your new SSH keypair)
- [ ] Check for your new keypair in the following directory:
  - `/c/Users/<first.last>/.ssh/`
- [ ] You should see two new files:
  - `id_ed25519` is your new private key - DO NOT share this with anyone
  - `id_ed25519.pub` is your new public key - you will place this in your GitHub
    account, to authenticate against (with your private key, hence "keypair")

### Associate Public Key with GitHub Account

- [ ] Log into your GitHub account that is associated with Summit's Git Organization.
  - [ ] If you don't have an account on GitHub, first create an account.
  - [ ] After the account has been created, reach out to the IT Department to have them invite you to Summit's Organization.
    - GitHub recommends having one account to manage both your personal and professional projects. There are easy methods of removing yourself from your organization after you leave Summit.
  - [ ] Enable 2FA after joining Summit's organization.
- [ ] Click on your avatar &rarr; `Settings` &rarr; `SSH and GPG keys`
- [ ] Back in File Explorer, open your public key in a text editor
  - [ ] Right-click on `id_ed25519.pub` &rarr; `Open With` &rarr; `Notepad`, for example
- [ ] In GitHub, click `New SSH key`.
- [ ] Paste the contents of `id_ed25519.pub` into the text box under "Key".
- [ ] Add a title to this key.
  - Something descriptive like `YYYYMMDD_Summit_laptop` works well.
- [ ] Click "Add SSH key"
  - Note for people who use multiple accounts: The same SSH Key cannot be used by multiple accounts, i.e. you cannot use a key on your personal account _and_ your work account. It is possible to use multiple keys on a single computer, but this approach is not recommended for most users.

### Clone This Repo to Test Everything So Far

- [ ] Go to the GitHub page for this project:
      https://github.com/summitllc/git_school.
- [ ] Copy the SSH URL for the project by selecting the green `<> Code` button above the file explorer box, then selecting the SSH tab. The URL takes the form `git@github.com:<owner of repo>/<name of repo>.git`
- [ ] In `Git Bash`, navigate to the directory where you want to create your
      local copy of this project (I recommend your Documents folder):
  - [ ] `cd ~/Documents`
- [ ] Clone the project:
      `git clone <url you copied in previous step>`

  - If you get the message below, answer `yes` to continue:
  ```
    Cloning into 'git_school'...
    The authenticity of host 'github.com (20.201.28.151)' can't be established.
    ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
    This key is not known by any other names
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

You should now have a copy of the project files in `C:/Users/<first.last>/Documents/git_school`.

---

**Next:** [Module 2 - Git Concepts](./02_concepts.md)
