# telegramlogger

Log to telegram

Example:

```
from telegramlogger import TelegramHandler


BOT_TOKEN = 'my_bot token from botfather'
CHAT_ID = 123456789

telegram_handler = TelegramHandler(BOT_TOKEN, CHAT_ID)
telegram_handler.setLevel(logging.DEBUG)

logger = logging.getLogger()

logger.addHandler(telegram_handler)
logger.setLevel(logging.DEBUG)


logger.info('some info')
logger.error('some error')
```
