# 整型变量的学习和注意事项：
# 在Python中, int 类型的变量可以表示：“4300”位的数字



import sys
# a = 9 ** 8888  # 在Python中, 使用“**”表示次方关系 2 ** 2 就表示2的平方;
# print(f"{a}")

### 不同进制的表示和输出：二进制是：0b; 八进制是：0o; 十进制不用说; 十六进制是：0x

# print(f"{0b11}")  
# print(f"{0o11}")
# print(f"{11}")
# print(f"{0x1a}")




# print("Size of int: {} bytes".format(sys.getsizeof(1)))
# print("Size of float: {} bytes".format(sys.getsizeof(3.14)))
# print("Size of string: {} bytes".format(sys.getsizeof("Hello, World!")))

print(f"{sys.getsizeof(0)}, 类型是：{type(0)}")

# 我现在感觉有点难受的是Python和C语言中的有些语法规则有点混了, 这个让我感觉有点难受, 一时间没有转变过来