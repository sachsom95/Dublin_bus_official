"""
Author : Sachin Soman
Last Modified:19 June '20

Description:
This script is to extract data from "https://data.gov.ie/dataset/real-time-passenger-information-rtpi-for-dublin-bus-bus-eireann-luas-and-irish-rail"
to make a csv file with StopID | bus stop name | latitude | longtitude | all buses in the route. This module has a main method and can run on its own to make the output in present working directory
"""

import requests	
import json
import csv


def getRequest(link):
	"""Function to get request object and returns a json . parameter will be API link"""
	try:
		data = requests.get(link)
	except requests.exceptions.RequestException as err:
		print("Error has occured\n",err)

	try:
		json_result = data.json()
	except requests.exceptions.RequestException as err:
		print("value error happened\n",err)
	return json_result




def extractData(json_obj,file_name):
	"""this function will take a reqest object convert to json and extract information such as STOIPID, LAT, LON , STATION NAME, BUSES IN ROUTE  after this writes to a csv file with header info provided"""

	with open(file_name, 'w', newline='') as csvfile:
		fieldnames = ['stopid','shortname','fullname','latitude','longitude','buses']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

		for x in range(len(json_obj["results"])):
			data = json_obj["results"][x]

			stopid = data['stopid']
			if(stopid.isnumeric() and data["operators"][0]["name"] == 'bac'):
				shortname = data['shortname']
				fullname = data['fullname']
				latitude = data['latitude']
				longitude = data['longitude']
				buses = ""
				for i in range(len(data["operators"][0]["routes"])):
					bus_data = data["operators"][0]["routes"]
					buses += (bus_data[i]+',')
				else:
					# Removes the last coma after execution of for loop
					buses = buses[:-1]
			else:
				continue

			try:
				writer.writerow({'stopid': stopid , 'shortname': shortname, 'fullname':fullname, 'latitude':latitude,'longitude':longitude,'buses':buses})
			except csv.Error as err:
				print("Error occured at writer part\n", err)


if __name__ == "__main__":
	
	api_link = "https://data.smartdublin.ie/cgi-bin/rtpi/busstopinformation?stopid&format=json"

	# header_used = ['stopid','shortname','fullname','latitude','longitude','operators']

	data = getRequest(api_link)
	extractData(data,"result.csv")
