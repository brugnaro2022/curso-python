PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')

textos = [
  'Joao gosta de futebol e politica',
  'A praia foi divertida'
]

for texto in textos:
  for palavra in texto.lower().split():
    if palavra in PALAVRAS_PROIBIDAS:
      print('Texto possui pelo menos uma palavra proibida: ', palavra)
      break
  else:
      print('Texto autorizado: ', texto)  
  