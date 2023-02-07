import requests
import csv
from bs4 import BeautifulSoup


url = "http://annuairesante.ameli.fr/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

Requete = requests.Session()
page = Requete.get(url, headers=header)
post = Requete.post(url, headers=header)
#paylod

if page.status_code == 200:
    lienrecherche = page.url

fichier = BeautifulSoup(page.text, "html.parser")
with open("page.html", "w") as file:
    file.write(str(fichier))


