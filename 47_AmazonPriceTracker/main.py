import requests
from bs4 import BeautifulSoup
import smtplib

# amazon didn't work, flipkart didn't work. using the tracker website for both prices.
FLIPKART_URL = r"https://www.flipkart.com/gopro-hero9-sports-action-camera/p/itmb882bafb449cb?pid=SAYFV7SYVRCGUNXF&lid=LSTSAYFV7SYVRCGUNXFHBJ75I&marketplace=FLIPKART&store=jek%2Fp31&spotlightTagId=FkPickId_jek%2Fp31&srno=b_1_1&otracker=browse&fm=organic&iid=50f4be60-0064-4cb4-ae06-1b8e0876b7ba.SAYFV7SYVRCGUNXF.SEARCH&ppt=browse&ppn=browse"

PRICEHISTORY_URL = "https://pricehistory.app/p/gopro-hero9-sports-action-camera-black-20-Y8rrcemb"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(PRICEHISTORY_URL, headers=header)

content = response.text

soup = BeautifulSoup(content, 'html.parser')

currentprice = float(soup.find(name="div", class_="ph-pricing-pricing").get_text().replace("₹", "").replace(",", ""))

print(currentprice)

my_email = "deepaksingh131120@gmail.com"
my_password = "[YOUR PASSWORD HERE]"

if currentprice < 25000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="deepaksingh131102@gmail.com",
            msg="Subject: Buy your GoPro now! It's below 25000.\n\nhttps://www.flipkart.com/gopro-hero9-sports-action-camera/p/itmb882bafb449cb?pid=SAYFV7SYVRCGUNXF&lid=LSTSAYFV7SYVRCGUNXFHBJ75I&marketplace=FLIPKART&store=jek%2Fp31&spotlightTagId=FkPickId_jek%2Fp31&srno=b_1_1&otracker=browse&fm=organic&iid=50f4be60-0064-4cb4-ae06-1b8e0876b7ba.SAYFV7SYVRCGUNXF.SEARCH&ppt=browse&ppn=browse",
        )
