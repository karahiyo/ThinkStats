#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thinkstats as ts
import math

p = [0.5, 0.5, 1.5, 1.5, 96]

print 'Pumpkins:'
print 'mean :', ts.Mean(p)
print 'Variance :', ts.Var(p, ts.Mean(p))
print 'Standard Diviation :', math.sqrt(ts.Var(p, ts.Mean(p)))

