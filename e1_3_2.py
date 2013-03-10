#!/usr/bin/python
# -*- coding: utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords('./data')
print u'妊娠レコード数： ',  len(table.records)

count = 0
for i in table.records:
    if i.birthord != 0:
        count += 1

print u'生児出生数:',  count
