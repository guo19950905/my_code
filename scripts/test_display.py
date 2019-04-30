from base.base_driver import get_driver
from page.page import Page


class T1estDisPlay:

    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_display(self):
        self.page.setting_page.click_display()
        self.page.display_page.click_fdj()
        self.page.display_page.input_fdj('hello')
        self.page.display_page.click_back()
