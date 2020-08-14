#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# this page is designed to test functions in journey planners
from selenium import webdriver
import time
import unittest
import clipboard
from selenium.webdriver.common.keys import Keys

print("=====Web access and journey planner test=====================================")
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
# https://group8dublinbus.xyz/
driver.get('https://group8dublinbus.xyz/') # this is used to test server file
# driver.get('http://127.0.0.1:8000') # this is used to test local file
time.sleep(3)
driver.refresh() # add this wait because i may need to skip the splash page -- the test is on traceless mode of web browser
print("if we can get the info of this page, it means this link works")
print(driver.title)
print(driver.current_url)
journeyplanner = driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]/a')
journeyplanner.click()
print("if this url contains weather information and other info, it means it works")
print(driver.find_element_by_xpath('//*[@id="floating-panel"]/div[1]').text)
time.sleep(1)
print()



print("=====test enter 2 location and time, then submit choice, and see if it works=================")

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

####### check results
print("if this function works, the prediction time for the journey will be shown below")
print(driver.find_element_by_xpath('//*[@id="precitionResult"]').text)
print()


print("===the test below need above things works====")
print("==========test share link====================")
driver.find_element_by_xpath('//*[@id="share_trip"]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sharable_link"]/div/div/div[3]/button[2]').click()
clipboard_text = clipboard.paste()
print("if share link works, below shared link will be shown")
print(clipboard_text)






# quit in 5 seconds
time.sleep(5)
driver.quit()



