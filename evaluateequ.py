#!/usr/bin/python3
##计算数学公式1/x+1/(x+1)+1/(x+2)+ ... +1/n，我们设 x = 1，n = 10
##思路：有x、n，模拟一些数值看结果,因为是加的公式，考虑用sum,n有取值范围用for循环
sum = 0
for i in range(1,11):
    sum = sum + 1 / i
    print("{:4d} {:4.2f}".format(i , sum))

