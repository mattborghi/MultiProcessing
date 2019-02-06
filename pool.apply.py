# multiprocessing.Pool() provides the apply(), map() and starmap() methods to make any function run in parallel.

# So what’s the difference between apply() and map()?

# Both apply and map take the function to be parallelized as the main argument. 
# But the difference is, apply() takes an args argument that accepts the parameters 
# passed to the ‘function-to-be-parallelized’ as an argument, whereas, 
# map can take only one iterable as an argument.

# Parallelizing using Pool.apply()

import multiprocessing as mp
from no_parallelization import Function
import time


def main():
	# Call instance of Function
	a = Function()
	# Step 1: Init multiprocessing.Pool()
	pool = mp.Pool(mp.cpu_count())

	# Step 2: `pool.apply` the `howmany_within_range()`
	results = [pool.apply(a.howmany_within_range, args=(row, 4, 8)) for row in a.data]

	# Step 3: Don't forget to close
	pool.close()    

	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)
	