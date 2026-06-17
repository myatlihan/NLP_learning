from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords


stop_words = set(stopwords.words('english'))
documents = [
    'natural language processing involves understating human language',
    'Artificial intelligence encopmasses machine learning and natural language',
]


vectorizer = CountVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

kelime_kümesi = [kelime for kelime in vectorizer.get_feature_names_out() if kelime not in stop_words]
kelime_vektörü = doc_vectors.toarray()
print(kelime_kümesi)
print(kelime_vektörü)