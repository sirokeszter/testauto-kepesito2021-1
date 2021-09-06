# 2. feladat: Színes reakció

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(2)

# Find locators:

start_btn = driver.find_element_by_id("start")
stop_btn = driver.find_element_by_id("stop")
random_color = driver.find_element_by_id("randomColorName")
test_color = driver.find_element_by_id("testColorName")
result = driver.find_element_by_id("result")

# Make a list from colors:
all_colors = driver.find_element_by_id("allcolors").text
color_list = all_colors.replace('"', "").split(", ")

print(color_list)


def test_tc01():
    # Alapból egy random kiválasztott szín jelenik meg az `==` bal oldalanán. A jobb oldalon csak a `[  ]` szimbólum látszik. <szín neve> [     ] == [     ]
    random_col_in = []
    for color in color_list:
        if random_color.text == color:
            random_col_in.append(color)
        assert random_col_in == random_color.text

    # Check the test color is empty:
    assert test_color.text == ""


def test_tc02():
    # El lehet indítani a játékot a `start` gommbal. Ha elindult a játék akkor a `stop` gombbal le lehet állítani.
    # Collect the colors after click start button:
    test_list = []
    for i in color_list:
        start_btn.click()
        test_list.append(i)

    assert len(test_list) != 0

    # Check click stop button the len of the test_list1 is < than test_list
    test_list1 = []
    for i in color_list:
        start_btn.click()
        test_list1.append(i)
        stop_btn.click()
        break

    assert len(test_list) > len(test_list1)


def test_tc03():
    # Eltaláltam, vagy nem találtam el. Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le
    # amikor a bal és a jobb oldal ugyan azt a színt tartalmazza akkor a `Correct!` felirat jelenik meg.
    # ha akkor amikor eltérő szín van a jobb és bal oldalon akkor az `Incorrect!` felirat kell megjelenjen.
    if random_color.text == test_color.text:
        assert result.text == "Correct!"
    else:
        assert result.text == "Incorrect!"


# test_tc01()
# test_tc02()
# test_tc03()
