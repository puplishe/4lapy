import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

class ParserBase:
    def __init__(self):
        self.driver = uc.Chrome()
        
    def find_element_text(self, value):
        element = self.driver.find_element(By.CSS_SELECTOR, value)
        return element.text

    def click_button(self, value):
        self.driver.find_element(By.CSS_SELECTOR, value).click()