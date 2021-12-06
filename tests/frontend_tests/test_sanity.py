def test_sanity_flow(registration_page, login_page, browser, ui_conf):
    browser.get(ui_conf.registration_page_url)
    registration_page.register_user(ui_conf.first_name,
                                    ui_conf.last_name,
                                    ui_conf.user_name,
                                    ui_conf.user_email,
                                    ui_conf.user_password)
    assert registration_page.is_registration_successful()
    browser.get(ui_conf.login_page_url)
    login_page.login(ui_conf.user_email, ui_conf.user_password)
    assert login_page.is_logged_in()
