from bs4 import BeautifulSoup
import requests


def GoBackAndGet(_hrefList_g, _hrefList_t):

    contentList_g = []
    contentList_t = []

    for i in _hrefList_t:
        tDict = {'Company': '', 'Schooling': '', 'Major': '',
                 'District': '', 'Method': '', 'Deadline': '', 'RequireJob': ''}
        tHtml = requests.get(i).text
        tSoup = BeautifulSoup(tHtml, "lxml")
        tDict['Company'] = tSoup.find(
            id="ctl00_ContentPlaceHolder1_lblRequireCompany").string
        tDict['RequireJob'] = tSoup.find(
            id="ctl00_ContentPlaceHolder1_lblRequireJob").string
        tDict['Schooling'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireStudyLevel').string
        tDict['Major'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireProfession').string
        tDict['District'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireWorkArea').string
        tDict['Method'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblGetJobType').string
        tDict['Deadline'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblEndTime').string
        contentList_t.append(tDict)

    for i in _hrefList_g:
        tDict = {'Company': '', 'Schooling': '', 'Major': '',
                 'District': '', 'Method': '', 'Deadline': '', 'RequireJob': ''}
        tHtml = requests.get(i).text
        tSoup = BeautifulSoup(tHtml, "lxml")
        tDict['Company'] = tSoup.find(
            id="ctl00_ContentPlaceHolder1_lblRequireCompany").string
        tDict['Schooling'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireStudyLevel').string
        tDict['RequireJob'] = tSoup.find(
            id="ctl00_ContentPlaceHolder1_lblRequireJob").string
        tDict['Major'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireProfession').string
        tDict['District'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblRequireWorkArea').string
        tDict['Method'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblGetJobType').string
        tDict['Deadline'] = tSoup.find(
            id='ctl00_ContentPlaceHolder1_lblEndTime').string
        contentList_g.append(tDict)

    return [contentList_g, contentList_t]
