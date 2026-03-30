"""
Command-line tool to calculate the median of numeric inputs.

Usage:
    python mediaani.py <number1> <number2> ...

Example:
    python mediaani.py 3 1 4 2

Output:
    4 syötelukua: 1.0 2.0 3.0 4.0
    Mediaani: 2.5
"""

import sys

nums = sys.argv[1:]
values = []

for arg in nums:
    try:
        values.append(float(arg))
    except ValueError:
        print(f"Laiton parametri: {arg}")
        sys.exit()

values = sorted(values)
n = len(values, )
index = n // 2

if n == 0:
    print(f"{len(values)} syötelukua")

if n > 0:
    print(f"{len(values)} syötelukua: ", end="")
    print(*values, end="\n")
    if(len(values) % 2):
        med = values[index]
    else:
        med = (values[index - 1] + values[index]) / 2
    print(f"Mediaani: {med}")

