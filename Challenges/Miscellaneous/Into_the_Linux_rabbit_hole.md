Here we have a remote machine on which we should find a flag that was divided into three parts.  
  
To get access we should first connect to the remote `nc rabbit.challs.olicyber.it 10501`, and then run provided python script with the integer sequence that we get after connecting to the remote machine.
Wait for hashlib to generate a valid code and then paste it into the remote. Access granted.   

Also, I suppose that with it is possible to find the entire flag with some grep magic.  

## Flag

### First part
---
To start I ran the recursive grep from the root looking for any occurence of *flag{*.
```bash  
grep -rnc 'flag{' / | grep ":" | awk '$1>0'
```

Then there was this file **cat /proc/19685/task/19685/environ**. In which we could see the first part of the flag.
```bash  
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=oc-trainingmiscmisc15-app-775868768d-5fpqfFLAG=flag{l1nux_15_4_.....}KUBERNETES_PORT=tcp://10.43.0.1:443KUBERNETES_PORT_443_TCP=tcp://10.43.0.1:443KUBERNETES_PORT_443_TCP_PROTO=tcpKUBERNETES_PORT_443_TCP_PORT=443KUBERNETES_PORT_443_TCP_ADDR=10.43.0.1KUBERNETES_SERVICE_HOST=10.43.0.1KUBERNETES_SERVICE_PORT=443KUBERNETES_SERVICE_PORT_HTTPS=443HOME=/rootREMOTE_HOST=10.42.0.94
```  

### Second part
---
Finding the first part was by far the easiest one. It is hidden in the /entrypoint.sh script. 
Just run **cat** command on it and it will be there. 
```
flag{....c0mpl3x_And_4m4.....}  
```
  
### Third part
---
I was checking the filesystem with **df -h** command and to my surpirse there was this file **/root/challenges/olicyber/training-misc/misc15/src/flag_piece** mounted on **/var/log/flg**.
```bash
> df -h  
Filesystem                                                                 Size  Used Avail Use% Mounted on
overlay                                                                     96G   79G   17G  83% /
tmpfs                                                                       64M     0   64M   0% /dev
/dev/vda1                                                                   96G   79G   17G  83% /etc/hosts
shm                                                                         64M     0   64M   0% /dev/shm
10.16.67.10:/root/challenges/olicyber/training-misc/misc15/src/flag_piece  896G  460G  399G  54% /var/log/flg
tmpfs                                                                      5.9G     0  5.9G   0% /proc/acpi
tmpfs                                                                      5.9G     0  5.9G   0% /proc/scsi
tmpfs                                                                      5.9G     0  5.9G   0% /sys/firmware
```

Running cat on it gives the last part of the flag.  
```bash
> cat /var/log/flg
flag{......Z1ng_cr34Tur3}
```
