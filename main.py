'''
Filename: /home/rakyui/Code/Bilibili_Download/main.py
Path: /home/rakyui/Code/Bilibili_Download
Created Date: Tuesday, August 31st 2021, 9:16:04 pm
Author: 辻一

Copyright (c) 2021 辻一
'''

from Config.Set_Config import conf_json
from Spider.Spider import Spider
from Downloader.Downloader import Downloader
import sys

def main(url):
    spider = Spider(url, conf_json)
    download = Downloader(spider.URL, spider.download_url, 'aria2c')
    download.downloader()


main(sys.argv[1])