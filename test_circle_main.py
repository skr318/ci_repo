from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import os

# chromedriver = "/"
os.chmod('driver/chromedriver', 0755) # e.g. os.chmod('/Users/user/Documents/my_project/chromedriver', 0755)
driver = webdriver.Chrome(executable_path='driver/chromedriver')
driver.set_window_size(1024, 600)
# driver.fullscreen_window()
driver.maximize_window()

def test_google():
    driver.get("https://www.google.com")
    driver.find_element_by_name("q").send_keys("Sanjev")
    driver.find_element_by_name("q").send_keys(Keys.ENTER)
    assert driver.title == "Google"
