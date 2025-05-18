import requests
from bs4 import BeautifulSoup
con = requests.get('https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_6_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_6_0_na_na_na&as-pos=6&as-type=TRENDING&suggestionId=mobiles&requestId=e96c716c-a468-4a52-86f8-83e6a31bc8c1')

soup = BeautifulSoup(con.text,'html.parser')

val = soup.find_all('div',class_ ='KzDlHZ')

phonename = []
for i in val:
    phonename.append(i.text)

ram,rom = [],[]

spec = soup.find_all('div',class_= '_6NESgJ')


for entry in spec:
    row = entry.text.split('|')
    
    ram.append(row[0].strip())
    
    rom_part = row[1].strip()
    value_before_rom = rom_part.split('ROM')[0].strip()
    rom.append(value_before_rom)
    
    

import pandas as pd
data = pd.DataFrame({'PHONE_NAME':phonename,
                      'RAM':ram,
                      'ROM':rom,
                    })







