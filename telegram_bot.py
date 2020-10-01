from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import re
import os
import config
from sensibo import *
sensibo = SensiboClientAPI(config.token_ac)


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def play(bot, update):
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/play')
    bot.send_message(chat_id, 'Playing')


def pause(bot, update):
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/pause')
    bot.send_message(chat_id, 'Paused')


def play_next(bot, update):
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/next')
    bot.send_message(chat_id, 'Playing Next')


def prev(bot, update):
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/sonos/prev')
    bot.send_message(chat_id, 'Playing Previous')




def refresh(bot, update):
    chat_id = update.message.chat_id
    ans = requests.get('http://127.0.0.1:8000/sonos/refresh').content
    bot.send_message(chat_id, '{}'.format(ans.decode()))
    bot.send_message(chat_id, 'Playing')


def photo(bot, update):
    chat_id = update.message.chat_id
    requests.get('http://127.0.0.1:8000/camera/capture')

    files = [f for f in os.listdir('./Camera') if re.match(r'[0-9]+.*\.jpg', f)]

    try:
        bot.send_photo(chat_id=chat_id, photo=open('/home/pi/Desktop/Home_Automation/Camera/{}'.format(files[0]), 'rb'))

    except FileNotFoundError:
        print('Could not find any photo to send')

    finally:
        for f in files:
            os.remove(os.path.join('/home/pi/Desktop/Home_Automation/Camera', f))


def get_devices():
    devices = sensibo.devices()
    return devices


def change_ac(bot, update):
    chat_id = update.message.chat_id
    devs = sensibo.devices()
    uid = devs['main']
    ac_state = sensibo.pod_ac_state(uid)
    sensibo.pod_change_ac_state(uid, ac_state, "on", not ac_state['on'])
    bot.send_message(chat_id, 'Turned the Ac On ')


def main():
    updater = Updater(config.token_bot)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('cameraPhoto', photo))
    dp.add_handler(CommandHandler('sonosPlay', play))
    dp.add_handler(CommandHandler('sonosPause', pause))
    dp.add_handler(CommandHandler('sonosNext', play_next))
    dp.add_handler(CommandHandler('sonosPrev', prev))
    dp.add_handler(CommandHandler('sonosRefresh', refresh))
    dp.add_handler(CommandHandler('ac_on', change_ac))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
