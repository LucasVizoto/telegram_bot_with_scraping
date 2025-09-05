import requests
from bs4 import BeautifulSoup, ResultSet

def scraping_five_recent_news_from_g1() -> ResultSet:
    '''
    ----------------------------------------------------------------
        Este método realiza um scraping da página de notícias g1.globo.com
        e são retornadas posteriormente os elementos resultantes desse scraping.
    ----------------------------------------------------------------
    
    '''

#-----------------------------------------------------------------------------------------

    '''
    ----------------------------------------------------------------
        PEGANDO TODOS OS ELEMENTOS DO HTML DA PÁGINA PRINCIPAL
    ----------------------------------------------------------------
    '''
    url = "https://g1.globo.com/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

   
    '''
    ----------------------------------------------------------------
                ENCONTRANDO MANCHETES E RETORNANDO-AS
    ----------------------------------------------------------------
    '''

    manchetes = soup.find_all("a", class_="feed-post-link")
    return manchetes