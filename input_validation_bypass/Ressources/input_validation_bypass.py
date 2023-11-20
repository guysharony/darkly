import sys
import requests
import urllib.parse

def try_input():
    encoded_params = urllib.parse.urlencode({ 'page': 'survey' })

    url = f'http://{sys.argv[1]}/?{{}}'.format(encoded_params)

    data = { 'sujet': '2', 'valeur': '11' }
    headers = { 'Content-Type': "application/x-www-form-urlencoded" }

    response = requests.post(url, data=data, headers=headers)

    return response.text

def main():
    try:
        assert len(sys.argv) == 2, "IP address is not valid."

        print(try_input())
    except Exception as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    main()