import requests
from bs4 import BeautifulSoup
import re

url = 'https://jsonplaceholder.typicode.com/posts'

def getText(url):
    response = requests.get(url)
    data = response.json()
    
    return data
   

data = getText(url)


raw_text = '''
@Doğal dil işleme (NLP), bilgisayarların ==== insan dilini yorumlamasına, 
manipüle etmesine ve anlamasına izin veren teknolojidir. 
Günümüzde kuruluşlar; e-postalar, metin mesajları, sosyal medya 
haber akışları,    videolar ve ses dosyaları gibi çeşitli iletişim 
kanallarından büyük hacimli ses ve metin verilerine sahiptir. 
Doğal dil işleme, eyleme geçirilebilir iş içgörüleri için bu verileri
analiz etmed]]]]e anahtardır. Kuruluşlar dil verilerinde gizlenen amacı
veya duyguyu sınıflandırabilir, sıralayabilir, filtreleyebilir ve 
anlayabilir. Doğal dil işleme, yapay zeka destekli otomasyonun önemli
bir özelliğidir ve gerçek zamanlı    makine-insan iletişimini destekler.
'''



def regex_text(text):
    text = text.lower()
    text = (' ').join(text.split())
    text = re.sub(r'[^\w\s;.,()]','',text)
    return text

text = regex_text(raw_text)
print(text)