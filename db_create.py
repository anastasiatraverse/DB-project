#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector



def check_db(newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True,
                                   charset='ascii'
                                   )
    cursor = conn.cursor()
    db=list()
    cursor.execute("SHOW DATABASES;")
    for i in cursor:
        db.append(i[0])

    if 'budget' not in db:
        cursor.execute("CREATE DATABASE budget;")

    cursor.execute("USE budget;")

    table = list()
    cursor.execute("SHOW TABLES;")
    for i in cursor:
        table.append(i[0])

    if 'incomes' not in table:
        cursor.execute("CREATE TABLE incomes(id INT AUTO_INCREMENT PRIMARY KEY, din VARCHAR(255), money INT,from_in VARCHAR(255));")
    if 'spends' not in table:
        cursor.execute("CREATE TABLE spends(id INT AUTO_INCREMENT PRIMARY KEY, dout VARCHAR (255), prod_name VARCHAR (255), total INT, info VARCHAR (255));")


