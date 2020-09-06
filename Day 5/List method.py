a = [1, 2, 3, 4, 5, 6]

'''以下是list可以调用的method'''

a.append(20)  # 在6的后面加上一个20
a.insert(1, 100)  # 在[1]的地方添加一个100
a.remove(2)  # 注意！2是数值不是索引
print(a[0])
print(a[-1])  # -1意思是最后一个号码的索引，负数是后面到前面的索引
print(a[0:3])  # 打印出第零位到二位的号码
print(a[:3])  # 同上，但是从第一位开始
print(a[5:])  # 从第五位开始打印
print(a.index(1))  # 打印出1的索引
print(a.count(3))  # 计算列表里一共出现了多少次的3
a.sort()  # 从小到大排序
a.sort(reverse=True)  # 从大到小排序
print(a)
