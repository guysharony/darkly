## Open Redirect Vulnerability

In the example index.php?page=redirect&site=facebook, the parameter site is directly used to determine the redirection target. If the application does not validate what site can contain, we can manipulate this parameter to redirect users to malicious sites.

This kind of flaw is known as an "open redirect" vulnerability. It occurs when an application takes a user-controlled input and redirects the user to the input's value without adequate validation. Attackers can exploit open redirects to craft URLs that appear to lead to a legitimate site but actually redirect the user to a phishing or malicious site

Change "facebook" by "flag" and be redirected to the flag page.

```
http://192.168.56.102/index.php?page=redirect&site=flag
```

## Source
https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html