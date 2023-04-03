import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

data = []
driver = webdriver.Chrome()

for page in range(1, 6):
    url = f'https://www.kinopoisk.ru/lists/movies/top250/?page={page}'
    driver.get(url)
    print(f'Парсим страницу = {page}')
    # извлекаем все блоки со страницы
    blocks = driver.find_elements(By.CLASS_NAME, 'styles_root__ti07r')
    for block in blocks:
        russion_name = block.find_element(By.CLASS_NAME, 'base-movie-main-info_mainInfo__ZL_u3').text
        # проверка фильмов без второго названия
        try:
            original_name = block.find_element(By.CLASS_NAME, 'desktop-list-main-info_secondaryTitleSlot__mc0mI').find_element(By.CLASS_NAME, 'desktop-list-main-info_secondaryTitle__ighTt').text
        except selenium.common.exceptions.NoSuchElementException:
            original_name = "----"
        blocks_link = block.find_element(By.TAG_NAME, 'a').get_attribute('href')
        country_genre = block.find_element(By.CLASS_NAME, 'desktop-list-main-info_additionalInfo__Hqzof').text
        try:
            rating = block.find_element(By.CLASS_NAME, 'styles_kinopoiskValuePositive__vOb2E').text
        except:
            rating = "_"
        data.append([russion_name, original_name, country_genre, rating, blocks_link])

handler = ['russion_name', 'original_name', "country_genre", 'rating', "link"]
print(data)
df = pd.DataFrame(data, columns=handler)
df.to_csv('/Users/Z_Sarsenov/Desktop/kinopoisk_top_250.csv', sep=';', encoding='utf8')


