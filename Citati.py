
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


for citat in vsi_citati[0:5]:
    print citat.text
