from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import time



while True:
    url = "https://www.bloomberght.com/"
    sayfa = urllib.request.urlopen(url)
    soup = BeautifulSoup(sayfa, "html.parser")

    a = soup.find(id="bist-100")
    a.find(a)
    alt = a.find('small',attrs={"data-secid":"XU100 Index"})
    ikinci = alt.get_text()

    print(ikinci)
