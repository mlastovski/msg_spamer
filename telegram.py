from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform


# Переменные
sendDelay = 1
print("You should manually confirm log in by entering your security code after you enter your phone number.")
phone_number = int(input("Please enter your phone number without your country code: "))
friendName = input("Please enter your friend name as it written in your Telegram: ")
print("Starting...")

# Проверка мак или винда
if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Открывает телегу
driver.get('https://web.telegram.org/#/login')
time.sleep(4)

# Login
driver.find_element_by_xpath('//*[@name="phone_number"]').send_keys(phone_number)
driver.find_element_by_class_name("login_head_submit_btn").click()
time.sleep(2)
driver.find_element_by_class_name("btn-md-primary").click()
# Это время на ввод секретного кода
time.sleep(20)


# Ищет пользователя
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

print("Reading text file...")
movie_script = []
with open('arkek.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            # Types words and submits
            actions = ActionChains(driver)
            actions.send_keys(word, Keys.ENTER)
            actions.perform()
            time.sleep(sendDelay)
