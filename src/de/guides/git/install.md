# Installation

Sie können überprüfen, ob Git auf Ihrem System bereits installiert ist, indem Sie den folgenden Befehl ausführen:

```sh
git version
```

Die Ausgabe sollte ähnlich wie folgt sein:

```plaintext
git version 2.43.1
```

Wenn Sie einen Fehler wie `git: Befehl nicht gefunden` erhalten, können Sie den folgenden Anweisungen folgen, um Git zu installieren.

## Installation unter Windows

Die Installation von `git` unter Windows ist unkompliziert.

1. Laden Sie den Installer von der [offiziellen Webseite](https://git-scm.com/download/win) herunter.
2. Führen Sie den Installer aus und folgen Sie den Anweisungen.
3. Nach der Installation können Sie das Terminal öffnen und `git version` ausführen, um zu überprüfen, ob die Installation erfolgreich war.

???+ Tipp
    Unter Windows 10 oder später können Sie auch WSL nutzen, das Ihnen erlaubt, Linux auf Windows auszuführen. Dies ermöglicht es Ihnen, in einer Linux-Umgebung zu sein, während Sie Windows verwenden.

???+ Hinweis
    Wählen Sie bei der `Anpassung Ihrer PATH-Umgebung` die Option `Git von der Kommandozeile und auch von Drittanbieter-Software`. Dies ermöglicht es Ihnen, `git` aus dem Windows-Terminal zu nutzen.
    Dieser Artikel geht davon aus, dass Sie dies getan haben. Andernfalls müssen Sie das Git Bash Terminal verwenden, das mit dem Installer geliefert wird, für die Befehle in diesem Guide.

## Installation unter macOS

Normalerweise ist `git` bereits auf macOS installiert. Aber falls es aus irgendeinem Grund nicht installiert ist, können Sie es entweder mit [Homebrew](#mit-homebrew) oder durch [Herunterladen des Installers](#mit-dem-installer) installieren.

### Mit Homebrew

Homebrew ist ein Paketmanager für macOS. Wenn Sie Homebrew installiert haben, können Sie `git` einfach installieren.

1. Öffnen Sie das Terminal und führen Sie den folgenden Befehl aus, um `git` zu installieren:

    ```sh
    brew install git
    ```

2. Nach der Installation können Sie `git version` ausführen, um zu überprüfen, ob die Installation erfolgreich war.

### Mit dem Installer

1. Laden Sie den neuesten [Installer](https://sourceforge.net/projects/git-osx-installer/files/git-2.23.0-intel-universal-mavericks.dmg/download?use_mirror=autoselect) herunter.
2. Führen Sie den Installer aus und folgen Sie den Anweisungen.
3. Nach der Installation können Sie die Installation überprüfen, indem Sie `git version` im Terminal ausführen.

## Installation unter Linux

Sie können `git` unter Linux mit dem Paketmanager Ihrer Distribution installieren.

### Debian/Ubuntu oder Derivate

```sh
sudo apt-get update
sudo apt-get install git
```

### Fedora oder Derivate

```sh
sudo dnf install git-all
```

### Arch Linux oder Derivate

```sh
sudo pacman -S git
```

Nach der Installation können Sie die Installation überprüfen, indem Sie `git version` im Terminal ausführen.

## Konfiguration

Die Installation von Git ermöglicht es Ihnen, Repositories zu klonen und Änderungen in Ihren Projekten zu verfolgen. Jedoch müssen Sie Git mit Ihren Anmeldedaten konfigurieren, bevor Sie Änderungen an ein entferntes Repository pushen können. Dies kann durch Ausführen der folgenden Befehle im Terminal geschehen:

```sh
git config --global user.email "you@example.com"
git config --global user.name "Ihr Name"
```

Sie können auch die `--global`-Flagge weglassen, um die Konfiguration für ein einzelnes Repository zu setzen. Dafür müssen Sie zu dem Repository navigieren und die gleichen Befehle ohne die `--global`-Flagge ausführen.

Von diesem Punkt an können Sie Git nutzen, um Änderungen in Ihrem Projekt zu verfolgen. Git wird Sie nach Ihren Anmeldedaten fragen, wenn Sie versuchen, Ihre Änderungen an ein entferntes Repository zu pushen. Sie können auch SSH-Schlüssel verwenden, um sich bei dem entfernten Repository zu authentifizieren. Dies ist nicht nur sicherer, sondern auch bequemer.

???+ Hinweis
    Wenn Sie GitHub verwenden, müssen Sie SSH-Schlüss

el verwenden, um sich bei dem entfernten Repository zu authentifizieren. GitHub hat die Unterstützung für Passwortauthentifizierung am 13. August 2021 entfernt.

### SSH-Schlüssel

Um einen SSH-Schlüssel zu erstellen, können Sie den folgenden Befehl im Terminal ausführen:

```sh
ssh-keygen -t ed25519 -C "ihre_email@example.com"
```

Dies erstellt einen neuen SSH-Schlüssel unter Verwendung der bereitgestellten E-Mail als Label. Sie können den Standarddateispeicherort bei der Frage akzeptieren. Sie können Ihrem SSH-Schlüssel auch ein Passwort hinzufügen, was für eine zusätzliche Sicherheitsebene empfohlen wird. Ohne Passwort wird der SSH-Schlüssel auf Ihrem Computer als Klartext gespeichert.

???+ Tipp
    Wenn ssh-keygen Sie fragt, ob die Datei überschrieben werden soll, bedeutet dies, dass Sie bereits in der Vergangenheit einen SSH-Schlüssel erstellt haben. Sie können entweder die Datei überschreiben oder einen neuen Dateinamen angeben. Um einen benutzerdefinierten SSH-Schlüssel zu erstellen, können Sie den Standarddateispeicherort eingeben und dann den Namen der neuen Datei.

Nachdem der SSH-Schlüssel generiert wurde, ist der nächste Schritt, ihn zu Ihrem entfernten Repository hinzuzufügen. Anleitungen für [GitHub](https://docs.github.com/de/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) und für [GitLab](https://docs.gitlab.com/ee/user/ssh.html#add-an-ssh-key-to-your-gitlab-account) sind in ihrer jeweiligen Dokumentation verfügbar.

Sie können den SSH-Schlüssel auch Ihrem SSH-Agenten hinzufügen, was Ihnen erlaubt, den Schlüssel zu nutzen, ohne jedes Mal das Passwort eingeben zu müssen. Dafür hat GitHub eine gute Anleitung, wie man [SSH-Schlüssel zum ssh-agent hinzufügt](https://docs.github.com/de/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
