#!/usr/bin/env python3
import requests

url = "http://web-11.challs.olicyber.it/"
data = {"username": "admin", "password": "admin"}

session = requests.Session()
rs = session.post(url + "login", json=data)

csrf = list(rs.json().items())[1][1]
flag = ""
for i in range(4):
    updated = url + "flag_piece?csrf=" + csrf + "&index=" + str(i)
    print("Getting from:", updated)

    rs1 = session.get(updated, cookies=session.cookies)
    print(rs1.text)

    csrf = list(rs1.json().items())[1][1]
    flag = "".join([flag, list(rs1.json().items())[0][1]])
    print(flag)
    print(csrf)

print(flag)
