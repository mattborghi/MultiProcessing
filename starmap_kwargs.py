from itertools import repeat
import multiprocessing as mp
API_LINK = ""
AUTH_STRING = 0
def fetch_api(project_name, api_extension, payload={}, headers={}, API_LINK=API_LINK, key=False):
	#print('sth')
	headers[AUTH_STRING] = 'Gogo'
	call_api = API_LINK + project_name + api_extension
	# response_api = requests.get(call_api, headers=headers, params=payload)
	response_api = 'holaa'

	if key: return project_name + ':' + response_api
	else: return response_api

def starmap_with_kwargs(pool, fn, args_iter, kwargs_iter):
	args_for_starmap = zip(repeat(fn), args_iter, kwargs_iter)
	# If we uncomment this printing lines the program will not parallelize
	#for elem in list(args_for_starmap):
	#	print(elem)
	return pool.starmap(apply_args_and_kwargs, args_for_starmap)

def apply_args_and_kwargs(fn, args, kwargs):
	return fn(*args, **kwargs)

def main():

	# Then you can call it in your case as:
	project_name = 'project_name'
	api_extensions = ['asd','ijk','lmn','opq']
	pool = mp.Pool(4)
	args_iter = ((project_name,elem) for elem in api_extensions) #zip(repeat(project_name), api_extensions)
	kwargs_iter = repeat(dict(payload={'a': 1}, key=True))
	branches = starmap_with_kwargs(pool, fetch_api, args_iter, kwargs_iter)
	print(branches)

if __name__ == '__main__':
	main()