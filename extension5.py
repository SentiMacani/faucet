from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_extension(r'./3.1.0_0.crx')
driver = webdriver.Chrome(options=options) 
driver.get('http://www.amazon.com')