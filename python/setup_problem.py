"""
only works for leetcode problems ( "id. description")
"""
import sys
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = input("Enter file name: ")
number, name = file.split(".")
problem_id = number
name = name.strip().lower().replace(" ", "-")
print(problem_id + "-" + name + ".py")
