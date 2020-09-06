25/8/2020

### 第二十五天

# 什么是 re 库 ？
Re 库是 Python 的标准库，主要用于字符串匹配

# 正则表达式的表示类型

## raw string 类型
> 原生字符串类型

re 库采用 raw string 类型表示正则表达式，表示为： `r ' text '`

> raw string 意思是不包含转义符的字符串

例如：

```re
r '[1-9]\d{5}'
r '\d{3}-\d{8}|\d{4}-\d{7}' （表示国内电话号码）
```

## string 类型

string 类型也是正则表达式的其中一种类型，但较 raw string 来的繁琐

```re
r '[1-9]\\d{5}'
r '\\d{3}-\\d{8}|\\d{4}-\\d{7}'
```

如果使用 `string` 类型的话，要在 `\d` 的前面新增 `\`

除此之外，**所有**在正则表达式中有斜杠的地方，如果是使用 `string` 类型来表示的话，都需要增加多一个斜杠。

**所以当正则表达式出现转义符（如 \d）的时候，比较好就是使用 raw string 类型来表达**

# Re 库的主要功能函数
<table>
<tr>
    <th>函数</th>
    <th>说明</th>
</tr>
<tr>
    <th>re.search()</th>
    <th>在一个字符串中搜索匹配正则表达式的第一个位置，返回 match 对象</th>
</tr>
<tr>
    <th>re.match()</th>
    <th>从一个字符串的开始位置起匹配正则表达式，返回 match 对象</th>
</tr>
<tr>
    <th>re.findall()</th>
    <th>搜索字符串，以列表类型返回全部能匹配的子串</th>
</tr>
<tr>
    <th>re.split()</th>
    <th>将一个字符串按照正则表达式匹配的结果进行分割，返回列表类型</th>
</tr>
<tr>
    <th>re.finditer()</th>
    <th>搜索字符串，返回一个匹配结果的送代类型，每个送代元素是 match 对象</th>
</tr>
<tr>
    <th>re.sub()</th>
    <th>在一个字符串中替换所有正则表达式的子串，返回替换后的字符串</th>
</tr>
</table>

# Re 库的主要功能函数说明
- re.search( pattern, string, flags=0 )
> - pattern： 正则表达式的字符串或原生字符串表示
> - string：待匹配字符串
> - flags：正则表达式使用时的控制标记

- flags 说明
> re.I / re.IGNORECASE：忽略正则表达式的大小写，[A-Z]能匹配小写字符
> 
> re.M / re.MULTILINE：正则表达式中的 ^ 操作符能够将给定字符串的每行当作匹配开始
>
>re.S / re.DOTALL：正则表达式中的 . 操作符能够匹配所有字串 ，默认匹配除换行外的所有字符

- re.search 列子:
```python
import re
```
导入 re 库

```python
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
```
使用 `re.search()` 来寻找 `r'[1-9]\d{5}'` 中的 `‘BIT 100081’`

```python
if match:
    print(match.group(0))
```
**Output:** 100081

---

- re.match( pattern, string, flags=0 )
> 从一个字符串的开始位置起匹配正则表达式，返回 match 对象
> - pattern： 正则表达式字符串或原生字符串表示
> - string：带匹配字符串
> - flags：正则表达式使用时的控制标记

- re.match 列子：
```python
match = re.match(r'[1-9]\d{5}', 'BIT 100081')
```
还是一样的创建一个函数，然后打印出来
```python
if match:
    print(match.group(0))
```
结果报错了
```python
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    match.group(0)
AttributeError: 'NoneType' object has no attribute 'group'
```
错误提示 `match` 对象为 `NoneType`，也是空的意思。这是因为 `match` 对象是从头开始匹配字符串的，但我们想要匹配的 `BIT 100081` 中的 `BIT` 并不再范围内，所以 `match` 对象为空的。

我们调整一下代码看看结果是怎样的：
```python
match = re.match(r'[1-9]\d{5}', '100081 BIT')

if match:
	match.group(0)

# Output：
'100081'
```
怎样？是不是不报错了啊 XD

---

- re.findall( pattern, string, flags=0 )
> - 搜素字符串，以列表方式返回全部能匹配的子串 
