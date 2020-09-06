apple = 100
a = None
def fun():
    global a
    a = apple # apple = 100
    return a+100

print(fun())
print(a)
