def detectlanguagesDIR(direntrada):
    langs = {}
    for root, dirs, files in os.walk(direntrada):
        for file in files:
            if file.endswith(".tmx"):
                file_path = os.path.join(root, file)
                try:
                    print(file)
                    context = ET.iterparse(file_path, events=("start", "end"))
                    root_elem = next(context)  # Get the root element
                    langs = {}

                    for event, elem in context:
                        if event == "end" and elem.tag == "tu":
                            for tuv in elem.findall("tuv"):
                                lang = tuv.attrib.get('{http://www.w3.org/XML/1998/namespace}lang')
                                if lang:
                                    langs[lang] = langs.get(lang, 0) + 1
                    # Ausgabe pro Datei
                    print(f"Sprachen in {file}: {', '.join(langs.keys())}")

                except Exception as e:
                    print(f"ERROR in {file_path}: {e}")
                        
    # Optional: Zusammenfassung aller Sprachen
    print("\n--- Alle erkannten Sprachcodes ---")
    for l in langs:
        print(l)
