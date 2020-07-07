#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector
from mysql.connector import Error
from time import sleep
import sshtunnel
from sshtunnel import SSHTunnelForwarder

sshtunnel.SSH_TIMEOUT = 10.0
sshtunnel.TUNNEL_TIMEOUT = 10.0


try:
    #global connection
    with SSHTunnelForwarder(
            ('ipa-009.ucd.ie' ,22),
            ssh_username='student',
            ssh_password='Ucd-cs-2019!',
            local_bind_address=('0.0.0.0',1234),
            remote_bind_address=('127.0.0.1', 8080)
    ) as tunnel:
        connection = mysql.connector.connect(host='137.43.49.25',
                                            database='bus_data',
                                            user='admin',
                                            password='Group8sql',
                                            port = "3306")
        if connection.is_connected():
            print("This connection worked!")
            # global cursor
            # cursor = connection.cursor(buffered=True)  # create cursor object - this can execute sql statments
            # return cursor
            # break
        else:
            print("Connection not established")

except Error as error:
    print("ERRROR!!: ", error)
    print("will try to connect again in 10 seconds")
    sleep(10)




server = SSHTunnelForwarder(
    ('ipa-009.ucd.ie',22),
    ssh_username="student",
    ssh_password="Ucd-cs-2019!",
    local_bind_address=('0.0.0.0',1234),
    remote_bind_address=('127.0.0.1', 8080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

server.stop()





#
# try:
#     global connection2
#     connection2 = mysql.connector.connect(host='localhost',
#                                          database='dublinBus',
#                                          user='root',
#                                          password='dt85226305',
#                                          #auth_plugin='mysql_native_password'
#                                         )
#     if connection2.is_connected():
#         print("This connection worked!")
#
#     else:
#         print("Connection not established")
#
# except Error as error:
#     print("ERRROR!!: ", error)
#     print("will try to connect again in 25 seconds")
#     sleep(10)

