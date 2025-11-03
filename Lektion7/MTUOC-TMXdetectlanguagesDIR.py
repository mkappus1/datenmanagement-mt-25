import argparse
import xml.etree.ElementTree as ET
import sys
import os

def localname(tag: str) -> str:
    # entfernt Namespace-Präfixe: "{ns}tu" -> "tu"
    return tag.split('}', 1)[-1] if tag.startswith('{') else tag

def detectlanguagesDIR(direntrada):
    for root_dir, dirs, files in os.walk(direntrada):
        for file in files:
            if not file.lower().endswith(".tmx"):
                continue

            file_path = os.path.join(root_dir, file)
            langs = {}  # Sprachcodes + Counts pro Datei

            try:
                # Streaming-Parse (iterparse) mit Pfad
                context = ET.iterparse(file_path, events=("start", "end"))
                # ersten Event konsumieren (('start', root_elem))
                _, _root = next(context)

                for event, elem in context:
                    if event == "end" and localname(elem.tag) == "tu":
                        # alle tuv-Kinder ansehen
                        for tuv in elem.findall(".//*"):
                            if localname(tuv.tag) != "tuv":
                                continue
                            # xml:lang (mit Namespace) ODER plain lang lesen
                            lang = (
                                tuv.attrib.get('{http://www.w3.org/XML/1998/namespace}lang')
                                or tuv.attrib.get('lang')
                            )
                            if lang:
                                langs[lang] = langs.get(lang, 0) + 1
                        # Speicher freigeben bei grossen Dateien
                        elem.clear()

                if langs:
                    codes = ", ".join(f"{k} ({v})" for k, v in sorted(langs.items()))
                    print(f"Sprachen in {file}: {codes}")
                else:
                    print(f"⚠️  Keine Sprachcodes gefunden in {file} (evtl. andere Struktur/Attribute).")

            except Exception as e:
                print(f"ERROR in {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Erkennt Sprachcodes in allen TMX-Dateien eines Verzeichnisses.')
    parser.add_argument('-d', '--dir', dest='inputdir', required=True, help='Eingabeverzeichnis mit TMX-Dateien')
    args = parser.parse_args()
    detectlanguagesDIR(args.inputdir)
