import stanza

# Türkçe NLP pipeline oluştur
nlp = stanza.Pipeline(
    lang='tr',
    processors='tokenize,pos,lemma,depparse'
)

# Cümleyi analiz et
sentence = 'Ali okula hızlıca yürüdü'
doc = nlp(sentence)

# Her kelime için dependency bilgilerini yazdır
for sent in doc.sentences:
    for word in sent.words:

        # head=0 ise kelime ağacın kökü (ROOT)'dür.
        # Aksi halde bağlı olduğu üst kelimeyi buluruz.
        head_text = (
            'ROOT'
            if word.head == 0
            else sent.words[word.head - 1].text
        )

        print(
            f'Kelime: {word.text:<10} '
            f'Head: {head_text:<10} '
            f'İlişki: {word.deprel}'
        )