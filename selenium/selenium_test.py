from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
#chrome_options = Options()
#chrome_options.add_argument("--headless")
# products = [
#     "https://analytics.google.com/analytics/web/provision/#/report/visitors-overview/a178931540w247408450p229643797/",
# ]
#driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome()
# for url in products:
#     print("start")
#     driver.get(url)
#     print(url)
#     print(driver.find_element_by_xpath('//*[@id="productTitle"]').text)
#     #print(driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text)
#     #print(driver.find_element_by_xpath('//*[@id="productDetails_detailBullets_sections1"]').text)
#     print("----------------------------\n")
# driver.close()

class Google:

    def __init__(self, username, password):

        self.driver = webdriver.Chrome()
        self.driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://analytics.google.com/analytics/web/provision/#/report/visitors-overview/a178931540w247408450p229643797/')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="reporting"]/div/div/div/ga-nav-link[2]/div[1]/a/div/span/span').click()
        sleep(5)
        self.driver.find_element_by_id('AnnotationDrawer').click()
        # self.driver.find_element_by_xpath('//*[@id="AnnotationDrawer_drawer_button"]').click()
        sleep(2)
        self.driver.find_element_by_xpath('<a href="#" onclick="return false;" class="_GALN _GAAu">+&nbsp;צור הערה חדשה</a>').click()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="AFB3siagZNXnPzPSEnBX46Q78DgwZFqbPGbrPhKxROBGs13evevzFTgbt-wfygR9wiWLsrTxhO7n:1600948746987"]/td/form/table/tbody/tr/td[3]/textarea').send_keys("hello world")
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="AFB3siagZNXnPzPSEnBX46Q78DgwZFqbPGbrPhKxROBGs13evevzFTgbt-wfygR9wiWLsrTxhO7n:1600948746987"]/td/form/table/tbody/tr/td[7]/a/b/b/b').click()
        #self.driver.close()
username = 'tunnnel59@gmail.com'
password = 'VeryShortad1!'
Google(username, password)