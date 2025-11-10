#!/usr/bin/env python3
"""
Liest eine Textdatei ein, analysiert sie mit spaCy
und schreibt die Wortarten (PoS-Tags) in eine neue Textdatei.
"""

import spacy
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Verwendung: python3 pos_to_txt.py <textdatei>")
        sys.exit(1)

    dateipfad = Path(sys.argv[1])

    if not dateipfad.exists():
        print(f"❌ Datei nicht gefunden: {dateipfad}")
        sys.exit(1)

    # Sprachmodell laden (Deutsch)
    nlp = spacy.load("de_core_news_sm")

    # Textdatei lesen
    with open(dateipfad, "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    # Name der Ausgabedatei erzeugen
    ausgabe_datei = dateipfad.with_suffix(".pos.txt")

    # Ausgabe in Datei schreiben
    with open(ausgabe_datei, "w", encoding="utf-8") as out:
        out.write(f"PoS-Tagging für Datei: {dateipfad.name}\n\n")
        out.write(f"{'Token':15} {'POS':10} {'Tag':10}\n")
        out.write("-" * 40 + "\n")
        for token in doc:
            out.write(f"{token.text:15} {token.pos_:10} {token.tag_}\n")

    print(f"✅ Ergebnis gespeichert in: {ausgabe_datei}")

if __name__ == "__main__":
    main()
