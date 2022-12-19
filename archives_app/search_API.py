import requests
import json
from time import sleep
import progressbar
import pyfiglet

def progressBar():
      
    widgets = ['  Carregando... ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        sleep(0.1)
        bar.update(i)

def searchInput():
    #   Agent based on Device:"https://deviceatlas.com/blog/list-of-user-agent-strings"   
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"}
    print()
    print("\n\n                     Bem-vindo(a) ao jBook!")
    print("\n            Pesquise e Cadastre seus Livros Favoritos.\n\n")
    progressBar()
    sleep(2)
    print(pyfiglet.figlet_format("    jBook ", font = "kban"))
    sleep(1)
#    for i in tqdm(range(int(9e6)), bar_format="   {l_bar}{bar}|", ncols=55):
#        pass
    nameBook = input("\n Autor ou Assunto: ")

    API = "https://www.googleapis.com/books/v1/volumes?fields=items(selfLink,volumeInfo(title,subtitle,authors))&q={}&maxResults=40&printType=books".format(nameBook)
    r = requests.get(url=API, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.content)
        n = 0
    else:
        print("Não consegui recuperar! Desculpe.")
    
    return data, n, headers
    
data, n, headers = searchInput()