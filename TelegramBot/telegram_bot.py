from telegram import Update
import os
import re
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import logger
import cfg_automation


telegram_logger = logger.Logger('telegramBot').logger
cfg = cfg_automation.Cfg()


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(update: Update, context: CallbackContext) -> None:
    url = get_url()
    chat_id = update.message.chat_id
    telegram_logger.info('Photo sent to {}'.format(update.message.chat.first_name))
    update.message.bot.send_photo(chat_id, url)


def plant_water(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    telegram_logger.info('Watering plant')
    response = requests.get('http://{0}:{1}/plant/auto_water'.format(cfg.plantAddress, cfg.plantPort)).content
    update.message.bot.send_message(chat_id, 'watering.. wait for mail please..')


def play(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id

    requests.get('http://{0}:{1}/sonos/play'.format(cfg.flaskAddress, cfg.flaskPort))
    update.message.bot.send_message(chat_id, 'Playing')


def pause(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://{0}:{1}/sonos/pause'.format(cfg.flaskAddress, cfg.flaskPort))
    update.message.bot.send_message(chat_id, 'Paused')


def play_next(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://{0}:{1}/sonos/next'.format(cfg.flaskAddress, cfg.flaskPort))
    update.message.bot.send_message(chat_id, 'Playing Next')


def prev(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://{0}:{1}/sonos/prev'.format(cfg.flaskAddress, cfg.flaskPort))
    update.message.bot.send_message(chat_id, 'Playing Previous')


def refresh(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    ans = requests.get('http://{0}:{1}/sonos/refresh'.format(cfg.flaskAddress, cfg.flaskPort)).content
    update.message.bot.send_message(chat_id, '{}'.format(ans.decode()))
    update.message.bot.send_message(chat_id, 'Playing')


def photo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/camera/capture')

    try:
        cfg = cfg_automation.Cfg()
        files = [f for f in os.listdir('../Camera') if re.match(r'[0-9]+.*\.jpg', f)]
        for file in files:
            update.message.bot.send_photo(chat_id=chat_id, photo=open(cfg.camera_photos_dir + "/" + file, 'rb'))
            telegram_logger.info("photo {0} send to {1}".format(file, update.message.chat.first_name))

    except FileNotFoundError:
        telegram_logger.error('could not send photos')

    finally:
        requests.get('http://127.0.0.1:8000/camera/clean')
        telegram_logger.info('cleaned all dir from photos')


class TelegramBot:
    def __init__(self):
        self.updater = Updater(cfg.telegramToken)
        self.updater.dispatcher.add_handler(CommandHandler('bop', bop))
        self.updater.dispatcher.add_handler(CommandHandler('photo', photo))
        self.updater.dispatcher.add_handler(CommandHandler('play', play))
        self.updater.dispatcher.add_handler(CommandHandler('pause', pause))
        self.updater.dispatcher.add_handler(CommandHandler('next', play_next))
        self.updater.dispatcher.add_handler(CommandHandler('prev', prev))
        self.updater.dispatcher.add_handler(CommandHandler('plant', plant_water))
        self.updater.start_polling()
        self.updater.idle()


tb = TelegramBot()
