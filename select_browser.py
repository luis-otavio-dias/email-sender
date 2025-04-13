from time import sleep

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROOT_FOLDER = Path(__file__).parent
DRIVER_PATH = ROOT_FOLDER / "drivers"

LAUNCHER_PATH = Path.home() / "AppData" / "Local" / "Programs"


def make_opera_browser(*options: str):
    OPERA_PATH = LAUNCHER_PATH / "Opera GX" / "opera.exe"
    OPERA_DRIVER_PATH = DRIVER_PATH / "opera_gx" / "chromedriver.exe"

    opera_options = Options()
    opera_options.add_experimental_option(
        "excludeSwitches",
        ["enable-logging"],
    )
    opera_options.binary_location = str(OPERA_PATH)
    opera_service = Service(executable_path=OPERA_DRIVER_PATH)
    opera_browser = webdriver.Chrome(
        service=opera_service,
        options=opera_options,
    )

    return opera_browser


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    CHROME_DRIVER_PATH = DRIVER_PATH / "chrome" / "chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10

    options = ()
    browser = make_chrome_browser(*options)

    browser.get("https://www.google.com")

    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, "q"),
        )
    )
    search_input.send_keys("Hello World!")
    search_input.send_keys(Keys.ENTER)

    sleep(TIME_TO_WAIT)
