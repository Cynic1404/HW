import time


def time_this(times):
    def repeat(function_to_decorate):
        def the_wrapper_around_the_original_function():
            t0 = time.time()
            for i in range(times):
                function_to_decorate()
            t1 = time.time()
            print("Выполнение заняло %.5f секунд" % (t1 - t0))
        return the_wrapper_around_the_original_function
    return repeat

# @time_this(100)
# def make_russian(n):
#     if n == 1 or n%10==1:
#         ok = ''
#     elif n%10==0:
#         ok = 'ов'
#     elif n>=2 and n<=4 or n > 20 and (int((str(n))[-1]) >=2 and int((str(n))[-1]) <=4):
#         ok = 'а'
#     elif n>=5 and n<=20 or n > 20 and (int((str(n))[-1]) >=5 and int((str(n))[-1]) <=9):
#         ok = 'ов'
#     print(f'{n} студент{ok}')
#
#
# make_russian()

@time_this(4)
def count():
    p = [i+100 for i in range(100)]
    print(p)

count()



