import time
from functools import wraps

__all__ = ["run_time"]


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"函数{func.__name__}运行{end - start}")
        return res

    return wrapper


@run_time
def a():
    time.sleep(3)
    return 12121


if __name__ == '__main__':
    print(a())
