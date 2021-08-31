import os

class Downloader(object):
    def __init__(self,original_url, download_url, shell):
        self.original_url = original_url
        self.download_url = download_url
        self.shell = shell

        self.check()

    #检查系统内是否安装aria2
    def check(self):
        if self.shell == 'aria2c':
            #判断是否存在此程序
            #flag = False 时存在
            #flag = True 时不存在
            flag = bool(os.system(shell + ' --version'))
            if flag:
                #shell 不存在
                return False

    #下载
    def downloader(self):
        command = '{0} {1} --referer={2}'.format(self.shell, self.download_url, self.original_url)
        os.system(command)

if __name__ == '__main__':
    original_url = "https://www.bilibili.com/video/BV17p4y1D7dA"
    download_url = "https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/92/54/198555492/198555492-1-32.flv?e=ig8euxZM2rNcNbRg7zdVhwdlhWNahwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1630425099&gen=playurlv2&os=hwbv&oi=1695962611&trid=9a01edfb491247a6b639e92331ff586du&platform=pc&upsig=e026320a96b4707de3496dc7665982b0&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000"
    shell = 'aria2c'
    d = Downloader(original_url,download_url, shell)
    d.downloader()