# It is possible to use apply_async() without providing a callback function. 
# Only that, if you don’t provide a callback, then you get a list of pool.ApplyResult 
# objects which contains the computed output values from each process. 
# From this, you need to use the pool.ApplyResult.get() method to retrieve the desired final result.

# Parallel processing with Pool.apply_async() without callback function

import multiprocessing as mp
import time
from no_parallelization import Function

class AsyncClass:
	# Step 1: Redefine, to accept `i`, the iteration number
	@staticmethod
	def howmany_within_range2(i, row, minimum, maximum):
	    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
	    count = 0
	    for n in row:
	        if minimum <= n <= maximum:
	            count = count + 1
	    return (i, count)

def main():
	# Load data
	a = Function()

	pool = mp.Pool(mp.cpu_count())

	results = []

	# Step 3: Use loop to parallelize
	# call apply_async() without callback
	result_objects = [pool.apply_async(AsyncClass.howmany_within_range2, 
					  args=(i, row, 4, 8)) for i, row in enumerate(a.data)]

	# result_objects is a list of pool.ApplyResult objects
	results = [r.get()[1] for r in result_objects]

	# Step 4: Close Pool and let all the processes complete    
	pool.close()
	pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]


if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)