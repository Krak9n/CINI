This challenge involves a bit of reading. If we just open the pcap file we'll see a lot of confussion and retransmissions of packets.
  
---  
  
If we look closer or try to sort the packets we'll notice that TCP sequence number doesn't equal to its actual value. However, there is another field we could use as an reference point, timestamps.
Sorting by packets by Time and by the length of 1 would give us something. By 1 because each PUSH packet contains just one byte.  
```bash
$ tshark -r CHAOS.pcap -Y "tcp.len == 1" -T fields -e frame.time_epoch -e tcp.payload
1616253131.665694138	48
1616253117.649958064	6c
1616253133.667193593	30
1616253123.656996582	30
1616253135.675089127	0a
1616253125.659428119	4d
1616253118.650453451	61
1616253135.675068253	7d
1616253122.656334211	30
1616253126.661107794	55
1616253134.674146067	35
1616253132.666520124	34
1616253128.663373391	48
1616253130.664860675	43
1616253121.655875624	54
1616253124.657611852	5f
1616253116.647530213	66
1616253129.663891128	5f
1616253127.662476033	43
1616253120.654308843	7b
1616253119.651979622	67
```

Here we obtain the timestamp and the value in hex.
The rest is just a couple of utils.
```bash
> tshark -r Downloads/CHAOS.pcap -Y "tcp.len == 1" -T fields -e frame.time_epoch -e tcp.payload | sort -n | awk '{print $2}' | tr -d '\n' | xxd -r -p
```