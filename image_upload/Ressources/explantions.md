### Introduction

Many websites allow file uploads, checking the size or MIME type of these files. It's relatively easy to upload malicious code contained in a .php file to access sensitive data.

### Procedure

While attempting to upload a file named `script.php`, we encountered an extension-based security restriction. Initially, we modified the file's extension to `script.php.jpeg` as this was the permitted format, but this approach did not yield the desired results.

Subsequently, we utilized the `curl` command to bypass the file extension security. The command used was:

```
curl -X POST "http://192.168.56.102/?page=upload" -F "uploaded=@script.php;type=image/jpeg" -F Upload=Upload -F MAX_FILE_SIZE=100000
```

This method involved specifying the MIME type as `image/jpeg` for the `script.php` file while sending the POST request. This effectively bypassed the extension restriction, allowing the PHP script to be uploaded successfully.

### How to Fix

To prevent such bypass techniques in file uploads, consider validate both the file extension and the MIME type on the server. Additionally, ensure that the MIME type is not just superficially checked but deeply analyzed to confirm the file's actual type.

### Source

[OWASP - FILE UPLOAD](https://owasp.org/www-chapter-pune/meetups/2023/Jan/File-upload-Vulnerability-Praveen-Sutar.pptx.pdf)