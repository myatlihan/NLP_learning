from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd


document = [
    'Köpek ve kuş aynı anda beslenebilir',
    'Çok çeşit köpek ırkı vardır',
    'Aynı anda birden fazla köpek beslenebilir',
    'Irk köpeklere özgü bir kavram değildir'
]


vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(document)
vocabulary = vectorizer.get_feature_names_out()
print((vocabulary))
print(tfidf_matrix)

df = pd.DataFrame (tfidf_matrix.toarray(),columns=vocabulary)
print(df)

mean_tfidf = df.mean(axis=0)

print(mean_tfidf)
