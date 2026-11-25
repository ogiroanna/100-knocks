str = 'stressed'
result = ''

for i in range(len(str)):
  result += str[(len(str) - 1) - i]

print(result)
