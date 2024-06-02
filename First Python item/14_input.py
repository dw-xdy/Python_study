# 这个章节学习input函数的使用方法, 和C语言中的scanf有点像,但是好像是更加灵活

name = input("我的姓名是：")
age = input("我的年龄是：")
gender = input("我的性别是：")

print("我的姓名是：", name)
print("我的年龄是：", age)
print("我的性别是：", gender)

# 注意细节：从控制台接受的数据类型是“str”类型
# 如果我们想要对接收到的数据进行算术运算, 则需要进行数据的转换

score = int(input("我的成绩是："))  # 可以直接进行在进行输入的时候就进行数据转换
print("我的成绩是", score + 23)

