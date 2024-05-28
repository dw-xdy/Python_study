# bool类型变量的使用方式

# num1 = 100
# num2 = 299
# ret = num1 < num2

# if ret:         # 只要是判断条件是“真的”就执行, 这个和C语言中的都是一样的, 但是只是写法什么有点不太一样,
#     print("num1 < num2")

# print("ret =", ret)

# # 在Python中, 会将True视为“1”, 将False视为“0”

# b1 = True
# b2 = False

# print(b1 + 10) # 这里是 1 + 10 = 11
# print(b2 + 10) # 这里是 0 + 10 = 10

# 其实我感觉这里的bool类型的东西都没有什么可以注意的, 只要在实际的操作中好好注意一下就行了, 
# 个人认为不是什么很重要的东西



year = int(input("Enter a year: "))

if year > 2100 or year < 2000:
    print("None!")
else:
    for i in range(2000, year):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            print(i)

# a = 10
# print(a)
