from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    base_url = 'https://www.just-eat.co.uk'
    url_path = None

    def __init__(self, driver: webdriver):
        self.driver = driver

    def get_url(self, **kwargs):
        url = "/".join([self.base_url, self.url_path])
        url = url.format(kwargs)
        return url

    def open(self, **kwargs) -> 'BasePage':
        self.driver.get(self.get_url(**kwargs))
        return self

    def _find(self, locator):
        return self.driver.find_element(*locator)

    def _find_all(self, locator):
        return self.driver.find_elements(*locator)

    def _type(self, locator, text):
        text_area = self._find(locator)
        text_area.clear()
        text_area.send_keys(text)
        return self
