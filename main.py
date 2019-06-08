#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, string, os
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

from langdetect import detect
from tkinter import *
root = Tk()
from db_insert_data import *
from db_get_data import *
from db_create import *
from unicode_check import *
import datetime

if len(sys.argv)<2:
    raise Exception("Must be entered username and password")

root.title("UCU student budget")
root.geometry("800x400")

today = datetime.date.today()

def result_parsing(a):
    result = []
    for i in a:
        result.append(list(i))
    return result


def check_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def distribution():
    def get_value():
        if v_name.get() and v_sum.get() and v_info.get():
            if check_int(v_sum.get()):
                if only_roman_chars(v_name.get()):
                    name = v_name.get()
                    total = v_sum.get()
                    info = str(v_info.get())
                    insert_outcomes(today, name, total, info, sys.argv[1], sys.argv[2])
                    Label(win, text="Додано до Бази Даних!").grid(column=1, row=8, columnspan=4)
                else:
                    Label(win, text="Будь ласка, введіть інформацію англійською мовою").grid(column=1, row=7, columnspan=2)
            else:
                Label(win, text="-- Був введен не правильний тип даних, \n"
                                "У перше поле варто ввести числовий тип даних\n").grid(row=6, column=1, columnspan=2)
        else:
            Label(win, text="Потрібно заповнити всі поля!").grid(row=5, column=1, columnspan=2)
    win = Toplevel(root)
    win.title("Розподілення")

    v_name = StringVar()
    v_sum = StringVar()
    v_info = StringVar()

    Label(win, text=" -- У полях 'назва', 'сума' та 'додат. інф.' слід вести куди саме були витрачені грошу('food','transport','entertainment','utility','other'),\n"
                    " суму витрат, та додаткову інформацію відповідно").grid(row=0, column=1, columnspan=2)
    Label(win, text="Назва").grid(row=1, column=1)
    Entry(win, textvariable=v_name).grid(row=1, column=2)
    Label(win, text="Сума").grid(row=2, column=1)
    Entry(win, textvariable=v_sum).grid(row=2, column=2)
    Label(win, text="UAH").grid(row=2, column=3)
    Label(win, text = "Додат. інф.").grid(row=3, column=1)
    Entry(win, textvariable=v_info).grid(row=3, column=2)

    Button(win, text="Ввід/Зберегти", command=get_value).grid(row=4, column=1)
    Button(win, text="Вихід", command = win.destroy).grid(row=4, column=2)


def get_date():
    def get_value():
        if v_day.get() and v_month.get() and v_year.get():
            if check_int(v_day.get()) and check_int(v_month.get()) and check_int(v_year.get()):
                day = v_day.get()
                month = v_month.get()
                year = v_year.get()
                full_date = "{}-{}-{}".format(year, month, day)
                if v_rad_1.get():
                    rad_butt = v_rad_1.get()
                    if rad_butt == "incomes":
                        display_incomes(full_date)
                    else:
                        display_outcomes(full_date)
                else:
                    Label(win, text="Потрібно обрати яка саме інформація необхідна - надходження або витрати ").grid(row=7, column=1, columnspan=2)
            else:
                Label(win, text="-- Був введен не правильний тип даних, \n"
                                "У всі поля варто ввести числовий тип даних\n").grid(row=6, column=1, columnspan=2)
        else:
            Label(win, text="Потрібно заповнити всі поля!").grid(row=6, column=1, columnspan=2)



    win = Toplevel(root)
    win.title("Введення дати")
    Label(win, text="-- У полях слід вести дату у наступному вигляді:\n"
                    "День 01\n"
                    "Місяць 05\n"
                    "Рік 2019\n"
                    "Також варто обрати яку саму інформацію вам потрібна - надходження або витрати ").grid(row=0, column=1, columnspan=2)
    Label(win, text="День").grid(row=1, column=1)
    Label(win, text="Місяць").grid(row=2, column=1)
    Label(win, text="Рік").grid(row=3, column=1)
    v_day=StringVar()
    v_month=StringVar()
    v_year=StringVar()

    v_rad_1 = StringVar()

    Entry(win, textvariable=v_day).grid(row=1, column=2)
    Entry(win, textvariable=v_month).grid(row=2, column=2)
    Entry(win, textvariable=v_year).grid(row=3, column=2)

    Radiobutton(win, text="Надходження за період", variable=v_rad_1, value="incomes").grid(row=4,column=1)
    Radiobutton(win, text="Витрати за період", variable=v_rad_1, value="outcomes").grid(row=4, column=2)
    Button(win, text="Далі", command = get_value).grid(row=5, column=1, columnspan=2)

