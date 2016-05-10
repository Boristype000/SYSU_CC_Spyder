# ÊµÏÖµÇÂ½
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time


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

    elem_need = driver.find_element_by_id("ctl00_leftfuncbar_TreeView1t15")
    elem_need.click()

    source_code_2 = None

    if(driver.find_element_by_link_text("2")):
        elem_next_page = driver.find_element_by_link_text("2")
        elem_next_page.click()
        time.sleep(5)
        source_code_2 = driver.page_source
        #driver.find_element_by_xpath("//*")
    driver.close()
    driver.quit()
    return [source_code, source_code_2, idUrl]
