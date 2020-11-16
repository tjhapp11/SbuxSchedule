import requests
import bs4


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # res = requests.get('https://starbucks-wfmr.jdadelivers.com/retail')
    req = requests.get('https://id.starbucks.com/SecureAuth87/SecureAuth.aspx?SAMLRequest=fZLdTuMwEIVfJfK98%2bMW2lhtpdIKEYldIlq42BvkOBOwSOzgsQu8PU667JaVlksfnTPz%2bdgLFF3b87V3T%2foWXjygi4rtkjxMGJzl57WkeSbO6LSqG5pX84rmKZvWbDqZsUyQ6B4sKqOXhMUpiQpED4VGJ7QLUspSmuaUzfcs5RPGWR5P0tkvEm3DFqWFG5NPzvXIk0TVcQjaystnjKXpEgTpLYhANp%2bdHGKB%2fRuJLo2VMGIvSSNahGF9KRDVAf4opTXOSNNeKF0r%2fbgk3mpuBCrkWnSA3Em%2bW%2f%2b45gGfV0cT8qv9vqTlzW5PojUi2IFzYzT6DuwO7EFJuLu9%2fkuODulBIZWt8XX2zy1MozAh0VvXauRj2d9T9L%2bRyWoxuPnYqT3Jfx8Xn8BkNdjui90m4wFwkZxMO47u%2bc8QL7alaZV8HwrthPv%2f9CzORkXVtBmt3GvsQapGQR2aalvzuglP5EL9zvrQfrI6bv36vVYf&RelayState=https%253A%252F%252Fsso-stb.jdadelivers.com')
    req.raise_for_status()
    # print(type(req))
    # print(res.status_code)

    loginPageWriter = open('LoginPage.txt', 'wb')
    # print(type(loginPageWriter))
    for chunk in req.iter_content(100000):
        loginPageWriter.write(chunk)
    print(loginPageWriter.read)
    loginPageWriter.close()

    loginPageSoup = bs4.BeautifulSoup(req.text, 'html.parser')
    # print(type(loginPageSoup))
    loginButton = loginPageSoup.select('#ContentPlaceHolder1_MFALoginControl1_UserIDView_btnSubmit')
    # print(type(loginButton))
