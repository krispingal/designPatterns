from time import perf_counter


def log(func):

    def wrapper_func(*args, **kwargs):
        print(f'{func.__name__} invoked with args {args}')
        start_time = perf_counter()
        res = func(*args, **kwargs)
        finish_time = perf_counter()
        print(f'{func.__name__} completed in {finish_time - start_time:.8f} s')
        return res
    return wrapper_func

@log
def fibonacci(n):
    if n < 2: return n
    prev, pprev = 1, 1
    for i in range(n - 2):
        prev, pprev = prev + pprev, prev
    return prev


if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(7) == 13
    assert fibonacci(19) == 4181

