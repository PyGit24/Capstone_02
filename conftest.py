import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="module")
def driver():
    # Using chrome Auto Installer
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Using Standalone Installer
    paths = r"D:\ProgramS\PyCharm\chromedriver.exe"
    # paths = r"E:\PyCharm\chromedriver.exe"
    os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()