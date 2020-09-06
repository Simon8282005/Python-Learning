'''
（Queue）线程的返回值
因为线程是不能用return来返回值的，所以要使用到Queue来得到返回值
'''

import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)

# 主要部分
def multithreading():
    q = Queue()  # 定义一个Queue的物体以便用来存放线程的返回值
    threads = []  # 定义一个threads的列表来存放所有Queue物体
    data = [[1, 2, 3],[3, 4, 5],[4, 4, 4],[5, 5, 5]]
    
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i],q))  # args=() 是要被回传的参数
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()
    
    results = []  # 定义一个results列表，用来存放全部Queue的返回值
    
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__ == '__main__':
    multithreading()