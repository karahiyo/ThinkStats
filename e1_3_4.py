#!/usr/bin/env python
# -*- coding: utf-8 -*-

import survey

table  =  survey.Pregnancies()
table.ReadRecords('./data')

first = 0
firstPrgL = 0
others = 0
othersPrgL = 0

for i in table.records:
    if i.outcome != 1:
        continue

    if i.birthord == 1:
        first += 1
        firstPrgL += i.prglength
    elif i.birthord > 1:
        others += 1
        othersPrgL += i.prglength
    else:
        pass

print u'第一子の妊娠期間平均    ：', float(firstPrgL)/first
print u'第二子以降の妊娠期間平均：', float(othersPrgL)/others

print u'その差：', (float(firstPrgL)/first -float(othersPrgL)/others) * 7



