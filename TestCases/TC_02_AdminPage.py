from BaseFiles.BaseClass import Login_Application
from Pages.AdminPage import AdminPage


class TestAdminData(Login_Application):

    def test_checkPresenceOfPendingLeaveRequestText(self):
        global admin
        admin = AdminPage(self.driver)
        admin.checkPresenceOfPendingLeaveRequestText()

    def test_checkPresenceOfAdminText(self):
        admin.moveCursorToAdminText()

    def test_checkPresenceOfUserManagementText(self):
        admin.moveCursorToUserManagementText()

    def test_clickUsersButton(self):
        admin.clickOnTheUsersButton()

    def test_enterSystemUserName(self):
        admin.enterSystemUserName()

    def test_selectUserRole(self):
        admin.selectUserRoleValue()

    def test_enterEmployeeName(self):
        admin.enterEmployeeName()

    def test_selectEmployeeStatus(self):
        admin.selectEmployeeStatus()

    def test_clickSearchButton(self):
        admin.clickSearchButton()

    def test_checkPresenceOfStatusColumn(self):
        admin.checkPresenceOfStatusColumn()

    def test_checkPresenceOfStatusColumnValue(self):
        admin.checkPresenceOfStatusColumnValue()