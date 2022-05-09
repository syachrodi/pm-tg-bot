from dotenv import load_dotenv
load_dotenv()

from selenium import webdriver
from pprint import pprint
from bs4 import BeautifulSoup
import time

BASE_URL = 'https://thesphynx.co/swap/'
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    '32520/0xB361D5953e21Cfde5CD62B89FDf40bc21903A6bb/',
    # '0x71946a5C9dA7C95ee804a9BE561EC15A3F286A7D/'
]

def main(event={}, context={}):
    for item in items:
        url = "https://thesphynx.co/swap/32520/0xB361D5953e21Cfde5CD62B89FDf40bc21903A6bb/"
        # headers = { 'User-Agent': 'Generic user agent' }
        # page = requests.get(url, headers=headers)
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        pprint(soup)
        # soup.find_all('div')[0].get_text()
        # tes = 
        # soup = BeautifulSoup(r.text, 'html.parser')
        harga = ""
        market = ""


        # soup = BeautifulSoup(urllib.urlopen(r).read(), 'html.parser')
        # res = soup.find_all('div', attrs={'class': 'sc-fSDTwv bijjgX'})
        # mcaps = soup.find_all('div', attrs={'class': 'sc-gsDKAQ zTPCH'})


        # for i in res:
        #     price = i.find('div', attrs={"class":"sc-gsDKAQ QYecP"})
        #     print('\ntitle:', price.text.strip())
        #     harga = price.text.strip()

        # for i in res:
        #     mcap = i.find('div', attrs={"class":"sc-gsDKAQ zTPCH"})
        #     print('\ntitle:', mcap.text.strip())
        #     market = mcap.text.strip()

        # str('soup.prettify()')
        # print('\nPrice:', price.text.strip())
        # print('\nMcap:', mcap.text.strip())
        # price = soup.select_one('div.sc-gsDKAQ QYecP').text
        # mcap = soup.select_one('div.sc-gsDKAQ zTPCH').text
        # price = soup.select_one('h1[class="sc-gsDKAQ QYecP"]').text
        # mcap = soup.select_one('h3[class="sc-gsDKAQ zTPCH"]').text
        # price = soup.select_one('h3[class="sc-gsDKAQ zTPCH"]')['content']

        data = {
            'chat_id': CHAT_ID,
            # 'text': soup.prettify(),

            'text': f'*${soup.prettify()}*\n({url})',
            # 'text': f'*${harga}*\n[{market}]({url})',
            'parse_mode': 'Markdown'
        }
        r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

if __name__ == '__main__':
    main()