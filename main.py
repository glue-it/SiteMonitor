""" This is a simple script to test site availability
"""

import argparse
from urllib.parse import urlparse
import sys
from site_monitor import SiteMonitor
from monitor_engine import MonitorEngine
from notifiers.slack_notifier import SlackNotifier
from notifiers.console_notifier import ConsoleNotifier


# handle url input if not valid
class Url(argparse.Action):
    """
    custom action for argparse to check Url validation
    """
    def __call__(self, parser, namespace, values, option_string=None):
        error_message = "url not valid, does it contain protocol?"
        try:
            url_parsed = urlparse(values)
            is_valid_url = all([url_parsed.scheme, url_parsed.netloc])
            if is_valid_url:
                setattr(namespace, self.dest, values)
            else:
                show_error(parser, error_message)
        except ValueError:
            show_error(parser, error_message)


def show_error(parser, error_message):
    """
    show help page on error and  prints error
    """
    print(error_message)
    parser.print_help()
    sys.exit(1)


def parse_args():
    """
    parsing arguments
    """
    global args
    parser = argparse.ArgumentParser(description=__doc__, epilog="example of a run python3.9 main.py -u URL")
    parser.add_argument('-u', '--url', action=Url, required=True, help='url to monitor')
    parser.add_argument('-i', '--interval', default=2, type=int, help='interval between checks in seconds')
    parser.add_argument('-r', '--retries', default=2, type=int, help='retry count until notification')
    parser.add_argument('-t', '--timeout', default=30, type=int, help='timeout for the check in seconds')
    parser.add_argument('-n', '--slack',
                        help='slack webhook notification value should be webhook url')
    return parser.parse_args()


def get_notifier(slack):
    """
    get relevant notifier type
    :param slack: slack webhook url
    :type slack: str
    """
    if slack is not None:
        return SlackNotifier(webhook_url=slack)
    else:
        return ConsoleNotifier()


if __name__ == '__main__':
    args = parse_args()
    notifier = get_notifier(args.slack)
    site = SiteMonitor(args.url, args.interval, args.retries, args.timeout)
    monitor_engine = MonitorEngine(site, notifier)
    monitor_engine.start_monitor()

