from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://feeds.soundcloud.com/users/soundcloud:users:40330678/sounds.rss"
URL2 = "http://feeds.soundcloud.com/users/soundcloud:users:429275703/sounds.rss"
URL3 = "http://feeds.feedburner.com/civillibertiesminute"
@plugin.route('/')
def main_menu():
    items = [
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.aclu.org/files/podcast/podcast-at-liberty-landing-page-cover.jpg"},
   {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000427832679-g12u3l-original.jpg"},
   {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://static.libsyn.com/p/assets/a/3/6/5/a36538cb1437928e/clm_cover_600x600.jpg"},
   ]
    return items

@plugin.route('/episodes/')
def episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(URL2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(URL3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

if __name__ == '__main__':
    plugin.run()
