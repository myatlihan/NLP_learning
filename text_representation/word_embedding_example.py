import pandas as pd
import numpy as np
import re 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from gensim.models import Word2Vec, FastText
from gensim.utils import simple_preprocess

import nltk
from nltk.corpus import stopwords

df = pd.read_csv('archive/IMDB_Dataset.csv')

#yorumları alıyoruz
comments = df['review']

#İngilizce stopwordları liste olarak alıyoruz.
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))



def clean_text(text):
    #Metni küçük harflere çeviriyoruz
    text = text.lower()

    #Sayıları kaldırıyoruz
    text = re.sub(r'\d+', '', text)

    #Özel karakterleri kaldırıyoruz
    text = re.sub('[^\w\s]', '', text)

    #Tokenization ve stopwords kurtulma
    tokens = text.split()
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [token for token in tokens if len(token) > 2]

    #Tokenları birleştirip text haline getirme
    cleaned_text = (' ').join(tokens)

    return cleaned_text

#yorumları yazdığımız fonksiyonla temizle
cleaned_comments = [clean_text(comment) for comment in comments]

#Toknization
tokenize_comments = [simple_preprocess(comment) for comment in cleaned_comments]

#Word2Vec model
Word2Vec_model = Word2Vec(
    sentences=tokenize_comments,
    vector_size=50,
    window=5,
    sg=0,
    min_count=1
)

#Trainden sonra oluşan kelime vektörleri
word_vectors = Word2Vec_model.wv
#İlk 500 kelime
words = list(word_vectors.index_to_key)[:500]
vectors = [word_vectors[w] for w in words]

kmeans = KMeans(n_clusters=2)
kmeans.fit(vectors)
cluster_labels = kmeans.labels_


#pca ile boyut indigime 50d => 2d
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)


plt.figure(figsize=(12,8))

plt.scatter(
    reduced_vectors[:,0],
    reduced_vectors[:,1],
    c=cluster_labels
)

for i, word in enumerate(words):
    plt.annotate(
        word,
        (reduced_vectors[i,0],
         reduced_vectors[i,1])
    )

plt.title('Word2Vec + KMeans')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')

plt.show()