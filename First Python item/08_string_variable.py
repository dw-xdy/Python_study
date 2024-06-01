# 字符串的使用方式
# C语言和Python语言的使用方式和语法知识都是有一定的区别的, 对于我来说有点麻烦, 还是要好好注意一下的

# str1 = 'hello "laobiao"'
# print(str1)

# str2 = 'int main函数的使用方式'
# print(str2)
# 若是想要打印字符串中的双引号“和单引号',那就在使用字符串的时候用单引号'和双引号"




# 使用三个单引号'''内容''', 或者三个双引号"""内容"""可以将字符串的内容(格式什么的都是一样的)保持原样进行输出
# 在输出复杂的格式的内容是比较有用的, 比如下面的形式

# str21 = """【船】把(锚)吊放在锚架上；宿娼；〈口〉呕吐；〈俚〉寻欢
# abbr.(=computerized axial tomography)【医】计算机化轴向层面X射线摄影法
# 网络卡特(Carter)；过氧化氢酶(catalase)；卡特彼勒(Caterpillar)"""

# print(str21)

# # 在字符串前面加'r'可以使整个字符串不会被转义
# str2 = "Jack\nming\tking"
# print(str2)

# str3 = r"Jack\nming\tking"
# print(str3)




# 字符串的驻留机制
str1 = "hello"
str2 = "hello"
str3 = "hello"

# id()函数可以返回对象/数据的内存地址
print(id(str1))
print(id(str2))
print(id(str3))

a = 10
b = 1000
print(id(a))
print(id(b))

# 驻留机制几种情况讨论（注意：需要在交互模式下win+r->python) (而且在Pycharm中会进行优化, 没有下面的这种情况)
# 1)字符串是由26个英文字母大小写，0-9，-组成
# 2)字符串长度为0或者1时
# 3)字符串在编译时进行驻留，而非运行时
# 4)[-5,256]的整数数字

str3 = "123###"
str4 = "123###"
print(id(str3))
print(id(str4))


