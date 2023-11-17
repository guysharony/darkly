### File Upload Bypass Technique Explanation

While attempting to upload a file named `script.php`, we encountered an extension-based security restriction. Initially, we modified the file's extension to `script.php.jpeg` as this was the permitted format, but this approach did not yield the desired results.

Subsequently, we utilized the `curl` command to bypass the file extension security. The command used was:

```
curl -X POST "http://192.168.56.102/?page=upload" -F "uploaded=@script.php;type=image/jpeg" -F Upload=Upload -F MAX_FILE_SIZE=100000
```

This method involved specifying the MIME type as `image/jpeg` for the `script.php` file while sending the POST request. This effectively bypassed the extension restriction, allowing the PHP script to be uploaded successfully.