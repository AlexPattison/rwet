#!/usr/bin/env python
# this is a comment in python
import sys
for line in sys.stdin:
  line = line.strip()
  offset = line.find(' for ')
  if offset != -1:
    print line[offset:]