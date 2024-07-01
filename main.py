from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




def captcha_wallet(driver):
    field = driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/input''')
    field.send_keys("0xFBAE4529A4fd3eF779d07581fb1e00aEE3FD3E97")
    print("passed the wallet address")
    driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/button''').click()
    print("clicked on the req")
    time.sleep(3)
    #field.clear()
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.recaptcha-checkbox-border"))).click()
    print("clicked on the recaptcha")   
    time.sleep(3)
    driver.switch_to.default_content()
    print("switched to the default content")
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge expires in two minutes']")))
    print("switched to the iframe for the extension click ")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#rc-imageselect > div.rc-footer > div.rc-controls > div.primary-controls > div.rc-buttons > div.button-holder.help-button-holder"))).click()
    print("clicked on the extension button")
    time.sleep(30)

    


def looping_wallets(driver):
    field = driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/input''')
    with open('wallets.csv', mode='r') as file:
        reader_obj = csv.reader(file)
        for row in reader_obj:
            wallet_address = row[0]  
            print("Sending wallet:", wallet_address)
            field.send_keys(wallet_address)
            print("Clicking the button")
            driver.find_element(By.XPATH, '''//*[@id="__next"]/main/form/button''').click()
            time.sleep(2)  
            print("Clearing the field")
            field.clear()

def main():
    #driver = webdriver.Chrome()
    #driver.maximize_window()
    #driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")

    extension_path = "C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\mpbjkejclgfgadiemmefgebjfooflfhl\\3.1.0_0"
    options = webdriver.ChromeOptions()
    options.add_argument(f'--load-extension={extension_path}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://faucet.triangleplatform.com/arbitrum/sepolia")
    driver.maximize_window()

    time.sleep(5)  
    captcha_wallet(driver)
    #looping_wallets(driver)
    driver.quit()  

if __name__ == "__main__":
    main()
