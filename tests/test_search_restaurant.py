import os
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.page_objects.home_page import HomePage
from tests.page_objects.search_result_page import SearchResultPage

# run all tests
scenarios('features')


@fixture()
def browser():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    _browser = WebDriver(os.path.join(dir_path, "chromedriver.exe"))
    yield _browser
    _browser.close()


@given(parsers.parse('I want food in "{postcode}"'))
def given_justeat_page_with_address(browser, postcode):
    HomePage(browser).open().enter_address(postcode)


@given(parsers.parse('I want food in an invalid location'))
def given_justeat_page_with_invalid_address(browser):
    HomePage(browser).open().enter_address('random')


@when("I search for restaurants")
def when_search_for_restaurants(browser):
    HomePage(browser).click_search()


@then(parsers.parse('I should see some restaurants in "{text}"'))
def then_restaurants_should_be_found(browser, text):
    search_results_page = SearchResultPage(browser)
    assert search_results_page.get_number_of_restaurants_displayed() > 0
    assert int(search_results_page.get_restaurants_result_count().text) > 0
    assert text in search_results_page.get_restaurants_result_message()


@then('I should see an error message')
def then_restaurants_should_be_found(browser):
    home_page = HomePage(browser)
    assert home_page.get_error_message_displayed() == 'Please enter a full, valid postcode'


# Helpful tips:
# run individually
# from pytest_bdd import scenario
# @scenario('features/search_resturant.feature', 'Search for restaurants in an area')
# @scenario('features/search_resturant.feature', 'Search for restaurants in a different area')
# @scenario('features/search_resturant.feature', 'Search for restaurants in an invalid area')
# def test_search_for_restaurants():
#    pass
