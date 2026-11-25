word1 = 'パトカー'
word2 = 'タクシー'
result = ''

word1_list = list(word1)
word2_list = list(word2)

for i in range(4):
  result += word1_list[i] + word2_list[i]

print(result)
