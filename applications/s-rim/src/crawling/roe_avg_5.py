import pandas as pd
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup


def open_page(url) -> WebDriver:
    """
    :WebDriver: driver
    """
    driver_path = '/home/scottbae37/chromedriver'
    options: Options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.183 Safari/537.36')
    driver: WebDriver = webdriver.Chrome(driver_path, options=options)
    driver.get(url)
    return driver


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


if __name__ == '__main__':
    roe_pd = pd.read_csv('/home/scottbae37/git/s-rim-analysis/resource/roe_list.csv', engine='python')
    roe_list = []

    for i in roe_pd.index:
        (name, code) = roe_pd.loc[i, ['회사명','ROE_5년_평균']]
        roe_list.append((name, code))
    roe_list.sort(key=lambda v: v[1], reverse=True)
    fp = open('roe_avg_5.csv', 'w')
    for (name, roe) in roe_list:
        fp.write(f'{name},{roe}')
        fp.write(os.linesep)
    fp.close()
    print(roe_list)
    # pd_comp_code = pd.read_csv('/home/scottbae37/git/s-rim-analysis/resource/comp_code.csv', engine='python')
    # roe_list = []
    #
    # for i in pd_comp_code.index:
    #     (name, code) = pd_comp_code.loc[i, ["회사명", "회사코드"]]
    #     code = str(code).zfill(6)
    #     url = f'http://search.itooza.com/index.htm?seName={code}'
    #     driver = open_page(url)
    #     roe = roe_avg_5yr(name, code, driver)
    #     roe_list.append((name, roe))
    # roe_list.sort(key=lambda v: v[1], reverse=True)
    # fp = open('roe_avg_5.csv', 'w')
    # for (name, roe) in roe_list:
    #     fp.write(f'{name},{roe}')
    #     fp.write(os.linesep)
    # fp.close()
    # print(roe_list)
