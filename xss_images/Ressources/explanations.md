### XSS <object> tag

When clicking on the NSA image, the redirection URL is

http://192.168.56.102/?page=media&src=nsa

By modifying the value of src, an <object> tag displays with a 404 error inside. This indicates that the <object> tag interprets HTML code.

A closer look at the code shows that the tag takes the image link as an argument.
We then attempt an XSS attack to display an alert.

It works! But no flag.
After some research, it's found that the <object> tag encodes the received files in base64. This encoding is commonly used when binary data needs to be stored and transferred over media designed for textual data.

We then transform our code into base64:

data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

Flag: 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D