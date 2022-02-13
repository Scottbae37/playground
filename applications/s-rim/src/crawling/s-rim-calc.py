import pandas as pd
import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup
import requests

ROOT_PATH = '/Users/scottbae37/git/playground/applications/s-rim'
CHROME_DRIVER_PATH = '/Users/scottbae37/bin'


def open_page(url) -> WebDriver:
    """
    :WebDriver: driver
    """
    driver_path = '%s/chromedriver' % CHROME_DRIVER_PATH
    options: Options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36')

    driver: WebDriver = webdriver.Chrome(driver_path, options=options)
    driver.get(url)
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


def get_req_earn_rate() -> float:
    page = get_page('https://www.kisrating.com/ratingsStatistics/statics_spread.do')
    soup = BeautifulSoup(page.content, 'html.parser')

    td = soup.find('td', {'class': 'fc_blue_dk'}, string='BBB-')
    bbb_minus_yield = 0.0
    for sib in td.next_siblings:
        text = getattr(sib, 'text', 0)
        if is_float(text):
            bbb_minus_yield = max(bbb_minus_yield, float(text))

    return bbb_minus_yield


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_fn_guide(comp_code: str) -> BeautifulSoup:
    url = f'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode={comp_code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    page = get_page(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_total_num_of_stocks(soup: BeautifulSoup) -> int:
    td = soup.find('span', {'class': 'csize'}, text='(보통주/ 우선주)')
    nums_stocks = 0
    for sib in td.parent.parent.next_siblings:
        if hasattr(sib, 'text') and '/' in sib.text:
            num = sib.text[:sib.text.index('/')].replace(',', '')
            num2 = sib.text[sib.text.index('/') + 1:].strip().replace(',', '')
            nums_stocks = int(num) + int(num2)
            break
    return nums_stocks


def get_value_price(ctrl_share: int, roe_pct, req_yield_pct, nums_stocks):
    roe = roe_pct / 100
    req_yield = req_yield_pct / 100
    value = ctrl_share + (ctrl_share * (roe - req_yield)) / req_yield
    return round(value / nums_stocks * 100000000)


def get_value_price_10_percent(ctrl_share: int, roe_pct: float, req_yield_pct: float, nums_stocks):
    roe = roe_pct / 100
    req_yield = req_yield_pct / 100
    over_earning = ctrl_share * (roe - req_yield)
    value = ctrl_share + over_earning * 0.9 / (1 + req_yield - 0.9)
    return round(value / nums_stocks * 100000000)


def get_value_price_20_percent(ctrl_share: int, roe_pct: float, req_yield_pct: float, nums_stocks):
    roe = roe_pct / 100
    req_yield = req_yield_pct / 100
    over_earning = ctrl_share * (roe - req_yield)
    value = ctrl_share + over_earning * 0.8 / (1 + req_yield - 0.8)
    return round(value / nums_stocks * 100000000)


def s_rim(comp_code: str, bbb_minus_yield: float) -> tuple:
    # FN_guild snapshot page
    soup = get_fn_guide(comp_code)

    # 주식수
    nums_stocks = get_total_num_of_stocks(soup)

    # `19년 ROE
    url = f'http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode={comp_code}&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    driver = open_page(url)
    comp_name = driver.find_element_by_xpath('//*[@id="giName"]').text
    print(f'[종목명], {comp_name}')
    driver.find_element_by_xpath('//*[@id="divHighFis"]/a[1]').click()
    ctrl_share: int = int(
        driver.find_element_by_xpath('//*[@id="highlight_D_A"]/table/tbody/tr[10]/td[3]').text.replace(',', ''))
    ctrl_share_net: int = int(
        driver.find_element_by_xpath('//*[@id="highlight_D_A"]/table/tbody/tr[5]/td[3]').text.replace(',', ''))
    roe = round(ctrl_share_net / ctrl_share * 100, 4)
    print(f'가치평가 기준 ROE, {roe}')

    # if driver.find_element_by_xpath('//*[@id="highlight_D_A"]/table/tbody/tr[10]/td[4]').text.replace(',',
    #                                                                                                   '').strip().isnumeric():
    #     ctrl_share_estimation = int(
    #         driver.find_element_by_xpath('//*[@id="highlight_D_A"]/table/tbody/tr[10]/td[4]').text.replace(',', ''))
    #     ctrl_share_net_estimation = int(
    #         driver.find_element_by_xpath('//*[@id="highlight_D_A"]/table/tbody/tr[5]/td[4]').text.replace(',', ''))
    #     roe_estimation = round(ctrl_share_net_estimation / ctrl_share_estimation, 4)
    # net estimation 이 공백인 경우 있음

    price_buy = get_value_price_20_percent(ctrl_share, roe, bbb_minus_yield, nums_stocks)
    price_sell_1 = get_value_price_10_percent(ctrl_share, roe, bbb_minus_yield, nums_stocks)
    price_sell_2 = get_value_price(ctrl_share, roe, bbb_minus_yield, nums_stocks)
    if roe <= bbb_minus_yield:
        print('[비추천 종목], BBB- 채권금리보다 ROE 낮음!')
        return (0, 0, 0, 0)

    # 현재 주가
    s = driver.find_element_by_xpath('//*[@id="svdMainGrid1"]/table/tbody/tr[1]/td[1]').text
    s = s[:s.index('/')]
    price_now = int(s.replace(',', ''))
    value_gap = round(price_now / price_sell_1 - 1, 2) * 100  # Percent
    return (value_gap, price_buy, price_sell_1, price_sell_2)


if __name__ == '__main__':
    comp_code_pd = pd.read_csv('%s/resource/comp_code.csv' % ROOT_PATH, engine='python')
    comp_code_list = {}
    for i in comp_code_pd.index:
        (name, code) = comp_code_pd.loc[i, ['회사명', '회사코드']]
        name = name.replace(' ', '')
        comp_code_list[name] = code

    bbb_minus_yield: float = get_req_earn_rate()
    print(f'요구수익률(BBB-채권금리), {bbb_minus_yield}')

    roe_pd = pd.read_csv('%s/resource/roe_list.csv' % ROOT_PATH, engine='python')

    fp = open('values_output.csv', 'w')
    try:
        for i in roe_pd.index:
            name = roe_pd.loc[i, ['회사명']]
            name['회사명'] = name['회사명'].replace(' ', '')
            # comp_code = 'A001880'
            comp_code = comp_code_list[name['회사명']]

            (value_gap, price_buy, price_sell_1, price_sell_2) = s_rim(comp_code, bbb_minus_yield)
            if price_buy == 0:
                continue
            fp.write(f'{name["회사명"]},{value_gap},{price_buy},{price_sell_1},{price_sell_2}{os.linesep}')
            print(f'가치평가,    {value_gap}%{os.linesep}'
                  f'매수가,    {price_buy}{os.linesep}'
                  f'1차 매도가,{price_sell_1}{os.linesep}'
                  f'2차 매도가,{price_sell_2}')
            time.sleep(61 * 2)
    except Exception as err:
        print(type(err), err)
    finally:
        fp.close()
