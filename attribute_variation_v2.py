import multiprocessing as mp
import time
import logging

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

def worker(host, additional_string):
    h = HClass(hostname = host)
    return h.go(additional_string)

result = []
def on_return(retval):
    result.append(retval)

if __name__ == "__main__":
    pls_string = "str concat"
    pool = mp.Pool(poolsize)
    for host in hostlist:
        pool.apply_async(worker, args = (host,pls_string,), callback = on_return)
    pool.close()
    pool.join()
    logger.info(result)