def test_registration_button_background_color(registration_page, browser):
    assert registration_page.get_register_btn_background_color() == 'rgba(210, 210, 255, 1)' \
        if browser.capabilities['browserName'] == 'chrome' else 'rgba(210, 210, 255)'
