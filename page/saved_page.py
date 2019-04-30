from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SavedPage(BaseAction):
    my_name = By.ID,'com.android.contacts:id/large_title'

    def get_title_text(self):
        return self.get_text(self.my_name)