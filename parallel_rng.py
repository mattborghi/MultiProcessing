from numpy import random 

from randomgen import RandomGenerator 
import time

def calculate(func):
	start_time = time.time()
	for i in range(10000):
		exec(func)
	print("Lasted %0.4f seconds using %s" % ((time.time()-start_time), func))

if __name__ == '__main__':
	# Default basic PRNG is Xoroshiro128
	rnd = RandomGenerator()
	calculate("rnd.standard_normal()")
	calculate("random.normal()")