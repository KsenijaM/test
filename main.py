#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

money = int(input("Enter sum: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

for value in per_cent.values():
    result = (int(money/100 * value))
    deposit.append (result)
print(deposit)
deposit.append(max(deposit))
print("Максимальная сумма, которую вы можете заработать -", deposit[-1])
