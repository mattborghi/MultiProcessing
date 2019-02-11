# This version ensures all arguments are passed as args
from itertools import repeat
import multiprocessing as mp
import numpy as np
import sys
from itertools import product

API_LINK = ""
headers = {'s0': 'Gago', 1:'Other'}
AUTH_STRING = 0
payload = {'k': 90}

def fetch_api(project_name, api_extension, payload, headers, key): 
	#print('sth')
	#headers[AUTH_STRING] = 'Gogo'
	call_api = API_LINK + project_name + api_extension#kwargs[0] + kwargs[1]#
	# response_api = requests.get(call_api, headers=headers, params=payload)
	response_api = 'holaa'

	if key: 
		print(headers, payload)
		print('\n')
		return project_name + ':' + response_api
	else: return response_api

def _recursive_lookup(key_name, list_dictionary, value_to_replace):
	for dictionary in list_dictionary:
		#print("Looking in dictionary: %s" % dictionary)
		if key_name in eval(dictionary):
			exec(dictionary+"[key_name] = value_to_replace")
			return
		for value in eval(dictionary).values():
			if isinstance(value, dict):
				return OneDimension._recursive_lookup(key_name, value, value_to_replace)
	sys.exit('There was an error with dictionary key: %s' % key_name)

def main(**kwargs):
	lookup_dict = ['headers', 'payload']
	# Generate variations
	variations = list(product(*kwargs.values()))
	names = [key for key, value in kwargs.items()]
	#print(list(variations))
	#print(list(names))
	# Replace kwargs in dictionaries
	list_dictionary = [None]*len(variations)
	payload_var = [None]*len(variations)
	headers_var = [None]*len(variations)

	for index_variation in range(len(variations)):
		for index_name in range(len(names)):
			#print(names[index_name], variations[index_variation][index_name])
			_recursive_lookup(names[index_name], lookup_dict, variations[index_variation][index_name])
		#print("end of inner loop")
		list_dictionary[index_variation] = (payload.copy(),headers.copy())

		payload_var[index_variation] = (payload.copy())
		headers_var[index_variation] = (headers.copy())

	print(type(headers_var))
	#print(payload)
	#for lista in list_dictionary:
	#	print(lista)

	# Then you can call it in your case as:
	project_name = 'project_name'
	api_extensions = 'asd' #['asd','ijk','lmn','opq']
	key = True
	pool = mp.Pool(mp.cpu_count())
	
	args_iter = zip(repeat(project_name),repeat(api_extensions),payload_var,headers_var,repeat(key))#(dict(project_name=project_name,api_extensions=elem,headers=headers) for elem in api_extensions) #zip(repeat(project_name), api_extensions)
	#for elem in list(args_iter):
	#	print(elem)
	
	return pool.starmap(fetch_api, args_iter)
	

if __name__ == '__main__':
	s0 = np.linspace(50, 250, 4)
	k = np.linspace(100, 120, 2)

	branches = main(s0=s0, k=k)
	print(branches)