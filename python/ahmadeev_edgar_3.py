import time
def maximum(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        max_freq_word = ''
        max_freq = 0
        for key in res:
            if res[key] > max_freq:
                max_freq = res[key]
                max_freq_word = key
        print(f'Word "{max_freq_word}" is used {max_freq} times')
        return res

    return wrapper


def memoize(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        consumed = time.time() - start
        print(f'Took {consumed} seconds')
        return res
    return wrapper


@time_it
@maximum
@memoize
def calculate_words(string):
    words = str.split(str.lower(string), ' ')
    words_freq = {}
    for word in words:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1
    return words_freq


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    sentence = 'Never gonna give you up Never gonna let you down Never gonna run around'
    sentence1 = 'Never gonna give you up Never gonna let you down Never gonna run'
    sentence2 = 'Never gonna give you up Never gonna let you down Never gonna'
    sentence3 = 'Never gonna give you up Never gonna let you down gonna run'
    print('*******************************')
    print(calculate_words(sentence))
    print('*******************************')
    print(calculate_words(sentence))
    print('*******************************')
    print(calculate_words(sentence1))
    print('*******************************')
    print(calculate_words(sentence2))
    print('*******************************')
    print(calculate_words(sentence3))
