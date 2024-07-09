from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest


class OrangePage:
    def __init__(self, driver):
        self.driver = driver
        self.forgot_link = (By.CLASS_NAME, "oxd-text.oxd-text--p.orangehrm-login-forgot-header")
        self.name_input = (By.XPATH, '//input[@placeholder="Username"]')
        self.reset_button = (By.XPATH, '//button[@type="submit"]')
        self.password_input = (By.XPATH, '//input[@placeholder="Password"]')
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.page_main = (By.CLASS_NAME, "oxd-main-menu-item active")
        self.page_main=(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
        # self.page_menu= (By.CLASS_NAME,"nav.oxd-topbar-body-nav")
        self.page_menu= (By. XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')

    def open(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(500, 500);")

    def fill_form(self, name):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.forgot_link)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)

    def click_reset(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.reset_button)).click()

    def header_validation(self, name, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_input)).send_keys(name)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def login_click(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_button)).click()

    def main_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.page_main)).click()

    def main_menu(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.page_menu)).click()
