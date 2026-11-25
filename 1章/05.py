def get_ngram(sequence, n):
  result = []
  for i in range(len(sequence) - n + 1):
    result.append(sequence[i : i + n])
  return result

text = 'I am an NLPer'

char_trigram = get_ngram(text, 3)
print('文字tri-gram:', char_trigram)

words = text.split(' ')
word_bigram = get_ngram(words, 2)
print('単語bi-gram:', word_bigram)
