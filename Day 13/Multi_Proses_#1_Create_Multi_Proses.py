'''
创建一个进程
'''

import multiprocessing as mp
#import threading as td

# 创建一个线程和进程是差不多一样的 XD
def job(a, b):
    print("Hello XD")
    print(a+b)

if __name__ == "__main__":
    # 线程
    #t1 = td.Thread(target=job, args=(1, 2))   # 如果是job的话是引用，job()的话是调用
    # 进程
    p1 = mp.Process(target=job, args=(1, 2))

    # 线程开始
    #t1.start()
    # 进程开始
    p1.start()

    # 线程join
    #t1.join()
    # 进程join
    p1.join()