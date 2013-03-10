#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Pmf

def RemainingLifeTimes(pmf, age):
    rpmf = pmf.Copy()
    rem = [v for v in rpmf.Values() if v <= age]
    for r in rem:
        rpmf.Remove(r)
    rpmf.Normalize()
    return rpmf

l = [2, 2, 3, 4, 5, 6, 7, 8, 8, 12]
p = Pmf.MakePmfFromList(l)
print "[Ex 2.4]"
for i in sorted(p.Items()):
    print "%d, %0.3f" % i
print "--------------"
print "total : %0.2f" % p.Total()
print

pp = RemainingLifeTimes(p, 4)
for i in sorted(pp.Items()):
    print "%d, %0.3f" % i
print "--------------"
print "total : %0.2f" % pp.Total()
print


