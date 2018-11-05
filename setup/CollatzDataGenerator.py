import pandas as pd
import numpy as np

# Interestingly, when using this method of calculating traces and stats
# as need without a database, loading times for the app are comparable
def memoize(func):
  results = {}
  def new_func(x):
    if x not in results:            
      results[x] = func(x)
    return results[x]
  return new_func

@memoize
def collatz(n):
  if n == 1:
    return [1], 1, 1, 0, 1
  if n % 2 == 0:
    trace, steps, largest, evens, odds = collatz(n // 2)
    evens += 1
  else:
    trace, steps, largest, evens, odds = collatz(3 * n + 1)
    odds += 1
  steps += 1
  if n > largest: largest = n
  return [n] + trace, steps, largest, evens, odds

collatz_results = pd.DataFrame([collatz(i) for i in range(2, 10000)])
collatz_results.columns = ['trace', 'steps', 'largest', 'evens', 'odds']
collatz_results['start_number'] = range(2, 10000)
collatz_results = collatz_results.set_index('start_number')

collatz_results.to_csv('../data/collatz.csv')
