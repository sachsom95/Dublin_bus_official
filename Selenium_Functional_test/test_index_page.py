#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# this page is designed to test whether this website is able to get access to and test headings
# it tests all link button in index page, journey planner is put in another file
from selenium import webdriver
import time
import unittest


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
# https://group8dublinbus.xyz/
driver.get('https://group8dublinbus.xyz/') # this is used to test server file
# driver.get('http://127.0.0.1:8000') # this is used to test local file
time.sleep(3)
driver.refresh() # add this wait because i may need to skip the splash page -- the test is on traceless mode of web browser
print("if we can get the info of this page, it means this link works")
print(driver.title)
print(driver.current_url)
time.sleep(2)
print()

print("======test covid-19 info=====================================")
covid_board_test = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[2]/a')
covid_board_test.click()
time.sleep(1) # hold on a second wait for this page to load
result_covid = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[2]/div/section[1]/div/div/div[1]/div/span[2]').text
print("if i can get info from this board, it means this function works well")
print(result_covid)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/button').click()
time.sleep(2)
print()

print("======test login page========================================")
login = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[3]/a')
login.click() # enter this page
print("if this url contains /login/, it means it works")
print(driver.current_url)
time.sleep(1.5)
print("now back to home page")
driver.back()
time.sleep(1)
print()

print("======test sign up page=====================================")
signup = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a')
signup.click() # enter this page
print("if this url contains /register/, it means it works")
print(driver.current_url)
time.sleep(1.5)
print("now back to home page")
driver.back()
time.sleep(1)
print()

print("======test journey planer page=====================================")
journeyplanner = driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]/a')
journeyplanner.click() # enter this page
print("if this url contains weather information and other info, it means it works")
print(driver.find_element_by_xpath('//*[@id="floating-panel"]/div[1]').text)
time.sleep(1)
print()

print("======test Tourism page=====================================")
tourism = driver.find_element_by_xpath('/html/body/div[2]/ul/li[2]/a')
tourism.click() # enter this page
print("if this url contains information in this page, it means it works")
print(driver.find_element_by_xpath('//*[@id="tourism-card"]/h2').text)
time.sleep(1)
print()

print("======test twitter page=====================================")
tourism = driver.find_element_by_xpath('/html/body/div[2]/ul/li[3]/a')
tourism.click() # enter this page
print("if contains information in today's twitter, it means it works")
driver.switch_to.frame('twitter-widget-0') # here we need to switch to another frame because twitter page is in another page, just like google map
tweets_elements = driver.find_elements_by_class_name('timeline-Tweet-text')
for t in tweets_elements:
    print(t)
    break # we only need to print one of these info




# quit in 5 seconds
time.sleep(5)
driver.quit()