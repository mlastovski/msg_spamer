from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform


# Variables
sendDelay = 1
email = input("Please enter your email: ")
print("Success, your email is: " + email)
print("Now enter your password")
password = input("Please enter your password: ")
print("OK, final step. Enter your friend nickname to send them text.")

friendName = input("Please enter friend's nickname: ")

# Checks if on Mac or Windows
if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Discord
driver.get('https://discordapp.com/login')
time.sleep(3)

# Login
driver.find_element_by_xpath('//*[@name="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@type="submit"]').click()

# Waits 8 seconds to finish loading page
time.sleep(8)

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
