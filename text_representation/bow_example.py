import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from collections import Counter 
import re 
import numpy as np




df = pd.read_csv('/home/yasin/Masaüstü/AI/NLP/text_representation/archive/IMDB_Dataset.csv')
stop_words = set(stopwords.words('english'))
stop_words.add('br')
def clean_text(text):
    text = text.lower()
    text = text.strip()
    tokens = text.split()
    tokens = [token for token in tokens if token not in stop_words]
    text = (' ').join(tokens)
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'[^\w\s\d+]', '', text)
    return text

df['review'] = df['review'].apply(clean_text)


vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(df['review'][:100])
vocabulary = vectorizer.get_feature_names_out() 


word_counts = Counter(vocabulary)

#bow_matrix = vectorizer.fit_transform(df['review'])

word_counts = pd.DataFrame({
    'word': vocabulary,
    'count': bow_matrix.sum(axis=0).A1
})

word_counts = word_counts.sort_values(
    by='count',
    ascending=False
)

print(word_counts.head(20))

print(bow_matrix.toarray())
print(vocabulary[1086])