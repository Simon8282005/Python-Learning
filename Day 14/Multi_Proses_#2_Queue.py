import multiprocessing as mp
import time

def job(q):
    result = 0
    for i in range(10000000):
        result = 10 + i**2
    q.put(result)

if __name__ == "__main__":
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join() 
    p2.join()
    print(q.get(p1)+q.get(p2))   
    print("Done !")
    print(time.process_time())