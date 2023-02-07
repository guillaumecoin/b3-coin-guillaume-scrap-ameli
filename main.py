import requests
import csv
from bs4 import BeautifulSoup

payload = {
    "type": "ps",
    "ps_profession": "34",
    "ps_profession_label": "Médecin généraliste",
     "ps_localisation": "HERAULT (34)",
    "localisation_category": "departements"
}

url = "http://annuairesante.ameli.fr/recherche.html"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}



Requete = requests.Session()
#page = Requete.get(url, headers=header)
post = Requete.post(url, params=payload, headers=header)


if post.status_code == 200:
    lienrecherche = post.url

fichier = BeautifulSoup(post.text, "html.parser")
with open("post.html", "w") as file:
    file.write(str(fichier))


