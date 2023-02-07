import requests
from bs4 import BeautifulSoup


Requete = requests.get("http://annuairesante.ameli.fr/")
fichier = BeautifulSoup(Requete.content, "html.parser")
with open("page.html", "w") as file:
    file.write(str(fichier))
