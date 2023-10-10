# INCOMPLETE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MY_EMAIL = 'YOUR EMAIL'
MY_PASSWORD = 'YOUR PASSWORD'

APPLY_LINK = r'https://www.linkedin.com/jobs/search/?currentJobId=3727715202&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(APPLY_LINK)
time.sleep(5)

SignInBtn = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
SignInBtn.click()
time.sleep(5)

EmailInput = driver.find_element(By.XPATH, '//*[@id="username"]')
PasswordInput = driver.find_element(By.XPATH, '//*[@id="password"]')

EmailInput.send_keys(MY_EMAIL)
time.sleep(5)
PasswordInput.send_keys(MY_PASSWORD)
time.sleep(5)

SignInBtn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
SignInBtn.click()
time.sleep(5)


