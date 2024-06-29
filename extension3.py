from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_extension(r'D:\arbitrum selenium\3.1.0_0.crx')
chrome_driver_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
