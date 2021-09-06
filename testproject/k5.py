# 5. feladat: Bingo

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")
time.sleep(2)

test_data = [25, 75]

# Select locators:
bingos = driver.find_elements_by_xpath('//*[@id="bingo-body"]//input')
numbers = driver.find_elements_by_xpath('//*[@id="numbers-list"]//input')
play_btn = driver.find_element_by_id("spin")
init_btn = driver.find_element_by_id("init")


def test_tc01():
    # Az applikáció helyesen megjelenik: A bingo tábla 25 darab cellát tartalmaz, A számlista 75 számot tartalmaz
    # Check the amounts:
    bingo_list = []
    for bingo in bingos:
        bingo_list.append(bingo.text)

    assert len(bingo_list) == test_data[0]

    num_list = []
    for num in numbers:
        num_list.append(num.text)

    assert len(num_list) == test_data[1]


def test_tc02():
    # Bingo számok ellenőrzése: Addig nyomjuk a `play` gobot amíg az első bingo felirat meg nem jelenik
    # Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki
    # Check if the numbers class name is checked in bingos and in numbers too:
    checked_bingo_list = driver.find_elements_by_xpath('//*[@id="bingo-body"]//td[@class="checked"]')
    checked_num_list = driver.find_elements_by_xpath('//*[@id="numbers-list"]//li[@class="checked"]')

    check_list = 0
    for i in range(test_data[1]):
        play_btn.click()
        for number in checked_num_list:
            if number in checked_bingo_list:
                check_list += 1

    assert check_list == 25


def test_tc03():
    # Új játékot tudunk indítani az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
    # új bingo szelvényt kapunk más számokkal.
    bingo_list = []
    for bingo in bingos:
        bingo_list.append(bingo.text)

    init_btn.click()
    time.sleep(1)

    bingo_list1 = []
    for bingo in bingos:
        bingo_list1.append(bingo.text)

    assert bingo_list != bingo_list1

# test_tc01()
# test_tc02()
# test_tc03()
