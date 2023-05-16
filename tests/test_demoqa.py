from page_objects.Base import Base


# def test_progress_bar(driver):
#     base = Base(driver)
#     base.get_url('https://demoqa.com/progress-bar')
#     base.get_locator_by_xpath('//*[@id="startStopButton"]').click()
#     time.sleep(2)
#     base.get_locator_by_xpath('//*[@id="startStopButton"]').click()
#     assert base.get_attribute_by_xpath_any_attribute('//*[@id="progressBar"]/div', 'aria-valuenow') != 0
    # base.get_locator_by_xpath('//*[@id="startStopButton"]').click()
    # base.get_element_by_attribute('//*[@id="progressBar"]/div')
    # assert base.get_locator_by_xpath('//*[@id="resetButton"]').text == 'Reset'
