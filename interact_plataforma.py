#Interacting with the plataforma.tcargo website
import selenium
from selenium import webdriver
import urllib

driver = webdriver.Chrome()


driver.get('https://plataforma.tcargo.com.ar/plataformav2/')

img = driver.find_element_by_xpath('//div[@class="a7col logo"]/img')
src = img.get_attribute('src')
print(src)
a = ur.urlretrieve(src, "filename.png")



element = driver.find_element_by_class_name('a7col logo')
src = element.get_attribute('alt')
print(src)
urllib.urlretrieve(src, "captcha.png")


#Input username y password godeto
driver.find_element_by_name('j_username').send_keys("Hello wasBDKJSADorld")
driver.find_element_by_name('j_password').send_keys("Hello wasBDKJSADorld")

driver.fin


import urllib
import urllib.request as ur
from PIL import Image