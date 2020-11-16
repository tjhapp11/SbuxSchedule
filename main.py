import requests
import bs4
from selenium.webdriver import Chrome
import time



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loginPageURL = 'https://id.starbucks.com/SecureAuth87/SecureAuth.aspx?SAMLRequest=fZJRb9owFIX%2fSuR3J9jAAhYgUVDVSN0aAevDXirj3KzWEjvztWn77%2buEtWWTVskvvjrn3u8ee4GybTqxDv7R7OB3APRJsV2Sh%2fGcwzwfzyjw6Rc6UTmjs9E0p8eazyd8UlcMGEnuwaG2Zkl4OiJJgRigMOil8bE04iPKWDwHPhaciSlPx%2fnsB0m2cYo20g%2fOR%2b87FFmmqzQa3TGoX5gq22YIKjiQkWyWX1xSid0zSa6tUzBgL0ktG4R%2bfCkR9QneK6Wz3irbXGlTafNzSYIzwkrUKIxsAYVXYr%2f%2beisivjieRShuDoeSlnf7A0nWiOB6zo01GFpwe3AnreD77vaDHD3Sk0aqGhsq9s8WttaYkeS5bQyKIezPKbo%2fyGS16NViyNRd%2bD%2b3yzdgsupl98V%2bw0QEXGQX3c6tO%2fEt2ottaRutXvpAW%2bn%2f352lbKjoitaDVASDHShda6hiUk1jnzbxiXyM37sQ089W56l%2ff6%2fVKw%3d%3d&RelayState=https%253A%252F%252Fsso-stb.jdadelivers.com'
    UserID = 'US2078886'
    # res = requests.get('https://starbucks-wfmr.jdadelivers.com/retail')
    req = requests.get(loginPageURL)
    req.raise_for_status()
    # print(type(req))
    # print(res.status_code)

    loginPageWriter = open('LoginPage.txt', 'wb')
    # print(type(loginPageWriter))
    for chunk in req.iter_content(100000):
        loginPageWriter.write(chunk)
    # print(loginPageWriter.read)
    loginPageWriter.close()

    ###BeatifulSoup element-finding process. Outdated by selenium process below
    # loginPageSoup = bs4.BeautifulSoup(req.text, 'html.parser')
    # print(type(loginPageSoup))
    # loginButton = loginPageSoup.select('#ContentPlaceHolder1_MFALoginControl1_UserIDView_btnSubmit')
    # print(type(loginButton))
    # print(str(loginButton))
    ###End BeatifulSoup process

    browser = Chrome()
    # print(type(driver))
    browser.get(loginPageURL)
    time.sleep(5)
    IDTextBox = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$UserIDView$txtUserid')
    # print('id: ',IDTextBox.id, ' tag_name: ', IDTextBox.tag_name)
    IDTextBox.send_keys(UserID)
    IDSubmitButton = browser.find_element_by_name('ctl00$ContentPlaceHolder1$MFALoginControl1$UserIDView$btnSubmit')
    IDSubmitButton.click()