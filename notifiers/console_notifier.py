class ConsoleNotifier:
    pass

    def notify(self, **kwargs):
        print(kwargs.get('text', "site is not reachable"))


