#  实现在钉钉使用机器人发送任务日志

from datetime import datetime

import requests


class DingLog:
    def __init__(self, url: str):
        now = datetime.now()
        self.msg = now.strftime("%Y/%m/%d (%A) %H:%M:%S")
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.url = url

    def end(self, msg: str, atAll=False):
        headers = {"Content-Type": "application/json"}
        self.msg += "\n= = = = = = = = = = = = = = = = = ="
        self.info(msg)
        if self.url is None or self.url == "ignore":
            pass
        elif self.url == "":
            print(self.msg)
        else:
            data = {"msgtype": "text", "text": {"content": self.msg}}
            if atAll:
                data["at"] = {"isAtAll": "true"}
            data = str(data).encode("utf-8")
            requests.session().post(url=self.url, headers=headers, data=data)

    def info(self, msg: str):
        self.msg += "\n" + msg
