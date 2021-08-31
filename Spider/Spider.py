import requests
import json

#定位父文件夹位置
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)

from Config.Set_Config import conf_json

class Spider(object):
    def __init__(self, url):
        #获取视频链接并提取BV号
        self.URL = self.check_url(url)
        tmp = [i for i in url.split('/') if i is not '']
        self.bvid = tmp[-1]

        #获取bilibili的api接口
        self.bv2detail_api = conf_json['spider']['bv2detail_api']
        self.player_api = conf_json['spider']['player_api']

        self.cid = self.get_cid()
        self.download_url = self.get_download_url()


    #检查链接地址是否合法
    def check_url(self, url):
        url_bool = 'bilibili' in url
        type_bool = 'video' in url
        BV_bool = 'BV' in url
        if url_bool & type_bool & BV_bool:
            return url
        else:
            raise IndexError('网址不合法')
        

    #获取cid
    def get_cid(self):
        payload = {'bvid':self.bvid}
        req = requests.get(self.bv2detail_api, params=payload)
        return req.json()['data']['cid']

    #获取下载链接
    def get_download_url(self):
        payload = {'cid':self.cid, 'bvid':self.bvid}
        req = requests.get(self.player_api, params=payload)
        return req.json()['data']['durl'][0]['url']



if __name__=="__main__":
    t = Spider("https://www.bilibili.com/video/BV17p4y1D7dA")
    print(t.bvid)