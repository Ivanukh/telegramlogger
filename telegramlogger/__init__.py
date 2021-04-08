__version__ = '1.0'

import logging
import requests


class TelegramHandler(logging.Handler):

    def __init__(self, token, chat_id):
        super().__init__()
        self.url = f'https://api.telegram.org/bot{token}/sendMessage'
        self.chat_id = chat_id

        self.setFormatter(
            logging.Formatter(f'*%(levelname)s* ```\n%(message)s```')
        )

    def emit(self, record):
        if record.module == 'connectionpool':
            return

        text = self.format(record)
        self._send(text)


    def _send(self, text):
        data = {
            'chat_id': self.chat_id,
            'text': text,
            'parse_mode': 'Markdown'
        }

        try:
            requests.post(self.url, data=data, timeout=1)
        except Exception as e:
            print(e)



class TelegramAggregateHandler(TelegramHandler):
    cache = []
    aggregate_by = None
    separator = None


    def __init__(self, token, chat_id, aggregate_by=50, separator='\n'):
        super().__init__(token, chat_id)
        self.aggregate_by = aggregate_by
        self.separator = separator
        self.setFormatter(
            logging.Formatter(f'%(levelname)s: %(message)s')
        )


    def _send(self, text):
        self.cache.append(text)
        if len(self.cache) > self.aggregate_by:
            super()._send(f'```\n{self.separator.join(self.cache)} ```')
            self.cache = []

    def flush(self):
        if len(self.cache):
            super()._send(f'```\n{self.separator.join(self.cache)} ```')
