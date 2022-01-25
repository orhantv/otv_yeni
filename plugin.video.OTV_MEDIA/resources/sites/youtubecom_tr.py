#-*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        YouTube
# Purpose:
#
# Author:      orhan
#
# Created:     29.04.2021
# Copyright:   (c) orhan 2021
# Licence:     <your licence>

#Host: www.youtube.com
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
#Accept-Language: de-DE,tr-TR;q=0.8,tr;q=0.6,en-US;q=0.4,en;q=0.2
#Connection: keep-alive
#Cookie: VISITOR_INFO1_LIVE=ZRDxplgH874; CONSENT=YES+DE.de+V14+BX+768; PREF=f4=4000000&tz=Europe.Berlin; GPS=1
#Upgrade-Insecure-Requests: 1
#Accept-Encoding: gzip, deflate
from resources.sites.LIVETV2 import *

SITE_IDENTIFIER = 'youtubecom_tr'
SITE_NAME = 'YouTube'
SITE_DESC = 'YouTube'

       
YUPA = 'https://www.y2mate.com/mates/analyze/ajax'
URL_MAIN = 'http://www.youtube.com/embed/'
URL_PIC = 'http://s.dogannet.tv/'
URL_LIVE = 'https://www.youtube.com/watch?v='
MOVIE_MOVIE = ('http://', 'showAlpha')
MOVIE_GENRES = (True, 'showGenre')

api_key=''
URL_SEARCH = ('', 'showMovies')
def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string
AddonID = 'plugin.video.OTV_MEDIA'
addon = xbmcaddon.Addon(AddonID)

USER_DATA_DIR = translatePath(addon.getAddonInfo("profile"))

playlistsFile2 = os.path.join(USER_DATA_DIR, "playLists.txt")
playlistsFile3 = os.path.join(USER_DATA_DIR, "FolderListe3.txt")

playlistsFile4 = os.path.join(USER_DATA_DIR, "FolderLists.txt")


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

#  ,"Referer": sUrl

from collections import OrderedDict				
if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)
from resources.lib.comaddon import dialog
from resources.lib.util import Unquote, Quote
def yvideos(v_id,itag):
         #sourcestr = 'https://raw.githubusercontent.com/iptv-org/iptv/master/scripts/data/countries.json'
         #sHtmlContent = getHtml(sourcestr) 
        # logger.info("metin-%s " %metin)
         from youtubesearchpython.extras import Video
         video = Video.get("https://www.youtube.com/watch?v=%s"%v_id )
		
                      
         
         sPattern = "'itag': "+itag+", 'url': '(.+?)'"
         oParser = cParser()
         aResult = oParser.parse(video, sPattern)
         if (aResult[0] == True):
              return  aResult[1][0] 
class Search:
	
	def __init__(self,video_id):
		
		        #"itag":18,"url":"
		html = urllib.request.urlopen("https://www.youtube.com/watch?v=" + video_id)
		
		self.source = html.read().decode('utf8')
		
		
	def videos(self):                                                                                                                                                 
		limit = self.limit
		source = self.source
		data  = re.findall('{\"videoRenderer\":{\"videoId\":\"(\S{11})\",\"thumbnail\":{\"thumbnails\":\[{\"url\":\"(\S+)\",\"width\":.+?,\"height\":.+?}\]},\"title\":{\"runs\":\[{\"text\":\"(.+?)\"}\],\"accessibility\":{\"accessibilityData\":{\"label\":\"(.+?)\"}}},\"longBylineText\"',source)
		data_ = []
		for i in data:
				js_data = {"video_id":"",
		            "video_title":"", 
		             "video_thumbnail" : "" ,
		              "video_description":""}
				js_data['video_id'] = i[0]
				js_data['video_title'] = i[2]
				js_data['video_thumbnail'] = i[1]
				js_data['video_description'] = i[3]
				data_.append(js_data)
		value =  json.dumps(data_ )
		return json.loads(value)






def youtubeHtml(sUrl):  # S'occupe des requetes
       # Host ='www.youtube.com'
        UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        headers = {"User-Agent": UA}
        req = urllib2.Request(sUrl, None, headers)
        try:
            response = urllib2.urlopen(req)
        except UrlError as e:
            print(e.read())
            print(e.reason)

        data = response.read()
        head = response.headers
        response.close()
        return to_utf8(data )
        logger.info("data : %s" % str(data))
        logger.info("sUrl : %s" % str(head))
        
