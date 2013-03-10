#!/usr/bin/env python
# -*- coding: utf-8 -*-

import thinkstats as ts
import math

p = [0.5, 0.5, 1.5, 1.5, 96]

print u'算術平均', ts.Mean(p)
print u'分散', ts.Var(p, ts.Mean(p))
print u'標準偏差', math.sqrt(ts.Var(p, ts.Mean(p)))

