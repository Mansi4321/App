from pageObjects.LoginPage import LoginPage


def open_application(driver, url):
    driver.get(url)

def login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.setUserName(username)
    login_page.setPassword(password)
    login_page.clickLogin()