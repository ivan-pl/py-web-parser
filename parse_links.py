import sys
from getopt import getopt, GetoptError
import requests
from bs4 import BeautifulSoup
import pprint


def get_url(argv):
    url = None
    try:
        opts, args = getopt(argv, 'hu:', ["help", "url="])
    except GetoptError:
        show_error()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        if opt in ("-u, --url"):
            url = arg

    if (url is None):
        show_error()
        sys.exit(3)
    return url


def show_help():
    print('Run "py parse_link.py -u https://ya.ru" '
          'or py parse_link.py --url=https://ya.ru"')


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


def output_result():
    pass


def main(argv):
    url = get_url(argv)
    links = get_links(url)
    result = {key: get_links(key) for key in links}
    pprint.pp(result)
    # output_result(result)


if __name__ == "__main__":
    main(sys.argv[1:])
