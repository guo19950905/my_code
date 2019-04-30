from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=10,poll=1):
        by,value = loc
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(by,value))

    def click_element(self,loc):
        self.find_element(loc).click()

    def input_element(self,loc,value):
        self.clear_element(loc)
        self.find_element(loc).send_keys(value)

    def get_text(self,loc):
        return self.find_element(loc)

    def clear_element(self,loc):
        self.find_element(loc).clear()

    def click_back(self):
        self.driver.press_keycode(4)

