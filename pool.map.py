# Pool.map() accepts only one iterable as argument. 
# So as a workaround, I modify the howmany_within_range function 
# by setting a default to the minimum and maximum parameters to create 
# a new howmany_within_range_rowonly() function so it accetps only an 
# iterable list of rows as input. 
# I know this is not a nice usecase of map(), 
# but it clearly shows how it differs from apply().

# Parallelizing using Pool.map()
import multiprocessing as mp
import time
from no_parallelization import Function

class ModifFunction:
	# Redefine, with only 1 mandatory argument.
	@staticmethod
	def howmany_within_range_rowonly(row, minimum=4, maximum=8):
	    count = 0
	    for n in row:
	        if minimum <= n <= maximum:
	            count = count + 1
	    return count

def main():
	a = Function()
	pool = mp.Pool(mp.cpu_count())

	results = pool.map(ModifFunction.howmany_within_range_rowonly, [row for row in a.data])

	pool.close()

	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)

