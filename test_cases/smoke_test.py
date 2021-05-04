#!/usr/bin/env python3
import pytest, random, string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initiate variables for used urls
homepage_URL = 'http://automationpractice.com/index.php'
auth_URL = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
blouse_URL = 'http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=Blouse&submit_search='

# generate random email, https://belekas.lt/ is a temporary email service
def random_email():
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return random_string + "@belekas.lt"

# define xpath for required elements
xpaths = {
    'registerEmailBox' : '//*[@id="email_create"]',
    'createAccBtn' : '//*[@id="SubmitCreate"]',
    'titleMrRadio' : '//*[@id="id_gender1"]',
    'regFirstName' : '//*[@id="customer_firstname"]',
    'regLastName' : '//*[@id="customer_lastname"]',
    'regPassword' : '//*[@id="passwd"]',
    'regDOBDay8' : '//*[@id="days"]/option[9]',
    'regDOBMonthMay' : '//*[@id="months"]/option[6]',
    'regDOBYear1989' : '//*[@id="years"]/option[34]',
    'newsletterBox' : '//*[@id="newsletter"]',
    'specOffersBox' : '//*[@id="optin"]',
    'addrFirstName' : '//*[@id="firstname"]',
    'addrLastName': '//*[@id="lastname"]',
    'addrCompany' : '//*[@id="company"]',
    'addrAddressLine1' : '//*[@id="address1"]',
    'addrAddressLine2' : '//*[@id="address2"]',
    'addrCity' : '//*[@id="city"]',
    'addrPO' : '//*[@id="postcode"]',
    'addrStateDC' : '//*[@id="id_state"]/option[10]',
    'addrAdditInfo' : '//*[@id="other"]',
    'addrHomePhone' : '//*[@id="phone"]',
    'addrMobilePhone' : '//*[@id="phone_mobile"]',
    'addrAlias' : '//*[@id="alias"]',
    'registerBtn' : '//*[@id="submitAccount"]',
    'infoAccMsg' : '//*[@id="center_column"]/p',
    'loginEmail' : '//*[@id="email"]',
    'loginPass' : '//*[@id="passwd"]',
    'loginBtn' : '//*[@id="SubmitLogin"]',
    'logoutBtn' : '//*[@id="header"]/div[2]/div/div/nav/div[2]/a',
    'searchInput' : '//*[@id="search_query_top"]',
    'searchSubmitBtn' : '//*[@id="searchbox"]/button',
    'searchProductNameRes' : '//*[@id="center_column"]/ul/li/div/div[2]/h5/a',
    'productImgContainer' : '//*[@id="center_column"]/ul/li/div/div[1]/div',
    'productAddToCart' : '//*[@id="add_to_cart"]/button',
    'productProceedChktBtn' : '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a',
    'productCartDescription' : '//*[@id="product_2_7_0_0"]/td[2]/p/a',
    'summaryProceedBtn' : '//*[@id="center_column"]/p[2]/a[1]',
    'addressProceedBtn' : '//*[@id="center_column"]/form/p/button',
    'shippingTOSChkbox' : '//*[@id="cgv"]',
    'shippingProceedBtn' : '//*[@id="form"]/p/button',
    'paymentBankwireBtn' : '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a',
    'paymentConfirmOrderBtn' : '//*[@id="cart_navigation"]/button',
    'orderCompleteText' : '//*[@id="center_column"]/div/p/strong'
}

# define test data
testdata = {
    'RandomRegEmail' : random_email(),
    'ValidEmailAddr' : 'JohnDoe@belekas.lt',
    'FirstName' : 'John',
    'LastName' : 'Doe',
    'RegPassword' : 'abc123456',
    'DOBDay' : '8',
    'DOBMonth' : 'May',
    'DOBYear' : '1989',
    'Company' : 'Amsiv Co',
    'AddressLine1' : '1600 Pennsylvania Avenue',
    'AddressLine2' : 'NW',
    'City' : 'Washington',
    'PO' : '20500',
    'AdditInfo' : 'No additional info to add',
    'HomePhone' : '+12024561111',
    'MobilePhone' : '+12000001111',
    'AddresAlias' : 'Home',
    'RegSuccessMsg' : 'Welcome to your account. Here you can manage all of your personal information and orders.',
    'SearchItem' : 'Blouse',
    'OrderCompleteMsg' : 'Your order on My Store is complete.'
}

