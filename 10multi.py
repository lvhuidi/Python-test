#!/usr/bin/python3
i = 1 
a = 1
print("-" * 60)
while i < 10:
    n = 1
    print("{:2d}的乘法表".format(a),end = "")
    while n < 10:
        print("{:5d}".format(i * n),end = "")#end不自动换行，以空格结尾
        n += 1
    print()
    i += 1
    a += 1
print ("-" * 60)
