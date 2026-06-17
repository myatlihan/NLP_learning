# ==========================================================
# N-GRAM MODELS
# ==========================================================
#
# N-Gram, bir metindeki ardışık N kelimelik dizileri ifade eder.
#
# Unigram (N=1):
#   ["makine", "öğrenmesi", "veri"]
#
# Bigram (N=2):
#   [("makine","öğrenmesi"),
#    ("öğrenmesi","veri")]
#
# Trigram (N=3):
#   [("makine","öğrenmesi","veri")]
#
# Amaç:
#   Önceki N-1 kelimeyi kullanarak sonraki kelimenin
#   olasılığını tahmin etmektir.
#
# Örnek:
#   "Bugün hava çok ..."
#
# Bigram modeli:
#   P(güzel | çok)
#
# Trigram modeli:
#   P(güzel | hava, çok)
#
# N-Gram modelleri NLP'de:
#   - Language Modeling
#   - Next Word Prediction
#   - Text Generation
#   - Speech Recognition
#   - Machine Translation
#
# Avantajlar:
#   - Basit ve hızlıdır.
#   - Dil modellemenin temelini öğretir.
#
# Dezavantajlar:
#   - Uzun bağlamı hatırlayamaz.
#   - Veri seyrekliği (Data Sparsity) problemi yaşar.
#
# Modern alternatifler:
#   - RNN
#   - LSTM
#   - GRU
#   - Transformer
#   - BERT
#   - GPT
#
# Temel olasılık:
#
#   P(w_n | w_(n-1))
#
# Bigram için:
#
#   P(w_n | w_(n-1))
#   = Count(w_(n-1), w_n) / Count(w_(n-1))
#
# ==========================================================



raw_text = '''
Machine learning models learn from data.  
Machine learning models improve with data.  
Machine learning models generalize from patterns.  
Data science uses data to build models.  
Models learn patterns from data and improve performance.  
Neural networks learn patterns from data.  
Neural networks improve learning with more data.
'''  

import re 

def unigram_manual(text):
    unigrams = text.lower().split()

    return unigrams


def bigram_manual(text):
    tokens_list = text.lower().split()

    bigrams = []
    for i in range((len(tokens_list)-1)):
        bigrams.append((tokens_list[i], tokens_list[i+1]))

    return bigrams


def trigram_manual(text): 
    text = text.lower()
    token_list = text.split()

    trigrams = []
    for i in range(len(token_list)-2):
        trigrams.append((token_list[i], token_list[i+1], token_list[i+2]))
    return trigrams


def ngrams_manual(text, n):
    tokens_list = text.lower().split()

    ngrams = []
    for i in range(len(tokens_list) - (n-1)):
        ngrams.append(tuple(tokens_list[i:i+n]))

    return ngrams


def counter(ngram):
    word_counts = {}
    for token in ngram:
        if token in word_counts:
            word_counts[token] += 1
        else:
            word_counts[token] = 1

    return word_counts

