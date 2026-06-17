# ==============================
# STOP WORD REMOVAL (STOP WORD ANALYSIS)
# ==============================

# Amaç:
# Metin içinde anlam açısından çok katkısı olmayan kelimeleri kaldırmak

# Örnek stop words (İngilizce):
# "the", "is", "in", "and", "a"

# Türkçe örnek:
# "ve", "bir", "bu", "şu", "için", "ile"

# Örnek cümle:
# "Ben bugün NLP öğreniyorum"

# Stop words kaldırıldıktan sonra:
# "bugün NLP öğreniyorum"

# ------------------------------

# Nasıl çalışır?
# - Önceden tanımlanmış bir stop word listesi kullanılır
# - Metindeki kelimeler bu liste ile karşılaştırılır
# - Listede olan kelimeler silinir

# ------------------------------

# Neden kullanılır?

# Avantaj:
# - Gürültüyü azaltır
# - Modeli hızlandırır
# - Gereksiz kelime sayısını düşürür

# Dezavantaj:
# - Bazı durumlarda anlam kaybı olabilir
#   Örnek: "not good" → "good" (anlam bozulur)

# ------------------------------

# NLP PIPELINE İÇİN YERİ

# Metin → Temizleme → Tokenization → Stop Word Removal →
# Stemming / Lemmatization → Vectorization

# ------------------------------

# ÖNEMLİ NOT:
# Modern LLM'lerde (BERT, GPT gibi)
# stop word removal genelde yapılmaz
# çünkü bağlam bilgisi önemlidir


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords_eng = set(stopwords.words('english'))
eng_text = 'This is just a simple example to how words can be removed from sentences. '
eng_text_list = eng_text.split()
filtered_word_eng = [word for word in eng_text_list if word.lower() not in stopwords_eng]
print(filtered_word_eng)




stopwords_turkish = set(stopwords.words('turkish'))
turkish_text = 'Fonetik, konuşulurken, dil, gırtlak, ses telleri, damak, dişler ve dudaklar ile çıkarılan sesleri ve bu seslerin dil ile olan ilişkilerini tanımlamak için kullanılan bir terimdir.'
turkish_text_list = turkish_text.split()
filtered_word_turkis = [word for word in turkish_text_list if word.lower() not in stopwords_turkish]
print(f' Filtered Turkish words: {filtered_word_turkis}')


