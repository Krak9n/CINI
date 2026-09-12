#!/usr/bin/env python3
import zipfile

def find_pwd(z):
    with open("rockyou.txt", "rb") as file:
        for line in file:
            for word in line.split():
                print(word.decode(errors='ignore'))
                try:
                    zip_ref.extractall(path="temp", pwd=word)
                    return True
                except:
                    continue
        return False
    
for i in range(100,0,-1):
    print(str(i)+".zip")
    with zipfile.ZipFile(str(i)+".zip", 'r') as zip_ref:
        find_pwd(zip_ref)
with open("flag.txt", "r") as file:
    print(file.read())
