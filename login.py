# 实现登陆
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


def login():
    driver = webdriver.Firefox()
    driver.get(
        "http://career.sysu.edu.cn/(S(hzw2csqmesicol22ryare345))/default.aspx")
    #
    elem_user = driver.find_element_by_name(
        "ctl00$ContentPlaceHolder1$txtLoginId")
    elem_user.send_keys("southAdmin")
    elem_pwd = driver.find_element_by_name(
        "ctl00$ContentPlaceHolder1$txtPassword")
    elem_pwd.send_keys("jyzxsouth")
    elem_domain = driver.find_element_by_id(
        "ctl00_ContentPlaceHolder1_radioAdmin")
    elem_domain.click()
    elem_pwd.send_keys(Keys.RETURN)

    return driver


def loginGet():

    driver = login()

    idUrl = driver.current_url[0:55]

    source_code = requests.get(
        idUrl + "/Management_Demand/JOL_Require/Admin/RequireManage.aspx").text

    driver.close()
    driver.quit()
    return [source_code, idUrl]
