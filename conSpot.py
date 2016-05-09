# used for extracting ids
import datetime
from bs4 import BeautifulSoup


def Spot(_inputString, _idUrl):
    testSoup = BeautifulSoup(_inputString, "lxml")

    d1 = datetime.datetime.now()
    d3 = d1 - datetime.timedelta(days=1)
    curTime = (d3.strftime('%Y/%m/%d'))
    curTime = '2016/5/6'  # temp
    # format the time
    curTime = curTime.replace("/0", "/")

    idList_Date = []
    for j in testSoup.find_all('span', text=curTime):
        idList_Date.append(j.get('id')[:-15])

    hrefList_graduate = []
    hrefList_trainee = []
    for i in idList_Date:
        tConditionID = i + '_lblVerifyStatus'
        # Fucking ResultSet!!!
        if(testSoup.find_all(id=tConditionID)[0].string == "已审核"):
            tHrefID = i + "_hplTitle"
            tempHref = testSoup.find_all(id=tHrefID)[0].get('href')
            tempI = _idUrl + "/Management_Demand/JOL_Require/Admin/" + tempHref
            tWorkTypeID = i + "_lblWorkType"
            if(testSoup.find(id=tWorkTypeID).string == "应届生"):
                hrefList_graduate.append(tempI)
            else:
                hrefList_trainee.append(tempI)

    return [hrefList_graduate, hrefList_trainee]
