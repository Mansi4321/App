import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from keywords import open_application, login

@pytest.mark.usefixtures("setup")
class Test_KeywordDriven:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_run_keyword_script(self,setup):
        self.logger.info("************* Test_KeywordDriven **********")


        self.driver = setup
        self.driver.get(self.baseURL)


        open_application(self.driver, self.baseURL)
        login(self.driver, self.username, self.password)


