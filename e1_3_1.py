#!/usr/bin/python
# -*- coding:utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords('./data')

print u'妊娠レコードの総数: ',  len(table.records)

