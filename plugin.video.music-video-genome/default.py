import json, urllib, urllib2, xbmc, xbmcgui, xbmcaddon, sys, time

__settings__ = xbmcaddon.Addon(id='script.music-video-genome')

    
def getInput():
    keyboard = xbmc.Keyboard('','Enter Artist:')
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        return keyboard.getText()
    else:
        return ''

def getPlayList(videos):
    ret = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    ret.clear()
    for video in videos:
        url = getURL(video)
        li = xbmcgui.ListItem(label = video['artist'], label2 = video['title'], path = url)
        li.setInfo('video', { 'artist' : video['artist'], 'title' : video['title']})
        ret.add(url, li)
    ret.shuffle()        
    return ret
        
def getURL(video):
    youtubeID = video['video_url'].split('v=')[1].split('&')[0]    
    youtubeurl = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % youtubeID    
    return youtubeurl
    
artistName = getInput()
if (artistName):
    url = u'http://musicvideogenome.com/services/lastfm/genome_artist_search.json?format=json&artist=' + urllib.quote_plus(artistName)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request, timeout = 30)
    videos = json.load(response)['videos']
    player = xbmc.Player()
    player.play(getPlayList(videos))



    