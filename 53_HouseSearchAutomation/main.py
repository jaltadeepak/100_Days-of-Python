from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

HOUSEWEBSITE_LINK = 'https://www.nobroker.in/property/rent/delhi/New%20Delhi/?searchParam=W3sibGF0IjoyOC42NTc5NjcwMDA5MzM4LCJsb24iOjc3LjA5NzM4Mzg3NTQ4NywicGxhY2VJZCI6IkNoSUpMYlotTkZ2OUREa1J6azBnVGttM3dsSSIsInBsYWNlTmFtZSI6Ik5ldyBEZWxoaSIsInNob3dNYXAiOmZhbHNlfV0=&sharedAccomodation=0&buildingType=AP&rent=5000,13000&leaseType=BACHELOR_MALE&type=BHK3'

FORM_LINK = 'https://forms.gle/JMWYih5VYcugRUrC8'

response = requests.get(HOUSEWEBSITE_LINK)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

content = soup.select("#listCardContainer .infinite-scroll-component__outerdiv div article")

# print(content)
address_list = []
price_list = []
link_list = []

for article in content:
    address = article.select_one(".flex.flex-col.flex-2.w-pe.mt-1\.8px.po\:justify-center.po\:p-1p.po\:mt-0.w-70pe div div").get_text().strip()
    address_list.append(address)

    price = int(next(article.select_one("#minimumRent").stripped_strings, None)[4::].replace(",", ''))
    price_list.append(price)

    link = article.select_one(".capitalize.text-defaultcolor.mb-0\.5p.font-semibold.no-underline.hover\:text-primary-color.po\:overflow-hidden.po\:overflow-ellipsis.po\:max-w-95.po\:m-0.po\:font-normal.cd\:group-hover\:text-primary-color.cd\:group-hover\:nounderline h2 a").get('href')
    link_list.append(f"nobroker.in{link}")
    
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_LINK)
time.sleep(5)

for i in range(len(address_list)):
    AddressQtn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(address_list[i])
    time.sleep(2)
    PriceQtn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(price_list[i])
    time.sleep(2)
    LinkQtn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(link_list[i])
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(3)

driver.quit()