def myoutubeHtml(sUrl):  # S'occupe des requetes

          
        #cookie_string = SetCookie(sUrl)
        #logger.info("sUrl : %s" % str(cookie_string))
        oRequestHandler = cRequestHandler(sUrl)
        oRequestHandler.addHeaderEntry('x-goog-visitor-id' ,'CgszMGVXU0tiMmZCayjukduOBg%3D%3D')
        oRequestHandler.addHeaderEntry('authorization' ,'SAPISIDHASH 1641466135_3e4b2ccb4f9945d23b06e27ceeba54a9800ded90')
        oRequestHandler.addHeaderEntry('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
        oRequestHandler.addHeaderEntry('Cookie','LOGIN_INFO=AFmmF2swRgIhAL7N_yOAYI9PB8CG5_cb5uPwqwdAPb50nL6Z2-fxUIbOAiEAr0ww73kuJRoC95NUysdInW6yGsQ5Xp5cB7zAlVSU-Qs:QUQ3MjNmeXFMY1hETDlPSmphTFBnYXVvdDI2cTZiM1N0S3ltZXNZSlJCN2djS3Exa0hCbXRLaXY3OXl2eFNOOFdCQ05hdTNSQ0NLT2Y3LWxnYUdMeWk4a3k5RnQxYmZsbkI3Q3NWMTE5VElOYWg3V1NTS0NFWmh1ZDE0TGVmNEQyUDFHdG9pZjBvNFhTbEZHMTVkTFVmVDNMemo3OTVwUl9n; PREF=f4=4000000&tz=Europe.Berlin; HSID=AKUnhe-ZlOfoqqgia; SSID=ADFkrrq3kH3zNWHJX; APISID=Jb69vpE8vMhmVodM/AGkP3Ufhk6NPhCzDY; SAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; __Secure-1PAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; __Secure-3PAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; SID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fgA5j1vInaJb6qt0Mpnqurug.; __Secure-1PSID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fgEkimUXvQjlRhpFiDX1FkEA.; __Secure-3PSID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fg-XVKhieotrywuaXC2K7VVQ.; VISITOR_INFO1_LIVE=30eWSKb2fBk; YSC=vXcBOM4sCO0; SIDCC=AJi4QfGc3xQZRYwttOPG8rUbhNbuaIpisv8tDLjJJ0ttZDYUDK1bNpBns1TQPEP1_lp-bXxVa4Y; __Secure-3PSIDCC=AJi4QfGsI9esg2nMe5iCwaaPdGK43suO8b1RAY-3I1DbDnYfKAgGVIBdanuKeBa22Oh904s8GJI')
       
#        oRequestHandler.addHeaderEntry('accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9')
        oRequestHandler.addHeaderEntry('Referer','https://www.youtube.com/embed/De0TY3j3_5s?rel=0&enablejsapi=1&autoplay=0')
        oRequestHandler.addHeaderEntry('x-client-data',' CIm2yQEIorbJAQjEtskBCKmdygEIibnKAQjDw8oBCPjHygEIy+XKAQiymssBCNWcywEI5JzLAQipncsBGOGaywE=Decoded:message ClientVariations {  // Active client experiment variation IDs. repeated int32 variation_id = [3300105, 3300130, 3300164, 3313321, 3316873, 3318211, 3318776, 3322571, 3329330, 3329621, 3329636, 3329705];// Active client experiment variation IDs that trigger server-side behavior.  repeated int32 trigger_variation_id = [3329377];}')
       # oRequestHandler.addHeaderEntry('Cookie', LOGIN_INFO=AFmmF2swRgIhAL7N_yOAYI9PB8CG5_cb5uPwqwdAPb50nL6Z2-fxUIbOAiEAr0ww73kuJRoC95NUysdInW6yGsQ5Xp5cB7zAlVSU-Qs:QUQ3MjNmeXFMY1hETDlPSmphTFBnYXVvdDI2cTZiM1N0S3ltZXNZSlJCN2djS3Exa0hCbXRLaXY3OXl2eFNOOFdCQ05hdTNSQ0NLT2Y3LWxnYUdMeWk4a3k5RnQxYmZsbkI3Q3NWMTE5VElOYWg3V1NTS0NFWmh1ZDE0TGVmNEQyUDFHdG9pZjBvNFhTbEZHMTVkTFVmVDNMemo3OTVwUl9n; PREF=f4=4000000&tz=Europe.Berlin; HSID=AKUnhe-ZlOfoqqgia; SSID=ADFkrrq3kH3zNWHJX; APISID=Jb69vpE8vMhmVodM/AGkP3Ufhk6NPhCzDY; SAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; __Secure-1PAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; __Secure-3PAPISID=nhtCujqQpHOmLSMv/AOtBo5bOZX9smEY1D; SID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fgA5j1vInaJb6qt0Mpnqurug.; __Secure-1PSID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fgEkimUXvQjlRhpFiDX1FkEA.; __Secure-3PSID=FQhgtwYaH5lG3lmYxc1WZXY4DlVfcwhvxH-o8aHiLtmJ17fg-XVKhieotrywuaXC2K7VVQ.; VISITOR_INFO1_LIVE=30eWSKb2fBk; YSC=vXcBOM4sCO0; SIDCC=AJi4QfGc3xQZRYwttOPG8rUbhNbuaIpisv8tDLjJJ0ttZDYUDK1bNpBns1TQPEP1_lp-bXxVa4Y; __Secure-3PSIDCC=AJi4QfGsI9esg2nMe5iCwaaPdGK43suO8b1RAY-3I1DbDnYfKAgGVIBdanuKeBa22Oh904s8GJI)
        data = oRequestHandler.request()
        logger.info("data : %s" % str(data))
        

        return to_utf8(data )





def YouTUBE():
    oGui = cGui()
    

    tarzlistesi = []
    tarzlistesi.append(("Search videos", "showSearch1"))
    
#    tarzlistesi.append(("Search channels", "Searchchannel"))
    tarzlistesi.append(("Search playlists", "Searchplaylist"))                                     
    tarzlistesi.append(("live broadcasts on youtube", "showSearch3")) 
    tarzlistesi.append(("canli yayin", "showSearch3")) 
    tarzlistesi.append(("canli radyo", "showSearch3")) 
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
        oGui.addDir(SITE_IDENTIFIER, sUrl2, sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
def Searchchannel():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'Searchchannel2', 'Search channels', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile3)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]                                                
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'Searchchannel5', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil3', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()   
def listeyisil3():
   from resources.lib import comon
   comon.DelFile(playlistsFile3)
   return      

