# Source page

Something interesting in that /thm.jpg:

```bash
curl http://$IP/thm.jpg thm.png
cat thm.png
```
Edit hex via hexed.it:

First string:
FFD8 FFE0 0010 4A46 4946

# Hidden directory:

/th1s_1s_h1dd3n

Url param:

http://10.10.247.67/th1s_1s_h1dd3n/?secret=1

Using Burp intruder:

secret=`73`

Passphrase is `y2RPJ4QaPF!B`

```bash
steghide extract -sf thm_edited.jpg
```

Username is `wbxre` (joker)