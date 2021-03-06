import soco
import device
import requests
import json


class SonosMove(device.Device):
    def __init__(self):
        super(SonosMove, self).__init__("SonosClient")

        try:
            self.logger.info("Sonos init .. trying to connect to speaker")
            self.speaker = soco.discover().pop()
            self.refresh()

        except AttributeError:
            self.logger.error("Problem with init speaker' make sure it's on")
            raise AttributeError('Failed to connect to Sonos')

    def is_alive(self):
        self.logger.info("is alive response => {}".format(str(len(soco.discover()) > 0)))
        return len(soco.discover()) > 0

    def play(self):
        self.speaker.play()
        self.logger.info("Playing, {}".format(self._get_current_song()))
        return "Playing...".format(self._get_current_song())

    def pause(self):
        self.speaker.pause()
        self.logger.info("Paused")
        return "Paused ..."

    def volume(self, value):
        try:
            if self.speaker.volume + int(value) < 0 or self.speaker.volume + int(value) > 100:
                return " Must be between 0 and 100"
            self.speaker.volume += int(value)
            return "Changed to {}".format(value)

        except ValueError:
            return "Value must be Integer "

    def next(self):
        self.speaker.next()
        self.logger.info("Skipped to => {}".format(self._get_current_song()))
        return "Skipped..."

    def prev(self):
        self.speaker.previous()
        self.logger.info("Going back to => {}".format(self._get_current_song()))
        return "Going back.."

    def _add_uri_to_sonos(self):
        uri_list = json.loads(requests.get("http://{0}:{1}/music_server/give_uris"
                                           .format(self.cfg.music_flask_host,
                                                   self.cfg.music_flask_port)).content.decode())['uris']
        try:
            [self.speaker.add_uri_to_queue(item) for item in uri_list if item.endswith('.mp3')]
        except Exception as e:
            self.logger.error(e)

        self.logger.info("add {} into playlist".format(len(uri_list)))
        self.speaker.play()
        return "Added all into queue"

    def refresh(self):
        old_size = len(self.speaker.get_queue())
        self.speaker.clear_queue()
        self._add_uri_to_sonos()
        new_size = len(self.speaker.get_queue())
        return "Refreshed, {} were add to playlist".format(new_size - old_size)

    def _get_current_song(self):
        return self.speaker.get_current_track_info()['title']
