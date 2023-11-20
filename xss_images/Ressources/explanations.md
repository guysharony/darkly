# XSS `<object>` data tag

### Introduction

The `<object>` data tag in HTML is a versatile element used to embed different types of multimedia, such as images, videos, and even HTML documents, into a web page. It offers a way to include complex objects which can be interactive or merely display content. Understanding the workings and security implications of the `<object>` tag is crucial for web developers and penetration testers alike, especially in the context of potential vulnerabilities like Cross-Site Scripting (XSS) attacks.

### Procedure

1. **Initial Setup and Observation**: 
   - On a test web page, an image linked to the National Security Agency (NSA) is observed, with the following URL: `http://192.168.56.102/?page=media&src=nsa`.
   - Clicking on the image redirects to this URL.

2. **Manipulating the `src` Parameter**:
   - The `src` parameter in the URL is modified, leading to the display of an `<object>` tag containing a 404 error. This suggests that the `<object>` tag is interpreting HTML code.

3. **Examining the Underlying Code**:
   - The source code reveals that the `<object>` tag uses the image link as an argument.

4. **Attempt at XSS Attack**:
   - An XSS attack is attempted by displaying an alert through the `<object>` tag. The attack is successful, indicating a vulnerability, although no flag (a common indicator of success in penetration testing scenarios) is found.

5. **Realization of Base64 Encoding**:
   - Further research reveals that the `<object>` tag encodes received files in base64, a method often used for encoding binary data for transfer over text-based systems.
     `base64(<script>alert("crazy XSS attack");</script>)` = `PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`

6. **Encoding Attack Vector in Base64**:
   - To exploit this vulnerability, the XSS attack code is converted into a base64 encoded string: `data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==`.

### How to Fix the Vulnerability

Ensure all input parameters, especially those used in the `<object>` tag, are properly validated and sanitized. This includes checks for type, format, and length.

### Sources

https://www.acunetix.com/websitesecurity/cross-site-scripting/
https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
