from tests.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    from tests.page_objects.search_result_page import SearchResultPage
    url_path = ""
    POSTCODE_INPUT_LOCATOR = (By.ID, "postcode")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[data-ft='btnSearchArea']")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "div.errorMessage")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_address(self, postcode: str) -> 'HomePage':
        self._type(self.POSTCODE_INPUT_LOCATOR, postcode)
        return self

    def click_search(self) -> 'SearchResultPage':
        submit_button = self._find(self.SUBMIT_BUTTON_LOCATOR)
        submit_button.click()
        from tests.page_objects.search_result_page import SearchResultPage
        return SearchResultPage(self.driver)

    def get_error_message_displayed(self):
        error_message_element = self._find(self.ERROR_MESSAGE_LOCATOR)
        return error_message_element.text
