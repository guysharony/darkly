

### XSS feedback

How to recognize an XSS vulnerability?

The XSS vulnerability, originally called CSS (Cross Site Scripting) but changed to avoid confusion with CSS (Cascading Style Sheets), is essentially the injection of JavaScript code into data when HTML is not disabled.

To test if the vulnerability is exploitable, we begin by attempting to add feedback that includes HTML.

We notice that the HTML is not disabled, and the HTML tags have disappeared.

The tags also vanish.


This feedback highlights that the XSS vulnerability arises from the improper handling of user input, specifically allowing HTML and JavaScript to be executed in the browser. The disappearance of HTML tags suggests that the application may be partially sanitizing input, but not effectively enough to prevent XSS attacks.

The successful generation of the flag using the "script" keyword confirms the presence of this vulnerability.