def Searchchannel2():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile3)
       listUrl = 'https://youtube.otvmedia'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile3, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
            
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', channel_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   
def Searchchannel5():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #sTitle =cat['Title']
            sPicture=cat['video_thumbnail']
            sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            channel_id=cat['channel_id']
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   

def Searchchannel3():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            channel_id = oInputParameterHandler.getValue('siteUrll')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.get_channel_metadata(channel_id)                   
            logger.info("Searchchannel3channel_id: %s" % data) 
            for cat in data:
                #video_id =cat['video_id']
            #sTitle =cat['Title']
                           
                sTitle=cat['title']
                des=cat['description']
                channel_id=cat['channel_id']
             
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', playlist_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel4', sTitle, sPicture, sPicture, "-- Bölüm- %s" %str(des) , oOutputParameterHandler)
            oGui.setEndOfDirectory()   


def Searchchannel4():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sTitle  = oInputParameterHandler.getValue('sMovieTitle')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            s_num = 0
            data =yt.get_video_metadata_gen(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video =cat['video_id']
            #sTitle =cat['Title']
               
                #sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                #des=cat['playlist_n_videos']
                #playlist_id=cat['playlist_id']
                s_num += 1 
              
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video)
               # oOutputParameterHandler.addParameter('siteUrll', video)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox3', sTitle+"-Video- %s" % str(s_num+0),'','', sTitle, oOutputParameterHandler)
            oGui.setEndOfDirectory()   

def msshowBox3():                       
    oGui = cGui()                                                                        
    oInputParameterHandler = cInputParameterHandler()
    v_id = oInputParameterHandler.getValue('siteUrl')
    logger.info("v_id : %s" % v_id )
    name = oInputParameterHandler.getValue('sMovieTitle')
    sHtmlContent = y2mate(v_id).replace('<span class="label label-primary"><small>', '-').replace('</small></span>', '')
    logger.info("sHtmlContent : %s" % sHtmlContent )
    if '.m3u8' in sHtmlContent:
      addLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,sHtmlContent,'')
    else:   
      
      oOutputParameterHandler = cOutputParameterHandler()
      oOutputParameterHandler.addParameter('siteUrl', v_id)
      oOutputParameterHandler.addParameter('sMovieTitle', str(name))
      oGui.addDir(SITE_IDENTIFIER, 'myeniplay', 'EXTRA_PLAY', 'genres.png', oOutputParameterHandler)
      sHtmlContent =sHtmlContent
      _id = re.search('k__id = "(.+?)"', sHtmlContent).group(1)
      oParser = cParser()         
      sPattern = '<a href=".*?" rel="nofollow">(.*?)</a>.*?<a href=".*?" rel="nofollow" type="button" class="btn btn-success" data-toggle=".*?" data-target=".*?" data-ftype="(.*?)" data-fquality="(.*?)">'
      aResult = oParser.parse(sHtmlContent, sPattern)
      if not (aResult[0] == False):
         total = len(aResult[1])
         for aEntry in aResult[1]:
           
            sTitle = aEntry[0]                                                                  
            
            ftype = aEntry[1]
            fquality= aEntry[2]
            sTitle = malfabekodla(sTitle)
            oOutputParameterHandler = cOutputParameterHandler()
