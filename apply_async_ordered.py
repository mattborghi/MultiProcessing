# apply_async() is very similar to apply() except that you need to 
# provide a callback function that tells how the computed results should be stored.

# However, a caveat with apply_async() is, 
# the order of numbers in the result gets jumbled up indicating the processes 
# did not complete in the order it was started.

# A workaround for this is, we redefine a new howmany_within_range2() 
# to accept and return the iteration number (i) as well and then sort the final results.

# Parallel processing with Pool.apply_async()

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


	# Step 2: Define callback function to collect the output in `results`
	@staticmethod
	def collect_result(result):
	    #global results
	    results.append(result)


def main():
	# Load data
	a = Function()

	pool = mp.Pool(mp.cpu_count())

	global results
	results = []

	# Step 3: Use loop to parallelize
	for i, row in enumerate(a.data):
	    pool.apply_async(AsyncClass.howmany_within_range2, args=(i, row, 4, 8), 
	    				 callback=AsyncClass.collect_result)

	# Step 4: Close Pool and let all the processes complete    
	pool.close()
	pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

	# Step 5: Sort results [OPTIONAL]
	results.sort(key=lambda x: x[0])
	results_final = [r for i, r in results]

	print(results_final[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]



if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)