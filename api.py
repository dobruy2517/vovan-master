import os

import null as null
import requests
from bs4 import BeautifulSoup

if os.path.exists('titles_values.txt'):
    os.remove(os.path.abspath('titles_values.txt'))

if os.path.exists('alts_values.txt'):
    os.remove(os.path.abspath('alts_values.txt'))

file_url = open('url_file.txt', 'r')
title_file = open('titles_values.txt', 'a')
alt_file = open('alts_values.txt', 'a')
for url in file_url.readlines():
    resp = requests.get(url.replace('\n', ''))
    page_content = resp.content
    soup = BeautifulSoup(page_content, 'html.parser')
    titles = soup.find_all('title')
    alts = soup.find_all('img')
    title_file.write('\n' + url)
    alt_file.write('\n' + url)
    for title in titles:
        title = title.get_text()
        title_file.write(title + '\n')

    for alt in alts:
        if alt.get('alt') != None:
            alt_file.write(alt.get('alt') + '\n')

alt_file.close()
title_file.close()
file_url.close()
