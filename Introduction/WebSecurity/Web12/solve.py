#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "http://web-12.challs.olicyber.it/"
page = requests.get(url)
soup_data = BeautifulSoup(page.text, 'html.parser')

for data in soup_data.find_all("p"):
    print(data)