# Fixture for Firefox to load browser before each class of tests
# and then close it after all test are executed. This will save me
# resources, time, and gives "clean slate" when required.
@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

#---------PREREQUISITE------------------------------
@pytest.mark.usefixtures("driver_init")
class Test_prerequisite():
        # TC_01
        # verify that the correct webpage is opened
        def test_tc_01(self):
            self.driver.get(homepage_URL)
            assert "My Store" == self.driver.title
#--------END OF PREREQUISITES---------------
#
#
#--------REGISTRATION TEST CASES----------------------

@pytest.mark.usefixtures("driver_init")
class Test_registration_functionality():
    # TC_02
    # verify that user is able to login with valid details when all registration fields are populated
    def test_tc_02(self):
        self.driver.get(auth_URL)
        self.driver.find_element_by_xpath(xpaths['registerEmailBox']).send_keys(testdata['RandomRegEmail'])
        self.driver.find_element_by_xpath(xpaths['createAccBtn']).click()
        WebDriverWait(self.driver, 5).until (
             EC.presence_of_element_located((By.ID, "customer_firstname"))
        )
        self.driver.find_element_by_xpath(xpaths['titleMrRadio']).click()
        self.driver.find_element_by_xpath(xpaths['regFirstName']).send_keys(testdata['FirstName'])
        self.driver.find_element_by_xpath(xpaths['regLastName']).send_keys(testdata['LastName'])
        self.driver.find_element_by_xpath(xpaths['regPassword']).send_keys(testdata['RegPassword'])
        self.driver.find_element_by_xpath(xpaths['regDOBDay8']).click()
        self.driver.find_element_by_xpath(xpaths['regDOBMonthMay']).click()
        self.driver.find_element_by_xpath(xpaths['regDOBYear1989']).click()
        self.driver.find_element_by_xpath(xpaths['newsletterBox']).click()
        self.driver.find_element_by_xpath(xpaths['specOffersBox']).click()
        self.driver.find_element_by_xpath(xpaths['addrCompany']).send_keys(testdata['Company'])
        self.driver.find_element_by_xpath(xpaths['addrAddressLine1']).send_keys(testdata['AddressLine1'])
        self.driver.find_element_by_xpath(xpaths['addrAddressLine2']).send_keys(testdata['AddressLine2'])
        self.driver.find_element_by_xpath(xpaths['addrCity']).send_keys(testdata['City'])
        self.driver.find_element_by_xpath(xpaths['addrPO']).send_keys(testdata['PO'])
        self.driver.find_element_by_xpath(xpaths['addrStateDC']).click()
        self.driver.find_element_by_xpath(xpaths['addrAdditInfo']).send_keys(testdata['AdditInfo'])
        self.driver.find_element_by_xpath(xpaths['addrHomePhone']).send_keys(testdata['HomePhone'])
        self.driver.find_element_by_xpath(xpaths['addrMobilePhone']).send_keys(testdata['MobilePhone'])
        self.driver.find_element_by_xpath(xpaths['addrAlias']).clear()
        self.driver.find_element_by_xpath(xpaths['addrAlias']).send_keys(testdata['AddresAlias'])
        self.driver.find_element_by_xpath(xpaths['registerBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        assert self.driver.find_element_by_xpath(xpaths['infoAccMsg']).text == testdata['RegSuccessMsg']

#-----END OF REGISTRATION TEST CASES-------
#
#
#---------USER ACCESS TEST CASES---------------

@pytest.mark.usefixtures("driver_init")
class Test_authentication_functionality():
    # TC_03
    # verify that user is able to login successfully wih valid email and password
    def test_tc_03(self):
        self.driver.get(auth_URL)
        self.driver.find_element_by_xpath(xpaths['loginEmail']).send_keys(testdata['ValidEmailAddr'])
        self.driver.find_element_by_xpath(xpaths['loginPass']).send_keys(testdata['RegPassword'])
        self.driver.find_element_by_xpath(xpaths['loginBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        assert self.driver.find_element_by_xpath(xpaths['infoAccMsg']).text == testdata['RegSuccessMsg']

    # TC_04
    # verify that logged in user is able to logout successfully. !!! This test case is dependant of TC_03 !!!
    def test_tc_04(self):
        self.driver.find_element_by_xpath(xpaths['logoutBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@title="Log in to your customer account"]'))
        )
        assert self.driver.find_element_by_xpath('//*[@title="Log in to your customer account"]').text == "Sign in"

#-----END OF USER ACCESS TEST CASES--------
#
#
#---------SEARCH  TEST CASES-----------------------

@pytest.mark.usefixtures("driver_init")
class Test_search_functionality():
    # TC_05
    # verify that user is able to search for a valid product
    def test_tc_05(self):
        self.driver.get(homepage_URL)
        self.driver.find_element_by_xpath(xpaths['searchInput']).send_keys(testdata['SearchItem'])
        self.driver.find_element_by_xpath(xpaths['searchSubmitBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        assert self.driver.find_element_by_xpath(xpaths['searchProductNameRes']).text == testdata['SearchItem']

#-----END OF SEARCH TEST CASES--------------
#
#
#---------SHOPPING CART  TEST CASES----------------

@pytest.mark.usefixtures("driver_init")
class Test_shopping_cart_functionality():
    # TC_06
    # verify that user is able to add an item to the shopping cart
    def test_tc_06(self):
        self.driver.get(blouse_URL)
        self.driver.find_element_by_xpath(xpaths['productImgContainer']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        self.driver.find_element_by_xpath(xpaths['productAddToCart']).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@title="Proceed to checkout"]'))
        )
        self.driver.find_element_by_xpath(xpaths['productProceedChktBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        assert self.driver.find_element_by_xpath(xpaths['productCartDescription']).text == 'Blouse'

#-----END OF SHOPPING CART TEST CASES-------
#
#
#---------CHECKOUT FLOW TEST CASES----------------
@pytest.mark.usefixtures("driver_init")
class Test_checkout_flow_functionality():
    # TC_07
    # verify that logged in user is able to search and purchase an item successfully.
    def test_tc_07(self):
        # login
        self.driver.get(auth_URL)
        self.driver.find_element_by_xpath(xpaths['loginEmail']).send_keys(testdata['ValidEmailAddr'])
        self.driver.find_element_by_xpath(xpaths['loginPass']).send_keys(testdata['RegPassword'])
        self.driver.find_element_by_xpath(xpaths['loginBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # search item
        self.driver.find_element_by_xpath(xpaths['searchInput']).send_keys(testdata['SearchItem'])
        self.driver.find_element_by_xpath(xpaths['searchSubmitBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # add item to cart
        self.driver.find_element_by_xpath(xpaths['productImgContainer']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        self.driver.find_element_by_xpath(xpaths['productAddToCart']).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@title="Proceed to checkout"]'))
        )
        self.driver.find_element_by_xpath(xpaths['productProceedChktBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # proceed to step 03. Address
        self.driver.find_element_by_xpath(xpaths['summaryProceedBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # proceed to step 04. Shipping
        self.driver.find_element_by_xpath(xpaths['addressProceedBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # proceed to stel 05. Payment
        self.driver.find_element_by_xpath(xpaths['shippingTOSChkbox']).click()
        self.driver.find_element_by_xpath(xpaths['shippingProceedBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # choose pay by bank wire
        self.driver.find_element_by_xpath(xpaths['paymentBankwireBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        # confim order
        self.driver.find_element_by_xpath(xpaths['paymentConfirmOrderBtn']).click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "center_column"))
        )
        assert self.driver.find_element_by_xpath(xpaths['orderCompleteText']).text == testdata['OrderCompleteMsg']

#-----END OF CHECKOUT FLOW TEST CASES-------