import multiprocessing as mp
import time
import logging
from itertools import repeat


logger = mp.log_to_stderr(logging.INFO)

hostlist = ['h1', 'h2', 'h3', 'h4']*3
poolsize = mp.cpu_count()

class HClass:
    def __init__(self, hostname="default"):
        self.hostname = hostname

    def go(self, another_string):
        logger.info('processing {h}'.format(h = self.hostname))
        time.sleep(1)
        return self.hostname + ' ' + another_string

    def go_other(self, another_string):
        time.sleep(1)
        return self.hostname + ' ' + another_string

def worker(host, additional_string):
    h = HClass(hostname = host)
    return h.go(additional_string)

def worker_other(host, additional_string):
    h = HClass(hostname = host)
    return h.go_other(additional_string)

result = []
def on_return(retval):
    result.append(retval)

def main_apply_async():
    print("Using apply_async")
    pls_string = "str concat"
    pool = mp.Pool(poolsize)
    for host in hostlist:
        pool.apply_async(worker, args = (host,pls_string,), callback = on_return)
    pool.close()
    pool.join()
    logger.info(result)

def main_apply():
    print("Using apply")
    pls_string = "str concat"
    pool = mp.Pool(poolsize)
    results = []
    for host in hostlist:
        results.append(pool.apply(worker_other, args = (host,pls_string,)))
    pool.close()
    pool.join()
    print(results)


def main_starmap():
    print("Using starmap")
    pls_string = "str concat"
    pool = mp.Pool(poolsize)
    results_starmap = []
    args = zip(repeat(pls_string), hostlist)
    results_starmap.append(pool.starmap(worker_other, args))
    pool.close()
    pool.join()
    print(results_starmap)

if __name__ == "__main__":
    main_apply_async()
    main_apply()
    main_starmap()