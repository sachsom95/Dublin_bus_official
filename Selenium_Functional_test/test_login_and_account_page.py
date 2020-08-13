#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

from selenium.webdriver.common.keys import Keys

print("Web access test=====================================")
########### initial web access test
# get driver get web page
###### my chrome version is 84.0.4147.30, if you need other version, download drive and put in this folder
###### if you leave it empty, you need to put them in the right place in your computer
###### here i only test chrome
# driver = webdriver.Firefox('./geckodriver') # firefox browser
# driver = webdriver.Ie() # IE browser
# driver = webdriver.Edge() # Edge browser
# driver = webdriver.Opera('./operadriver') # Opera browser
# driver = webdriver.Safari() # Safari browser, the file is in /usr/bin/safaridriver
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(1)
# https://group8dublinbus.xyz/login/
driver.get('http://127.0.0.1:8000/login/') # this is used to test local file
time.sleep(3)
driver.refresh() # add this wait because i may need to skip the splash page -- the test is on traceless mode of web browser
print("if we can get the info of this page, it means this link works")
print(driver.title)
print(driver.current_url)
time.sleep(2)
print()

print("=================test login function==================")
print("==Before login==")
# print title of this page
print(driver.title)
# print current URL
print(driver.current_url)
# perform login
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("sachinsoman")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123")
driver.find_element_by_xpath('//*[@id="col1"]/div/div/form/div[1]/button').click()
time.sleep(2)

print("==After login==")
# if works, index page will change
print("if this works, current index page should have 'Account' link")
print(driver.current_url)
print(driver.find_element_by_link_text('Account').text)
time.sleep(2)


print("=================test save favourite location==================")
######## pass elements to From:
driver.find_element_by_id('searchTextField_start').clear()
input_from_location = driver.find_element_by_id('searchTextField_start')
input_from_location.send_keys("UCD Computer Science and Informatics Centre, Belfield, Dublin, Ireland")
time.sleep(1)
input_from_location.send_keys(Keys.DOWN)
input_from_location.send_keys(Keys.RETURN)
time.sleep(1)
######## pass elements to TO:
driver.find_element_by_id('searchTextField_destination').clear()
input_to_location = driver.find_element_by_id('searchTextField_destination')
input_to_location.send_keys("Guinness Enterprise Centre, Taylor's Lane, Saint Catherine's, Dublin 8, Ireland")
time.sleep(1)
input_to_location.send_keys(Keys.DOWN)
input_to_location.send_keys(Keys.RETURN)
time.sleep(1)
######## select departure time
default_time = driver.find_element_by_id("datetimepicker4").get_attribute("value")
# explain of below operation:
# it is hard to choose time for today because testing time could be tomorrow, so i set time to today and later, suppose we don't do tests late than 9:00 PM
changed_time = default_time[0:8] + " 9:00 PM"
#print(changed_time)
driver.find_element_by_id('datetimepicker4').clear()
travel_time = driver.find_element_by_id('datetimepicker4')
travel_time.send_keys(changed_time)
time.sleep(1)
####### press submit
driver.find_element_by_id('submit-btn').click()
time.sleep(2)
####### press submit
driver.find_element_by_id('favDestBtn').click()
time.sleep(0.5)
###### favourite location
driver.switch_to.alert.send_keys("Guinness Enterprise") # save favourite location as Guinness Enterprise
time.sleep(0.3)
driver.switch_to.alert.accept()
time.sleep(10) ## you can see if you have added this location
driver.refresh()
time.sleep(1)
###### test take me to function
sel = driver.find_element_by_id("favDestSelect")
Select(sel).select_by_visible_text("Guinness Enterprise")
driver.find_element_by_xpath('//*[@id="floating-panel"]/span/button').click()
time.sleep(8)
print("here i wait 8 seconds, you can check if this function works")



print()
print()
print("=================test Account page==================")
# if above works, we click account and enter account page
driver.find_element_by_link_text('Account').click()
time.sleep(2)
info_username = driver.find_element_by_class_name('account-heading').text
info_leapcard_balancee = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/p').text
# info_favourite_location = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/p').text
print("if below info show, it means this page works")
print("we get your username is "+info_username)
print("Your "+info_leapcard_balancee)
# print("Your "+info_favourite_location)
time.sleep(3)

print("=================test log out==================")
driver.find_element_by_xpath('//*[@id="menu"]/ul/li[3]/a').click()
print("if this works, current page have log out info")
print(driver.current_url)
print(driver.find_element_by_xpath('/html/body/div[2]/h1').text)

print()
# go back to main page
driver.find_element_by_xpath('//*[@id="menu"]/ul/li[1]/a').click()
print("now index page should have Login In button")
print(driver.find_element_by_xpath('//*[@id="menu"]/ul/li[3]/a').text)


# quit in 5 seconds
time.sleep(5)
driver.quit()
