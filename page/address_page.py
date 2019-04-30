from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddRessPage(BaseAction):
    add_contacts = By.XPATH,'//*[@content-desc="添加新联系人"]'

    def click_add_contacts(self):
        self.click_element(self.add_contacts)