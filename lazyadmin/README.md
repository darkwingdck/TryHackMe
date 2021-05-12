# Nmap

Open ports:
22/ssh
80 http

# Gobuster

/content

CMS is SweetRice

https://www.cvedetails.com/cve/CVE-2007-0994/ tells us that we have 'Execute CodeBypass a restriction or similar'
https://www.exploit-db.com/exploits/10246 tells us that we have 'Remote File Include Vulnerability'

or we can use 
```
searchsploit sweetrice
```
sql backup at /content/inc/mysql_backup/

Password is 'Password123'

Just put an add like https://jc01.ninja/ctf/lazy-admin/

User flag is at /home/itguy/user.txt
