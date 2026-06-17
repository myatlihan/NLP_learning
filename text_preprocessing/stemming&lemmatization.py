# ==============================
# STEMMING (GÖVDE BULMA)
# ==============================

# Amaç:
# Kelimeleri eklerinden ayırarak kök benzeri bir forma indirgemek

# Örnek:
# "koşuyor", "koştu", "koşacak"
# → "koş"

# Nasıl çalışır?
# - Kural tabanlıdır (rule-based)
# - Sözlük kullanmaz
# - Sadece ekleri keser

# Avantaj:
# - Çok hızlıdır
# - Basit uygulanır

# Dezavantaj:
# - Bazen anlamsız sonuç üretir
#   Örnek: "studies" → "studi"

# ==============================
# LEMMATIZATION (KÖK BULMA)
# ==============================

# Amaç:
# Kelimeyi sözlükteki gerçek kök haline çevirmek

# Örnek:
# "better" → "good"
# "running" → "run"
# "was" → "be"

# Nasıl çalışır?
# - Sözlük (dictionary) kullanır
# - Dil bilgisi kurallarını dikkate alır
# - POS tagging (kelime türü analizi) yapar

# Avantaj:
# - Daha doğru sonuç verir
# - Gerçek kelime üretir

# Dezavantaj:
# - Daha yavaştır
# - Daha fazla hesaplama ister

# ==============================
# TEMEL FARK
# ==============================

# Stemming:
# Hızlı ama kaba (rule-based)

# Lemmatization:
# Daha yavaş ama daha doğru (linguistic + dictionary-based)

# ==============================
# NLP PIPELINE İÇİN YERİ
# ==============================

# Metin → Temizleme → Tokenization → Stopwords → 
# Stemming / Lemmatization → Vectorization (TF-IDF / Embedding)


import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import PorterStemmer
words_stems = ['play', 'played', 'plays', 'studied','studies']

stemer = PorterStemmer()

stems = [stemer.stem(w) for w in words_stems]

print(f'Orjinal: {words_stems}')
print(f'Kökler: {stems}')





from nltk.stem import WordNetLemmatizer
lematizer = WordNetLemmatizer()

word_lemma = ['running', 'better', 'gone', 'children', 'better']

lemas = [lematizer.lemmatize(w) for w in word_lemma]
print(f'Orjinal: {word_lemma}')
print(f'Lemas: {lemas}')
