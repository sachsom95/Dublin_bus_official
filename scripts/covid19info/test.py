#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import re
import json

# open up connection and grab the page
covid_url = 'https://www.rte.ie/news/coronavirus/summary/'
uClient = uReq(covid_url)
page_html = uClient.read()
uClient.close()

# html parasing
page_soup = BeautifulSoup(page_html, 'html.parser').body

# js = page_soup.body.findAll('script')
# print(js)
# pattern = re.compile(r"(\[.*\])", re.MULTILINE | re.DOTALL)
# daily_feed = page_soup.body.find("script",text=pattern)
# print(daily_feed)

# grab info
# pattern = re.compile(r"(\[.*\])", re.MULTILINE | re.DOTALL)
record_raw = page_soup.findAll('script')[4].get_text()
# print(record_raw)
# # record = record_raw.find('script',text=pattern)

record = re.findall(r"\[(.+?)\]", record_raw)
print(record)
# json_record = json.loads(json.dumps(record_raw))
# print(json_record)
