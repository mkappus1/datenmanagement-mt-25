# erste_anfrage.py
# Dieses Skript lädt eine Webseite herunter
# und zeigt Informationen zur Antwort an.

import requests   # Modul zum Herunterladen von Webseiten

# URL festlegen
url = "https://www.python.org"

# Webseite herunterladen
response = requests.get(url)

#  Statuscode anzeigen
print("Statuscode:", response.status_code)

# Ersten Teil des HTML-Codes anzeigen
print("\nErste 500 Zeichen der Webseite:")
print(response.text[:500])
