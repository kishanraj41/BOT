from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
username = 'user name'
password = 'password'

browser = webdriver.Firefox()# varies for different browsers refer the document
browser.get(('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier'))



username = browser.find_element_by_id('identifierId')
username.send_keys(username)

nextButton = browser.find_element_by_id('identifierNext')
nextButton.click()


password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "password")))

password.send_keys(password)

time.sleep(2)
signInButton = browser.find_element_by_id('passwordNext')
signInButton.click()
while True:
    actions = ActionChains(browser)
    for i in range(49):
        actions.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
    nextmailpage=browser.find_element_by_id(':ir')
    nextmailpage.click()
    
