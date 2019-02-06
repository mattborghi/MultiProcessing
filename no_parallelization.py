import numpy as np
import time 

# Solution Without Paralleization
class Function:
	def __init__(self):
		# Prepare data
		np.random.RandomState(100)
		arr = np.random.randint(0, 10, size=[200000, 5])
		self.data = arr.tolist()
		self.data[:5]

	def howmany_within_range(self,row, minimum, maximum):
	    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
	    count = 0
	    for n in row:
	        if minimum <= n <= maximum:
	            count = count + 1
	    return count

def main():
	results = []
	a = Function()
	for row in a.data:
	    results.append(a.howmany_within_range(row, minimum=4, maximum=8))

	print(results[:10])
	#> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

if __name__ == '__main__':
	start_time = time.time()
	main()
	final_time = time.time() - start_time
	print("Lasted %0.4f seconds" % final_time)