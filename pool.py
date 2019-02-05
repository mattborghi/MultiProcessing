from multiprocessing import Pool
import os
import time


def function(x):
    f = open("10mb.txt", "r")
    for line in f:
        pass
    # print("process: " + str(x))
    return x

if __name__ == '__main__':

    # os.cpu_count()
    processes = [1,2,3,4]
    N = [10,20,30,40,50,60,70,80,90,100]
    lista = [None] * len(processes)
    for index in range(len(processes)):
        lista[index] = [None]*len(N)
        # print(lista)
        with Pool(processes[index]) as p:
            for index_n in range(len(N)):
                start_time = time.clock()
                # print(p.map(function, list(range(10))))
                p.map(function, list(range(N[index_n])))
                total_time = time.clock()-start_time
                lista[index][index_n] = total_time

        # print("Total time with " + str(num_process) + " processes: " + str(total_time))
    import matplotlib.pyplot as plt
    plt.figure()
    with plt.style.context('ggplot'):
        for index_proc in range(len(processes)):
            plt.plot(N,lista[index_proc], label="%s" % processes[index_proc])

        plt.xlabel('# iterations')
        plt.ylabel('Time [s]')
        plt.title("MultiProcessing")
        plt.legend(title="Process", fancybox=True)
        plt.savefig('MultiProcessing.pdf')
