import threading

lock_a=threading.Lock()
lock_b=threading.Lock()

def task1():
    with lock_a:
        print(f"Task1 acquired Lock A")
        with lock_b:
            print(f"Task1 acquired Lock B")


def task2():
    with lock_b:
        print(f"Task1 acquired Lock B")
        with lock_a:
            print(f"Task1 acquired Lock A")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()
