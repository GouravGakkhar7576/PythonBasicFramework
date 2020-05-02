from BaseFiles.BaseClass import TestBaseClass
from Pages.LoginPage import LoginPage


class TestLoginData(TestBaseClass):

    def test_checkPresenceOfForgotPasswordText(self):
        global login
        login = LoginPage(self.driver)
        login.checkPresenceOfForgotPasswordText()

    def test_enterUsername(self):
        login.enterUsername()

    def test_enterPassword(self):
        login.enterPassword()

    def test_clickLoginButton(self):
        login.clickLoginButton()