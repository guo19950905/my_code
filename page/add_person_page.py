from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddPersonPage(BaseAction):
    name = By.XPATH,'//*[@text="姓名"]'
    phone = By.XPATH,'//*[@text="电话"]'
    back_button = By.XPATH,'//*[@content-desc="向上导航"]'
    def input_name(self,value):
        self.input_element(self.name,value)

    def input_phone(self,value):
        self.input_element(self.phone,value)

    def click_back(self):
        self.click_element(self.back_button)

