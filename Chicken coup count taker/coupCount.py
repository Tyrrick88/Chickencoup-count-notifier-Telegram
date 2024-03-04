import time
from telegram import Bot
from telegram.error import TelegramError

# Here add your Telegram bot token
bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')


CHICKEN_COUP_COUNT = 50

# Here input your telegram user id
FARMER_TELEGRAM_USER_ID = (int(Input("Your telegram   user id: ").strip()),)

def send_chicken_count_to_farmer():
    try:
        bot.send_message(chat_id=FARMER_TELEGRAM_USER_ID, text=f'Chicken coup count: {CHICKEN_COUP_COUNT}')
    except TelegramError as e:
        print(f'Error sending message to Telegram: {e}')

while True:
    time.sleep(3600 * 7) # wait for 7 hours
    send_chicken_count_to_farmer()
