import os
import spacy

nlp = spacy.load("en_core_web_sm")
wiki_path = "../beautifuls/text_files"
wikis = [f for f in os.listdir(wiki_path) if f.endswith('.txt')]

for wiki in wikis:
    with open(os.path.join(wiki_path, wiki), 'r', encoding='utf-8') as w:
        text = w.read()


doc = nlp(text)
print(f"doc for nlp ==> {len(doc)}")
print(f"doc for nlp ==> {len(text)}")

for token in text.split()[:10]:
    print(token)
print("___________________________")
for token in doc[:10]:
    print(token)

for sent in doc.sents[:20]:
    print(sent)