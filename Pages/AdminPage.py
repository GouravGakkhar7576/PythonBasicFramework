from selenium.webdriver.common.by import By

from ControlledLocators.DropDownPage import DropDownPage
from ControlledLocators.ReusableActions import Locators


class AdminPage(Locators):

    def __init__(self, driver):
        super().__init__(driver)

    # Admin Page Locators
    Pending_Leave_Request_Text = (By.XPATH, "//legend[contains(text(),'Pending Leave Requests')]")
    User_Management_Text = (By.XPATH, "//a[@id='menu_admin_UserManagement']")
    Users_Button = (By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")
    Username_Text = (By.XPATH, "//input[@id='searchSystemUser_userName']")
    User_Role_DropDown = "//select[@id='searchSystemUser_userType']"
    Employee_Name_Text = (By.XPATH, "//input[@id='searchSystemUser_employeeName_empName']")
    Status_DropDown = "//select[@id='searchSystemUser_status']"
    Reset_Button = (By.XPATH, "//input[@id='resetBtn']")
    Column_Status_Id = (By.XPATH, "//a[@class='null'][contains(text(),'Status')]")
    Table_Id = (By.XPATH, "//table[@id='resultTable']")
    Enabled_Status_Id = (By.XPATH, "//tr[@class='odd']//td[contains(text(),'Enabled')]")

    # Test Data
    Presence_Of_Pending_Text = "Pending Leave Requests"
    Username = "Admin"
    Employee_Name = "Admin"
    UserRole = "Admin"
    Status = "Enabled"
    Column_Name = "Status"
    Column_Value = "Enabled"

    # Get Locator Ids Actions Performed
    def getPresenceOfPendingLeaveRequestText(self):
        return self.Pending_Leave_Request_Text

    def getPresenceOfUserManagementText(self):
        return self.User_Management_Text

    def getPresenceOfUsersButton(self):
        return self.Users_Button

    def getUsernameTextId(self):
        return self.Username_Text

    def getUserName(self):
        return self.Username

    def getUserRoleList(self):
        return self.User_Role_DropDown

    def getEmployeeNameId(self):
        return self.Employee_Name_Text

    def getEmployeeName(self):
        return self.Employee_Name

    def getStatusList(self):
        return self.Status_DropDown

    def getColumnNameId(self):
        return self.Column_Status_Id

    def getColumnValueId(self):
        return self.Enabled_Status_Id

    # Check Presence of element Actions Performed
    def checkPresenceOfPendingLeaveRequestText(self):
        self.verifyElementText(self.getPresenceOfPendingLeaveRequestText(), self.Presence_Of_Pending_Text)
        return AdminPage(self.driver)

    def checkPresenceOfStatusColumn(self):
        for col in self.Table_Id:
            self.verifyElementText(self.getColumnNameId(), self.Column_Name)
        return AdminPage(self.driver)

    def checkPresenceOfStatusColumnValue(self):
        for col in self.Table_Id:
            self.verifyElementText(self.getColumnValueId(), self.Column_Value)
        return AdminPage(self.driver)

    # Click Actions Performed
    def clickOnTheUsersButton(self):
        self.click(self.Users_Button)
        return AdminPage(self.driver)

    def clickSearchButton(self):
        self.click(self.getSearchButtonId())

    # Mouse Hover Actions Performed
    def moveCursorToAdminText(self):
        self.mouseHoverToElement(self.getPresenceOfAdminText())

    def moveCursorToUserManagementText(self):
        self.mouseHoverToElement(self.getPresenceOfUserManagementText())
        return AdminPage(self.driver)

    # Enter Data in to the text field Actions Performed
    def enterSystemUserName(self):
        self.sendKeys(self.getUsernameTextId(), self.getUserName())
        return AdminPage(self.driver)

    def enterEmployeeName(self):
        self.sendKeys(self.getEmployeeNameId(), self.getEmployeeName())
        return AdminPage(self.driver)

    # Select Value from Drop Down Actions Performed
    def selectUserRoleValue(self):
        global drop
        drop = DropDownPage(self.driver)
        drop.Select_By_Visible_Text_From_DropDown(self.getUserRoleList(), self.UserRole)
        return AdminPage(self.driver)

    def selectEmployeeStatus(self):
        drop.Select_By_Visible_Text_From_DropDown(self.getStatusList(), self.Status)
        return AdminPage(self.driver)
