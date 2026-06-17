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


text = "Makine öğrenmesi veri ile öğrenir"

def unigram_manuel(text):
    text = text.lower()
    tokens = text.split()

    unigrams = []

    for token in tokens:
        unigrams.append(token)

    print(unigrams)





def bigram_manuel(text):
    text = text.lower()
    tokens = text.split()

    bigrams = []

    for i in (range(len(tokens) - 1)):
         
        bigrams.append((tokens[i] , tokens[i + 1]))

    print(bigrams)





def trigram_manuel(text):
    
    tokens = text.split().lower()

    bigrams = []

    for i in (range(len(tokens) - 2)):
         
        bigrams.append((tokens[i] ,tokens[i + 1], tokens[i + 1]))

    print(bigrams)







text = """
Ben okula gittim
ben evE gittim
ben markete gittim
"""
#"ben" kelimesinden sonra en çok hangi kelime geliyor?

def example_unigram(text):
    text = text.lower()
    tokens = text.split()

    unigrams = [token for token in tokens]
    counts = {}
    for i in range(len(unigrams) -1):
        current_word = unigrams[i]
        next_word = unigrams[i + 1]
        if current_word == 'ben':
            if next_word in counts:
                counts[next_word] += 1
            else:
                counts[next_word] = 1

    print(counts)

    for word, count in counts.items():
        print(word, count / sum(counts.values()))

   
text = '''
Ben okula gittim
Ben eve gittim
Ben okula döndüm
Ben okula geldim
'''

def example_bigram(text):
    text = text.lower()
    tokens = text.split()

    bigrams = []
    word_count = {}

    for i in range(len(tokens)-1):
       bigrams.append((tokens[i+1],tokens[i+2]))

    for bigram in bigrams:
        if bigram in word_count:
            word_count[bigram] += 1
        else:
            word_count[bigram] = 1

    count_ben = 0
    for words,count in word_count.items():
        if words[0] == 'ben':
            count_ben += count

    olasilik = word_count[('ben', 'okula')] / count_ben

    print(olasilik)



####################################################################################
####################################################################################

from collections import Counter
from nltk import ngrams
from nltk import word_tokenize

raw_corpus = [
    'I love apples',
    'I love you',
    'we love you',
    'You love me',
    'He loves apples',
    'Thye loves apples',
    'I love coding and you love learning',
    'We love machine learning',
    'You love apples and bananas',
    'I truly love natural language processing' 
]


tokenized_sent = []
for sent in raw_corpus:
    sent = sent.lower()
    tokenized_sent.append(word_tokenize(sent))

bigram_list = []
trigram_list = []

for token in tokenized_sent:
    bigram_list.extend(list(ngrams(token, 2)))
    trigram_list.extend(list(ngrams(token, 3)))

#print(f'Biagram list: \n {bigram_list}')
#print('\n\n')
#print(f'Trigram list: \n {trigram_list}')

word_count_bigram = Counter(bigram_list)
word_count_trigram = Counter(trigram_list)

#print(word_count_biagram.most_common(5))
#print(word_count_trigram.most_common(5))


context_bigram = ('i', 'love')
candidates = ['you', 'love', 'nlp', 'coding']

def condditional_prob(w1,w2,w3):
    numerator = word_count_trigram.get((w1,w2,w3), 0) 
    denominator = word_count_bigram.get((w1,w2), 0)
    if denominator == 0: 
        return 0
    return numerator /denominator

print(f'Bağlam : {context_bigram}')
for cand in candidates:
    p = condditional_prob(context_bigram[0], context_bigram[1], cand)
    print(f'P({cand }|   { context_bigram[0]},{context_bigram[1]}) ={p:.4f}')












