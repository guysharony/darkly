import requests
import urllib.parse


def try_robots(path: str):
    url = f'http://192.168.56.101/.hidden/{path}'

    response = requests.get(url)

    return response.text


def filter_index(path: str = "/"):
    text = try_robots()

    lines = text.split('\n')

    links = [x for x in lines if x.startswith('<a href=')]
    for link in links:
        if type(link) == str:
            start_index = link.find('"') + 1
            end_index = link.find('"', start_index + 1)
            if start_index != -1 and end_index != -1:
                print(path + link[start_index:end_index])


def main():
    print(filter_index(response))


if __name__ == "__main__":
    main()