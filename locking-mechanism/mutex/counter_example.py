import threading
import time
counter = 0
lock = threading.Lock()
def main():
    try:
        thread1 = threading.Thread(target=utility_function, args=("thread-1",))
        thread2 = threading.Thread(target=utility_function, args=("thread-2",))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
    except Exception as e:
        print(f"Message: {e}")

def utility_function(name):
    global counter
    try:
        for i in range(5):
            # lock.acquire()
            print(f"{name} => reading counter: {counter}")
            time.sleep(0.1)
            counter += 1
            print(f"{name} => updated counter: {counter}")
            # lock.release()
            time.sleep(0.1)
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()