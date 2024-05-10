import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver=webdriver.Ie()
    return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setupp method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hookk for Adding Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'nop Commerce'
    metadata['Module Name'] = 'Customers'
    metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
#@pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)