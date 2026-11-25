def char_bigram(text):
  bi_grams = []
  for i in range(len(text) - 1):
    bi_grams.append(text[i : i + 2])
  return set(bi_grams)


X = char_bigram('paraparaparadise')
Y = char_bigram('paragraph')

union_set = X | Y
intersection_set = X & Y
diff_set = X - Y

print('X:', X)
print('Y:', Y)
print('和集合（X∨Y）:', union_set)
print('積集合（X∧Y）:', intersection_set)
print('差集合 (X-Y):', diff_set)
print("'se' は X に含まれるか:", 'se' in X)
print("'se' は Y に含まれるか:", 'se' in Y)
