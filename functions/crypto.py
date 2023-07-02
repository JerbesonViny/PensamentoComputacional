def encrypt(text):
  encrypted = ''

  for word in text:
    if ord(word.lower()) >= 97 and ord(word.lower()) <= 101:
      encrypted += "1"
    
    elif ord(word.lower()) >= 102 and ord(word.lower()) <= 106:
      encrypted += "2"
    
    elif ord(word.lower()) >= 107 and ord(word.lower()) <= 111:
      encrypted += "3"
    
    elif ord(word.lower()) >= 112 and ord(word.lower()) <= 122:
      encrypted += "4"
    
    else:
      encrypted += "5"
  
  return encrypted

text = input("Digite o texto: ")

print(f'Encriptado: {encrypt(text)}')