from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

PROMISED_DOWN = 200
PROMISED_UP = 100
TWITTER_LINK = 'https://twitter.com/i/flow/login'
TWITTER_USERNAME = 'your email'
TWITTER_PASSWORD = 'your password'

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0
        self.driver.get("https://fast.com/")
        time.sleep(40)
        

    def get_internet_speed(self):
        MoreInfoBtn = self.driver.find_element(By.XPATH, '//*[@id="show-more-details-link"]')
        MoreInfoBtn.click()
        self.down = int(self.driver.find_element(By.XPATH, '//*[@id="speed-value"]').text)
        self.up = int(self.driver.find_element(By.XPATH, '//*[@id="upload-value"]').text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:

            self.driver.get(TWITTER_LINK)
            time.sleep(4)

            UsernameBtn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            UsernameBtn.send_keys(TWITTER_USERNAME)
            time.sleep(4)

            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
            time.sleep(5)

            PwdBtn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            PwdBtn.send_keys(TWITTER_PASSWORD)
            LoginBtn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
            LoginBtn.click()
            time.sleep(10)

            self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
            time.sleep(3)

            TweetArea = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div').send_keys(f'Hey Template Internet Company,\nI was promise {PROMISED_DOWN}Mbps down and {PROMISED_UP}Mbps up speed but am getting only {self.down}Mbps down and {self.up}Mbps up speed.')
            time.sleep(5)

            PostBtn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
            PostBtn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
