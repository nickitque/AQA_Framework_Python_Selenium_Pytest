from pages.page_404 import Page404

link = "https://takservice.pl/ru/deals/"


def test_guest_can_visit_404_page_and_back_to_home(browser):
    """Test for clicking the 'back to homepage' button."""
    page = Page404(browser, link)
    page.open()
    page.click_back_to_homepage_button()


def test_guest_can_see_subtitle_text(browser):
    """Test for the presence of subtitle text."""
    page = Page404(browser, link)
    page.open()
    page.check_subtitle_text()


def test_guest_can_see_error_code_text(browser):
    """Test for the presence of error code text."""
    page = Page404(browser, link)
    page.open()
    page.check_error_code_text()


def test_guest_can_see_message_text(browser):
    """Test for the presence of message text."""
    page = Page404(browser, link)
    page.open()
    page.check_message_text()
