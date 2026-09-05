#!/usr/bin/env python3
import requests
from urllib.parse import urljoin
session = requests.Session()
url = "http://too-small-reminder.challs.olicyber.it/"
data = {"username": "temp_user1", "password": ""}

#registered = session.post(urljoin(url, "register"), json=data)
#print(registered.text)

login = session.post(urljoin(url, "login"), json=data)
print(session.cookies)
d = session.get(urljoin(url, "logout"), cookies=session.cookies)
print(d.text)
print(session.cookies)
#admin = session.get(urljoin(url, "admin"), cookies=session.cookies)
#print(admin.text)
