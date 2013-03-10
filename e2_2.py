#!/usr/bin/env python
# -*- coding: utf-8 -*-

import survey
import e1_3 as F
import thinkstats as ts
import math

def Summarize(data_dir):
    table, first, others = F.MakeTables(data_dir)
    F.ProcessTables(first, others)

    print u'第一子総数：',  first.n
    print u'第二子以降の総数：', others.n

    mu1, mu2 = first.mu, others.mu

    print u'妊娠期間'
    print '第一子',  mu1
    print 'その他', mu2
    print '差：',  mu1-mu2

    return first, others, mu1, mu2

def TVar(table, mu):
    if mu is None:
        mu = F.Process(table)

    dev2 = [(x.prglength -mu)**2 for x in table.records]
    var = ts.Mean(dev2)
    return var


def Summarize2(data_dir):
    table, first, others = F.MakeTables(data_dir)
    first, others, mu1, mu2 =Summarize(data_dir)

    v1 = TVar(first, mu1)
    v2 = TVar(first, mu2)

    return v1, v2

def main(name, data_dir='./data'):
    v1, v2 = Summarize2(data_dir)
    print u'第一子の妊娠期間の分散：', v1
    print u'第二子以降の妊娠期間の分散：', v2

    print u'第一子の妊娠期間の標準偏差：', math.sqrt(v1)
    print u'第二子以降の妊娠期間の標準偏差：', math.sqrt(v2)

if __name__ == '__main__':
    import sys
    main(*sys.argv)



