#!/usr/bin/env python3
"""
Lädt eine Liste von URLs herunter und speichert deren Texte in einer einzigen Datei
oder in einem Zielordner, in der Reihenfolge der Linkliste.
"""

import subprocess
from pathlib import Path
import sys

def main():
    if len(sys.argv) < 3:
        print("Verwendung: python3 crawl_trafilatura.py <linkliste.txt> <zielordner>")
        sys.exit(1)

    linkliste = Path(sys.argv[1])
    zielordner = Path(sys.argv[2])
    zielordner.mkdir(parents=True, exist_ok=True)

    gesamtausgabe = zielordner / "alle_texte.txt"

    # Alte Datei löschen, falls vorhanden
    if gesamtausgabe.exists():
        gesamtausgabe.unlink()

    with open(linkliste, encoding="utf-8") as f:
        for i, url in enumerate(f, start=1):
            url = url.strip()
            if not url:
                continue
            print(f"[{i}] Lade {url} ...")

            # Text mit trafilatura abrufen
            try:
                result = subprocess.run(
                    ["trafilatura", "-u", url],
                    capture_output=True, text=True, check=True
                )
                text = result.stdout.strip()
            except subprocess.CalledProcessError as e:
                print(f"⚠️ Fehler bei {url}: {e}")
                continue

            # Ausgabe an eine Sammeldatei anhängen
            with open(gesamtausgabe, "a", encoding="utf-8") as out:
                out.write(f"== {url} ==\n{text}\n\n")

    print(f"\n✅ Fertig! Alle Texte gespeichert in: {gesamtausgabe}")

if __name__ == "__main__":
    main()
