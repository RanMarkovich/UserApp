def test_login_with_non_existing_credentials(login_page, browser, ui_conf):
    """
    1. Opens login page
    2. Tries to login with non-existing user credentials
    3. Asserts Login Failed error message is present
    """

    login_page.login(ui_conf.user_email, ui_conf.user_password)
    assert not login_page.is_logged_in()
