import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

pd_url = pd.read_csv('namelist.csv', engine='python')

# http://search.itooza.com/index.htm?seName=023910

'//*[@id="stockItem"]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[3]'

for i in pd_url.index:
    #    print(pd_url.loc[i, "회사명"])
    url = pd_url.loc[i, "URL"]
    handle = None
    while handle == None:
        try:
            handle = urllib.request.urlopen(url)
        except:
            pass
    page = handle.read()
    soup = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
    table = soup.findAll('div', {'id': 'indexTable2'})
    th_list = table[0].findAll('th')
    tr_list = table[0].findAll('tr')
    td_list = tr_list[6].findAll('td')

    td = tr_list[1].findAll('td')
    eps = []
    for tdi in td:
        if tdi.text == "N/A":
            eps.append(0)
        else:
            eps.append(int(tdi.text.replace(",", "")))
    flag = 0
    for j in range(len(eps) - 1):
        if eps[j] - eps[j + 1] > 0:
            flag = flag + 1
        else:
            break
    if flag > 5:
        print("OK !! 5 years " + pd_url.loc[i, "회사명"])
