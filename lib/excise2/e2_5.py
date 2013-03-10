#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pmf

def PmfMean(pmf):
    return sum([(k * v) for k, v in pmf.Items()])

def PmfVar(pmf, mu=None):
    if mu is None:
        mu = PmfMean(pmf)
    return sum([v *((k-mu)**2) for k, v in pmf.Items()])

def main():
    l = [1, 2, 3, 3, 4, 5, 6, 6, 5, 7, 8, 12, 3, 4, 5]
    pmf = Pmf.MakePmfFromList(l)

    print "Mean is %0.3f" % pmf.Mean()
    print "PmfMean is %0.3f" % PmfMean(pmf)

    print "Var is %0.3f" % pmf.Var()
    print "PmfVar is %0.3f" % PmfVar(pmf)

if __name__ == '__main__':
    main()
