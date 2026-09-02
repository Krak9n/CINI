#!/usr/bin/env python3
"""
In this challenge I had to work with CSRF tokens.
  
Basically, everything started from passing json with admin credentials to /login page and then I was having the first CSRF token with which I could proceed with completing the challenge.

The logic here is to do a GET request to /flag_piece 4 times with each retrieving a piece of a flag. Each of these GETs should contain this query:
/flag_piece?csrf=<CSRF token>&index=<Index of a piece>
  
After everything was successfully ran I had the flag.  
"""
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
