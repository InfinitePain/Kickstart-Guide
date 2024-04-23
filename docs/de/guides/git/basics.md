# Grundlagen

In diesem Guide werden wir hauptsächlich die Kommandozeile verwenden, um mit Git zu interagieren. All dies kann jedoch auch mit einem GUI-Tool wie GitHub Desktop, GitKraken oder sogar VS Code durchgeführt werden.

## Ein Repository erstellen

Es gibt mehrere Wege, dies zu tun. Sie können ein neues Repository auf GitHub mit einigen Anfangsdateien erstellen und es dann auf Ihren lokalen Rechner [klonen](#klonen). Oder Sie können ein neues Repository auf Ihrem lokalen Rechner erstellen und es dann auf GitHub veröffentlichen. In VS Code drücken Sie ++ctrl+shift+p++ oder ++cmd+shift+p++, um die Befehlspalette zu öffnen und geben `Publish to GitHub` ein, um ein neues Repository auf GitHub zu erstellen.

![Ein neues Repository auf GitHub erstellen](../../img/git/Creating-New-Repo.png)

## Clone

Ein Repository zu clonen bedeutet, dass Sie eine Kopie des Repositories auf Ihrem lokalen Rechner anlegen. Dies kann durch Ausführen des folgenden Befehls im Terminal geschehen:

```sh
git clone <repository-url>
```

???+ Tip
    Wenn Sie Ihren SSH-Schlüssel zur Authentifizierung verwenden möchten, klonen Sie das Repository mit dem SSH-Pfad. Wenn Sie das Repository bereits mit HTTPS geklont haben, aber SSH zur Authentifizierung verwenden möchten, können Sie die Remote-URL mit dem folgenden Befehl ändern:

    ```sh
    git remote set-url origin <new-repository-url>
    ```

## Status

Der Befehl `git status` zeigt den Status des Arbeitsverzeichnisses und des Staging-Bereichs an. Er verändert nichts in Ihrem Repository, zeigt Ihnen nur den aktuellen Status an, wie welche Dateien gestaged, nicht gestaged oder nicht verfolgt werden.

## Add

Der Befehl `git add` fügt Änderungen im Arbeitsverzeichnis zum Staging-Bereich hinzu und teilt Git effektiv mit, dass Sie Updates einer bestimmten Datei im nächsten Commit einschließen möchten.

Um spezifische Dateien hinzuzufügen, können Sie den folgenden Befehl ausführen:

```sh
git add <file>
```

Um alle Dateien hinzuzufügen, können Sie den folgenden Befehl ausführen:

```sh
git add .
```

???+ Tip
    Wenn Sie eine Datei aus einem Repository löschen, müssen Sie trotzdem `git add` ausführen, sonst wird git sich der Löschung nicht bewusst.

## Commit

Der Befehl `git commit` wird verwendet, um Änderungen im lokalen Repository zu speichern. Es ist wie ein Snapshot Ihres Repositories zu einem bestimmten Zeitpunkt. Aber die Änderungen sind noch nicht im Remote-Repository.

Um Änderungen zu commiten, können Sie den folgenden Befehl ausführen:

```sh
git commit -m "commit message"
```

Es wird dringend empfohlen, sich über [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) zu informieren. Es ist eine Spezifikation, um Commit-Nachrichten menschen- und maschinenlesbare Bedeutung hinzuzufügen.

## Push

Der Befehl `git push` wird verwendet, um Inhalte des lokalen Repositories auf ein Remote-Repository hochzuladen. Er wird verwendet, um die Commits, die Sie in Ihrem lokalen Repository gemacht haben, online zu stellen. Es wird empfohlen, die neuesten Änderungen aus dem Remote-Repository [pullen](#pull), bevor Sie Ihre Änderungen pushen. Dadurch können Sie Konflikte lösen, bevor Sie Ihre Änderungen pushen und die Chancen auf Merge-Konflikte reduzieren.

Um Änderungen zu pushen, können Sie den folgenden Befehl ausführen:

```sh
git push
```

## Pull

Der Befehl `git pull` wird verwendet, um die lokale Version eines Repositories von einem Remote zu aktualisieren. Dies kann durch Ausführen des folgenden Befehls geschehen:

```sh
git pull
```
