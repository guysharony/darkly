# htpasswd File

### Introduction
htpasswd is used for creating and maintaining text files where usernames and passwords for basic HTTP user authentication are stored.

### Procedure
Upon visiting http://192.168.56.102/robots.txt, several files are found for exploration.

```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```

While navigating through ``/whatever``, an htpasswd file is encountered.

```
root:437394baff5aa33daa618be47b75cb49
```

Converting the root's password using MD5 yields ``qwerty123@``.

This leads to the administrator login platform at http://192.168.56.102/admin.

### How to fix
Add a in the htaccess file a code to protect the robot.txt file and avoid indexing.
```
<FilesMatch "robots.txt">
	Header set X-Robots-Tag "noindex, nofollow"
</FilesMatch>
```
It's crucial to ensure that the .htpasswd file is not located in a directory that is accessible to users and to remember to delete any files containing sensitive data.
