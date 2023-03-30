import requests
import pandas as pd
from bs4 import BeautifulSoup


def big_eight_price():
    url = 'https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx'
    re = requests.get(url)
    soup = BeautifulSoup(re.text, 'lxml')  # 使用lxml解析
    tables = soup.find_all('table', attrs={'cellpadding': '2'})  # 觀察到網頁表格table的差異性,使用此方式抓取資料
    # print(tables)  #測試
    data = []
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date, value, price = [td.text for td in tr.find_all('td')]  # 建立資料清單
            if date == '日期':
                continue
            data.append([date, value, price])

    df = pd.DataFrame(data, columns=['日期', '買賣超金額', '台指期'])
    df.to_csv('八大官股買賣超.csv')
    print(data)
    df.to_csv()