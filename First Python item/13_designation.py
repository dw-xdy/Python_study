# Python中的标识符的命名规则

# 1、由26个英文字母大小写，0-9，一组成
# 2、数字不可以开头
# 3、不可以使用关键字，但能包含关键字
# 4、Python区分大小写
# 5、标识符不能包含空格

# Python中的标识符的命名规则
# 1) 变量：变量要小写, 若是有多个单词, 使用下划线分开, 常量全部大写
num = 20
my_friend_age = 23
PI = 3.1425926

# 2) 函数：函数名一律小写, 若是有多个单词, 使用下划线隔开, 另外：私有函数用双下划线开头

def my_func(var1, var2):
    pass
def __private_func(var1, var2):
    pass



# 3) 类：使用大驼峰命名
# 1.驼峰命名法有两种，大驼峰命名和小驼峰命名
# 2.大驼峰命名，多个单词的首字母用大写开头，比如：MyName
# 3.小驼峰命名，第1个单词的首字母用小写，后面的单词首字母都大写，例如：youName
#案例
class Foo:
    pass

