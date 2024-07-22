import requests
from bs4 import BeautifulSoup

link = "https://www.google.com.br/search?q=cotacao+dolar"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 "
                  "Safari/537.36"
}

requisicao = requests.get(link, headers=headers)
print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())
# print(site.title)
titulo = site.title.get_text()
print(titulo)

# # pesquisa = site.find("input")
# pesquisa = site.find_all("input")
# print(pesquisa[1])
#
# pesquisa2 = site.find("textarea", class_="gLFyf")
# print(pesquisa2)
# print(pesquisa2["value"])

cotacao_dolar = site.find("span", class_="SwHCTb")
print(cotacao_dolar.get_text())
print(cotacao_dolar["data-value"])
