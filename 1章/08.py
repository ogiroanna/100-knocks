def cipher(text):
  encrypted = ''
  for char in text:
    code = ord(char)
    if 97 <= code <= 122:
      new_code = 219 - code
      encrypted += chr(new_code)
    else:
      encrypted += char
  return encrypted


message = 'I am an NLPer '
enc = cipher(message)
dec = cipher(enc)

print('元の文:', message)
print('暗号化:', enc)
print('復号化:', dec)
