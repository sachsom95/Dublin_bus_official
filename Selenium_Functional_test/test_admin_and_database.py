#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import unittest

# admin page is used to store all database related stuff
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
# https://group8dublinbus.xyz/admin/
driver.get('http://127.0.0.1:8000/admin/') # this is used to test local file
time.sleep(1)
driver.refresh() # add this wait because i may need to skip the splash page -- the test is on traceless mode of web browser
print("if we can get the info of this page, it means this link works")
print(driver.title)
print(driver.current_url)
time.sleep(1)
print()

print("===========test admin log in=====================================")
print("==Before login==")
print(driver.title)
print(driver.current_url)
# perform login
driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input').clear()
driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div/input').send_keys("sachinsoman")
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input').clear()
driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div/input').send_keys("123")
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/button').click()
time.sleep(1)

print("==After login==")
# if works, index page will change
print("if this works, it will get heading info")
print(driver.current_url)
print(driver.find_element_by_xpath('//*[@id="main"]/section/aside/div/div/div[2]/span').text)
time.sleep(2)


print("==================test all tables=====================================")
print(driver.current_url)
print()
# User table
print("****if you can see records of each table, it means it works:  ****")
print("=====first record of table Users:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[2]/a').click()
time.sleep(1) # load table
# move to frame
driver.switch_to.frame(0)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page
print()

# Covids table
print("=====first record of table Covids:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[3]/a').click()
time.sleep(0.5) # load table
# move to frame
driver.switch_to.frame(1)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page
print()

# Currentweather table
print("=====first record of table Currentweather:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[4]/a').click()
time.sleep(0.5) # load table
# move to frame
driver.switch_to.frame(2)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page
time.sleep(1)
print()

# Forecastweather table
print("=====first record of table Forecastweather:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[5]/a').click()
time.sleep(0.5) # load table
# move to frame
driver.switch_to.frame(3)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page
time.sleep(1)
print()

# Favourite destination table
print("=====first record of table Favourite destination:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[6]/a').click()
time.sleep(0.5) # load table
# move to frame
driver.switch_to.frame(4)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page
time.sleep(1)
print()

# Profiles table
print("=====first record of table Profiles:")
driver.find_element_by_xpath('//*[@id="home"]/div[1]/div/div/div[2]/div/div[7]/a').click()
time.sleep(0.5) # load table
# move to frame
driver.switch_to.frame(5)
print(driver.find_element_by_class_name('row1').text)
# move out of frame
driver.switch_to.default_content()
driver.find_element_by_xpath('//*[@id="main"]/section/aside/ul/div[1]/li').click() # go back to admin home page




# quit in 5 seconds
time.sleep(5)
driver.quit()