import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from collections import Counter 
import re 

df = pd.read_csv(r'text_representation/archive/spam.csv', encoding='ISO-8859-1')

message = df['v2']

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = text.strip()
    text = re.sub('[^a-zA-Z\s]', '', text)
    tokens = [
        token
        for token in text.split() 
        if token not in stop_words
    ]

    text = (' ').join(tokens)
    

    return text

sms = [clean_text(text) for text in message]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(sms[:20])
vocabulary =  vectorizer.get_feature_names_out()


df_tfidf = pd.DataFrame(tfidf_matrix.toarray(),
                        columns=vocabulary)


row = df_tfidf.iloc[3]

print(row.sort_values(ascending=False).head(10))


