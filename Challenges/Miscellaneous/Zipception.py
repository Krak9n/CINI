#!/usr/bin/env python3
import zipfile
for i in range(3000,-1,-1):
    print("flag"+str(i)+".zip")
    with zipfile.ZipFile("flag"+str(i)+".zip", 'r') as zip_ref:
        zip_ref.extractall(".")
with open("flag.txt", "r") as file:
    print(file.read())
