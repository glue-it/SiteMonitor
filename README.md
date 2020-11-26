# SiteMonitor
Python version: Python 3.9


This is a simple script to test site availability

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     url to monitor
  -i INTERVAL, --interval INTERVAL
                        interval between checks in seconds
  -r RETRIES, --retries RETRIES
                        retry count until notification
  -t TIMEOUT, --timeout TIMEOUT
                        timeout for the check in seconds
  -n SLACK, --slack SLACK
                        slack webhook notification value should be webhook url




Usage example: usage: main.py [-h] -u URL [-i INTERVAL] [-r RETRIES] [-t TIMEOUT] [-n SLACK]

without slack: python3.9 main.py --url http://google.com --interval 2 --slack webhookurl
with slack: python3.9 main.py --url http://google.com --interval 2 





 
