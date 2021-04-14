import datetime
import math
import multiprocessing
import threading


def main():
    num = 30_000_000
    cpu_count = multiprocessing.cpu_count()

    results = []
    threads = [threading.Thread(
        target=lambda r, *args: r.append(do_math(*args)),
        args=(results, num * (n - 1) / cpu_count, num * n / cpu_count)
    ) for n in range(1, cpu_count + 1)]

    t_start = datetime.datetime.now()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    dt = datetime.datetime.now() - t_start
    print(f'Multithreading done in {dt.total_seconds():.2f} s')
    print(f'{(sum(results) / len(results)):.2f}')

    t_start = datetime.datetime.now()
    result = do_math(num=num)
    dt = datetime.datetime.now() - t_start
    print(f'Single done in {dt.total_seconds():.2f} s')
    print(f'{result:.2f}')

    pool = multiprocessing.Pool()
    tasks = [pool.apply_async(
        do_math,
        args=(num * (n - 1) / cpu_count, num * n / cpu_count)
    ) for n in range(1, cpu_count + 1)]

    t_start = datetime.datetime.now()
    pool.close()
    pool.join()
    dt = datetime.datetime.now() - t_start
    print(f'Multiprocessing done in {dt.total_seconds():.2f} s')
    print(f'{(sum(task.get() for task in tasks) / len(tasks)):.2f}')


def do_math(start=0, num=10):
    pos = start
    k_sq = 1000 * 1000
    summ = 0
    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) ** 2)
        summ += val

    return summ / (num - start)


if __name__ == '__main__':
    main()
