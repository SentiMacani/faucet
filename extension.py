# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# def extension(driver):
#    extension_path = '3.1.0_0.crx'
#    options = webdriver.ChromeOptions()
#    options.add_extension(extension_path)




# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")
#     extension(driver)
#     time.sleep(5)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

op = Options()

op.add_extension('3.1.0_0.crx')

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
options=op)
driver.maximize_window()

driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")