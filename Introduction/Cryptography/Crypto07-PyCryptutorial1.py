#!/usr/bin/env python3
from Crypto.Cipher import DES, AES, ChaCha20
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from pwn import *
# primo passo
r = remote("crypto-07.challs.olicyber.it", 30000)
r.recvuntil(b"\n\n")
r.recvline()
r.recvline()
key = bytes.fromhex(r.recvline().decode().split()[2].replace("'", ""))
pt = str(r.recvline().decode().split("plaintext = ", 1)[1].replace("'","").replace("\n", "")).encode()
scheme = r.recvline().decode().split()[3]
cipher = DES.new(key, DES.MODE_CBC)
f = cipher.encrypt(pad(pt, 8, scheme))
r.sendlineafter(b"esadecimale)? ", f.hex().encode())
r.sendlineafter(b'? ', cipher.iv.hex().encode())
# secondo passo
r.recvline() # response
r.recvline() # new
r.recvline() # new
r.recvline() # cipher
r.recvline() # modee
pt = str(r.recvline().decode().split("plaintext = ", 1)[1].replace("'","").replace("\n", "")).encode() 
r.recvline() # padding 
r.recvline() # segment 
r.recvline() # new
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_CFB, segment_size=24)
f = cipher.encrypt(pad(pt, 16, "pkcs7"))
r.sendlineafter(b'? ', key.hex().encode()) # send key in hex
r.recvline()
r.recvline()
r.sendlineafter(b'? ', f.hex().encode())
r.sendlineafter(b'? ', cipher.iv.hex().encode())
r.recvline()
# terzo passo
r.recvuntil(b'ChaCha20\n') # cipher
key = bytes.fromhex(r.recvline().decode().split("key.hex() = ", 1)[1].replace("'", "").replace("\n", "")) # key hex
ciphertext = bytes.fromhex(r.recvline().decode().split("ciphertext.hex() = ", 1)[1].replace("'", "").replace("\n", "")) # key hex
non = bytes.fromhex(r.recvline().decode().split("cipher.nonce.hex() = ", 1)[1].replace("'", "").replace("\n", "")) # key hex
r.recvline()
cipher = ChaCha20.new(key=key, nonce=non)
plaintext = cipher.decrypt(ciphertext)
r.sendlineafter(b')? ', plaintext)
r.recvuntil(b'Grande! ')
print(r.recvline().decode())
