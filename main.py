import threading
import random
import time
import os


class Thread(threading.Thread):
    def __init__(self, priority, name):
        threading.Thread.__init__(self)
        self.name = f"Thread_{name}"
        self.priority = priority
        self.active = True

    def run(self):
        while self.active:
            with open(f"data/{self.name}.txt", "a") as file:
                file.write("1")


class Threads(object):
    def __init__(self):
        self.one_time_array = []  # массив времени каждого потока
        self.sum_time = 0  # сумма всего времени

    def start(self):
        threads = []  # список со всеми потоками
        priority = [random.randint(1, 10) for _ in range(10)]
        print(priority)
        min_priority = max(priority)
        for name, prior in enumerate(priority):
            thread = Thread(prior, str(name))

            threads.append(thread)

        threads = sorted(threads, key=lambda thread: thread.priority)

        time_out = {}  # {'1': [thread1, thread2],}
        for thread in threads:
            count = time_out.get(thread.priority)
            if count is None:
                time_out.update({thread.priority: [thread]})
            else:
                threads_ = time_out.get(thread.priority)
                threads_.append(thread)
                time_out.update({thread.priority: threads_})

        all_time = 60
        for key, value in sorted(time_out.items()):
            one_time = all_time / len(value)  # все время/кол-потоков 1 приоритета
            start_time = time.time()
            for thread in value:
                if thread.priority != min_priority:
                    thread.start()
                    self.sum_time += one_time
                    self.one_time_array.append(one_time)
                else:
                    self.one_time_array.append(0)

            print(one_time)
            if value[0].priority != min_priority:  # !
                value[0].join(one_time)
                end_time = time.time()
                print(end_time - start_time)
                for thread in value:
                    thread.active = False

                for thread in value:
                    thread.priority = min_priority
        if self.sum_time:
            self.run()
            print("6 сек +- 1 сек на каждый поток")
        else:
            print("Все потоки с минимальным приоритетом")

    def run(self):
        flag = False
        while True:
            array = []
            for i, one in enumerate(self.one_time_array):
                if flag:
                    if _sum == 0:
                        x = [0.1] * 10
                        print(x)
                        return
                    self.one_time_array[i] += x[i] / _sum * 60
                if one:
                    array.append(1 - self.one_time_array[i] / self.sum_time)
                else:
                    if not flag:
                        array.append(0)
                    else:
                        array.append(1 - self.one_time_array[i] / self.sum_time)

            flag = True
            _sum = sum(array)
            x = []
            for value in array:
                if value == 0:
                    x.append(_sum)
                else:
                    x.append(value / _sum)

            # print("x: ", x)
            print("sum: ", _sum)
            self.sum_time += 60
            _break = 0
            for value in x:
                if _sum != 0:
                    if 5 <= (value / _sum) * 600 <= 7:
                        _break += 1
            if _break == len(x):
                print(x)
                return


if __name__ == "__main__":
    if not os.path.exists('data'):
        os.mkdir('data')
    Threads().start()
