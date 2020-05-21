from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform


# Variables
sendDelay = 1
username = input("Please enter your username: ")
print("Your username is: " + username)
print("Next step is your password.")
password = input("Please enter your password: ")
print("Success, finnaly enter friend name to send text to.")
friendName = input("Please enter friend name: ")
print("Starting...")
# Checks if on Mac or Windows
if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Discord
driver.get('https://www.instagram.com/')
time.sleep(3)

# Login
driver.find_element_by_xpath('//*[@name="username"]').send_keys(username)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@type="submit"]').click()

# Waits 8 seconds to finish loading page
time.sleep(6)

# driver.find_element_by_xpath('//*[@type="button"]').click()
# time.sleep(1)
driver.find_element_by_xpath("//a[@href='/direct/inbox/']").click()
time.sleep(3)

# Finds user in DM list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

movie_script = []
print("Reading text file...")
with open('arkek.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            # Types words and submits
            actions = ActionChains(driver)
            actions.send_keys(word, Keys.ENTER)
            actions.perform()
            time.sleep(sendDelay)
