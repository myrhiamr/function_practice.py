"""
Python function called max_num()to find the maximum of three numbers.
Python function called mult_list() to multiply all the numbers in a list.
Python function called rev_string() to reverse a string.
Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Python function called pascal() that prints out the first n rows of Pascal's triangle. The function accepts the number n, the number of rows to print
"""


def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_num(3, 5, 2))



def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


print(mult_list([1, 2, 3, 4]))


def rev_string(s):
    return s[::-1]

print(rev_string("hello"))


def num_within(x, start, end):
    return start <= x <= end

print(num_within(10, 2, 5))


def pascal(n):
    triangle = []
    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    for row in triangle:
        print(row)

pascal(5)
