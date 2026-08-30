#!/usr/bin/env python3
import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "http://web-16.challs.olicyber.it"
visited = []

def spider(url):
    index = requests.get(url)
    soup = BeautifulSoup(index.text, 'html.parser')
    detect_flag(soup)

    links = links_on_this_page(soup)
    print(links)

    for i, x in enumerate(links):
        traverse_through_the_links_on_this_page(urljoin(url, x))

def links_on_this_page(soup):
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links

def detect_flag(soup):
    for s in soup.find_all('h1'):
        print("\n",s.text,"\n")
    
def traverse_through_the_links_on_this_page(current_url):
    links_present = []

    print("Operating on: ",current_url)
    if current_url in visited:
        print("Already visited this url.")
        return
    
    visited.append(current_url)

    page_data = requests.get(current_url)
    soup = BeautifulSoup(page_data.text, 'html.parser')
    detect_flag(soup)
        
    links_present = links_on_this_page(soup)
    print(links_present)

    for link in links_present:
        temp_full_url = urljoin(url, link)
        print("Current url is:", temp_full_url)
        if temp_full_url.startswith(url):
            traverse_through_the_links_on_this_page(urljoin(url, link))

spider(url)
