import telegram



def send_chicken_count_to_farmer():
    telegram.bot("YOUR_TELEGRAM_BOT_TOKEN")
    try:
        bot.send_message(chat_id=("FARMER_CHATID"), text=f'Chicken coup count: {CHICKEN_COUP_COUNT}')
    except:
        print('Error sending message to Telegram')

