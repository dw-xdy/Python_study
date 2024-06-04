# while循环的使用方法

# 用while循环打印10行："hello, world"

i = 1
while i <= 3:
    print("hello, world")
    i += 1
    

# 感觉和C语言中的有些不同, 但是说实话我现在也理解不了, 这个else存在的意义是什么?(和for循环一样, 真的有点不理解)
count = 0
while count < 3:
    print(f"count is {count}")
    count += 1
else:
    print("count is no longer less than 3")




# 1) 打印1 ~ 100之间所有能被3整除的数

i = 1

while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1



# 打印40 ~ 200之间的偶数
# 该程序使用while循环打印在指定范围内的偶数

j = 40
max = 200

while j <= max:
    if j % 2 == 0:
        print(j)
    j += 1


name = ""

while name != "exit":
     name = input("请输入姓名：")


count = 0
sum = 0
num = 1
max_num = 100

while num <= max_num:
    if num % 9 == 0:
        count += 1
        sum += num
    num += 1

print(sum)
print(count)




i = 0
num = int(input("请输入数字："))

while i <= num:
    print(f"{i} +   {num - i}   =   {num}")
    i += 1
    
    