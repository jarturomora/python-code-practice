#!/bin/python

import sys

def sum_arr(arr):
    num_arr = [int(n) for n in arr]
    print sum(num_arr)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum_arr(arr)