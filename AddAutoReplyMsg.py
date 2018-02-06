import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as UI # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import sys


# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('--no-sandbox')
# driver=webdriver.Chrome(chrome_options=options)

options=webdriver.FirefoxOptions()
options.add_argument('-headless')
driver=webdriver.Firefox("geckodriver.exe",options=options)

driver.get("https://mail.csulb.edu")
driver.implicitly_wait(100)
OKTA_USERNAME=sys.argv[1]
OKTA_PASSWORD=sys.argv[2]
AUTO_REPLY_TEXT=sys.argv[3]


UI.WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "okta-signin-username")))
driver.find_element_by_id("okta-signin-username").send_keys(OKTA_USERNAME)

UI.WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "okta-signin-password")))
driver.find_element_by_id("okta-signin-password").send_keys(OKTA_PASSWORD,Keys.ENTER)

driver.find_element_by_id("idBtn_Back").click()
driver.implicitly_wait(100)


driver.get("https://outlook.office365.com/owa/?path=/options/automaticreplies/mode/popup")
UI.WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Send automatic replies')]")))
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(), 'Send automatic replies')]").click()

textBoxes = driver.find_elements_by_class_name("customScrollBar")
for textbox in textBoxes:
    if textbox.get_attribute("role") == "textbox":
        textbox.clear()
        textbox.send_keys(AUTO_REPLY_TEXT)
        time.sleep(1)
driver.find_element_by_xpath("//button[@title='OK']").click()
time.sleep(4)
driver.quit()


