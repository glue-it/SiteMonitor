import time


class MonitorEngine:
    """
    Monitor engine logic while loop
    """
    def __init__(self, site_monitor, notifier):

        self.__site = site_monitor
        self.__notifier = notifier

    def start_monitor(self):
        """
        Monitor method which starts the infinite loop
        """
        while True:
            self.__site.monitor_site()
            if self.__site.errorCount == self.__site.retries:
                self.__notifier.notify(text=f"site:{self.__site.url} is down. Error:{self.__site.last_error_message}")
                self.__site.errorCount = 0
            time.sleep(self.__site.interval)

