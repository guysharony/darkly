import sys
import requests


def try_robots(path: str = ""):
    url = f'http://{sys.argv[1]}/.hidden{path}'

    response = requests.get(url)

    return response.text

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

def main():
    try:
        assert len(sys.argv) == 2, "IP address is not valid."

        print(filter_index("/"))
    except Exception as err:
        print(f'Error: {err}')

if __name__ == "__main__":
    main()
