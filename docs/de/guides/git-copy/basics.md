# Basics

In this guide, we will mostly use the command line to interact with Git. But all of these can also be done using a GUI tool like GitHub Desktop, GitKraken or even VS Code.

## Creating a Repository

There is couple of ways you can do this. You can create a new repository on GitHub with some initial files and then [clone](#clone) it to your local machine. Or you can create a new repository on your local machine and then publish it to GitHub. In VS Code press ++ctrl+shift+p++ or ++cmd+shift+p++ to open the command palette and type `Publish to GitHub` to create a new repository on GitHub.

![Create a new repository on GitHub](../../img/git/Creating-New-Repo.png)

## Clone

Cloning a repository means that you are making a copy of the repository on your local machine. This can be done by running the following command in the terminal:

```sh
git clone <repository-url>
```

???+ Tip
    If you want to use your SSH key for authentication, clone the repository using the SSH path. If you have already cloned the repository using HTTPS but want to use SSH for authentication, you can change the remote URL using the following command:

    ```sh
    git remote set-url origin <new-repository-url>
    ```

## Status

The `git status` command shows the status of the working directory and the staging area. It won't modify anything in your repository, it just shows you the current status like which files are staged, unstaged, or untracked.

## Add

The `git add` command adds changes in the working directory to the staging area effectively telling Git that you want to include updates to a particular file in the next commit.

To add specific files, you can run the following command:

```sh
git add <file>
```

To add all files, you can run the following command:

```sh
git add .
```

???+ Tip
    When you delete a file from a repository, you still need to run `git add` otherwise git won't be aware of the deletion.

## Commit

The `git commit` command is used to save changes to the local repository. It is like a snapshot of your repository at a particular point in time. But the changes are not yet on the remote repository.

To commit changes, you can run the following command:

```sh
git commit -m "commit message"
```

It's highly recommended to read about [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). It's a specification for adding human and machine readable meaning to commit messages.

## Push

The `git push` command is used to upload local repository content to a remote repository. It is used to make the commits you have made on your local repository online. It's recommended to [pull](#pull) the latest changes from the remote repository before pushing your changes. By doing so, you can resolve any conflicts before pushing your changes and reduce the chances of merge conflicts.

To push changes, you can run the following command:

```sh
git push
```

## Pull

The `git pull` command is used to update the local version of a repository from a remote. It can be done by running the following command:

```sh
git pull
```
