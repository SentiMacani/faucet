from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_extension('3.1.0_0.crx')
chrome = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chrome.exe',chrome_options=options)

# options = webdriver.ChromeOptions()
# options.add_extension(r)