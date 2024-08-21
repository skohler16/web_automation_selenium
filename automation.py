from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import time

chrome_options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome_browser = webdriver.Chrome(options=options)
# chrome_browser.maximize_window()
chrome_browser.get('https://www.scottckohler.com')
button = chrome_browser.find_element(By.CLASS_NAME, "fab.fa-github")
button_text = button.get_attribute('innerHTML')
print(button_text)

# assert 'Selenium Easy Demo' in chrome_browser.title



# chrome_browser.quit()

# # This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()
#
# user_message = chrome_browser.find_element(By.ID, 'user-message')
# user_message.clear()
# user_message.send_keys('I AM EXTRA COOOOL')
#
# time.sleep(2)
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()
#
# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOL' in output_message.text