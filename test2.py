from selenium import webdriver
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox('/usr/local/bin/geckodriver')
driver.get('http://google.com/')