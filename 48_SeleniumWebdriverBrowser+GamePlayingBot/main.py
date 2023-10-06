from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get(r"https://www.flipkart.com/gopro-hero9-sports-action-camera/p/itmb882bafb449cb?pid=SAYFV7SYVRCGUNXF&lid=LSTSAYFV7SYVRCGUNXFHBJ75I&marketplace=FLIPKART&store=jek%2Fp31&spotlightTagId=FkPickId_jek%2Fp31&srno=b_1_1&otracker=browse&fm=organic&iid=50f4be60-0064-4cb4-ae06-1b8e0876b7ba.SAYFV7SYVRCGUNXF.SEARCH&ppt=browse&ppn=browse")
# price_string = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
# print(price_string.text)

driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu a')

event_dict = {index: {'time': event_dates[index].text, 'name': event_names[index].text} for index in range(len(event_names))}
print(event_dict)

# driver.close() closes one tab
# driver.quit() closes browswer
driver.quit()

