def test_sanity_flow(pages, browser, ui_conf):
    browser.get(ui_conf.registration_page_url)
    pages.register_user(ui_conf.first_name,
                             ui_conf.last_name,
                             ui_conf.user_name,
                             ui_conf.user_email,
                             ui_conf.user_password)
    assert pages.is_registration_successful()
    browser.get(ui_conf.login_page_url)
    pages.login(ui_conf.user_email, ui_conf.user_password)
    assert pages.is_logged_in()
