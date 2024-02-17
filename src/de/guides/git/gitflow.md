# Gitflow

Gitflow ist ein Branching-Modell, das für das Management der Entwicklung eines Projekts verwendet wird. Sie haben es wahrscheinlich in verschiedenen Open-Source-Projekten gesehen. Es ist im Grunde ein Satz von Regeln, der definiert, wie Branches erstellt und zusammengeführt werden, um die Entwicklung eines Projekts zu managen. Es besteht aus zwei Komponenten: den Hauptbranches und den unterstützenden Branches.

![Gitflow](../../img/git/Gitflow.png)

## Die Hauptbranches

Die Hauptbranches sind die Branches, die verwendet werden, um die Veröffentlichung des Projekts zu managen. Sie sind:

1. `main`-Branch: Dies ist der Branch, der die offizielle Veröffentlichung des Projekts enthält.
2. `develop`-Branch: Dies ist der Branch, der die neueste Entwicklung des Projekts enthält und verwendet wird, um die Veröffentlichung des Projekts zu erstellen. Hier kommen alle neuen Features zusammen und werden getestet, bevor sie veröffentlicht werden.

## Die unterstützenden Branches

Die unterstützenden Branches sind die Branches, die verwendet werden, um neue Features zu entwickeln und Bugs zu beheben. Sie sind:

1. `feature`-Branch: Dies ist der Branch, der zur Entwicklung neuer Features verwendet wird. Er wird vom `develop`-Branch abgezweigt und zurück in den `develop`-Branch gemerged, wenn das Feature fertig ist.
2. `release`-Branch: Dies ist der Branch, der zur Vorbereitung der Veröffentlichung des Projekts verwendet wird. Der Zweck dieses Branches ist es, die Entwicklung neuer Features zu stoppen und Bugs zu beheben. Er wird vom `develop`-Branch abgezweigt und zurück in den `main`-Branch gemerged, wenn die Veröffentlichung abgeschlossen ist.
3. `hotfix`-Branch: Dies ist der Branch, der zur Behebung von Bugs in der Veröffentlichung verwendet wird. Er wird vom `main`-Branch abgezweigt und zurück in den `main`-Branch gemerged, wenn der Bug behoben ist.

## Der Workflow

Stellen wir uns ein Szenario vor, in dem wir ein Projekt haben, das entwickelt wird. Das Projekt hat die folgenden Branches:

1. `main`-Branch
2. `develop`-Branch

### Ein Feature erstellen/beenden

Wir möchten ein neues Feature für das Projekt entwickeln. Zuerst erstellen wir einen neuen Branch namens `feature-my-feature` vom `develop`-Branch.

```bash
# Erstelle einen neuen Branch namens feature-my-feature vom develop-Branch
git checkout -b feature-my-feature develop
```

Nachdem wir die Entwicklung des Features abgeschlossen haben, mergen wir den `feature-my-feature`-Branch zurück in den `develop`-Branch.

```bash
# Merge den feature-my-feature-Branch in den develop-Branch
git checkout develop
git merge --no-ff feature-my-feature
git branch -d feature-my-feature
```

???+ Tipp
    Der letzte Befehl ist optional, aber empfohlen. Er löscht den `feature-my-feature`-Branch, nachdem er in den `develop`-Branch gemerged wurde. Keine Sorge, die Änderungen sind immer noch im `develop`-Branch. Wir möchten nur unsere Branches sauber halten.

### Eine Veröffentlichung erstellen/beenden
 
... Nach einiger Zeit erreichen wir einen Punkt, an dem wir das Projekt veröffentlichen möchten. In dieser Phase ist es entscheidend, wie wir unsere Veröffentlichungen versionieren. Hier kommt Semantic Versioning (SemVer) ins Spiel. SemVer ist ein Versionierungsschema für Software, das durch die Versionsnummer selbst Bedeutung über die zugrunde liegenden Änderungen in einer Veröffentlichung vermitteln soll. Es ist formatiert als `MAJOR.MINOR.PATCH`, wobei:

- **MAJOR**-Versionen inkompatible API-Änderungen anzeigen,
- **MINOR**-Versionen Funktionalität auf eine rückwärtskompatible Weise hinzufügen, und
- **PATCH**-Versionen rückwärtskompatible Bugfixes enthalten.

Für detailliertere Informationen zu SemVer und seinen Regeln besuchen Sie [semver.org](https://semver.org/).

Nun, um unser Projekt für die Veröffentlichung vorzubereiten, erstellen wir

 einen neuen Branch namens `release-1.0` vom `develop`-Branch. Die Versionsnummer `1.0` sollte den SemVer-Richtlinien folgen, was darauf hindeutet, dass dies unsere erste stabile Veröffentlichung mit einem Satz von fertiggestellten Features ist.

```bash
# Erstelle einen neuen Branch namens release-1.0 vom develop-Branch
git checkout -b release-1.0 develop
./bump-version.sh 1.0
git commit -a -m "chore(release): bump version number to 1.0"
```

Das `bump-version.sh`-Skript ist ein imaginäres Skript, das wir verwenden, um die Versionsnummer des Projekts zu erhöhen. Nachdem wir die Veröffentlichung vorbereitet haben, mergen wir den `release-1.0`-Branch zurück in den `main`-Branch.

```bash
git checkout main
git merge --no-ff release-1.0
# Tagge die Veröffentlichung
git tag -a 1.0
# Merge auch den develop-Branch, um ihn auf dem neuesten Stand mit der Veröffentlichung zu halten
git checkout develop
git merge --no-ff release-1.0
git branch -d release-1.0
```

???+ Tipp
    Der letzte Befehl ist optional, aber empfohlen. Er löscht den `release-1.0`-Branch, nachdem er in den `main`-Branch gemerged wurde. Keine Sorge, die Änderungen sind immer noch im `main`-Branch. Wir möchten nur unsere Branches sauber halten.

### Einen Bug in der Veröffentlichung beheben

Nachdem wir die Version 1.0 unseres Projekts veröffentlicht haben, entdecken wir einen Bug, der sofort behoben werden muss. Es ist auch wichtig, sich an die SemVer-Prinzipien zu halten. Wenn der Bugfix rückwärtskompatibel ist und keine neuen Features einführt, sollte er die PATCH-Version erhöhen. Wenn wir beispielsweise einen Bug in Version `1.0` beheben, wäre die Hotfix-Version `1.0.1`.

```bash
# Erstelle einen neuen Branch namens hotfix-1.0.1 vom main-Branch
git checkout -b hotfix-1.0.1 main
./bump-version.sh 1.0.1
git commit -a -m "chore(release): bump version number to 1.0.1"
```

Nachdem wir den Bug behoben haben, mergen wir den `hotfix-1.0.1`-Branch zurück in den `main`-Branch.

```bash
git checkout main
git merge --no-ff hotfix-1.0.1
# Tagge die Veröffentlichung
git tag -a 1.0.1
# Merge auch den develop-Branch, um ihn auf dem neuesten Stand mit dem main zu halten
git checkout develop
git merge --no-ff hotfix-1.0.1
git branch -d hotfix-1.0.1
```

???+ Tipp
    Der letzte Befehl ist optional, aber empfohlen. Er löscht den `hotfix-1.0.1`-Branch, nachdem er in den `main`-Branch gemerged wurde. Keine Sorge, die Änderungen sind immer noch im `main`-Branch. Wir möchten nur unsere Branches sauber halten.
