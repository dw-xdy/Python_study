# 学习怎么进行输出
# 有兴趣可以看一下(网站中的进行输出的方式)
a = 5
fact = 120
name  = "老表"
age = 19
id = 345
ming = 2.55
# 1) 使用“%”进行输出
print("%d 的阶乘为：%d" %(a, fact))
print("%d 的阶乘为：%d" %(a, fact))
print("%s %d %d" %(name, age, id))
# https://blog.csdn.net/hesongzefairy/article/details/104179419


# 2) 使用format函数进行输出
print("{} 的阶乘为：{}".format(a, fact))
print("{} {} {}".format(name, age, id))
# https://www.runoob.com/python/att-string-format.html


# 3) 使用f-string的方式进行输出  (个人认为这个方式是最简单的, 只是和C语言中的方式有点不一样, 可能还是需要适应一下就好了)
print(f"个人信息：姓名{name} 年龄{age} 信息{id} 小数：{ming}")
#  https://blog.csdn.net/weixin_44200553/article/details/130408971
# 这篇文章是将这个形式的输出方式进行全面讲解的, 有兴趣可以看一下

