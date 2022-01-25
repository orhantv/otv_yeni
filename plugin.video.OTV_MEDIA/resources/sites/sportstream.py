# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# Arias800
import re
import time

from resources.sites.LIVETV2 import *
from resources.lib.packer import cPacker
from resources.lib.comaddon import addon, isMatrix
from resources.lib.gui.gui import cGui
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import Quote

from datetime import datetime, timedelta

SITE_IDENTIFIER = 'sportstream'
SITE_NAME = 'Channel Stream'
SITE_DESC = 'Chaines TV en directs'

URL_MAIN = "https://channelstream.es"
SPORT_SPORTS = (True, 'load')
SPORT_LIVE = 'https://channelstream.es/programme.php'

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'


def load():
    oGui = cGui()

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SPORT_LIVE[0])
    oGui.addDir(SITE_IDENTIFIER, SPORT_LIVE[1], 'Sports (En direct)', 'sportstream.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies():
    oGui = cGui()
    oParser = cParser()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = SPORT_LIVE+ oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    if isMatrix():
        sHtmlContent = sHtmlContent.replace('Ã®', 'î').replace('Ã©', 'é')

    # récupérer les drapeaux pour en faire des thumb
    sPattern = "\.flag\.([^{]+){.+?url\(([^)]+)\)"
    aResult = oParser.parse(sHtmlContent, sPattern)
    flags = dict(aResult[1])

    sPattern = "colspan=\"7\".+?<b>([^<]+)<\/b>.+?location\.href = '([^']+).+?text-align.+?>(.+?)<\/td>.+?<span class=\"flag ([^\"]+).+?text-align.+?>([^<]+).+?text-align: left.+?>([^<]+).+?<span class=\"t\">([^<]+)<\/span>"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sUrl2 = aEntry[1]
            sDate = aEntry[2].replace('<br />', ' ')
            flag =  aEntry[3]
            sdesc1 = aEntry[4]
            sdesc2 = aEntry[5]
            sTime = aEntry[6]

            sThumb = flags.get(flag)
            sTitle = ''
            if sDate:
                try:
                    sDate +=  ' ' + sTime
                    d = datetime(*(time.strptime(sDate, '%Y-%m-%d %H:%M')[0:6]))
                    d +=  timedelta(hours=6)
                    sDate = d.strftime("%d/%m/%y %H:%M")
                except Exception as e:
                    pass
                sTitle += sDate +' '
            sTitle += ' - '

            if sdesc1:
                sTitle += sdesc1 + ' - ' + sdesc2 + ' - '
            sTitle += '(' + aEntry[0] + ')'
            sDisplayTitle = sTitle
            sDesc = sDisplayTitle

            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addMisc(SITE_IDENTIFIER, 'showHoster', sTitle, sThumb, sThumb, sDisplayTitle, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showHoster():
    oGui = cGui()
    oParser = cParser()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = URL_MAIN + oInputParameterHandler.getValue('siteUrl')
    sTitle = oInputParameterHandler.getValue('sMovieTitle')
    sDesc = oInputParameterHandler.getValue('sDesc')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sCat = 6
    sMeta = 0

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    # Double Iframe a passer.
    sPattern = "document\.getElementById\('video'\)\.src='([^']+)'.+?>([^<]+)<"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if not aResult[1]:  # Pas de flux
        oGui.setEndOfDirectory()
        return

    for entry in aResult[1]:
        oOutputParameterHandler = cOutputParameterHandler()
        iframeURL1 = entry[0]
        canal = entry[1]
        sMovieTitle = sTitle
        if canal not in sMovieTitle:
            sMovieTitle += ' [' + canal + ']'
            
        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
        oOutputParameterHandler.addParameter('sThumbnail', sThumb)
        oOutputParameterHandler.addParameter('sDesc', sDesc)

        oGuiElement = cGuiElement()
        oGuiElement.setTitle(sMovieTitle)
        oGuiElement.setDescription(sDesc)
        oGuiElement.setFileName(sMovieTitle)
        oGuiElement.setSiteName(SITE_IDENTIFIER)
        oGuiElement.setFunction('play__')
        oGuiElement.setIcon('tv.png')
        oGuiElement.setMeta(sMeta)
        oGuiElement.setThumbnail(sThumb)
        #oGuiElement.setDirectTvFanart()
        oGuiElement.setCat(sCat)
        oGuiElement.setMeta(sMeta)

        if 'dailymotion' in iframeURL1:
            oOutputParameterHandler.addParameter('sHosterIdentifier', 'dailymotion')
            oOutputParameterHandler.addParameter('sMediaUrl', iframeURL1)
            oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
            oOutputParameterHandler.addParameter('sFileName', sMovieTitle)
            oGuiElement.setFunction('play')
            oGuiElement.setSiteName('cHosterGui')
            oGui.addHost(oGuiElement, oOutputParameterHandler)
            cGui.CONTENT = 'movies'
            oGui.setEndOfDirectory()
            return

        oRequestHandler = cRequestHandler(iframeURL1)
        oRequestHandler.addHeaderEntry('User-Agent', UA)
        # oRequestHandler.addHeaderEntry('Referer', siterefer) # a verifier
        sHtmlContent = oRequestHandler.request()

        sHosterUrl = ''
        oParser = cParser()
        sPattern = '<iframe.+?src="([^"]+)'
        aResult2 = oParser.parse(sHtmlContent, sPattern)
        try:
            # Lien telerium qui ne marche pas, mais qui n'est pas toujours present
            iframeURL1 = aResult2[1][1]
        except:
            iframeURL1 = aResult2[1][0]

        oRequestHandler = cRequestHandler(iframeURL1)
        oRequestHandler.addHeaderEntry('User-Agent', UA)
        sHtmlContent = oRequestHandler.request()
    
        oParser = cParser()
        sPattern = '<iframe.+?src="([^"]+)'
        aResult2 = oParser.parse(sHtmlContent, sPattern)
    
        if aResult2[1]:
            urlHoster = aResult2[1][0]
            if 'primetubsub' in urlHoster:
                sHosterUrl = getHosterPrimetubsub(urlHoster, iframeURL1)
            else:
                sHosterUrl = getHosterWigistream(urlHoster, iframeURL1)
            if sHosterUrl:
                oOutputParameterHandler.addParameter('siteUrl', sHosterUrl)
                oGui.addFolder(oGuiElement, oOutputParameterHandler)
            
    cGui.CONTENT = 'files'
    oGui.setEndOfDirectory()


def getHosterWigistream(url, referer):
    url = url.strip()
    if not url.startswith('http'):
        url = 'http:'+url
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()

    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
    aResult = re.findall(sPattern, sHtmlContent)

    if aResult:
        sstr = aResult[0]
        if not sstr.endswith(';'):
            sstr = sstr + ';'
        sUnpack = cPacker().unpack(sstr)
        sPattern = 'src="(.+?)"'
        aResult = re.findall(sPattern, sUnpack)
        if aResult:
            return aResult[0] + '|User-Agent=' + UA + '&Referer=' + Quote(url)

    return False

def getHosterPrimetubsub(url, referer):
    oParser = cParser()
    
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()
    sPattern = '<iframe.+?src="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if not aResult[0]:
        return

    referer = url
    url = aResult[1][0]
    
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()
    sPattern = "(src|[^/]source):'([^']+)"
    aResult = oParser.parse(sHtmlContent, sPattern)

    if not aResult[0]:
        return
    
    referer = url
    url = aResult[1][0][1]
    
    return url + '|User-Agent=' + UA + '&Referer=' + Quote(referer)

def play__():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    url = oInputParameterHandler.getValue('siteUrl')
    title = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
        
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(SITE_IDENTIFIER)
    oGuiElement.setTitle(title)
    oGuiElement.setMediaUrl(url)
        

    oPlayer = cPlayer()
    oPlayer.clearPlayList()
    oPlayer.addItemToPlaylist(oGuiElement)
    oPlayer.startPlayer()  
  