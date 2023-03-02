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


@runtime_function
def write_file(data: str):
    """
    Write generated data to file
    :param data: str of data
    :return:
    """

    with open(file='file.txt', mode='w', encoding='utf-8') as file:
        file.write(data)


def main():
    data = genarate_data()

    # One task
    print('Time work with one task')
    write_file(data)

    # Two task Threading
    print('\nTime work with two task - Threading')
    thread1 = Thread(target=write_file, args=(data,))
    thread2 = Thread(target=write_file, args=(data,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # Two task Process
    print('\nTime work with two task - Process')
    process1 = Process(target=write_file, args=(data,))
    process2 = Process(target=write_file, args=(data,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


if __name__ == '__main__':
    main()
