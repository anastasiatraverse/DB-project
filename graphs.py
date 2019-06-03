from datetime import timedelta, date
import matplotlib.pyplot as plt
from db_get_data import *

def date_list(lst_from, lst_to):
    def daterange(date1, date2):
        for n in range(int((date2 - date1).days) + 1):
            yield date1 + timedelta(n)

    start_dt = date(lst_from[0], lst_from[1], lst_from[2])
    end_dt = date(lst_to[0], lst_to[1], lst_to[2])

    date_list = []
    for dt in daterange(start_dt, end_dt):
        date_list.append(dt.strftime("%Y-%m-%d"))
    return date_list

def value_for_graph(category, lst_from, lst_to):
    date_lst = date_list(lst_from, lst_to)
    outcomes_list = []
    for i in date_lst:
        result = get_outcomes_category(i, category)
        for j in result:
            outcomes_list.append(j[0])
    make_plot(date_lst, outcomes_list)

def make_plot(date_lst, out_lst):
    fig, res_plot = plt.subplots()
    res_plot.plot(date_lst, out_lst)
    res_plot.set(xlabel='dates', ylabel='spends',
       title='Витрати по категорії')
    res_plot.grid()
    fig.savefig("plot_categ.png")

