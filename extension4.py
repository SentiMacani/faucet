import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
# executable_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
# os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension(r'D:\\arbitrum selenium\\3.1.0_0.crx')

# driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=driver, chrome_options=chrome_options)
driver.get("http://stackoverflow.com")
driver.quit()