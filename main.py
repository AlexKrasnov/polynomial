import os
import math
from multiprocessing import Process, current_process

from polynomial import Polynomial

p = Polynomial([1, 0, 4])
p.print()
print(p.solve())


# def substitute(P, number):
#     """
#     Функция вычислить значение полинома
#     """
#     result = P.substitute_number(number)
#     #process = os.getpid()
#     process_name = current_process().name
#     print('x = {0}, P(x) = {1} by process id: {2}'.format(number, result, process_name))
#
#
# if __name__ == '__main__':
#     numbers = [5, 10, 15, 20, 25]
#     processes = []
#
#     for index, number in enumerate(numbers):
#         process = Process(target=substitute, args=(A, number,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()