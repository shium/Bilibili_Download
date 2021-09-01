import requests
import json

class Spider(object):
    def __init__(self, url, conf_json):
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
    conf = {
    "header":{
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.51 Safari/537.36 Edg/93.0.961.27"
    },
    "spider":{
        "//1":"?bvid=",
        "//2":"?cid=(cid)&qn=(qn)&bvid=(bvid)",
        "bv2detail_api":"https://api.bilibili.com/x/web-interface/view",
        "player_api":"https://api.bilibili.com/x/player/playurl"
    },
    "downloader_shell":{
        "name":"./aria2c"
    },
    "video_process":{},
    "qn":{
        "4K":120,
        "1080p60":116,
        "720p60":74,
        "1080p+":112,
        "1080p":80,
        "720p":64,
        "480p":32,
        "360p":16
    }
}
    t = Spider("https://www.bilibili.com/video/BV17p4y1D7dA",conf)
    print(t.bvid)