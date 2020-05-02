from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Waits:
    def __init__(self, driver):
        self.driver = driver

    def staticWaitTime(self):
        global timeperiod
        timeperiod = 30
        return timeperiod

    def waitForPageToBeLoad(self):
        self.driver.implicitly_wait(timeperiod)

    def waitForElementToBeLocated(self, by_locator):
        wait = WebDriverWait(self.driver, timeperiod)
        wait.until(EC.visibility_of_element_located(by_locator))
