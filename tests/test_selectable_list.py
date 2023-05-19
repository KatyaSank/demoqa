from page_objects.SelectableListPage import *


@allure.title('Check the page starting with unselected list lines')
def test_unselected_lines(driver):
    selectable_list = SelectableList(driver)
    selectable_list.open_page()
    selectable_list.maximize_window()
    selectable_list.assert_that_first_line_is_not_selected()
    selectable_list.assert_that_second_line_is_not_selected()
    selectable_list.assert_that_third_line_is_not_selected()
    selectable_list.assert_that_fourth_line_is_not_selected()


@allure.title('Check select/unselect list option for first line')
def test_first_line_in_selectable_list_selected_unselected(driver):
    selectable_list = SelectableList(driver)
    selectable_list.open_page()
    selectable_list.maximize_window()
    selectable_list.click_first_line()
    selectable_list.assert_that_first_line_is_selected()
    selectable_list.click_second_line()
    selectable_list.assert_that_first_line_is_selected()
    selectable_list.assert_that_second_line_is_selected()
    selectable_list.click_first_line()
    selectable_list.assert_that_first_line_is_not_selected()


@allure.title('Check select/unselect list option for second line')
def test_second_line_in_selectable_list_selected_unselected(driver):
    selectable_list = SelectableList(driver)
    selectable_list.open_page()
    selectable_list.maximize_window()
    selectable_list.click_second_line()
    selectable_list.assert_that_second_line_is_selected()
    selectable_list.click_third_line()
    selectable_list.assert_that_second_line_is_selected()
    selectable_list.assert_that_third_line_is_selected()
    selectable_list.click_second_line()
    selectable_list.assert_that_second_line_is_not_selected()


@allure.title('Check select/unselect list option for third line')
def test_third_line_in_selectable_list_selected_unselected(driver):
    selectable_list = SelectableList(driver)
    selectable_list.open_page()
    selectable_list.maximize_window()
    selectable_list.click_third_line()
    selectable_list.assert_that_third_line_is_selected()
    selectable_list.click_fourth_line()
    selectable_list.assert_that_third_line_is_selected()
    selectable_list.assert_that_fourth_line_is_selected()
    selectable_list.click_third_line()
    selectable_list.assert_that_third_line_is_not_selected()


@allure.title('Check select/unselect list option for fourth line')
def test_fourth_line_in_selectable_list_selected_unselected(driver):
    selectable_list = SelectableList(driver)
    selectable_list.open_page()
    selectable_list.maximize_window()
    selectable_list.click_fourth_line()
    selectable_list.assert_that_fourth_line_is_selected()
    selectable_list.click_third_line()
    selectable_list.assert_that_fourth_line_is_selected()
    selectable_list.assert_that_third_line_is_selected()
    selectable_list.click_fourth_line()
    selectable_list.assert_that_fourth_line_is_not_selected()
