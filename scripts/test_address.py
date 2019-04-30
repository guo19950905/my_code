from time import sleep

import pytest

from base.base_driver import get_driver
from page.page import Page


class TestAddRess:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize(('name','phone'),[('哈哈红','10086444000'),('哈是红','10086444000'),('哈哈咯','10086444000')])
    def test_phone(self,name,phone):
        self.page.add_ress.click_add_contacts()
        self.page.add_person.input_name(name)
        self.page.add_person.input_phone(phone)
        self.page.add_person.click_back()
        sleep(2)
        assert self.page.saved_page.get_title_text().text == name