# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-PlaTDFU1riJGSbeyyYlABHam_eDdcP0
"""

def quarter_of(month):
    quarter_dictionary = {
        "месяц 1 (январь) является частью первого квартала" : [1],
        "месяц 2 (февраль) является частью первого квартала" : [2],
        "месяц 3 (март) является частью первого квартала" : [3],
        "месяц 4 (апрель) является частью второго квартала" : [4],
        "месяц 5 (май) является частью второго квартала" : [5],
        "месяц 6 (июнь) является частью второго квартала" : [6],
        "месяц 7 (июль) является частью третьего квартала" : [7],
        "месяц 8 (август) является частью третьего квартала" : [8],
        "месяц 9 (сентябрь) является частью третьего квартала" : [9],
        "месяц 10 (октябрь) является частью четвертого квартала" : [10],
        "месяц 11 (ноябрь) является частью четвертого квартала" : [11],
        "месяц 12 (декабрь) является частью четвертого квартала" : [12]
    }

    for key,values in quarter_dictionary.items():
        for value in values:
            if value == month:
                return key

print(get_quarter(1))