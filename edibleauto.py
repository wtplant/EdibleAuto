# -*- coding: utf-8 -*-

#autopost edible dialect

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from EdibleAutoSet import eal
# from secrets import pw

class InstaBot:

    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.edibledialect.com/wp-login.php?loggedout=true")
        sleep(3)

        # Fills login fields
        self.driver.find_element_by_xpath('/html/body/div[1]/form/p[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/form/div/p[1]/input').send_keys(pw)
        sleep(2)

        # Clicks to login
        self.driver.find_element_by_xpath('/html/body/div[1]/form/p[3]/input').click()
        sleep(3)

        self.driver.get('http://www.edibledialect.com/wp-admin/post-new.php')
        # move to post dashboard
        # self.driver.get('http://www.edibledialect.com/wp-admin/edit.php')
        # sleep(3)
