from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from .select_browser import make_chrome_browser


def remove_period(string: str) -> str:
    """
    Removes the period of a string.

    Parameters:
        str (str): A string to remove the period.

    Returns:
        str: String without the period.

    Example:
        >>> remove_period("example@email.com.")
        "example@email.com"
    """

    string_cleaned = string
    dot_index = len(string) - 1
    for i in range(len(string)):
        if string[dot_index] == ".":
            string_cleaned = string[:dot_index]

    return string_cleaned


def get_email(user_search: str) -> list:
    """
    Gets a list with emails (strings) by google search.

    Parameters:
        user_search (str): A text to do the search.

    Returns:
        list: String list with founded emails.

    """
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

    results = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (
                By.ID,
                "m-x-content",
            )
        )
    )

    email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    emails = re.findall(email_pattern, results.text)

    browser.quit()

    return emails
