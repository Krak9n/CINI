#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from bs4 import Comment

url = "http://web-14.challs.olicyber.it/"
index_page = requests.get(url)
soup = BeautifulSoup(index_page.text, 'html.parser')

for s in soup.find_all(string = lambda text_to_analyze: isinstance(text_to_analyze, Comment)):
    print(s.extract())
