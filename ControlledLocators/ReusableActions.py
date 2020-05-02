import logging
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Locators:

    def __init__(self, driver):
        self.driver = driver

    # Reusable methods in the complete Application

    # This function used to automate the complete Admin section details
    Admin_Text = (By.XPATH, "//b[contains(text(),'Admin')]")
    Search_Button = (By.XPATH, "//input[@id='searchBtn']")
    Add_Button = (By.XPATH, "//input[@id='btnAdd']")
    Save_Button = (By.XPATH, "//input[@id='btnSave']")
    Validation_Error_Id = (By.XPATH, "//span[@class='validation-error']")

    def getPresenceOfAdminText(self):
        return self.Admin_Text

    def getSearchButtonId(self):
        return self.Search_Button

    def getAddButtonId(self):
        return self.Add_Button

    def getSaveButtonId(self):
        return self.Save_Button

    # Methods to perform actions on the pages

    # Time Period to wait until element located
    def staticWaitTime(self):
        timeout = 30
        return timeout

    # Method to perform action on the Browser
    def backBrowserButton(self):
        self.driver.execute_script("window.history.go(-1)")

    # Method for Traceable actions
    def executionStartTime(self):
        starting = time.perf_counter()
        return round(starting)

    def executionStopTime(self):
        showtime = time.perf_counter()
        return round(showtime)

    def getValidationErrorId(self):
        return self.Validation_Error_Id

    # this function used to verify that data should already exist or not.
    def checkPresenceOfValidationError(self, by_locator, text):
        if self.checkPresenceofElement(self.getValidationErrorId()):
            print("Validation Error Exists")
            time.sleep(5)
            self.clearTheTextData(by_locator)
            rename_text = ("Rename" + str(text))
            print("Data should be renamed : " + str(rename_text))
            self.sendKeys(by_locator, rename_text)
            pass
        else:
            print("No Validation Error exists")
            pass

    # this function used to click on the button in any page.
    def click(self, by_locator):
        start = self.executionStartTime()
        print("Looking for an Element")
        WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator)).click()
        stop = self.executionStopTime()
        total_time = round(stop - start)
        print("Element should be found and clicked in - " + str(total_time) + "ms")

    # this function asserts comparison of a web element's text with passed in text.
    def verifyElementText(self, by_locator, element_text):
        start = self.executionStartTime()
        print("Searching for an element start")
        web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
            EC.visibility_of_element_located(by_locator))
        stop = self.executionStopTime()
        total_time = round(stop - start)
        print("Element should be found in - " + str(total_time) + "ms")
        assert web_element.text == element_text
        print("Element should be matched successfully")

    # this function return a web element's for used for any other purpose in the script.
    def getElementText(self, by_locator):
        web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
            EC.visibility_of_element_located(by_locator))
        print("Text should be present in Element locator is : " + str(web_element.text))
        return web_element.text

    # this function return a web element's value.
    def getElementValue(self, by_locator):
        web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(
            EC.visibility_of_element_located(by_locator))
        print("Value should be present in Element locator is : " + str(web_element.value))
        return web_element.value

    # this function clear the data added in the text field
    def clearTheTextData(self, by_locator):
        WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator)).clear()
        print("Element should be clear from the text field successfully")

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def sendKeys(self, by_locator, text):
        element = WebDriverWait(self.driver, self.staticWaitTime()).\
            until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        print("Data should be entered in the text field : " + str(text))
        return element

    # this function checks if the web element is present on the page or not whose locator has been passed to it
    def shouldBeDisplayed(self, by_locator):
        print("Start looking for an element")
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        print("Element should be displayed Successfully")
        return element

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def visibilityOfElement(self, by_locator):
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    # this function checks if the web element whose locator has been passed to it, is present on the web page or not.
    # return true or false depending upon its presence.
    def checkAssertion(self, by_locator, text):
        global not_found
        try:
            web_element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.presence_of_element_located(by_locator))
            if web_element.text == text:
                not_found = True
                print("Element should be found on the page")
        except:
            not_found = False
            print("No Element should be found on the page")
        return not_found

    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def mouseHoverToElement(self, by_locator):
        element = WebDriverWait(self.driver, self.staticWaitTime()).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
        print("Element should be displayed ")

    # this function return presence of Element on Web page or not.
    def checkPresenceofElement(self, by_locator):
        try:
            WebDriverWait(self.driver, self.staticWaitTime()).until(EC.presence_of_element_located(by_locator))
            not_found = True
            print("Element found on the page")
        except:
            not_found = False
            print("No Element should be found on the page")

        return not_found
