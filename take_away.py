from itertools import product
from itertools import repeat
import multiprocessing as mp
import sys

API_LINK = ""
AUTH_STRING = 0

class TakeAway:
	@staticmethod
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

	@staticmethod
	def _recursive_lookup(key_name, list_dictionary, value_to_replace):
		for k,v in list_dictionary.items():
			#print("Looking in dictionary: %s" % dictionary)
			if key_name in v:
				v[key_name] = value_to_replace
				return
			for value in v.values():
				if isinstance(value, dict):
					return TakeAway._recursive_lookup(key_name, value, value_to_replace)
		sys.exit('There was an error with dictionary key: %s' % key_name)

	@staticmethod
	def main(headers, payload, **kwargs):
		lookup_dict = ['headers', 'payload']
		default_dict = {'payload':payload.copy(),'headers':headers.copy()}

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
				TakeAway._recursive_lookup(names[index_name], default_dict, variations[index_variation][index_name])
			#print("end of inner loop")
			list_dictionary[index_variation] = (payload.copy(),headers.copy())

			payload_var[index_variation] = (payload.copy())
			headers_var[index_variation] = (headers.copy())

		#print(type(headers_var))
		#print(payload)
		#for lista in list_dictionary:
		#	print(lista)

		# Then you can call it in your case as:
		project_name = 'project_name'
		api_extensions = 'asd' #['asd','ijk','lmn','opq']
		key = True
		pool = mp.Pool(mp.cpu_count())
		
		args_iter = zip(repeat(project_name),repeat(api_extensions),payload_var,headers_var,repeat(key))
		#(dict(project_name=project_name,api_extensions=elem,headers=headers) for elem in api_extensions)
		#zip(repeat(project_name), api_extensions)
		#for elem in list(args_iter):
		#	print(elem)
		
		return pool.starmap(TakeAway.fetch_api, args_iter)
		