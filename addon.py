from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.soundcloud.com/users/soundcloud:users:40330678/sounds.rss"
url2 = "http://feeds.soundcloud.com/users/soundcloud:users:429275703/sounds.rss"
url3 = "http://feeds.feedburner.com/civillibertiesminute"
url4 = "http://feeds.soundcloud.com/users/soundcloud:users:651588261/sounds.rss"
url5 = "http://feeds.soundcloud.com/users/soundcloud:users:469662171/sounds.rss"
url6 = "https://ca-ns-1.bulkstorage.ca/v1/AUTH_0d09c87549084f4ba4ad4a9e807d0d76/8054/feeds/APOR4.xml?temp_url_sig=58589393e4a6720a751332b0e2c747c6cff79af6&temp_url_expires=1888195959&inline"
url7 = "https://aclumnpod.libsyn.com/rss"
url8 = "http://www.acluohio.org/feed/audio"
url9 = "http://feeds.soundcloud.com/users/soundcloud:users:317981333/sounds.rss"
url10 = "https://feed.podbean.com/aclunh/feed.xml"

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
   {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://static.libsyn.com/p/assets/a/3/6/5/a36538cb1437928e/clm_cover_600x600.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000471014112-rqx3e7-original.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://ca-ns-1.bulkstorage.ca/v1/AUTH_0d09c87549084f4ba4ad4a9e807d0d76/8054/feeds/APOR4.jpg?temp_url_sig=975795aca8756b684b736bc82b0b4c74605b0432&temp_url_expires=1572842594&inline"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/0/b/6/c/0b6c44b4b3290fe6/Power_to_Podcast_itunes.png"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://www.podbean.com/podcast-detail/szrfp-4baea/ACLU-of-Ohio-Audio-Podcast"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000409010103-cnijln-original.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/6178760/Logo-1400-final.jpg"},
   ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast3(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
if __name__ == '__main__':
    plugin.run()
