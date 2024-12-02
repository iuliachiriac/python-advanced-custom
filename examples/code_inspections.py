# Intentionally problematic Python code to trigger PyCharm inspections

import os, sys
import random


def calculate(value, value):
    """
    Do something
    :param value:
    :return:
    """
    result = valu * 2
    return result

def UnusedFunction():
    pass

class testclass:
    def __init__(self, value):
        self.value =value

    def badMethodName(self):  # method_name
        print "Hello, world!"

for i in range(5):
    print(i)
    i = 10

if True
    print   ("Missing colon")


# camelCase - never used in Python
# PascalCase - class names
# snake_case - functions, methods, variables
# UPPERCASE_SNAKE_CASE - constants