First of all you should filter the packets by an address from which the connections were comming.
```bash
	ip.src == 192.168.100.1 && ip.dst == 192.168.100.2  
```

After that right click on the packet that was sending the PSH (push) and ACK (acknowledgement), then **File** -> **Export Packet Bytes**.    
  
**decoder.py** script just reads the byte data from the file and puts into the data.  
Then we create a bytearray that gets decompressed with gzip, and at the end decoded as a UTF-8 string.  