#            oOutputParameterHandler.addParameter('sThumbnail', str(sPicture))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('v_id', v_id)
            oOutputParameterHandler.addParameter('_id', _id)
            oOutputParameterHandler.addParameter('ftype', ftype)
            oOutputParameterHandler.addParameter('fquality', fquality)
            oGui.addMovie(SITE_IDENTIFIER, 'y2mateplay', sTitle,'', '','', oOutputParameterHandler)

    oGui.setEndOfDirectory()

name=None
mode=None
desc=None
resim=None
m_id=None
konu=None
isTv = '0'
timestamp = 0
def mmsshowBox2():                       
    oGui = cGui()                                                                        
    oInputParameterHandler = cInputParameterHandler()
    v_id = oInputParameterHandler.getValue('siteUrl')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = 'https://www.youtube.com/watch?v=' + v_id
    oynat(url,name,resim,desc,m_id,timestamp,isTv)
def msshowBox2():                       
    oGui = cGui()                                                                        
    oInputParameterHandler = cInputParameterHandler()
    v_id = oInputParameterHandler.getValue('siteUrl')
    sPicture = oInputParameterHandler.getValue('sThumbnail')
    name = oInputParameterHandler.getValue('sMovieTitle')
    url = 'https://www.youtube.com/watch?v=' + v_id
    html =youtubeHtml(url)
    html = html.replace('\\','')
    logger.info("html : %s" % url )
    if '.m3u8' in html:
        link = re.findall('"(http[^"]+m3u8)"', html, re.IGNORECASE)[0]
        page =youtubeHtml(link)
        url_main = '/'.join(link.split('/')[:-1]) + '/'
        page1 = youtubeHtml(url_main)
        qualitylist = re.findall(',RESOLUTION=.*?x([0-9]+)', page1)
        videolist= re.findall('(https.*?m3u8)', page1)
        sHtmlContent=videolist[-1:][0]
        addLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,sHtmlContent,sPicture)
    else:   
        #from youtubesearchpython.extras import Video
        #from youtubesearchpython.streamurlfetcher import StreamURLFetcher    
        #fetcher = StreamURLFetcher()                   
        video = v_id
        url = yvideos(video, '22')
        logger.info("22url: %s" % url)
        if url == None:
           url = yvideos(video, '18')
          
           logger.info("18url: %s" % url)
