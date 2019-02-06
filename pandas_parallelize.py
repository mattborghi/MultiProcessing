# When working in data analysis or machine learning projects, you might want to parallelize Pandas Dataframes, 
# which are the most commonly used objects (besides numpy arrays) to store tabular data.

# When it comes to parallelizing a DataFrame, you can make the function-to-be-parallelized 
# to take as an input parameter:

# one row of the dataframe
# one column of the dataframe
# the entire dataframe itself

# The first 2 can be done using multiprocessing module itself. 
# But for the last one, that is parallelizing on an entire dataframe, 
# we will use the pathos package that uses dill for serialization internally.

# First, lets create a sample dataframe and see how to do row-wise and column-wise paralleization. 
# Something like using pd.apply() on a user defined function but in parallel.

import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
print(df.head())
#>    0  1
#> 0  8  5
#> 1  5  3
#> 2  3  4
#> 3  4  4
#> 4  7  9

# We have a dataframe. Let’s apply the hypotenuse function on each row, but running 4 processes at a time.

# To do this, we exploit the df.itertuples(name=False). 
# By setting name=False, you are passing each row of the dataframe as a simple tuple to the hypotenuse function.

# Row wise Operation
def hypotenuse(row):
    return round(row[1]**2 + row[2]**2, 2)**0.5

with mp.Pool(4) as pool:
    result = pool.imap(hypotenuse, df.itertuples(name=False), chunksize=10)
    output = [round(x, 2) for x in result]

print(output)
#> [9.43, 5.83, 5.0, 5.66, 11.4]

# That was an example of row-wise parallelization. 
# Let’s also do a column-wise parallelization. 
# For this, I use df.iteritems() to pass an entire column as a series to the sum_of_squares function.

# Column wise Operation
def sum_of_squares(column):
    return sum([i**2 for i in column[1]])

with mp.Pool(2) as pool:
    result = pool.imap(sum_of_squares, df.iteritems(), chunksize=10)
    output = [x for x in result]

print(output) 
#> [163, 147]

# Now comes the third part – Parallelizing a function that accepts a Pandas Dataframe, NumPy Array, etc. 
# Pathos follows the multiprocessing style of: 
# Pool > Map > Close > Join > Clear. Check out the pathos docs for more info.

import numpy as np
import pandas as pd
import multiprocessing as mp
from pathos.multiprocessing import ProcessingPool as Pool

df = pd.DataFrame(np.random.randint(3, 10, size=[500, 2]))

def func(df):
    return df.shape

cores=mp.cpu_count()

df_split = np.array_split(df, cores, axis=0)

# create the multiprocessing pool
pool = Pool(cores)

# process the DataFrame by mapping function to each df across the pool
df_out = np.vstack(pool.map(func, df_split))

# close down the pool and join
pool.close()
pool.join()
pool.clear()