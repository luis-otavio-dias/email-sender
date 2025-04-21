from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import re

from select_browser import make_chrome_browser


def remove_period(list: list) -> list:
    """
    Removes the period of an email into a given list.

    Parameters:
        list (list): A list with the strings to remove the period

    Returns:
        list: List of strings without the period.

    Example:
        >>> remove_period(["example@email.com."])
        ["example@email.com"]
    """

    email_cleaned = []

    for i in range(len(list)):
        dot_index = len(list[i]) - 1
        if list[i][dot_index] == ".":
            old_email = list[i]
            new_email = old_email[:dot_index]
            email_cleaned.append(new_email)

    return email_cleaned


def get_email(user_search: str):
    TIME_TO_WAIT = 10

    options = (
        "--headless",
        "--window-size=1920,1080",
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    )
    browser = make_chrome_browser(*options)
    browser.get("https://www.google.com")

    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, "q"),
        )
    )
    search_input.send_keys(user_search)
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(
        By.ID,
        "m-x-content",
    )

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, results.text)

    email_finded = []

    for email in emails:
        email_finded.append(email)
    sleep(TIME_TO_WAIT)

    browser.quit()

    email_list = remove_period(email_finded)
    return email_list
