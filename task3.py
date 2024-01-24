import timeit

from method_BM import build_shift_table, boyer_moore_search
from method_KMP import compute_lps, kmp_search
from method_RK import polynomial_hash, rabin_karp_search

def read_file(filename):
    with open(filename, 'r', encoding = 'cp1251') as f:
        return f.read()
    
def compare(func, text, pattern):
    setup = f"from __main__ import {func.__name__}"
    condition = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt = condition, setup = setup, number = 10, globals = {'text': text, 'pattern': pattern })

def output(text,real_pattern,fake_pattern ):
    
    results = []

    for pattern in (real_pattern, fake_pattern):
        time = compare(boyer_moore_search, text, pattern)
        results.append((boyer_moore_search.__name__,pattern,time))
        time = compare(kmp_search, text, pattern)
        results.append((kmp_search.__name__,pattern,time))
        time = compare(kmp_search, text, pattern)
        results.append((rabin_karp_search.__name__,pattern,time))
    
    
    title = f"{'Алгоритм': <30} | {'Підрядок': <30} | {'Час виконання, сек'}"
    print('-' * len(title))
    print(title)
    print('-' * len(title))
    for result in results:
        print(f"{result[0]: <30} | {result[1]: <30} | {result[2]: <30}")
    print('-' * len(title))

    
if __name__ == '__main__':

    real_pattern = 'алгоритм'
    fake_pattern = 'мама мила раму'
      
    text = read_file('article_1.txt')
    print('article_1.txt')
    output(text,real_pattern,fake_pattern)

    text = read_file('article_2.txt')
    print('article_2.txt')
    output(text,real_pattern,fake_pattern)