#        logger.info("data : %s" % data)   
        #url =url+'&alr=yes&cpn=skj1Expb38VhETbH&cver=2.20220121.01.00&range=163759-332602&rn=13&rbuf=9255'
        nextplay('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url)
               
def y2mate( __sUrl):
    from resources.lib.gui import parsers
    url = 'https://www.youtube.com/watch?v=' + __sUrl 
    html =youtubeHtml(url)
    html = html.replace('\\','')
    logger.info("html : %s" % url )
    if '.m3u8' in html:
        link = re.findall('"(http[^"]+m3u8)"', html, re.IGNORECASE)[0]
        page =youtubeHtml(link)
        url_main = '/'.join(link.split('/')[:-1]) + '/'
        page1 = youtubeHtml(url_main)
        qualitylist = re.findall(',RESOLUTION=.*?x([0-9]+)', page1)
        videolist= re.findall('(https.*?m3u8)', page1)
        return videolist[-1:][0]
           
def y2mateplay():
        oInputParameterHandler = cInputParameterHandler()
        name = oInputParameterHandler.getValue('sMovieTitle')
        v_id = oInputParameterHandler.getValue('v_id')
        _id = oInputParameterHandler.getValue('_id')
        ftype = oInputParameterHandler.getValue('ftype')
        fquality = oInputParameterHandler.getValue('fquality')
        sPicture = oInputParameterHandler.getValue('sThumbnail')   
        
        s = requests.Session()
        cookie_string = "; ".join([str(x) + "=" + str(y) for x, y in s.cookies.items()])
        token = 'https://y2mate.tv/mates/convert'
        post_data = {'type': 'youtube','_id':_id,'v_id':v_id,'ajax':'1','token':'','ftype':ftype,'fquality':fquality}
        r = s.post(token, headers={'Referer': 'https://y2mate.tv/youtube/'+v_id,
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Host': 'y2mate.tv',
             'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'}, data=post_data, timeout=10)
        urll = to_utf8(r.text).replace("\\n", '').replace("\\r", '').replace("\\", '')
        #urll = r.text.replace("\n", '').replace("\t", '')
        url = re.search('<a href="(.+?)"', urll).group(1)
        logger.info("urllurll  : %s" % urll )
        nextplay('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url)
def Searchplaylist():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'Searchplaylist2', 'Search playlists', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile4)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'Searchplaylist5', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil2', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()   
def Searchplaylist5():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #sTitle =cat['Title']
            sPicture=cat['video_thumbnail']
            sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            channel_id=cat['channel_id']
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   

def listeyisil2():
   from resources.lib import comon
   comon.DelFile(playlistsFile4)
   return

def Searchplaylist2():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile4)
       listUrl = 'https://youtube.otvmedia'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile4, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
            
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   
def Searchplaylist3():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.get_playlists(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                #video_id =cat['video_id']
            #sTitle =cat['Title']
               
                sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                des=cat['playlist_n_videos']
                playlist_id=cat['playlist_id']
             
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', playlist_id)
                oOutputParameterHandler.addParameter('siteUrll', playlist_id)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchplaylist4', sTitle, sPicture, sPicture, "-- Videos- %s" %str(des) , oOutputParameterHandler)
            oGui.setEndOfDirectory()   

def Searchplaylist4():
            oGui = cGui()
            oInputParameterHandler = cInputParameterHandler()
            playlist_id = oInputParameterHandler.getValue('siteUrll')
            sTitle  = oInputParameterHandler.getValue('sMovieTitle')
            sPicture= oInputParameterHandler.getValue('sThumbnail')
            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            s_num = 0
            data =yt.get_videos_from_playlist_id(playlist_id)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video =cat['video_id']
            #sTitle =cat['Title']
               
                #sTitle=cat['playlist_name'].replace('#', '').replace('amp;', '').replace('39;', '')
                #des=cat['playlist_n_videos']
                #playlist_id=cat['playlist_id']
                s_num += 1 
              
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video)
               # oOutputParameterHandler.addParameter('siteUrll', video)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox3', sTitle+"-Bölüm- %s" % str(s_num+0),'','', sTitle, oOutputParameterHandler)
            oGui.setEndOfDirectory()   


def showSearch():
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile2)
       listUrl = 'https://youtube.otvmedia'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile2, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            
            data =yt.search(sSearchText)                   
            logger.info("showSearch-video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
                des=videoDetails(video_id)
                logger.info("video_id-des : %s" % des)
                
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                channel_id=cat['channel_id']
                desc=desc+'--------' + des
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', video_id)
                oOutputParameterHandler.addParameter('siteUrll', channel_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   

def showSearch1():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Search', 'search.png', oOutputParameterHandler)

    from resources.lib import comon
    listDir = comon.ReadList(playlistsFile2)
    for fold in listDir:
      name = fold["name"]
      url =fold["url"]
 
      tarzlistesi = []
      
      tarzlistesi.append((name, url))
      for sTitle,sUrl2 in tarzlistesi:
        sTitle =replaceHTMLCodes(sTitle)    
        sTitle =malfabekodla(sTitle) 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oGui.addDir(SITE_IDENTIFIER,'showSearch3', sTitle, 'genres.png', oOutputParameterHandler)         
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', 'http://')
    oGui.addDir(SITE_IDENTIFIER, 'listeyisil', '[COLOR blue][B]Delete search list--Arama listesini sil[/B][/COLOR]' , 'icondelete.jpg', oOutputParameterHandler)

                                               
    oGui.setEndOfDirectory()                   
def listeyisil():
   from resources.lib import comon
   comon.DelFile(playlistsFile2)
   return
def raw_json_with_datetime(item):
    '''
    Returns the raw json output from the API.
    '''
    item['collection_date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    return item

def showSearch3():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =yt.search(sSearchText)                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #des=videoDetails(video_id)
            #logger.info("video_id-des : %s" % des)
            sPicture=cat['video_thumbnail']
            name=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            de=cat['collection_date'] #= datetime.datetime.now()
            channel_id=cat['channel_id']
            desc=desc+"[COLOR red] TIME - %s[/COLOR]" % de
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sSearchText ))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', name, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory()   


def myfeeds():
    oGui = cGui()
    from .YouTubeUi import YouTubeSetup
    tarzlistesi = []
    tarzlistesi.append(("My Subscriptions", "my_subscriptions"))
    
    tarzlistesi.append(("Liked videos", "my_liked_videos"))
    tarzlistesi.append(("Uploads", "my_uploads"))                                     
    tarzlistesi.append(("Playlists", "my_playlists")) 
    for sTitle,sUrl2 in tarzlistesi:
           
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl2)
        if sTitle == 'TÚRK Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeturk', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'Search2':
             oGui.addDir(SITE_IDENTIFIER, 'showSearch2', sTitle, 'genres.png', oOutputParameterHandler)

        elif sTitle == 'Arabic Sinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubearabic', sTitle, 'genres.png', oOutputParameterHandler)
        elif sTitle == 'German Cinema Musik Video':
             oGui.addDir(SITE_IDENTIFIER, 'yotubeargermany', sTitle, 'genres.png', oOutputParameterHandler)

        else:
             oGui.addDir(SITE_IDENTIFIER, 'pageshowMovies', sTitle, 'genres.png', oOutputParameterHandler)
                   
                    
    oGui.setEndOfDirectory()
       
