# 4. feladat: Műveletek karakterekkel

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(2)

# Find locators:
character = driver.find_element_by_id("chr")
operator = driver.find_element_by_id("op")
number = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

test_data = [""]
reference_data = [""]


def test_tc01():
    # Helyesen betöltődik az applikáció: Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
    # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    assert result.text == reference_data[0]


def test_tc02():
    # Megjelenik egy érvényes művelet:
    # `chr` megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
    # `op` mező vagy + vagy - karaktert tartlamaz
    # `num` mező egy egész számot tartalamaz

    assert result.text == reference_data[1]


def test_tc03():
    # Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
    # A megjelenő `chr` mezőben lévő karaktert kikeresve a táblában
    # Ha a `+` művelet jelenik meg akkor balra lépve ha a `-` akkor jobbra lépve
    # A `num` mezőben megjelenő mennyiségű karaktert
    # az `result` mező helyes karaktert fog mutatni

    assert result.text == reference_data[2]

# test_tc01()
# test_tc02()
# test_tc03()