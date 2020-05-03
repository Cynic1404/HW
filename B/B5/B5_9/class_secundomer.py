import time


class Timer:
    def __init__(self, function_to_decorate, times_to_repeat=100):
        self.times_to_repeat = times_to_repeat
        self.function_to_decorate = function_to_decorate


    def __call__(self, *args):
        avg_time = 0
        for _ in range(self.times_to_repeat):
            t0 = time.time()
            self.function_to_decorate(*args)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.times_to_repeat
        print("Функция выполнена %s раз. \nСреднее время выполнения - %.5f секунд" % (self.times_to_repeat, (t1 - t0)))


@Timer
def f_with_parameters(n):
    for j in range(n):
        pass

f_with_parameters(1000000)

