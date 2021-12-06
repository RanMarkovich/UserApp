def test_registration_button_background_color(registration_page, browser, ui_conf):
    browser.get(ui_conf.registration_page_url)
    assert registration_page.get_register_btn_background_color() == 'rgba(210, 210, 255, 1)' \
        if browser.capabilities['browserName'] == 'chrome' else 'rgba(210, 210, 255)'
