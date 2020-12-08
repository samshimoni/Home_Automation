import os
import random
import device


def find_my_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


class MusicServer(device.Device):
    def __init__(self):
        self.sonos_playlist = []
        super(MusicServer, self).__init__(__name__)
        self.ip_address = self.cfg.music_server_host
        self.playlist = os.listdir(self.cfg.music_server_src)

        for item in self.playlist:
            self.sonos_playlist.append('http://{0}/music/{1}'
                                       .format(self.cfg.music_server_host, item.replace(' ', '%20')))
        random.shuffle(self.sonos_playlist)
        self.logger.info("music server ip is {}".format(find_my_ip()))

    def give_list(self):
        return self.playlist

    def give_uris(self):
        return self.sonos_playlist

    def is_alive(self):
        pass
