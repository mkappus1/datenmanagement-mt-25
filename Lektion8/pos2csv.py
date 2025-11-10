#!/usr/bin/env python3
"""
Liest eine Textdatei ein, analysiert sie mit spaCy
und schreibt die Wortarten (PoS-Tags) in eine CSV-Datei.
"""

import csv
import spacy
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Verwendung: python3 pos_to_csv.py <textdatei>")
        sys.exit(1)

    dateipfad = Path(sys.argv[1])
    if not dateipfad.exists():
        print(f"❌ Datei nicht gefunden: {dateipfad}")
        sys.exit(1)

    nlp = spacy.load("de_core_news_sm")

    text = dateipfad.read_text(encoding="utf-8")
    doc = nlp(text)

    csv_datei = dateipfad.with_suffix(".pos.csv")

    with open(csv_datei, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["Token", "POS", "Tag"])
        for token in doc:
            writer.writerow([token.text, token.pos_, token.tag_])

    print(f"✅ CSV-Datei erstellt: {csv_datei}")

if __name__ == "__main__":
    main()
