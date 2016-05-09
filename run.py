import conSpot
import backGet
import login
import toWord
import __main__

[pageString, idUrl] = login.loginGet()
#get WebSite's Id
[hrefList_g, hrefList_t] = conSpot.Spot(pageString, idUrl)

[conList_g, conList_t] = backGet.GoBackAndGet(hrefList_g, hrefList_t)

toWord.toWord(conList_g, conList_t)