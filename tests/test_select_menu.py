from page_objects.SelectMenuPage import *


@allure.title('Check selection from dropdown')
def test_dropdown(driver):
    select = Select(driver)
    select.open_page()
    select.select_value_from_dropdown()
    select.assert_selected_value_from_dropdown()


