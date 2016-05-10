# used for extracting ids

import datetime
from bs4 import BeautifulSoup


def Spot(_inputString, _inputString2, _idUrl):
    d1 = datetime.datetime.now()
    d3 = d1 - datetime.timedelta(days=1)
    curTime = (d3.strftime('%Y/%m/%d'))
    # curTime = '2016/5/6'  # temp
    # format the time
    curTime = curTime.replace("/0", "/")

    idList_Date1 = []
    idList_Date2=[]
    #Page 1
    Soup1 = BeautifulSoup(_inputString, "lxml")
    for j in Soup1.find_all('span', text=curTime):
        idList_Date1.append(j.get('id')[:-15])
    #Page 2
    if(_inputString2 is not None):
        Soup2 = BeautifulSoup(_inputString2, "lxml")
        for j in Soup2.find_all('span', text=curTime):
            idList_Date2.append(j.get('id')[:-15])

    hrefList_graduate = []
    hrefList_trainee = []
    for i in idList_Date1:
        tConditionID = i + '_lblVerifyStatus'
        # Fucking ResultSet!!!
        if(Soup1.find_all(id=tConditionID)[0].string == "已审核"):
            tHrefID = i + "_hplTitle"
            tempHref = Soup1.find_all(id=tHrefID)[0].get('href')
            tempI = _idUrl + "/Management_Demand/JOL_Require/Admin/" + tempHref
            tWorkTypeID = i + "_lblWorkType"
            if(Soup1.find(id=tWorkTypeID).string == "应届生"):
                hrefList_graduate.append(tempI)
            else:
                hrefList_trainee.append(tempI)

    for i in idList_Date2:
        tConditionID = i + '_lblVerifyStatus'
        # Fucking ResultSet!!!
        if(Soup2.find_all(id=tConditionID)[0].string == "已审核"):
            tHrefID = i + "_hplTitle"
            tempHref = Soup2.find_all(id=tHrefID)[0].get('href')
            tempI = _idUrl + "/Management_Demand/JOL_Require/Admin/" + tempHref
            tWorkTypeID = i + "_lblWorkType"
            if(Soup2.find(id=tWorkTypeID).string == "应届生"):
                hrefList_graduate.append(tempI)
            else:
                hrefList_trainee.append(tempI)       



    return [hrefList_graduate, hrefList_trainee]
