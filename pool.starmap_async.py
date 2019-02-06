# Parallelizing with Pool.starmap_async()

import multiprocessing as mp
import time
from apply_async_unordered import AsyncClass
from no_parallelization import Function


def main():
	# Load Data
	a = Function()

	pool = mp.Pool(mp.cpu_count())

	results = []

	results = pool.starmap_async(AsyncClass.howmany_within_range2, [(i, row, 4, 8) 
								 for i, row in enumerate(a.data)]).get()

	# With map, use `howmany_within_range_rowonly` instead
	# results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()

	pool.close()

	results = [elem[1] for elem in results]
	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)