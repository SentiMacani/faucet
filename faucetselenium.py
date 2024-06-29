from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from twocaptcha import TwoCaptcha
import sys 
#faker=Faker()

# def opening_browser(driver):
#   driver=webdriver.Chrome()
#   driver.maximize_window()
#   driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")



def wallet_for_captcha(driver):
    # print("passing the hardcoded wallet")
    # field = driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/input''')
    # field.send_keys("0x444fF5081f718cd01f940935b017ac94Fa71E39a")
    # driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/button''').click()
    # print("requested with the hardcoded wallet")

    api_key = "a0895d79373f55d0acc7af07c9ad27a1"
    solver = TwoCaptcha(api_key)
    try:
    

        result = solver.recaptcha(
         sitekey='6LfuM6giAAAAAOSzQAA57VwKBSEOgcRstYXUGqTa',
         url='https://faucet.triangleplatform.com/arbitrum/sepolia')
        code = result['code']
        print("the code is"+str(code))

        # time.sleep(2)
        # recaptcha_response_element = driver.find_element(By.ID, 'g-recaptcha-response-100000')

        recaptcha_response_element = driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

        print(recaptcha_response_element)
        #recaptcha_response_element = driver.find_element(By.XPATH, '//*[@id="g-recaptcha-response-100000"]')
        driver.execute_script(f'arguments[0].value = "{code}";', recaptcha_response_element)

        print("passing the hardcoded wallet")
        field = driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/input''')
        field.send_keys("0x444fF5081f718cd01f940935b017ac94Fa71E39a")
        driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/button''').click()
        print("requested with the hardcoded wallet")

    except Exception as e:
     sys.exit(e)

    else:
     sys.exit('exiting ...')

    

def looping_wallets(driver):
    field = driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/input''')
    with open('wallets.csv', mode='r')as file:
      reader_obj=csv.reader(file)
      for row in reader_obj:
         print("done")
         field.send_keys(row)
         print("done1")
         driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/button''').click()
         time.sleep(2)

         time.sleep(2)

         print("done2")
         time.sleep(2)
         print("done3")
         field.clear()
         print("done4")


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")

    wallet_for_captcha(driver)
    # looping_wallets(driver)













