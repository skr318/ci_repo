from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest

# chromedriver = "/"
driver = webdriver.Chrome(executable_path='/home/circleci/project/chromedriver')
driver.set_window_size(1024, 600)
# driver.fullscreen_window()
driver.maximize_window()

def test_google():
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("Sanjev")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    assert driver.title == "Google"