def playlit():

        from youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
        video_id = 'DdnALiv-z8g'
        video_container = 'Takiyeli Siyaset'
        video_title='Takiyeli Siyaset" nereye kadar'
        aResult =yt.get_video_streams(video_title, video_container, video_id)[0]
        for data in aResult['meta']:
            url=data['video']['title']              
            logger.info("get_video_streams : %s" % url)    
                #Py3 a besoin de la deuxieme version, je laisse le 1er replace au cas où pour Py2
                #sUrl=aEntry[0].replace("\u0026","&").replace("\\u0026","&")
                #sTitle =aEntry[1]
           
                #oOutputParameterHandler = cOutputParameterHandler()
                #oOutputParameterHandler.addParameter('siteUrl', sUrl)
                #oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
               # oGui.addDir(SITE_IDENTIFIER,'yeniplay', sTitle, 'search.png', oOutputParameterHandler)


          
          
def nextplay(name, url):
	        sUrl =(url)
	        sUrl1 =(url)
	        sUrl2 =(url)
	        sUrl3 =(url)
	        sUrl4 =(url)
	        sUrl5 =(url)
	        sUrl6 =(url)
	        sUrl7 =(url)
	     
   
	        playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO); 
    
	        playlist.clear();
	        listitem1 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl,listitem1);
	        listitem2 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl1,listitem2);
	        listitem3 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl2,listitem3);
	        listitem4 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl3,listitem4);
	        listitem5 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl4,listitem5);                                                                         
	        listitem6 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl5,listitem6);
	        listitem7 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl6,listitem7);                                                                         
	        listitem8 = xbmcgui.ListItem(''+name)
	        playlist.add(sUrl7,listitem8);
	        player_type = sPlayerType()
	        xbmcPlayer = xbmc.Player (); 
	        xbmcPlayer.play (playlist)  
	        sys.exit()
	        return ok 
def sPlayerType():
       
        
        try:
            if (sPlayerType == '0'):
               
                return xbmc.PLAYER_CORE_AUTO

            if (sPlayerType == '1'):
                
                return xbmc.PLAYER_CORE_MPLAYER

            if (sPlayerType == '2'):
                
                return xbmc.PLAYER_CORE_DVDPLAYER
        except: return False
          
          
              
import datetime 
  
def mconvert(n): 
    return str(datetime.timedelta(seconds = n)) 
          
import time 
  
def convert(n): 
    return str(time.strftime("%H:%M:%S", time.gmtime(n))) 