def display_incomes(date):
    win = Toplevel(root)
    win.title("Надходження за період")
    result = get_incomes(date, sys.argv[1], sys.argv[2])
    parser = result_parsing(result)
    if len(parser)>0:
        Label(win, text="За вибраний період були наступні надходження").grid(row=0, column=1)
        for i in range(len(parser)):
            a = 'Сума: {}\n Від: {}'.format(parser[i][0], parser[i][1])
            Label(win, text=a).grid(row = i+1, column = 1)
    else:
        Label(win, text="За даний період немає надходжень").grid(row=1, column=1)

def display_outcomes(date):
    win = Toplevel(root)
    win.title("Витрати за період")
    result = get_outcomes(date, sys.argv[1], sys.argv[2])
    parser = result_parsing(result)

    if len(parser)>0:
        Label(win, text="За вибраний період були наступні витрати").grid(row=0, column=1)
        for i in range(len(parser)):
            a = 'Назва: {}\nСума: {}\nДодат. інфо.: {}'.format(parser[i][0], parser[i][1], parser[i][2])
            Label(win, text=a).grid(row = i+1, column = 1)
    else:
        Label(win, text="За даний період немає витрат").grid(row=1, column=1)


def new_incomes():
    def get_value():
        if v.get() and v1.get():
            if check_int(v.get()):
                if only_roman_chars(v1.get()):
                    sum = int(v.get())
                    from_in = str(v1.get())
                    insert_incomes(today, sum, from_in, sys.argv[1], sys.argv[2])
                    Label(win, text="Додано до Бази Даних!").grid(column=1, row=7, columnspan =4)
                else:
                    Label(win, text="Будь ласка, введіть інформацію англійською мовою").grid(column=1, row=6, columnspan=4)
            else:
                Label(win, text="-- Був введен не правильний тип даних, \n"
                                "У перше поле варто ввести числовий тип даних\n").grid(column=1, row=5, columnspan=4)
        else:
            Label(win, text='Потрібно заповнити всі поля!').grid(row=4, column=1, columnspan = 4)
    win = Toplevel(root)
    win.title("Прибуток")
    v = StringVar()
    v1 = StringVar()
    Label(win, text=" -- У полях 'сума' та 'від' слід вести суму надходжень та звідки надішли гроші відповідно").grid(row=0, column=1, columnspan=3)
    Label(win, text="Сума").grid(row=1, column=1)
    Entry(win, textvariable=v).grid(row=1, column=2)
    Label(win, text="UAH").grid(row=1,column=3)
    Button(win, text="Ввід", command = get_value).grid(row=1, column=4)
    Label(win, text="Від:").grid(row=2, column=1)
    Entry(win, textvariable=v1).grid(row=2, column=2)

    Button(win, text ="Розподілення", command = distribution).grid(row=2, column=4)
    Button(win, text="Вихід", command=win.destroy).grid(row=3, column=2, padx=(0, 100))


def display_stat():
    win = Toplevel(root)
    win.title("Статистика")
    food, trans, ut_cost, enter, other = get_outcomes_stat(sys.argv[1], sys.argv[2])
    Label(win, text='Статистика витрат по категоріям за весь час:').grid(row=0, column=1)
    Label(win, text="Їжа ------ {}".format(food)).grid(row=1, column=1)
    Label(win, text="Транспорт ------ {}".format(trans)).grid(row=2, column=1)
    Label(win, text="Розваги ------ {}".format(enter)).grid(row=3, column=1)
    Label(win, text="Комунальні витрати ------ {}".format(ut_cost)).grid(row=4, column=1)
    Label(win, text="Інше ------ {}".format(other)).grid(row=5, column=1)
    Button(win, text="Вихід",command=win.destroy).grid(row=6, column=1)


check_db(sys.argv[1], sys.argv[2])


Label(root, text="Привіт!\n Дана програма предназначена для ведення твого студентського бюджету."
                 "\nБудь ласка, оберіть одну з наступних функцій").grid(row=0, column=1, columnspan=2)

Button(root, text="Прибуток", command=new_incomes).grid(row=1, column=1)
Label(root, text=" - введення нових грошових надходжень до бази даних").grid(row=1, column=2)

Button(root, text="Витрати", command=distribution).grid(row=2, column=1)
Label(root, text=" - введення нових витрат до бази даних").grid(row=2, column=2)

Button(root, text="Надходження за період", command=get_date).grid(row=3, column=1)
Label(root, text=" - знаходження інформації надходжень за вибраний період").grid(row=3, column=2)


Button(root, text="Витрати за період", command = get_date).grid(row=4, column=1)
Label(root, text=" - знаходження інформації витрат за вибраний період").grid(row=4, column=2)


Button(root, text="Статистика витрат", command=display_stat).grid(row=5, column=1)
Label(root, text=" - відображення статистики за вибраними параметрами").grid(row=5, column=2)


Button(root, text="Вихід", command=root.destroy).grid(row=7, column=1)
Label(root, text=" - вихід з програми").grid(row=7, column=2)


root.mainloop()


