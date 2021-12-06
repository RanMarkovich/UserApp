def test_field_checker_displays_when_fields_are_empty(login_page, browser, ui_conf):
    """
    1. Opens login page
    2. Clicks login button
    3. Asserts 'check all fields' message is persent
    """

    browser.get(ui_conf.login_page_url)
    login_page.click_login_btn()
    assert login_page.is_field_checker_visible()
