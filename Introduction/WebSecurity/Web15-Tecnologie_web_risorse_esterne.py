#!/usr/bin/env python3
"""
The goal of this challenge was to extract contents from all of the page related files, and traverse through while looking for the "flag{" string.  
"""
def traverse_js(soup):
    scripts = []
    for script in soup.find_all('script'):
        if script.attrs.get('src'):
            script_url = urljoin(url, script.attrs.get('src'))
            scripts.append(script_url)

    contents = []
    for script in scripts:
        contents.append(requests.get(script).text)

    return contents

def traverse_css(soup):
    css_s = []
    for css in soup.find_all('link'):
        if css.attrs.get('href'):
            css_url = urljoin(url, css.attrs.get('href'))
            css_s.append(css_url)

    contents = []
    for css in css_s:
        contents.append(requests.get(css).text)

    return contents

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://web-15.challs.olicyber.it/"
index = requests.get(url)
soup = BeautifulSoup(index.text, 'html.parser')

contents_js = traverse_js(soup)
for content in contents_js:
    if content.find("flag{"):
        print(content)

contents_css = traverse_css(soup)
for content in contents_css:
    if content.find("flag{"):
        print(content)

