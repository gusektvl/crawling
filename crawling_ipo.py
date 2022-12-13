import re
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url = 'http://www.38.co.kr/html/fund/?o=v&no=1807&l=&page=1'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select_one('body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)')
    print(title)
else :
    print(response.status_code)


for i in range(len(data) - 2):
    try:
        print(i, data[i][0][0])
    except:
        pass
