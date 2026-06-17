# ==============================
# TEXT PREPROCESSING PIPELINE
# ==============================

# 1. Normalization (case folding)
# Unicode ve string normalization yapılır (NFKC / NFKD)
# Amaç: "İ" vs "i̇" gibi Unicode farklarını ortadan kaldırmak
# Lowercasing uygulanarak vocabulary boyutu azaltılır

# 2. Noise Removal (regex filtering)
# HTML tag'leri, URL'ler, mention (@user), hashtag (#tag)
# özel karakterler regex ile temizlenir
# Amaç: modelin öğrenmesini bozacak gürültüyü kaldırmak

# 3. Punctuation handling
# Noktalama işaretleri genellikle kaldırılır veya ayrı token yapılır
# Sentiment analysis gibi görevlerde "!" önemli feature olabilir

# 4. Tokenization
# Metin subword / word / character seviyesinde tokenlara ayrılır
# Modern sistemlerde BPE, WordPiece, SentencePiece kullanılır
# Amaç: text → discrete token sequence dönüşümü

# 5. Stopword filtering (task-dependent)
# TF-IDF / klasik ML pipeline'da kaldırılır
# Transformer tabanlı modellerde genellikle kaldırılmaz
# Çünkü bağlam bilgisi önemlidir

# 6. Stemming (Porter / Snowball)
# Heuristik rule-based suffix stripping yapılır
# "running" → "run"
# Hızlıdır ama anlamsal doğruluk düşük olabilir

# 7. Lemmatization (linguistic normalization)
# POS-tagging kullanılarak sözlük formu bulunur
# "better" → "good"
# Daha doğru ama computationally expensive

# 8. Feature representation
# Bag of Words (BoW), TF-IDF veya Dense Embedding'e dönüşüm
# BoW: sparse vector representation
# Embedding: dense semantic vector (Word2Vec, GloVe, BERT)

# 9. Padding / Truncation (sequence models)
# RNN / Transformer inputları sabit length'e getirilir
# padding: 0 ekleme
# truncation: max length sonrası kırpma

# 10. Attention-ready encoding (modern NLP)
# input_ids, attention_mask oluşturulur
# Transformer architecture için gerekli format

# ==============================
# FINAL OUTPUT
# ==============================
# Cleaned + tokenized + vectorized representation
# artık model training / inference için hazır hale gelir



#Fazla boşlukları temizleme
raw_text = 'Python,     NLP!    OpenCV'
normalized_text = ((' ').join(raw_text.split()))
print(normalized_text)


#Büyük ve küçük harf dönüşümü.
raw_text  = 'NLP: Natural Language Processing '
normalized_text_2= raw_text.lower()
print(normalized_text_2)


#Noktalama işaretlerini kaldırma
import string
raw_text = '''NLP (Doğal Dil İşleme); yapay zekânın —özellikle bilgisayarların— 
insan dilini (yazıları, cümleleri ve konuşmaları) anlamasını, analiz etmesini
ve yorumlamasını sağlayan alt dalıdır.'''
normalized_text_3 = raw_text.translate(str.maketrans('', '', string.punctuation))
print(normalized_text_3)

import re
normalized_text_4 = re.sub(r'[^\w\s]', '',raw_text)
print(normalized_text_4)


#Yazım hatalarını düzeltme 
from textblob import TextBlob 
raw_text = 'NLP (Natural Langage Processing) is a branch of AI; it helps computers understand human language.'
normalized_text_5 = TextBlob(raw_text).correct()
print(f'Yazım hataları: {normalized_text_5}')


#html etiketlerinden düz metin 
import requests
from bs4 import BeautifulSoup
import re
headers = {
    "User-Agent": "MyNLPProject/1.0 (learning NLP project; contact: test@mail.com)"
}
url = 'https://tr.wikipedia.org/wiki/NLP'
html = requests.get(url=url,headers=headers).text

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
text = (' ').join(text.split())
text = re.sub(r'[^\w\s]', '', text)
print(text)
