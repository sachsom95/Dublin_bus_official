#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import json
import requests
import logging
import mysql.connector
from mysql.connector import Error
from time import sleep

logging.basicConfig(filename='virus_database_connect_error_log.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

while True:
    # make connection
    def establishConnection():
        """This function connects to the mysql database on the VM
        NB user must enter their own password details below"""
        while True:
            try:
                global connection
                connection = mysql.connector.connect(host='localhost',
                                                    database='bus_data',
                                                    user='admin',
                                                    password='Group8sql',)
                if connection.is_connected():
                    #print("This connection worked!")
                    global cursor
                    cursor = connection.cursor(buffered=True)  # create cursor object - this can execute sql statments

                    return cursor
                    break

                else:
                    print("Connection not established")
                    logging.info('Connection not established')

            except Error as error:
                print("ERRROR!!: ", error)
                logging.error('error at ' + str(error))
                print("will try to connect again in 25 seconds")
                sleep(25)

    sleep(60)
    # get data of covid 19
    url = "https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/CovidStatisticsProfileHPSCIrelandOpenData/FeatureServer/0/query?where=1%3D1&outFields=Date,RequiringICUCovidCases,CommunityTransmission,TotalConfirmedCovidCases,TotalCovidDeaths,ConfirmedCovidCases,ConfirmedCovidDeaths,CloseContact,StatisticsProfileDate,FID,TravelAbroad,HospitalisedCovidCases&outSR=4326&f=json"
    lm_json = requests.get(url).json()
    featurelist = lm_json['features']
    # print(featurelist[-1])

    # write data into the database
    establishConnection()
    query = "SELECT COUNT(*) from bus_data.covid"
    cursor.execute(query)
    result = cursor.fetchone()
    rows = result[0]  # total rows
    #    print("number of rows:", rows)
    if rows == 0:
        cursor.execute('truncate table bus_data.covid')
        for i in featurelist:
            attribute = i["attributes"]
            Date = attribute["Date"]
            RequiringICUCovidCases = attribute["RequiringICUCovidCases"]
            CommunityTransmission = attribute["CommunityTransmission"]
            TotalConfirmedCovidCases = attribute["TotalConfirmedCovidCases"]
            TotalCovidDeaths = attribute["TotalCovidDeaths"]
            ConfirmedCovidCases = attribute["ConfirmedCovidCases"]
            ConfirmedCovidDeaths = attribute["ConfirmedCovidDeaths"]
            CloseContact = attribute["CloseContact"]
            StatisticsProfileDate = attribute["StatisticsProfileDate"]
            FID = attribute["FID"]
            TravelAbroad = attribute["TravelAbroad"]
            HospitalisedCovidCases = attribute["HospitalisedCovidCases"]

            cursor.execute('insert into bus_data.covid(Date, RequiringICUCovidCases, CommunityTransmission, TotalConfirmedCovidCases, TotalCovidDeaths, ConfirmedCovidCases, ConfirmedCovidDeaths, CloseContact, StatisticsProfileDate, FID, TravelAbroad, HospitalisedCovidCases)' \
                'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (Date, RequiringICUCovidCases, CommunityTransmission, TotalConfirmedCovidCases, TotalCovidDeaths, ConfirmedCovidCases, ConfirmedCovidDeaths, CloseContact, StatisticsProfileDate, FID, TravelAbroad, HospitalisedCovidCases))
        connection.commit()
        cursor.close()
        connection.close()
        # run once a day
        sleep(86400)

    else:
        attribute = featurelist[-1]["attributes"]
        Date = attribute["Date"]
        RequiringICUCovidCases = attribute["RequiringICUCovidCases"]
        CommunityTransmission = attribute["CommunityTransmission"]
        TotalConfirmedCovidCases = attribute["TotalConfirmedCovidCases"]
        TotalCovidDeaths = attribute["TotalCovidDeaths"]
        ConfirmedCovidCases = attribute["ConfirmedCovidCases"]
        ConfirmedCovidDeaths = attribute["ConfirmedCovidDeaths"]
        CloseContact = attribute["CloseContact"]
        StatisticsProfileDate = attribute["StatisticsProfileDate"]
        FID = attribute["FID"]
        TravelAbroad = attribute["TravelAbroad"]
        HospitalisedCovidCases = attribute["HospitalisedCovidCases"]

        cursor.execute(
            'insert into bus_data.covid(Date, RequiringICUCovidCases, CommunityTransmission, TotalConfirmedCovidCases, TotalCovidDeaths, ConfirmedCovidCases, ConfirmedCovidDeaths, CloseContact, StatisticsProfileDate, FID, TravelAbroad, HospitalisedCovidCases)' \
            'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (Date, RequiringICUCovidCases, CommunityTransmission, TotalConfirmedCovidCases, TotalCovidDeaths, ConfirmedCovidCases, ConfirmedCovidDeaths, CloseContact, StatisticsProfileDate, FID, TravelAbroad,HospitalisedCovidCases))
        connection.commit()
        cursor.close()
        connection.close()
        # run once a day
        sleep(86400)