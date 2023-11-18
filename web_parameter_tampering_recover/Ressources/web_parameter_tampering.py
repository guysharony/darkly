import requests
import urllib.parse

def try_recover(mail: str):
    encoded_params = urllib.parse.urlencode({ 'page': 'recover' })

    url = 'http://192.168.56.2/?{}'.format(encoded_params)

    data = { 'mail': mail, 'Submit': 'Submit' }
    headers = { 'Content-Type': "application/x-www-form-urlencoded" }

    response = requests.post(url, data=data, headers=headers)

    return response.text

def main():
    print(try_recover('admin@borntosec.com'))

if __name__ == "__main__":
    main()