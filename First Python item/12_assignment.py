# 赋值运算符的使用

# C语言中交换a和b的值, 是设定一个变量temp, 进行交换;
# 但是在Python中可以直接使用一种更加简单的方式进行交换

a = 100
b = 67987
c = 789
print(a, b)
a, b = b, a
print(a, b)

# 三元运算符：和C语言中的不一样, C语言的是 a > b ? a : b
max = a if a > b else b
print(max)

max = a if (a > b and a > c) else (b if b > c else c)
print(max)
