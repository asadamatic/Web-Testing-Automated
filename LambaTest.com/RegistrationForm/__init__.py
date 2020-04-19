from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()

browser.get('https://accounts.lambdatest.com/register')


def verifyExpectedElements():

    logo = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/a/img')

    signupText = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/h1')

    termsText = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[1]/a[2]')

    privacyText = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[1]/a[1]')

    signInLink = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[2]/a')

    return logo.is_displayed() and signupText.is_displayed() and termsText.is_displayed() and privacyText.is_displayed() and signInLink.is_displayed()


def termsLinkRedirection():

    termsLink = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[1]/a[2]')
    termsLink.click()

    windows = browser.window_handles

    for window in windows:

        browser.switch_to.window(window)


    url = browser.current_url

    title = browser.title

    return url, title


def privacyLinkRedirection():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    privacyLink = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[1]/a[1]')
    privacyLink.click()

    windows = browser.window_handles

    for window in windows:

        browser.switch_to.window(window)


    url = browser.current_url

    title = browser.title

    return url, title



def loginLinkRedirection():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    loginLink = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[7]/p[2]/a')
    loginLink.click()

    url = browser.current_url

    title = browser.title

    return url, title


def logoRedirection():

    browser.back()

    logo = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/a/img')
    logo.click()

    windows = browser.window_handles

    for window in windows:

        browser.switch_to.window(window)

    url = browser.current_url

    title = browser.title

    return url, title

def registrationWithValidInput():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testfinal@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('5748923094')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    logout()

    return url, title

def registrationWithEmptyFullName():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testName2@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('8274950684')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title


def registrationWithEmptyEmail():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('3829784568')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)
    
    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title


def registrationWithInvalidEmail():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testActor@test.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('8374058456')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title


def registrationWithAlreadyRegisteredEmail():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testActor@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('5678983457')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title
    
    clearFields()

    return url, title


def registrationWithEmptyPassword():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testName2@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('3475987610')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title
    
def registrationWithInvalidPassword():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testName2@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('1234567')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('2345765489')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title


def registrationWithEmptyPhone():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testName2@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)
    
    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title

def registrationWithInvalidPhone():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('testName2@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('Test Compnay Name')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('123')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)

    url = browser.current_url

    title = browser.title

    clearFields()

    return url, title

def registrationWithEmptyCompanyName():

    signupWindow = browser.window_handles[0]

    browser.switch_to.window(signupWindow)

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')
    fullNameField.send_keys('Test Actor Name')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    emailField.send_keys('finalName@gmail.com')

    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    passwordField.send_keys('12345678')

    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    compnayNameField.send_keys('')

    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    phoneField.send_keys('5678940987')

    signupButton = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[6]/button')
    signupButton.click()

    sleep(2)
    
    url = browser.current_url

    title = browser.title

    logout()

    return url, title


def clearFields():

    fullNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[1]/input')

    emailField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[2]/input')
    
    passwordField = browser.find_element_by_xpath('//*[@id="userpassword"]')
    
    compnayNameField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[4]/input')
    
    phoneField = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/form/div[5]/input')
    
    fullNameField.clear()

    emailField.clear()

    passwordField.clear()

    compnayNameField.clear()

    phoneField.clear()


def logout():

    dropDownLink = browser.find_element_by_xpath('//*[@id="navbarDropdown"]')
    dropDownLink.click()

    logoutLink = browser.find_element_by_xpath('//*[@id="navbarSupportedContent"]/ul[2]/li/div/a[4]')
    logoutLink.click()

    browser.get('https://accounts.lambdatest.com/register')

def closeBrowser():

    browser.quit()


closeBrowser()


    
