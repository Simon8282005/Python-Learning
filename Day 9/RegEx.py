"""
正则表达式
"""

import re

pattern1 = 'cat'
pattern2 = 'bird'
string = 'cat run to dog'

print('Cat: ', re.search(pattern1, string))
print('Dog: ', re.search(pattern2, string))

# multiple patterns ("run" or "ran")
ptn = r"r[au]n"  # 无论是run还是ran都可以被找到,而r则是把这段普通的文字变成正则表达式的文字
print("Ran or run: ", re.search(ptn, "dog runs to cat"))

#  continue
print("---------------------------------------------")
print(re.search(r"r[A-Z]n", "dog RUNS to cat"))
print(re.search(r"r[a-z]", "dog runs to cat"))
print(re.search(r"r[0-9]n", "dog r2n to cat"))
print(re.search(r"r[0-9a-z]n", "dog r2ns to cat"))

print("-----------所有数字和所有不是不是数字的-------------")
# \d : 所有数字
print(re.search(r"r\dn", "run r4n to cat"))
# \D : 所有不是不是数字的
print(re.search(r"r\Dn", "run r4n to cat"))

print("-----任何空白的和任何不是空白的---------------------")
# \s : 任何空白的 [\t\n\r\f\v]， \t是tab键
print(re.search(r"r\sn", "r\nn r4n"))
# \S : 任何不是空白的
print(re.search(r"r\Sn", "r\nn r4n"))

