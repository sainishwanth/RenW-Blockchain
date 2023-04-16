from bs4 import BeautifulSoup
import requests

try:
    URL = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    headers = ['h1', 'h2', 'h3', 'h4', 'h5']
    words_list = ['sustainable',
    'green',
    'clean',
    'eco-friendly',
    'renw',
    'carbon-neutral',
    'alternative']

    def check() -> int:
        count: int = 0
        for heads in soup.findAll(headers):
            lst = heads.contents[0].split()
            for words in lst:
                if words.lower() in words_list:
                    print(words)
                    count += 1
        return count
except:
    print("WebScraping Failed :(")