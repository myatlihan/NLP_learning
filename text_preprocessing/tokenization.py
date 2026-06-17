# ==============================
# TOKENIZATION
# ==============================

# Amaç:
# Metni modelin işleyebileceği küçük parçalara (tokenlara) ayırmak

# Örnek metin:
# "merhaba ben yasin"

# Tokenization sonrası:
# ["merhaba", "ben", "yasin"]

# Her bir parçaya "token" denir

# Neden gerekli?
# Bilgisayar cümleyi bir bütün olarak anlayamaz
# Önce kelimelere veya alt parçalara ayırmak gerekir

# Tokenization NLP pipeline'ının temel adımlarından biridir

# Tokenization seviyeleri:

# 1. Word Tokenization
# Cümleyi kelimelere ayırır
# "bugün hava güzel"
# → ["bugün", "hava", "güzel"]

# 2. Sentence Tokenization
# Metni cümlelere ayırır
# "Merhaba. Nasılsın?"
# → ["Merhaba.", "Nasılsın?"]

# 3. Character Tokenization
# Kelimeyi karakterlere ayırır
# "NLP"
# → ["N", "L", "P"]

# Modern LLM'lerde genellikle:
# Word tokenization yerine Subword Tokenization kullanılır

# Örnek:
# "öğreniyorum"
# → ["öğren", "iyor", "um"]

# Bunun amacı:
# Bilinmeyen kelimeleri daha iyi temsil edebilmek
# Vocabulary boyutunu küçültmek

# Sonuç:
# Temizlenmiş metin → Tokenlar → Sayısallaştırma (Encoding)


import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

raw_text = "Merhaba dünya! Bu bir NLP örneğidir. Sen nasılsın?, Hello, hi ..."

word_tokens = nltk.word_tokenize(raw_text)
print(f'Word tokens : {word_tokens}')
print(f'Word tokens count: {len(word_tokens)}')


sentence_tokens = nltk.sent_tokenize(raw_text)
print(f'Sentence tokens: {sentence_tokens}')
print(f'Sentence tokens count: {len(sentence_tokens)}')