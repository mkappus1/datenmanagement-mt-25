# 🔗 Browser-Erweiterungen zur Link-Extraktion

Um aus Webseiten oder Sitemaps Listen mit URLs zu erstellen, können Sie verschiedene Browser-Erweiterungen verwenden.  
Diese Tools helfen Ihnen, alle Links einer Seite sichtbar zu machen und als Textdatei zu exportieren.  
Im Folgenden finden Sie eine Übersicht über die gängigsten Optionen für verschiedene Browser.

---

## 🦊 Firefox: Link Gopher

- **Name:** [Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)  
- **Funktion:** Extrahiert alle Links (oder gefilterte) aus der aktuellen Seite, kann sie sortieren, filtern und als Text exportieren.  
- **Besonderheit:** Funktioniert auch mit XML-Sitemaps.  
- **Empfehlung:** Ideal für Lehrzwecke, da es sehr transparent arbeitet und keine Programmierkenntnisse erfordert.

**Add-on-Seite:** [addons.mozilla.org/en-US/firefox/addon/link-gopher/](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)

---

## 🌐 Google Chrome / Microsoft Edge: Link Grabber

- **Name:** [Link Grabber](https://chrome.google.com/webstore/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma)  
- **Funktion:** Listet alle auf einer Webseite gefundenen Links in einem neuen Tab auf.  
- **Export:** Kopieren oder Speichern als Text möglich.  
- **Einschränkung:** Keine Filter oder Sortierfunktionen wie bei Link Gopher.  
- **Verfügbarkeit:** Läuft auch unter Edge, da Edge auf Chromium basiert.

**Chrome Web Store:** [chrome.google.com/webstore/detail/link-grabber/](https://chrome.google.com/webstore/detail/link-grabber/)

---

## 🍎 Safari: Alternativen

Safari erlaubt technisch weniger tiefgreifende Erweiterungen als Firefox oder Chrome.  
Es gibt aber einige praktikable Alternativen:

### a) [Scraper for Safari](https://apps.apple.com/app/scraper/id6443440169)
- **Beschreibung:** Ermöglicht das Extrahieren bestimmter HTML-Elemente oder Links aus einer Seite.  
- **Einsatzgebiet:** Funktioniert ähnlich wie Link Gopher, ist aber etwas technischer.  
- **Ideal für:** Fortgeschrittene Nutzerinnen und Nutzer, die gezielt bestimmte Linktypen (z. B. nur Artikel oder PDFs) sammeln möchten.

### b) Manuell über den Seitenquelltext
- Öffnen Sie in Safari den Quelltext einer Seite über  
  `Darstellung → Seitenquelltext einblenden` oder **⌥⌘U (Alt–Cmd–U)**.  
- Suchen Sie im Quelltext nach `href="https://` – so finden Sie alle eingebetteten Links.  
- Diese können Sie kopieren und mit einem Texteditor (z. B. BBEdit oder Visual Studio Code) weiterverarbeiten.

### c) Nutzung externer Tools oder Online-Dienste
Wenn Sie keine Erweiterung installieren möchten, können Sie externe Tools verwenden, z. B.:

- **Trafilatura** (Kommandozeilen-Tool)  
- **wget** oder **curl**  
- **Online-Link-Extractor:** [https://tools.webdevpuneet.com/extract-urls-from-webpage](https://tools.webdevpuneet.com/extract-urls-from-webpage)

Dort geben Sie einfach die URL einer Webseite ein und erhalten alle enthaltenen Links als Liste.

---

## 🧩 Vergleichsübersicht

| Browser | Erweiterung / Methode | Export als Text | Bemerkung |
|----------|----------------------|------------------|------------|
| **Firefox** | [Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/) | ✅ | Vollständiger Funktionsumfang, beste Wahl für den Unterricht |
| **Chrome / Edge** | [Link Grabber](https://chrome.google.com/webstore/detail/link-grabber/caodelkhipncidmoebgbbeemedohcdma) | ✅ | Einfache Bedienung, keine Filter |
| **Safari** | [Scraper App](https://apps.apple.com/app/scraper/id6443440169) oder Quelltext anzeigen | ⚙️ Teilweise | Weniger komfortabel, aber möglich |
| **Alternative für alle Browser** | [Online-Link-Extractor](https://tools.webdevpuneet.com/extract-urls-from-webpage) oder **Trafilatura** | ✅ | Ideal, wenn keine Erweiterung installiert werden kann |


