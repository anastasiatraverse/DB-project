import MySQLdb

conn=MySQLdb.connect("localhost",
                     "root",
                     "root",
                     "budget",
                     use_unicode=True,
                     charset="utf8")
cursor = conn.cursor()


def insert_incomes(d, var, from_in):
    a = "INSERT INTO incomes (din, money, from_in) VALUES ('{}', '{}', '{}');".format(str(d),str(var), str(from_in))
    cursor.execute(a)
    conn.commit()

def insert_outcomes(date, prod_name, total, info):
    a = "INSERT INTO spends (dout, prod_name, total, info) VALUES ('{}', '{}', '{}','{}');".format(str(date), prod_name, int(total), info)
    cursor.execute(a)
    conn.commit()

