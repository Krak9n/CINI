Let's first analyze the traffic. There is a lot of TCP and HTTP packets.  
Our goal is to filter the packets by files that they contain.
```bash
$ tshark -r intercepted.pcap -Y 'http.request.method == "POST"'
```

If we however look into the filenames we would see different cat images being uploaded. However, there is packet *18626* which contains a zip archive.
If we were to export the bytedata and then unzip it we would see that it needs a password.
```bash
$ 7z x record.txt.zip
password: 
```

---

To find a password one would need to simply look through TCP packets.
```bash
$ frame contains "password"
```

And then just unzip the archive and read the file.