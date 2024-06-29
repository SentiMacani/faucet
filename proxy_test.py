from seleniumwire import webdriver
import time

options = {
	'proxy': {
	    'http':'http://aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000',
	    'https':'http://aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000',
	    'no proxy':'localhost,127.0.0.1'
	}
}
driver = webdriver.Chrome()
driver.get('https://faucet.triangleplatform.com/arbitrum/sepolia')
time.sleep(8)


#BROWSERSTACK
PROXY = "res.proxy-seller.com:10000"
chrome_options = driver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = driver.Chrome(chrome_options=chrome_options)
chrome.get("https://faucet.triangleplatform.com/arbitrum/sepolia")