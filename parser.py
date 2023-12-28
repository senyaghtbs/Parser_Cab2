import parser
import time
import requests
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie
import webbrowser

# URL страницы с формой авторизации и страницы с данными после авторизации
login_url = "http://cab2.ru/eng.php"

#куки ебашим
def parserpy():
    data_url = "http://cab2.ru/sched.php?date=29-12-2023+22%3A20%3A05"
    saved_cookies = {'PHPSESSID': 'o5328lmjv562nnf89kae6vq0t0', }
    session = requests.Session()
    session.cookies.update(saved_cookies)
    #парсим
    target_response = session.get(data_url)
    html_code = target_response.text
    soup = BeautifulSoup(html_code, 'html.parser')
    #делаем дф
    second_table = soup.find_all('table')[1]
    #headers = [th.text.strip() for th in second_table.find_all('th')]
    data = []
    for row in second_table.find_all('tr')[1:]:
        cols = [col.text.strip() for col in row.find_all(['th', 'td'])]
        data.append(cols)

    while True:
        session.cookies.update(saved_cookies)
        new_target_response = session.get(data_url)
        new_html_code = new_target_response.text
        new_soup = BeautifulSoup(new_html_code, 'html.parser')
        new_second_table = new_soup.find_all('table')[1]
        #new_headers = [th.text.strip() for th in new_second_table.find_all('th')]
        new_data = []
        #print(new_data[1:])

        for new_row in new_second_table.find_all('tr')[1:]:
            new_cols = [col.text.strip() for col in new_row.find_all(['th', 'td'])]
            new_data.append(new_cols)
        if new_data == data:
            print(new_data[1:],f'проходит проверка иф')
            time.sleep(5)
            continue
        else:
            new_info = new_data[1:]
            time.sleep(5)
            return new_info
print('закончился парсер')
