from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


extension_path = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\mpbjkejclgfgadiemmefgebjfooflfhl\\3.1.0_0"
options = webdriver.ChromeOptions()
options.add_argument(f'--load-extension={extension_path}')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")

time.sleep(10000)


# xpath = //*[@id="recaptcha-anchor"]/div[1]

# xpth solver = //*[@id="solver-button"]