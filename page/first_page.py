from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class FirstPage(BaseAction):
    first_network = By.XPATH,'//*[@text="首选网络类型"]'

    def click_first_network(self):
        self.click_element(self.first_network)

