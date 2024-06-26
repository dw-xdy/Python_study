# 这一章节主要是学习“位运算”和“原码, 反码, 补码”的知识, 也算是一个查漏补缺吧

# 不知道为什么, 我感觉目前来说, 位运算对于我来说的意义不大, 但是我一般也是知道的, 主要是因为


'''以下是一个简单的例子，展示了位运算在状态压缩方面的应用。
假设有一个集合{A, B, C, D, E}，我们需要列举出所有子集的情况。'''

elements = ['A', 'B', 'C', 'D', 'E']
n = len(elements)

# 遍历集合的所有子集
for i in range(1 << n):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(elements[j])
    print(subset)
'''我们使用了位运算来实现了集合的所有子集的列举。通过对集合的每个元素进行位运算，
我们可以高效地表示和遍历所有可能的子集情冋。这种使用位运算来实现状态压缩和高效遍历的方法，
可以帮助我们在算法优化中提高效率。'''