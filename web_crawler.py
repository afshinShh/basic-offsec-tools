import requests
import argparse
from termcolor import colored
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',dest='url',
                        help="Target URL or IP address, provide it along http/https",required=True)
    parser.add_argument('-d','--depth',dest='depth',type=int, default=1,
                        help="Depth of crawling, default is 1")
    return parser.parse_args()

class WebCrawler:
    def __init__(self, url, depth):
        pass
    def print_banner(self):
        pass
    def start_crawling(self):
        pass
    def print_results(self):
        pass

if __name__ == '__main__':
    args = get_args()
    web_crawler = WebCrawler(args.url, args.depth)
    web_crawler.print_banner()
    web_crawler.start_crawling()
    web_crawler.print_results()