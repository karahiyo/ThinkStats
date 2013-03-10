#!/usr/bin/python
# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords('./data')

count = 0
for i in table.records:
    if i.birthord != 0:
        count += 1

print 'Num of birthord: ',  count
