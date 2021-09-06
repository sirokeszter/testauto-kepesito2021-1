# 1. feladat: Pitagorasz-tétel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")
time.sleep(2)

# Find locators:
input_a = driver.find_element_by_id('a')
input_b = driver.find_element_by_id('b')
result_c = driver.find_element_by_id('result')


def pith(a, b):
    submit_btn = driver.find_element_by_id('submit')

    input_a.clear()
    time.sleep(1)
    input_a.send_keys(a)
    input_b.clear()
    time.sleep(1)
    input_b.send_keys(b)
    submit_btn.click()
    time.sleep(2)


# Select separeted test data:
test_data = [["", ""], [2, 3], ["", ""]]
reference_data = [False, "10", "NaN"]


def test_tc01():
    # * Helyesen jelenik meg az applikáció betöltéskor: a: <üres>, b: <üres>, c: <nem látszik>
    assert input_a.get_attribute("value") == test_data[0][0]
    assert input_b.get_attribute("value") == test_data[0][1]
    assert result_c.is_displayed() == reference_data[0]


def test_tc02():
    # Számítás helyes, megfelelő bemenettel: a: 2, b: 3, c: 10
    pith(test_data[1][0], test_data[1][1])
    assert result_c.text == reference_data[1]


def test_tc03():
    #  Üres kitöltés: a: <üres>, b: <üres>, c: NaN
    pith(test_data[2][0], test_data[2][1])
    assert result_c.text == reference_data[2]

# test_tc01()
# test_tc02()
# test_tc03()

