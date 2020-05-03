import time

def time_this(times_to_repeat=10):
    def wraper(function_to_decorate):
        def parameters(*args):
            avg_time = 0
            for _ in range(times_to_repeat):
                t0 = time.time()
                function_to_decorate(*args)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= times_to_repeat
            print("Функция выполнена %s раз. \nСреднее время выполнения - %.5f секунд" % (times_to_repeat, (t1 - t0)))
        return parameters
    return wraper


@time_this(15)
def f_with_parameters(n):
    for j in range(n):
        pass

f_with_parameters(1000)


@time_this()
def f_no_parameters():
    for j in range(10000):
        pass
f_no_parameters()