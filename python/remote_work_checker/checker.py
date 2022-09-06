import pandas as pd
import os
import time
from datetime import date
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests


def open_page(url: str) -> WebDriver:
    """
    :WebDriver: driver
    """
    options: Options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.183 Safari/537.36')
    driver: WebDriver = webdriver.Chrome(options=options)
    # driver.get(url)
    return driver


def get_page(url):
    user_agent_ie = 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
    headers = {'User-Agent': user_agent_ie}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res


def roe_avg_5yr(name, code, driver) -> float:
    roe_5_years_x_path = '//*[@id="stockItem"]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[3]'
    roe = -100
    try:
        roe = driver.find_element_by_xpath(roe_5_years_x_path).text
        roe = roe[:-1]
        roe = float(roe)
        print(f'name:{name}, roe:{roe}')
    except NoSuchElementException as err:
        print(f'=======> 제외 기업: {name}')
        print(err)
    finally:
        return float(roe)



def validate_page(driver: WebDriver):
    search_btn = driver.find_element_by_id('btnSearch')
    date_input = driver.find_element_by_id('startDt')
    today = date_input.get_attribute('value')
    date_input.clear()
    date_input.send_keys('2020.01.02')
    search_btn.click()

    xpath_bbb_minus = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
    actual = driver.find_element_by_xpath(xpath_bbb_minus).text
    expected_yield = '8.02'
    assert actual == expected_yield

    search_btn = driver.find_element_by_id('btnSearch')
    date_input = driver.find_element_by_id('startDt')
    date_input.clear()
    date_input.send_keys(today)
    search_btn.click()


def get_bond_driver():
    global driver_path, yield_url
    options: Options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.183 Safari/537.36')
    driver: WebDriver = webdriver.Chrome(driver_path, options=options)
    driver.get(yield_url)
    return driver


def get_bond_yield() -> float:
    driver = get_bond_driver()
    validate_page(driver)
    xpath_bbb_minus = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
    bbb_minus_yield = driver.find_element_by_xpath(xpath_bbb_minus).text
    driver.quit()
    return float(bbb_minus_yield)

# def get_req_earn_rate() -> float:
#     page = get_page('https://www.kisrating.com/ratingsStatistics/statics_spread.do')
#     soup = BeautifulSoup(page.content, 'html.parser')
#
#     td = soup.find('td', {'class': 'fc_blue_dk'}, string='BBB-')
#     bbb_minus_yield = 0.0
#     for sib in td.next_siblings:
#         text = getattr(sib, 'text', 0)
#         bbb_minus_yield = max(bbb_minus_yield, float(text))
#
#     return bbb_minus_yield



if __name__ == '__main__':
    cd_path = "/usr/local/bin/chromedriver"
    home_path = "https://myehr.hmckmc.co.kr/main/essMain.do"


    options: Options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.183 Safari/537.36')
    driver: WebDriver = webdriver.Chrome(executable_path=cd_path, options=options)
    print(driver)
    wd = open_page(home_path)
    month = '7'
    day = '8'
    btn_id = f'btnTd{date.today().strftime("%Y")}{month}{day}'
    # search_btn = driver.find_element_by_id('btnSearch')
    # date_input = driver.find_element_by_id('startDt')
    # today = date_input.get_attribute('value')
    # date_input.clear()
    # date_input.send_keys('2020.01.02')
    # search_btn.click()

    # roe_pd = pd.read_csv('/Users/7110992/Desktop/removeme/s-rim-analysis/resource/roe_list.csv', engine='python')

    # fp = open('../../resource/values_output.csv', 'w')
    # now_time = time.strftime('%Y.%m.%d', time.localtime())
    # fp.write(now_time)
    # try:
    #     for i in roe_pd.index:
    #         name = roe_pd.loc[i, ['회사명']]
    #         name['회사명'] = name['회사명'].replace(' ', '')
    #         # comp_code = 'A001880'
    #         comp_code = comp_code_list[name['회사명']]
    #
    #         (value_gap, price_buy, price_sell_1, price_sell_2) = s_rim(comp_code, bbb_minus_yield)
    #         if price_buy == 0:
    #             continue
    #         fp.write(f'{name["회사명"]},{value_gap},{price_buy},{price_sell_1},{price_sell_2}{os.linesep}')
    #         print(f'가치평가,    {value_gap}%{os.linesep}'
    #               f'매수가,    {price_buy}{os.linesep}'
    #               f'1차 매도가,{price_sell_1}{os.linesep}'
    #               f'2차 매도가,{price_sell_2}')
    #         time.sleep(20)
    # except Exception as err:
    #     print(type(err), err)
    # finally:
    #     fp.close()

