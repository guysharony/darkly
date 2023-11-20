# Open Redirect Vulnerability

### Introduction

This kind of flaw is known as an "open redirect" vulnerability. It occurs when an application takes a user-controlled input and redirects the user to the input's value without adequate validation. Attackers can exploit open redirects to craft URLs that appear to lead to a legitimate site but actually redirect the user to a phishing or malicious site

### Procedure

By looking at the code, the social media images are linked to ``index.php?page=redirect&site=facebook``, the parameter site is directly used to determine the redirection target. If the application does not validate what site can contain, we can manipulate this parameter to redirect users to malicious sites.

Change "facebook" by "flag" and be redirected to the flag page.

``http://192.168.56.102/index.php?page=redirect&site=flag``

### How to fix

Open redirects are mostly caused by processing unvalidated user inputs, especially URL query strings. To minimize the risk of unwanted redirects, avoid user-controllable data in URLs where possible and carefully sanitize it when it must be used.

### Source
[Open Redirect - Owasp](https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html)
