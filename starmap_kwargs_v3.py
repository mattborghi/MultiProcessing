# This version ensures all arguments are passed as args
import numpy as np


from take_away import TakeAway

headers = {'s0': 'Gago', 1:'Other'}
payload = {'k': 90}

if __name__ == '__main__':
	s0 = np.linspace(50, 250, 4)
	k = np.linspace(100, 120, 2)

	branches = TakeAway.main(headers, payload, s0=s0, k=k)
	print(branches)