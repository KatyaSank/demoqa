import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

# from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    s = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


# @pytest.fixture
# def open_page(driver):
#     browser.get('https://academybugs.com/#')


# def pytest_addoption(parser):
#     parser.addoption("--address", action="store", default="http://192.168.122.244/", help="HuntBox web address")
#     parser.addoption("--browser", action="store", default="firefox", help="Browser name")


# import time
# from datetime import datetime
# import pytest
# import os
# from selenium import webdriver as selenium_webdriver
# from selenium.webdriver.chrome.options import Options
#
# # set up webdriver fixture
# @pytest.fixture(scope='session')
# def driver(request):
#     chrome_options = Options()
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#
#     driver = selenium_webdriver.Chrome(options=chrome_options)
#     driver.set_window_size(1920, 1080)
#     driver.maximize_window()
#     driver.implicitly_wait(5)
#
#     yield driver
#     driver.quit()
#
# # set up a hook to be able to check if a test has failed
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)
#
# # check if a test has failed
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     yield
#     # request.node is an "item" because we use the default
#     # "function" scope
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             driver = request.node.funcargs['driver']
#             take_screenshot(driver, request.node.nodeid)
#             print("executing test failed", request.node.nodeid)
#
# # make a screenshot with a name of the test, date and time
# def take_screenshot(driver, nodeid):
#     time.sleep(1)
#     file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/","_").replace("::","__")
#     driver.save_screenshot(file_name)