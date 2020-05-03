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
            t0 = time.time()
            for i in range(times_to_repeat):
                function_to_decorate(param)
            t1 = time.time()
            print("Выполнение заняло %.5f секунд" % (t1 - t0))
        return parameters
    return wraper

def time_this(times_to_repeat):
    def wraper(function_to_decorate):
        def the_wrapper_around_the_original_function():
            t0 = time.time()
            for i in range(times_to_repeat):
                function_to_decorate()
            t1 = time.time()
            print("Выполнение заняло %.5f секунд" % (t1 - t0))
        return the_wrapper_around_the_original_function
    return wraper


def time_this_args_parameters(times_to_repeat):
    def wraper(function_to_decorate):
        def parameters(*args):
            t0 = time.time()
            for i in range(times_to_repeat):
                function_to_decorate(*args)
            t1 = time.time()
            print("Выполнение заняло %.5f секунд" % (t1 - t0))
        return parameters
    return wraper


@time_this_args_parameters(6)
def count(*args):
    res = 0
    for i in args:
        res+=i
    print(res)

count(1,2,3,4,5)