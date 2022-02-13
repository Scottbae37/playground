from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def open_page() -> WebDriver:
    """
    :WebDriver: driver
    """
    yield_url = 'https://www.kisrating.com/ratingsStatistics/statics_spread.do'
    driver_path = '/home/scottbae37/chromedriver'
    options: Options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.183 Safari/537.36')
    driver: WebDriver = webdriver.Chrome(driver_path, options=options)
    driver.get(yield_url)
    return driver


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


def get_bond_yield() -> float:
    driver = open_page()
    validate_page(driver)
    xpath_bbb_minus = '//*[@id="con_tab1"]/div[2]/table/tbody/tr[11]/td[9]'
    bbb_minus_yield = driver.find_element_by_xpath(xpath_bbb_minus).text
    driver.quit()
    return float(bbb_minus_yield)


if __name__ == '__main__':
    required_profit_rate = get_bond_yield()
    print(required_profit_rate)
