# ==========================================================
# DİLBİLGİSİ (GRAMMAR) VE AYRIŞTIRMA (PARSING)
# ==========================================================

# NLP'de (Natural Language Processing) bir cümleyi anlamadan önce
# onun sözdizimsel (syntactic) yapısını analiz etmek gerekir.
#
# Bu analiz işlemine Parsing (Ayrıştırma) denir.
#
# Parsing'in amacı:
#
# 1. Cümledeki kelimelerin görevlerini bulmak
# 2. Kelimeler arasındaki ilişkileri çıkarmak
# 3. Cümlenin gramer yapısını oluşturmak
#
# Örnek:
#
# "Ali kırmızı arabayı sürdü."
#
# İnsanlar bu cümleyi kolayca anlar ancak bilgisayar için:
#
# - Ali kim?
# - Arabayı ne yapmış?
# - Kırmızı hangi kelimeyi açıklıyor?
#
# gibi soruların cevaplanması gerekir.


# ==========================================================
# DİLBİLGİSİ (GRAMMAR) NEDİR?
# ==========================================================

# Grammar (Dilbilgisi),
# bir dildeki cümlelerin nasıl oluşturulduğunu tanımlayan kurallar
# bütünüdür.
#
# Örnek:
#
# Cümle -> Özne + Yüklem
#
# veya
#
# Sentence -> Noun Phrase + Verb Phrase
#
# Bu kurallar sayesinde bilgisayar,
# hangi kelime dizilerinin anlamlı cümle oluşturduğunu öğrenebilir.


# ==========================================================
# CONTEXT FREE GRAMMAR (CFG)
# ==========================================================

# NLP'de en çok kullanılan gramer yapılarından biri
# Context Free Grammar (CFG)'dir.
#
# CFG kuralları:
#
# S  -> NP VP
#
# NP -> DT NN
#
# VP -> VB NP
#
# Açıklama:
#
# S  : Sentence (Cümle)
# NP : Noun Phrase (İsim Öbeği)
# VP : Verb Phrase (Fiil Öbeği)
# DT : Determiner (Belirteç)
# NN : Noun (İsim)
# VB : Verb (Fiil)


# Örnek cümle:
#
# "The cat chased the mouse"
#
# CFG kurallarına göre:
#
# S
# ├── NP
# │   ├── The
# │   └── cat
# │
# └── VP
#     ├── chased
#     └── NP
#         ├── the
#         └── mouse
#
# Böylece cümlenin hangi parçalardan oluştuğu bulunur.


# ==========================================================
# PARSING (AYRIŞTIRMA) NEDİR?
# ==========================================================

# Parsing,
# cümlenin grammar kurallarına göre analiz edilmesidir.
#
# Girdi:
#
# "The cat chased the mouse"
#
# Çıktı:
#
# Parse Tree (Ayrıştırma Ağacı)
#
# Parser'ın görevi:
#
# Kelimeleri kullanarak en uygun sözdizimsel ağacı oluşturmaktır.


# ==========================================================
# CONSTITUENCY PARSING
# ==========================================================

# Constituency Parsing (Phrase Structure Parsing),
# cümleyi kelime gruplarına ayırır.
#
# Amaç:
#
# Cümle hangi öbeklerden oluşuyor?
#
# sorusuna cevap vermektir.


# Örnek:
#
# "The red car moved"
#
# Parse Tree:
#
#            S
#          /   \
#        NP     VP
#      / | \      \
#    DT JJ NN     VB
#    |  |  |      |
#   The red car moved
#
# Burada:
#
# NP = The red car
#
# bir isim öbeğidir.
#
# Parser,
# tek tek kelimeler yerine
# kelime gruplarıyla ilgilenir.


# ==========================================================
# DEPENDENCY PARSING
# ==========================================================

# Dependency Parsing farklı çalışır.
#
# Burada amaç:
#
# Kelimeler arasındaki bağımlılıkları bulmaktır.
#
# Soru:
#
# Hangi kelime hangi kelimeye bağlı?


# Örnek:
#
# "The red car moved"
#
# Dependency Tree:
#
#       moved
#         |
#        car
#       /   \
#     The   red
#
# İlişkiler:
#
# nsubj(moved, car)
# det(car, The)
# amod(car, red)
#
# Açıklama:
#
# car -> moved fiilinin öznesidir
#
# The -> car kelimesinin belirtecidir
#
# red -> car kelimesinin sıfatıdır


# ==========================================================
# HEAD VE DEPENDENT
# ==========================================================

# Dependency Parsing'de her ilişkinin:
#
# 1. Head
# 2. Dependent
#
# olmak üzere iki tarafı vardır.


# Örnek:
#
# "red car"
#
# car = Head
# red = Dependent
#
# Çünkü asıl anlamı taşıyan kelime car'dır.
#
# red sadece car'ı açıklamaktadır.


# ==========================================================
# UNIVERSAL DEPENDENCIES (UD)
# ==========================================================

# Modern NLP sistemleri
# Universal Dependencies standardını kullanır.
#
# Yaygın etiketler:
#
# nsubj  -> nominal subject
# obj    -> object
# iobj   -> indirect object
# amod   -> adjectival modifier
# advmod -> adverb modifier
# det    -> determiner
# root   -> sentence root


# Örnek:
#
# "John eats an apple"
#
# root(eats)
# nsubj(eats, John)
# obj(eats, apple)
# det(apple, an)


# ==========================================================
# NEDEN PARSING YAPILIR?
# ==========================================================

# Parsing sayesinde:
#
# - Bilgi çıkarımı yapılabilir
# - Soru cevap sistemleri geliştirilebilir
# - Makine çevirisi yapılabilir
# - Metin analizi yapılabilir
# - Chatbotlar geliştirilebilir
#
# Çünkü parser,
# cümlenin sadece kelimelerini değil,
# kelimeler arasındaki anlamlı ilişkileri de ortaya çıkarır.


# ==========================================================
# ÖZET
# ==========================================================

# Grammar:
# Bir dilin kurallarını tanımlar.
#
# Parsing:
# Bu kuralları kullanarak cümleyi analiz eder.
#
# Constituency Parsing:
# Cümleyi kelime gruplarına ayırır.
#
# Dependency Parsing:
# Kelimeler arasındaki bağımlılık ilişkilerini bulur.
#
# Modern NLP uygulamalarında
# özellikle bilgi çıkarımı ve ilişki analizi görevlerinde
# Dependency Parsing daha yaygın kullanılmaktadır.

import spacy
nlp_model = spacy.load('en_core_web_sm')

sentence  = 'Can you recommend a good restuarent in London.'

doc = nlp_model(sentence)

for token in doc:
    print(f'{token.text:12} {token.pos_}')


import stanza
nlp = stanza.Pipeline('tr')

sentence = 'Bugün NLP öğrenmeye hızlıca başladım'
doc = nlp(sentence)
doc.sentences
for sent in doc.sentences:
    for word in sent.words:
        print(f'{word.text:15} {word.upos:12}')

