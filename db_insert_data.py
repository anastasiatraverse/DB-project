#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector




def insert_incomes(d, var, from_in, newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True,
                                   charset='ascii'
                                   )
    cursor = conn.cursor()
    a = "INSERT INTO incomes (din, money, from_in) VALUES ('{}', '{}', '{}');".format(str(d),str(var), str(from_in))
    cursor.execute(a)
    conn.commit()

def insert_outcomes(date, prod_name, total, info, newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True,
                                   charset='ascii'
                                   )
    cursor = conn.cursor()
    a = "INSERT INTO spends (dout, prod_name, total, info) VALUES ('{}', '{}', '{}','{}');".format(str(date), prod_name, int(total), info)
    cursor.execute(a)
    conn.commit()

