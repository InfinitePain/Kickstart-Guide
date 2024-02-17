# Gitflow

Gitflow is a branching model that is used for managing the development of a project. You have probably seen it in various open-source projects. It's bascially a set of rules that define how branches are created and merged in order to manage the development of a project. It is consist of two components, the main branches and the supporting branches.

![Gitflow](../../img/git/Gitflow.png)

## The Main Branches

The main branches are the branches that are used to manage the release of the project. They are:

1. `main` branch: This is the branch that contains the official release of the project.
2. `develop` branch: This is the branch that contains the latest development of the project and used to create the release of the project.It is where all the new features come together and are tested before they are released.

## The Supporting Branches

The supporting branches are the branches that are used to develop new features and fix bugs. They are:

1. `feature` branch: This is the branch that is used to develop new features. It is branched off from the `develop` branch and merged back into the `develop` branch when the feature is complete.
2. `release` branch: This is the branch that is used to prepare the release of the project. The purpose of this branch is to stop the development of new features and fix bugs. It is branched off from the `develop` branch and merged back into the `main` branch when the release is complete.
3. `hotfix` branch: This is the branch that is used to fix bugs in the release. It is branched off from the `main` branch and merged back into the `main` branch when the bug is fixed.

## The Workflow

Let's think of a scenario where we have a project that is being developed. The project has the following branches:

1. `main` branch
2. `develop` branch

### Creating/Finishing a Feature

We want to develop a new feature for the project. First, we create a new branch called `feature-my-feature` from the `develop` branch.

```bash
# Create a new branch called feature-my-feature from the develop branch
git checkout -b feature-my-feature develop
```

After we have finished developing the feature, we merge the `feature-my-feature` branch back into the `develop` branch.

```bash
# Merge the feature-my-feature branch into the develop branch
git checkout develop
git merge --no-ff feature-my-feature
git branch -d feature-my-feature
```

???+ Tip
    The last command is optional but recommended. It deletes the `feature-my-feature` branch after it has been merged into the `develop` branch. Don't worry, the changes are still there in the `develop` branch. We just want to keep our branches clean.

### Creating/Finishing a Release

... After some time, we reach a point where we want to release the project. At this stage, it's crucial to consider how we version our releases. This is where Semantic Versioning (SemVer) comes into play. SemVer is a versioning scheme for software that aims to convey meaning about the underlying changes in a release through the version number itself. It is formatted as `MAJOR.MINOR.PATCH`, where:

- **MAJOR** versions indicate incompatible API changes,
- **MINOR** versions add functionality in a backwards-compatible manner, and
- **PATCH** versions include backwards-compatible bug fixes.

For more detailed information on SemVer and its rules, visit [semver.org](https://semver.org/).

Now, to prepare our project for release, we create a new branch called `release-1.0` from the `develop` branch. The version number `1.0` should follow the SemVer guidelines, indicating this is our first stable release with a set of completed features.

```bash
# Create a new branch called release-1.0 from the develop branch
git checkout -b release-1.0 develop
./bump-version.sh 1.0
git commit -a -m "chore(release): bump version number to 1.0"
```

The `bump-version.sh` script is an imaginary script that we use to bump the version number of the project. After we have finished preparing the release, we merge the `release-1.0` branch back into the `main` branch.

```bash
git checkout main
git merge --no-ff release-1.0
# Tag the release
git tag -a 1.0
# Also Merge develop branch to keep it up to date with the release
git checkout develop
git merge --no-ff release-1.0
git branch -d release-1.0
```

???+ Tip
    The last command is optional but recommended. It deletes the `release-1.0` branch after it has been merged into the `main` branch. Don't worry, the changes are still there in the `main` branch. We just want to keep our branches clean.

### Fixing a Bug in the Release

After releasing version 1.0 of our project, we discovered a bug that needs to be addressed immediately. It's also important to adhere to SemVer principles. If the bug fix is backward compatible and doesn’t introduce new features, it should increment the PATCH version. For instance, if we're fixing a bug in version `1.0`, the hotfix version would be `1.0.1`.

```bash
# Create a new branch called hotfix-1.0.1 from the main branch
git checkout -b hotfix-1.0.1 main
./bump-version.sh 1.0.1
git commit -a -m "chore(release): bump version number to 1.0.1"
```

After we have fixed the bug, we merge the `hotfix-1.0.1` branch back into the `main` branch.

```bash
git checkout main
git merge --no-ff hotfix-1.0.1
# Tag the release
git tag -a 1.0.1
# Also Merge develop branch to keep it up to date with the main
git checkout develop
git merge --no-ff hotfix-1.0.1
git branch -d hotfix-1.0.1
```

???+ Tip
    The last command is optional but recommended. It deletes the `hotfix-1.0.1` branch after it has been merged into the `main` branch. Don't worry, the changes are still there in the `main` branch. We just want to keep our branches clean.
