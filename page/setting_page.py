from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SetTing(BaseAction):
    more = By.XPATH,'//*[@text="更多"]'
    display = By.XPATH,'//*[@text="显示"]'

    def click_more(self):
        self.click_element(self.more)

    def click_display(self):
        self.click_element(self.display)

