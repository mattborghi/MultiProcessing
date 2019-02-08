from multiprocessing import Pool
import os
import time
from itertools import product

def function(x, y):
    f = open("10mb.txt", "r")
    for line in f:
        pass
    # print("job: " + str(x) + " " + str(y))
    return x*y

if __name__ == '__main__':

    # os.cpu_count()
    processes = [1,2,3,4]
    N = [10,20,30,40,50]
    M = [1]
    array_of_tuple =  [(n,m) for m in M for i in N for n in range(i)]
    lista = [None] * len(processes)
    for index in range(len(processes)):
        print("Current process: " + str(processes[index]))
        lista[index] = [None]*len(array_of_tuple)
        # print(lista)
        with Pool(processes[index]) as p:
            for index_var in range(len(array_of_tuple)):
                start_time = time.clock()
                # print(p.map(function, list(range(10))))
                # (list(range(N[index_n]))
                p.starmap(function, array_of_tuple)
                total_time = time.clock()-start_time
                # lista[index] = total_time
                lista[index][index_var] = total_time

        # print("Total time with " + str(processes[index]) + " processes: " + str(total_time))
    import matplotlib.pyplot as plt
    plt.figure()
    with plt.style.context('ggplot'):
        for index_proc in range(len(processes)):
            plt.plot(N,lista[index_proc], label="%s" % processes[index_proc])

        plt.xlabel('# iterations')
        plt.ylabel('Time [s]')
        plt.title("MultiProcessing - Starmap method")
        plt.legend(title="Process", fancybox=True)
        plt.savefig('starmap.pdf')
