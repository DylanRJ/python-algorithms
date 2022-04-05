# from timeit import Timer
import timeit

def reverse_arr(arr):
  new_arr = []
  count = len(arr)
  i = 0
  while i < count:
    new_arr.append(arr[count-1])
    count -= 1
  return new_arr

# t = Timer("reverse_arr()", "from __main__ import reverse_arr")
# print(t.timeit())

print(timeit.timeit(setup="from __main__ import reverse_arr", stmt="assert reverse_arr(['Reverse', 'this', 'array', 'please']) == ['please', 'array', 'this', 'Reverse']"))
print(timeit.timeit(setup="from __main__ import reverse_arr", stmt="assert len(reverse_arr(['Reverse', 'this', 'array', 'please'])) == 4"))
print(timeit.timeit(setup="from __main__ import reverse_arr", stmt="assert reverse_arr(['OMG', 'this', 'method', 'is', 'working', '=', 'Reverse', 'this', 'array', 'please']) == ['please', 'array', 'this', 'Reverse', '=', 'working', 'is', 'method', 'this', 'OMG']"))