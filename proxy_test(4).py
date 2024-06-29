from seleniumwire import webdriver
import time

options={
	'proxy':{
	   'http': 'http://aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000'
	}
}
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--ssl-version-max=tls1.2')
chrome_options.add_argument('–disable-dev-sh-usage')
driver = webdriver.Chrome(options=chrome_options,seleniumwire_options=options)
driver.get('https://faucet.triangleplatform.com/arbitrum/sepolia')

time.sleep(120)

#'http': 'http://res.proxy-seller.com:10009
#'http':'http://aecba55b52c2b576:RNW78Fm5@proxy-seller.com:10000'