from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'user'

class AbstractPageObject(object):

    def __init__(self, driver):
        self.driver = driver

    def waitingForAPage(self, by, locator):
        self.waitingForAElement(by, locator)

    def waitingForAElement(self, by, locator):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(by, locator))

class MainPage(AbstractPageObject):

    def __init__(self, driver):
        self.driver = driver
        self.waitingForAPage(By.ID, "short_text")

    def search_some_commodity(self, name):
        self.driver.find_element(By.CLASS_NAME, "header-search-input-text").send_keys(name)
        self.driver.find_element(By.CLASS_NAME, "btn-link-i").click()

class SearchResultsPage(AbstractPageObject):

    def __init__(self, driver):
        self.driver = driver
        self.waitingForAPage(By.CLASS_NAME, "search-result-count")

    def is_commodity_enable(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".g-i-list-status.available")
            return True
        except WebDriverException:
            return False

    def get_commodity_price(self):
        value = self.driver.find_element(By.CLASS_NAME, "g-i-list-price-uah").text
        return int(filter(lambda x: x.isdigit(), value))