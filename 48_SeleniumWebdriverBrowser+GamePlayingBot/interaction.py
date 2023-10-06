from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
# article_count.click()
# link_text = driver.find_element(By.LINK_TEXT, 'Drew Weissman')
# link_text.click()
# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME, 'fName')
fName.send_keys("Deepak")
lName = driver.find_element(By.NAME, 'lName')
lName.send_keys("Singh")
email = driver.find_element(By.NAME, 'email')
email.send_keys("deepakemail@emailed.com")
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.send_keys(Keys.ENTER)

