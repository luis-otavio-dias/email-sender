from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re

from select_browser import make_chrome_browser


TIME_TO_WAIT = 10

options = ()
browser = make_chrome_browser(*options)
browser.get("https://www.google.com")

search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, "q"),
    )
)
search_input.send_keys("e mail rh da empresa ideal ctvm")
search_input.send_keys(Keys.ENTER)

results = browser.find_element(
    By.ID,
    "m-x-content",
)

email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(email_pattern, results.text)

for email in emails:
    print(email)
sleep(TIME_TO_WAIT)

browser.quit()
