#!/usr/bin/env python3
"""
Very simple challenge but I want to have a reference for the case I ever lose access to the documentation.   

Here I just had to retrieve the page with requests and search for all <p> tags with BeautifulSoup.   
"""
import requests
from bs4 import BeautifulSoup

url = "http://web-12.challs.olicyber.it/"
page = requests.get(url)
soup_data = BeautifulSoup(page.text, 'html.parser')

for data in soup_data.find_all("p"):
    print(data)
