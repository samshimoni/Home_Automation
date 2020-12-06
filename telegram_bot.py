from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import logger
from cfg_automation import Cfg


telegram_logger = logger.Logger('telegramBot').logger


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(update: Update, context: CallbackContext) -> None:
    url = get_url()
    chat_id = update.message.chat_id
    telegram_logger.info('Photo sent to {}'.format(update.message.chat.first_name))
    update.message.bot.send_photo(chat_id, url)


def play(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/play')
    update.message.bot.send_message(chat_id, 'Playing')


def pause(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/pause')
    update.message.bot.send_message(chat_id, 'Paused')


def play_next(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/next')
    update.message.bot.send_message(chat_id, 'Playing Next')


def prev(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/prev')
    update.message.bot.send_message(chat_id, 'Playing Previous')


def refresh(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    ans = requests.get('http://127.0.0.1:8000/sonos/refresh').content
    update.message.bot.send_message(chat_id, '{}'.format(ans.decode()))
    update.message.bot.send_message(chat_id, 'Playing')


def photo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/camera/capture')

    try:
        update.message.bot.send_photo(chat_id=chat_id, photo=open('/home/pi/Desktop/Home_Automation/Camera/{}'.format(files[0]), 'rb'))

    except FileNotFoundError:
        print('Could not find any photo to send')

    finally:
        requests.get('http://127.0.0.1:8000/camera/clean')
        telegram_logger.info('cleaned all dir from photos')


class TelegramBot:
    def __init__(self):

        self.cfg = Cfg('cfg.json')
        self.updater = Updater(self.cfg.telegramToken)
        self.updater.dispatcher.add_handler(CommandHandler('bop', bop))
        self.updater.dispatcher.add_handler(CommandHandler('photo', photo))
        self.updater.dispatcher.add_handler(CommandHandler('play', play))
        self.updater.dispatcher.add_handler(CommandHandler('pause', pause))
        self.updater.dispatcher.add_handler(CommandHandler('next', play_next))
        self.updater.dispatcher.add_handler(CommandHandler('prev', prev))
        self.updater.start_polling()
        self.updater.idle()


tb = TelegramBot()

