from urllib.request import Request, urlopen
from urllib.error import URLError
import json


class SlackNotifier:
    """
    Slack webhook notification class
    """
    def __init__(self, webhook_url):
        self.__url = webhook_url
        self.__headers = {"Content-type": "application/json"}
        self.__method = "POST"

    def notify(self, **kwargs):
        data = json.dumps(kwargs).encode()
        req = Request(self.__url, data=data, headers=self.__headers, method=self.__method)
        try:
            return urlopen(req).read().decode()
        except URLError as e:
            print(f"slack notification error: {e}")

