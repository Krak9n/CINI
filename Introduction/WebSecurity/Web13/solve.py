#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = "http://web-13.challs.olicyber.it/"
index = requests.get(url)
filter = BeautifulSoup(index.text, 'html.parser')

result = ""
for temp in filter.find_all('span'):
    result += temp.text

print(result.replace("\n", ""))
