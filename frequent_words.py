import timeit

# def find_duplicates(arr):
#   new_arr = []
#   for word in arr:
#     if word not in new_arr:
#       new_arr.append(word)
#     else:
#       print(word)

def frequent_words(arr):
  new_dic = {}
  for word in arr:
    if word not in new_dic:
      new_dic.update({word: 1})
    else:
      new_dic[word] += 1
  for word in new_dic:
    if new_dic.get(word) > 1:
      print(f'{word} : {new_dic.get(word)}')
