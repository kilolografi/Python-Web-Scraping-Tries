# import webdriver 
import urllib.request
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import matplotlib.pyplot as plt
import urllib
import os
import numpy as np
i = 0
path = "imgs"
topic = input("What do you want?: ")
driver = webdriver.Chrome()
driver.get("https://www.amazon.com.tr/")
#bypass captcha
while True:
    try:
        driver.find_element(By.ID, "twotabsearchtextbox")
    except NoSuchElementException:
        driver.refresh()
    else:
        break
#search
inp=driver.find_element(By.ID, "twotabsearchtextbox" )
inp.send_keys(topic,Keys.ENTER) 
driver.find_element(By.ID,"sp-cc-accept").click()
#enter first item page
img = driver.find_elements(By.CSS_SELECTOR, "img.s-image")
title = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
price = driver.find_elements(By.CLASS_NAME, "a-price-whole")

piyasa = []
for i in range(20):
    urllib.request.urlretrieve(img[i].get_attribute("src"), os.path.join("imgs",f"{topic}{str(i)}.jpg"))
    print(title[i].text+"\ncosts:"+price[i].text)
    piyasa.append(int(price[i].text.replace(".","")))
print(piyasa)
plt.figure(figsize=(10,6))
plt.xlabel("products")
plt.ylabel("price range")
plt.title(f"{topic} prices")
plt.plot(piyasa,"o")

for x,y in zip(np.arange(0,20,1),piyasa):
    label = "{}".format(y)

    plt.annotate(label,(x,y),textcoords="offset points", # how to position the text
                 xytext=(0,8), # distance from text to points (x,y)
                 ha='center')
plt.plot([0,20],[np.mean(piyasa),np.mean(piyasa)],"r-")
plt.show()
for i in range(20):
    os.remove(os.path.join("imgs",f"{topic}{str(i)}.jpg"))