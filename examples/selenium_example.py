import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service = Service('path/to/chromedriver')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

sleep_time = 5

driver = webdriver.Chrome()

driver.get("https://www.python.org")
time.sleep(sleep_time)

search_box = driver.find_element(By.ID, "id-search-field")

search_box.send_keys("guide")
search_box.send_keys(Keys.RETURN)
time.sleep(sleep_time)

wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
style_guide_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Python Style Guide")))

style_guide_link.click()
time.sleep(sleep_time)

pep8_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "PEP 8")))

pep8_link.click()

time.sleep(sleep_time)

driver.quit()
