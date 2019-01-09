
import random
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = 'https://quotes.yourdictionary.com/theme/marriage/'
response = urlopen(url).read()

soup = BeautifulSoup(response)

print soup.html.head.title.string


vsi_citati = []
vsi_citati = soup.findAll("p", attrs={"class": "quoteContent"})
citat = {"citat"}

vsi_citati.append(citat)

rand_citati = random.sample(vsi_citati, 5)


for citat in rand_citati:
    print citat.text
