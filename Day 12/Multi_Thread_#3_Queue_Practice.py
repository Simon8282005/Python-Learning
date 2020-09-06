import threading
from queue import Queue

def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)
    
# Main
def multithreading():
    q = Queue()
    threads = []
    data =[[1, 2, 3],[3, 4, 5],[5, 5, 5],[6, 6, 6]]

    # Open new thread
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)

    # Join this thread to main thread
    for thread in threads:
        thread.join()

    result = []

    for _ in range(4):
        result.append(q.get())
    print(result)

    print(threading.currentThread())

if __name__ == '__main__':
    multithreading()