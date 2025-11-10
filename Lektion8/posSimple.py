import spacy

# Sprachmodell laden
nlp = spacy.load("de_core_news_sm")

# Beispieltext
text = "Die Studentin liest einen Artikel über Sprachdaten."
doc = nlp(text)

# Ausgabe Wort + Wortart
for token in doc:
    print(token.text, token.pos_)
