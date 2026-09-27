#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
url = "http://infinite.challs.olicyber.it/"
d = webdriver.Firefox()
d.get(url)

def math(soup, driver):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).split()
    driver.find_element(By.ID, "sum").send_keys(str(int(p[2]) + int(p[4].replace("?", ""))));
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    
def art(soup, driver):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).replace("?","").split()
    driver.find_element(By.ID, p[5]).click()		

def grammar(soup, driver):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).replace("?", "").replace('"', "").split()
    c = 0
    for i in p[6]:
        if i == p[1]:
            c += 1
    driver.find_element(By.ID, "letter").send_keys(str(c));
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

i = 0
while True:
    page = requests.get(url)
    print(i, d.page_source)
    soup = BeautifulSoup(d.page_source, 'html.parser')
    if "flag{" in d.page_source:
        break
    for s in soup.find_all('h2'):
        if s.text == "ART TEST":
            art(soup, d)
        elif s.text == "GRAMMAR TEST":
            grammar(soup, d)
        elif s.text == "MATH TEST":
            math(soup, d)
    i += 1
