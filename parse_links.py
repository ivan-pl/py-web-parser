def args_is_correct():
    pass


def get_options():
    pass


def get_links():
    pass


def show_help():
    pass


def output_result():
    pass


def main():
    if (not args_is_correct()):
        print('Invalid function arguments. Run "py parse_links.py -h"'
              'to get help')
        return

    options = get_options()

    if (options.help):
        show_help()

    links = get_links(options.url)
    result = {key: get_links(key) for key in links}
    output_result(result, options)


if __name__ == "__main__":
    main()
