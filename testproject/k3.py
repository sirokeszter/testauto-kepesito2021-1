# 3. feladat: Alfanumerikus mező

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")
time.sleep(2)


def input_char(char):
    input_field = driver.find_element_by_id("title")

    input_field.clear()
    input_field.send_keys(char)


test_data = ["abcd1234", "teszt233@", "abcd"]
reference_data = [False, "Only a-z and 0-9 characters allewed", "Title should be at least 8 characters; you entered 4."]

error_msg = driver.find_element_by_xpath("//span")

def test_tc01():
    # Helyes kitöltés esete: title: abcd1234, Nincs validációs hibazüzenet
    input_char(test_data[0])
    assert error_msg.is_displayed() == reference_data[0]


def test_tc02():
    # Illegális karakterek esete: title: teszt233@, Only a-z and 0-9 characters allewed.
    input_char(test_data[1])
    assert error_msg.text == reference_data[1]


def test_tc03():
    # Túl rövid bemenet esete: title: abcd, Title should be at least 8 characters; you entered 4.
    input_char(test_data[2])
    assert error_msg.text == reference_data[2]

# test_tc01()
# test_tc02()
# test_tc03()
