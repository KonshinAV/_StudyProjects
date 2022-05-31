from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

brouser_chrome = webdriver.Chrome()
brouser_firefox = webdriver.Firefox()
brouser_firefox.get('https://youtube.com')
xpath_login_button = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button"
# brouser.find_element_by_xpath(path_login_button).click()
brouser_firefox.find_element(by=By.XPATH, value=xpath_login_button).click()
xpath_login_email_field = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
brouser_firefox.find_element(by=By.XPATH, value=xpath_login_email_field).send_keys('konshinav88@gmail.com')
xpath_next_button = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
brouser_firefox.find_element_by_xpath(xpath=xpath_next_button).click()
# brouser.get('https://ya.ru')
# brouser.save_screenshot('screen_yandex')w