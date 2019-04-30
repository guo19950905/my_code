from page.add_person_page import AddPersonPage
from page.address_page import AddRessPage
from page.display_page import DisPlay
from page.first_network_page import FirstNetWorkPage
from page.first_page import FirstPage
from page.more_page import MorePage
from page.saved_page import SavedPage
from page.setting_page import SetTing


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def add_person(self):
        return AddPersonPage(self.driver)

    @property
    def add_ress(self):
        return AddRessPage(self.driver)

    @property
    def saved_page(self):
        return SavedPage(self.driver)

    @property
    def display_page(self):
        return DisPlay(self.driver)

    @property
    def first_page(self):
        return FirstPage(self.driver)

    @property
    def more_page(self):
        return MorePage(self.driver)


    @property
    def setting_page(self):
        return SetTing(self.driver)

    @property
    def first_network_page(self):
        return FirstNetWorkPage(self.driver)
