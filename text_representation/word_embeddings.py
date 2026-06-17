# ============================================================
# WORD EMBEDDINGS
# ============================================================
#
# Word Embedding, kelimeleri sayılarla temsil etme yöntemidir.
#
# Amaç:
# Kelimelerin anlamlarını matematiksel olarak ifade edebilmek.
#
# Bag of Words ve TF-IDF yöntemlerinde:
#
# "king"  -> [0, 1, 0, 0, 0]
# "queen" -> [0, 0, 1, 0, 0]
#
# şeklinde temsil yapılır.
#
# Bu yöntemlerde kelimeler arasındaki anlam ilişkileri yoktur.
#
# Örneğin:
#
# king ve queen
#
# anlam olarak birbirine yakın olmasına rağmen
# vektörleri tamamen bağımsızdır.
#
# ============================================================
# WORD EMBEDDING FİKRİ
# ============================================================
#
# Her kelimeyi sabit uzunlukta yoğun (dense) bir vektör ile
# temsil ederiz.
#
# Örnek:
#
# king  -> [0.82, -0.15, 0.44, 0.93]
# queen -> [0.79, -0.12, 0.41, 0.89]
#
# Görüldüğü gibi benzer anlamdaki kelimeler
# birbirine yakın vektörlere sahip olur.
#
# ============================================================
# DENSE VECTOR
# ============================================================
#
# Dense = Yoğun vektör
#
# TF-IDF:
#
# [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
#
# Çok fazla sıfır içerir.
#
# Word Embedding:
#
# [0.34, -0.22, 0.81, 0.56]
#
# Çoğu değer doludur.
#
# Bu nedenle Dense Representation denir.
#
# ============================================================
# SEMANTIC MEANING (ANLAMSAL BİLGİ)
# ============================================================
#
# Word Embedding'in en önemli özelliği:
#
# Benzer anlamlı kelimeler yakın konumlarda bulunur.
#
# Örnek:
#
# cat
# dog
# puppy
#
# birbirine yakın olabilir.
#
# car
# truck
# bus
#
# başka bir bölgede kümelenebilir.
#
# ============================================================
# CONTEXT (BAĞLAM)
# ============================================================
#
# Word Embedding modelleri bir kelimenin anlamını
# çevresindeki kelimelere bakarak öğrenir.
#
# Örnek:
#
# "The cat is sleeping."
# "The dog is sleeping."
#
# cat ve dog benzer bağlamlarda geçtiği için
# benzer vektörler öğrenilir.
#
# Bu NLP'nin temel varsayımlarından biridir.
#
# "A word is known by the company it keeps."
#
# Bir kelimenin anlamı komşularından anlaşılır.
#
# ============================================================
# WORD2VEC
# ============================================================
#
# En popüler Word Embedding yöntemlerinden biridir.
#
# Google tarafından geliştirilmiştir.
#
# İki temel mimarisi vardır:
#
# 1) CBOW (Continuous Bag of Words)
# 2) Skip-Gram
#
# ============================================================
# CBOW
# ============================================================
#
# Çevredeki kelimeleri kullanarak
# ortadaki kelimeyi tahmin etmeye çalışır.
#
# Örnek:
#
# "I love ___ very much"
#
# Model:
#
# I
# love
# very
# much
#
# kelimelerine bakarak
#
# "football"
#
# kelimesini tahmin etmeye çalışır.
#
# ============================================================
# SKIP-GRAM
# ============================================================
#
# Tam tersi çalışır.
#
# Merkez kelime verilir.
#
# Çevredeki kelimeler tahmin edilir.
#
# Örnek:
#
# "football"
#
# verildiğinde:
#
# love
# play
# game
# team
#
# gibi komşu kelimeler tahmin edilmeye çalışılır.
#
# ============================================================
# EMBEDDING DIMENSION
# ============================================================
#
# Her kelime belirli boyutta bir vektöre dönüştürülür.
#
# Örnek:
#
# 50 Boyut
# 100 Boyut
# 200 Boyut
# 300 Boyut
#
# king ->
#
# [0.25, -0.82, 0.11, ...]
#
# 300 elemanlı olabilir.
#
# ============================================================
# COSINE SIMILARITY
# ============================================================
#
# İki kelimenin ne kadar benzer olduğunu
# ölçmek için kullanılır.
#
# Sonuç:
#
# 1'e yakınsa -> çok benzer
# 0'a yakınsa -> ilgisiz
# -1'e yakınsa -> zıt yönlü
#
# Örnek:
#
# similarity(cat, dog) = 0.91
#
# similarity(cat, car) = 0.12
#
# ============================================================
# WORD EMBEDDING AVANTAJLARI
# ============================================================
#
# 1) Anlamsal ilişkileri öğrenebilir.
#
# 2) Boyut sayısı düşüktür.
#
# 3) Dense temsil kullanır.
#
# 4) Benzer kelimeleri yakınlaştırır.
#
# 5) NLP modellerinin performansını artırabilir.
#
# ============================================================
# WORD EMBEDDING DEZAVANTAJLARI
# ============================================================
#
# 1) Eğitim maliyeti vardır.
#
# 2) Her kelime için tek vektör üretir.
#
# Örnek:
#
# bank
#
# hem:
#
# banka
#
# hem:
#
# nehir kıyısı
#
# anlamına gelebilir.
#
# Ama Word2Vec genellikle tek bir vektör üretir.
#
# Bu problem daha sonra:
#
# BERT
# ELMo
# RoBERTa
#
# gibi Contextual Embedding modelleriyle çözülmüştür.
#
# ============================================================
# ÖZET
# ============================================================
#
# Bag of Words:
# Kelime sayıları
#
# TF-IDF:
# Kelime önemi
#
# Word Embedding:
# Kelime anlamı + Kelime ilişkileri
#
# Modern NLP sistemlerinin temel taşlarından biridir.
#
# ============================================================

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec, FastText
from gensim.utils import simple_preprocess


documents = [
    'Köpek çok tatlı bir hayvandır.',
    'Köpekler evcil hayvanlardır.',
    'Kediler genellikle bağımsız hareket etmeyi severler.',
    'Hayvanlar insanlar için iyi arkadaştırlar.',
    "Türkiye'nin başkenti Ankaradır.",
    "Türkiye'de Ankara ve Gaziantep'in yemekleri çok güzeldir."
    ]

tokennize_sentence = [simple_preprocess(w) for w in documents]


Word2Vec_model = Word2Vec(
    sentences= tokennize_sentence,
    vector_size=50,
    window=5,
    min_count=1,
    sg=0 #CBOW=0 Skip-Gram=1 , burada yapacağımız tercihle bağlamdan kelimeyi ya da kelimeden bağlamı bulmayı seçiyoruz
)


FastText_model = FastText(
    sentences=tokennize_sentence,
    vector_size=50,
    window=5,
    min_count=1,
    sg=0
)



def plot_word_embedings(model, title):

    word_vectors =model.wv
    words = list(word_vectors.index_to_key)
    vectors = [word_vectors[w] for w in words]
    pca = PCA(n_components=3)
    reduced_vectors = pca.fit_transform(vectors)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(reduced_vectors[:, 0],
               reduced_vectors[:, 1],
               reduced_vectors[:, 2])
    
    for i, word in enumerate(words):
        ax.text(
        reduced_vectors[i, 0],
        reduced_vectors[i, 1],
        reduced_vectors[i, 2],
        word
        )   

    ax.set_title(title)
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    ax.set_zlabel('Component 3')
    plt.show()


plot_word_embedings(Word2Vec_model, 'Word2Vec Graph')