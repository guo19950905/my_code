from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstNetWorkPage(BaseAction):

    network_2g = By.XPATH,"//*[contains(@text,'2G')]"
    network_3g = By.XPATH,"//*[contains(@text,'3G')]"

    def click_network_2G(self):
        self.click_element(self.network_2g)

    def click_network_3G(self):
        self.click_element(self.network_3g)