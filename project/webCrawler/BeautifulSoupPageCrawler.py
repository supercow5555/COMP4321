import requests
from bs4 import BeautifulSoup


def page_crawler(input_URL):
    reqs = requests.get(input_URL)
    bs_object = BeautifulSoup(reqs.text, 'html.parser')

    for link in bs_object.findAll("a"):         # Find all <a> tags in the parsed HTML content
        print(link.get('href'))

page_crawler('https://cse.hkust.edu.hk')