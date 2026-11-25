sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
result = {}

sentence = sentence.replace(',', '')
sentence = sentence.replace('.', '')
word_list = sentence.split(' ')

for i in range(len(word_list)):
  if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
    result[word_list[i][0]] = i + 1
  else:
    result[word_list[i][0:2]] = i + 1

print(result)
