from Config.Set_Config import conf_json
from Spider import Spider
import sys

def main(url):
    spider = Spider(url, conf_json)

main(sys.argv)