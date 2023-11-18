import requests
import urllib.parse

def try_input():
    encoded_params = urllib.parse.urlencode({ 'page': 'survey' })

    url = 'http://192.168.56.101/?{}'.format(encoded_params)

    data = { 'sujet': '2', 'valeur': '11' }
    headers = { 'Content-Type': "application/x-www-form-urlencoded" }

    response = requests.post(url, data=data, headers=headers)

    return response.text

def main():
    print(try_input())

if __name__ == "__main__":
    main()