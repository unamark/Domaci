import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.realitica.com/index.php?for=Prodaja&pZpa=Crna+Gora&pState=Crna+Gora&type%5B%5D=&price-min=&price-max=&qry=&lng=hr"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
lista = soup.find_all('#thumb_div')

data = []
for elem in lista:
    link = lista.find('a')['href']
    data.append(link)
    un = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    l = soup.find_all('.detailLRAd < strong')
    for i in l:
        a = i.next_element().strip()
        data.append(a)
'''podrucje = soup.find('.detailLRAd < strong').next_element().strip()
    lokacija = soup.find('.detailLRAd < strong').next_element().strip()
    adresa = soup.find('.detailLRAd < strong').next_element().strip()
    e_razred = soup.find('.detailLRAd < strong').next_element().strip()
    cena = soup.find('.detailLRAd < strong').next_element().strip()
    godina = soup.find('.detailLRAd < strong').next_element().strip()
    sobe = soup.find('.detailLRAd < strong').next_element().strip()
    kupatila = soup.find('.detailLRAd < strong').next_element().strip()
    povrsina = soup.find('.detailLRAd < strong').next_element().strip()
    parking = soup.find('.detailLRAd < strong').next_element().strip()
'''

columns = ['link', 'vrsta', 'područje', 'lokacija', 'broj spavaćih soba', 'broj kupila', 'cena', 'stambena površina', 'zemljište', 'parking mesta',
           'od mora', 'novogradnja', 'klima', 'naslov', 'opis', 'web stranica', 'oglasio', 'mobilni', 'broj/id oglasa', 'zadnja promjena', 'slike']
df = pd.DataFrame(data, columns=columns)
df.to_csv('realitica.csv', index=False)
