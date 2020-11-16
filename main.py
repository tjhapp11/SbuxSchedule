import requests
import bs4
from selenium.webdriver import Chrome
import time


def init_browser():
    browser = Chrome()
    return browser


def page_writer(url, text_doc, mode):
    req = requests.get(login_page_url)
    req.raise_for_status()
    writer = open(text_doc, mode)
    # print(type(loginPageWriter))
    for chunk in req.iter_content(100000):
        writer.write(chunk)
    # print(loginPageWriter.read)
    writer.close()


def login(browser):
    browser.get(login_page_url)
    time.sleep(5)

    id_text_box = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$UserIDView$txtUserid')
    id_text_box.send_keys(user_id)
    ##id_text_box.submit() #not functional
    id_submit_button = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$UserIDView$btnSubmit')
    id_submit_button.click()
    time.sleep(5)

    security_question = browser.find_element_by_id('ContentPlaceHolder1_MFALoginControl1_KBARegistrationView_lblKBQ1')
    security_answer = input(security_question.text)
    security_text_box = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$KBARegistrationView$tbxKBA1')
    security_text_box.send_keys(security_answer)
    #security_text_box.submit()
    security_submit_button = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$KBARegistrationView$btnSubmit')
    security_submit_button.click()
    time.sleep(5)

    pass_text_box = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$PasswordView$tbxPassword')
    pass_answer = input('Password: ')
    pass_text_box.send_keys(pass_answer)
    pass_submit_button = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$PasswordView$btnSubmit')
    pass_submit_button.click()
    time.sleep(5)


def nav_to_schedule(browser):
    #TODO: Navigate to schedule editor page


def record_weekly_schedule(browser):
    #TODO: Read and record weekly schedule


def sync_schedule_google(browser, weekly_schedule):
    #TODO: Synchronise recorded schedule to google calendar
    #TODO also: learn how to do this


if __name__ == '__main__':
    login_page_url = 'https://id.starbucks.com/SecureAuth87/SecureAuth.aspx?SAMLRequest=fZJRb9owFIX%2fSuR3J9jAAhYgUVDVSN0aAevDXirj3KzWEjvztWn77%2buEtWWTVskvvjrn3u8ee4GybTqxDv7R7OB3APRJsV2Sh%2fGcwzwfzyjw6Rc6UTmjs9E0p8eazyd8UlcMGEnuwaG2Zkl4OiJJgRigMOil8bE04iPKWDwHPhaciSlPx%2fnsB0m2cYo20g%2fOR%2b87FFmmqzQa3TGoX5gq22YIKjiQkWyWX1xSid0zSa6tUzBgL0ktG4R%2bfCkR9QneK6Wz3irbXGlTafNzSYIzwkrUKIxsAYVXYr%2f%2beisivjieRShuDoeSlnf7A0nWiOB6zo01GFpwe3AnreD77vaDHD3Sk0aqGhsq9s8WttaYkeS5bQyKIezPKbo%2fyGS16NViyNRd%2bD%2b3yzdgsupl98V%2bw0QEXGQX3c6tO%2fEt2ottaRutXvpAW%2bn%2f352lbKjoitaDVASDHShda6hiUk1jnzbxiXyM37sQ089W56l%2ff6%2fVKw%3d%3d&RelayState=https%253A%252F%252Fsso-stb.jdadelivers.com'
    user_id = 'US2078886'

    page_writer(login_page_url, 'LoginPage.txt', 'wb')

    selenium_browser = init_browser()
    login(selenium_browser)
