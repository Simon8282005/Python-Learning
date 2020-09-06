"""
set可以把一串character或句子中重复的部分给删了
"""

char_list = ['a', 'b', 'c', 'd', 'aa', 'a', 'a', 'b', 'c', 'd', ]
sentence = "Hello World"

# print(set(char_list))
# print(set(sentence))、

unique_char = set(char_list)
# unique_char.add(['a', 'x'])  # Output : Error. 不能添加列表啦
unique_char.add('x')  # 这样就能加一个x进去
# unique_char.clear()  # 清除所有的东西

# print(unique_char.remove('x'))  # 如果没有这个元素就会报错
# print(unique_char.discard('y'))  # 没有这个元素的话不会报错
# print(unique_char)#

set1 = unique_char
set2 = {'a', 'e', 'i'}
print(set1.difference(set2))  # 比较两个set之间的差别
# Output: 只输出不同的东西，一样的不会输出
print(set1.intersection(set2))  # 输出两个set之间的一样并被删除了的东西的东西
