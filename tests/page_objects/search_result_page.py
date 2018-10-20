from tests.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchResultPage(BasePage):

    url_path = "area/{}"
    RESTAURANT_RESULT_LOCATOR = (By.CSS_SELECTOR, 'div[itemtype="http://schema.org/Restaurant"]')
    RESTAURANT_RESULT_MESSAGE_LOCATOR = (By.CSS_SELECTOR, 'div[data-ft="serpHeaderMobile"] p')
    RESTAURANT_RESULT_COUNT_LOCATOR = (By.CSS_SELECTOR, 'span.c-serp__header--count')

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, area_code) -> 'SearchResultPage':
        self.get_url().format(area_code)
        self.driver.get(self.get_url())
        return self

    def get_number_of_restaurants_displayed(self):
        return len(self._find_all(self.RESTAURANT_RESULT_LOCATOR))

    def get_restaurants_result_message(self):
        message_element = self._find(self.RESTAURANT_RESULT_MESSAGE_LOCATOR)
        message = message_element.get_attribute("innerText")
        return message

    def get_restaurants_result_count(self):
        return self._find(self.RESTAURANT_RESULT_COUNT_LOCATOR)
