from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import config

def rand_proxy():
    proxy = random.choice(config.ips)

def main():
    #get rand proxy
    proxy = rand_proxy()
    #target urls
    url = "https://httpbin.org/ip"
    # url = "https://www.map.com.tw/"
    #add setting
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(options = options)
    driver.get(url)
    time.sleep(2)
    driver.close()
main()