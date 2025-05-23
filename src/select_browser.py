from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent.parent
DRIVER_PATH = ROOT_FOLDER / "drivers"

LAUNCHER_PATH = Path.home() / "AppData" / "Local" / "Programs"


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    CHROME_DRIVER_PATH = DRIVER_PATH / "chrome" / "chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled",
    )

    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"],
    )
    chrome_options.add_experimental_option("useAutomationExtension", False)

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return browser
