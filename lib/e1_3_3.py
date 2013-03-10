#!/usr/bin/env python
# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies();
table.ReadRecords('./data')

first = 0
second = 0
third = 0
for i in table.records:
    if i.birthord == 1:
        first += 1
    elif i.birthord == 2:
        second += 1
    elif i.birthord == 3:
        third += 1
    else:
        pass

print 'First: ', first
print 'Second: ', second
print 'Third: ', third

