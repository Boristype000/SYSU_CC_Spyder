import conSpot
import backGet
import login
import toWord
import __main__

[pageString, pageString2, idUrl] = login.loginGet()

[hrefList_g, hrefList_t] = conSpot.Spot(pageString, pageString2, idUrl)

[conList_g, conList_t] = backGet.GoBackAndGet(hrefList_g, hrefList_t)

toWord.toWord(conList_g, conList_t)
