#    MTUOC-TMX2TSV
#    Erstellt 2025 von Antoni Oliver, angepasst für Lehrzwecke von M. Kappus
#
#    Dieses Programm ist freie Software unter der GNU General Public License v3.
#    Es konvertiert alle TMX-Dateien in einem Verzeichnis in tabulatorgetrennte Dateien (.tsv).

import argparse
import xml.etree.ElementTree as ET
import sys
import codecs
import os

def tmx2tsv_dir(inputdir, outputdir):
    """Konvertiert alle TMX-Dateien in einem Verzeichnis in TSV-Dateien"""
    os.makedirs(outputdir, exist_ok=True)

    for root, dirs, files in os.walk(inputdir):
        for file in files:
            if file.endswith(".tmx"):
                file_path = os.path.join(root, file)
                print(f"Verarbeite {file_path} ...")

                try:
                    tree = ET.parse(file_path)
                    tmx_root = tree.getroot()

                    # Namespace bereinigen (optional)
                    ns = {'xml': 'http://www.w3.org/XML/1998/namespace'}

                    # TSV-Dateiname vorbereiten
                    outname = os.path.splitext(file)[0] + ".tsv"
                    outfile = os.path.join(outputdir, outname)

                    with codecs.open(outfile, "w", "utf-8") as out:
                        out.write("source_text\ttarget_text\n")

                        for tu in tmx_root.iter("tu"):
                            segs = []
                            for tuv in tu.findall("tuv"):
                                seg = tuv.find("seg")
                                if seg is not None and seg.text:
                                    segs.append(seg.text.strip())

                            # nur Paare schreiben
                            if len(segs) == 2:
                                out.write(f"{segs[0]}\t{segs[1]}\n")

                    print(f"✅ {outfile} erstellt")

                except Exception as e:
                    print(f"⚠️  Fehler in {file_path}: {e}")
                    continue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Konvertiert TMX-Dateien in einem Verzeichnis in tabulatorgetrennte Textdateien.')
    parser.add_argument('-d', '--dir', required=True, help='Eingabeverzeichnis mit TMX-Dateien')
    parser.add_argument('-o', '--out', required=False, default="tsv_out", help='Ausgabeverzeichnis für TSV-Dateien')
    args = parser.parse_args()

    tmx2tsv_dir(args.dir, args.out)
