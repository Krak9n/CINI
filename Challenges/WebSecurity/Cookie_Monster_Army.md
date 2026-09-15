The goal of the challenge is quite simple. Change the cookie value until it is the one that produces the flag.
If we register a new user, lets say **11111111**. Their cookie would look like this:
```bash
MjAyNi8wOS8xNS0xNzg5NDU2MjU2LTExMTExMTExMQ==
```
It is in base64, and if we were to decode it:
```bash
2026/09/15-1789456256-111111111
```

The catch is obvious. Change the last cookie value to **admin**, encode it, and send.  
