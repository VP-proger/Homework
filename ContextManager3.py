import time


class CacheManager:
    cache = {}

    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def compute(self, func, *args, **kwargs):
        start_time = time.time()
        key = f'{func}:{sorted(args)}:{sorted(kwargs)}'
        result = None
        if key in CacheManager.cache:
            result = CacheManager.cache[key]
        else:
            result = func(*args, **kwargs)
            CacheManager.cache[key] = result
        end_time = time.time()
        return result, end_time - start_time


def factorial(n):
    time.sleep(1)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


with CacheManager() as cache:
    print(cache.compute(factorial, 5))

with CacheManager() as cache:
    print(cache.compute(factorial, 5))