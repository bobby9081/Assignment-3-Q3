# -*- coding: utf-8 -*-
"""Assignment 3 Q3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OPxLr0Ywhq0TfhSVKN9b0j_kWUjfbEKD
"""

Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(a):
    b={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in a:
        if c.isupper():
           b["UPPER_CASE"]+=1
        elif c.islower():
           b["LOWER_CASE"]+=1
        else:
            pass
    print ("No. of Upper case characters : ", b["UPPER_CASE"])
    print ("No. of Lower case Characters : ", b["LOWER_CASE"])

string_test('The quick Brown Fox')