import requests
import pprint
from bs4 import BeautifulSoup


def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all(title='Wikipedia:Citation needed')
    return len(results)


def get_citations_needed_report(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all("a", {"title" : "Wikipedia:Citation needed"}).parent

    return results





print(get_citations_needed_count('https://en.wikipedia.org/wiki/Database'))
print(get_citations_needed_report('https://en.wikipedia.org/wiki/Database'))