
import requests
from bs4 import BeautifulSoup

url = 'https://www.ynet.co.il/home/0,7340,L-184,00.html'
r = requests.get(url)
soup = BeautifulSoup(r.text)
for link in soup.select('a.smallheader'):
    print(link.text)


num = int(input("Choose a number"))

def raise_unless(num):
    if num % 3 != 0:
        raise Exception("Hahahah")




try:
    raise_unless(num)
except Exception:
    print("Nice")



class LightBuld:
    def __init__(self):
        self.is_lights_on = False

    def light_on(self):
        if not self.is_lights_on:
            print("Lights On")
            self.is_lights_on = True

    def light_off(self):
        if self.is_lights_on:
            print("Lights Off")
            self.is_lights_on = False

