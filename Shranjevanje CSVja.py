# https://scrapebook22.appspot.com/

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()


soup = BeautifulSoup(response)

print soup.html.head.title.string
vsi_trji = soup.findAll("tr")

vse_osebe =[]

for tr in vsi_trji:
    ime = tr.find("td")
    vsi_tdji = tr.findAll("td")
    oseba = {
        "ime": "",
        "priimek": "",
        "email": ""
    }

    if ime:
        oseba["ime"] = ime.string

    if vsi_tdji and len(vsi_tdji) > 1:
        priimek = vsi_tdji[1].string
        oseba["priimek"] = priimek

    vse_osebe.append(oseba)

    link = tr.find("a")

    if link and link.string == "See full profile":
        link_do_osebe = 'https://scrapebook22.appspot.com/' + link["href"]

        response2 = urlopen(link_do_osebe).read()
        soup2 = BeautifulSoup(response2)

        email = soup2.find("span", attrs={"class": "email"}).string
        oseba["email"] = email

    vse_osebe.append(oseba)

    csv_file.write(oseba["ime"] + "," + oseba["priimek"] + "," + oseba["email"] + "\n")

csv_file.close()

print vse_osebe