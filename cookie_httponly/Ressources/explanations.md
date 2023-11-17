## HttpOnly Attribut Missing 

Upon inspecting the page, the 'I_am_admin' cookie lacks protection by the 'HttpOnly' and 'Secure' attributes. This indicates that the cookie can be accessed and modified on the client side.

Changing the value to true in md5 and the flag is displayed.

### Source

https://owasp.org/www-community/HttpOnly