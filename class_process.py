#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, requests, json, httplib2, urllib3, time

class notify:

    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': 'wx754b9',
                  'corpsecret': 'upslRirre4PHo4o',
                  }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        req = requests.post(url, params=values, verify=False)
        data = json.loads(req.text)
        return data["access_token"]

    def send_msg(self):
        h = httplib2.Http('.cache')
        url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + proxy.get_token()
        user = "touser"
        msg = "IP:%s,Service:%s, is halt" %(self.ip, self.name)
        values = {
            "touser": "{}".format(user),
            "msgtype": "text",
            "agentid": "1000004",
            "text": {
                "content": msg
            }
        }

        response, content = h.request(url, 'POST', json.dumps(values), headers={'Content-Type': 'application/json'})

class monitor(notify):

    def __init__(self):
        pass

    def service(self):
        result = {}
        for line in open('ip'):
            line = line.strip('\n').split(":")
            result[(line[0])] = line[1]

        val = result["server"] + ":" + result["port"]
        value = os.system('netstat -na | findstr TCP | findstr %s' % (val))

        if value == 1:
            os.system('start start_python.bat')
            notify.send_msg(self)
        else:
            time.sleep(int(result["time"]))

if __name__=="__main__":
    proxy = monitor()
    proxy.service()



