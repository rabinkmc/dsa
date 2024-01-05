"""
Binary search in python
bisect module

This module provides support for maintaining a list in sorted order without having to sort the list after each insertion.

As the name says, it uses bisection algorithm.

bisect.bisect_left
-> locate the insertion point for x in a to maintain sorted order., say ip is the insertion point

partitions the array into two parts
arr[:ip] -> In this half, all the elements are less than x
arr[ip:] -> In this half, all the elements are greater than x

bisect.bisect_right, bisect
-> locates the insertion point for x such that insertion point, ip comes after the existing entries of x
partitions the array into two parts
arr[:ip] -> In this half, all the elements are less than or equal to x
arr[ip:] -> In this half, all the elements are greater than x

bisect.insort_left
inserts x in a sorted order, first performs bisect_left to get the insertion point and then performs list.insert(ip)
so, it is 0(n)

so 0(lgn) search is dominated by 0(n) insertion 

bisect.insort_right, bisect.insort
inserts x in a sorted order, first performs bisect_right to get the insertion point and then performs list.insert(ip)

so 0(lgn) search is dominated by 0(n) insertion 
"""

"""
This is practice module to learn to work with bisection library in python
I will try to implement basic queries in sorted array
"""
import bisect

def index(arr, x):
    """
    find left most values exactly equal to x
    """
    ip = bisect.bisect_left(arr, x)
    if ip != len(arr) and arr[ip] == x:
        return ip
    raise ValueError

def find_lt(arr, x):
    """
    find left most value just less than x
    if ip == 0, it means there is no value in arr that is less than x
    [1, 2, 3, 7]
    """
    ip = bisect.bisect_left(arr, x)
    if ip:
        return arr[ip-1]
    raise ValueError

def find_le(arr, x):
    """
    find right most value that is just equal to x
    if ip == 0, it means there is no value in arr that is less than x
    """
    ip = bisect.bisect_right(arr, x)
    if ip:
        return arr[ip-1]
    raise ValueError

def find_gt(arr, x):
    """
    find left most value that is greater than x
    if ip == len(arr), it means there is no value in arr that is greater than x
    """
    ip = bisect.bisect_right(arr, x)
    if ip != len(arr):
        return arr[ip]
    raise ValueError

def find_ge(arr, x):
    """
    find left most value that is greater than or equal to x
    """
    ip = bisect.bisect_left(arr, x)
    if ip != len(arr):
        return arr[ip]
    raise ValueError
