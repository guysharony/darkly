# XSS feedback

### Introduction

Cross-Site Scripting (XSS) is a significant security vulnerability that occurs in web applications. It involves the injection of malicious JavaScript code into web pages viewed by other users. The term "XSS" was coined to distinguish it from "CSS," or Cascading Style Sheets, to avoid confusion. The core of this vulnerability lies in the application's failure to properly handle user-supplied input, which can lead to the execution of unintended scripts in the user's browser, compromising the security of user data and interactions with the website.

### Procedure

1. **Identifying Potential XSS Points**: 
   - Begin by identifying areas in the application where user input is accepted and displayed, such as feedback forms, comment sections, or search queries.

2. **Initial Testing with HTML**: 
   - Input HTML code as part of the feedback. Observe whether the HTML is executed or if the tags are simply displayed as plain text.
   `<h1>hello<\h1>` become `hello`
   - In this case, it is noted that the HTML is not disabled, and the HTML tags disappear from the input, indicating that they are processed in some manner.

3. **Further Testing for Script Execution**: 
   - Since the HTML tags vanish, it suggests that the application might be partially sanitizing the input. However, this does not rule out the possibility of XSS.
   - To further test, attempt to insert a simple JavaScript snippet using the `<script>` tag in the feedback.

4. **Observing Behavior and Output**:
   - If the script runs (e.g., a JavaScript alert box appears), this confirms the presence of an XSS vulnerability.
   - The successful generation of a flag (a response from the system indicating a successful exploit) using the "script" keyword also confirms this vulnerability.

### How to Fix

Ensure all input parameters and properly validate and sanitize. This includes checks for type, format, and length.

### Sources

[XSS](https://www.acunetix.com/websitesecurity/cross-site-scripting/)

[XSS - Owasp](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
