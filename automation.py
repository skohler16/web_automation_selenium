from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import time

chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)
chrome_browser.maximize_window()
chrome_browser.get('https://www.scottckohler.com')
send_message_button = chrome_browser.find_element(By.ID, "submit")

assert 'Send Message' in chrome_browser.page_source

fName = chrome_browser.find_element(By.ID, 'fName')
fName.clear()
fName.send_keys("selenium")

lName = chrome_browser.find_element(By.ID, 'lName')
lName.clear()
lName.send_keys("automation")

email = chrome_browser.find_element(By.ID, 'email')
email.clear()
email.send_keys("example@howcool.com")

message = chrome_browser.find_element(By.ID, 'message')
message.clear()
message.send_keys("This is an automated message that has been sent using selenium")

send_message_button.click()

conf_message = chrome_browser.find_element(By.ID, 'back-link')

assert "Back to our site" in conf_message.text
chrome_browser.quit()