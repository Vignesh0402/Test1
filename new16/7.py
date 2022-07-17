"""
import mysql.connector as connection

db  = connection.connect( host = "localhost",
                          user = "root",
                          passwd = "Jaijai1@@11",
                          db = "ineuron_working")
"""

'''
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print("+ ", end="")
    print("\r")
'''

'''
num = int(input("Enter a number of rows: "))
for i in range(num, 0, -1):
    for j in range(num-i):
        print("", end=" ")

    for j in range(2*i-i):
        print("*", end=" ")
    print()
'''

'''
n = 8
for i in range(n, 0, -1):
    for j in range(i*2-1):
        print('', end="")
    for j in range(i-1):
        print('*', end="")
    print()
'''


n = int(input("Enter a number:"))
i = 0
while i < n:
    print(' '*(2*i+1) + ' *'*(n-2*i+1))
    i += 1
