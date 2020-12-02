import os
import random


def find_my_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


class MusicServer:
    def __init__(self):
        self.playlist = []
        self.sonos_playlist = []
        self.match = {}
        self.playlist = os.listdir('/var/www/html/music')
        #random.shuffle(self.playlist)

        for item in self.playlist:
            self.sonos_playlist.append('http://{0}/music/{1}'.format(find_my_ip(), item.replace(' ', '%20')))

        self.match = dict(zip(self.playlist, self.sonos_playlist))

    def give_list(self):
        return self.playlist

    def give_uris(self):
        return self.sonos_playlist
