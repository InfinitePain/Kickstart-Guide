# Install

You can check if Git is installed on your system by running the following command:

```sh
git version
```

The output should be similar to this:

```plaintext
git version 2.43.1
```

If you get an error like `git: command not found`, you can fallow the instructions below to install Git.

## Installing on Windows

Installing `git` on Windows is straightforward

1. Download the installer from the [official website](https://git-scm.com/download/win).
2. Run the installer and follow the instructions.
3. After the installation is complete, you can open terminal and run `git version` to check if the installation was successful.

???+ Tip
    In Windows 10 or later, you can also use WSL which allows you to run a Linux on top of Windows. This allows you to be in a Linux environment while still using Windows.

???+ Note
    At the `Adjusting your PATH environment` choose `Git from the command line and also from 3rd-party software`. This will allow you to use `git` from the windows terminal.
    This article assumes that you have done this. Otherwise you will have to use the Git Bash terminal that comes with the installer for the commands in this guide.

## Installing on macOS

Usially `git` is already installed on macOS. But if it for some reason is not installed, you can install it either with [Homebrew](#using-homebrew) or by [downloading the installer](#using-the-installer).

### Using Homebrew

Homebrew is a package manager for macOS. If you have Homebrew installed, you can install `git` easily.

1. Open terminal and run the following command to install `git`:

    ```sh
    brew install git
    ```

2. After the installation is complete, you can run `git version` to verify that the installation was successful.

### Using the installer

1. Download the latest [installer](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect).
2. Run the installer and follow the instructions.
3. After the installation is complete. You can verify the installation by running `git version` in the terminal.

## Installing on Linux

You can install `git` on Linux using the package manager of your distribution.

### Debian/Ubuntu or derivatives

```sh
sudo apt-get update
sudo apt-get install git
```

### Fedora or derivatives

```sh
sudo dnf install git-all
```

### Arch Linux or derivatives

```sh
sudo pacman -S git
```

After the installation is complete, you can verify the installation by running `git version` in the terminal.

## Configuration

Installing git allows you to clone repositories and track changes in your projects. However, you need to configure git with your credentials before you can push changes to a remote repository. This can be done by running the following commands in the terminal:

```sh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

You can also omit the `--global` flag to set the configuration for a single repository. For that you need to navigate to the repository and run the same commands without the `--global` flag.

From this point on you can use git to track changes in your project. Git will ask you your credentials when you try to push your changes to a remote repository. You can also use SSH keys to authenticate with the remote repository. Which is not only more secure but also more convenient.

???+ Note
    If you are using GitHub, you have to use SSH keys to authenticate with the remote repository. GitHub has removed support for password authentication on August 13, 2021.

### SSH Keys

To create an SSH key, you can run the following command in the terminal:

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

This will create a new SSH key, using the provided email as a label. You can safely accept the default file location when asked. You can also add a passphrase to your SSH key for an extra layer of security. Which is recommended. Without a passphrase the ssh key will be stored in your computer as plain text.

???+ Tip
    If ssh-keygen asks you to overwrite the file this means that you already have created an SSH key in the past. You can either overwrite the file or provide a new file name. To create a custom-named SSH key you can type the default file location and then the name of the new file.

After generating the SSH key, the next step is adding it to your remote repository. Instructions for [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) and for [GitLab](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account) are available in their respective documentation.

You can also add the SSH key to your SSH agent which will allow you to use the key without having to enter the passphrase every time you use it. For that GitHub has a good guide on how to [add SSH key to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
