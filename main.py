import string
from threading import Thread
from datetime import datetime
from multiprocessing import Process


def runtime_function(func):
    """
    Decorator for get delta time of function work
    :param func: object of func
    :return:
    """

    def wrapper(*args, **kwargs):
        time_start = datetime.now()
        func(*args, **kwargs)
        time_stop = datetime.now()
        print(time_stop - time_start)

    return wrapper


def genarate_data() -> str:
    """
    Generate string of ASCII symbols
    :return: str of symbols
    """
    return string.ascii_lowercase * 100000000


def write_file(data: str, title: str):
    """
    Write generated data to file
    :param data: str of data
    :return:
    """

    with open(file=f'file_{title}.txt', mode='w', encoding='utf-8') as file:
        file.write(data)


@runtime_function
def task_main(data):
    print('\nTime work with - Main')
    write_file(data=data, title='main')


@runtime_function
def task_thread(data: str):
    print('\nTime work with two task - Threading')
    thread1 = Thread(target=write_file, kwargs={'data': data, 'title': 'thread1'})
    thread2 = Thread(target=write_file, kwargs={'data': data, 'title': 'thread2'})
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


@runtime_function
def task_process(data: str):
    print('\nTime work with two task - Process')
    process1 = Process(target=write_file, kwargs={'data': data, 'title': 'process1'})
    process2 = Process(target=write_file, kwargs={'data': data, 'title': 'process2'})
    process1.start()
    process2.start()
    process1.join()
    process2.join()


def main():
    data = genarate_data()

    task_main(data)
    task_thread(data)
    task_process(data)


if __name__ == '__main__':
    main()