def videoDetails():
        oGui = cGui()
        oInputParameterHandler = cInputParameterHandler()
        sSearchText = oInputParameterHandler.getValue('sMovieTitle')

        from resources.lib.youtube_api import YouTubeDataAPI
        yt = YouTubeDataAPI(api_key)
            
        data =Search(sSearchText).videos()                   
        logger.info("video_id : %s" % data) 
        for cat in data:
            video_id =cat['video_id']
            #des=videoDetails(video_id)
            #logger.info("video_id-des : %s" % des)
            sPicture=cat['video_thumbnail']
            name=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
            desc=cat['video_description']
            #de=cat['collection_date'] = datetime.datetime.now()
            #channel_id=cat['channel_id']
            desc="[COLOR red] TIME - %s[/COLOR]"+ desc
            sPicture=malfabekodla (sPicture)
            
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', video_id)
            #oOutputParameterHandler.addParameter('siteUrll', channel_id)
            oOutputParameterHandler.addParameter('sMovieTitle', str(sSearchText ))            
            oOutputParameterHandler.addParameter('sThumbnail', sPicture)
            oGui.addMovie(SITE_IDENTIFIER, 'msshowBox2', name, sPicture, sPicture, desc, oOutputParameterHandler)
        oGui.setEndOfDirectory() 
def mvideoDetails():
    
    oGui = cGui()
    exists = ""
    sSearchText = oGui.showKeyBoard()
    if (sSearchText != False):
       sSearchText
       from resources.lib import comon
       list=[]
       list = comon.ReadList(playlistsFile3)
       listUrl = 'https://youtube.otvmedia'
       if exists == "": 
          list.append({"name": sSearchText, "url": listUrl})
          if comon.SaveList(playlistsFile3, list):

            from resources.lib.youtube_api import YouTubeDataAPI
            yt = YouTubeDataAPI(api_key)
            data =Search(sSearchText).videos()  
            #data =yt.search(sSearchText)                   
            logger.info("video_id : %s" % data) 
            for cat in data:
                video_id =cat['video_id']
            #sTitle =cat['Title']
                sPicture=cat['video_thumbnail']
                sTitle=cat['video_title'].replace('#', '').replace('amp;', '').replace('39;', '')
                desc=cat['video_description']
                #channel_id=cat['channel_id']
                logger.info("sTitle : %s" % sTitle) 
                oOutputParameterHandler = cOutputParameterHandler()
               # oOutputParameterHandler.addParameter('siteUrl', channel_id)
                oOutputParameterHandler.addParameter('siteUrll', video_id)
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))            
                oOutputParameterHandler.addParameter('sThumbnail', sPicture)
                oGui.addMovie(SITE_IDENTIFIER, 'Searchchannel3', sTitle, sPicture, sPicture, desc, oOutputParameterHandler)
    oGui.setEndOfDirectory()   


#videoDetails()              
   # oGui.setEndOfDirectory()

def fileru(name,video_id):
             tarzlistesi = []
             tarzlistesi.append((name, video_id))
             for sTitle,sUrl2 in tarzlistesi:
                qualitylist.append(sTitle)
                videolist.append(sUrl2)
                videoid=select(qualitylist,videolist)
                from youtube_api import YouTubeDataAPI
                yt = YouTubeDataAPI(api_key)
                data =yt.get_video_streams(sTitle,'', videoid)
                sUrl =(data[0]['url'])
                sUrl1 =(data[0]['url'])
                sUrl2 =(data[0]['url'])
                sUrl3 =(data[0]['url'])
                sUrl4 =(data[0]['url'])
                sUrl5 =(data[0]['url'])
                sUrl6 =(data[0]['url'])
                sUrl7 =(data[0]['url'])
                playlist=xbmc.PlayList(xbmc.PLAYLIST_VIDEO);
                playlist.clear();
                listitem1 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl,listitem1);
                listitem2 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl1,listitem2);
                listitem3 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl2,listitem3);
                listitem4 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl3,listitem4);
                listitem5 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl4,listitem5);
                listitem6 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl5,listitem6);
                listitem7 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl6,listitem7);
                listitem8 = xbmcgui.ListItem(data[1]['title'])
                playlist.add(sUrl7,listitem8);
                player_type = sPlayerType()
                xbmcPlayer = xbmc.Player ();
                xbmcPlayer.play (playlist)
                sys.exit()
                return ok


def bold(value):
        return ''.join(['[B]', value, '[/B]'])



