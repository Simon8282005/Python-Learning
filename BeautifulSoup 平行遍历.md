# 第十四天
### **平行遍历**

### .**next_sibling**
- 说明：返回按照 HTML 文本顺序的下一个平行节点

### .**previous_sibling**
- 说明：返回按照 HTML 文本顺序的上一个平行节点

### .**next_siblings**
- 说明：送代类型，返回按照 HTML 文本顺序的后续所有平行节点标签

### .**previous_sibling**
- 说明：送代类型，返回按照 HTML 文本顺序的前续所有平行节点标签

！！！注意，平行遍历必须发生在同一个父节点下，比如这段文本中：
```
<html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello Python XD</h1>
        <p>Just for test</p>
    </body>
</html>
```
`<title>` 和 `<h1>` 之间不是平行遍历，因为它们两个的父标签不一样, 所以我们不能通过 `<title>` 直接获得 `<h1>` 标签。 而`<h1>` 就能直接获得 `<p>` 标签， 因为它们的父节点是一样的

## 列子：
### `soup.a.next_sibling  # 后一个平行节点`

- **Output：** `' and '`

这里我们看到`<a>` 标签的下一个节点是一个字符串， 虽然HTML 是由标签来组织的，但是标签和标签之间的 `NavigableString` 还是可以构成一个节点的。所以我们不能理所当然的认为使用平行遍历的下一个内容一定是标签信息，也有可能是一串字符串类型的信息。

### `soup.a.next_sibling.next_sibling  # 后一个平行节点的后后一个平行节点` 
- **Output**： 
`<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>`

### `soup.a.previous_sibling  # 上一个平行节点`
- **Output：**
`'Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n'`

### `soup.a.previous_sibling.prebious_sibling  # 上一个平行节点的上一个平行节点`、
- **Output: `Null`**

### `soup.a.parent`
**Output**: `<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>`

我们发现`<a>` 节点的父亲节点是一个 `<p>` 节点

### 平行遍历的实现
```
# 遍历后续节点
for sibling in soup.a.next_sibling:
    print(sibling)

# 遍历前续节点
for sibling in soup.a.previous_sibling:
    print(sibling)

```
