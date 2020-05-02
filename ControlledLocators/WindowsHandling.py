

class WindowsHandling:

    def __init__(self, driver):
        self.driver = driver

    def perform_Action_On_New_Tab(self, expected_url):
        self.driver.implicitly_wait(5)
        allTabs = self.driver.window_handles
        for tab in allTabs:
            self.driver.switch_to_window(tab)
            if self.driver.current_url == expected_url:
                self.driver.switch_to_window(tab)
            else:
                self.driver.close()

    # Perform WindowHandler action and come back to main window
    def perform_Action_And_Back_To_Current_Tab(self, old_url, new_url):
        self.driver.find_element_by_xpath(old_url).click()
        self.driver.implicitly_wait(10)
        allWindows = self.driver.window_handles
        mainwin = ''
        for wind in allWindows:
            self.driver.switch_to_window(wind)
            self.driver.find_element_by_xpath(new_url)
            mainwin = wind
        self.driver.switch_to_window(mainwin)

    # Handle Popups displayed on the same window
    def close_Popup_And_Get_Main_Window(self, expected_url):
        allWindows = self.driver.window_handles
        mainWin = ''
        for wind in allWindows:
            self.driver.switch_to_window(wind)
            if self.driver.current_url == expected_url:
                mainWin = wind
            else:
                self.driver.close()
        self.driver.switch_to_window(mainWin)

    # frame_locator is either by id or name or any element locator to switch to frame
    def switch_To_Frame(self, frame_locator):
        self.driver.switch_to.frame(frame_locator)

    # Switch back to window from the frame
    def switch_To_Frame_And_Back_To_Window(self):
        self.driver.switch_to.default_content()
