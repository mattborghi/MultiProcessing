# Like Pool.map(), Pool.starmap() also accepts only one iterable as argument, 
# but in starmap(), each element in that iterable is also a iterable. 
# You can to provide the arguments to the ‘function-to-be-parallelized’ 
# in the same order in this inner iterable element, will in turn be unpacked during execution.

# So effectively, Pool.starmap() is like a version of Pool.map() that accepts arguments.

# Parallelizing with Pool.starmap()
import multiprocessing as mp
import time
from no_parallelization import Function


def main():
	a = Function()

	pool = mp.Pool(mp.cpu_count())

	results = pool.starmap(a.howmany_within_range, [(row, 4, 8) for row in a.data])

	pool.close()

	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)