from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Library import ConfigReader
import pytest

driver = None


@pytest.fixture(scope="class")
def startBrowser(request):
    global driver

    if (ConfigReader.readConfigData('Details', 'Browser')) == 'Chrome':
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)
    elif (ConfigReader.readConfigData('Details', 'Browser')) == 'firefox':
        path = "./Driver/geckodriver.exe"
        driver = Firefox(executable_path=path)
    else:
        path = "./Driver/chromedriver.exe"
        driver = Chrome(executable_path=path)

    driver.get(ConfigReader.readConfigData('Details', 'Application_URL'))
    #    driver.implicitly_wait(20)
    #    driver.set_page_load_timeout(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()