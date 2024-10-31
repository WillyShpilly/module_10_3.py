from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            value = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')



# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def increment(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter += 1
#         print(name, counter)
#     lock.release()
#
#
# def decrement(name):
#     global counter
#     lock.acquire()
#     for i in range(1000):
#         counter -= 1
#         print(name, counter)
#     lock.release()
#
# thread1 = threading.Thread(target=increment, args=('thread1',))
# thread2 = threading.Thread(target=decrement, args=('thread2',))
# thread3 = threading.Thread(target=increment, args=('thread1',))
# thread4 = threading.Thread(target=decrement, args=('thread1',))
# thread1.start()
# thread3.start()
# thread2.start()
# thread4.start()

# import threading
#
# counter = 0
# lock = threading.Lock()
#
# def increment(name):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter += 1
#             print(name, counter)
#
#
# def decrement(name):
#     global counter
#     with lock:
#         for i in range(1000):
#             counter -= 1
#             print(name, counter)
#
# thread1 = threading.Thread(target=increment, args=('thread1',))
# thread2 = threading.Thread(target=decrement, args=('thread2',))
# thread3 = threading.Thread(target=increment, args=('thread1',))
# thread4 = threading.Thread(target=decrement, args=('thread1',))
# thread1.start()
# thread3.start()
# thread2.start()
# thread4.start()