def getvideostreams(  video_id):
        context=''
        from resources.lib.youtube_api.yardim.video_info import VideoInfo
        video_info = VideoInfo(context, access_token='', language='en-US')
        video_streams = video_info.load_stream_infos(video_id)

        for video_stream in video_streams:
            title = '%s (%s)' % (bold(video_stream['title']), video_stream['container'])

            if 'audio' in video_stream and 'video' in video_stream:
                if video_stream['audio']['bitrate'] > 0 and video_stream['video']['encoding'] and \
                        video_stream['audio']['encoding']:
                    title = '%s (%s; %s / %s@%d)' % (bold(video_stream['title']),
                                                     video_stream['container'],
                                                     video_stream['video']['encoding'],
                                                     video_stream['audio']['encoding'],
                                                     video_stream['audio']['bitrate'])

                elif video_stream['video']['encoding'] and video_stream['audio']['encoding']:
                    title = '%s (%s; %s / %s)' % (bold(video_stream['title']),
                                                  video_stream['container'],
                                                  video_stream['video']['encoding'],
                                                  video_stream['audio']['encoding'])
            elif 'audio' in video_stream and 'video' not in video_stream:
                if video_stream['audio']['encoding'] and video_stream['audio']['bitrate'] > 0:
                    title = '%s (%s; %s@%d)' % (bold(video_stream['title']),
                                                video_stream['container'],
                                                video_stream['audio']['encoding'],
                                                video_stream['audio']['bitrate'])

            elif 'audio' in video_stream or 'video' in video_stream:
                encoding = video_stream.get('audio', dict()).get('encoding')
                if not encoding:
                    encoding = video_stream.get('video', dict()).get('encoding')
                if encoding:
                    title = '%s (%s; %s)' % (bold(video_stream['title']),
                                             video_stream['container'],
                                             encoding)

            video_stream['title'] = title

        return video_streams


def myeniplay():
        from resources.lib.youtube_api.yardim.video_info import VideoInfo
        name = 'sMovieTitle'
        from youtubesearchpython.extras import Video
        #from youtubesearchpython.streamurlfetcher import StreamURLFetcher    
        #fetcher = StreamURLFetcher()                   
        video = Video.get("https://www.youtube.com/watch?v=Zv11L-ZfrSg" )
        logger.info("videom : %s" % video )
       # url = fetcher.get(video, 22)
        video_id='Zv11L-ZfrSg'
        context=''
        video_info = VideoInfo(context, access_token='', language='en-US')
        #url= video_info.load_stream_infos(video_id)   
        url= video_info.load_stream_infos(video_id)
        logger.info("18url: %s" % url)
        itag='271' 
        v_id='Zv11L-ZfrSg'   
        url= getvideostreams(v_id)
        logger.info("18url: %s" % url)
        #url =yvideos(v_id,itag)
       # nextplay('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url)
       #get_video_streams(  video_id)




def veyeniplay(name,url):
        v_id = url.replace('https://www.youtube.com/watch?v=', '')
        v_id = url.replace('https://www.youtube.com/embed/', '')
        v_id = v_id.replace('?', '')
#        v_id = re.search('https://www.youtube.com/embed/(.+?)?', url).group(1)
        logger.info("v_id: %s" % v_id)
        from youtubesearchpython.extras import Video
        video = Video.get("https://www.youtube.com/watch?v=%s"%v_id )
        #from youtubesearchpython.streamurlfetcher import StreamURLFetcher    
        #fetcher = StreamURLFetcher()                   
        video = Video.get("https://www.youtube.com/watch?v=%s"%v_id )
        logger.info("22url: %s" % url)
        url = fetcher.get(video, 22)
        logger.info("22url: %s" % url)
        if url == None:
           url = fetcher.get(video, 18)
          
           logger.info("18url: %s" % url)
#        logger.info("data : %s" % data)   
        
        nextplay('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url)

                
def vyeniplay():
        oInputParameterHandler = cInputParameterHandler()
        name = oInputParameterHandler.getValue('sMovieTitle')
        v_id = oInputParameterHandler.getValue('siteUrl')
                               
        logger.info("sUrl : %s" % url)
        s = requests.Session()
        cookie_string = "; ".join([str(x) + "=" + str(y) for x, y in s.cookies.items()])
        token = 'https://redirectdetective.com/ld.px'
        post_data = {'w':v_id,'f':'false'}
        r = s.post(token, headers={'Cookie': '__utma=132634637.1201225376.1617003196.1617003196.1617003196.1; __utmc=132634637; __utmz=132634637.1617003196.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=132634637.3.10.1617003196',
             'Referer': 'https://redirectdetective.com/',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
             'Origin': 'https://redirectdetective.com',
             #'Connection': 'Keep-Alive',
             'Accept-Encoding': 'gzip'}, data=post_data, timeout=10)
        urll = r.text#.replace("\\", '')
        logger.info("sUrl : %s" % urll)
        url = re.search('.+?title="(.+?)">https://.+?....</a></button>', urll).group(1)
        
        addLink('[COLOR lightblue][B]OTV MEDIA YOUTUBE Player>>  [/B][/COLOR]'+name,url,'')


 