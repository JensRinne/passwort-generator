# Passwort Generator

Ein sicheres, interaktives Python-Tool zur schnellen Generierung von Passwörtern mit individuellen Einstellungen (Länge, Zeichentypen, HIBP-Prüfung usw.).

## Features
- Interaktives Terminal-Menü mit Auswahl aller Parameter
- Generierung mehrerer Passwörter auf einmal
- Optionaler HIBP-Leak-Check ("Have I Been Pwned")
- Komfortable Bedienung per Doppelklick oder Kommandozeile

## Voraussetzungen
- Python 3.7 oder neuer
- Die Pakete `requests` und `argparse` (argparse ist ab Python 3.2 Standard)

## Installation der Abhängigkeiten

Installiere das benötigte Paket mit:

```
pip install requests
```

## Nutzung

1. Starte das Skript per Doppelklick oder im Terminal:

```
python passwort_generator.py
```

2. Folge den Anweisungen im Menü und wähle die gewünschten Optionen.

3. Die generierten Passwörter werden angezeigt und können einfach kopiert werden.

## Automatische Installation von requirements.txt

Optional: Das Skript kann so erweitert werden, dass es beim Start prüft, ob eine `requirements.txt` im gleichen Verzeichnis liegt und die Pakete automatisch installiert. (Siehe unten)

---

## Hinweise
- Die HIBP-Prüfung benötigt eine Internetverbindung.
- Die Passwörter werden nicht gespeichert.
- Das Skript funktioniert auf Windows, Linux und macOS.
