from time import sleep
from pathlib import Path

from selenium import webdriver
from bs4 import BeautifulSoup


url = 'https://www.wildberries.ru/catalog/0/search.aspx?search='

def get_page_html(url: str, good: str):
    """Получение структуры страницы для дальнейшего парсинга"""
    url = url + good
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        sleep(10)
        print('here')
        with open('page-to-parse.html', 'w') as f:
            f.write(driver.page_source)

    except Exception as e:
        print(e)

    finally:
        try:
            driver.close()
            driver.quit()
        except:
            pass

def parse_page_html(good: str):
    """Парсинг html страницы, получение наименования товаров и ссылок на них"""
    get_page_html(url, good)

    goods = []
    file_path = Path(Path.cwd() / 'page-to-parse.html')
    if file_path.exists():
        with open('page-to-parse.html', 'r') as f:
            page = f.read()
        file_path.unlink()
        soup = BeautifulSoup(page, 'lxml')
        items = soup.findAll('div', class_='product-card__wrapper')

        for i in range(10):
            title_tag = items[i].find('a').get('aria-label')
            link_tag = items[i].find('a').get('href')
            goods.append(f'{title_tag}: {link_tag}')
    else:
        print('no such file')
    return goods
