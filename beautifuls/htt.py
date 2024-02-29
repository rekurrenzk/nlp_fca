import os
from bs4 import BeautifulSoup
from urllib import request

def text_extraction(url):
    webpage = request.urlopen(url).read()
    goofy_soup = BeautifulSoup(webpage, 'html.parser')
    text = goofy_soup.get_text()
    return text

def text_to_file(text, filename):
    os.makedirs('text_files', exist_ok=True)
    with open(os.path.join('text_files', filename), 'w', encoding='utf-8') as file:
        file.write(text)

def spooky_extraction():
    url_path = './url.txt'

    with open(url_path, 'r', encoding='utf-8') as uf:
        urls = uf.readlines()

    for idx, url in enumerate(urls):
        text = text_extraction(url.strip())
        text_to_file(text, f"wiki_{idx}.txt")

spooky_extraction()
