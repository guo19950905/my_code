from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MorePage(BaseAction):
    phone_network = By.XPATH,'//*[@text="移动网络"]'

    def click_phone_network(self):
        self.click_element(self.phone_network)
