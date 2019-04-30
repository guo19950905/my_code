from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class DisPlay(BaseAction):

    fdj = By.XPATH,'//*[@content-desc="搜索"]'
    sousu = By.XPATH,'//*[@text="搜索…"]'
    def click_fdj(self):
        self.click_element(self.fdj)

    def input_fdj(self,value):
        self.input_element(self.sousu,value)