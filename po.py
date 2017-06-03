import os

from selenium import webdriver

driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
driver.maximize_window()
if os.path.exists('titles_values.txt'):
    os.remove(os.path.abspath('titles_values.txt'))

if os.path.exists('alts_values.txt'):
    os.remove(os.path.abspath('alts_values.txt'))

f = open("url_file.txt")

for url in f.readlines():
    driver.get(url)
    file_title = open('titles_values.txt', 'a')
    file_title.write(url + ':\n')
    file_alt = open('alts_values.txt', 'a')
    file_alt.write(url + ':\n')
    title_tegs = driver.find_elements_by_css_selector('[title]')
    for title_value in title_tegs:
        text = title_value.get_attribute('title')
        file_title.write(text + '\n')

    alt_tags = driver.find_elements_by_css_selector('[alt]')
    for alt_value in alt_tags:
        alt_text = alt_value.get_attribute('alt')
        titles = open('alts_values.txt', 'a')
        titles.write(url + '\n' + alt_text + '\n\n')

driver.close()
