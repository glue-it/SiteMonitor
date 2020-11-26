import urllib.request
from urllib.error import URLError, HTTPError
import socket


class SiteMonitor:
    """
    Class for site monitor
    :param url: Url of the site we need to check
    :type url: str
    :param errorCount: number of errors in checks
    :type errorCount: int
    :param interval: interval between checks
    :type url: int
    :param retries: number of max retries threshold
    :type url: int
    :param timeout: timeout of a check
    :type url: int

    """
    def __init__(self, url, interval, retries, timeout):
        self.last_error_message = None
        self.errorCount = 0
        self.url = url
        self.interval = interval
        self.retries = retries
        self.timeout = timeout

    def monitor_site(self):
        try:

            self.__check_site()
            self.errorCount = 0
        # catch in case of HTTP error
        except (HTTPError, URLError) as e:
            self.__handler_error(e.reason)
        # catch in case of socket timeout
        except socket.timeout as e:
            self.__handler_error(e.strerror)
        return

    def __check_site(self):
        urllib.request.urlopen(self.url, timeout=self.timeout)

    def __handler_error(self,error_msg):
        self.errorCount += 1
        self.last_error_message = error_msg
