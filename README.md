# OSWC-Semesteraufgabe

## Beschreibung
Unser Semesteraufgabe für das Modul Betriebssysteme und Web-Computing. Eine TODO-List in Python als CGI-Script.

## Ziele
- [Three tier architecture](https://www.youtube.com/watch?v=n4J30QEFjDk)
- [Software Tests](https://www.youtube.com/watch?v=DhUpxWjOhME&t=115s)


## Deployment
Wir verwenden für das testen Docker.

### Build
Zum bauen wird folgender Commad benutzt (Im Verzeichnis mit dem Dockerfile): `sudo docker build -t cgi .`

### Testing
Commad um Ergebnis zu testen:
`sudo docker run -dit -p 8080:80 cgi; firefox http://localhost:8080/cgi/presentation_layer/index.cgi`

### Debuging 
Um im Docker Fehler zu suchen folgendes ausführen: `sudo docker run -it cgi bash`
Besonders hilfreich für debuging war `/usr/sbin/apache2` auszuführen.
Und `docker ps` braucht man auch sehr oft.

## Unittest

Im Repo Ordner: `python3 -m tests.test_todo_database`