# 这个章节学习“逻辑运算符” (感觉和C语言基本上是一样的, 自己看一下就行了, 就当做是复习巩固了)

'''and or not'''# (三个逻辑运算符)


# 布尔"与(and)"：如果x为False,x and y, 返回x的值，否则返回y的计算值。
a = 10
b = 20
print(a and b) # 20 # 这两个最后的输出结果是不一样的, 
print(b and a) # 10

# 布尔"或(or)"：如果x是True,它返回x的值，否则它返回y的计算值。
print(a or b) # 10
print(b or a) # 20

# 布尔"非(not)"：如果x为True,返回False。如果x为False,它返回True。
print(not(a and b))