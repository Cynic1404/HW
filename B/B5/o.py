import time


def time_this_two_parameters(times_to_repeat):
    def wraper(function_to_decorate):
        def parameters(param, param2):
            t0 = time.time()
            for i in range(times_to_repeat):
                function_to_decorate(param, param2)
            t1 = time.time()
            print("Выполнение заняло %.5f секунд" % (t1 - t0))
        return parameters
    return wraper


def time_this_one_parameter(times_to_repeat):
    def wraper(function_to_decorate):
        def parameters(param):
            avg_time = 0
            for _ in range(times_to_repeat):
                t0 = time.time()
                function_to_decorate(param)
                for j in range(1000000):
                    pass
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= times_to_repeat
            print("Выполнение заняло %.5f секунд" % avg_time)
        return parameters
    return wraper

def time_this(times_to_repeat):
    def wraper(function_to_decorate):
        def the_wrapper_around_the_original_function():
            avg_time = 0
            for _ in range(times_to_repeat):
                t0 = time.time()
                function_to_decorate()
                for j in range(1000000):
                    pass
                t1 = time.time()
                avg_time += (t1 - t0)
                print(avg_time)
            avg_time /= times_to_repeat
            print("Выполнение заняло %.5f секунд" % avg_time)
        return the_wrapper_around_the_original_function
    return wraper


def time_this_args_parameters(times_to_repeat):
    def wraper(function_to_decorate):
        def parameters(*args):
            avg_time = 0
            for _ in range(times_to_repeat):
                t0 = time.time()
                function_to_decorate(*args)
                for j in range(1000000):
                    pass
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= times_to_repeat
            print("Выполнение заняло %.5f секунд" % avg_time)
        return parameters
    return wraper


# @time_this_args_parameters(100)
# def count(*args):
#     res = 0
#     for i in args:
#         res+=i
#     return res
#
# count(1,2,3,4,5)
#
# @time_this_args_parameters(100)
# def na():
#     return 1080
#
# na()

@time_this_args_parameters(10)
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print(a)
        return a
    elif n == 1:
        print(b)
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        print(b)
        return b

# fibonacci(1)
# fibonacci(2)
# fibonacci(3)
# fibonacci(4)
# fibonacci(5)
fibonacci(190000)
