import requests
from bs4 import BeautifulSoup
import time

class Checked:
    url = 'https://www.investing.com/crypto/ethereum'
    headers = {
        'user-agent': '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36''',   
    }

    max_price_ethusd = 0.0 

    def __get_checked_ethusd(self):
        try:
            result = requests.get(self.url, headers=self.headers)
            html = BeautifulSoup(result.content, 'html.parser')

            ethusd = html.find_all('span', {'class': 'pid-1061443-last', 'id': 'last_last'})
            return ethusd[0].text.replace(',', '')
        except:
            print(f'Не удалось считать курс ETHUSD с данного url: {self.url}')

    def check_ETHUSD(self):
        try:  
            crypto_price = float(self.__get_checked_ethusd())  
            if crypto_price > self.max_price_ethusd:
                self.max_price_ethusd = crypto_price
            dif_price = crypto_price < self.max_price_ethusd * 0.99
            if dif_price:
                print(
                    'Цена ETHUSD упала на 1% от '
                    f'максимальной цены за последний час: {self.max_price_ethusd}')
                self.max_price_ethusd = 0.0
            diff = round((self.max_price_ethusd/crypto_price - 1) * 100, 2)
            print(
                f'Максимальная цена {self.max_price_ethusd}, '
                f'текущая {crypto_price} разница: %{diff}')           
            time.sleep(10)
            self.check_ETHUSD()
        except Exception as e:
            print(f'Произошла ошибка: {e}')
            

check = Checked().check_ETHUSD()







