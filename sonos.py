import soco
import music_server
import device


class SonosMove(device.Device):

    def __init__(self):
        try:
            self.speaker = soco.discover().pop()
            self.refresh()
        except AttributeError:
            raise AttributeError('Failed to connect to Sonos')

    def is_alive(self):
        return str(len(soco.discover()) > 0)

    def play(self):
        self.speaker.play()
        return "Playing..."

    def pause(self):
        self.speaker.pause()
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
        return "Skipped..."

    def prev(self):
        self.speaker.previous()
        return "Going back.."

    def _add_uri_to_sonos(self):
        uri_list = music_server.MusicServer().sonos_playlist
        [self.speaker.add_uri_to_queue(item) for item in uri_list if item.endswith('.mp3')]
        return "Added all into queue"

    def refresh(self):
        old_size = len(self.speaker.get_queue())
        self.speaker.clear_queue()
        self._add_uri_to_sonos()
        new_size = len(self.speaker.get_queue())

        return "Refreshed, {} were add to playlist".format(new_size - old_size)





