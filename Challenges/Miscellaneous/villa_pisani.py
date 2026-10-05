#!/usr/bin/env python3
# Reference here: https://stackoverflow.com/questions/3898363/set-specific-dns-server-using-dns-resolver-pythondns
import socket
import dns.resolver
maze = "00000000-0000-4000-0000-000000000000.maze.localhost"
re = dns.resolver.Resolver()
re.port = 10500
re.nameservers = [socket.gethostbyname('pisani.challs.olicyber.it')]
v = []
# filter by cname records
def move(direct):
    if direct in v:
        return
    v.append(direct)
    m = ""
    try: 
        m = str(re.resolve(direct, "txt").response.answer[0][0]).split(" ")[0]
    except dns.resolver.LifetimeTimeout:
        print(f"Timed out, try again later maybe? m: {m}")
    if not "flag" in m:
        print(f"Not in {direct}")
    else:
        print("Here:", m)
        return
    directions = ["up."+direct, "down."+direct, "left."+direct, "right."+direct]
    for i in directions:
        print(i)
        try:
            m = str(re.resolve(i, "cname").response.answer[0][0]).replace('"',"").split()[0]
        except dns.resolver.NoAnswer:
            continue
        move(m)    
move(maze)
