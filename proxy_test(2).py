from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import undetected_chromedriver as uc 

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000"
#proxy.ssl_proxy = "username:password@ip:prt"
capabilities = webdriver.DesiredCapabilities.CHROME.copy()
proxy.add_to_capabilities(capabilities)

driver = uc.Chrome(use_subprocess=True, desired_capabilities=capabilities)




#STACKOVERFLOW
# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.http_proxy = "res.proxy-seller.com:10000"

# capabilities = webdriver.DesiredCapabilities.CHROME
# Proxy.add_to_capabilities(capabilities)

# driver = webdriver.Chrome(desired_capabilities=capabilities)