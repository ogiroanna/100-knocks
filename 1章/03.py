sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
result = []

sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')
word_list = sentence.split(' ')

for word in word_list:
  result.append(len(word))

print(result)
