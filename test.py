from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# this package can manipulate websites and click on buttons based off of thier names. that way we can adapt this to many kind of websites.
# https://selenium-python.readthedocs.io/installation.html#introduction

# driver = webdriver.Chrome()

# arguments
username = "5139677960"
password = "551042Bc!"
otp = True
headless = True
# link of product
link = 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG'

# do not change for amazon
amazon_button1 = "//input[@id='buy-now-button']"
amazon_button2 = "//input[@id='turbo-checkout-pyo-button']"

chrome_options = webdriver.ChromeOptions()
if headless:
    chrome_options.add_argument("--headless") #does not open the chrome window
driver = webdriver.Chrome(options=chrome_options)

def amazon_login():    
    driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
    driver.find_element_by_id("ap_email").send_keys(username, Keys.ENTER)
    driver.find_element_by_id("ap_password").send_keys(password, Keys.ENTER)
    # enter OTP identification to login
    if otp:
        tempotp = input("Enter OTP:")
        driver.find_element_by_id("auth-mfa-otpcode").send_keys(tempotp, Keys.ENTER)

# playstation link
# https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_13?dchild=1&keywords=PS5&qid=1606011034&sr=8-13
amazon_login()
driver.get(link)
flag = False
count = 0
while(not flag):
    try:
        driver.find_element_by_xpath(amazon_button1).click() #this might be unique
        driver.find_element_by_xpath(amazon_button2).click()
        flag = not flag
    except:
        print("trying again - " + str(count))
        driver.get(link)
        count = count + 1

print("Product ordered suscessfuly")

# driver.find_element_by_id('sltArr').find_elements_by_tag_name('option')[1].click() # Selects the "Arrive" option