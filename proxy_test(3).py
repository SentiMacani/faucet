
from seleniumwire import webdrivers
from webdriver_manager.chrome import ChromeDriverManager

## Define Your Proxy Endpoints
proxy_options = {
    'proxy': {
        'http': 'http://aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000',
        'https': 'http://aecba55b52c2b576:RNW78Fm5@res.proxy-seller.com:10000',
        'no_proxy': 'localhost:127.0.0.1'
    }
}

## Set Up Selenium Chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install(), 
                            seleniumwire_options=proxy_options)

## Send Request Using Proxy
driver.get('http://httpbin.org/ip')




#ZENROWS WAY
# proxy_username = '7a4253e74c81980a'
# proxy_password = 'RNW78Fm5'
# seleniumwire_options = {
#     'proxy': {
#        'http': f'http://{proxy_username}:{proxy_password}',
#        'verify_ssl': False,

#     }
# }
# driver = webdriver.Chrome(
#     seleniumwire_options=seleniumwire_options
#     )
