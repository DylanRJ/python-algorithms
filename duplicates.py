import timeit

def find_duplicates(arr):
  new_arr = []
  for word in arr:
    if word not in new_arr:
      new_arr.append(word)
    else:
      print(word)

print(timeit.timeit(setup="from __main__ import find_duplicates", stmt="assert find_duplicates(['Okay', 'this', 'is', 'a', 'string']) == None"))
print(timeit.timeit(setup="from __main__ import find_duplicates", stmt="assert find_duplicates(['Okay', 'this', 'is', 'a', 'string', 'Okay']) == Okay"))