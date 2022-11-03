import sys
from getopt import getopt, GetoptError
import requests
from bs4 import BeautifulSoup
import pprint
import json


def get_options(argv):
    try:
        opts, args = getopt(argv, 'hu:o:', ["help", "url=", "output-path="])
    except GetoptError:
        show_error()
        sys.exit(2)

    options = {"url": None, "output-path": None}
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        if opt in ("-u", "--url"):
            options["url"] = arg
        if opt in ("-o", "--output-path"):
            options['output-path'] = arg

    if (options["url"] is None):
        show_error()
        sys.exit(3)
    return options


def show_help():
    print('Run "py parse_link.py -u https://ya.ru" '
          'or py parse_link.py --url=https://ya.ru".\n'
          'In order to save the result use -o or --output-file flags, for '
          'example, py parse_link.py -u https://ya.ru -o file.txt.')


def show_error():
    print('Invalid function arguments. Run "py parse_links.py -h" '
          'to get help')


def get_links(url):
    r = requests.get(url)
    if r.status_code != 200:
        return []
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return [link.get('href') for link in soup.find_all('a')]


def output_result(data, path):
    if path is None:
        pprint.pprint(data)
    else:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(json.dumps(data))
                print("Successfully saved in", path)
        except Exception as e:
            print("Failed to save file.\n" + e)


def main(argv):
    options = get_options(argv)
    links = get_links(options["url"])
    result = {key: get_links(key) for key in links}
    output_result(result, options["output-path"])


if __name__ == "__main__":
    main(sys.argv[1:])
