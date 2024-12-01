# Intentionally problematic Python code to trigger PyCharm inspections

import os, sys
import random


def calculate(value, value):
    result = valu * 2
    return result

def UnusedFunction():
    pass

class testclass:
    def __init__(self, value):
        self.value =value

    def badMethodName(self):
        print "Hello, world!"

for i in range(5):
    print(i)
    i = 10

if True
    print   ("Missing colon")
