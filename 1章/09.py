import random

def typoglycemia(sentence):
  words = sentence.split(' ')
  result_words = []

  for word in words:
    if len(word) <= 4:
      result_words.append(word)
    else:
      first_char = word[0]
      last_char = word[-1]
      middle_chars = list(word[1:-1])
      random.shuffle(middle_chars)
      shuffled_word = first_char + ''.join(middle_chars) + last_char
      result_words.append(shuffled_word)

  return ' '.join(result_words)

text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(typoglycemia(text))
