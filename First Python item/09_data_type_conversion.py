# 这一章节学习 数据类型转换

# 隐式类型转换
# Python变量的类型不是固定的, 会根据变量当前的值在运行的时候决定的, 可以通过内置函数type()查看, 

# 1) 在Python语言中会根据上下文, 自动进行转换
var1 = 10
print(type(var1)) # int类型

var1 = 1.2
print(type(var1)) # float类型

var1 = "真是的, 我服了"
print(type(var1)) # 字符串类型

# 2) 在运算的时候, 数据类型会向高精度转换, float类型的精度高于int类型
var2 = 10
var3 = 1.2
var4 = var2 + var3
print(f"var4 = {var4}, var4的类型是: {type(var4)}")
var2 = var2 + 0.1
print(f"var2 = {var2}, var2的类型是: {type(var2)}")


# 显式类型转换 
a = 10.6
a = int(a)
print(a)

# 注意事项：
# 1) 不管什么样的值：int类型, float类型都可以转为str, str(x)将对象x转换为字符串
# 2) int转换为float会增加小数部分, 反过来会去掉小数部分,(这一点和C语言一样)
# 3) str可以转换为“int类型”和“float类型”,但是需要注意的是要进行分离, 如123.3->float, 不能是int, 
#                                                              12345->float和int
# 4) 注意str转换的格式和有效的数据, 比如"hello"不能转换为“int类型”.
# 5) 对一个变量进行强制转换，会返回一个数据/值，注意，强制转换后，并不会影响原变量的数据类型（即：不会影响
# 原变量指向的数据/值的数据类型)，
str1 = "123.54"
str1 = float(str1)
print(str1, type(str1))

str2 = "12354"
print(float(str2), type(str2))  # 这里需要注意的地方是：数据转换发生在print函数中, 不会对原数据有影响.

