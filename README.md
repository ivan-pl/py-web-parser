# py-web-parser
Run parser in order to get all links from some website.
## How
1. Install all dependencies:
  - `pip install -r requirements.txt`
2. Run command:
  - `py parse_links.py -u https://ya.ru`
  
## Options
Supports following flags:
- -o or --output-path — path to save result
- -u or --url — website from which parse links
- -h or --help — get help

## Examples
`py parse_links.py -u https://ya.ru` — print result to console

`py parse_links.py --url=https://ya.ru -o links.txt` — save result in links.txt
