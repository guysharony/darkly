# Path traversal

### Introduction
A path traversal attack involves manipulating inputs to gain unauthorized access to files outside the intended directory or area.

### Procedure
By inspecting the website's requests, we can identify that the server used by the website is `nginx/1.4.6 (Ubuntu)`. This information is crucial as it informs us about the operating system, which, in turn, gives insights into how files and directories are organized. One potentially interesting file to explore is `/etc/passwd`. This file holds information about user accounts on the system and can be a significant source of details regarding the users and their privileges.

To access this file, we'll use the `page` parameter in the URL by successively adding `../` at the beginning of `/etc/passwd`` until we successfully retrieve the desired information.

### Program
We will develop a program that sends requests to the server, gradually appending `../` at the start of `/etc/passwd` until the server's response contains the word `flag` at the very beginning of the page response. The program will end either upon finding the word `flag` or when it reaches the maximum number of loops.
```python
def try_directory(path: str, max: int = 20):
	for i in range(max):
		page = '/'.join(['..'] * i) + '/' + path

		response = requests.get(f'http://192.168.56.2/?page={page}')

		script = response.text.partition('\n')[0].split("'")[1::2]

		if len(script) > 0 and script[0].find("flag") != -1:
			return script[0]
```

### How to fix
To address this issue, it is recommended to implement strict access controls on specific directories, preventing users from exploring server directories. Additionally, ensure thorough validation and sanitization of all user inputs to mitigate the risk of unauthorized access and directory traversal.

### Sources
[OWASP - Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)