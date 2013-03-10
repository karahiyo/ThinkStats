#!/usr/bin/python
# -*- coding:utf-8 -*-

import survey

table = survey.Pregnancies()
table.ReadRecords('./data')

print 'The total number of pregnancy records: ',  len(table.records)

