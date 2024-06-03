# 学习一下Python中的if,elif,else语句(选择控制)
# if 语句中的缩进是很重要的, 相当于是C语言中的大括号, 那怕是进行了换行,
# 中间有一行空的, 只要有相同的缩进就是在一个“if”语句之下, 相当于在一个大括号里面.
if 4 > 1:
    print("zhenshihuagnayn")
    print("mginmignmginmginggjnm")
    
    print("wdxiangyfanshi")

# 最短的缩进对最长的有包含关系, 缩进前后是没有要求的 (和C语言一样, 只要稍微注意一下就行了)

# 输入一个程序, 若是一个人的年龄大于18, 就输出 "已经是成年人了"

age = int(input("请输入年龄："))

if age >= 18:
    print("你已经是一个成年人了")
elif 0 <= age < 28:
    print("你还是一个未成年人")
else:
    print("md给我输入年龄")



x = 4
y = 1
if x > 2:
    if y > 2:
        print(x + y)
    else:
        print("x = ", x)
        


a = 10
b = 3

if a + b > 50:
    print("hello world")
else:
    print("w zhen d shi fu le")

c = 15.4
d = 12.3

if c > 10.0 and d < 20.0:
    print(c + d)
    
    

    
    
e = 61

if e % 3 == 0 and e % 5 == 0:
    print(e)

year = int(input("请输入年份："))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year)
    
    
    
    

high = float(input("请输入身高："))
money = int(input("请输入财富："))
handsome = input("帅吗?请输入(Y/N) ")

if high > 180 and money > 10000000 and handsome == 'Y':
    print("我一定要")
elif high > 180 or money > 10000000 or handsome == 'Y':
    print("bishagnbuzu")
else:
    print("buxign ")






score = float(input("请输入成绩："))

if score > 8:
    gender = input("请输入性别：")
    if gender == '男':
        print("去男子组")
    elif gender == '女':
        print("去女子组")
elif score <= 8:
    print("淘汰")






month = int(input("请输入月份："))
age = int(input("请输入年龄："))

if 4 <= month <= 10:
    if age < 18:
        print("支付30元")
    elif 18 <= age <= 60:
        print("支付60元")
    else:
        print("支付20元")
if 10 < month <= 12 or 1 <= month < 4:
    if age >= 18:
        print("支付40元")
    else:
        print("支付20元")
        
        
