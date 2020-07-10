#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector
from mysql.connector import Error
from time import sleep
import logging

# guide: https://dev.mysql.com/doc/connector-python/en/
# guide2: https://www.w3schools.com/python/python_mysql_getstarted.asp
# guide3: https://www.geeksforgeeks.org/mysqldb-connection-python/

# create log file to register database connection errors
logging.basicConfig(filename='database_connect_error_log.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def establishConnection():
    """This function connects to the mysql database on the VM
    NB user must enter their own password details below"""
    while True:
        try:
            global connection
            connection = mysql.connector.connect(host='localhost',
                                                 database='bus_data',
                                                 user='root',  # 'admin',
                                                 password='dt85226305')  # 'Group8sql')
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



def weather_writer(dt, city_id, city_name, lat, lon, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon):
    """This function writes the current weather from openweathermap api call to the table currentWeather on our DB. If table has data, it will update it. If table is emtpy
    it will leave data there"""
    establishConnection()
    query = "SELECT COUNT(*) from bus_data.currentWeather"
    cursor.execute(query)
    result = cursor.fetchone()
    rows = result[0]  # total rows
    print("number of rows:", rows)
    if rows>0:
        cursor.execute('truncate table bus_data.currentWeather')
    if rows==0:
        logging.info('Table is empty')
    cursor.execute('insert into bus_data.currentWeather (dt, city_id, city_name, lat, lon, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon)' \
    'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (dt, city_id, city_name, lat, lon, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon))
    connection.commit()
    cursor.close()
    connection.close()



def forecast_writer(dt, dt_iso, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon):
    """This function writes the 5-day weather forecast from openweathermap api call to the table forecastWeather on our DB. If table has data, it will update it. If table is emtpy
    it will leave data there"""
    establishConnection()
    query = "SELECT COUNT(*) from bus_data.forecastWeather"
    cursor.execute(query)
    cursor.execute('insert into bus_data.forecastWeather (dt, dt_iso, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon)' \
    'values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (dt, dt_iso, temp, temp_min, temp_max, pressure, humidity, wind_speed, wind_deg, clouds_all, weather_id, weather_main, weather_description, weather_icon))
    connection.commit()
    cursor.close()
    connection.close()



def empty_table():
    """This function empties the forecastWeather table on our database if there is already info in it - if it is already empty, it does nothing"""
    establishConnection()
    query = "SELECT COUNT(*) from bus_data.forecastWeather"
    cursor.execute(query)
    result = cursor.fetchone()
    rows = result[0]  # total rows
    print("number of rows in forecast table:", rows)
    if rows>0:
        cursor.execute('truncate table bus_data.forecastWeather')
    if rows==0:
        logging.info('Forecast Table is empty')
    connection.commit()
    cursor.close()
    connection.close()