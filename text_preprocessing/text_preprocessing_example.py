# =====================================
# QUESTION 1
# =====================================

# Aşağıdaki metni temizle:
#
# "Merhaba!!! Ben Yasin. NLP öğreniyorum :) 2026 yılında mezun olacağım."
#
# Yapılacaklar:
# 1. Metni küçük harfe çevir.
# 2. Noktalama işaretlerini kaldır.
# 3. Fazla boşlukları temizle.
# 4. Sonucu ekrana yazdır.

raw_text = "Merhaba!!! Ben Yasin. NLP öğreniyorum :) 2026 yılında mezun olacağım."

def question1(text):
    import re
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    final_text = (' ').join(text.split())
    print(final_text)





# =====================================
# QUESTION 2
# =====================================

# Aşağıdaki metinde bulunan tüm sayıları regex ile bul:
#
# "Ali 25 yaşında, Ayşe 19 yaşında ve Mehmet 42 yaşında."
#
# Bulduğun sayıları bir liste olarak ekrana yazdır.

raw_text2 = "Ali 25 yaşında, Ayşe 19 yaşında ve Mehmet 42 yaşında."

def question2(text):
    import re

    numbers = re.findall('\d+', text)
    print(numbers)



# =====================================
# QUESTION 3
# =====================================

# Aşağıdaki metindeki e-posta adreslerini regex ile bul:
#
# "Bana yasin@test.com veya destek@gmail.com adreslerinden ulaşabilirsiniz."
#
# Tüm e-postaları liste halinde yazdır.

raw_text3 = "Bana yasin@test.com veya destek@gmail.com adreslerinden ulaşabilirsiniz."

def question3(text):
    import re
    filtered_list = re.findall(r"\S+@\S+", text)
    print(filtered_list)




# =====================================
# QUESTION 4
# =====================================

# Aşağıdaki metni tokenize et:
#
# "Makine öğrenmesi veri ile öğrenir."
#
# Toplam kaç token oluştuğunu hesapla.
# Token listesini ve token sayısını yazdır.

raw_text4 =  "Makine öğrenmesi veri ile öğrenir."

def question4(text):
    import nltk
    word_tokenazation_list = nltk.word_tokenize(text)
    print(f'Word Tokenization List: {word_tokenazation_list}')
    print(f'Word Tokenization List Length {len(word_tokenazation_list)}')








# =====================================
# QUESTION 5
# =====================================

# Aşağıdaki token listesinden stop word'leri kaldır:
#
# ["ben", "bugün", "nlp", "ve", "makine", "öğrenmesi"]
#
# Stop words:
#
# ["ben", "ve"]
#
# Kalan tokenları ekrana yazdır.



token_list = ["ben", "bugün", "nlp", "ve", "makine", "öğrenmesi"]
stop_words = ["ben", "ve"]
def question5(token_list):
    from nltk.corpus import stopwords
    stopwords_turkish = set(stopwords.words('turkish'))
    filtered_stopwords_turkish = [word for word in token_list if word not in stopwords_turkish]
    print(filtered_stopwords_turkish)



def question5_2(token_list,stop_words):
    filtered_stopwords = [word for word in token_list if word not in stop_words]
    print(filtered_stopwords)






# =====================================
# QUESTION 6
# =====================================

# Aşağıdaki metinde en çok geçen kelimeyi bul:
#
# "python python veri nlp python veri makine"
#
# İpucu:
# Counter kullanabilirsin.


raw_text5 = "python python veri nlp python veri makine"

def question6(text):
    tokens = text.split()
    word_counts = {}

    for word in tokens:
        if word in word_counts:
            word_counts[word] +=1
        else:
            word_counts[word] = 1 

    print(word_counts)
    most_common_word = ''
    max_count = 0 
    for word, count in word_counts.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    print(f'En sık geçen kelime: {most_common_word}')
    print(f'Geçme sayısı: {max_count}')


def question6_2(text):
    from collections import Counter
    token_list = text.split()
    counter = Counter(token_list)
    print(counter.most_common(1))








# =====================================
# QUESTION 7
# =====================================

# Aşağıdaki metindeki URL'leri regex ile bul:
#
# "Projelerimi https://github.com/yasin ve https://kaggle.com/yasin adreslerinde paylaşıyorum."
#
# Tüm URL'leri liste halinde yazdır.


raw_text6 = "Projelerimi https://github.com/yasin ve https://kaggle.com/yasin adreslerinde paylaşıyorum 12."

def question7(text):
    import re
    url_list = re.findall('\d+',text)
    print(url_list)



# =====================================
# QUESTION 8
# =====================================

# Aşağıdaki metni cümlelere ayır:
#
# "Merhaba. Ben Yasin. NLP öğreniyorum. Çok eğlenceli."
#
# Toplam cümle sayısını bul.
# Her cümleyi ayrı satırda yazdır.
raw_text7 = "Merhaba. Ben Yasin. NLP öğreniyorum. Çok eğlenceli."

def question8(text):
    import nltk
    sent_token_list = nltk.sent_tokenize(raw_text7)
    print(sent_token_list)




# =====================================
# QUESTION 9
# =====================================

# Aşağıdaki metinde bulunan tüm özel karakterleri kaldır:
#
# "@@NLP!!! %%%öğreniyorum###"
#
# Sonucu:
#
# "nlp öğreniyorum"
#
# formatına getir.

raw_text8 = "@@NLP!!! %öğreniyorum###"

def question9(text):
    import re 
    text = text.lower()
    filtered_text = re.sub(r'[^\w\s]', '',text)
    print(filtered_text)




# =====================================
# QUESTION 10
# =====================================

# JSONPlaceholder API'sinden post verilerini çek.
#
# https://jsonplaceholder.typicode.com/posts
#
# Yapılacaklar:
#
# 1. Tüm title'ları al.
# 2. Küçük harfe çevir.
# 3. Tokenization uygula.
# 4. En sık geçen 10 kelimeyi bul.
# 5. Sonuçları ekrana yazdır.

url = 'https://jsonplaceholder.typicode.com/posts'

def question10(url):
    import requests
    import nltk
    response = requests.get(url)
    data = response.json()
    

    all_token = {}

    for element in data:
        title =element['title']
        title = title.lower()
        title_tokenize =nltk.word_tokenize(title)
        for token in title_tokenize:
            if token in all_token:
                all_token[token] +=1
            else:
                all_token[token] = 1

    sorted_word  = sorted(all_token.items(),                         
                          key = lambda x: x[1],
                          reverse=True)
       

    print(sorted_word[:10])

question10(url)