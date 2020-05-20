from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.set_window_size(1024, 600)
# driver.fullscreen_window()
driver.maximize_window()

driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys("Sanjev")
driver.find_element_by_name("q").send_keys(Keys.ENTER)