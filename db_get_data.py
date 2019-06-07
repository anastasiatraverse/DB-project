#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector

def get_incomes(date, newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True
                                   )
    cursor = conn.cursor()
    cursor.execute("SELECT money, from_in FROM incomes WHERE din='{}'".format(str(date)))
    result = cursor.fetchall()
    return result

def get_outcomes(date, newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True
                                   )
    cursor = conn.cursor()
    cursor.execute("SELECT prod_name, total, info FROM spends WHERE dout='{}'".format(str(date)))
    result = cursor.fetchall()
    return result

def get_outcomes_category(date, category, newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True
                                   )
    cursor = conn.cursor()
    cursor.execute("SELECT total FROM spends WHERE dout='{}', prod_name='{}'".format(str(date), str(category)))
    result = cursor.fetchall()
    return result

def get_outcomes_all(newuser, password):
    conn = mysql.connector.connect(host="localhost",
                                   user=newuser,
                                   passwd=password,
                                   database="budget",
                                   use_unicode=True
                                   )
    cursor = conn.cursor()
    cursor.execute("SELECT prod_name, total FROM spends")
    result = cursor.fetchall()
    return result

def get_outcomes_stat(newuser, password):
    a = get_outcomes_all(newuser, password)
    food = 0
    trans = 0
    enter =0
    ut_costs=0 #utility costs
    other=0
    for i in a:
        if i[0]=='food':
            food+=i[1]
        if i[0] =='transport':
            trans +=i[1]
        if i[0]=='entertainment':
            enter+=i[1]
        if i[0]=='utility':
            ut_costs+=i[1]
        if i[0] =='other':
            other+=i[1]
    return(food, trans, ut_costs, enter, other)


