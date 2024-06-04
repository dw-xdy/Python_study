# 这章节主要学习Python中的for循环语句, 总体来说还是比较简单的, 因为我自己也是有C语言的基础的还是


# Python中的for循环
# range()函数用于生成一系列的数字序列(列表)
# 1) 生成一个[1, 2, 3, 4, 5]
r1 = range(1, 6)

print(list(r1))

# 2) 生成一个[0, 1, 2, 3, 4, 5]

r2 = range(0, 6)

print(list(r2))

# 3) 生成一个[1, 3, 5, 7, 9]
r3 = range(1, 10, 2)

print(list(r3))

# 4) 用range函数输出10句hello Python
for i in range(10):
    print("hello Python")
    



languages = ["c", "c++", "Python"]

for i in languages:
    print(i)

# 注意, for循环和else也是可以进行组合的, 执行了for循环之后就会执行else, 
# 若是for循环中break, 跳过了就不会执行else

# 感觉和C语言中的有些不同, 但是说实话我现在也理解不了, 这个else存在的意义是什么?
