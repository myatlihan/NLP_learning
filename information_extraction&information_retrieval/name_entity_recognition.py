import spacy
import pandas as pd

nlp_model = spacy.load('en_core_web_sm')

sentence = 'Alice works at Amazon and lives in London. She visited the British Museum last weekend'

doc = nlp_model(sentence)


entities_list = [(entity.text, entity.label_, entity.lemma_) for entity in doc.ents]
df = pd.DataFrame(entities_list, columns=['text', 'label', 'lemma'],)

print(df)