from time import sleep

from base.base_driver import get_driver
from page.page import Page


class T1estNetWork3G:

    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_betwork_2g(self):
        self.page.setting_page.click_more()
        self.page.more_page.click_phone_network()
        self.page.first_page.click_first_network()
        sleep(2)
        self.page.first_network_page.click_network_3G()