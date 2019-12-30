from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://lawfare.libsyn.com/rss" #LAWFARE
url2 = "http://steptoecyber.libsyn.com/rss" #CYBERLAW
url3 = "http://rationalsecurity.libsyn.com/rss" #RATIONALSECURITY
url4 = "http://jihadologynet.libsyn.com/rss" #JIHADOLOGY
url5 = "https://feeds.blubrry.com/feeds/national_security_law_podcast.xml" #NATSEC
url6 = "https://feed.pippa.io/public/shows/5d28ef74d3cc3f013778b13b" #THEREPORT
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://lawfare.s3-us-west-2.amazonaws.com/staging/s3fs-public/styles/medium/public/Lawfare-PodcastAvatar.png?itok=rjK_6oT8"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://lawfare.s3-us-west-2.amazonaws.com/staging/s3fs-public/styles/medium/public/TheCyberlawPodcast_2017-08-hires%20%281%29.jpg?itok=b___ahR-"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://lawfare.s3-us-west-2.amazonaws.com/staging/s3fs-public/styles/medium/public/Rational%20Security%20logo_0.png?itok=pcVRKwJE"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://lawfare.s3-us-west-2.amazonaws.com/staging/s3fs-public/styles/medium/public/NkOfBNFM.jpg?itok=BcuDzXqJ"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://is2-ssl.mzstatic.com/image/thumb/Podcasts123/v4/10/b5/66/10b566ac-5343-f075-a8c1-a7b71cabbae2/mza_6922631826374802411.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/bd/26/aa/bd26aa3d-ad9e-9e1d-3633-5fab41bb9373/mza_15643729862565464029.jpeg/600x600bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
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
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
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

if __name__ == '__main__':
    plugin.run()

