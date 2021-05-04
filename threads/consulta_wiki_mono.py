import time
import requests



#Função que realiza uma requisição http para uma url.
#Recebemos a resposta e verificamos qual é o status_code.
#Se for 200, sabemos que a página existe. Se for 404 a página não existe.
#Para maiores informações sobre o pacote requests(https://docs.python-requests.org/en/master/)
#Para instalar o pacote requests utilize o comando # pip install requests
def get_wiki_page_existence(wiki_page_url, timeout=10):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    #conteudo da requisicao
    #response.text

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


#A ideia deste código é verificar se a wikipedia possui as páginas para os números
#de 1 a 50. (https://en.wikipedia.org/wiki/1, https://en.wikipedia.org/wiki/2, etc)
#Para cada página será necessário fazer uma requisição http para o servidor e aguardar a resposta.

if __name__ == "__main__":
    print("Executando de forma sequêncial:")
    
    #forma mais concisa de fazer a inicialização das urls
    wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]

    #o código acima produz o mesmo resultado que o código abaixo.
    #wiki_page_urls = []
    #for i in range(50):
    #   wiki_page_urls.append("https://en.wikipedia.org/wiki/" + str(i))

    #armazenamos o tempo no momento do início da execução das consultas http
    inicio = time.time()
    #realizamos as consultas de forma sequêncial
    for url in wiki_page_urls:
        print(get_wiki_page_existence(wiki_page_url=url))
    
    #armazenamos o tempo ao final das consultas
    fim = time.time()
    
    print(f"Tempo sequêncial: {fim-inicio}s")

