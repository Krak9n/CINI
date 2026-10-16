#!/usr/bin/env python3
import requests
import PIL as pl
import time
import pytesseract as ts
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
url = "http://captcha.challs.olicyber.it"
d = webdriver.Firefox()
d.get(url)
s = requests.Session()
# find link to the image
# determine text on the image
# enter the text
# click on the button
# repeat
def img(link):
    with open("text.png", "wb") as f:
        f.write(requests.get(url+link).content)
    
def determine_text(filename):
    i = pl.Image.open('text.png')
    return ts.image_to_string(i).replace("\n", "")

while True:
    index = s.get(url)
    soup = BeautifulSoup(d.page_source, 'html.parser')
    link = ''.join([l['src'] for l in soup.find_all("img")])
    img(link)
    print(d.page_source)
    if "flag{" in d.page_source:
        break
    d.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(determine_text('text.png'))
    d.find_element(By.ID, "next").click()
    print("------------------------")
