#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
url = "http://infinite.challs.olicyber.it/"
def math(soup):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).split()
    print(p)
    print(p[2] + p[4])
    return requests.post(url, data={str(p[2] + p[4])})
    
def art(soup):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).replace("?","").split()
    print(p)
    return requests.post(url, data=p[5])

def grammar(soup):
    p = ''.join([p_tag.get_text() for p_tag in soup.find_all("p")]).replace("?", "").replace('"', "").split()
    c = 0
    for i in p[6]:
        if i == p[1]:
            c += 1
    print(p)
    print(c)
    return requests.post(url, data={str(c)})

i = 0
page = requests.get(url)
while True:
    print(i, page.text, page.cookies.get_dict())
    soup = BeautifulSoup(page.text, 'html.parser')
    if "flag{" in page.text:
        break
    for s in soup.find_all('h2'):
        if s.text == "ART TEST":
            print("a entered")
            page = art(soup)
            print("a exited")
        elif s.text == "GRAMMAR TEST":
            print("g entered")
            page = grammar(soup)
            print("g exited")
        elif s.text == "MATH TEST":
            print("m entered")
            page = math(soup)
            print("m exited")
    i += 1
